init python:
    notesLib["TheComingStormMeeting"] = Note(
        _("Attend the meeting"), 
        _("I was prompted to come to the guild after dark. Something important's going down."))

    # WARNING, THIS MODULE IS PRE-FIRED BY EITHER ROMANCE NYX OR MARKUS POST-TWO-EMPS EVENT, THEN IT CONSTANTLY CHECKS FOR ITS CONDITIONS TO BEGIN!
    @AppendToAllQuests
    class PrimerTheComingStorm(LogicModule):
        def onEnter(self):  
            if self.progress == 0:
                if IsDaytime():
                    if QstIsOver(RomanceNyx) or (QstIsActive(RomanceNyx) and QstGetProgress(RomanceNyx) >= 3):
                        if QstIsOver(EventNovarasMarkusTavernTwoEmps):
                            if GetLocID() in LocIDList_NovarasCityStreets:
                                return TriggeredEvent("qst_thecomingstorm_primer")

        def locationMod(self):
            btnMods = {}            
            if GetLocID() == "novaras_adv_guild":
                if not IsDaytime():
                    if self.progress == 1:
                        btnMods["btn_thecomingstorm_attend_meeting"] = BtnJumpLabel(_("Attend the meeting"), "qst_thecomingstorm_attendmeeting_button")
            return LocButtonMod(directMods = btnMods)

    @AppendToAllQuests
    class QstTheComingStorm(BaseQuest):
        TITLE = _("The Coming Storm")
        DESCRIPTION = _("Soon, Novaras will fall under a terrible siege by the Demorai... I must do what I can to help the city prepare.")
        GOALS = {
            10: QuestStage(_("Warn Captain Nyx"),               trackTag = "btn_novaras_fort_seb", hintTxt = _("Kiara, back from the dead, has warned me of an impending siege upon Novaras... I must talk to Captain Nyx.")),
            20: QuestStage(_("Talk to the guards"),             trackTag = "btn_novaras_gates_exit_city", hintTxt = _("I must talk to the guards at the gates about Poltrik, Captain Nyx's agent gone missing.")),
            30: QuestStage(_("Check the Iron Unicorn"),         trackTag = "btn_novaras_tavern", hintTxt = _("Sergeant Poltrik was seen at the Iron Unicorn tavern, investigating some traders. Perhaps I should check there...")),

            40: QuestStage(_("Keep looking for Poltrik"),       trackTag = ["btn_novaras_bordello", "btn_mc_house"], hintTxt = _("Shay suggests I seek information on missing guards or strange traders in {i}less reputable places{/i}. I should talk to the working girls at the Pleasure District.\nOr, perhaps Regina could help? She is close with Erika, and Erika is Inquisition. 'Inquisition sees all', as they say...")),

            # alt investigation. (odd two-digit numbers)
            45: QuestStage(_("Go to the library"),              trackTag = "btn_novaras_library", hintTxt = _("The Inquisition seems to also be looking for the missing guards. I can try get in contact with Inquisitor Saren by following the instructions from the letter Erika left for me.\nI'll need a password to contact Saren: a name of some book I am to ask about at the library. The letter said I should start with {i}'Dreams of Astatar'{/i}, whatever that is.")),
            55: QuestStage(_("Pick up a parcel for Vala"),      hintTxt = _("I need to get to the market district, after dark, to pick up a parcel for Vala in exchange for her help.")),
            65: QuestStage(_("Follow the assassin's instructions"), trackTag = "btn_novaras_bordello", hintTxt = _("The parcel retrieval did not go as planned, at all. Whoever I had to contact demanded 'her head' but quite soon lost his own to a third party, who also snatched the package. I have no choice but to buy out the parcel now.\nI need to put a thousand coins in a special hidden spot near the Weeping Heart. I should do this next night.")),
            75: QuestStage(_("Deal with the assassin"),         hintTxt = _("Time to retrieve the package, for real now.")),
            85: QuestStage(_("Bring the parcel to Vala"),       trackTag = "btn_novaras_library", hintTxt = _("Having dealt with the assassin I have retrieved the parcel. Time to head back to the library, hopefully I'll get some answers from Vala.")),
            # this is 'in place' of 310
            95: QuestStage(_("Return to Captain Nyx"),          trackTag = "btn_novaras_fort_seb", hintTxt = _("Vala or... whatever her real name is, shared some dark information on the missing guards. Apparently they might be hiding in the southern Housing District, at one of Poltrik's family properties. I need to report to Captain Nyx, she should know the exact place.")),
            # "return to nyx" (after ambush)
            99: QuestStage(_("Return to Captain Nyx"),          trackTag = "btn_novaras_fort_seb", hintTxt = _("It seems we have found Poltrik. Whatever abomination he is now... It is still roaming free in the city. I need to talk to Nyx.")),
            # this is in place of 350
            97: QuestStage(_("Get to the library"),             trackTag = "btn_novaras_library", hintTxt = _("Erika had helped me escape, but now I need a place to hide. Perhaps Vala could help? I should be careful getting there.")),

            # branches-out the route1 into two variants. 1** is sex show route
            150: QuestStage(_("Put on a show"),                 trackTag = "btn_novaras_library", hintTxt = _("I have agreed to put on a show for Carina in exchange for her help looking for the missing guards. I should return to her the next day. Anything for the City of Novaras...")),

            # 2** is valchek route 
            250: QuestStage(_("Look for Valchek"),              hintTxt = _("I must deal with an associate of Carina gone rogue, Valchek. She wants him gone, one way or another. I should be able to find him in the market district.")),
            # this only appears (and gets complete) if you do not pay lucius during first dialogue
            260: QuestStage(_("Pay for the meeting"),           trackTag = "btn_novaras_store_int", hintTxt = _("Lucius Mal can set up a meeting with Valchek for me, but not for free.")),
            270: QuestStage(_("Come to the store after dark"),  trackTag = "btn_novaras_store_int", hintTxt = _("I have paid Lucius Mal to set up a meeting with Valchek. I need to come to his store at night.")),
            271: QuestStage(_("Kill Valchek"),                  hintTxt = _("I have met Valchek. Now, it's time for some problem-solving, the ancient way...")),
            # valchek killed 
            280: QuestStage(_("Report to Carina"),              trackTag = "btn_novaras_bordello", hintTxt = _("Valchek is dealt with... for good. I should turn in. Carina will like the good news.")),
            # valchek smuggle variant
            290: QuestStage(_("Speak to Carina on behalf of Caskell"), trackTag = "btn_novaras_bordello", hintTxt = _("I have agreed to smuggle Valchek out of Novaras.\nLucius Mal will help arrange that, but not for free. He asked me to convince Carina to meet with someone who goes by the name Caskell.")),
            # (yea the following is squashed together)
            291: QuestStage(_("Return to Lucius Mal"),          trackTag = "btn_novaras_store_int", hintTxt = _("I have talked to Carina, she agreed to meet up with Caskell. I should meet with Lucius Mal so that we can move on with smuggling Valchek out of the city. I think Lucius will want this done at night...")),
            292: QuestStage(_("Report to Carina"),              trackTag = "btn_novaras_bordello", hintTxt = _("Carina will never hear from Valchek again. Hopefully, she will not find out that Valchek is still alive though...")),

            # 3** is convergence at "return to carina in 3 days" and onwards
            # "return to carina" part
            300: QuestStage(_("Return to Carina in three days"), trackTag = "btn_novaras_bordello", hintTxt = _("Carina is using her resources to help me find Poltrik. She said she would need three days to gather the intelligence.")),

            # "return to nyx" part (after above OR vala)
            310: QuestStage(_("Return to Captain Nyx"),         trackTag = "btn_novaras_fort_seb", hintTxt = _("Carina's sources report that the guards might be hiding in the southern Housing District. I need to report to Captain Nyx.")),
            # "return to nyx" (after ambush)
            320: QuestStage(_("Return to Captain Nyx"),         trackTag = "btn_novaras_fort_seb", hintTxt = _("It seems we have found Poltrik. Whatever abomination he is now... It is still roaming free in the city. I need to talk to Nyx.")),
            
            330: QuestStage(_("Go to Poltrik's family estate"), hintTxt = _("Nyx says Poltrik's uncle has a manor in the south-eastern district. Perhaps this is where Poltrik hides. I need to get there at once.")),
            340: QuestStage(_("Defeat Poltrik"),                hintTxt = _("Having surrendered himself to the darkness, Poltrik has... {i}changed.{/i} A monster himself, he also turned his uncle's estate into a breeding ground for some kind of Demorai abominations.")),

            350: QuestStage(_("Talk to Carina"),                trackTag = "btn_novaras_bordello", hintTxt = _("Erika had helped me escape, but now I need a place to hide. Perhaps Carina could help? I should be careful getting there.")),
        }

        # appear timer on top of screen
        # A countdown appears each day: '10 days left until it all ends...' counting down to zero.

        # If the player fails to complete the quest in time, the battle sequence triggers with variant 2—where multiple characters die.


        SIMPLE_GOALS = False

        def __init__(self):
            super().__init__()

            self.XpReward = 800
            # progress is only used for progression, not for goals
            # 0 is free-roam post-meeting (go meet nyx OR HOME to trigger alt path)
            # 1 is past that        
            self.suggestedLevel = 9
            self.IsMain = True

            self.DaysLimit = 10
            self.DaysLeft = self.DaysLimit
            self.ShowAndSpinCountdown = False
            self.TimeOutFlag = False

            # if true, adara *and* her father survive, if false, only adara.
            # affects narrative 
            self.GaveAdaraMoneyForEscape = False

            self.SexShowChoice = None # "regina" or "shani"
            # helper to make sex show trigger just "at night"
            self.TriggerSexShow = False

            self.WayIntoPoltrikEstate = None # "kick" or "pick"

            # this will store char IDs who have left player party
            # during that nquisitor bust scene
            self.PoltrikEstateLeftPlayerPartyChars = set()

            self.TrackOverrides = {"day":set(), "night":set()}

            # turned true if you saw that scene where guard talks to mc
            # during "get to carina" sneak-like section
            self.SeenGuardSceneInSneakSession = False

            # set to true if you ask vala about dreams of astatar
            self.ValaInvestigationOpenedSpecialBookshelf = False 
            
            self.ValaInvestigationDistractedBanditsDuringChase = False
            self.ValaInvestigationGoldStashDayPassed = False
            # this flag is for the "return" sequence (where plaeyr has to sneak to: carina or vala's)
            self.ValaInvestigationPath = False
            
            self.ValchekSawMarketEnterScene = False

            self.ValchekLuciusMalArrangeCost = 300 # can negotiate down to 150

        def onNoon(self):
            if IsGoalVisible(self, 150):
                self.TriggerSexShow = True
            
            # this will lock player from stashing the gold the same night they met the assassin
            if IsGoalVisible(self, 65):
                self.ValaInvestigationGoldStashDayPassed = True
            return

        # this should always return a dict of X:Y, X:Y
        # where X is track to replace,
        # Y is track to replace with
        # REGARDLESS of day/night/ambience/whatever
        def OverrideAmbienceOrMusicTrack(self):
            Result = {
                "audio/music/3_Novaras_L.ogg":"audio/music/45_Looming_Dusk.ogg",
                "audio/music/7_novaras_d.ogg":"audio/music/45_Looming_Dusk.ogg"}
            return Result

        # in onExit events, you usually want to check lastTag to say 
        # "what location tag am I leaving?""
        def onExit(self):
            # remove books player mightve jacked
            if IsGoalVisible(self, 45) or IsGoalVisible(self, 55):
                if PlayerPos.lastTag == "novaras_library_int":
                    if PlayerItemQty("book_dreams_of_astatar") > 0 or PlayerItemQty("book_the_first_darkness") > 0 or PlayerItemQty("book_loving_ophelia") > 0:
                        renpy.jump("qst_thecomingstorm_alt_investigation_vala_returnbooksonexit")

        def onEnter(self):  
            if self.TimeOutFlag:
                for GoalID, Goal in self.GOALS.items():
                    if IsGoalVisible(self, GoalID):
                        GoalFail(self, GoalID)
                QstFail(self)
                QstStart(QstJudgementDay)
                if CharInParty("elena"):
                    QstTheComingStorm().PoltrikEstateLeftPlayerPartyChars.add("elena")
                    PartyRemChar("elena", Silent = True)

                if CharInParty("myu"):
                    QstTheComingStorm().PoltrikEstateLeftPlayerPartyChars.add("myu")
                    PartyRemChar("myu", Silent = True)
                
                PartyRemChar("markus", Silent = True)
                return TriggeredEvent("qst_JudgementDay_SiegeStart", 666)

            if GetLocID() == "novaras_tavern":
                if IsGoalVisible(self, 30):
                    return TriggeredEvent("qst_thecomingstorm_route1_visit_iron_unicorn")

            # sex show trigger
            elif GetLocID() == "novaras_bordello_interior":
                if IsGoalVisible(self, 150):
                    if self.TriggerSexShow:
                        return TriggeredEvent("qst_thecomingstorm_route1_subr1_sexshow")

            elif GetLocID() == "novaras_bordello_office":
                if IsGoalVisible(self, 300):
                    if self.delayCheck():
                        return TriggeredEvent("qst_thecomingstorm_return_to_carina_in_3_days")
                if IsGoalVisible(self, 350):
                    return TriggeredEvent("qst_TheComingStorm_GetToCarinaSneak_Arrived")

            elif GetLocID() == "novaras_fort_seb_captains_office":
                if IsGoalVisible(self, 320) or IsGoalVisible(self, 99):
                    return TriggeredEvent("qst_thecomingstorm_return_to_nyx_after_ambush")

            elif GetLocID() == "novaras_library_int":
                if IsGoalVisible(self, 45):
                    if GetItemQty(bookshelf_comingstorm_special, "book_dreams_of_astatar") == 0:
                        AddItemTo(bookshelf_comingstorm_special, "book_dreams_of_astatar")
                    if GetItemQty(bookshelf_comingstorm_special, "book_the_first_darkness") == 0:
                        AddItemTo(bookshelf_comingstorm_special, "book_the_first_darkness")
                    if GetItemQty(bookshelf_comingstorm_special, "book_loving_ophelia") == 0:
                        AddItemTo(bookshelf_comingstorm_special, "book_loving_ophelia")
                if IsGoalVisible(self, 85):
                    return TriggeredEvent("qst_thecomingstorm_alt_investigation_return_with_parcel")

            elif GetLocID() == "novaras_dist_market":
                if IsGoalVisible(self, 55):
                    if not IsDaytime():
                        return TriggeredEvent("qst_thecomingstorm_alt_investigation_enter_market_district")
                if IsGoalVisible(self, 250):
                    if not self.ValchekSawMarketEnterScene:
                        return TriggeredEvent("qst_thecomingstorm_valchek_atmarket")

        def locationMod(self):
            btnMods = {}
            # vala investigation alt route, that special bookshelf
            if GetLocID() == "novaras_library_int":
                if IsGoalVisible(self, 45):
                    if self.ValaInvestigationOpenedSpecialBookshelf:
                        btnMods["btn_comingstorm_bookshelves"] = BtnShowScreen(_("Bookshelves upstairs"), "container", bookshelf_comingstorm_special, HideOnTakeAll = True)

            elif GetLocID() == "novaras_dist_army":
                if IsGoalVisible(self, 350) or IsGoalVisible(self, 97):
                    btnMods["btn_novaras_gates_exit_city"] = BtnJumpLabel(STR_LOC.NOV_GATES, "qst_TheComingStorm_GetToCarinaSneak_CityGates")
                    btnMods["bridge_novaras_army_to_market"] = BtnJumpLabel(STR_LOC.NOV_DIST_MARKET, "qst_TheComingStorm_GetToCarinaSneak_ArmyToMarketBridge")
                    btnMods["bridge_novaras_army_to_centre"] = BtnJumpLabel(STR_LOC.NOV_DIST_CENTRE, "qst_TheComingStorm_GetToCarinaSneak_ToCentreBridge")
                    btnMods["btn_novaras_fort_seb"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT, "qst_TheComingStorm_GetToCarinaSneak_ArmyToFortSebastian")
                else:
                    btnMods["btn_novaras_gates_exit_city"] = BtnJumpLabel(STR_LOC.NOV_GATES, "qst_TheComingStorm_NovarasGatesCantExit")
                    if IsGoalVisible(self, 310) or IsGoalVisible(self, 95):
                        if IsDaytime():
                            btnMods["btn_novaras_fort_seb"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT, "qst_thecomingstorm_return_to_nyx_after_carina_day")
                        else:
                            btnMods["btn_novaras_fort_seb"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT, "qst_thecomingstorm_return_to_nyx_after_carina_night")
    

            elif GetLocID() == "novaras_dist_house_south":
                if IsGoalVisible(self, 330):
                    btnMods["btn_novaras_poltrik_family_estate"] = BtnJumpLabel(STR_LOC.NOV_POLTRIK_ESTATE, "qst_thecomingstorm_poltrik_family_estate")

            elif GetLocID() == "novaras_dist_house":
                if IsGoalVisible(self, 350) or IsGoalVisible(self, 97):
                    btnMods["btn_mc_house"] = BtnJumpLabel(STR_LOC.NOV_MC_HOUSE, "qst_TheComingStorm_GetToCarinaSneak_MCHouse")
                    btnMods["bridge_novaras_house_to_centre"] = BtnJumpLabel(STR_LOC.NOV_DIST_CENTRE, "qst_TheComingStorm_GetToCarinaSneak_ToCentreBridge")
                    if QstIsActive(HouseLockAzul):
                        if QstIsComplete(QstRavenousJelly):
                            btnMods["btn_azul_safehouse"] = BtnJumpLabel(STR_LOC.NOV_MYU_HIDEOUT, "qst_TheComingStorm_GetToCarinaSneak_NotNow")
                        else:
                            btnMods["btn_azul_safehouse"] = BtnJumpLabel(STR_LOC.NOV_AZUL_SH, "qst_TheComingStorm_GetToCarinaSneak_NotNow")
                    if QstIsActive(HouseLockNijah):
                        btnMods["btn_azul_safehouse"] = BtnJumpLabel(STR_LOC.NOV_NIJAH_HOUSE, "qst_TheComingStorm_GetToCarinaSneak_NotNow")

            elif GetLocID() == "novaras_dist_mage":
                if IsGoalVisible(self, 350) or IsGoalVisible(self, 97):
                    btnMods["btn_novaras_palam_mainhall_door"] = BtnJumpLabel(STR_LOC.NOV_PALAM, "qst_TheComingStorm_GetToCarinaSneak_Palam")

            elif GetLocID() == "novaras_dist_farm":
                if IsGoalVisible(self, 350) or IsGoalVisible(self, 97):
                    btnMods["bridge_novaras_farm_to_centre"] = BtnJumpLabel(STR_LOC.NOV_DIST_CENTRE, "qst_TheComingStorm_GetToCarinaSneak_ToCentreBridge")
            
            elif GetLocID() == "novaras_dist_pleasure":
                if IsGoalVisible(self, 350) or IsGoalVisible(self, 97):
                    btnMods["bridge_novaras_pleasure_to_centre"] = BtnJumpLabel(STR_LOC.NOV_DIST_CENTRE, "qst_TheComingStorm_GetToCarinaSneak_ToCentreBridge")
                    btnMods["novaras_diamond"] = BtnJumpLabel(STR_LOC.NOV_BDIAMOND, "qst_TheComingStorm_GetToCarinaSneak_BlackDiamond")
                    if IsGoalVisible(self, 97):
                        btnMods["btn_novaras_bordello"] = BtnJumpLabel(STR_LOC.NOV_BORDELLO, "qst_TheComingStorm_GetToValaSneak_BordelloBlock")
                    
            elif GetLocID() == "novaras_dist_market":
                if IsGoalVisible(self, 350) or IsGoalVisible(self, 97):
                    btnMods["btn_novaras_tavern"] = BtnJumpLabel(STR_LOC.NOV_TAVERN, "qst_TheComingStorm_GetToCarinaSneak_Tavern")
                    btnMods["btn_novaras_adv_guild"] = BtnJumpLabel(STR_LOC.NOV_ADV_GUILD, "qst_TheComingStorm_GetToCarinaSneak_AdvGuild")
                    if self.SeenGuardSceneInSneakSession:
                        btnMods["bridge_novaras_market_to_army"] = BtnJumpLabel(STR_LOC.NOV_BDIAMOND, "qst_TheComingStorm_GetToCarinaSneak_MarketToArmyBridge_seen")
                    else:
                        btnMods["bridge_novaras_market_to_army"] = BtnJumpLabel(STR_LOC.NOV_BDIAMOND, "qst_TheComingStorm_GetToCarinaSneak_MarketToArmyBridge")

                if IsGoalVisible(self, 270):
                    if not IsDaytime():
                        btnMods["btn_novaras_store_int"] = BtnJumpLabel(STR_LOC.NOV_GENERAL_STORE, "qst_thecomingstorm_valchek_return_to_store_after_dark_to_meet_valchek")

                if IsGoalVisible(self, 291):
                    btnMods["btn_novaras_store_int"] = BtnJumpLabel(STR_LOC.NOV_GENERAL_STORE, "qst_thecomingstorm_valchek_smuggle_away")

            elif GetLocID() == "novaras_bordello_ext":
                if IsGoalVisible(self, 65):
                    TooltipClear()
                    if self.ValaInvestigationGoldStashDayPassed:
                        btnMods["btn_comingstorm_assassin_gold_stash_spot"] = BtnJumpLabel(_("Stash gold"), "qst_thecomingstorm_alt_investigation_stash_gold")
                    else:
                        btnMods["btn_comingstorm_assassin_gold_stash_spot"] = BtnJumpLabel(_("Stash gold"), "qst_thecomingstorm_alt_investigation_stash_gold_next_night")
            
            elif GetLocID() == "novaras_bordello_interior":
                if IsGoalVisible(self, 350) or IsGoalVisible(self, 97):
                    if QstIsActive(DoorNovarasSexDungeon):
                        btnMods["btn_novaras_bordello_mainhall_to_dungeon"] = BtnDisabled()

            elif GetLocID() == "novaras_dist_edu":
                if IsGoalVisible(self, 97):
                    btnMods["btn_novaras_library"] = BtnJumpLabel(STR_LOC.NOV_LIBRARY_INT, "qst_TheComingStorm_GetToValaSneak_Arrived")

            # make adara not appear
            elif GetLocID() in ["adara_house_bedroom", "adara_house_living_room"]:
                if self.ShowAndSpinCountdown:
                    btnMods["btn_talk_adara"] = BtnDisabled()
                    btnMods["btn_talk_gerard"] = BtnDisabled()

            # higher priority to ovveride all the stuff
            return LocButtonMod(directMods = btnMods, priority = 2)

        def onStart(self):
            QstComplete(PrimerTheComingStorm)
            return

        def onComplete(self):
            GoalComplete(self, 350)
            QstStart(QstJudgementDay)

            if can_unlock_achievement("LOOK_AT_YOU_DETECTIVE"):
                unlock_achievement("LOOK_AT_YOU_DETECTIVE")
            return

        def onMidnight(self):
            if self.ShowAndSpinCountdown:
                self.DaysLeft -= 1
                if self.DaysLeft < 1:
                    self.TimeOutFlag = True
            return

        def extraDialogue(self):
            if IsGoalVisible(self, 10):
                yield ("nyx_root", DNode(_("I must speak with you about an urgent matter at once!"), "qst_thecomingstorm_route1_talktonyx_firsttime"))

            if IsGoalVisible(self, 40):
                if QstIsComplete(QstBeneathTheShadows):
                    yield ("carina_root", DNode(_("I need information on some guards gone missing."), "qst_thecomingstorm_route1_talk_carina"))
                else:
                    yield ("carina_root", DNode(_("I need information on some guards gone missing."), "qst_thecomingstorm_route1_talk_carina_refuse"))

                yield ("regina_root", DNode(_("Where's Erika? I must speak with her at once!"), "qst_thecomingstorm_alt_investigation_reginatalk", order = 5))

            if IsGoalVisible(self, 300):
                yield ("carina_root", DNode(_("Have you found anything useful?"), "qst_thecomingstorm_return_to_carina_in_3_days_early"))

            if IsGoalVisible(self, 45):
                if self.ValaInvestigationOpenedSpecialBookshelf:
                    yield ("vala_root", DNode(_("I wanted to ask about a particular book..."), "qst_thecomingstorm_alt_investigation_vala_password"))
                else:
                    yield ("vala_root", DNode(_("Do you know of a book called Dreams of Astatar?"), "qst_thecomingstorm_alt_investigation_vala_ask_about_astatar", order = 5))

            if IsGoalVisible(self, 250):
                yield ("luciusmal_root", DNode(_("I'm looking for someone called Valchek."), "qst_thecomingstorm_valchek_atlucius_initial", order = 5))
            if IsGoalVisible(self, 260):
                yield ("luciusmal_root", DNode(_("About Valchek..."), "qst_thecomingstorm_valchek_atlucius_repeat", order = 5))
            
            if IsGoalVisible(self, 291):
                if IsDaytime():
                    yield ("luciusmal_root", DNode(_("I have dealt with Caskell."), "qst_thecomingstorm_valchek_carina_report_caskell_day", order = 5))

            if IsGoalVisible(self, 280):
                yield ("carina_root", DNode(_("Valchek is dead."), "qst_thecomingstorm_valchek_report_death_conclusion", order = 5))
            if IsGoalVisible(self, 292):
                yield ("carina_root", DNode(_("Valchek is gone...."), "qst_thecomingstorm_valchek_report_smuggled_conclusion", order = 5))
            
            if IsGoalVisible(self, 290):
                yield ("carina_root", DNode(_("A merchant who goes by the name Caskell wants to meet with you."), "qst_thecomingstorm_valchek_carina_ask_caskell", order = 5))

label qst_TheComingStorm_NovarasGatesCantExit:
    # If the player tries to leave the city
    show cg_guard onlayer characters at left as guard1
    show cg_guard onlayer characters at right_f as guard2
    with dissolve
    "At the city gates, dozens of wagons sat motionless, traders, merchants, and families arguing for their right to leave."
    "Each was denied by the stationed guards."
    show cg_guard onlayer characters at shake, left as guard1
    GUARD "HALT!"
    show cg_guard onlayer characters at right_f as guard2
    GUARD "By order of the Emperor, no one may leave Novaras until the siege threat has passed!"
    # "talk to guards bout poltrik"
    menu:
        "Captain Nyx sent me to investigate Sergeant Poltrik's disappearance..." if IsGoalVisible(QstTheComingStorm, 20):
            jump qst_thecomingstorm_route1_talk_to_guards_about_poltrik

        "Where do I get an official permit?":
            GUARD "Official permits are only granted to high lords or ranking military officials."
            GUARD "Neither of which you are... Move along."
            MC "(Fuck... Looks like I'm not getting out through the main gate.)"   
            pass

        "Leave":
            GUARD "Be ready for further announcements from the city guard!"
            pass

    $ LocEnter()