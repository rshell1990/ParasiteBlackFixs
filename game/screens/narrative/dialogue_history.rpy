screen dialogue_history():
    tag ingame_menu
    modal True
    predict False
    use close_outside("dialogue_history")
    use outer_frame(padd_top=45):
        vbox:
            yoffset 20
            spacing 10
            xalign 0.5
            label _("Dialogue History"):
                xalign 0.5
            frame:
                xsize 1400
                ysize 710
                viewport:
                    xalign 0.5
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    vbox:
                        spacing 5
                        for h in reversed(_history_list):
                            hbox:
                                spacing 10
                                if h.who:
                                    label "%s:" % h.who:
                                        style "credits_label"
                                        substitute False
                                    if h.what:
                                        text h.what:
                                            style "credits_text"
                                            substitute False
                                else:
                                    if h.what.startswith("NOTIF_"):
                                        text "{i}" + h.what.removeprefix("NOTIF_") + "{/i}":
                                            style "credits_text"
                                            substitute False
                                    else:
                                        text "{i}" + h.what + "{/i}":
                                            style "credits_text"
                                            substitute False
                        if not _history_list:
                            text _("The dialogue history is empty.")
                        
init python:
    def AddChoiceToHistory(i, _history_list):
        new_history_entry = renpy.character.HistoryEntry()
        new_history_entry.who = "{color=#c7644a}" + tra(_("Choice")) + "{/color}"
        new_history_entry.what = tra(i.caption)
        _history_list.append(new_history_entry)
