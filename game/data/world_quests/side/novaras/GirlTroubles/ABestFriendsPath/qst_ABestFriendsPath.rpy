init python:
    @AppendToAllQuests
    class QstABestFriendsPath(BaseQuest): 
        TITLE = _("A best friend's path")
        DESCRIPTION = _("Even though I didn't return Mika's feelings, I believe Markus would definitely want to. And since I'm a good friend, I'll be the bridge between the two lovebirds.")

        GOALS = {
            0:QuestStage(_("Talk to Markus about Mika"),        hintTxt = _("I should discuss Mika with Markus... Not in the tower, obviously.")),
            1:QuestStage(_("Give Mika and Markus some time"),   hintTxt = _("Now that the two have met, I should give them some room. I should check up on them tomorrow.")),
            2:QuestStage(_("Train Mika at the arena"),          trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I'm supposed to meet Mika at the Palam Tower arena for a daily training session.\nShe will wait for me there early in the day.\nShould she fail, we will have to try again another day...")),
            3:QuestStage(_("Check up on Markus and Mika in the evening"),       hintTxt = _("I should check up on the two lovebirds. I am quite certain I can find them at Palam tower, evening time.")),
            4:QuestStage(_("Train Mika at the arena"),          trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I'm supposed to meet Mika at the Palam Tower arena for a daily training session.\nShe will wait for me there early in the day.\nShould she fail, we will have to try again another day...")),
            5:QuestStage(_("Check up on Markus and Mika in the evening again"), hintTxt = _("I should check up on the two lovebirds. I am quite certain I can find them at Palam tower, evening time.")),
            6:QuestStage(_("Train Mika at the arena"),          trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I'm supposed to meet Mika at the Palam Tower arena for a daily training session.\nShe will wait for me there early in the day.\nShould she fail, we will have to try again another day...")),
            7:QuestStage(_("Meet Mika and Markus at the Iron Unicorn"),         hintTxt = _("I should meet up with Mika and Markus for the celebration of sorts, at the Iron Unicorn. They will be waiting for me after dark.")),
            8:QuestStage(_("Check up on Mika"),                 hintTxt = _("I should catch up with Mika after that celebration we've had. I can find her at the Palam tower, early in the day.")),
            9:QuestStage(_("Train Mika one last time"),         trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I should give Mika some time. Then, we'll have that last training session.\nShe will wait for me at the arena, early in the day.")),
        }

        def __init__(self):
            super().__init__()

            self.XpReward = 600 # a sum of loverspath and letscelebrate


        def onEnter(self):  
            if self.progress == 1:
                if GetLocID() == "novaras_palam_mainhall":
                    if self.delayCheck():
                        return TriggeredEvent("qst_a_best_friends_path_3")
            elif self.progress == 3:
                if GetLocID() == "novaras_palam_e_wing":
                    if IsInTimeFrame(TIME_DAY_END, TIME_LATENIGHT):
                        return TriggeredEvent("qst_a_best_friends_path_5")
            elif self.progress == 5:
                if GetLocID() == "novaras_palam_e_wing":
                    if IsInTimeFrame(TIME_DAY_END, TIME_LATENIGHT):
                        return TriggeredEvent("qst_a_best_friends_path_7")
            elif self.progress == 7:
                if GetLocID() == "novaras_tavern":
                    if not IsDaytime():
                        return TriggeredEvent("qst_a_best_friends_path_9")
            elif self.progress == 8:
                if GetLocID() in ["novaras_palam_e_wing", "novaras_palam_w_wing"]:
                    if IsInTimeFrame(TIME_DAY_START, TIME_DUSK):                
                        return TriggeredEvent("qst_a_best_friends_path_10")

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_palam_arena":
                if IsDawnToNoon():
                    if self.progress == 2:
                        btnMods["btn_palam_arena_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_a_best_friends_path_4")
                    elif self.progress == 4:
                        btnMods["btn_palam_arena_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_a_best_friends_path_6")
                    elif self.progress == 6:
                        btnMods["btn_palam_arena_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_a_best_friends_path_8")
                    elif self.progress == 9 and self.delayCheck():
                        btnMods["btn_palam_arena_mika_talk"] = BtnJumpLabel(_("Talk to Mika"), "qst_a_best_friends_path_12")

            return LocButtonMod(directMods = btnMods)

        def onComplete(self):
            QstStart(EventMikaMarkusRepScenes)

            GoalComplete(QstGirlTroubles, 2)
            GoalShow(QstGirlTroubles, 3)
            
            QstGirlTroubles().mika_training_done = True

            ## crutchy fix for wrong qst completed numbers
            QstLetsCelebrate().isOver = True
            QstLetsCelebrate().isComplete = True
            QstLetsCelebrate().FinishOrder = store.QuestsFinished
            QstLetsCelebrate().QuestOverShowInHistory = False
            store.QuestsFinished += 1

            QstTheLoversPath().isOver = True
            QstTheLoversPath().isComplete = True
            QstTheLoversPath().FinishOrder = store.QuestsFinished
            QstTheLoversPath().QuestOverShowInHistory = False
            store.QuestsFinished += 1
            return


image cg_drunkard_dark:
    "images/characters/swindler/normal.webp"
    matrixcolor BrightnessMatrix(-1.0)

init python:
    config.tag_layer["cg_drunkard_dark"] = "characters"