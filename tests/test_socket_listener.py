"""Unit tests for socket_listener() message dispatch.

Uses the same fake `renpy` package trick as test_get_meta.py to import the
warp service module outside a Ren'Py runtime, and stubs out py_exec() to
capture the script text that would be executed.
"""

import importlib.util
import json
import sys
import types
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).resolve().parent.parent / "game" / "libs" / \
    "vscode_renpy_warp_3.5.0_22c4d2ff.rpe.py"


def _install_fake_renpy() -> None:
    """Create just enough of the renpy API for the module to import."""
    if "renpy" in sys.modules:
        return

    renpy = types.ModuleType("renpy")

    ui = types.ModuleType("renpy.ui")
    ui.Action = type("Action", (), {})

    config = types.ModuleType("renpy.config")
    config.quit_action = None
    config.display_start_callbacks = []
    config.all_character_callbacks = []
    config.label_callbacks = []
    config.interact_callbacks = []
    config.developer = True
    config.gamedir = ""

    exports = types.ModuleType("renpy.exports")
    exports.is_init_phase = lambda: False
    exports.invoke_in_main_thread = lambda fn: None

    python = types.ModuleType("renpy.python")
    python.py_exec = lambda text: None
    python.store_dicts = {"store.build": {"classify": lambda *a: None}}

    game = types.ModuleType("renpy.game")
    game.post_init = []

    for name, mod in [("ui", ui), ("config", config), ("exports", exports),
                      ("python", python), ("game", game)]:
        renpy.__dict__[name] = mod
        sys.modules[f"renpy.{name}"] = mod

    sys.modules["renpy"] = renpy


def _load_module():
    _install_fake_renpy()
    spec = importlib.util.spec_from_file_location(
        "vscode_renpy_warp_test", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def warp_module():
    return _load_module()


class FakeWebsocket:
    """Iterates over a fixed list of messages."""

    def __init__(self, messages):
        self._messages = messages

    def __iter__(self):
        return iter(self._messages)


@pytest.fixture
def executed_scripts(monkeypatch, warp_module):
    """Stub py_exec to record executed script text; returns the record list."""
    scripts = []
    monkeypatch.setattr(
        warp_module, "py_exec", lambda text: scripts.append(text))
    return scripts


def test_warp_to_line_builds_expected_script(warp_module, executed_scripts):
    messages = [json.dumps({"type": "warp_to_line", "file": "script.rpy",
                            "line": 42})]
    warp_module.socket_listener(FakeWebsocket(messages))

    assert executed_scripts == ["renpy.warp_to_line('script.rpy:42')"]


def test_set_autoreload_builds_expected_script(warp_module, executed_scripts):
    messages = [json.dumps({"type": "set_autoreload"})]
    warp_module.socket_listener(FakeWebsocket(messages))

    assert len(executed_scripts) == 1
    assert "renpy.set_autoreload(True)" in executed_scripts[0]
    assert "renpy.reload_script()" in executed_scripts[0]


def test_jump_to_label_builds_expected_script(warp_module, executed_scripts):
    messages = [json.dumps({"type": "jump_to_label", "label": "start"})]
    warp_module.socket_listener(FakeWebsocket(messages))

    assert len(executed_scripts) == 1
    assert "renpy.jump('start')" in executed_scripts[0]
    assert "renpy.jump_out_of_context('start')" in executed_scripts[0]


def test_unhandled_message_type_is_ignored(warp_module, executed_scripts,
                                           caplog):
    messages = [json.dumps({"type": "something_else"})]
    warp_module.socket_listener(FakeWebsocket(messages))

    assert executed_scripts == []
    assert any("unhandled message type 'something_else'" in r.message
               for r in caplog.records)


def test_malformed_json_does_not_crash(warp_module, executed_scripts, caplog):
    messages = ["not valid json at all"]
    warp_module.socket_listener(FakeWebsocket(messages))

    assert executed_scripts == []
    assert any("malformed message" in r.message for r in caplog.records)


def test_missing_keys_do_not_crash(warp_module, executed_scripts, caplog):
    messages = [
        json.dumps({"type": "warp_to_line"}),   # missing file and line
        json.dumps({"type": "jump_to_label"}),  # missing label
        json.dumps([1, 2, 3]),                  # not an object
    ]
    warp_module.socket_listener(FakeWebsocket(messages))

    assert executed_scripts == []
    assert any("malformed message" in r.message for r in caplog.records)
    assert any("missing required key" in r.message for r in caplog.records)


def test_subsequent_valid_message_processed_after_bad_one(
        warp_module, executed_scripts):
    messages = [
        "garbage",
        json.dumps({"type": "warp_to_line", "file": "a.rpy", "line": 1}),
    ]
    warp_module.socket_listener(FakeWebsocket(messages))

    assert executed_scripts == ["renpy.warp_to_line('a.rpy:1')"]
