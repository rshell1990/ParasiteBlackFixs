##################################
default UI_PartyCharsExtend = False # <- adds offset to notifications if True

screen party_panel():
    if (gui_parts["party_panel"]
        and not IsPlayerInBattle() 
        and not IsPlayerInBaratiGame()
        and IsUIDisplayed()):
        if UI_PartyCharsExtend:
            frame:
                anchor (1.0, 1.0)
                pos (1.0, 1.0)
                if GetPartySize() < 3:
                    xoffset (3 - GetPartySize()) * 100 + 60
                else:
                    xoffset 60
                yoffset 45
                padding (72, 60, 72, 60)
                style "frame_outer_smaller"
                vpgrid:
                    cols 3
                    spacing 5
                    align (1.0, 1.0)
                    for CharID in player_party:
                        vbox:
                            align (0.5, 0.5)
                            fixed:
                                xysize (96, 96)
                                add "images/gui/unsorted/portrait_background.webp" align (0.5, 0.5)
                                imagebutton:
                                    align (0.5, 0.5)
                                    idle Transform(worldChars[CharID]["portrait"], size = (80, 80), xzoom = -1.0)
                                    hover Transform(worldChars[CharID]["portrait"], size = (80, 80), matrixcolor = BrightnessMatrix(0.1), xzoom = -1.0)
                                    if StoryCharIsPoisoned(CharID):
                                        hovered TooltipSetUI(worldChars[CharID]["name"] + _(" (Poisoned! ") + str(StoryStatusEffects[CharID]["Poison"]) + _(" hours)"))
                                    else:
                                        hovered TooltipSetUI(worldChars[CharID]["name"])
                                    unhovered TooltipClearUI()
                                    action Show("inventory", transition = Dissolve(0.15), charID = CharID)
                            bar:
                                if StoryCharIsPoisoned(CharID):
                                    style "bar_brgreen_256"
                                else:
                                    style "bar_red_256"
                                ysize 17
                                xsize 100
                                xalign 0.5
                                value worldChars[CharID]["Health"]
                                range worldChars[CharID]["HealthMax"]

        imagebutton:
            anchor (0.5, 0.5)
            pos (0.755, 0.975)
            idle Transform("images/gui/top_left/party_extend_button.webp", size = (52, 52), matrixcolor = IdentityMatrix())
            hover Transform("images/gui/top_left/party_extend_button.webp", size = (52, 52), matrixcolor = BrightnessMatrix(0.1))
            selected_idle Transform("images/gui/top_left/party_extend_button.webp", xzoom = -1.0, size = (52, 52), matrixcolor = IdentityMatrix())
            selected_hover Transform("images/gui/top_left/party_extend_button.webp", xzoom = -1.0, size = (52, 52), matrixcolor = BrightnessMatrix(0.1))
            selected UI_PartyCharsExtend
            if UI_PartyCharsExtend:
                hovered TooltipSetUI(_("Hide party characters"))
                action [TooltipSetUI(_("Show party characters")), SetVariable("UI_PartyCharsExtend", False), With(Dissolve(0.15))]
            else:
                hovered TooltipSetUI(_("Show party characters"))
                action [TooltipSetUI(_("Hide party characters")), SetVariable("UI_PartyCharsExtend", True), With(Dissolve(0.15))]
                if [ Char_ID for Char_ID in player_party if worldChars[Char_ID]["Health"] / worldChars[Char_ID]["HealthMax"] < 0.6]:
                    at red_eye_catching_flash
            unhovered TooltipClearUI()

transform red_eye_catching_flash:
    matrixcolor TintMatrix("#ffffff00")
    linear 1.5:
        matrixcolor TintMatrix("#ff0000ff")
    linear 1.5:
        matrixcolor TintMatrix("#ffffff00")
    repeat
