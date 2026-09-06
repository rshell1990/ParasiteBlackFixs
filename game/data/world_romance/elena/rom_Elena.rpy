init python:
    notesLib["ElenaRomanceGetReginaOut"] = Note(
        _("Elena's itch"), 
        _("Elena needs a bath. I need to get Regina out for a while..."))
    # all related to "get lingerie" stuff
    notesLib["ElenaRomanceGetLingerie"] = Note(
        _("Elena's request"), 
        _("Elena wants a new, more... attractive set of clothes. Perhaps a tailor could help."))
    notesLib["ElenaRomanceLingerieInProgress"] = Note(
        _("Elena's request"), 
        _("A new set of lingerie for Elena is being worked on. Should be ready in a couple days."),
        journal_flag_delayed = True)
    notesLib["ElenaRomanceDeliverLingerie"] = Note(
        _("Elena's request"), 
        _("Now that I have a set of lingerie for Elena, I've gotta deliver it."))
    # ask regina to leave again
    notesLib["ElenaRomanceGetReginaOutAgain"] = Note(
        _("Get Regina to leave"), 
        _("See if [regina_ref!t] will give you some 'alone time' again..."))
    @AppendToAllQuests
    # elena romance logic
    # prog 0 - trigger intro
    # prog 1 - ask regina to leave
    # prog 2 - post-leave, rom begins
    class RomanceElena(LogicModule):
        def __init__(self):
            super().__init__()

            # delayed day counter for starting the quest
            self.dayToStartFiringEvent = -1
            # when regina appears again
            self.reginaReturnTime = -1
            # dros lingerie day counter
            self.dayToHaveLingReady = -1
            # wear ling. flag for scenes
            self.wearLingeriePlease = False

        def onMidnight(self):
            if self.dayToStartFiringEvent == -1:
                self.dayToStartFiringEvent = GetGameDay() + 2

            if self.progress == 4:
                if self.dayToHaveLingReady == -1:
                    self.dayToHaveLingReady = GetGameDay() + 2

        def onEnter(self):  
            if GetLocID() == "mc_house_bedroom":
                if self.dayToStartFiringEvent != -1:
                    if GetGameDay() >= self.dayToStartFiringEvent:
                        if self.progress == 0:
                            if QstIsOver(QstWomansTouch):
                                return TriggeredEvent("rom_Elena_ItchyIntro")

            elif GetLocID() == "mc_house_kitchen":
                if IsInTimeFrame(TIME_MORNING, TIME_LATEEVENING):
                    if QstDelayCheck(self):
                        if self.progress == 8:
                            return TriggeredEvent("rom_Elena_CookingIntro")
                        elif self.progress == 9:
                            return TriggeredEvent("rom_Elena_Cooking")

                # since this LM "hides" regina during some scenes, 
                # we need to re-show
                if self.reginaReturnTime != -1:
                    if store.rpTime > self.reginaReturnTime:
                        self.reginaReturnTime = -1
                        CharSetVar("regina", "hide", False)

        def extraDialogue(self):
            if self.progress == 1:
                yield ("regina_root", DNode(_("I need to ask something of you...(persuade to leave the house)"), "rom_Elena_AskReginaLeave"))
            elif self.progress == 3:
                yield ("dros_root", DNode(_("I need some lingerie done."), "rom_ElenaGetLingerieDrosLines"))
            elif self.progress == 4:
                if GetGameDay() >= self.dayToHaveLingReady:
                    yield ("dros_root", DNode(_("About that lingerie..."), "rom_ElenaGetLingerieDrosComplete"))
                else:
                    yield ("dros_root", DNode(_("About that lingerie..."), "rom_ElenaGetLingerieDrosInProgress"))
            elif self.progress == 5:
                yield ("elena_root", DNode(_("I have something to give you..."), "rom_ElenaGetLingerieDeliver"))
            elif self.progress == 6:
                yield ("regina_root", DNode(_("I was wondering if perhaps you could give me some alone time again..."), "rom_AskReginaLeaveAgain"))
            elif self.progress >= 8:
                yield ("elena_root", DNode(_("How are you feeling?"), "rom_ElenaHowYOuFeelin"))
                yield ("elena_root", DNode(_("Come closer..."), "rom_ElenaComeCloseer"))
                yield ("elena_root", DNode(_("I was thinking perhaps we could do something together"), "rom_ElenaSexOptions"))

        def onComplete(self):
            CharSetVar("regina", "hide", False)
