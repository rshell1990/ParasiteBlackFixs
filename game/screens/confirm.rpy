screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    add "images/gui/unsorted/black_under.webp"
    frame:
        style "frame_outer"
        align (0.5,0.5)
        vbox:
            spacing 30
            text _(message):
                text_align 0.5
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 50
                textbutton _("Yes"):
                    style "confirm_button"
                    action yes_action
                    keysym ["K_y", "K_RETURN"]
                textbutton _("No"):
                    style "confirm_button"
                    action no_action
                    keysym ["K_ESCAPE"]
    key "game_menu" action no_action
    