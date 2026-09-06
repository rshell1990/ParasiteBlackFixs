screen menu_button():
    if gui_parts["menu_button"] and IsUIDisplayed():
        # dialogue history button
        if not IsPlayerInBattle() and not IsPlayerInBaratiGame() and ShowDialogueHistoryButton:
            add "images/gui/unsorted/line_panel.webp":
                anchor (1.0, 0.0)
                pos (1.19, 0.0)
            imagebutton:    # dialogue history button
                anchor (1.0, 0.0)
                pos (0.947, 0.0034)
                idle Transform("images/gui/top_right/hist_b.webp", size = gui.button_size)
                hover Transform("images/gui/top_right/hist_h.webp", size = gui.button_size)
                hovered TooltipSetUI(GetHotkeyStr("dialogue_history", Parens = True, Space = True) + tra("Dialogue History"))
                if _history_list:
                    action ToggleScreen("dialogue_history", transition = Dissolve(0.15))
                selected_idle Transform("images/gui/top_right/hist_s.webp", size = gui.button_size)
                selected_hover Transform("images/gui/top_right/hist_s.webp", size = gui.button_size)
                if not renpy.get_screen("input"):
                    keysym config.keymap["dialogue_history"]
        add "images/gui/top_right/under.webp":
            anchor (1.0, 0.0)
            pos (1.0, 0.0)
        # main menu button
        imagebutton:
            anchor (1.0,0.0)
            pos (0.995,0.015)
            idle Transform("images/gui/top_right/menu_b.webp", size = gui.button_size)
            hover Transform("images/gui/top_right/menu_h.webp", size = gui.button_size)
            hovered TooltipSetUI(tra("Main Menu"))
            action ShowMenu("main_menu")
