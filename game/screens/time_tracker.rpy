screen time_tracker():
    if gui_parts["time_tracker"] and not IsPlayerInBattle() and not IsPlayerInBaratiGame() and IsUIDisplayed():
        fixed:
            anchor (0.0, 0.0)
            pos (0.0, 0.0)
            if PlayerItemQty("gold") > 0:
                add "images/gui/unsorted/line_panel.webp":
                    anchor (0.0, 0.0)
                    pos (-0.1, 0.0)
                    xzoom -1.0
                add "images/gui/top_left/gold.webp":
                    anchor (0.0, 0.0)
                    pos (0.084, 0.007)
                    size (56, 56)
                fixed:
                    xmaximum 250
                    ymaximum 80
                    anchor (0.5, 0.5)
                    pos (0.144, 0.03)
                    text str(PlayerItemQty("gold")):
                        align (0.5, 0.5)
                        size 45
                        color "#f1c1b5"

            add "images/gui/top_left/time_circle.webp":
                anchor (0.5, 0.5)
                zoom 0.5
                pos (41, 41)
                rotate store.rpTime / 240-47
            if FreezeAutoTime:
                add "images/gui/top_left/over_closed.webp":
                    pos (-30, -30)
                    zoom 0.5
            else:
                add "images/gui/top_left/over.webp":
                    pos (-30, -30)
                    zoom 0.5

            # wait button
            imagebutton:
                pos (12, 12)
                if Time_GUI_CanPlayerWait():
                    if block_wait_dynamic == True:
                        idle Transform("images/gui/top_left/rest_b_gray.webp", size = gui.button_size)
                        hover Transform("images/gui/top_left/rest_b_gray.webp", size = gui.button_size)
                    else:
                        idle Transform("images/gui/top_left/rest_b.webp", size = gui.button_size)
                        hover Transform("images/gui/top_left/rest_h.webp", size = gui.button_size)

                    hovered TooltipSetUI("%s,\n%s, %s%s%s \n%s\n%s %s" % (
                        tra(Time_GUI_GetTimeOfDayName()), 
                        tra(STR_TIME.WEEKDAYS[GetCurWeekday()]), 
                        getOrdinalSuffix(Time_DateFromDays(GetGameDay()).day), 
                        tra(_(" of ")), 
                        tra(rpDate_months[Time_DateFromDays(GetGameDay()).monthIdx][1]), 
                        Time_GetCurDate().year, 
                        GetHotkeyStr("gui_rest_menu", Parens = True, Space = False),
                        tra(_("Wait / Rest"))))

                    if renpy.get_ongoing_transition() == None:
                        action ToggleScreen("rest_menu", transition = Dissolve(0.15))
                    else:
                        action NullAction()

                    selected_idle Transform("images/gui/top_left/rest_s.webp", size = gui.button_size)
                    selected_hover Transform("images/gui/top_left/rest_s.webp", size = gui.button_size)

                    keysym config.keymap["gui_rest_menu"]

                else:
                    idle Transform("images/gui/top_left/rest_b_gray.webp", size = gui.button_size)

                    hovered TooltipSetUI("%s,\n%s, %s%s%s \n%s\n%s" % (
                        tra(Time_GUI_GetTimeOfDayName()), 
                        tra(STR_TIME.WEEKDAYS[GetCurWeekday()]), 
                        getOrdinalSuffix(Time_DateFromDays(GetGameDay()).day), 
                        tra(_(" of ")), 
                        tra(rpDate_months[Time_DateFromDays(GetGameDay()).monthIdx][1]), 
                        Time_GetCurDate().year, 
                        tra(_("You cannot wait right now."))))

                    action NullAction()