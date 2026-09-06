screen options():
    tag menu
    modal True

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    add "images/gui/unsorted/black_under.webp"
    label _("Options") style "menu_header"
    hbox:
        spacing 25
        align (0.5, 0.45)
        vbox:
            style "pref_vbox"
            vbox:
                label _("Display") style "pref_cat_header"
                null height 5
                textbutton _("Fullscreen"):
                    style "pref_toggle"
                    action Preference("display", "toggle")

                if Build_Kind != "steam": 
                    textbutton _("Large fonts {color=#ff0000}(Experimental){/color}"):
                        style "pref_toggle"
                        hovered TooltipSetUI(_("If enabled, significantly increases the font size of texts.\n{color=#ffd000}WARNING:{/color} This is a {i}temporary solution{/i} for playing the game on smaller displays (phones). Some texts will overflow frames and borders."))
                        unhovered TooltipClearUI()
                        action [ToggleField(persistent, "large_font"), Function(_refresh_font), Function(style.rebuild)]

            null height 2
            vbox:
                label _("Gameplay") style "pref_cat_header"
                null height 1
                textbutton _("Difficulty: [DIFFICULTY.NAMES[CurrentDifficulty]]"):
                    style "pref_toggle"
                    action Show("difficulty_dropdown")

                if config.developer:
                    textbutton _("Developer menu"):
                        style "pref_toggle"
                        action Show("dropdown_example")

                textbutton _("Fast battle animations"):
                    style "pref_toggle"
                    hovered TooltipSetUI(_("If enabled, there will be very little delay between combat events, such as battle animations or turns.\nIt can speed up your gameplay, but can be a little confusing."))
                    unhovered TooltipClearUI()
                    action ToggleField(persistent, "BattlePref_FastLoop")

                textbutton _("Auto-fill combat team"):
                    style "pref_toggle"
                    hovered TooltipSetUI(_("If enabled, the game will automatically fill player combat team to capacity.\nYou will be prompted to adjust your battle party if necessary."))
                    unhovered TooltipClearUI()
                    action ToggleField(persistent, "BattlePref_AutoFillPlayerCombatTeam")
                
                textbutton _("Auto-battle by default"):
                    style "pref_toggle"
                    hovered TooltipSetUI(_("If enabled, the game will play out the battles automatically when available."))
                    unhovered TooltipClearUI()
                    action ToggleField(persistent, "BattlePref_AutoBattleByDefault")

                textbutton _("Auto-select during AI turns"):
                    style "pref_toggle"
                    hovered TooltipSetUI(_("If enabled, during AI turns the game will automatically select the actor and target.\nThis has no effect besides changing currently selected enemy/ally."))
                    unhovered TooltipClearUI()
                    action ToggleField(persistent, "Battle_AutoSelectActorAndTargetForAI")
                
                textbutton _("Auto-loot enemies after battle"):
                    style "pref_toggle"
                    hovered TooltipSetUI(_("If enabled, the battle loot screen will be skipped after battle, giving you all items automatically."))
                    unhovered TooltipClearUI()
                    action ToggleField(persistent, "BattlePref_AutoLootAll")

                textbutton _("Skip navigation input phase"):
                    style "pref_toggle"
                    hovered TooltipSetUI(_("If enabled, holding skip (by default, ctrl) will skip the 'hit space to proceed' phase of traveling in case you have a destination set."))
                    unhovered TooltipClearUI()
                    action ToggleField(persistent, "TravelPref_SkipMap")
        vbox:
            style "pref_vbox"
            label _("Narrative") style "pref_cat_header"
            null height 10
            button:
                xfill True
                hbox:
                    xalign 0.45
                    add "images/gui/buttons_loc/travel.webp" zoom 0.4 yalign 0.5
                    null width 6
                    text _("Language"):
                        style "button_text"
                        yalign 0.5
                action Show("LanguageSelection", transition = Dissolve(0.25))
            textbutton _("Skip Unseen Text"):
                style "pref_toggle"
                action Preference("skip", "toggle")
            textbutton _("Skip After Choices"):
                style "pref_toggle"
                action Preference("after choices", "toggle")
            textbutton _("Skip Transitions"):
                style "pref_toggle"
                action InvertSelected(Preference("transitions", "toggle"))
            textbutton _("Auto-Forward"):
                style "pref_toggle"
                action Preference("auto-forward", "toggle")
            null height 5
            if preferences.text_cps != 0:
                text tra(_("Text Speed (%s chars/sec)")) % int(preferences.text_cps)
            else:
                text _("Text Speed (Instant)")
            bar:
                style "pref_slider"
                value Preference("text speed")
            if preferences.afm_enable:
                text tra(_("Auto-Forward Delay (%s sec)")) % round(preferences.afm_time, 1)
                bar:
                    style "pref_slider"
                    value Preference("auto-forward time")
            null height 20
            vbox:
                label _("Tutorial messages") style "pref_cat_header"
                null height 10
                textbutton _("Reset all tutorial messages"):
                    style "pref_toggle"
                    hovered TooltipSetUI(_("This option will mark all tutorial messages as 'new', making them pop up contextually."))
                    unhovered TooltipClearUI()
                    action Function(UI_TutorialsSetAllToTrue)

                textbutton _("Disable all tutorial messages"):
                    style "pref_toggle"
                    hovered TooltipSetUI(_("This option will mark all tutorial messages as 'seen', effectively disabling all of them."))
                    unhovered TooltipClearUI()
                    action Function(UI_TutorialsSetAllToFalse)

        vbox:
            style "pref_vbox"
            label _("Volume") style "pref_cat_header"
            null height 10
            text _("Master Volume")
            bar:
                style "pref_slider"
                value Preference("main volume")
            text _("Music")
            bar:
                style "pref_slider"
                value Preference("music volume")
            text _("Ambience")
            bar:
                style "pref_slider"
                value Preference("ambience volume")
            text _("General sounds")
            bar:
                style "pref_slider"
                value Preference("sound volume")
            text _("Sex sounds")
            bar:
                style "pref_slider"
                value Preference("sexfx volume")
            text _("Interface")
            bar:
                style "pref_slider"
                value Preference("guisfx volume")

    textbutton _("Return"):
        style "menu_return"
        default_focus True
        action ShowMenu("main_menu")
        if main_menu:
            keysym "K_ESCAPE"

screen dropdown_example():
    modal True
    frame:
        align (0.5, 0.4)
        padding (20, 20)
        
        vbox:
            spacing 10
            text "Select Development Menu:"
            
            # 2. Trigger Button: Captures screen area focus to position the dropdown
            textbutton _("Clear persistent data"):
                style "pref_button"
                action Show(
                    "confirm",
                    message = _("Are you sure? This will clear persistent data,\nsuch as gallery unlocks and seen dialogue.\n{color=#ff2424}The game will restart.{/color}"),
                    yes_action = [Function(clearPersistent), Hide("confirm")], 
                    no_action = Hide("confirm"))
            textbutton _("Delete all saves"):
                style "pref_button"
                action Show("confirm",
                    message = _("Are you sure? This will delete all save files."), 
                    yes_action = [Function(delSaves), Hide("confirm")], 
                    no_action = Hide("confirm"))
            textbutton _("Save Naming"):
                style "pref_toggle"
                action ToggleField(persistent, "save_naming")
            textbutton _("Enter Cheat Code"):
                style "pref_button"
                action Show("enterCheatCode")
            if Build_Kind == "steam":
                textbutton _("Sync Achievements"):
                    style "pref_button"
                    action achievement.Sync()

    textbutton _("Return"):
        style "menu_return"
        default_focus True
        action Hide("dropdown_example")

screen difficulty_dropdown():
    modal True
    zorder 200

    frame:
        align (0.5, 0.4)
        padding (20, 20)

        vbox:
            spacing 10
            text _("Select difficulty:")
            for difficulty, name in DIFFICULTY.NAMES.items():
                textbutton name:
                    style "pref_toggle"
                    action [SetVariable("CurrentDifficulty", difficulty), Hide("difficulty_dropdown")]

    textbutton _("Return"):
        style "menu_return"
        default_focus True
        action Hide("difficulty_dropdown")
        

screen LanguageSelection(FromFirstLaunch = False):
    modal True
    zorder 200

    add "images/gui/unsorted/black_under.webp"
    frame:
        style "frame_outer"
        align (0.5, 0.5)
        vbox:
            xalign 0.5
            null height 5
            label _("Select game language") xalign 0.5
            null height 5
            vbox:
                xalign 0.5
                xsize 400
                if config.developer:
                    for LangName, LangCode in zip([_("English"), _("Spanish"), _("Chinese"), _("Japanese"), _("Russian"), _("Turkish"), _("Korean"), _("French"),_("Portuguese")], [None, "es", "zh", "ja", "ru", "tr", "kr", "fr", "ptPT"]):
                        textbutton tra(LangName):
                            style "pref_toggle"
                            if FromFirstLaunch == True:
                                action [Language(LangCode), Hide("LanguageSelection"), Return()]
                            else:
                                action Language(LangCode)
                else:
                    for LangName, LangCode in zip([_("English"), _("Spanish"), _("Chinese"), _("Japanese"), _("Russian"), _("Turkish"), _("Korean"), _("French"),_("Portuguese")], [None, "es", "zh", "ja", "ru", "tr", "kr", "fr", "ptPT"]):
                        textbutton tra(LangName):
                            style "pref_toggle"
                            if FromFirstLaunch == True:
                                action [Language(LangCode), Hide("LanguageSelection"), Return()]
                            else:
                                action Language(LangCode)

                if FromFirstLaunch:
                    text _("You can change the language later in game options."):
                        xalign 0.5 
                        text_align 0.5
                else:
                    null height 15
                    textbutton _("Return"):
                        xalign 0.5
                        action Hide("LanguageSelection")
                        default_focus True
                        if main_menu:
                            keysym "K_ESCAPE"
