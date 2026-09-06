init python:
    notesLib["GirlTroublesNote"] = Note(
        _("Message from Sister Divine"),
        _("I should stop by the tower of Palam and talk to Sister Divine when I get a chance."))
    @AppendToAllQuests
    class PrimerGirlTroubles(LogicModule):
        def __init__(self):
            super().__init__()
            # prog 0 is receive message on street,
            # 1 is talk to divine in her office,
            # 2 is talk to divine in main hall

        def onEnter(self):
            if GetLocID() in LocIDList_NovarasCityStreets:
                if IsDaytime():
                    if QstIsOver(QstHighFasion):
                        if self.progress == 0:
                            return TriggeredEvent("primer_girl_troubles_1")
            elif GetLocID() == "novaras_palam_divine_office":
                if self.progress == 1:
                    return TriggeredEvent("primer_girl_troubles_2")

        def extraDialogue(self):
            if self.progress == 2:
                yield ("divine_root", DNode(_("Continuing our conversation about the girls..."), "primer_girl_troubles_2_menu_repeat", order = 100))

        def locationMod(self):
            btnMods = {}
            if self.progress == 1:
                if GetLocID() == "novaras_palam_mainhall":
                    btnMods["btn_palam_mainhall_talk_divine"] = BtnDisabled()
            return LocButtonMod(directMods = btnMods, priority = 1)

        def onComplete(self):
            QstStart(QstGirlTroubles)
            return

    @AppendToAllQuests
    class QstGirlTroubles(BaseQuest):
        TITLE = _("Girl troubles")
        DESCRIPTION = _("Sister Divine asked me to help her deal with the mages of Palam. I have no idea what awaits me.")
        # WARNING, after EITHER of new wip goals are in, after_load routine that ends the quest will need an update.
        # like re-initialize this quest? or what?
        GOALS = {
            0: QuestStage(_("(WIP) Deal with Jana's troublesome behaviour"), 
                hintTxt = _("(WIP) Jana's reckless behaviour needs to be dealt with... I have to uncover the cause.")),
            1: QuestStage(_("(WIP) Investigate Zara and her outbursts"), 
                hintTxt = _("(WIP) I must discover the cause of Zara's rampage before it happens again.")),
            2: QuestStage(_("Help Mika overcome her fear of battle"), 
                hintTxt = _("I must help Mika overcome her fear of battle. As Sister Divine put it, Mika is {i}afraid of her own shadow{/i}.")),
            3: QuestStage(_("Report your progress to Divine"), 
                hintTxt = _("The training with Mika has finally come to an end, so now I have to report my progress to Sister Divine.")),
        }

        SIMPLE_GOALS = False

        def __init__(self):
            super().__init__()
        
            self.XpReward = 550
            self.mika_training_done = False

        def extraDialogue(self):
            yield ("divine_root", DNode(_("I need to talk about one of the girls..."), "qst_girl_troubles_main_label", order = 100))


        def onStart(self):
            GoalShow(self, 0)
            GoalShow(self, 1)
            GoalShow(self, 2)

            # QstRebelYell # not yet available
            # QstThePerfectGirl # not yet available
            QstStart(QstLittleLies)
