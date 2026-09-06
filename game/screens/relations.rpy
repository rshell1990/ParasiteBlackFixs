screen relations():
    # toggle waiting availability
    on "show" action SetVariable("block_wait_dynamic", True)
    on "hide" action SetVariable("block_wait_dynamic", False)

    tag ingame_menu
    modal True
    zorder 1

    default chosen_tab = 1

    use close_outside("relations")
    use outer_frame(padd_top = 45):
        vbox:
            spacing 10
            xalign 0.5
            hbox: # tab switch buttons
                xalign 0.5
                ypos 10
                spacing 300
                textbutton _("Characters"):
                    style "quest_tab"
                    action SetScreenVariable("chosen_tab", 1)
                textbutton _("(WIP) Factions"):
                    style "quest_tab"
                    pass # action SetScreenVariable('chosen_tab', 2)
            if chosen_tab == 1:
                use relations_characters()

init python:
    def Rel_AssembleFiltersForScreenShow():
        Result = set()
        for RelID in Rel_Status_ID_Strings.keys():
            if RelID not in RelScreenFilterStatusesExcluded:
                Result.add(RelID)
        if "dead" not in RelScreenFilterStatusesExcluded:
            Result.add("dead")
        return Result

    def Rel_ListVisibleCharIDs(FilterList):
        # build the visible list according to the current hide-set
        Result = []
        for CharID in rel_known_chars:
            RelStatus   = worldChars[CharID]["relstatus"]
            IsDead      = worldChars[CharID]["relisdead"]
            if IsDead and "dead" in FilterList:
                Result.append(CharID)
            else:
                if RelStatus in FilterList:
                    if not IsDead:
                        Result.append(CharID)
        Result.sort()
        return Result

init python:
    RelIDToCategoryDescMap = {
        "rel_acquaintance"  :_("Toggle acquaintances"),
        "rel_friend"        :_("Toggle friends"),
        "rel_lover"         :_("Toggle lovers"),
        "rel_enemy"         :_("Toggle enemies"),
        "dead"              :_("Toggle deceased"),
    }

screen relations_characters():
    default ChosenCharID = None
    
    default ActiveFilterCategories = Rel_AssembleFiltersForScreenShow()
    hbox:
        xalign 0.5
        frame:
            #padding (20, 10)
            xsize 810
            ysize 725
            vbox:
                xalign 0.5
                xfill True
                null height 8
                hbox:
                    xalign 0.5
                    spacing 5
                    for FilterID in ["rel_acquaintance", "rel_friend", "rel_lover", "rel_enemy", "dead"]:
                        # textbutton FilterID:
                        #     text_size 25
                        #     style "button_sel"
                        #     selected FilterID in ActiveFilterCategories
                        #     action [ToggleSetMembership(ActiveFilterCategories, FilterID), ToggleSetMembership(RelScreenFilterStatusesExcluded, FilterID)]
                        button:
                            selected FilterID in ActiveFilterCategories
                            xysize (96, 64)
                            hovered TooltipSetUI(tra(RelIDToCategoryDescMap[FilterID]))
                            unhovered TooltipClearUI()
                            idle_background Transform(Frame("images/gui/frames/frame5.webp",  Borders(24, 24, 24, 24)), matrixcolor = OpacityMatrix(0.25))
                            hover_background Transform(Frame("images/gui/frames/frame5.webp", Borders(24, 24, 24, 24)), matrixcolor = OpacityMatrix(0.25))
                            selected_hover_background Transform(Frame("images/gui/frames/frame5.webp", Borders(24, 24, 24, 24)), matrixcolor = IdentityMatrix())
                            selected_idle_background Transform(Frame("images/gui/frames/frame5.webp",  Borders(24, 24, 24, 24)), matrixcolor = IdentityMatrix())
                            if FilterID == "rel_acquaintance":
                                add ICON.DRAMA size (54, 54) fit "contain" align (0.5, 0.5)
                            elif FilterID == "dead":
                                add ICON.DEATH size (48, 48) fit "contain" align (0.5, 0.5)
                            elif FilterID == "rel_friend":
                                add "images/gui/story/handshake.webp" size (68, 68) fit "contain" align (0.5, 0.5)
                            elif FilterID == "rel_lover":
                                add "images/gui/story/heart.webp" size (47, 47) fit "contain" align (0.5, 0.5)
                            elif FilterID == "rel_enemy":
                                add "images/gui/story/swords.webp" size (48, 48) fit "contain" align (0.5, 0.5)

                            action [ToggleSetMembership(ActiveFilterCategories, FilterID), ToggleSetMembership(RelScreenFilterStatusesExcluded, FilterID)]
                null height 8
                vpgrid:
                    xalign 0.5
                    spacing 4
                    cols 2
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                        # xfill True
                        # spacing 10
                    for CharID in Rel_ListVisibleCharIDs(ActiveFilterCategories):
                        button:
                            xalign 0.5
                            style "button_sel"
                            xsize 375
                            padding (14, 14)
                            hbox:
                                xfill True
                                fixed:
                                    xysize (96, 96)
                                    add "images/gui/unsorted/portrait_background.webp"
                                    add worldChars[CharID]["portrait"] size (80, 80) align (0.5, 0.5)
                                vbox:
                                    xfill True
                                    ysize 96
                                    xoffset 8
                                    text worldChars[CharID]["name"] anchor (0.0, 0.0) pos (0.0, 0.0)
                                    hbox:
                                        xfill True
                                        ysize 48
                                        align (0.0, 1.0)
                                        hbox:
                                            spacing 5
                                            if worldChars[CharID]["relisdead"]:
                                                add "images/gui/story/death.webp":
                                                    size (60, 40)
                                                    anchor (0.0, 0.0)
                                                    pos (0.0, 0.0)
                                                    fit "contain"
                                            else:
                                                if Rel_Status_ID_Strings[worldChars[CharID]["relstatus"]]["Icon"] is not None:
                                                    add Rel_Status_ID_Strings[worldChars[CharID]["relstatus"]]["Icon"]:
                                                        size (60, 40) 
                                                        anchor (0.0, 0.0) 
                                                        pos (0.0, 0.0) 
                                                        fit "contain"
                                                    if Rel_Status_ID_Strings[worldChars[CharID]["relstatus"]]["ShowNumber"]:
                                                        text "{color=#c4c0c0}" + tra(_("Rel: %s")) % (worldChars[CharID]["relation"] + 1) + "{/color}":
                                                            anchor (0.0, 0.0)
                                                            pos (0.0, 0.0)
                                        fixed:
                                            xfill True
                                            if Rel_Status_ID_Strings[worldChars[CharID]["relstatus"]]["Title"] is not None:
                                                text "{i}{color=#c4c0c0}%s{/color}{/i}" % tra(Rel_Status_ID_Strings[worldChars[CharID]["relstatus"]]["Title"]):
                                                    anchor (1.0, 0.0)
                                                    pos (1.0, 0.5)
                                                    size 24
                                                    xoffset -8
                                            else:
                                                text "" size 20

                            selected ChosenCharID == CharID
                            action SetLocalVariable("ChosenCharID", CharID)
        frame:
            xsize 590
            ysize 725
            viewport:
                yalign 0.0
                xalign 0.0
                xfill True
                draggable True
                mousewheel True
                scrollbars "vertical"

                ysize 690
                # portrait, name, summary & relationships
                vbox:
                    xfill True
                    xalign 0.5
                    if ChosenCharID is None:
                        null height 10
                        text _("Select a character to view their entry."):
                            xalign 0.5
                    else:
                        fixed:
                            xysize (256, 256)
                            align (0.5, 0.5)
                            add worldChars[ChosenCharID]["portrait"]:
                                align (0.5, 0.5) 
                                size (240, 240) 
                                fit "contain" 
                                xzoom -1.0
                            add "images/gui/unsorted/gallery_frame.webp":
                                align (0.5, 0.5)
                        null height 2
                        label worldChars[ChosenCharID]["name"]:
                            xalign 0.5 
                            text_size 50
                        null height 8
                        if Rel_Status_ID_Strings[worldChars[ChosenCharID]["relstatus"]]["ShowNumber"]:
                            hbox:
                                xalign 0.5
                                add "images/gui/story/heart.webp"
                                null width 10
                                text "{i}{color=#c4c0c0}" + tra(_("Relationship: %s")) % (worldChars[ChosenCharID]["relation"] + 1) + "{/color}{/i}"
                        null height 10
                        if ChosenCharID in RelText:
                            for EntryData in sorted([EntryData for EntryID, EntryData in RelText[ChosenCharID].items() if EntryID in worldChars[ChosenCharID]["RelTextIDs"]], key = lambda x: x["order"]):
                                text EntryData["text"]:
                                    xfill True
                                    xalign 0.0
                                    xoffset 10
                                null height 10