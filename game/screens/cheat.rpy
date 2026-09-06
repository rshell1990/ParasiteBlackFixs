default cheat_menu_bool = False # off by default

screen cheat_menu():
    tag ingame_menu
    modal True

    use close_outside("cheat_menu")
    frame:
        align (0.5, 0.5)
        style "frame_outer"
        vbox:
            xalign 0.5
            label "Cheat menu":
                xalign 0.5

            null height 40
            if IsPlayerInBattle():
                textbutton _("Win battle"):
                    xalign 0.5
                    action [Function(Battle_Win), Hide("cheat_menu")]
                add "images/gui/unsorted/splitter_line.webp":
                    xalign 0.5
                    size (800, 30)
            else:
                text "{i}In battle, a button to instantly win will appear here.{/i}" xalign 0.5
                add "images/gui/unsorted/splitter_line.webp":
                    xalign 0.5
                    size (800, 30)

            hbox:
                xalign 0.5
                textbutton _("Set infection to 0"):
                    action Function(InfChangeBy, 0, SetTo = True)
            add "images/gui/unsorted/splitter_line.webp":
                xalign 0.5
                size (800, 30)

            hbox:
                xalign 0.5
                textbutton _("Nightly infection gain"):
                    action Function(InfGainDaily, not InfectionModule().DailyGain)
                    selected InfectionModule().DailyGain
                    style "button_sel"
            add "images/gui/unsorted/splitter_line.webp":
                xalign 0.5
                size (800, 30)

            hbox:
                xalign 0.5
                textbutton _("Naked party"):
                    action Function(CHEAT_NakedParty)
                textbutton _("Clothed party"):
                    action Function(CHEAT_NakedPartyUndo)
            add "images/gui/unsorted/splitter_line.webp":
                xalign 0.5
                size (800, 30)

            hbox:
                xalign 0.5
                textbutton _("Add all perks"):
                    action Function(DEBUG_AddAllPerks)
            add "images/gui/unsorted/splitter_line.webp":
                xalign 0.5
                size (800, 30)

            hbox:
                xalign 0.5
                textbutton "Get 3000 gold":
                    action Function(PlayerAddItem, ("gold"), 3000, using_cheat = True)
            null height 40
            
            hbox:
                xalign 0.5
                textbutton _("Close"):
                    action Hide("cheat_menu")

screen cheat_menu_button():
    if (cheat_menu_bool == True and IsUIDisplayed()) or DEBUG_ShowCheatMenu:
        imagebutton:
            anchor (1.0, 0.0)
            pos (0.9, 0.01)
            idle Transform("images/gui/top_right/dev_menu_b.webp", size = gui.button_size,matrixcolor = IdentityMatrix())
            hover Transform("images/gui/top_right/dev_menu_b.webp", size = gui.button_size,matrixcolor = MxMapHover())
            action ToggleScreen("cheat_menu")
            selected_idle Transform("images/gui/top_right/dev_menu_b.webp", size = gui.button_size, matrixcolor = MxMapHover())
            selected_hover Transform("images/gui/top_right/dev_menu_b.webp", size = gui.button_size , matrixcolor = MxMapHover())
            hovered TooltipSetUI(_("Cheat Menu"))
