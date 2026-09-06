init python:
    # this event triggers nijah questline if player investigates it,
    # progress: 0 for initial on-enter trigger, 1 for re-visitable state, 2 for post-rescue, 3 for nijah staying at MCs
    # note that gets unlocked after you bring nijah home
    notesLib["NijahStayingAtMCs"] = Note(
        _("Nijah stays over"), 
        _("Nijah, a Ramonian lady in a very... tricky situation is currently staying at my house. I should solve her situation somehow. I can only hide her for a week or so."))
    @AppendToAllQuests
    class EventNijahRescue(LogicModule):
        def __init__(self):
            super().__init__()

            self.checkDay = 0
            self.investigateFlag = True
            self.execTimes = 0

        def onEnter(self):  
            if GetLocID() == "novaras_dist_pleasure":
                if IsDaytime():
                    if self.checkDay != GetGameDay():
                        self.checkDay = GetGameDay()
                        if self.progress == 0:
                            if QstIsComplete(QstFromAnotherWorld):
                                if QstIsComplete(QstProperReunion):
                                    return TriggeredEvent("ev_nijah_rescue_0")
                        elif self.progress == 1:
                            self.investigateFlag = not self.investigateFlag
            elif GetLocID() == "mc_house_bedroom":
                if IsDaytime():
                    if self.progress == 2:
                        return TriggeredEvent("ev_nijah_rescue_2")

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_pleasure":
                if IsDaytime():
                    if self.progress == 1:
                        if self.investigateFlag:
                            btnMods["btn_nijah_rescue"] = BtnJumpLabel(_("Troubling sounds"), "ev_nijah_rescue_1")

            elif GetLocID() == "mc_house_bedroom":
                if IsDaytime():
                    if self.progress in [2, 3]:
                        # this jumps to a label down at nijah dialogue file,
                        # but the event-relevant dialogue nodes are all defined further down in this file
                        btnMods["btn_talkNijahMcHouse"] = BtnJumpLabel(_("Talk to Nijah"), "nijah_talk")

            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            if self.progress == 3:
                yield ("nijah_root", DNode(_("You'll have to flee the city."), "ev_nijah_rescue_fleecity"))

        def onStart(self):
            QstStart(PrimerDamzelInDiztrezz)

# on first time entering pl. district with event on
label ev_nijah_rescue_0:
    'Making my way through the streets of Novaras, In the distance, I heard the shrieking sounds of a cry and panicked pleading.'
    'Looking around, People went about their business obliviously, unable to hear the cries that to me were almost deafening.'
    MC '(What is that sound?)'
    MC "(It sounds like it's nearby...)"
    jump ev_nijah_rescue_1

# investigate troubling sounds button -> thugs scene -> mc house
label ev_nijah_rescue_1:
    call evscr_nijah_rescue_1 from _call_evscr_nijah_rescue_1
    call evscr_nijah_rescue_2 from _call_evscr_nijah_rescue_2
    # we land here if player rescues nijah by any means
    $ QstSetProgress(EventNijahRescue, 2)
    # transition to diff. location
    $ LocSet("mc_house_kitchen")
    $ LocFlush()
    with dissolve
    # call the 3rd part of the script at mc house
    call evscr_nijah_rescue_3 from _call_evscr_nijah_rescue_3
    $ NoteUnlock("NijahStayingAtMCs")
    $ LocEnterQ()

# nijah initial scene as she sits in mc bedroom
label ev_nijah_rescue_2:
    call evscr_nijah_rescue_4 from _call_evscr_nijah_rescue_4
    $ QstSetProgress(EventNijahRescue, 3)
    call processDialogue("nijah_root") from _call_processDialogue_23
    $ LocEnter()

# if player suggests she should leave
label ev_nijah_rescue_fleecity:
    call evscr_nijah_rescue_fleecity from _call_evscr_nijah_rescue_fleecity
