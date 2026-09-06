screen steam_window(_pos = (1.0, 1.0)):
    frame:
        style "frame_trans"
        anchor (1.0, 1.0)
        pos _pos
        xoffset 9
        yoffset 9
        padding (25, 25)
        vbox:
            align (0.5, 0.5)
            spacing 10

            add "images/gui/steam/logo_steam.webp" xalign 0.5

            text _("Parasite Black is now on steam!"):
            
                size 28
                color "#FFFFFF"
                xalign 0.5
                yalign 0.5
                outlines [ (2, "#000000", 0, 0) ]

            frame:
                align (0.5, 0.5)
                imagebutton:
                    idle Transform("images/gui/steam/header.webp", matrixcolor = TintMatrix((255, 255, 255)), zoom = 0.9)
                    hover Transform("images/gui/steam/header.webp", matrixcolor = TintMatrix((148, 148, 148)), zoom = 0.9)
                    action OpenURL("https://store.steampowered.com/app/2174500?utm_source=Ingamelink")

screen SteamQuit():
    modal True
    zorder 200

    add "images/gui/unsorted/black_under.webp"
    frame:
        style "frame_outer"
        align (0.5,0.5)
        vbox:
            spacing 30
            use steam_window((0.983, 1.0))
            text _("Are you sure you want to leave?"):
                text_align 0.5
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 50
                textbutton _("Yes"):
                    style "confirm_button"
                    action Quit(False)
                textbutton _("No"):
                    style "confirm_button"
                    action Hide("SteamQuit")
    key "game_menu" action Hide("SteamQuit")