# This file managed by the Ren'Py Launch and Sync Visual Studio Code extension.
#
# This script provides a mechanism for your Ren'Py game to connect to VS Code
# via a websocket server. It is automatically excluded from builds of your game.
# You can delete this file if you do not want to use the features provided by
# the extension.
#
# This file should not be checked into source control. You can add it to your
# `.gitignore` file by adding the following line:
#
# vscode_renpy_warp_*.rpe*
#
# For more information, see https://github.com/furudean/vscode-renpy-warp
#

import renpy  # type: ignore
from time import sleep
import textwrap
import threading
import json
import functools
import re
import os
from pathlib import Path
import logging
from typing import Any, Callable, Iterator, Mapping, Optional, Protocol, Tuple

def _resolve_log_level():
    """Resolve WARP_LOGLEVEL to a logging level, defaulting to INFO."""
    value = os.getenv('WARP_LOGLEVEL')
    if not value:
        return logging.INFO
    level = logging.getLevelName(value.upper())
    return level if isinstance(level, int) else logging.INFO


logging.basicConfig()

logger = logging.getLogger("renpy_warp_service")

logger.setLevel(level=_resolve_log_level())


class WebsocketConnection(Protocol):
    """Minimal structural interface of a websockets sync connection."""

    def send(self, message: str) -> None: ...

    def close(self, code: int = 1000, reason: str = "") -> None: ...

    def __iter__(self) -> Iterator[str]: ...


class RenpyWarpQuitAction(renpy.ui.Action):
    def __call__(self):
        renpy.exports.quit()


original_quit_action = renpy.config.quit_action


def get_meta():
    RPE_FILE_PATTERN = re.compile(
        r"(?:vscode_)?renpy_warp_(?P<version>\d+\.\d+\.\d+)(?:_(?P<checksum>[a-z0-9]+))?\.rpe(?:\.py)?")

    file = Path(__file__) if __file__.endswith(
        '.rpe.py') else Path(__file__).parent

    filename = os.path.basename(file)
    match = RPE_FILE_PATTERN.match(filename)

    if not match:
        raise Exception(
            f"could not parse filename '{filename}'"
            f" with pattern '{RPE_FILE_PATTERN.pattern}'")

    d = match.groupdict()

    return d["version"], d["checksum"]


def py_exec(text):
    while renpy.exports.is_init_phase():
        logger.debug("in init phase, waiting...")
        sleep(0.2)

    fn = functools.partial(renpy.python.py_exec, text)
    renpy.exports.invoke_in_main_thread(fn)


def socket_send(message: Mapping[str, Any], websocket: WebsocketConnection) -> None:
    """sends a message to the socket server"""
    stringified = json.dumps(message)
    websocket.send(stringified)
    logger.debug(f"sent message: {stringified}")


def socket_listener(websocket: WebsocketConnection) -> None:
    """listens for messages from the socket server"""
    for message in websocket:
        logger.debug(f"receive message: {message}")

        try:
            payload = json.loads(message)
            payload_type = payload["type"]
        except (json.JSONDecodeError, KeyError, TypeError):
            logger.warning(f"malformed message received: {message!r}")
            continue

        try:
            if payload_type == "warp_to_line":
                file = payload["file"]
                line = payload["line"]

                py_exec(f"renpy.warp_to_line('{file}:{line}')")

            elif payload_type == "set_autoreload":
                script = textwrap.dedent("""
                    if renpy.get_autoreload() == False:
                        renpy.set_autoreload(True)
                        renpy.reload_script()
                """)
                py_exec(script)

            elif payload_type == "jump_to_label":
                label = payload["label"]

                script = textwrap.dedent(f"""
                    if renpy.context_nesting_level() > 0:
                        renpy.jump_out_of_context('{label}')
                    else:
                        renpy.jump('{label}')
                """)

                py_exec(script)

            else:
                logger.warning(f"unhandled message type '{payload_type}'")
        except KeyError as e:
            logger.warning(
                f"message of type '{payload_type}' missing required key {e}")


def socket_producer(websocket: WebsocketConnection) -> None:
    """produces messages to the socket server"""
    from websockets.exceptions import ConnectionClosed  # type: ignore

    send = functools.partial(socket_send, websocket=websocket)

    # report current line to warp server
    def fn(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "begin":
            try:
                filename, line = renpy.exports.get_filename_line()
                relative_filename = Path(filename).relative_to('game')
                filename_abs = Path(renpy.config.gamedir, relative_filename)

                message = {
                    "type": "current_line",
                    "line": line,
                    "path": filename_abs.resolve().as_posix(),
                    "relative_path": relative_filename.resolve().as_posix(),
                }
            except ValueError:
                # filename is not under the game dir, fall back to raw name
                logger.warning(
                    f"could not resolve script path '{filename}' relative to game dir")
                message = {
                    "type": "current_line",
                    "line": line,
                    "path": filename,
                    "relative_path": filename,
                }

            try:
                send(message)
            except Exception:  # noqa: BLE001 - any failure means the socket is unusable
                # socket is closed or broken, remove the callback
                logger.debug("producer send failed, removing callback", exc_info=True)
                if fn in renpy.config.all_character_callbacks:
                    renpy.config.all_character_callbacks.remove(fn)

    renpy.config.all_character_callbacks.append(fn)

    def label_callback(name, abnormal):
        try:
            send({"type": "current_label", "label": name})
        except Exception:  # noqa: BLE001 - any failure means the socket is unusable
            # socket is closed or broken, remove the callback
            logger.debug("label send failed, removing callback", exc_info=True)
            if label_callback in renpy.config.label_callbacks:
                renpy.config.label_callbacks.remove(label_callback)

    renpy.config.label_callbacks.append(label_callback)

    send({"type": "list_labels", "labels": list(renpy.exports.get_all_labels())})


def _build_headers(version: str, checksum: Optional[str]) -> dict:
    """Build the handshake headers sent to the warp socket server."""
    headers = {
        "pid": str(os.getpid()),
        "warp-project-root": Path(renpy.config.gamedir).parent.resolve().as_posix(),
        "warp-version": version,
        "warp-checksum": checksum,
    }

    if os.getenv("WARP_WS_NONCE"):
        headers["warp-nonce"] = os.getenv("WARP_WS_NONCE")

    return headers


def _register_quit_handlers(
    websocket: WebsocketConnection,
    port: int,
    on_quit: Callable[[], None],
) -> Callable[[], None]:
    """Register quit callback/action for the warp connection.

    Returns a cleanup callable that undoes the registration.
    """
    def renpy_warp_quit_callback():
        on_quit()
        logger.info(f"closing websocket connection :{port}")
        websocket.close(4000, 'renpy quit')

    renpy.config.quit_callbacks.append(renpy_warp_quit_callback)
    renpy.config.quit_action = RenpyWarpQuitAction()

    def cleanup() -> None:
        if renpy_warp_quit_callback in renpy.config.quit_callbacks:
            renpy.config.quit_callbacks.remove(renpy_warp_quit_callback)
        renpy.config.quit_action = original_quit_action

    return cleanup


def socket_service(port: int, version: str, checksum: Optional[str]) -> bool:
    """connects to the socket server. returns True if the connection has completed its lifecycle"""
    # websockets module is bundled with renpy on versions >=8.2.0
    from websockets.sync.client import connect  # type: ignore
    from websockets.exceptions import (  # type: ignore
        WebSocketException,
        ConnectionClosedOK,
        ConnectionClosedError
    )

    logger.debug(f"try port {port}")

    try:
        headers = _build_headers(version, checksum)

        with connect(
            f"ws://localhost:{port}",
            additional_headers=headers,
            open_timeout=None,
            close_timeout=5,
        ) as websocket:
            quitting = False

            def set_quitting() -> None:
                nonlocal quitting
                quitting = True

            cleanup = _register_quit_handlers(websocket, port, set_quitting)

            try:
                logger.info(f"connected to renpy warp socket server on :{port}")
                py_exec("renpy.notify(\"Connected to Ren'Py Launch and Sync\")")

                socket_producer(websocket)
                socket_listener(websocket)  # this blocks until socket is closed
            finally:
                cleanup()

            logger.info(f"socket service on :{port} exited")

            if not quitting:
                py_exec(
                    "renpy.notify(\"Disconnected from  Ren'Py Launch and Sync\")")

    except ConnectionClosedOK:
        logger.info(f"socket service on :{port} was terminated by server")
        pass

    except ConnectionClosedError:
        logger.info("connection replaced, service exiting")
        return True

    except WebSocketException as e:
        logger.exception("unexpected websocket error", exc_info=e)

    except (ConnectionError, TimeoutError) as e:
        logger.debug(
            f"{e.__class__.__name__}: could not establish connection to socket server")

    return False


def try_socket_ports_forever() -> None:
    version, checksum = get_meta()
    service_closed = False

    while service_closed is False:
        for port in range(40111, 40121):
            service_closed = socket_service(
                port=port, version=version, checksum=checksum)

            if service_closed:
                break

        if service_closed:
            break

        logger.debug(
            "exhausted all ports, waiting 3 seconds before retrying")
        sleep(3)

    logger.info("service closed")


def start_renpy_warp_service():
    if renpy.config.developer:
        renpy_warp_thread = threading.Thread(
            target=try_socket_ports_forever, daemon=True)
        renpy_warp_thread.start()

        logger.info(
            "service thread started. periodically scanning ports for warp server")


def declassify():
    """
    removes `renpy_warp_*.rpe{.py}` from build

    on renpy 8.3 and later, this is automatically done by the renpy build system
    """

    classify = renpy.python.store_dicts["store.build"]["classify"]
    classify("game/renpy_warp_*.rpe", None)
    classify("game/renpy_warp_*.rpe.py", None)


renpy.game.post_init.append(declassify)
renpy.config.display_start_callbacks.append(start_renpy_warp_service)
