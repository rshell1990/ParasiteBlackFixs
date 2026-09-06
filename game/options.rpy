###########################################
#### PRE-BUILD CHECKLIST:
# 1) fix all lint errors
#    optional: search for LINT_CHECK_LIST 
#    and enable more, then run lint
# 2) check that some random old saves load/work
#    (with DEBUG_BypassDevFixup set to True!)
# 3) run Renparse.exe, fix broken file paths if any
# 4) make sure all images are .webp
#    (and their corresponding file extension names in code)
#    it not mandatory but it saves *alot* of space long-term
# 5) make sure that SaveGameVersion is being set to this builds 
#    (even if no save update stuff was required)
#    serach for SAVE_UPDATE_ANCHOR in project
#    look *just above* it, in there, you'll see sth like: 
#    if SaveGameVersion == X: ... 
#       SaveGameVersion = Y
#    Y should be equal to config.version
# 6) change cheats (if needed)
#    scroll down to ch_enablecheatmenu 
#    no spaces, lower case
#    ALSO CHANGE CHEATS IN SUPPORTER PACK DLC! at Cheats.txt
# 7) make sure you dont have any stray changed files (on git)
#    commit/push any changes you made so far

###########################################
#### BUILD PROCEDURE:
# 1) "update old-game" in launcher->distributions
# 2) commit all newly changed files as "pre-build-X" 
# 3) input new build date (down below at configBuildDate)

# 4) generic build: Build_Kind = "nosteam", 
#    build with PC and Mac checkboxes, then do Android separately
# 5) Steam: Build_Kind = "steam", 
#    1 checkbox: "Windows, Mac Linux for Markets"
# 6) GOG: Build_Kind = "gog", 
#    build with PC and Mac checkboxes, do Android separately

# 7) check that at least 1 assembled build (like, pc-windows) runs/works
# 8) change config.version to +0.001 (AFTER doing all the builds)
# 9) add a pair of "if SaveGameVersion == old SaveGameVersion = new" 
#    at SAVE_UPDATE_ANCHOR (even if no save update is required!)
# 10) set Build_Kind to "nosteam" (its a default one we use on dev)
# 11) commit as "post-build-X" where X is the previous version
#     (the one you had just built)

#### ^ you don't need to do anything else per build besides that
#### IF YOU DO, ADD IT TO THE LIST

init python early:
    # valid values are: "steam", "nosteam", "gog"
    # "steam" and "gog" builds have no subscribestar 
    # and no "buy game" message spam
    Build_Kind = "nosteam" 

# increment by 0.001 once AFTER build
# (think of it like, "the version we are currently working on")
define config.version = "0.200"
# be a good person and punch in build date dd.mm.yyyy
define configBuildDate = "21.08.2026"

# cheats (supporter dlc cheats.txt needs a manual change!)
init python:
    ch_enablecheatmenu  = "imgoingonanadventure"
    ch_unlockallgallery = "titslaybeyondhere"
    ch_lockallgallery   = "begonetiddies"
##### build-related stuff over









##### stuff below is not build-related 
# (shouldnt be changed unless u know what u doing)
define config.steam_appid = 2174500     
define config.developer = "auto"

# Windows: %APPDATA\RenPy\<config.save_directory>, Mac: $HOME/Library/RenPy/<config.save_directory>, Linux: $HOME/.renpy/<config.save_directory>
# save_directory must not be set for crossplatform cloud saving to work (steam release)
define config.save_directory = "ParasiteBlack" if Build_Kind == "nosteam" else None 
define config.quicksave_slots = 6

define config.console = config.developer
define config.rollback_enabled = config.developer
default preferences.skip_unseen = config.developer

init python:
    Assert(Build_Kind == "steam" or Build_Kind == "nosteam" or Build_Kind == "gog", "Build_Kind can only be steam, nosteam or gog")
    if Build_Kind == "nosteam":
        config.quit_action = Show("SteamQuit")

    if config.developer:
        config.quit_action = Quit(confirm = False)

define config.layers = ["master",       # main layer for show, scene etc, used mostly for bgs/cgs
                        "scene_objects",# all the interactables (buttons) on a scene, houses, bridges etc, also battle chars
                        "vfx",          # visual effects over master & clickables
                        "characters",   # chars layer to avoid vfx overlap
                        "transient",    # renpy native, cleared after each interaction
                        "screens",      # all the screens use this one by default
                        "overlay"]      # used for ingame ui (corner panels)


define config.defer_tl_scripts = True   # this makes translation only load on lang change

define config.window_icon = "images/gui/logos/app_icon.webp"

default preferences.text_cps = 50 # chars per second
default preferences.afm_time = 15

define config.scene = ClearScene

define config.name = _("Parasite Black")
define build.name = "ParasiteBlack"

define config.allow_underfull_grids = True

define config.check_conflicting_properties = True

default persistent.save_naming = True
default persistent.first_time_language_selection = True