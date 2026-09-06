screen ok_popup(label = None, text = None, onOk="return", timer = None):
    modal True
    default timer_delay = timer if timer is not None else None
    default can_close = True if timer is None else False
    frame:
        style "frame_outer"
        xminimum 400
        xmaximum 1200
        align (0.5,0.5)
        vbox:
            xalign 0.5
            spacing 10
            if label is not None:
                label label:
                    style "say_label"
                    xalign 0.5
            if text is not None:
                text text:
                    style "say_dialogue"
                    text_align 0.5
            textbutton _("Ok"):
                style "confirm_button"
                xalign 0.5
                if can_close:
                    if onOk == "return":
                        action [Hide("ok_popup", transition = Dissolve(0.5)), Return()]
                    if onOk == "hide":
                        action Hide("ok_popup", transition = Dissolve(0.5))
                    keysym config.keymap["game_menu"] + ["K_RETURN", "K_y"]
    if timer_delay:
        timer timer_delay action SetLocalVariable("can_close", True)
