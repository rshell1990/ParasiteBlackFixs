screen access_buttons(): # a row of buttons to access various screens
    # the row
    if gui_parts["access_buttons"] and not IsPlayerInBattle() and not IsPlayerInBaratiGame() and IsUIDisplayed():
        add "images/gui/access_panel/under.webp":
            anchor (0.5, 1.0)
            pos (0.5, 1.0)
        hbox:
            anchor (0.5, 1.0)
            pos (0.5, 1.0)

            if gui_parts["world_map"] and len(seenWMapLocTags) > 1:
                # in travel mode, we will first show the travel path map, 
                # which will have "world map" tab-out
                imagebutton:
                    idle Transform("images/gui/access_panel/map_b.webp", size = gui.button_size)
                    hover Transform("images/gui/access_panel/map_h.webp", size = gui.button_size)
                    hovered TooltipSetUI(tra(_("Map (%s)")) % GetHotkeyStr("map", Parens = False, Space = False))
                    if TravelState is None:
                        action ToggleScreen("map", Context = Travel_GetMapContext(), transition = Dissolve(0.15))
                    else:
                        action ToggleScreen("map", OpenTab = "travel", Context = "travel_player", RouteID = TravelState.RouteID, transition = Dissolve(0.15))
                    selected_idle Transform("images/gui/access_panel/map_s.webp", size = gui.button_size)
                    selected_hover Transform("images/gui/access_panel/map_s.webp", size = gui.button_size)
                    if not renpy.get_screen("input"):
                        keysym config.keymap["map"]

            if gui_parts["relations"]:
                imagebutton:
                    idle Transform("images/gui/access_panel/rel_b.webp", size = gui.button_size)
                    hover Transform("images/gui/access_panel/rel_h.webp", size = gui.button_size)
                    hovered TooltipSetUI(tra(_("Relationships (%s)")) % GetHotkeyStr("relations", Parens = False, Space = False))
                    action ToggleScreen("relations", transition = Dissolve(0.15))
                    selected_idle Transform("images/gui/access_panel/rel_s.webp", size = gui.button_size)
                    selected_hover Transform("images/gui/access_panel/rel_s.webp", size = gui.button_size)
                    if not renpy.get_screen("input"):
                        keysym config.keymap["relations"]

            if gui_parts["journal"]:
                imagebutton:
                    idle Transform("images/gui/access_panel/jrn_b.webp", size = gui.button_size)
                    hover Transform("images/gui/access_panel/jrn_h.webp", size = gui.button_size)
                    hovered TooltipSetUI(tra(_("Journal (%s)")) % GetHotkeyStr("journal", Parens = False, Space = False))
                    action ToggleScreen("journal", transition = Dissolve(0.15))
                    selected_idle Transform("images/gui/access_panel/jrn_s.webp", size = gui.button_size)
                    selected_hover Transform("images/gui/access_panel/jrn_s.webp", size = gui.button_size)
                    if not renpy.get_screen("input"):
                        keysym config.keymap["journal"]

            if gui_parts["inventory"]:
                imagebutton:
                    idle Transform("images/gui/access_panel/inv_b.webp", size = gui.button_size)
                    hover Transform("images/gui/access_panel/inv_h.webp", size = gui.button_size)
                    hovered TooltipSetUI(tra(_("Inventory (%s)")) % GetHotkeyStr("inventory", Parens = False, Space = False))
                    selected_idle Transform("images/gui/access_panel/inv_s.webp", size = gui.button_size)
                    selected_hover Transform("images/gui/access_panel/inv_s.webp", size = gui.button_size)
                    if not renpy.get_screen("input"):
                        keysym config.keymap["inventory"]

                    action ToggleScreen("inventory", transition = Dissolve(0.15))

            if gui_parts["characters"]:
                fixed:
                    xysize (64, 64)
                    imagebutton:
                        idle Transform("images/gui/access_panel/char_b.webp", size = gui.button_size)
                        hover Transform("images/gui/access_panel/char_h.webp", size = gui.button_size)
                        hovered TooltipSetUI(tra(_("Characters (%s)")) % GetHotkeyStr("characters", Parens = False, Space = False))
                        selected_idle Transform("images/gui/access_panel/char_s.webp", size = gui.button_size)
                        selected_hover Transform("images/gui/access_panel/char_s.webp", size = gui.button_size)
                        if not renpy.get_screen("input"):
                            keysym config.keymap["characters"]
                        action Show("characters", transition = Dissolve(0.15))

                        if not renpy.showing("characters", "screens") and [Char_ID for Char_ID in player_party if worldChars[Char_ID]["lvlPoints"] > 0 or len(GetNextPerkBunch()) > 0 or worldChars[Char_ID]["skillPoints"] > 0 or (worldChars[Char_ID]["HasAltForm"] and worldChars[Char_ID]["AltForm_SkillPoints"] > 0)]:
                            at eye_catching_flash

    # auto-forward button
    if gui_parts["access_buttons"] and not IsPlayerInBattle() and not IsPlayerInBaratiGame() and IsUIDisplayed():
        imagebutton:
            anchor (0.5, 0.5)
            pos (0.245, 0.975)
            idle Transform("images/gui/access_panel/auto_forward_button.webp", size = (52, 52), matrixcolor = IdentityMatrix())
            hover Transform("images/gui/access_panel/auto_forward_button.webp", size = (52, 52), matrixcolor = BrightnessMatrix(0.1))
            selected_idle Transform("images/gui/access_panel/auto_forward_button.webp", size = (52, 52), matrixcolor = BrightnessMatrix(0.2))
            selected_hover Transform("images/gui/access_panel/auto_forward_button.webp", size = (52, 52), matrixcolor = BrightnessMatrix(0.3))
            selected preferences.afm_enable
            if preferences.afm_enable:
                hovered TooltipSetUI(_("Disable auto-forward"))
                action [TooltipSetUI(_("Enable auto-forward")), Preference("auto-forward", "toggle")]
            else:
                hovered TooltipSetUI(_("Enable auto-forward"))
                action [TooltipSetUI(_("Disable auto-forward")), Preference("auto-forward", "toggle")]
            unhovered TooltipClearUI()

transform eye_catching_flash:
    matrixcolor BrightnessMatrix(0.0)
    linear 0.5:
        matrixcolor BrightnessMatrix(1.0)
    linear 0.5:
        matrixcolor BrightnessMatrix(0.0)
    repeat
