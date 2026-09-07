"""Unit tests for get_meta() filename parsing.

The warp service module imports `renpy` at the top level, which is only
available inside a Ren'Py runtime. To import it standalone, a minimal fake
`renpy` package is installed into sys.modules first.
"""

import importlib.util
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


def _run_get_meta(monkeypatch, warp_module, filename):
    """Call get_meta() as if the module file were named `filename`.

    For plain .rpe names, get_meta() reads the parent directory's name, so
    the fake path nests the filename as a directory with a .py file inside.
    """
    if filename.endswith(".rpe.py"):
        fake_path = Path("/game") / filename
    else:
        fake_path = Path("/game") / filename / "__init__.py"
    monkeypatch.setattr(warp_module, "__file__", str(fake_path))
    return warp_module.get_meta()


@pytest.mark.parametrize("filename,expected", [
    ("renpy_warp_3.5.0.rpe.py", ("3.5.0", None)),
    ("renpy_warp_3.5.0.rpe", ("3.5.0", None)),
    ("renpy_warp_3.5.0_22c4d2ff.rpe.py", ("3.5.0", "22c4d2ff")),
    ("renpy_warp_3.5.0_22c4d2ff.rpe", ("3.5.0", "22c4d2ff")),
    ("vscode_renpy_warp_3.5.0_22c4d2ff.rpe.py", ("3.5.0", "22c4d2ff")),
    ("vscode_renpy_warp_1.2.3.rpe.py", ("1.2.3", None)),
])
def test_valid_filenames(monkeypatch, warp_module, filename, expected):
    assert _run_get_meta(monkeypatch, warp_module, filename) == expected


@pytest.mark.parametrize("filename", [
    "renpy_warp.rpe.py",            # missing version
    "renpy_warp_ab.rpe.py",         # malformed version
    "renpy_warp_3.5.rpe.py",        # two-part version
    "some_other_file.rpe.py",       # unrelated name
    "renpy_warp_3.5.0.py",          # missing .rpe extension
])
def test_invalid_filenames_raise(monkeypatch, warp_module, filename):
    with pytest.raises(Exception, match="could not parse filename"):
        _run_get_meta(monkeypatch, warp_module, filename)
