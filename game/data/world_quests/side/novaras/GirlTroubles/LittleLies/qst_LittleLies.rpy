init python:
    notesLib["LittleLiesNote"] = Note(
        _("Information about Rhuvan, the white bear"),
        _("I feel like I've heard of this bear that Sister Divine mentioned, I might end up meeting it during an expedition on the way to Lake Balun."))
    @AppendToAllQuests
    class QstLittleLies(BaseQuest):
        TITLE = _("Little lies")
        DESCRIPTION = _("Mika didn't seem to be telling me the truth, so I'd better investigate.")
        GOALS = {
            0: QuestStage(_("Finding Mika"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("Mika must be in the Tower of Palam somewhere?")),
            1: QuestStage(_("Finding Mika, again..."), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("Mika must be in the Tower of Palam somewhere?")),
            2: QuestStage(_("Talk to Mika"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("Mika must be in the Palam Tower dormitory")),
            3: QuestStage(_("Talk to Sister Divine"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I need to convince Divine to give Mika what she wants")),
            4: QuestStage(_("Talk to Mika"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("Now I have to tell Mika the good news, she must be in the Palam Tower dormitory")),
            4.1: QuestStage(_("Meet Mika and Sister Divine"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("Well, Mika told me I could meet her at the bathhouse in the evening")),
            5: QuestStage(_("Meet Mika"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("Mika should be waiting for me in the classroom, I'll stop by during the day")),
            6: QuestStage(_("Finding Mika"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I need to find Mika and understand this whole situation, she must be somewhere in Palam's tower")),
            7: QuestStage(_("Meet Mika"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I'm supposed to meet Mika at the Palam Tower arena around morning")),
            8: QuestStage(_("I need to have a serious talk with Mika"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("Mika must be in the Palam Tower dormitory, I should be there in the evening")),
            8.1: QuestStage(_("Meet Mika at the Iron Unicorn"), trackTag = "btn_novaras_tavern", hintTxt = _("Well, I must meet Mika at the Iron Unicorn in the evening")),
            }

        def __init__(self):# IsMorning()
            super().__init__()
    
            self.XpReward = 550
            self.mikaOfferedCost = False
            self.persuasionCost = 20000
            self.persuasionPaid = False
            self.mikaGotFarmingPatch = False
            self.mikaWillHaveHerDate = False
            self.divinePersuasionCost = 2500
            self.divinePersuasionPaid = False
            self.divineWantsRhuvansHide = False
            self.divineGotRhuvanHide = False
            self.mikaToldAboutHerDivineCrush = False
            self.askToGoOutWithMika = False
            self.askToGiveMikaTheFarmingPatch = False
            self.mikaXDivineSceneSkipped = None
            self.block_dorm_day = None

            self.GoalStates[4.1] = GoalState.OFF
            self.GoalStates[8.1] = GoalState.OFF

            self.suggestedLevel = 7

        def isDormBlocked(self):
            if self.block_dorm_day == GetGameDay():
                return True
            else:
                return False

        def onEnter(self):  
            if GetLocID() == "novaras_palam_bath":
                if IsEvening():
                    if self.progress == 4.1:
                        return TriggeredEvent("qst_little_lies_bathhouse_scene")
            elif GetLocID() == "novaras_palam_dorm":
                if self.progress == 6:
                    return TriggeredEvent("qst_little_lies_class_meet_2")
                if self.progress == 8:
                    if IsEvening():
                        return TriggeredEvent("qst_little_lies_class_meet_4")
            elif GetLocID() == "novaras_tavern":
                if IsEvening():
                    if self.progress == 8.1:
                        return TriggeredEvent("qst_little_lies_class_meet_5")

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_palam_garden":
                if self.progress == 0:
                    btnMods["btn_palam_garden_mika_talk_btn"] = BtnJumpLabel(_("Talk to Mika"), "qst_little_lies_on_enter_1")
            elif GetLocID() == "novaras_palam_dorm":
                if self.progress == 1:
                    btnMods["btn_palam_dorm_mika_talk_btn"] = BtnJumpLabel(_("Talk to Mika"), "qst_little_lies_on_enter_2")
                if self.progress in [2, 3, 4]:
                    btnMods["btn_palam_dorm_mika_talk_btn"] = BtnJumpLabel(_("Talk to Mika"), "qst_little_lies_on_enter_3")
            elif GetLocID() == "novaras_palam_class":
                if self.progress == 5:
                    if IsDaytime():
                        btnMods["btn_palam_class_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_little_lies_class_meet")
            elif GetLocID() == "novaras_palam_arena":
                if self.progress == 7:
                    if IsDawnToNoon():
                        btnMods["btn_palam_arena_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_little_lies_class_meet_3")
            elif GetLocID() == "novaras_palam_e_wing": 
                if self.isDormBlocked():
                    btnMods["btn_palam_e_wing_to_dorm"] = BtnJumpLabel(
                        STR_LOC.NOV_PALAM_DORM, "qst_little_lies_dorm_blocked")
            return LocButtonMod(directMods = btnMods)
    
        def onComplete(self):
            QstStart(QstTheMagesPath)
            NoteLock("LittleLiesNote")
            return

        def extraDialogue(self):
            if self.divineWantsRhuvansHide:
                if self.divineGotRhuvanHide == False:
                    yield ("divine_root", DNode(_("About the Rhuvan..."), "qst_girl_troubles_about_rhuvan"))