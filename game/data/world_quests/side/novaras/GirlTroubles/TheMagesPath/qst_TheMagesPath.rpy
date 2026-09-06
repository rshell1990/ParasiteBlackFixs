init python:
    @AppendToAllQuests
    class QstTheMagesPath(BaseQuest):
        TITLE = _("The mage's path")
        DESCRIPTION = _("Now that I know Mika's past, I think we'll get along better from now on. Now we'll start her true training.")
        GOALS = {
            0: QuestStage(_("Meet Mika at the arena"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I'm supposed to meet Mika at the Palam Tower arena for a daily training session.\nShould she fail, we will have to try again another day...")),
            1: QuestStage(_("Meet Mika at the arena again"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("Our last class was quite interesting... anyway, I'm supposed to meet Mika at the Palam Tower arena for a daily training session.\nShould she fail, we will have to try again another day...")),
            2: QuestStage(_("Meet Mika at the arena for another training section"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I'm supposed to meet Mika at the Palam Tower arena for a daily training session.\nShould she fail, we will have to try again another day...")),
            3: QuestStage(_("Walk around the city"), hintTxt = _("Since we didn't have class today, I think I'll take a walk around the city")),
            4: QuestStage(_("Speak to Mika"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I need to understand how Mika really feels and how I feel about it. I should meet her at the Palam Tower arena.")),
        }

        def __init__(self):
            super().__init__()

            self.XpReward = 250
            self.mcTalkedAboutTheButtplug = False
            self.mikaWetDreamSkipped = None
            self.AvertedGazeDuringBPScene = False

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_palam_arena":
                if IsDaytime():
                    if self.delayCheck():
                        if self.progress == 0:
                            btnMods["btn_palam_arena_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_the_mages_path_meet_1")
                        elif self.progress == 1:
                            btnMods["btn_palam_arena_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_the_mages_path_meet_2")
                        elif self.progress == 2:
                            btnMods["btn_palam_arena_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_the_mages_path_meet_3")
                        elif self.progress == 4:
                            btnMods["btn_palam_arena_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_the_mages_path_meet_5")
            return LocButtonMod(directMods = btnMods)

        def onEnter(self):  
            if GetLocID() == "novaras_dist_market":
                if self.progress == 3:
                    return TriggeredEvent("qst_the_mages_path_meet_4")

