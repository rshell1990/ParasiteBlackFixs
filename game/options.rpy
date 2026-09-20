###########################################
#### PRE-BUILD CHECKLIST:
# 1) Fix all lint errors
#    Optional: search for LINT_CHECK_LIST 
#    and enable more, then run lint
# 2) Check that random old saves load/work
#    (with DEBUG_BypassDevFixup set to True!)
# 3) Run Renparse.exe, fix broken file paths if any
# 4) Make sure all images are .webp
#    (and their corresponding file extension names in code)
#    It's not mandatory, but saves a lot of space long-term
# 5) Make sure that SaveGameVersion is set to this build 
#    (even if no save update stuff was required)
#    Search for SAVE_UPDATE_ANCHOR in project
#    Look just above it; you'll see something like: 
#    if SaveGameVersion == X: ... 
#       SaveGameVersion = Y
#    Y should be equal to config.version
# 6) Change cheats (if needed)
#    Scroll down to ch_enablecheatmenu 
#    no spaces, lower case
#    ALSO CHANGE CHEATS IN SUPPORTER PACK DLC at Cheats.txt
# 7) Make sure you don't have any stray changed files (on git)
#    Commit/push any changes you made so far

###########################################
#### BUILD PROCEDURE:
# 1) "Update old-game" in launcher -> distributions
# 2) Commit all newly changed files as "pre-build-X" 
# 3) Input new build date (down below at configBuildDate)

# 4) Generic build: Build_Kind = "nosteam", 
#    Build with PC and Mac checkboxes, then do Android separately
# 5) Steam: Build_Kind = "steam", 
#    1 checkbox: "Windows, Mac, Linux for Markets"
# 6) GOG: Build_Kind = "gog", 
#    Build with PC and Mac checkboxes, do Android separately

# 7) Check that at least 1 assembled build (e.g., PC/Windows) runs/works
# 8) Change config.version to +0.001 (AFTER doing all the builds)
# 9) Add a pair of "if SaveGameVersion == old: SaveGameVersion = new" 
#    at SAVE_UPDATE_ANCHOR (even if no save update is required!)
# 10) Set Build_Kind to "nosteam" (it's the default used in development)
# 11) Commit as "post-build-X" where X is the previous version
#     (the one you had just built)

#### You don't need to do anything else per build besides that.
#### IF YOU DO, ADD IT TO THE LIST

init python early:
    # Valid values: "steam", "nosteam", "gog"
    # "steam" and "gog" builds have no Subscribestar 
    # and no "buy game" message prompts
    Build_Kind = "nosteam" 

    # Validate build kind early
    assert Build_Kind in ("steam", "nosteam", "gog"), "Build_Kind must be 'steam', 'nosteam', or 'gog'"

# Increment by 0.001 once AFTER build
# ("the version currently in active development")
define config.version = "0.200"
# Build date dd.mm.yyyy
define configBuildDate = "21.08.2026"

# Cheats (supporter dlc cheats.txt needs a manual change!)
init python:
    ch_enablecheatmenu  = "imgoingonanadventure"
    ch_unlockallgallery = "titslaybeyondhere"
    ch_lockallgallery   = "begonetiddies"

##### BUILD-RELATED CONFIGURATION END #####


##### GENERAL GAME CONFIGURATION #####
define config.steam_appid = 2174500     
define config.developer = "auto"

# Windows: %APPDATA%\RenPy\<config.save_directory>
# Mac: $HOME/Library/RenPy/<config.save_directory>
# Linux: $HOME/.renpy/<config.save_directory>
# save_directory must be None on Steam release for cloud saving
define config.save_directory = "ParasiteBlack" if Build_Kind == "nosteam" else None 
define config.quicksave_slots = 6

define config.console = config.developer
define config.rollback_enabled = config.developer

init python:
    if config.developer:
        config.quit_action = Quit(confirm=False)
    elif Build_Kind == "nosteam":
        config.quit_action = Show("SteamQuit")

define config.layers = [
    "master",          # Main layer for show/scene background and graphics
    "scene_objects",   # Interactables (buttons), environmental objects, battle units
    "vfx",             # Visual effects over master & clickables
    "characters",      # Character layer to avoid VFX overlap
    "transient",       # Ren'Py native layer, cleared after interactions
    "screens",         # Standard screen display layer
    "overlay"          # Permanent in-game UI overlay panels
]

define config.defer_tl_scripts = True   # Defers translation script loads until language switch

define config.window_icon = "images/gui/logos/app_icon.webp"

default preferences.text_cps = 50
default preferences.afm_time = 15

define config.scene = ClearScene

define config.name = _("Parasite Black")
define build.name = "ParasiteBlack"

define config.allow_underfull_grids = True
define config.check_conflicting_properties = True

default persistent.save_naming = True
default persistent.first_time_language_selection = True