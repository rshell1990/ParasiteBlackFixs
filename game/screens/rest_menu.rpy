default rest_menu_wait_hours = 1

screen rest_menu():
    modal True

    key "w" action SetVariable("rest_menu_wait_hours", 24)
    key "s" action SetVariable("rest_menu_wait_hours", 1)
    key "a" action SetVariable("rest_menu_wait_hours", max(1, min(rest_menu_wait_hours - 1, 24)))
    key "d" action SetVariable("rest_menu_wait_hours", max(1, min(rest_menu_wait_hours + 1, 24)))
    on "show" action [TooltipClearUI(), SetVariable("rest_menu_wait_hours", max(1, min(rest_menu_wait_hours, 24)))]

    add "images/gui/unsorted/black_under.webp"
    use outer_frame(y_size = 465, padd_top = 30, padd_left = 96, padd_right = 96, XStretch = True):
        vbox:
            ypos 0.1
            xalign 0.5
            spacing 10

            text _("%s, %s %s %s, %i\n%s.\n%s %s.") % (tra(STR_TIME.WEEKDAYS[GetCurWeekday()]), getOrdinalSuffix(Time_DateFromDays(GetGameDay()).day), tra(_(" of")), tra(rpDate_months[Time_DateFromDays(GetGameDay()).monthIdx][1]), Time_GetCurDate().year, tra(Time_GUI_GetTimeOfDayName()), tra(_("You are currently in")), PlayerPos.getName()):
                text_align .5
                xalign 0.5
            add "images/gui/unsorted/splitter_line.webp":
                xalign 0.5
                xsize 600
                ysize 20
            if rest_menu_wait_hours == 1:
                text "%s %s %s" % (tra(_("You can wait for")), rest_menu_wait_hours, tra(_("hour"))):
                    xalign 0.5
            else:
                text "%s %s %s" % (tra(_("You can wait for")), rest_menu_wait_hours, tra(_("hours"))):
                    xalign 0.5
            bar:
                xalign 0.5
                value VariableValue("rest_menu_wait_hours", 23, style = "slider", offset = 1, step = 1)
                range 24
                xsize 600
            hbox:
                xalign 0.5
                spacing 5
                textbutton _("Wait (e)"):
                    style "confirm_button"
                    keysym ["K_RETURN", "K_e"]
                    action [Hide("rest_menu", transition = dissolve), Jump("wait")]
                textbutton _("Cancel (t)"):
                    style "confirm_button"
                    action Hide("rest_menu", transition = Dissolve(0.15))
                    keysym config.keymap["gui_rest_menu"]
                textbutton _("Rest"):
                    style "confirm_button"