init python:
    @AppendToAllQuests
    class QstTheDarkPass(BaseQuest):
        GOALS = {
            0: QuestStage(_("March out"), hintTxt = _("We are to form ranks and to head out of the city. Our path lies across {i}the Valley of Death{/i}.")),
            1: QuestStage(_("Defeat the Demorai ambush"), hintTxt = _("Just as we've been taught, the Demorai have set up a trap for us as we were navigating the Valley of Death. Time to put our training to the {i}real{/i} test.")),
            2: QuestStage(_("March on"), hintTxt = _("We have claimed victory in our first real battle against the Demorai. I do realize we'd likely be crushed if it wasn't for First Officer Borras at our side, but all the training sessions vanish compared to what {i}real combat{/i} feels like.")),
            3: QuestStage(_("Defeat the scorpion monster!"), hintTxt = _("We have walked into a horrifying monster. A gigantic scorpion that seemed to have... somehow inhabited a woman's body? It had burned First Officer Borras with a single spit of acidic substance. We are not prepared...")),
            4: QuestStage(_("Get to the abandoned fort"), hintTxt = _("We are now past the Valley of Death. Word is, it is going to take us more than a week to get to our objective. Having seen what we had seen, I really want this to be over, {i}soon.{/i}")),
            5: QuestStage(_("Stand guard as mages open the seal"), hintTxt = _("At the deep cave beneath the deserted fort, we have found what seems to be a magically-sealed door. Captain Duprey ordered some of our mages to unlock it. There's tension in the air. Something's off...")),
            6: QuestStage(_("Survive the Demorai onslaught"), hintTxt = _("The moment we have breached the seal, the fort was attacked by Demorai forces. We must come out of this alive!")),
            7: QuestStage(_("Examine the chamber"), hintTxt = _("Me and Markus have survived the battle by locking ourselves inside the chamber the mages have unlocked. Duprey, Kiara, countless other scouts died before our very eyes. We must find a way out. What is that eerie sound? It sounds like a heartbeat, but a little off-tempo...")),
        }
        TITLE = _("The Dark Passenger")
        DESCRIPTION = _("Our training was interrupted by what Captain Duprey called a top-secret mission to accomplish. We are to retrieve a relic of sorts from a fort way down south. It doesn't really sound scary, but I've got a bad feeling about it. Most of us do.")

        def __init__(self):
            super().__init__()

            self.XpReward = 400

            # these are ticked True as player navigates the camp
            self.CampMarkusTalked   = False
            self.CampKiaraTalked    = False
            self.CampBorrasTalked   = False
            self.CampDupreyTalked   = False
            self.CampPlayedCards    = False

            # these are ticked as player talks to kiara & mc in aband fort
            self.AbandFortMarkusTalked = False
            self.AbandFortKiaraTalked = False

            # whether or not to show kiara camp sex scene
            self.AgreedToSleepWithKiara = False

            # obelisks room checkboxes, ticking all of these enables player to click obelisks
            self.ObelisksRoomSeenPapers = False
            self.ObelisksRoomSeenPotions = False
            self.ObelisksRoomSeenSkeleton = False

            self.IsMain = True

            self.CampTriggeredSleepInTentByWaiting = False

        def onEnter(self):  
            if GetLocID() in ["qst_darkpass_desertcamp", "qst_darkpass_desertcamp_fireplace_area", "qst_darkpass_desertcamp_mc_tent"]:
                if IsInTimeFrame(TIME_LATENIGHT, TIME_DAY_START):
                    if self.CampTriggeredSleepInTentByWaiting == False:
                        self.CampTriggeredSleepInTentByWaiting = True
                        return TriggeredEvent("qst_TheDarkPass_TooLateGoToSleep")
            elif GetLocID() == "qst_darkpass_abandoned_fort":
                if IsInTimeFrame(TIME_DAY_END, TIME_NIGHT):
                    return TriggeredEvent("qst_TheDarkPass_GateIsOpen")
                else:
                    if self.AbandFortMarkusTalked and self.AbandFortKiaraTalked:
                        return TriggeredEvent("qst_TheDarkPass_SkipTimeAndGateIsOpen")

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "qst_darkpass_desertcamp":
                if not self.CampMarkusTalked:
                    btnMods["btn_darkpass_camp_talk_markus"] = BtnJumpLabel(_("Markus"), "qst_TheDarkPass_CampTalkMarkus")
                else:
                    btnMods["btn_darkpass_camp_talk_markus"] = BtnJumpLabel(_("Markus"), "qst_TheDarkPass_CampTalkMarkus_rep")

                if not self.CampKiaraTalked:
                    btnMods["btn_darkpass_camp_talk_kiara"] = BtnJumpLabel(_("Kiara"), "qst_TheDarkPass_CampTalkKiara")
                else:
                    btnMods["btn_darkpass_camp_talk_kiara"] = BtnJumpLabel(_("Kiara"), "qst_TheDarkPass_CampTalkKiara_rep")

            elif GetLocID() == "qst_darkpass_desertcamp_fireplace_area":
                if not self.CampBorrasTalked:
                    btnMods["btn_darkpass_camp_fireplace_talk_borras"] = BtnJumpLabel(_("Borras"), "qst_TheDarkPass_CampTalkBorras")
                else:
                    btnMods["btn_darkpass_camp_fireplace_talk_borras"] = BtnDisabled()

                if not self.CampDupreyTalked:
                    btnMods["btn_darkpass_camp_fireplace_talk_duprey"] = BtnJumpLabel(_("Captain Duprey"), "qst_TheDarkPass_CampTalkDuprey")
                else:
                    btnMods["btn_darkpass_camp_fireplace_talk_duprey"] = BtnJumpLabel(_("Captain Duprey"), "qst_TheDarkPass_CampTalkDuprey_rep")
                
                if not self.CampPlayedCards:
                    btnMods["btn_darkpass_camp_fireplace_play_cards"] = BtnJumpLabel(_("Scouts playing cards"), "qst_TheDarkPass_CampPlayCards")
                else:
                    btnMods["btn_darkpass_camp_fireplace_play_cards"] = BtnDisabled()
            
            elif GetLocID() == "qst_darkpass_abandoned_fort":
                if not self.AbandFortMarkusTalked:
                    btnMods["btn_darkpass_aband_fort_talk_markus"] = BtnJumpLabel(_("Markus"), "qst_TheDarkPass_TalkToMarkusInAbandFort")
                else:
                    btnMods["btn_darkpass_aband_fort_talk_markus"] = BtnJumpLabel(_("Markus"), "qst_TheDarkPass_TalkToMarkusInAbandFort_rep")
                if not self.AbandFortKiaraTalked:
                    btnMods["btn_darkpass_aband_fort_talk_kiara"] = BtnJumpLabel(_("Kiara"), "qst_TheDarkPass_TalkToKiaraInAbandFort")
                else:
                    btnMods["btn_darkpass_aband_fort_talk_kiara"] = BtnJumpLabel(_("Kiara"), "qst_TheDarkPass_TalkToKiaraInAbandFort_rep")
                btnMods["btn_darkpass_aband_fort_cave_entrance"] = BtnJumpLabel(_("Cave entrance"), "qst_TheDarkPass_CaveEntrance")
            
            elif GetLocID() == "qst_darkpass_obelisks":
                if not self.ObelisksRoomSeenPapers:
                    btnMods["btn_darkpass_obeliskroom_papers"] = BtnJumpLabel(_("Papers"), "qst_TheDarkPass_ObelisksRoomPapers")
                if not self.ObelisksRoomSeenPotions:
                    btnMods["btn_darkpass_obeliskroom_potions"] = BtnJumpLabel(_("Potions"), "qst_TheDarkPass_ObelisksRoomPotions")
                if not self.ObelisksRoomSeenSkeleton:
                    btnMods["btn_darkpass_obeliskroom_skeleton"] = BtnJumpLabel(_("Skeleton"), "qst_TheDarkPass_ObelisksRoomSkeleton")
                if self.ObelisksRoomSeenPapers and self.ObelisksRoomSeenPotions and self.ObelisksRoomSeenSkeleton:
                    btnMods["btn_darkpass_obeliskroom_obelisks"] = BtnJumpLabel(_("The Obelisks"), "qst_TheDarkPass_ObelisksRoomCheckObelisks")
                
            return LocButtonMod(directMods = btnMods, priority = 1)

        def onComplete(self):
            QstStart(EventAdventureGuildShowUp)

            QstStart(DialogueKylisa)
            DialogueThea().isAdventurer = True

            store.MARKUS.image_tag = "markus"
            store.MC.image_tag = "mc"

            CharSetPortrait("mc", "images/characters/mc/portrait.webp")
            CharSetPortrait("markus", "images/characters/markus/portrait.webp")

            CharSetBattleSkinID("mc", "mc")
            CharSetBattleSkinID("markus", "markus")

            if CharGetVar("kiara", "romanced"):
                CharSetLover("kiara", Silent = False)
                CharAddRelEntry("kiara", "prol_romance")
                CharChangeRel("kiara", 1)
            CharKill("kiara")
            CharAddRelEntry("kiara", "prol_killed")
            CharKill("borras")
            CharAddRelEntry("borras", "prol_killed")
            CharKill("duprey")
            CharAddRelEntry("duprey", "prol_killed")

            QstStart(HouseLockTannerShop)
            QstStart(DialogueMrsWinward)

            AddCharAttr("mc", "Strength",   1)
            AddCharAttr("mc", "Endurance",  1)
            AddCharAttr("mc", "Willpower",  1)
            AddCharAttr("mc", "Agility",    1)
            AddCharAttr("mc", "Dexterity",  1)
            AddCharAttr("mc", "Luck",       1)
            AddCharAttr("mc", "Charisma",   1)
            AddCharAttr("mc", "Barter",     1)
            CharHeal("mc")
            CharRestoreEnergy("mc")

            AddCharAttr("markus", "Strength",   1)
            AddCharAttr("markus", "Endurance",  1)
            AddCharAttr("markus", "Willpower",  1)
            AddCharAttr("markus", "Agility",    1)
            AddCharAttr("markus", "Dexterity",  1)
            AddCharAttr("markus", "Luck",       1)
            CharHeal("markus")
            CharRestoreEnergy("markus")
            return