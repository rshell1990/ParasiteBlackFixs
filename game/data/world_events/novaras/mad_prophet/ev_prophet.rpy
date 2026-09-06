init python:
    @AppendToAllQuests
    class EventMadProphet(LogicModule): # prog 0 is first encounter
        def __init__(self):
            super().__init__()

            self.nextSpeechDay = -1
            self.IntervalInDays = 8  # < - how many days between each event happening
            self.ClickableLocID = LocEvent_GetFreeNovarasDistrict()
            self.origSpeechLabels = [ # this is used as a template to sample label list from
                "ev_madprophet_var1",
                "ev_madprophet_var2",
                "ev_madprophet_var3",
                "ev_madprophet_var4",
                "ev_madprophet_var5",
                "ev_madprophet_var6",
                "ev_madprophet_var7",
                "ev_madprophet_var8"]
            # this one is actually involved in logic, copy & shuffle if empty -> pop
            self.shuffledSpeechLabels = [] 
            self.SeenToday = False

        def onEnter(self):  
            if GetLocID() == self.ClickableLocID:
                if self.progress == 0:
                    if IsDaytime():
                        self.progress = 1
                        self.nextSpeechDay = GetGameDay() + RngInt(self.IntervalInDays - 1, self.IntervalInDays + 1)
                        return TriggeredEvent("ev_madProphetFirstMeet")

        # 1) repeat chooses a new loc ID
        def onMidnight(self):
            if self.progress == 1:
                # if prophet was today, roll clickable id (for the next one) and sched. next one
                if GetGameDay() == self.nextSpeechDay:
                    self.ClickableLocID = LocEvent_GetFreeNovarasDistrict()

                    self.nextSpeechDay = GetGameDay() + RngInt(self.IntervalInDays - 1, self.IntervalInDays + 1)
                    self.SeenToday = False

                # if next prophet day is in the past, something broke so re-schedule it
                if self.nextSpeechDay < GetGameDay():
                    self.nextSpeechDay = GetGameDay() + RngInt(self.IntervalInDays - 1, self.IntervalInDays + 1)
                    self.SeenToday = False

        # 2) and displays a button at corresp loc
        def locationMod(self):
            btnMods = {}
            if self.progress == 1:
                if IsDaytime():
                    if self.nextSpeechDay == GetGameDay():
                        if GetLocID() == self.ClickableLocID:
                            if self.SeenToday == False:
                                BtnID = LocIDList_NovarasCityStreets_SharedBtnIDMap[self.ClickableLocID]
                                btnMods[BtnID] = BtnJumpLabel(_("The Mad Prophet"), "ev_madProphetAgain")
            return LocButtonMod(directMods = btnMods)        
                

label ev_madProphetFirstMeet:
    $ Pause(0.1)
    if QstIsActive(QstTerminus):
        show mcprologue at left with easeinleft
    else:
        show mc at left with easeinleft
    "While making my way through the streets of Novaras, I heard the shrill voice of a figure towering over the others that a small crowd of people began to gather around."
    "Stepping closer, I took a closer look at the figure who was stood onto a few old wooden barrels to give him height, the hunched, half naked, emancipated old man began his mad preachings."
    call ev_madProphetRollSpeech from _call_ev_madProphetRollSpeech
    $ LocEnter()

label ev_madProphetAgain:
    $ Pause(0.1)
    if QstIsActive(QstTerminus):
        show mcprologue at left with easeinleft
    else:
        show mc at left with easeinleft
    "While making my way through the streets of Novaras, I heard the shrill voice of a figure towering over the others that a small crowd of people began to gather around."
    MC "(That doomsday preacher again.)"
    menu:
        "Listen to the Mad Prophet' speech.":
            $ EventMadProphet().SeenToday = True
            call ev_madProphetRollSpeech from _call_ev_madProphetRollSpeech_1
        "Move on.":
            hide mc with easeoutright
    $ LocEnterQ()


label ev_madProphetRollSpeech:
    if len(EventMadProphet().shuffledSpeechLabels) == 0:
        $ EventMadProphet().shuffledSpeechLabels = EventMadProphet().origSpeechLabels.copy()
        $ renpy.random.shuffle(EventMadProphet().shuffledSpeechLabels)
    hide mc
    hide mcprologue
    show cg_prophet
    with dissolve
    $ Pause()
    call expression EventMadProphet().shuffledSpeechLabels.pop() from _call_expression_2
    hide cg_prophet with dissolve
    return