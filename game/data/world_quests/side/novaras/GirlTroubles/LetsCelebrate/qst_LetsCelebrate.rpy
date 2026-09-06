init python:
    @AppendToAllQuests
    class QstLetsCelebrate(BaseQuest):
        TITLE = _("Let's celebrate")
        DESCRIPTION = _("Mika's training is almost complete, she's really improved a lot, I think it's time I gave her a reward.")

        GOALS = {
            0: QuestStage(_("Meet Mika at the Market"), trackTag = "btn_novaras_market_stalls", hintTxt = _("I should meet Mika at the market around morning")),
            1: QuestStage(_("Meet Mika at the Iron Unicorn"), trackTag = "btn_novaras_tavern", hintTxt = _("Well, I must meet Mika at the Iron Unicorn in the evening")),
            2: QuestStage(_("Meet Mika at the Palam tower"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("It's best to see her in the morning, so she has more time to calm down")),
            3: QuestStage(_("Meet Mika in the Tower of Palam rooftop gardens"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I must meet Mika at the rooftop gardens around morning")),
            4: QuestStage(_("Meet Mika in the girls' dormitory"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I'm supposed to meet Mika at the girls' dormitory in the evening")),
            5: QuestStage(_("Meet Mika at the arena"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("It's time to give Mika his final training, I guess that's part of the celebration in a sense. I'm supposed to meet Mika at the Palam Tower arena around morning")),
            }

        def __init__(self):
            super().__init__()
        
            self.XpReward = 350

        def onEnter(self):  
            if GetLocID() == "novaras_market_stalls":
                if IsDawnToNoon():
                    if self.progress == 0:
                        return TriggeredEvent("qst_lets_celebrate_meet_0")
            elif GetLocID() == "novaras_palam_mainhall":
                if IsDawnToNoon():
                    if self.progress == 2:
                        return TriggeredEvent("qst_lets_celebrate_meet_2")
            elif GetLocID() == "novaras_palam_dorm":
                if IsEvening():
                    if self.progress == 4:
                        return TriggeredEvent("qst_lets_celebrate_meet_4")

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_tavern":
                if self.progress == 1:
                    if IsEvening():
                        btnMods["btn_novaras_tavern_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_lets_celebrate_meet_1")
            elif GetLocID() == "novaras_palam_garden":
                if self.progress == 3:
                    if IsDawnToNoon():
                        btnMods["btn_palam_garden_mika_talk_btn"] = BtnJumpLabel(_("Talk to Mika"), "qst_lets_celebrate_meet_3")
            elif GetLocID() == "novaras_palam_arena":
                if self.progress == 5:
                    if IsDawnToNoon():
                        btnMods["btn_palam_arena_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_lets_celebrate_meet_5")
            return LocButtonMod(directMods=btnMods)

        def onComplete(self):
            QstStart(RomanceMika)
            GoalComplete(QstGirlTroubles, 2)
            GoalShow(QstGirlTroubles, 3)
            QstGirlTroubles().mika_training_done = True

            # for "completed quest count"
            QstABestFriendsPath().isOver = True
            QstABestFriendsPath().isComplete = True
            QstABestFriendsPath().FinishOrder = store.QuestsFinished
            QstABestFriendsPath().QuestOverShowInHistory = False
            store.QuestsFinished += 1

            return