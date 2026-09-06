# an outside frame. used by many ui screens
screen outer_frame(x_size = 1600, y_size = 930, padd_top = 60, padd_left = 0, padd_right = 0, padd_bot = 0, align_point = (0.5, 0.4), XStretch = False):
    tag ingame_menu
    frame:
        style "frame_outer"
        padding (padd_left, padd_top, padd_right, padd_bot)
        align align_point
        if not XStretch:
            xsize x_size
        ysize y_size
        transclude

# important, do_return = True is for any screens that do some logic. ex: trading
# or, for screens that must "roll the narrative forward"
screen close_outside(screenname, do_return = False):
    imagebutton: # bottom
        xalign 0.5
        yalign 1.0
        xsize 1920
        ysize 115
        idle "images/gui/blank.webp"
        hover "images/gui/blank.webp"
        hovered TooltipSetUI(GetHotkeyStr("game_menu", Parens = True, Space = True) + tra(_("Close screen")))
        unhovered TooltipClearUI()
        keyboard_focus False
        if do_return:
            action [Hide(screenname, transition = Dissolve(0.15)), Return()]
        else:
            action Hide(screenname, transition = Dissolve(0.15))

        if screenname in config.keymap:
            keysym config.keymap[screenname] + ["game_menu"]
        else:
            keysym "game_menu"

    imagebutton: # top
        xalign 0.5
        yalign 0.0
        xsize 1920
        ysize 90
        idle "images/gui/blank.webp"
        hover "images/gui/blank.webp"
        hovered TooltipSetUI(GetHotkeyStr("game_menu", Parens = True, Space = True) + tra(_("Close screen")))
        unhovered TooltipClearUI()
        keyboard_focus False
        if do_return:
            action [Hide(screenname, transition = Dissolve(0.15)), Return()]
        else:
            action Hide(screenname, transition = Dissolve(0.15))

    imagebutton: # left
        xalign 0.0
        yalign 0.5
        xsize 190
        ysize 1080
        idle "images/gui/blank.webp"
        hover "images/gui/blank.webp"
        hovered TooltipSetUI(GetHotkeyStr("game_menu", Parens = True, Space = True) + tra(_("Close screen")))
        unhovered TooltipClearUI()
        keyboard_focus False
        if do_return:
            action [Hide(screenname, transition = Dissolve(0.15)), Return()]
        else:
            action Hide(screenname, transition = Dissolve(0.15))

    imagebutton: # right
        xalign 1.0
        yalign 0.5
        xsize 190
        ysize 1080
        idle "images/gui/blank.webp"
        hover "images/gui/blank.webp"
        hovered TooltipSetUI(GetHotkeyStr("game_menu", Parens = True, Space = True) + tra(_("Close screen")))
        unhovered TooltipClearUI()
        keyboard_focus False
        if do_return:
            action [Hide(screenname, transition = Dissolve(0.15)), Return()]
        else:
            action Hide(screenname, transition = Dissolve(0.15))

    transclude

    on "hide" action TooltipClearUI()
