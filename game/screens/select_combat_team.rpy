screen select_combat_team(MaximumCharsForTeam = 4, RightBeforeBattle = False):
    on "show" action SetVariable("block_wait_dynamic", True)
    on "hide" action SetVariable("block_wait_dynamic", False)
    tag ingame_menu
    modal True
    default NewPlayerTeam = set(PlayerCombatTeam)

    use outer_frame():
        vbox:
            spacing 20
            xalign 0.5

            label _("Select characters for battle") xalign 0.5

            hbox:
                spacing 100
                xalign 0.5

                hbox:
                    spacing 20
                    label _("Maximum:") yalign 0.5 text_size 30
                    text str(MaximumCharsForTeam) yalign 0.5 yoffset -1

                hbox:
                    spacing 20
                    label _("Selected:") yalign 0.5 text_size 30
                    text str(len(NewPlayerTeam)) yalign 0.5 yoffset -1

            vpgrid:
                cols 4
                spacing 20

                for idx, char_ID in enumerate(player_party):
                    vbox:
                        fixed:
                            xysize (256, 256)

                            imagebutton:
                                align (0.5, 0.5)
                                xysize (230, 230)
                                idle Frame(worldChars[char_ID]["portrait"])
                                hover Frame(Transform(worldChars[char_ID]["portrait"], matrixcolor = BrightnessMatrix(0.15)))
                                if char_ID in NewPlayerTeam:
                                    if char_ID != "mc":
                                        action RemoveFromSet(NewPlayerTeam, char_ID)
                                elif len(NewPlayerTeam) < MaximumCharsForTeam:
                                    action AddToSet(NewPlayerTeam, char_ID)

                            if char_ID in NewPlayerTeam:
                                label _("SELECTED") align (0.5, 0.86) text_outlines [ (1,"#000000") ]

                            add "images/gui/unsorted/gallery_frame.webp"

                    
                        vbox:
                            align (0.5, 0.5)
                            # health bar, curr/max
                            bar:
                                
                                if StoryCharIsPoisoned(char_ID):
                                    style "bar_brgreen_256"
                                else:
                                    style "bar_red_256"
                                xalign 0.5
                                value AnimatedValue(worldChars[char_ID]["Health"], worldChars[char_ID]["HealthMax"], delay = 0.15)
                            # EP OR mana bar, curr/max
                            bar: 
                                
                                xalign 0.5
                                if worldChars[char_ID]["is_mage"]:
                                    value AnimatedValue(worldChars[char_ID]["Mana"], worldChars[char_ID]["ManaMax"], delay = 0.15)
                                else:
                                    style "bar_green_256"
                                    value AnimatedValue(worldChars[char_ID]["Energy"], worldChars[char_ID]["EnergyMax"], delay = 0.15)
                    

                        label worldChars[char_ID]["name"] xalign 0.5 text_size 25


            if RightBeforeBattle:
                textbutton _("(Space) Continue"):
                    xalign 0.5
                    keysym ["K_SPACE", config.keymap["skip"][0], "repeat_" + config.keymap["skip"][0]]
                    sensitive len(NewPlayerTeam)
                    if len(NewPlayerTeam) <= MaximumCharsForTeam:
                        action [SetVariable("PlayerCombatTeam", list(NewPlayerTeam)), Return()]
            else:
                hbox:
                    xalign 0.5
                    spacing 50

                    textbutton _("Cancel"):
                        keysym "game_menu"
                        action Show("characters")

                    textbutton _("Confirm"):
                        keysym [ "K_RETURN", "K_KP_ENTER" ]
                        sensitive len(NewPlayerTeam)
                        action [ SetVariable("PlayerCombatTeam", list(NewPlayerTeam)), Show("characters") ]
