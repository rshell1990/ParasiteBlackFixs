init python:
    @AppendToAllQuests
    class QstTheLoversPath(BaseQuest):
        TITLE = _("The lover's path")
        DESCRIPTION = _("Mika and I are no longer just student and teacher, we're lovers. I think our lessons from now on will be interesting to say the least.")

        GOALS = {
            0: QuestStage(_("Continuing Mika's training"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I'm supposed to meet Mika at the Palam Tower arena around morning to continue our training")),
            1: QuestStage(_("Meet Mika at the arena again"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("Our last class was quite interesting... anyway, I'm supposed to meet Mika at the Palam Tower arena around morning to continue our training")),
            2: QuestStage(_("Meet Mika in the girls' dormitory"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I'm supposed to meet Mika at the girls' dormitory around morning")),
            3: QuestStage(_("Meet Mika at the arena again"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I'm supposed to meet Mika at the Palam Tower arena around morning to continue our training")),
            }

        def __init__(self):
            super().__init__()
    
            self.XpReward = 250

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_palam_arena":
                if IsDawnToNoon():
                    if self.progress == 0:
                        btnMods["btn_palam_arena_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_the_lovers_path_meet_1")
                    elif self.progress == 1:
                        if self.delayCheck():
                            btnMods["btn_palam_arena_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_the_lovers_path_meet_2")
                    elif self.progress == 3:
                        if self.delayCheck():
                            btnMods["btn_palam_arena_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_the_lovers_path_meet_4")
            elif GetLocID() == "novaras_palam_dorm":
                if IsDawnToNoon():
                    if self.progress == 2:
                        btnMods["btn_palam_dorm_mika_talk_btn"] = BtnJumpLabel(_("Talk to Mika"), "qst_the_lovers_path_meet_3")
            return LocButtonMod(directMods = btnMods)

        def onComplete(self):
            # canon is, mc takes mika for himself
            if not CharIsLover("mika"):
                CharSetLover("mika", Silent = True)
                CharChangeRel("mika", 1)
            QstStart(QstLetsCelebrate)
            return