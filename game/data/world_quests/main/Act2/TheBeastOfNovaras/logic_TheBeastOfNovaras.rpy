init python:
    @AppendToAllQuests
    class PrimerTheBeastOfNovaras(LogicModule):
        def __init__(self):
            super().__init__()

            self.Kind = 0 # 0 is "good morning" 1 is "walk-in"

        def onEnter(self):  
            if GetLocID() == "hamun_hookah_bar_room":
                self.Kind = 0
            elif GetLocID() == "hamun_dist_docks":
                self.Kind = 1
            elif GetLocID() == "hamun_hookah_bar":
                if IsDaytime():
                    if self.Kind == 0:
                        return TriggeredEvent("qst_TheBeastOfNovaras_IntroWakeUp")
                    elif self.Kind == 1:
                        return TriggeredEvent("qst_TheBeastOfNovaras_IntroWalkIn")
            return

    @AppendToAllQuests
    class QstTheBeastOfNovaras(BaseQuest):
        TITLE = _("The Beast of Novaras")
        DESCRIPTION = _("I have been tasked by Garen, a member of The Greater Trading Company, to persuade Lord Zanzibat to step aside and allow a lucrative trade deal to pass...")
        GOALS = {
                0: QuestStage(_("Go to the Arena"),             hintTxt = _("Lord Zanzibat frequents the arena in Hamun. Perhaps I might be able to catch his eye there?")),
                1: QuestStage(_("Reach the rank of Sun Forged"),hintTxt = _("It seems I will need to at least clear through the arena ranks of {i}Sun Forged{/i} in the Hamun arena before I can tempt Zanzibat to the arena.")),
                2: QuestStage(_("Speak to Yarrick"),            hintTxt = _("I have reached Sun-forged rank at the arena. I should return to Yarrick when I can...")),
                3: QuestStage(_("Let Yarrick set up the fight"),hintTxt = _("I have talked to Yarrick after reaching the Sun Forged rank at the Hamun arena. Now he wants to set up a special fight for me, which will surely attract Lord Zanzibat's attention.\nHe said it will take three days.")),
                4: QuestStage(_("Defeat the Caltrack"),         hintTxt = _("The special battle Yarrick had set up for me is against a monstrous being, Caltrack. Time to earn us an audience...")),
                5: QuestStage(_("Return to Yarrick"),         hintTxt = _("I have defeated the monster Yarrick set me up against. That should get us an audience with Zanzibat.")),
                6: QuestStage(_("Head to Lord Zanzibat's home"), trackTag = "hamun_dist_merch_lord_to_zanzibat_house", hintTxt = _("While I was out, Lord Zanzibat had already made the arrangements to meet me. I can find his house outside the great palace.")),
                7: QuestStage(_("Report to Garen"), trackTag = "hamun_docks_to_hookah_bar", hintTxt = _("I have spoken to Lord Zanzibat on Greater Trading Company's behalf. I should return to Garen and report on the terms I have managed to arrange.")),
                8: QuestStage(_("Meet Sypha at the market, night time"), trackTag = "hamun_docks_to_market", hintTxt = _("Sypha has invited me on a 'date' in the night market in return for information... I should be careful, who knows what she's planning?")),
            }

        def __init__(self):
            super().__init__()
        
            self.IsMain = True
            self.XpReward = 700
            self.suggestedLevel = 10
            self.YarrickSetsUpTheFightDay = -1
            self.BoughtLocket = False

        def onEnter(self):  
            if GetLocID() == "hamun_arena_ext":
                if IsDaytime():
                    if self.progress == 0:
                        return TriggeredEvent("qst_TheBeastOfNovaras_ApproachArena") 
                    elif self.progress == 5:
                        return TriggeredEvent("qst_TheBeastOfNovaras_ReturnToYarrickAfterCaltrack")
            elif GetLocID() == "hamun_market":
                if self.progress == 8:
                    if not IsDaytime():
                        return TriggeredEvent("qst_TheBeastOfNovaras_SyphaDate")
            return

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_arena_ext":
                if IsDaytime():
                    if self.progress == 1:
                            btnMods["btn_hamun_arena_ext_yarrick_talk"] = BtnJumpLabel(_("Talk to Yarrick"), "qst_TheBeastOfNovaras_SpeakToYarrickBeforeSunForged")
                    elif self.progress == 2:
                            btnMods["btn_hamun_arena_ext_yarrick_talk"] = BtnJumpLabel(_("Talk to Yarrick"), "qst_TheBeastOfNovaras_SpeakToYarrickSunForged")
                    elif self.progress == 3:
                            btnMods["btn_hamun_arena_ext_yarrick_talk"] = BtnJumpLabel(_("Talk to Yarrick"), "qst_TheBeastOfNovaras_SpeakToYarrickFightSetup")
            elif GetLocID() == "hamun_dist_merch_lord":
                if self.progress == 6:
                    if IsDaytime():
                        btnMods["hamun_dist_merch_lord_to_zanzibat_house"] = BtnJumpLabel(STR_LOC.HAMUN_ZANZIBAT_HOUSE, "qst_TheBeastOfNovaras_ZanzibatHouse")
                    else:
                        btnMods["hamun_dist_merch_lord_to_zanzibat_house"] = BtnJumpLabel(STR_LOC.HAMUN_ZANZIBAT_HOUSE, "qst_TheBeastOfNovaras_ZanzibatHouse_returnatday")
            elif GetLocID() == "hamun_hookah_bar":
                if IsDaytime():
                    if self.progress <= 7:
                        btnMods["btn_hamun_hookah_bar_garen"] = BtnJumpLabel(_("Talk to Garen"), "qst_TheBeastOfNovaras_TalkToGarenBar")
                
            return LocButtonMod(directMods = btnMods, priority = 1)

        def onStart(self):
            QstComplete(PrimerTheBeastOfNovaras)
            QstStart(DialogueSypha)
            PartyAddChar("sypha")
            PlayerAddItem("xeriya_spear", Silent = True)
            PlayerAddItem("xeriya_armor", Silent = True)
            PlayerPartyCharEquipItem("sypha", "xeriya_spear")
            PlayerPartyCharEquipItem("sypha", "xeriya_armor")
            return

        def onComplete(self):
            QstStart(HouseLockZanzibatHouse)

            if can_unlock_achievement("A_BEAST_OR_SAVIOR"):
                unlock_achievement("A_BEAST_OR_SAVIOR")
            return

        def onOver(self):
            QstStart(PrimerTheTarbecks)
            QstSetDelay(PrimerTheTarbecks, 2)
            QstStart(PrimerBigTroubleLH)
            QstStart(DialogueZanzibat)
            QstStart(PrimerDreamhouse)
            return

image cg_para_ship_hive_lord_anim = Movie(
    start_image = "images/cgs/beast_of_novaras/cg_para_ship_start.webp",
    play = "images/cgs/beast_of_novaras/cg_para_ship.webm")

image cg_sypha_wine_bathhouse_anim = Movie(
    start_image = "images/cgs/beast_of_novaras/cg_sypha_wine_bathhouse_start.webp",
    play = "images/cgs/beast_of_novaras/cg_sypha_wine_bathhouse.webm")

image cg_sypha_tease_anim = Movie(
    start_image = "images/cgs/beast_of_novaras/cg_sypha_tease_start.webp",
    play = "images/cgs/beast_of_novaras/cg_sypha_tease.webm")

image cg_savage_kain:
    "cg_savage_kain_base"
    yoffset 150
    zoom 0.96

image cg_savage_kain_dead:
    "cg_savage_kain_dead_base"
    yoffset 270
    zoom 0.9