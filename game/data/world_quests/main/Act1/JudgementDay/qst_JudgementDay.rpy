init python:
    @AppendToAllQuests
    class QstJudgementDay(BaseQuest):
        TITLE = _("Judgement Day")
        DESCRIPTION = _("At last, the Demorai army is at our gates. I must defend the city, no matter the cost...")
        GOALS = {
            # the top one is highest order to sort in journal, that's all
            100: QuestStage(_("Defend Novaras"), hintTxt = _("I must help people of Novaras repel the Demorai assault.")),

            10: QuestStage(_("Disperse the crowd"), hintTxt = _("A crowd is forming in the Market District. Captain Nyx needs me to deal with it, before the Demorai artillery does.")),
            20: QuestStage(_("Find Markus"), hintTxt = _("If I am to do any good here, I need to find Markus. Together, we might have a chance....")),
            30: QuestStage(_("Rescue the mages"), hintTxt = _("Sister Divine wants me to rescue a group of mages. I should be able to find them in the south-eastern district.")),
            35: QuestStage(_("Find Prince Naran"), hintTxt = _("Princess Cecilia has tasked me with finding her younger brother, Prince Naran.")),
            40: QuestStage(_("Get to the south-eastern wall"), hintTxt = _("I must get to the south-eastern wall: something is disrupting the supplies there.")),
            50: QuestStage(_("Defeat Zanarak"), hintTxt = _("I have met Zanarak again. This time, we will beat him. Or die trying.")),

            # 110 to display higher than def. novaras
            110: QuestStage(_("Win the trial"), hintTxt = _("For doing my best to protect the city during the siege I now stand trial, facing absurd charges. I will do my best to make it through this mess...")),
        }

        def __init__(self):
            super().__init__()

            self.XpReward = 800
            self.suggestedLevel = 9
            self.IsMain = True
            self.PlayerPrepared = False # set to True in the end of thecomingstorm quest
            # will store all char IDs of all chars (Except mc) who were in party during that sequence
            self.CharactersWhoWereAtTheWall = set()
            # post-trial, stores char ids who are still in there
            self.ImprisonedCharacters = set()
            self.TrialPoints = {"pos":0, "neg":0}

        def onComplete(self):
            renpy.hide("vignette_neg")
            renpy.hide("vignette_pos")            

            InfGainDaily(True)
            AutoTimeFreeze(False)
            BlockWaitGlobal(False)
            WorldMapLocAdd("ves_camp")

            QstStart(DialogueKatiya)
            QstStart(DialogueNuma)
            QstStart(DialogueEsme)
            QstStart(DialogueRania)

            QstStart(HouseLockHamunStore)
            QstStart(EventPlayerBanishedFromNovaras)
            QstStart(HouseLockHamunBrothel)
            QstStart(HouseLockHamunBrothelRoom)
            
            QstStart(DialogueMarbella)
            QstStart(HouseLockHamunSmithy)
            QstStart(DialogueBeshar)

            CharAltFormUnlock("kiara")
            TransformMC(False)
            TransformMarkus(False)
            TransformKiara(False)
            TransformElena(False)

            if can_unlock_achievement("THE_SECOND_SIEGE_OF_NOVARAS"):
                unlock_achievement("THE_SECOND_SIEGE_OF_NOVARAS")

            QstStart(EventAdaraDreamAct2Start)
            QstStart(EventCrashedShipEncounter)

            # this is more like save compat thing 
            # for the cases where they saved BEFORE completing the quest but AFTER meeting chars / seeing them die
            if not CharIsMet("alysha"):
                if QstIsOver(QstTheSlavemaster):
                    if not QstTheSlavemaster().AlyshaDead:
                        worldChars["alysha"] = PBCharacter("alysha")
                        CharMeet("alysha", Silent = True)

            # same as above
            if not CharIsMet("marion"):
                CharMeet("marion", Silent = True, DefaultRel = "rel_enemy")

            # sophira dead 
            if not CharIsAlive("sophira"):
                CharAddRelEntry("sophira", "died_during_siege")

            # stop prophetizing
            QstComplete(EventMadProphet)

            # (this is being added later) more act2 stuff
            QstStart(DialogueLuna)
            QstStart(DialogueKiara)
            QstStart(PrimerTheBeastOfNovaras)
            QstStart(HamunArena)
            QstStart(DialogueGiselra)
            return

        def CourtPositive(self, Amount = 1):
            self.TrialPoints["pos"] += Amount
            renpy.music.play("audio/cfx/trial_positive.ogg", channel = "sound")
            renpy.hide("vignette_pos", layer = "screens")
            renpy.show("vignette_pos", at_list=[FX_FadeOutCourtOverlay], layer="screens", zorder = -5)
            if config.developer:
                renpy.say(None, "DEBUG: current pts (%s pos -- %s neg)" % (self.TrialPoints["pos"], self.TrialPoints["neg"]))
            return

        def CourtNegative(self, Amount = 1):
            self.TrialPoints["neg"] += Amount
            renpy.music.play("audio/cfx/trial_negative.ogg", channel = "sound")
            renpy.hide("vignette_neg", layer = "screens")
            renpy.show("vignette_neg", at_list=[FX_FadeOutCourtOverlay], layer="screens", zorder = -5)
            if config.developer:
                renpy.say(None, "DEBUG: current pts (%s pos -- %s neg)" % (self.TrialPoints["pos"], self.TrialPoints["neg"]))
            return

    @AppendToAllQuests
    class EventPlayerBanishedFromNovaras(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_gates":
                btnMods["btn_novaras_gates_enter_city"] = BtnJumpLabel(STR_LOC.NOV_GATES, "ev_PlayerBanishedFromNovaras_Lines")
            return LocButtonMod(directMods = btnMods, priority = 1)

transform FX_FadeOutCourtOverlay:
    ease 1.0 alpha 0.0

label ev_PlayerBanishedFromNovaras_Lines:
    show mc sad at cright_f with easeinright
    "Looking at the walls of the city, I felt immense longing engulf me."
    MC @sad "(...No point coming any closer.)"
    MC @sad "(Being banished, I cannot enter the city.)"
    $ LocEnter()