init python:
    gui.init(1920, 1080)
### transitions (this is messy and barely used, we often directly set the transition actually)
define transition_default            = Dissolve(0.15)
define transition_move_between_locs  = Dissolve(0.25)
define transition_popup              = Dissolve(0.15)
define config.enter_transition       = Dissolve(0.25)  # game menu from in-game
define config.exit_transition        = Dissolve(0.25)  # back to game from in-game menu, doesnt work 4 new game :<
define config.enter_yesno_transition = Dissolve(0.25)  # confirm screen? I guess
define config.exit_yesno_transition  = Dissolve(0.25)  # same as above
define config.game_main_transition   = Dissolve(0.25)  # when using MainMenu()
define config.intra_transition       = Dissolve(0.25)  # when using ShowMenu()
define config.after_load_transition  = Fade(0.25, 0.0, 0.5) # post-load
define config.end_game_transition    = Fade(0.25, 0.0, 0.5) # on quit
define config.end_splash_transition  = Dissolve(0.5)   # post-splash
define config.window_hide_transition = None            # on say() hide
define config.window_show_transition = Dissolve(0.25)  # on say() show
define config.window = "hide"                           # default say window state

######## sizes for battle & inventory
define gui.general_icon_size = (80, 80)
define gui.inventory_stored_item_size = (104, 104)
define gui.general_icon_size_lower = (67, 67)
#########
define config.mouse = {
    "default":  [("images/gui/cursor/default.webp", 0, 0)],
    "hover":    [("images/gui/cursor/glow.webp",    0, 0)]}


default hide_ui = False
default gui_parts = {
    "location_name":False,
    "notifications":True,
    "time_tracker": False,
    "menu_button":  True,
    "party_panel":  False,
    "access_buttons":False,
    "world_map":    False,
    "relations":    False,
    "journal":      False,
    "inventory":    False,
    "characters":   False}

define gui.button_size = (64.0, 64.0) # *mostly* access button sizes

# appending ingame ui parts to renpy overlay thingy
init python:
    config.overlay_screens.append("access_buttons")
    config.overlay_screens.append("location_name")
    config.overlay_screens.append("time_tracker")
    config.overlay_screens.append("party_panel")
    config.overlay_screens.append("infection_bar")
    config.overlay_screens.append("menu_button")
    config.overlay_screens.append("dev_menu_button")
    config.overlay_screens.append("cheat_menu_button")

    config.always_shown_screens.append("tooltip")

    # use to temporarily hide all ui
    def HideUI(TrueOrFalse):
        store.hide_ui = TrueOrFalse
        return

    def IsUIDisplayed():
        return (not store.hide_ui)
    
    # this is FOR DISPLAY to display shiut like (z) or (Esc), DONT USE FOR ACTUAL LOGIC
    def GetHotkeyStr(key_id, Parens = False, Space = False):
        HotkeyString = config.keymap[key_id][0]
        if config.keymap[key_id][0] == "K_ESCAPE":
            HotkeyString = _("Esc")
        elif HotkeyString.startswith("K_") and len(HotkeyString) == 3:
            HotkeyString = HotkeyString.strip("K_")
        CondSpace = ""
        if Space:
            CondSpace = " "
        if Parens == True:
            return "(" + HotkeyString + ")" + CondSpace
        else:
            return HotkeyString + CondSpace
        

default _game_menu_screen = "main_menu"

define config.history_length = 60

define config.thumbnail_width =     384 # 20% of 1920/1080
define config.thumbnail_height =    216

define gui.game_menu_background = Transform("images/gui/menu_bg_ingame.webp", matrixcolor = OpacityMatrix(0.85))
define gui.main_menu_background = Movie(start_image = "images/gui/menu_movie_start.webp", play = "video/menu.webm")