# there are two menus, alt+d and f2. alt+d is broad inspection thingy, f2 is for simpler/smaller stuff

# a mode that skips/speeds up some transitions, accessed via menu
default DEBUG_FastMode = False

# to show current var we're in
default DEBUG_CurrentLabel = ""
default DEBUG_TrackedVariables = []

init python:
    # called whenever a labels is reached. 
    # The first arg (Val) is the name of the label. 
    # The second (Arg) is True if the label was reached through jumping, calling, or creating a new context, and False otherwise.
    def DEBUG_StoreCurrentLabel(Val, Arg):
        if Val not in ["_return", "after_load", "_after_load", "_noisy_return", "_hide_windows", "_gl_test"]: # <- these are built-in renpy labels for tech stuff
            store.DEBUG_CurrentLabel = Val
        return
    config.label_callbacks.append(DEBUG_StoreCurrentLabel)
    if config.developer:
        DEBUG_TrackedVariables = [
            "DEBUG_CurrentLabel"]
        config.always_shown_screens.append("dev_quick_inspect")
        config.keymap["dev_menu"] =     ["alt_K_d", "K_F2"]
        config.underlay[0].keymap["dev_menu"] = Show("dev_menu")
        config.keymap["dev_quests"] =   ["alt_K_q"]
        config.underlay[0].keymap["dev_quests"] = Show("dev_quests")

    DEV_VARIABLES = {    
        "MAIN_MENU_OPTS"      :(True if config.developer else False),
        "LOC_IDS"             :(True if config.developer else False),
        "DEV_MENU_BTN"        :(True if config.developer else False),
        "HOVER_ITEM_IDS_AND_ORIG_VALUE" : (True if config.developer else False),
        "HOVER_BTN_TAGS"      :(True if config.developer else False),
        "SHOW_EXTRA_MAP_DATA" :False,
    }

    # (this is GUI-only)
    def DEBUG_GUI_DevMenuGetLogicModulesToShow(show_active, show_inactive, show_logicmodules, show_quests, quest_filter): 
        Result = []
        # two pass, first get active or inactive shit in
        for lmod in allQuests:
            if QstIsActive(lmod):
                if show_active:
                    Result.append(lmod)
            else:
                if show_inactive:
                    Result.append(lmod)
        Result2 = []
        # second pass, remove stuff according to quest / lmod filter
        for lmod in Result:
            if show_logicmodules:
                if lmod().HIDDEN:
                    Result2.append(lmod)
            if show_quests:
                if not lmod.HIDDEN:
                    Result2.append(lmod)
        Result = list(set(Result2))
        # name filter
        Result = [logicmod for logicmod in Result if re.match(f".*{quest_filter}.*", logicmod.__name__.lower())]
        # sorting
        Result = sorted(Result, key=lambda x: x.__name__)
        return Result

###### clipboard mode gui funcs
    def DEBUG_GUI_GetClipboardText():
        import pygame.scrap
        Result = pygame.scrap.get(pygame.SCRAP_TEXT).decode()
        if Result:
            return Result
        else:
            return ""

    def DEBUG_GUI_SaveClickedPosToClipboard():
        import pygame.scrap
        CurrentBuffer = pygame.scrap.get(pygame.SCRAP_TEXT).decode()
        MousePos = renpy.get_mouse_pos()
        CurrentBuffer += str(MousePos)
        CurrentBuffer += "\n("
        CurrentBuffer += str(round(MousePos[0] / 1920, 3))
        CurrentBuffer += ", "
        CurrentBuffer += str(round(MousePos[1] / 1080, 3))
        CurrentBuffer += ")"
        CurrentBuffer += "\n"
        pygame.scrap.put(pygame.SCRAP_TEXT, CurrentBuffer.encode("utf-8", "ignore"))
        return
    
    def DEBUG_GUI_ClearClipboard():
        import pygame.scrap
        pygame.scrap.put(pygame.SCRAP_TEXT, "".encode("utf-8", "ignore"))
        return

    # skips X days, RUNS GAME LOGIC but suppresses on-enter events and infection gain
    # uses rest_menu var to store data
    def DEBUG_InitiateTimeWarp(DaysAmt):
        store.rest_menu_wait_hours = DaysAmt * 24
        renpy.jump("DEBUG_TimeWarpWait")



label DEBUG_TimeWarpWait:
    $ tmpvar["stored_inf_gain_mode"] = InfectionModule().DailyGain
    $ InfGainDaily(False)
    scene black with dissolve
    $ tmpvar["wait_hours"] = rest_menu_wait_hours
    while tmpvar["wait_hours"] > 0:
        $ TimeAdvBy(TIME_1H)
        $ tmpvar["wait_hours"] -= 1
    $ InfGainDaily(tmpvar["stored_inf_gain_mode"])
    $ tmpvar = {}
    $ LocEnter()

######### Alt+d menu screens
screen dev_tabs():
    style_prefix "devmode"
    add "#000000e6"
    vbox:
        spacing 5
        hbox:
            spacing 5

            textbutton _("Menu"):
                action Show("dev_menu")
            textbutton _("Logic modules"):
                action Show("dev_quests")
            textbutton _("Characters"):
                action Show("dev_characters")
            textbutton _("Locations"):
                action Show("dev_locations")
        fixed:
            transclude
    key ["game_menu", "dev_menu"] action Hide()

screen dev_locations():
    tag devmenu
    modal True
    default loc_filter = ""
    default loc_selected = ""
    style_prefix "devmode"
    use dev_tabs():
        frame:
            hbox:
                spacing 30
                vbox:
                    spacing 20
                    xsize 600
                    hbox:
                        spacing 30
                        label _("Filter:") yalign 0.5
                        input:
                            value ScreenVariableInputValue("loc_filter")
                            yalign 0.5
                            color "#ffffff"
                            allow "abcdefghijklmnopqrstuvwxyz0123456789 '_"
                            size 35
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        side_spacing 10
                        xsize 600
                        vbox:
                            spacing 10
                            for LocationObject in sorted([LocObject for LocObject in wLocs.values() if loc_filter in LocObject.tag.lower() or loc_filter in LocObject.displayName.lower()],  key=lambda x: x.displayName):
                                textbutton "%s\n%s" % (LocationObject.displayName, LocationObject.tag):
                                    style "pref_toggle"
                                    action SetScreenVariable("loc_selected", LocationObject.tag)
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    side_spacing 10
                    vbox:
                        spacing 20
                        if loc_selected:
                            vbox:
                                xfill True
                                text "{u}Location{/u}: [loc_selected]"
                                textbutton "Jump to":
                                    if not IsPlayerInBattle() and not IsPlayerInGalleryScene():
                                        action [Function(LocSet, loc_selected), Function(LocFlush), Hide("dev_locations"), Jump("main_recheck"), SetVariable("TravelState", None)]
                            vbox:
                                spacing 10
                                for key, value in wLocs[loc_selected].__dict__.items():
                                    hbox:
                                        spacing 10
                                        text key:
                                            color "#f59a84"
                                        text "==":
                                            color "#9b928f"
                                        text str(value).replace("{","{{").replace("[","[["):
                                            size 30 
                                            yalign 0.5

screen dev_menu():
    tag devmenu
    modal True
    style_prefix "devmode"
    key ["game_menu", "dev_menu"] action Hide()
    use dev_tabs():
        frame:
            xfill True
            yfill True
            # a hbox of vboxes filled with stuff such as "experience" "time" etc
            hbox:
                spacing 5
                vbox:
                    spacing 5
                    frame:
                        vbox:
                            label "inventory"
                            hbox:
                                textbutton "+100 gold":
                                    action Function(PlayerAddItem, "gold", 100)
                                textbutton "+1000 gold":
                                    action Function(PlayerAddItem, "gold", 1000)
                                textbutton "+10000 gold":
                                    action Function(PlayerAddItem, "gold", 10000)
                            hbox:
                                textbutton "-100 gold":
                                    action Function(PlayerRemItem, "gold", 100)
                                textbutton "-1000 gold":
                                    action Function(PlayerRemItem, "gold", 1000)
                                textbutton "-10000 gold":
                                    action Function(PlayerRemItem, "gold", 10000)
                            textbutton _("Get all items"):
                                action Function(DEBUG_PlayerAddAllItems)
                            textbutton _("Get all items (x50)"):
                                action Function(DEBUG_PlayerAddAllItems, 50)
                            textbutton _("Remove all inv items"):
                                action Function(DEBUG_PlayerRemoveAllItems)
                    frame:
                        vbox:
                            label "gallery"
                            textbutton _("Unlock all gallery entries"):
                                action Function(GalUnlockAllScenes)
                            textbutton _("Lock all gallery entries"):
                                action Function(GalLockAllScenes)
                    frame:
                        vbox:
                            label "fast nav"
                            textbutton _("(g) jump to Novaras City gates"):
                                action [TooltipClearUI(), Hide("dev_menu"), Function(LocSet, "novaras_gates"), Function(LocFlush), Jump("main_recheck")]
                                if config.developer: # just in case
                                    keysym "K_g"
                    frame:
                        vbox:
                            label "battle"

                            textbutton _("win battle"):
                                if IsPlayerInBattle():
                                    action [Hide("dev_menu"), Function(Battle_Win)]
                            textbutton _("restart"):
                                if IsPlayerInBattle():
                                    action [Hide("dev_menu"), Jump("Battle_Start")]
                            textbutton _("toggle sel.  outlines"):
                                if IsPlayerInBattle():
                                    action [Hide("dev_menu"), ToggleVariable("Battle_ShowSelectionOutlines")]
                    frame:
                        vbox:
                            label "infection"
                            hbox:
                                textbutton "+5":
                                    action Function(InfChangeBy, 5)
                                textbutton "-5":
                                    action Function(InfChangeBy, -5)
                                textbutton "+15":
                                    action Function(InfChangeBy, 15)
                                textbutton "-15":
                                    action Function(InfChangeBy, -15)
                            hbox:
                                textbutton "set to 0":
                                    action Function(InfChangeBy, -999)
                                textbutton "set to 25":
                                    action Function(InfChangeBy, 25, SetTo = True)
                                textbutton "set to 50%":
                                    action Function(InfChangeBy, 50, SetTo = True)
                    frame:
                        vbox:
                            label "time"
                            hbox:
                                textbutton "toggle fast mode" action ToggleVariable("DEBUG_FastMode")
                            hbox:
                                textbutton "LIGHTSTART":
                                    action SetVariable("rpTime", TIME_DAY_START)
                                textbutton "noon":
                                    action SetVariable("rpTime", 60 * 60 * 12)
                                textbutton "LIGHTEND":
                                    action SetVariable("rpTime", TIME_DAY_END)
                                textbutton "midnight":
                                    action SetVariable("rpTime", 0)
                            hbox:
                                textbutton "+30m":
                                    action Function(TimeAdvTo, TIME_05H)
                                textbutton "+1h":
                                    action Function(TimeAdvBy, TIME_1H)
                                textbutton "-30m":
                                    action SetVariable("rpTime", (store.rpTime - 1800) % SECS_IN_DAY)
                                textbutton "-1h":
                                    action SetVariable("rpTime", (store.rpTime - 3600) % SECS_IN_DAY)
                            hbox:
                                textbutton "+7 days":
                                    action [Hide("dev_menu"), Function(DEBUG_InitiateTimeWarp, 7)]
                                textbutton "+14 days":
                                    action [Hide("dev_menu"), Function(DEBUG_InitiateTimeWarp, 14)]
                                textbutton "+30 days":
                                    action [Hide("dev_menu"), Function(DEBUG_InitiateTimeWarp, 30)]
                vbox:
                    spacing 5
                    frame:
                        vbox:
                            xsize 500
                            label "player party"
                            textbutton "heal everyone" action Function(HealParty)
                            hbox:
                                spacing 3
                                textbutton "Add all" action Function(DEBUG_AddAllCompanions)
                                textbutton "Rem all" action Function(DEBUG_RemAllCompanions)

                            for CharID in [x for x in worldChars if worldChars[x]["IsCompanion"] is True]:
                                textbutton CharID:
                                    if not CharInParty(CharID):
                                        action Function(PartyAddChar, CharID)
                                    else:
                                        action Function(PartyRemChar, CharID)
                            text "Current player party: "
                            text "%s" % ", ".join(x for x in player_party)
                    frame:
                        vbox:
                            label "experience"
                            vbox:
                                textbutton _("Add 50 XP"):
                                    action Function(AddExpPlayer, 50)
                                textbutton _("Add 300 XP"):
                                    action Function(AddExpPlayer, 300)
                                textbutton _("Add 1000 XP"):
                                    action Function(AddExpPlayer, 1000)
                                textbutton _("Add 20000 XP"):
                                    action Function(AddExpPlayer, 20000)
                                textbutton _("Add 100000 XP"):
                                    action Function(AddExpPlayer, 100000)
                                textbutton _("Set all stats for all chars to 20"):
                                    action Function(DEBUG_SetAllStatsTo, Value = 20)
                                textbutton _("Set all stats for all chars to 30"):
                                    action Function(DEBUG_SetAllStatsTo, Value = 30)
                                textbutton _("Add 1 level to all party battle skills"):
                                    action Function(DEBUG_AddOneToAllClassSkills)
                                textbutton _("Add all perks to player"):
                                    action Function(DEBUG_AddAllPerks)
                vbox:
                    spacing 5
                    frame:
                        vbox:
                            label "show/hide dev only stuff"
                            textbutton "internal loc ID":
                                action ToggleDict(DEV_VARIABLES, "LOC_IDS")
                            textbutton "dev menu btn top-right (alt + d)":
                                action ToggleDict(DEV_VARIABLES, "DEV_MENU_BTN")
                            textbutton "item ID on inv. hover\nand pre-discounts shop value":
                                action ToggleDict(DEV_VARIABLES, "HOVER_ITEM_IDS_AND_ORIG_VALUE")
                            textbutton "intern. button tags on hover":
                                action ToggleDict(DEV_VARIABLES, "HOVER_BTN_TAGS")
                            textbutton "extra travel map node/connection info":
                                action ToggleDict(DEV_VARIABLES, "SHOW_EXTRA_MAP_DATA")
                    frame:
                        vbox:
                            label "add/remove locations from world map"
                            for LocID in [x for x in wLocs.keys() if hasattr(wLocs[x], "wMap_DisplayName")]:
                                textbutton LocID:
                                    selected LocID in seenWMapLocTags
                                    if LocID not in seenWMapLocTags:
                                        action AddToSet(seenWMapLocTags, LocID)
                                    else:
                                        action RemoveFromSet(seenWMapLocTags, LocID)

screen dev_quests():
    tag devmenu
    modal True
    default quest_selected  = ""
    default quest_filter    = ""
    default show_quests     = True    # show non-HIDDEN logicmodules (real quests) 
    default show_logicmodules = True  # show HIDDEN logicmodules (stuff that is not real quests)
    default show_active     = True    # show any active
    default show_inactive   = True    # show any inactive
    style_prefix "devmode"
    use dev_tabs():
        frame:
            hbox:
                spacing 30
                vbox:
                    spacing 20
                    xsize 600
                    hbox:
                        spacing 20
                        xfill True
                        textbutton "Active":
                            action ToggleScreenVariable("show_active")
                            xsize 120
                            xalign 0.5
                        textbutton "Inactive":
                            action ToggleScreenVariable("show_inactive")
                            xsize 120
                            xalign 0.5
                        textbutton "Quests":
                            action ToggleScreenVariable("show_quests")
                            xsize 120
                            xalign 0.5
                        textbutton "Logic modules":
                            action ToggleScreenVariable("show_logicmodules")
                            xsize 120
                            xalign 0.5
                    hbox:
                        spacing 30
                        label _("Filter:") yalign 0.5
                        input:
                            value ScreenVariableInputValue("quest_filter")
                            yalign 0.5
                            color "#ffffff"
                            allow "abcdefghijklmnopqrstuvwxyz0123456789_"
                            size 35
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        side_spacing 10
                        xsize 600

                        vbox:
                            spacing 2
                            text "total filtered: %s" % len(DEBUG_GUI_DevMenuGetLogicModulesToShow(show_active, show_inactive, show_logicmodules, show_quests, quest_filter))
                            for qst in DEBUG_GUI_DevMenuGetLogicModulesToShow(show_active, show_inactive, show_logicmodules, show_quests, quest_filter):
                                textbutton qst.__name__:
                                    action SetScreenVariable("quest_selected", qst.__name__)

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    side_spacing 10
                    vbox:
                        spacing 20
                        if quest_selected:
                            hbox:
                                xfill True
                                text "Logic module: [quest_selected]"
                                text f"  (Current day: {day})" color "#f59a84" xalign 1.0
                            vbox:
                                spacing 10
                                for key, value in questObjs[quest_selected].__dict__.items():
                                    hbox:
                                        spacing 10
                                        text key:
                                            color "#f59a84"
                                        text "==":
                                            color "#9b928f"
                                        text str(value).replace("{","{{").replace("[","[["):
                                            size 30 
                                            yalign 0.5
                            hbox:
                                text "warning these are unsafe to mash randomly"
                                textbutton "Start" action Function(questObjs[quest_selected].start, silent = True)
                                textbutton "Finish" action Function(questObjs[quest_selected].finish, silent = True)

screen dev_characters():
    tag devmenu
    modal True
    style_prefix "devmode"
    default char_selected = ""
    default char_filter = ""

    use dev_tabs():
        frame:
            hbox:
                spacing 30
                vbox:
                    spacing 20
                    xsize 500
                    hbox:
                        spacing 30
                        label _("Filter:") yalign 0.5
                        input:
                            value ScreenVariableInputValue("char_filter")
                            yalign 0.5
                            color "#ffffff"
                            allow "abcdefghijklmnopqrstuvwxyz0123456789_"
                            size 35

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        side_spacing 10
                        xsize 500
                        vbox:
                            spacing 10
                            for chr in sorted([c for c in worldChars if re.match(f".*{char_filter}.*", c.lower())], key=lambda x: x):
                                textbutton chr:
                                    style "pref_toggle"
                                    action SetScreenVariable("char_selected", chr)

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    side_spacing 10
                    vbox:
                        spacing 20
                        if char_selected:
                            hbox:
                                xfill True
                                text "{u}Name{/u}: " + worldChars[char_selected]["name"]
                            vbox:
                                spacing 10
                                for key, value in worldChars[char_selected].props.items():
                                    hbox:
                                        spacing 10
                                        text key:
                                            color "#f59a84"
                                        text "==":
                                            color "#9b928f"
                                        text str(value).replace("{","{{").replace("[","[["):
                                            size 30 
                                            yalign 0.5

screen dev_menu_button():
    if DEV_VARIABLES["DEV_MENU_BTN"] and not IsPlayerInBattle() and config.developer:
        textbutton "dev menu (alt+d)":
            anchor (1.0, 0.0)
            pos (0.85, 0.01)
            keyboard_focus False
            action ToggleScreen("dev_menu")

#########  F2 menu
screen dev_quick_inspect():
    zorder 666
    default force_refresh = False
    default show_dev_menu = False

    # for mousepos
    default XY = (0, 0)     
    default ShowPos = False

    default DoPosThing = False

    key "K_F2" action [ToggleLocalVariable("show_dev_menu"), SetLocalVariable("DoPosThing", False), Function(DEBUG_GUI_ClearClipboard)]
    if DoPosThing:
        button:
            xsize 1920
            ysize 1080
            action NullAction()
            background Null()
            selected False
    if config.developer and show_dev_menu:
        drag:
            align (0.5, 0.1)
            drag_handle (0, 0, 1.0, 1.0) # entire frame
            frame:
                style_prefix "devmode"
                vbox:
                    hbox:
                        xalign 1.0
                        textbutton "force refresh" action ToggleLocalVariable("force_refresh")
                        textbutton "X" xalign 1.0 action Hide("dev_quick_inspect")
                    hbox:
                        # vars
                        vbox:
                            for Var in DEBUG_TrackedVariables:
                                if getattr(store, Var, None) is not None:
                                    text Var + " : " xalign 1.0
                        # values
                        vbox:
                            for Var in DEBUG_TrackedVariables:
                                if getattr(store, Var, None) is not None:
                                    hbox:
                                        text str(getattr(store, Var)) xalign 0.0
                    if DoPosThing:
                        hbox:
                            spacing 10
                            text "Mouse pos X: %i" % XY[0]
                            text "Y: %i" % XY[1]
                        hbox:
                            spacing 10
                            text "X (pos): %f" % round(float(XY[0]) / 1920, 3)
                            text "Y (pos): %f" % round(float(XY[1]) / 1080, 3)
                        #text "Clicking will save mouse pixel pos and relative screen pos to your clipboard!"
                        #text "(reset the screen with F2 to exit mouse & clipboard mode)"
                        textbutton "Empty clipboard" action Function(DEBUG_GUI_ClearClipboard)
                        text "Current clipboard:"
                        text DEBUG_GUI_GetClipboardText()
                    else:
                        textbutton "Enalbe mouse pos & clipboard mode" action ToggleLocalVariable("DoPosThing")
    if DoPosThing:
        key "mousedown_1" action Function(DEBUG_GUI_SaveClickedPosToClipboard)
        timer 0.033 action SetLocalVariable("XY", renpy.get_mouse_pos()) repeat True

    if force_refresh:
        timer 0.01 repeat True action Function(renpy.restart_interaction)
