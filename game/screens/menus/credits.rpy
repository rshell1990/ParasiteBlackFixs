screen credits():
    tag menu
    modal True
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    add "images/gui/unsorted/black_under.webp"
    label _("Credits") style "menu_header"
    viewport:
        xoffset 10 # because scrollbar offsets the entire shit
        align (0.5, 0.5)
        xsize 1400
        ysize 800
        scrollbars "vertical"
        draggable True
        mousewheel True

        vbox:
            xalign 0.5
            xfill True
            label _("Damned Studios"):
                xalign 0.5
            null height 11
            for Category, WhoList in STR.CREDITS_TEAM.items():
                hbox:
                    xalign 0.5
                    xfill True
                    hbox:
                        xalign 1.0
                        xsize 620
                        label Category:
                            style "credits_label"
                    spacing 20
                    vbox:
                        xsize 640
                        xalign 0.0
                        for Entry in WhoList:
                            text Entry:
                                xalign 0.0
                                style "credits_text"
                                xsize 650

            null height 60
            label _("Ex-members / contractors"):
                xalign 0.5
            null height 11
            for Category2, WhoList2 in STR.CREDITS_EX.items():
                hbox:
                    xalign 0.5
                    xfill True
                    hbox:
                        xalign 1.0
                        xsize 620
                        label Category2 style "credits_label"
                    spacing 20
                    vbox:
                        xsize 640
                        xalign 0.0
                        for Entry in WhoList2:
                            text Entry:
                                xalign 0.0
                                style "credits_text"
                                xsize 650

    textbutton _("Return"):
        style "menu_return"
        action ShowMenu("main_menu")
        default_focus True
        if main_menu:
            keysym "K_ESCAPE"