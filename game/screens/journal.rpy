screen journal():
    # toggle waiting availability
    on "show" action SetVariable("block_wait_dynamic", True)
    on "hide" action SetVariable("block_wait_dynamic", False)

    tag ingame_menu
    modal True

    default chosen_tab = 1
    default note_selIdx = 0

    use close_outside("journal")
    use outer_frame(padd_top = 45):
        vbox:
            spacing 10
            xalign 0.5
            hbox: # tab switch buttons
                xalign 0.5
                ypos 10
                spacing 300
                textbutton _("Quests"):
                    style "quest_tab"
                    action SetScreenVariable('chosen_tab', 1)
                textbutton _("Notes"):
                    style "quest_tab"
                    action SetScreenVariable('chosen_tab', 2)
                ## will display completed/total "real quests"
                textbutton tra(_("History (%s/%s)")) % (len([x for x in allQuests if not x().HIDDEN and QstIsOver(x)]), len([x for x in allQuests if not x().HIDDEN])):
                    style "quest_tab"
                    action SetScreenVariable('chosen_tab', 3)
            if chosen_tab == 1:
                use journal_sub_quests(False)
            if chosen_tab == 2:
                use journal_sub_notes(note_selIdx)
            if chosen_tab == 3:
                use journal_sub_quests(True)


screen journal_sub_quests(isHistory):
    python:
        qstList = []
        for Quest in GetAllGameQuests():
            if (isHistory and Quest.isOver and Quest.QuestOverShowInHistory) or (not isHistory and Quest.isActive):
                qstList.append(Quest)
        
        # sort by quest completion order for log
        if isHistory:
            qstList = sorted(qstList, key = lambda x: x.FinishOrder, reverse = True)

        selIdx = -1 # Select first item in list if nothing is selected
        for idx, x in enumerate(qstList):
            if x.log_isSelected():
                selIdx = idx
                break
        if selIdx == -1 and len(qstList) != 0:
            qstList[0].log_select()
            selIdx = 0

    hbox:
        frame:
            padding (20,0)
            xsize 450
            ysize 725
            viewport:
                draggable True
                mousewheel True
                ysize 700
                yalign 0.5
                vbox:
                    null height 0
                    spacing 10
                    for qstObj in qstList:
                        hbox:
                            spacing 5
                            if isHistory: 
                                if qstObj.IsMain:
                                    add "images/gui/journal/track_crown.webp":
                                        size (40, 40)
                                        yalign 0.5
                            else:
                                # toggle quest tracker
                                imagebutton:
                                    yalign 0.5
                                    if qstObj.IsMain:
                                        idle Transform("images/gui/journal/track_crown.webp", size = (40, 40))
                                        hovered TooltipSetUI(_("Main quest,\nalways tracked"))
                                        unhovered TooltipClearUI()
                                        action NullAction()
                                    else:
                                        if qstObj.isTracked:
                                            idle Transform("images/gui/journal/track_on.webp", size = (40, 40))
                                        else:
                                            idle Transform("images/gui/journal/track_off.webp", size = (40, 40))
                                        hovered TooltipSetUI(_("Toggle tracking"))
                                        unhovered TooltipClearUI()
                                        action SetField(qstObj, "isTracked", not qstObj.isTracked)

                            python:
                                if qstObj.isFailed:
                                    adjTitle = tra(_("(failed) %s")) % qstObj.TITLE
                                else:
                                    adjTitle = tra(qstObj.TITLE)
                                if not isHistory:
                                    if hasattr(qstObj, "suggestedLevel") and qstObj.suggestedLevel:
                                        adjsuggestedLevel = tra(_("Suggested Level %s")) % qstObj.suggestedLevel
                                        if GetPlayerLevel() >= qstObj.suggestedLevel:
                                            adjsuggestedLevel = "{color=#42ff55}" + adjsuggestedLevel + "{/color}"
                                        else:
                                            adjsuggestedLevel = "{color=#ff4242}" + adjsuggestedLevel + "{/color}"
                                        adjTitle += ( "\n" + adjsuggestedLevel )
                            textbutton adjTitle:
                                style "quest_entry"
                                text_textalign 0.5
                                selected qstObj.log_isSelected()
                                action Function(qstObj.log_select)
                    
        frame:
            xsize 950
            ysize 725
            
            fixed:
                ypos 10
                viewport:
                    yalign 0.0
                    xalign 0.5
                    draggable True
                    mousewheel True
                    ysize 690
                    vbox: # summary, current objective and steps list
                        xfill True
                        #null height 10
                        spacing 10
                        if selIdx != -1:
                            text qstList[selIdx].DESCRIPTION:
                                xalign 0.5
                                xsize 900
                                text_align .5
                            add "images/gui/unsorted/splitter_line.webp":
                                anchor(0.5,0.5)
                                pos(0.5,0.5)
                                size (800,30)
                            if not isHistory:
                                for ActveStage in [qstList[selIdx].GOALS[StageKey] for StageKey in reversed(sorted(qstList[selIdx].GoalStates.keys())) if qstList[selIdx].GoalStates[StageKey] == GoalState.VISIBLE]:
                                    if ActveStage.hintTxt is not None:
                                        text ActveStage.hintTxt:
                                            xalign 0.5
                                            xsize 900
                                            text_align .5
                                        add "images/gui/unsorted/splitter_line.webp":
                                            yzoom -1.0
                                            xalign 0.5
                                            size (800, 30)
                            # a list of completed stages & a current one
                            for gState, qstStage in reversed(qstList[selIdx].getOrderedStages()):
                                if gState == GoalState.HIDDEN:
                                    pass
                                if gState == GoalState.VISIBLE:
                                    hbox:
                                        xoffset 10
                                        spacing 7
                                        add "images/gui/journal/questmark_current.webp":
                                            yalign 0.5
                                            size (32,32)
                                        text qstStage.title style "quest_stage_active"
                                if gState == GoalState.FAILED:
                                    hbox:
                                        xoffset 10
                                        spacing 7
                                        add "images/gui/journal/questmark_failed.webp":
                                            yalign 0.5
                                            size (32,32)
                                        text qstStage.title style "quest_stage_completed"
                                if gState == GoalState.COMPLETE:
                                    hbox:
                                        xoffset 10
                                        spacing 7
                                        add "images/gui/journal/questmark_completed.webp":
                                            yalign 0.5
                                            size (32,32)
                                        text qstStage.title style "quest_stage_completed"
                        else:
                            if isHistory:
                                text _("Any quests you have completed will be listed here.") xalign 0.5 text_align 0.5
                            else:
                                text _("Any active quests you have will be listed here.") xalign 0.5 text_align 0.5

screen journal_sub_notes(selIdx):
    default NoteList = sorted(
        (notesLib[k] for k in unlockedNotes),               # only unlocked
        key = lambda n: (                                   # sort key tuple
            n.journal_flag_persistent,                      # False < True
            n.journal_flag_delayed                         # False < True
        )
    )

    hbox:
        frame:
            padding (20,0)
            xsize 450
            ysize 725
            viewport:
                draggable True
                mousewheel True
                ysize 700
                yalign 0.5
                vbox:
                    null height 0
                    spacing 10
                    for NoteIndex, NoteObj in enumerate(NoteList):
                        hbox:
                            spacing 5
                            if NoteObj.journal_flag_delayed:
                                imagebutton:
                                    yalign 0.5
                                    idle Transform(ICON.HOURGLASS, size = (40, 40), fit = "contain")
                                    hovered TooltipSetUI(_("Delayed\nThis note describes an event or an activity that is likely to happen after some time had passed."))
                                    unhovered TooltipClearUI()
                                    action NullAction()
                            if NoteObj.journal_flag_persistent:
                                imagebutton:
                                    yalign 0.5
                                    idle Transform(ICON.REPEAT, size = (40, 40), fit = "contain")
                                    hovered TooltipSetUI(_("Persistent\nThis note describes a recurring event or an activity in the world."))
                                    unhovered TooltipClearUI()
                                    action NullAction()

                            textbutton NoteObj.name:
                                style "quest_entry"
                                selected (NoteIndex == selIdx)
                                action SetScreenVariable("note_selIdx", NoteIndex)
        frame:
            xsize 950
            ysize 725
            fixed:
                ypos 10
                viewport:
                    xalign 0.5
                    draggable True
                    mousewheel True
                    vbox:
                        xfill True
                        spacing 10
                        if NoteList:
                            text NoteList[selIdx].text:
                                xalign 0.5
                                xsize 900
                                text_align .5
                        else:
                            text _("Various important, but not quest-related notes will be listed here as you navigate the world.") xalign 0.5 text_align 0.5