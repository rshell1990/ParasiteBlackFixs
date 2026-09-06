init python:
    notesLib["RomWinward_VisitTomorrow"] = Note(
        _("Visit Mrs. Winward"), 
        _("I should visit Mrs. Winward tomorrow, at the tanning shop."),
        journal_flag_delayed = True)
    notesLib["RomWinward_VisitInAWeek"] = Note(
        _("Visit Mrs. Winward in a week"), 
        _("I should visit Mrs. Winward after some time has passed."),
        journal_flag_delayed = True)
    notesLib["RomWinward_FindButtplug"] = Note(
        _("Find something for Mrs. Winward's rear"), 
        _("If I plan to get into Mrs. Winwards' backdoor, I should loosen her up with a toy first."))
    notesLib["RomWinward_PickupButtplug"] = Note(
        _("Wait for Arlena to finish her work"), 
        _("I have commissioned a special toy for Mrs. Winward. It should be ready in about a week."),
        journal_flag_delayed = True)
    notesLib["RomWinward_BringButtplug"] = Note(
        _("Give the toy to Mrs. Winward"), 
        _("I should bring the new toy to Mrs. Winward, she will certainly appreciate it."))
    notesLib["RomWinward_SetUpEveningScene"] = Note(
        _("Visit Mrs. Winward at night"), 
        _("I should visit Mrs. Winward come nightfall."))
    notesLib["RomWinward_MurderVisitGraveyardAtNight"] = Note(
        _("Visit graveyard at night"), 
        _("I should visit Mrs. Winward at the graveyard come nightfall."))
    notesLib["RomWinward_MurderVisitAtGraveyard"] = Note(
        _("Meet Mrs. Winward at the funeral"), 
        _("I should visit Mrs. Winward at the graveyard. Her husband's funeral will take place in three days."))

    @AppendToAllQuests
    class EventArlenaOrderButtplugForWinward(LogicModule):
        def __init__(self):
            super().__init__()
            
            # prog: 0 ask arlena, 1 wait for it, 2 return
            self.Arlena_ButtplugPickupDay = None # will be set to X day

        def onStart(self):
            NoteUnlock("RomWinward_FindButtplug")
            return

        def extraDialogue(self):
            if QstIsComplete(QstADazzlingTail):
                if self.progress == 0:
                    yield ("arlena_root", DNode(_("I need you to make a 'special' toy for me."), "rom_winward_plug", order = 666))
                else:
                    if self.progress == 1:
                        if self.Arlena_ButtplugPickupDay <= GetGameDay():
                            yield ("arlena_root", DNode(_("Is the toy ready?"), "rom_winward_plug_pickup", order = 666))
                        else:
                            yield ("arlena_root", DNode(_("Is the toy ready?"), "rom_winward_plug_notready", order = 666))                        

        def onComplete(self):
            NoteLock("RomWinward_BringButtplug")
            NoteLock("RomWinward_FindButtplug")
            return


    @AppendToAllQuests
    class RomanceWinward(LogicModule):
        def __init__(self):
            super().__init__()
            
            # prog: 0 is initial, 1 and further is post-jackpot

            self.SeenSecondHidesBatchScene = False

            self.CanEnterHouseAtNight = False # set true by doing jackpot

            self.RomanceVariant = None # set by the ending of the jackpot quest to:  # "control" "invest" "pimp" "divorce" "murder"

            self.DayToUnlockAnalSex = None # she will be "stretching" a day or two
            self.UnlockedAnalSex = False

            self.Invest_SeenReturnNextDayScene = False
            self.Invest_SetUpEveningScene = False # "come visit at night"

            self.Divorce_SeenReturnFewDaysLaterScene = False
            self.Divorce_SetUpEveningScene = False

            self.Divorce_FirstTimeDoingDoorScene = True # turned false after entering the scene once
            self.Divorce_DidDoorSceneToday = False # turned true onmidnight

            self.Control_SeenReturnNextDayScene = False
            self.Control_SetUpEveningScene = False
            self.Control_DidStoolSceneToday = False

            self.Pimp_SeenReturnNextDayScene = False
            self.Pimp_SetUpEveningScene = False
            self.Pimp_ChosenPimpScene = None # "markus", "threesome", "doublehj"
            self.Pimp_DayPlayerCanGetHisCut = -1

            self.Murder_FirstGraveyardScene_IsAtGraveyard = False
            self.Murder_FirstGraveyardScene_SpokeAtGraveyardAboutNightScene = False
            self.Murder_FirstGraveyardScene_TriggerGraveyardEnterSexscene = False
            self.Murder_FirstGraveyardScene_IsOver = False # controls "repeated" grave visits

            self.Murder_RepGraveyardScene_IsAtGraveyard = False
            self.Murder_RepGraveyardIsOver = False
        
            self.Murder_SeenReturnFromGraveyardScene = False
            self.Murder_DoRepeatTuesaGraveVisits = False # turned True on the return scene
            self.Murder_SetUpEveningScene = False

        def onEnter(self):  
            if GetLocID() == "novaras_dist_house":
                if CharInParty("markus"):
                    if self.Pimp_ChosenPimpScene == "markus":
                        self.Pimp_ChosenPimpScene = None
                        if IsDaytime():
                            return TriggeredEvent("rom_winward_pimp_markus_bj")

            elif GetLocID() == "novaras_dist_pleasure":
                if self.RomanceVariant == "pimp":
                    if self.Pimp_ChosenPimpScene == "doublehj":
                        self.Pimp_ChosenPimpScene = None
                        if not IsDaytime():
                            return TriggeredEvent("rom_winward_pimp_double_hj")

            elif GetLocID() == "novaras_tanner_shop":
                if not self.SeenSecondHidesBatchScene:
                    if DialogueMrsWinward().HidesBroughtIn >= 12:
                        return TriggeredEvent("nov_mrs_winward_brought_more_hides", priority = 1)

                if self.RomanceVariant == "invest":
                    if not self.Invest_SeenReturnNextDayScene:
                        if IsDaytime():
                            return TriggeredEvent("rom_winward_invest_returnnextday")
                
                elif self.RomanceVariant == "pimp":
                    if not self.Pimp_SeenReturnNextDayScene:
                        if IsDaytime():
                            return TriggeredEvent("rom_winward_pimp_returnnextday")

                    if self.Pimp_ChosenPimpScene == "threesome":
                        self.Pimp_ChosenPimpScene = None
                        if not IsDaytime():
                            return TriggeredEvent("rom_winward_pimp_threesome")

                elif self.RomanceVariant == "divorce":
                    if not self.Divorce_SeenReturnFewDaysLaterScene:
                        if IsDaytime():
                            return TriggeredEvent("rom_winward_divorce_visit_after_some_time")

                    if not IsDaytime():
                        if not self.Divorce_SetUpEveningScene:
                            rng = renpy.random.randint(1, 3)
                            if rng == 1:
                                if not self.Divorce_DidDoorSceneToday:
                                    return TriggeredEvent("rom_winward_divorce_enter_at_night")

                elif self.RomanceVariant == "control":
                    if not self.Control_SeenReturnNextDayScene:
                        if IsDaytime():
                            return TriggeredEvent("rom_winward_control_visit_next_day")
                    if self.UnlockedAnalSex == True:
                        if IsDaytime():
                            if not self.Control_DidStoolSceneToday:
                                if renpy.random.randint(1, 3) == 1:
                                    return TriggeredEvent("rom_winward_control_stool")

                elif self.RomanceVariant == "murder":
                    if not self.Murder_SeenReturnFromGraveyardScene:
                        if IsDaytime():
                            return TriggeredEvent("rom_winward_murder_after_graveyard")

            elif GetLocID() == "novaras_tanner_shop_bedroom":
                if not IsDaytime():
                    if self.Invest_SetUpEveningScene:
                        return TriggeredEvent("rom_winward_invest_visit_bedroom_miss")
                    if self.Divorce_SetUpEveningScene:
                        return TriggeredEvent("rom_winward_divorce_visit_bedroom_miss")
                    if self.Control_SetUpEveningScene:
                        return TriggeredEvent("rom_winward_control_visit_bedroom_miss")
                    if self.Murder_SetUpEveningScene:
                        return TriggeredEvent("rom_winward_murder_visit_bedroom_miss")
                    if self.Pimp_SetUpEveningScene:
                        return TriggeredEvent("rom_winward_pimp_visit_bedroom_miss")

            elif GetLocID() == "novaras_graveyard":
                if self.Murder_FirstGraveyardScene_TriggerGraveyardEnterSexscene:
                    if not IsDaytime():
                        return TriggeredEvent("rom_winward_murder_visit_at_graveyard_night")
                if self.Murder_RepGraveyardScene_IsAtGraveyard:
                    if not IsDaytime():
                        if not self.Murder_RepGraveyardIsOver:
                            return TriggeredEvent("rom_winward_murder_rep_graveyard")

        def onMidnight(self):
            if self.RomanceVariant == "pimp":
                if self.Pimp_SeenReturnNextDayScene:
                    self.Pimp_ChosenPimpScene = renpy.random.choice(["markus", "doublehj", "threesome"])
            elif self.RomanceVariant == "murder":
                if self.Murder_SeenReturnFromGraveyardScene:
                    if IsCurWeekday(WEEKDAY_MON):
                        self.Murder_RepGraveyardScene_IsAtGraveyard = True
                        self.Murder_RepGraveyardIsOver = False
            elif self.RomanceVariant == "divorce":
                self.Divorce_DidDoorSceneToday = False
            elif self.RomanceVariant == "control":
                self.Control_DidStoolSceneToday = False

            if self.DayToUnlockAnalSex is not None:
                if self.DayToUnlockAnalSex >= GetGameDay():
                    self.DayToUnlockAnalSex = None
                    self.UnlockedAnalSex = True
            return

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_house":
                # block entry till x days passed
                if self.RomanceVariant == "invest":
                    if self.delayCheck() == False:
                        btnMods["btn_tanner_shop"] = BtnJumpLabel(tra(STR_LOC.NOV_TANNER_SHOP), "rom_winward_visit_tomorrow")

                # block entry till x days passed
                elif self.RomanceVariant == "divorce":
                    if self.delayCheck() == False:
                        btnMods["btn_tanner_shop"] = BtnJumpLabel(tra(STR_LOC.NOV_TANNER_SHOP), "rom_winward_visit_give_some_time")

                # block entry till x days passed
                elif self.RomanceVariant == "control":
                    if self.delayCheck() == False:
                        btnMods["btn_tanner_shop"] = BtnJumpLabel(tra(STR_LOC.NOV_TANNER_SHOP), "rom_winward_visit_give_some_time")

                # block entry till x days passed
                elif self.RomanceVariant == "pimp":
                    if self.delayCheck() == False:
                        btnMods["btn_tanner_shop"] = BtnJumpLabel(tra(STR_LOC.NOV_TANNER_SHOP), "rom_winward_visit_tomorrow")

                elif self.RomanceVariant == "murder":
                    if self.delayCheck() == False:
                        btnMods["btn_tanner_shop"] = BtnJumpLabel(tra(STR_LOC.NOV_TANNER_SHOP), "rom_winward_visit_give_some_time")
                    if self.Murder_FirstGraveyardScene_IsAtGraveyard == True:
                        btnMods["btn_tanner_shop"] = BtnJumpLabel(tra(STR_LOC.NOV_TANNER_SHOP), "HouseLockLines")
                    if self.Murder_RepGraveyardScene_IsAtGraveyard == True:
                        if not IsDaytime():
                            if not self.Murder_SetUpEveningScene:
                                btnMods["btn_tanner_shop"] = BtnJumpLabel(tra(STR_LOC.NOV_TANNER_SHOP), "HouseLockLines")

            elif GetLocID() == "novaras_tanner_shop":
                if self.RomanceVariant == "invest" or self.RomanceVariant == "control" or self.RomanceVariant == "pimp":
                    if GetGameDay() % 3 == 0:
                        if IsDaytime():
                            btnMods["btn_talk_mr_winward"] = BtnJumpLabel(_("Talk to Mr. Winward"), "nov_mr_winward_talk")

            elif GetLocID() == "novaras_graveyard":
                if self.Murder_FirstGraveyardScene_IsAtGraveyard:
                    if self.delayCheck() == True:
                        if not self.Murder_FirstGraveyardScene_SpokeAtGraveyardAboutNightScene:
                            btnMods["btn_mrswinward"] = BtnJumpLabel(_("Talk to Mrs. Winward"), "rom_winward_murder_visit_at_graveyard")
                        else:
                            btnMods["btn_mrswinward"] = BtnJumpLabel(_("Talk to Mrs. Winward"), "rom_winward_murder_visit_at_graveyard_dont")

            return LocButtonMod(directMods = btnMods, priority = 1)

        def extraDialogue(self):
            if not self.UnlockedAnalSex:
                if PlayerItemQty("qst_winward_plug") > 0:
                    if self.DayToUnlockAnalSex is None:
                        yield ("mrs_winward_root", DNode(_("I have something for you..."), "rom_winward_plug_bring"))

            if self.RomanceVariant == "invest":
                if self.Invest_SeenReturnNextDayScene == True:
                    if not self.Invest_SetUpEveningScene:
                        yield ("mrs_winward_root", DNode(_("Your bull is here for some {i}'milking.'{/i}"), "rom_winward_invest_initiate_sex"))
                yield ("mr_winward_root", DNode(_("How are you?"), "dialogue_mr_winward_invest_howareyou"))
                yield ("mr_winward_root", DNode(_("We should discuss your wife..."), "dialogue_mr_winward_invest_discusswife"))

            elif self.RomanceVariant == "pimp":
                if self.Pimp_SeenReturnNextDayScene == True:
                    if not self.Pimp_SetUpEveningScene:
                        yield ("mrs_winward_root", DNode(_("Your bull is here for some {i}'milking.'{/i}"), "rom_winward_pimp_initiate_sex"))
                yield ("mr_winward_root", DNode(_("I'm here to get my cut of the earnings..."), "dialogue_mr_winward_pimp_cut"))
                yield ("mr_winward_root", DNode(_("How are you?"), "dialogue_mr_winward_pimp_howareyou"))
                yield ("mr_winward_root", DNode(_("We should discuss your wife..."), "dialogue_mr_winward_pimp_discusswife"))

            elif self.RomanceVariant == "divorce":
                if self.Divorce_SeenReturnFewDaysLaterScene == True:
                    if not self.Divorce_SetUpEveningScene:
                        yield ("mrs_winward_root", DNode(_("Your bull is here for some {i}'milking.'{/i}"), "rom_winward_divorce_initiate_sex"))
            
            elif self.RomanceVariant == "control":
                if self.Control_SeenReturnNextDayScene == True:
                    if not self.Control_SetUpEveningScene:
                        yield ("mrs_winward_root", DNode(_("Your bull is here for some {i}'milking.'{/i}"), "rom_winward_control_initiate_sex"))
                yield ("mr_winward_root", DNode(_("How are you?"), "dialogue_mr_winward_control_howareyou"))
                yield ("mr_winward_root", DNode(_("We should discuss your wife..."), "dialogue_mr_winward_control_discusswife"))

            elif self.RomanceVariant == "murder":
                if self.Murder_SeenReturnFromGraveyardScene == True:
                    if not self.Murder_SetUpEveningScene:
                        yield ("mrs_winward_root", DNode(_("Your bull is here for some {i}'milking.'{/i}"), "rom_winward_murder_initiate_sex"))

            if PregWinward().NumBirths > 0:
                if RomanceWinward().RomanceVariant == "invest":
                    yield ("mrs_winward_root", DNode(_("How is our child?"), "rom_winward_invest_how_is_our_child"))
                elif RomanceWinward().RomanceVariant == "divorce":
                    yield ("mrs_winward_root", DNode(_("How is our child?"), "rom_winward_divorce_how_is_our_child"))
                elif RomanceWinward().RomanceVariant == "control":
                    yield ("mrs_winward_root", DNode(_("How is our child?"), "rom_winward_control_how_is_our_child"))
                elif RomanceWinward().RomanceVariant == "murder":
                    yield ("mrs_winward_root", DNode(_("How is our child?"), "rom_winward_murder_how_is_our_child"))
                elif RomanceWinward().RomanceVariant == "pimp":
                    yield ("mrs_winward_root", DNode(_("How is our child?"), "rom_winward_pimp_how_is_our_child"))


    
label rom_winward_visit_tomorrow:
    MC "(I should visit Mrs. Winward tomorrow.)"
    $ LocEnterQ()

label rom_winward_visit_give_some_time:
    MC "(I should give Mrs. Winward some time.)"
    $ LocEnterQ()

label rom_winward_murder_not_at_home:
    MC "(It doesn't seem like Mrs. Winward is at home.)"
    $ LocEnterQ()