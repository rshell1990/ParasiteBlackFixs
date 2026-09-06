default gela_ref = _("Gela") 

init python:
    # primer: checks for invest level, started by after-load or by completing beast of novaras
    @AppendToAllQuests
    class PrimerBigTroubleLH(LogicModule):
        def __init__(self):
            super().__init__()
            # to avoid triggering *instantly* after we have invested
            self.ShowScene = False

        def onEnter(self):
            if GetLocID() == "hamun_dist_docks":
                if DialogueMarbella().InvestLevel > 0:
                    self.ShowScene = True
            elif GetLocID() == "hamun_miningco":
                if IsDaytime():
                    if DialogueMarbella().InvestLevel > 0:
                        if self.ShowScene:
                            return TriggeredEvent("qst_BigTroubleLHamun_intro")


    @AppendToAllQuests
    class QstBigTroubleLH(BaseQuest):
        TITLE = _("Big Trouble in Little Hamun")
        DESCRIPTION = _("Marbella is in trouble. It seems the Greater Trading Company wants to snuff out her mining company before it's even begun. I need to find some protection for her...")
        GOALS = {
            0: QuestStage(_("Speak to Lord Zanzibat"), 
                trackTag = "hamun_dist_merch_lord_to_zanzibat_house", 
                hintTxt = _("Maybe a Merchant Lord could help?")),

            # when you're back from zanzibat OR while you can scout for other variants
            1: QuestStage(_("Speak to Marbella or look for someone else to help out"), 
                trackTag = "hamun_docks_to_miningco", 
                hintTxt = _("In return for his help dealing with the GTC, Lord Zanzibat wants me to wipe out the Khazah gang who have set up shop in Hamun. I should speak to Marbella about his offer... \n\nBut maybe The Khazah themselves have a counteroffer? Or, I could try have some sort of a protection device crafted for Marbella, so that she doesn't need to rely on others?")), 
            # these activate when you enter a corresponding place
            2: QuestStage(_("Beshar's offer"),
                hintTxt = _("Beshar can build a golem to protect Marbella.")),
            3: QuestStage(_("The Khazahs' offer"),
                hintTxt = _("The Khazahs gang can help if Marbella agrees to become their gang whore.")),

            # here the goals will split into 
            # dom (golem) / gang (khazah) / love (zanzibat help) routes
            #### golem-specific stuff, 2 digits
            # after you offer marbella golem for ass
            10: QuestStage(_("Talk to Marbella later"),
                trackTag = "hamun_docks_to_miningco", 
                hintTxt = _("I should let Marbella calm down for a day or two before approaching her again...")),

            # after marbella caves
            20: QuestStage(_("Talk to Beshar"),
                trackTag = "hamun_docks_to_smithy", 
                hintTxt = _("The deal is on, I should tell Beshar when I'm ready...")),

            # after you tell besahr you're in to get golem
            30: QuestStage(_("Return to Beshar later"),
                trackTag = "hamun_docks_to_smithy", 
                hintTxt = _("I should prepare for this little expedition, and when I'm ready, I need to tell Beshar it's time.")), 

            # when set off into the deserrt with beshar
            40: QuestStage(_("Travel with Beshar"), 
                hintTxt = _("The temple awaits...")), 

            # when arrived to temple & entererd
            50: QuestStage(_("Find Golem parts"),  
                hintTxt = _("I should look around and see what I can find here... Need to keep my wits about me.")), 

            # return to beshar next day after you bring golem parts back
            60: QuestStage(_("Return to Beshar later"),  
                hintTxt = _("Beshar has asked for time to check over the parts from the temple, I should give it a couple of days before checking in on his progress.")),  

            # pay beshar's fee (only gets shown if you say "i'll go get money")
            65: QuestStage(_("Pay Beshar's fee"),  
                hintTxt = _("Before he can start work on the golem, there is the matter of Beshar's fee that I'll need to pay first...")),  

            # wait for beshar to complete his work
            70: QuestStage(_("Let Beshar work"),  
                hintTxt = _("Beshar will need a few days to make the Golem... I should check back in a day or so.")),  
            
            # return to marbella when golem is done, after sending golem over to her
            80: QuestStage(_("Return to Marbella"),
                hintTxt = _("Now that the golem is ready, I should tell Marbella the good news.")),  

            ### khazah-specific stuff
            # four digits

            # after you offer marbella the gang deal
            1000: QuestStage(_("Talk to Marbella later"),
                trackTag = "hamun_docks_to_miningco", 
                hintTxt = _("I should let Marbella think about the Khazahs' offer.")),
            # when she tells you to "go tell khazahs im ready"
            1010: QuestStage(_("Talk to the Khazah leader"),
                trackTag = "hamun_docks_to_khazah_hideout",
                hintTxt = _("Marbella has agreed to the Khazah's terms... Now I just need to tell their leader.")),
            # when khazahs send you to deal with their rivals
            1020: QuestStage(_("Deal with the Khazahs' rivals"),
                hintTxt = _("The Khazah want me to deal with some of the smaller rival gangs... I should hunt for them around Hamun at night.)")), 
            # return to khazahs after dealing with rivals
            1030: QuestStage(_("Return to Khazah leader"),
                trackTag = "hamun_docks_to_khazah_hideout",
                hintTxt = _("Now the rival gangs have been dealt with, I can report back to the Khazah my progress.")), 

            ### love-specific stuff
            # three digits

            # after you commit her to the zanzibat deal,
            # you gotta go tell zanzibat about it
            100: QuestStage(_("Inform Lord Zanzibat of Marbella's agreement"), 
                trackTag = "hamun_dist_merch_lord_to_zanzibat_house", 
                hintTxt = _("Marbella has agreed to Lord Zanzibat's terms... I should tell him the good news")), 

            # then zanzibat asks you to deal with khazah, 
            # the goal is shared between kill and plant device
            105: QuestStage(_("Destroy the Khazah's hideout in Hamun"), 
                trackTag = "hamun_docks_to_khazah_hideout", 
                hintTxt = _("The Khazah are hiding out in the dock district of Hamun... I need to find them and deal with them, one way or another.")), 

            # after you deal with khazah, you gotta report to zanzibat
            110: QuestStage(_("Report your success to Lord Zanzibat"), 
                trackTag = "hamun_dist_merch_lord_to_zanzibat_house", 
                hintTxt = _("The Khazah have been dealt with, I should report back the news to Lord Zanzibat.")), 

            # after you report about khazah to zanzibat,
            # he sends you off to marbella
            115: QuestStage(_("Inform Marbella her business is now protected."), 
                trackTag = "hamun_docks_to_miningco", 
                hintTxt = _("I have kept up to my end of the deal, now I should let Marbella know she is under Lord Zanzibat's protection officially.")), 
        }

        SIMPLE_GOALS = False

        def __init__(self):
            super().__init__()

            self.XpReward = 950
            self.suggestedLevel = 11

            # generic non-committed stuff
            self.LockedDownForToday_First = False
            self.DoAmbush = False
            self.DoPostAmbushScene = False

            self.TalkedToKhazahOffer = False
            self.TalkedToGolemOffer = False

            # golem, khazah, zanzibat resp.
            # will be "dom", "gang", "love"
            self.Kind = None

            # golem-specific vars
            self.Golem_ComeBackNextDay = False
            self.Golem_BesharCanGo = False
            # 1st, 2nd, 3rd ... dials, -1 is for offset
            self.Golem_DialPositions_Correct = [-1, 4, 3, 6, 1, 2, 5]
            self.Golem_DialPositions_Current = [-1, 0, 0, 0, 0, 0, 0]
            self.Golem_ShrineNames = [-1, 
                _("The masked prince"), _("The crown of blades"), 
                _("The weeping widow"), _("The dreaming god"), 
                _("The drowned man"), _("The Blood moon")
            ]
            self.Golem_DialsSolved = False

            self.Golem_BridgeUnlocked = False

            self.Golem_ShowDialsRoomFirstEnter = True
            self.Golem_ShowPodsRoomFirstEnter = True

            self.Golem_BesharIsReadyPostReturn = False

            self.Golem_NegotiatedBetterDeal = False
            self.Golem_FinalPrice = 4000

            self.Golem_DaysLeftToComplete = 3

            # khazah-specific vars
            self.Gang_ComeBackNextDay = False
            self.Gang_TalkedToLeaderAboutRivals = False
            self.Gang_DealWithRivalsPay = 1500
            self.Gang_SlainRivalGangs = 0



############## quest-specific funcs
        def RollInitialDialState(self):
            for i in range(1, 7):
                ChooseFrom = [1, 2, 3, 4, 5, 6]
                ChooseFrom.remove(self.Golem_DialPositions_Correct[i])
                self.Golem_DialPositions_Current[i] = renpy.random.choice(ChooseFrom)

        # just to save hair
        def GetDialName(self, DialIndex):
            return self.Golem_ShrineNames[self.Golem_DialPositions_Current[DialIndex]]
        def IsDialCorrect(self, DialIndex):
            return self.Golem_DialPositions_Current[DialIndex] == self.Golem_DialPositions_Correct[DialIndex]

        def LoseRandomPotion(self):
            Potions = ["potion_heal_minor", "potion_heal_regular",
                "potion_heal_large", "goblin_stims", "potion_antidote"]
            LoseablePots = [x for x in player_inv.keys() if x in Potions]
            if len(LoseablePots) > 0:
                PlayerRemItem(renpy.random.choice(LoseablePots), MuteSfx = True)
            return

#######################################
        def onMidnight(self):
            if self.LockedDownForToday_First == True:
                self.LockedDownForToday_First = False

            if self.Golem_ComeBackNextDay == True:
                self.Golem_ComeBackNextDay = False

            if self.Gang_ComeBackNextDay == True:
                self.Gang_ComeBackNextDay = False
            
            if IsGoalVisible(self, 30):
                if self.Golem_BesharCanGo == False:
                    self.Golem_BesharCanGo = True

            if IsGoalVisible(self, 60):
                if self.Golem_BesharIsReadyPostReturn == False:
                    self.Golem_BesharIsReadyPostReturn = True

            if IsGoalVisible(self, 70):
                if self.Golem_DaysLeftToComplete > 0:
                    self.Golem_DaysLeftToComplete -= 1


        def locationMod(self):
            btnMods = {}
            # shared-likes
            if IsGoalVisible(self, 0):
                if GetLocID() == "hamun_dist_merch_lord":
                    btnMods["hamun_dist_merch_lord_to_zanzibat_house"] = BtnJumpLabel(STR_LOC.HAMUN_ZANZIBAT_HOUSE, "qst_BigTroubleLHamun_zanzibat_doors")
                elif GetLocID() == "hamun_dist_docks":
                    if self.LockedDownForToday_First == True:
                        btnMods["hamun_docks_to_miningco"] = BtnJumpLabel(STR_LOC.HAMUN_MININGCO, "qst_BigTroubleLHamun_marbella_closed")
            
            elif IsGoalVisible(self, 1):
                if GetLocID() == "hamun_dist_docks":
                    if self.LockedDownForToday_First == True:
                        btnMods["hamun_docks_to_miningco"] = BtnJumpLabel(STR_LOC.HAMUN_MININGCO, "qst_BigTroubleLHamun_marbella_closed")
                    else:
                        if self.DoAmbush == True:
                            btnMods["hamun_docks_to_miningco"] = BtnJumpLabel(STR_LOC.HAMUN_MININGCO, "qst_BigTroubleLHamun_miningco_ambush")
                    btnMods["hamun_docks_to_khazah_hideout"] = BtnJumpLabel(STR_LOC.HAMUN_KHAZAH_HIDEOUT, "qst_BigTroubleLHamun_khazah_approach_hideout")
            
            # golem
            elif IsGoalVisible(self, 10):
                if GetLocID() == "hamun_dist_docks":
                    if self.Golem_ComeBackNextDay == True:
                        btnMods["hamun_docks_to_miningco"] = BtnJumpLabel(STR_LOC.HAMUN_MININGCO, "qst_BigTroubleLHamun_marbella_golem_closed")
            
            # gang
            elif IsGoalVisible(self, 1000):
                if GetLocID() == "hamun_dist_docks":
                    if self.Gang_ComeBackNextDay == True:
                        btnMods["hamun_docks_to_miningco"] = BtnJumpLabel(STR_LOC.HAMUN_MININGCO, "qst_BigTroubleLHamun_marbella_gang_closed")

            # love ones            
            elif IsGoalVisible(self, 100):
                if GetLocID() == "hamun_dist_merch_lord":
                    btnMods["hamun_dist_merch_lord_to_zanzibat_house"] = BtnJumpLabel(STR_LOC.HAMUN_ZANZIBAT_HOUSE, "qst_BigTroubleLHamun_zanzibat_doors")

            elif IsGoalVisible(self, 105):
                if GetLocID() == "hamun_dist_docks":
                    btnMods["hamun_docks_to_khazah_hideout"] = BtnJumpLabel(STR_LOC.HAMUN_KHAZAH_HIDEOUT, "qst_BigTroubleLHamun_love_khazah_hideout")

            elif IsGoalVisible(self, 110):
                if GetLocID() == "hamun_dist_merch_lord":
                    btnMods["hamun_dist_merch_lord_to_zanzibat_house"] = BtnJumpLabel(STR_LOC.HAMUN_ZANZIBAT_HOUSE, "qst_BigTroubleLHamun_zanzibat_doors")
            
            # golem temple
            if GetLocID() == "qst_bigtrouble_temple_bridge":
                if self.Golem_BridgeUnlocked == True:
                    btnMods["btn_bigtrouble_temple_bridge"] = BtnJumpLabel(_("The bridge"), "qst_BigTroubleLHamun_temple_bridge_cross")

            
            
                        
            # higher priority to override zanzibat's "i have no busienss here" stuff
            return LocButtonMod(directMods = btnMods, priority = 1)

        def OverrideLocBg(self):
            Result = {}
            if GetLocID() == "qst_bigtrouble_temple_bridge":
                if self.Golem_BridgeUnlocked:
                    Result["qst_bigtrouble_temple_bridge"] = "bg_arakan_temple_bridge_open"
            return Result

        def onEnter(self):
        ####### beshar and golem
            if IsGoalVisible(self, 1):
                if not IsGoalVisible(self, 2):
                    if GetLocID() == "hamun_smithy":
                        if IsDaytime():
                            return TriggeredEvent("qst_BigTroubleLHamun_beshar_golem")
                if self.DoPostAmbushScene == True:
                    if GetLocID() == "hamun_miningco":
                        if IsDaytime():
                            return TriggeredEvent("qst_BigTroubleLHamun_return_to_marbella_after_ambush")

            elif IsGoalVisible(self, 10):
                if GetLocID() == "hamun_miningco":
                    if IsDaytime():
                        return TriggeredEvent("qst_BigTroubleLHamun_marbella_golem_return_after_offer")
            elif IsGoalVisible(self, 60):
                if GetLocID() == "hamun_smithy":
                    if IsDaytime():
                        if self.Golem_BesharIsReadyPostReturn == True:
                            return TriggeredEvent("qst_BigTroubleLHamun_golem_beshar_pay")
            elif IsGoalVisible(self, 70):
                if GetLocID() == "hamun_smithy":
                    if IsDaytime():
                        if self.Golem_DaysLeftToComplete == 0:
                            return TriggeredEvent("qst_BigTroubleLHamun_golem_beshar_build_over")
            elif IsGoalVisible(self, 80):
                if GetLocID() == "hamun_miningco":
                    if IsDaytime():
                        return TriggeredEvent("qst_BigTroubleLHamun_golem_return_to_marbella")

            # temple section only, loc-based not goal-based
            if GetLocID() == "qst_bigtrouble_temple_dials":
                if self.Golem_ShowDialsRoomFirstEnter:
                    return TriggeredEvent("qst_BigTroubleLHamun_temple_dials_first_enter")
            elif GetLocID() == "qst_bigtrouble_temple_pods":
                if self.Golem_ShowPodsRoomFirstEnter:
                    return TriggeredEvent("qst_BigTroubleLHamun_temple_obelisk_first_enter")
        #####################

        ###### khazahs-related
            if IsGoalVisible(self, 1000):
                if GetLocID() == "hamun_miningco":
                    if IsDaytime():
                        return TriggeredEvent("qst_BigTroubleLHamun_marbella_khazah_return_after_offer")
            
            if IsGoalVisible(self, 1020):
                renpy.hide_screen("HamunFindKhazahRivals")
                if not IsDaytime():
                    if GetLocID() in ["hamun_dist_docks"]:
                        renpy.show_screen("HamunFindKhazahRivals")
        #####################

        ###### love-related
            if IsGoalVisible(self, 115):
                if GetLocID() == "hamun_miningco":
                    if IsDaytime():
                        return TriggeredEvent("qst_BigTroubleLHamun_love_return_to_marbella_after_zanzibat_deal")


        def extraDialogue(self):
            if IsGoalVisible(self, 0):
                yield ("zanzibat_root", DNode(_("I need your help with a matter."), "qst_BigTroubleLHamun_talk_to_zanzibat"))
            if IsGoalVisible(self, 1):
                yield ("marbella_root", DNode(_("About your GTC situation..."), "qst_BigTroubleLHamun_marbella_repeat_menu", order = 100))

            # beshar golem related stuff
            if IsGoalVisible(self, 20):
                yield ("beshar_root", DNode(_("I'm ready to help you collect the Golem parts."), "qst_BigTroubleLHamun_beshar_golem_commit", order = 100))
            if IsGoalVisible(self, 30):
                if self.Golem_BesharCanGo == True:
                    yield ("beshar_root", DNode(_("Let's go get the Golem parts."), "qst_BigTroubleLHamun_beshar_golem_journey_go", order = 100))
                else:
                    yield ("beshar_root", DNode(_("Let's go get the Golem parts."), "qst_BigTroubleLHamun_beshar_golem_journey_no_go", order = 100))

            # if you bother beshar after return but before he's ready to talk
            if IsGoalVisible(self, 60):
                yield ("beshar_root", DNode(_("About that Golem..."), "qst_BigTroubleLHamun_golem_beshar_not_ready_after_return", order = 100))
            # beshar-golem if you said "i'll go get the money"
            if IsGoalVisible(self, 65):
                yield ("beshar_root", DNode(_("Let's talk about your fee."), "qst_BigTroubleLHamun_golem_beshar_pay_menu", order = 100))
            if IsGoalVisible(self, 70):
                yield ("beshar_root", DNode(_("Is that Golem ready?"), "qst_BigTroubleLHamun_golem_beshar_build_inprog", order = 100))

            # khazahs
            if IsGoalVisible(self, 1010):
                if self.Gang_TalkedToLeaderAboutRivals:
                    yield ("hamun_khazah_leader_root", DNode(_("About these rivals of yours..."), "qst_BigTroubleLHamun_marbella_khazah_talk_to_leader_marbella_agreed_rep", order = 100))
                else:
                    yield ("hamun_khazah_leader_root", DNode(_("Marbella has agreed to your terms."), "qst_BigTroubleLHamun_marbella_khazah_talk_to_leader_marbella_agreed", order = 100))
            
            elif IsGoalVisible(self, 1020) or IsGoalVisible(self, 1030):
                yield ("hamun_khazah_leader_root", DNode(_("About these rivals of yours..."), "qst_BigTroubleLHamun_marbella_khazah_rivals_report", order = 100))

            # love route
            if IsGoalVisible(self, 100):
                yield ("zanzibat_root", DNode(_("Marbella is willing to agree to your terms."), "qst_BigTroubleLHamun_love_return_to_zanzibat_after_marbella_commits", order = 100))
            elif IsGoalVisible(self, 110):
                yield ("zanzibat_root", DNode(_("The Khazah have been dealt with."), "qst_BigTroubleLHamun_love_return_to_zanzibat_after_khazah", order = 100))


        def onStart(self):
            self.RollInitialDialState()
            return

        def onComplete(self):
            Assert(self.Kind in ["dom", "gang", "love"])
            QstStart(RomanceMarbella)
            if not QstIsActive(HouseLockHamunKhazahHideout):
                QstStart(HouseLockHamunKhazahHideout)
            if self.Kind == "dom":
                HouseLockHamunKhazahHideout().State = "no_biz"
            elif self.Kind == "love":
                HouseLockHamunKhazahHideout().State = "cleaned"
            elif self.Kind == "gang":
                HouseLockHamunKhazahHideout().State = "operating"