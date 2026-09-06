init python:
    @AppendToAllQuests
    class PrimerTheTarbecks(LogicModule):
        def onEnter(self):  
            if GetLocID() in ["hamun_dist_docks", "hamun_dist_arena", "hamun_dist_merch_lord"]:
                if IsDaytime():
                    if QstDelayCheck(self):
                        return TriggeredEvent("qst_TheTarbecks_PrimerInvite")
            return

label qst_TheTarbecks_PrimerInvite:
    $ QstComplete(PrimerTheTarbecks)
    show mc at cright with easeinleft
    GUARD "You there!"
    show cg_guard_hamun at cleft with easeinleft
    show mc at blurin, cright_f
    "I turned to look toward one of the city guards approaching me."
    "Instinctively, my hand reached for the hilt of my blade."
    MC @think "Who calls for me?"
    GUARD "Garen Quiltshire of the Greater Trading Company requests your presence."
    GUARD "He will be waiting for you at {i}The Pale Dragon{/i}."
    "I loosened my grip as I begin to relax."
    MC @talk "Thanks..."
    show cg_guard_hamun at blurin, cleft_f
    hide cg_guard_hamun with easeoutleft
    "The guard bows curtly before turning to leave."
    show mc at center_f with ease
    $ QstStart(QstTheTarbecks)
    $ GoalShow(QstTheTarbecks, 0)
    MC @serious "(Here we go again...)"
    $ LocEnter()

init python:
    @AppendToAllQuests
    class QstTheTarbecks(BaseQuest):
        TITLE = _("The Tarbecks")
        DESCRIPTION = _("Garen Quiltshire of the Greater Trading Company has summoned me to talk once more, no doubt to discuss the other lord, Lord Tarbeck...")
        GOALS = {
            0: QuestStage(_("Go to The Pale Dragon"), 
                trackTag = "hamun_docks_to_hookah_bar", 
                hintTxt = _("I must speak to Garen Quiltshire at The Pale Dragon. I will be able to find him there at daytime.")),
            1: QuestStage(_("Head to Giselra's tailor store"), 
                hintTxt = _("I need to head to Giselra's tailor in order to have some more appropriate clothes made for Lord Tarbeck's party.")),
            # purchase clothes
            2: QuestStage(_("Purchase clothes"), 
                hintTxt = _("Giselra needs 2000 coin for the party clothes.")),
            # wait for clothes
            3: QuestStage(_("Let Giselra finish her work"), 
                hintTxt = _("Giselra will need at least a week to prepare my clothes...")),
            # (side route) hire a prostitute
            4: QuestStage(_("Hire a prostitute"), 
                trackTag = "hamun_docks_to_brothel",
                hintTxt = _("I need to hire a prostitute to attend as my plus one to Tarbeck's party... Perhaps I should try the Kitten's Paw.")),

            # go to lord tarbeck's estate
            5: QuestStage(_("Head to Lord Tarbeck's party"), 
                trackTag = "hamun_dist_merch_lord_to_tarbeck_mainhall",
                hintTxt = _("Lord Tarbeck's party begins in the evening... I should make my way over when ready.")),

            6: QuestStage(_("Find Sypha"), 
                hintTxt = _("Sypha has to be here... But where?")),

            7: QuestStage(_("Head back to the main hall"), 
                hintTxt = _("Enjoy the party...")),

            8: QuestStage(_("Earn at least five golden tokens"), 
                hintTxt = _("It seems if I'm going to gain access to the upstairs, I'll need to play Lord Tarbeck's perverse games and win at least five tokens... But maybe there's another way?")),

            ######### ingrid route goals. BE AWARE that ingrid route still keeps qst module on progress 8
            9: QuestStage(_("(Optional) Find the fleeing woman"), 
                hintTxt = _("Some guards are pursuing a woman seemingly trying to escape Lord Tarbeck... Should I investigate further?")),
            10: QuestStage(_("Head to the library and speak to Lady Tarbeck"), 
                hintTxt = _("Ingrid said Lady Tarbeck may know a secret way out, I must find her... Ingrid suggested I look in the library.")),
            11: QuestStage(_("Return to Ingrid"), 
                hintTxt = _("Lady Tarbeck has provided a key, I must retun to Ingrid at once!")),
            #########

            # progress 9+
            101: QuestStage(_("Turn in your golden tokens"), 
                hintTxt = _("I have enough golden tokens, I should now bring them to the watcher, at the main hall.")),
            102: QuestStage(_("Defeat the succubus"), 
                hintTxt = _("Lord Tarbeck prepared a surprise for us: a succubus! Apparently, he had made some sort of a deal with it, letting it 'feed' on his guests...")),

        }

        SIMPLE_GOALS = False

        def __init__(self):
            super().__init__()

            self.IsMain = True
            self.XpReward = 800
            self.suggestedLevel = 11
#################################################################
            self.ShowGiselraFirstQstEnterScene = True
            self.GiselraClothesReadyDay = -1    # when player commissions clothes, this is when they'll be made
            self.PartyCompanion = None          # "ves" "kiara" "markus" "esme"
            self.StashedPartyChars = None       # will be set to a list of party chars player had when arriving to party

            # this is parallel progress value to use for the ingrid branch, 5 is "complete"
            self.IngridProgress = 0 
            self.IngridRescuedOutcome = None

            # stores ids of rooms you have already tagged, variants: "maid", "tentacle", "orgy", "mirrors", "temptations", "femdom"
            self.PlayedInRooms = set() 

            self.TarbeckLocationIDs = [
                "hamun_tarbeck_mainhall",
                "hamun_tarbeck_library",
                "hamun_tarbeck_ballroom",
                "hamun_tarbeck_garden_main",
                "hamun_tarbeck_garden_east",
                "hamun_tarbeck_west_wing",
                "hamun_tarbeck_east_wing",
                "hamun_tarbeck_quarters_lord",
                "hamun_tarbeck_quarters_lady",
                "hamun_tarbeck_treasury",
                "hamun_tarbeck_room_maidmaster",
                "hamun_tarbeck_room_temptations",
                "hamun_tarbeck_room_mirrors",
                "hamun_tarbeck_room_femdom",
                "hamun_tarbeck_room_orgy",
                "hamun_tarbeck_room_tentacle",
                "hamun_tarbeck_dining",
                "hamun_tarbeck_playhallway"
            ]

        def OverrideLocBg(self):
            Result = {}
            Result["hamun_tarbeck_mainhall"] = "cg_tarbeck_main_hall_night_party"
            Result["hamun_tarbeck_ballroom"] = "cg_tarbeck_ballroom_night_party"
            Result["hamun_tarbeck_room_maidmaster"] = "cg_tarbeck_master_maid_room_party"
            Result["hamun_tarbeck_room_mirrors"] = "cg_tarbeck_mirrors_party"
            Result["hamun_tarbeck_room_orgy"] = "cg_tarbeck_orgy_room_party"
            Result["hamun_tarbeck_room_temptations"] = "cg_tarbeck_tempt_room_party"
            return Result

        def onEnter(self):  
            wLocs["hamun_tarbeck_mainhall"].SetDayNightMatrixClass(None)
            wLocs["hamun_tarbeck_ballroom"].SetDayNightMatrixClass(None)
            # amb
            wLocs["hamun_tarbeck_mainhall"].withGenAmbience("audio/ambience_loc/party_crowd_talking.ogg")

            for LocID in self.TarbeckLocationIDs:
                wLocs[LocID].withGenMusic("audio/music/53_SunDance.ogg")

            if self.progress == 0:
                if GetLocID() == "hamun_hookah_bar":
                    if IsDaytime():
                        return TriggeredEvent("qst_TheTarbecks_MeetGarenFirstTimeAtPaleDragon") 
            elif self.progress == 1:
                if GetLocID() == "hamun_giselra_store":
                    if IsDaytime():
                        if self.ShowGiselraFirstQstEnterScene:
                            return TriggeredEvent("qst_TheTarbecks_VisitGiselraOrderClothes") 
            elif self.progress == 7:
                if GetLocID() == "hamun_tarbeck_mainhall":
                    return TriggeredEvent("qst_TheTarbecks_PartyBegins")
            elif self.progress == 8:
                if GetLocID() == "hamun_tarbeck_garden_main":
                    if self.IngridProgress == 0:
                        return TriggeredEvent("qst_TheTarbecks_Ingrid_ReturnToGarden")
                elif GetLocID() == "hamun_tarbeck_garden_east":
                    if self.IngridProgress == 1:
                        return TriggeredEvent("qst_TheTarbecks_Ingrid_Investigate")
            return

        def onStart(self):
            QstStart(HouseLockTarbeckHouse)
            return

        def onOver(self):
            CharSetBattleSkinID("mc", "mc_na")
            CharSetBattleSkinID("ves", "ves")
            CharSetBattleSkinID("kiara", "kiara")
            CharSetBattleSkinID("markus", "markus")

            wLocs["hamun_tarbeck_mainhall"].SetDayNightMatrixClass(MxDayNight_Desert)
            wLocs["hamun_tarbeck_ballroom"].SetDayNightMatrixClass(MxDayNight_Desert)
            # amb
            wLocs["hamun_tarbeck_mainhall"].withGenAmbience(None)

            # music
            for LocID in self.TarbeckLocationIDs:
                wLocs[LocID].withDayMusic("audio/music/43_Hamun_day.ogg")
                wLocs[LocID].withNightMusic("audio/music/44_Hamun_night.ogg")

            QstSetProgress(HouseLockTarbeckHouse, 1)

            if self.StashedPartyChars is not None:
                for CharID in self.StashedPartyChars:
                    PartyAddChar(CharID)

            CharSetClothes("ves",   "normal")
            CharSetClothes("markus","normal")
            CharSetClothes("kiara", "normal")
            CharSetClothes("esme",  "in_gold")
            CharSetClothes("sypha", "normal")
            CharSetClothes("mc",    "normal")

            BlockWaitGlobal(False)
            AutoTimeFreeze(False)

            TransformMC(False)
            TransformKiara(False)
            TransformMarkus(False)

            CharMeet("lady_tarbeck", Silent = True)
            CharMeet("lord_tarbeck", Silent = True)
            return

        def extraDialogue(self):
            if self.progress == 1:
                yield ("giselra_root", DNode(_("I’m looking to buy some new clothes."), "qst_TheTarbecks_GiselraBuyClothes"))
            elif self.progress == 2:
                yield ("giselra_root", DNode(_("Purchase clothes."), "qst_TheTarbecks_GiselraBuyClothesMenu"))
            elif self.progress == 3:
                if GetGameDay() < self.GiselraClothesReadyDay:
                    yield ("giselra_root", DNode(_("About my clothes..."), "qst_TheTarbecks_GiselraClothesTooEarly"))
                else:
                    yield ("giselra_root", DNode(_("About my clothes..."), "qst_TheTarbecks_GiselraClothesRetrieveAndContinue"))
            elif self.progress == 4:
                yield ("esme_root", DNode(_("I need a companion..."), "qst_TheTarbecks_SpeakToEsme", order = 1))

        def locationMod(self):
            btnMods = {}
            
            if self.progress == 5:
                if GetLocID() == "hamun_brothel":
                    if self.PartyCompanion == "esme":
                        btnMods["btn_hamun_brothel_esme_talk"] = BtnDisabled()
                elif GetLocID() == "hamun_dist_merch_lord":
                    if IsInTimeFrame(TIME_VISUAL_DUSK, TIME_VISUAL_DAWN):
                        btnMods["hamun_dist_merch_lord_to_tarbeck_mainhall"] = BtnJumpLabel(STR_LOC.HAMUN_TARBECK_ESTATE, "qst_TheTarbecks_ArriveToParty")
                    else:
                        btnMods["hamun_dist_merch_lord_to_tarbeck_mainhall"] = BtnJumpLabel(STR_LOC.HAMUN_TARBECK_ESTATE, "qst_TheTarbecks_ArriveToParty_AtDay")

            elif self.progress == 6:
                if GetLocID() == "hamun_tarbeck_mainhall":
                    btnMods["hamun_tarbeck_mainhall_to_dist_merch_lord"] = BtnJumpLabel(STR_LOC.HAMUN_DIST_MERCH_LORD, "qst_TheTarbecks_CantLeaveParty")
                    btnMods["hamun_tarbeck_mainhall_to_tarbeck_playhallway"] = BtnDisabled()
                    btnMods["hamun_tarbeck_mainhall_to_tarbeck_west_wing"] = BtnDisabled()
                    btnMods["hamun_tarbeck_mainhall_to_tarbeck_east_wing"] = BtnDisabled()
                elif GetLocID() == "hamun_tarbeck_garden_main":
                    btnMods["btn_hamun_tarbeck_garden_sypha"] = BtnJumpLabel(_("Sypha"), "qst_TheTarbecks_MeetSyphaInGarden")
                elif GetLocID() == "hamun_tarbeck_library":
                    btnMods["hamun_tarbeck_library_to_tarbeck_dining"] = BtnJumpLabel(STR_LOC.HAMUN_TARBECK_DINING, "qst_TheTarbecks_CantGoThere")

            elif self.progress == 7:
                if GetLocID() == "hamun_tarbeck_mainhall":
                    btnMods["hamun_tarbeck_mainhall_to_dist_merch_lord"] = BtnJumpLabel(STR_LOC.HAMUN_DIST_MERCH_LORD, "qst_TheTarbecks_CantLeaveParty")
                    btnMods["hamun_tarbeck_mainhall_to_tarbeck_playhallway"] = BtnDisabled()
                    btnMods["hamun_tarbeck_mainhall_to_tarbeck_west_wing"] = BtnDisabled()
                    btnMods["hamun_tarbeck_mainhall_to_tarbeck_east_wing"] = BtnDisabled()
                elif GetLocID() == "hamun_tarbeck_library":
                    btnMods["hamun_tarbeck_library_to_tarbeck_dining"] = BtnJumpLabel(STR_LOC.HAMUN_TARBECK_DINING, "qst_TheTarbecks_CantGoThere")
            
            elif self.progress in [8, 9]:
                if GetLocID() == "hamun_tarbeck_mainhall":
                    btnMods["hamun_tarbeck_mainhall_to_dist_merch_lord"] = BtnJumpLabel(STR_LOC.HAMUN_DIST_MERCH_LORD, "qst_TheTarbecks_CantLeaveParty")
                    btnMods["hamun_tarbeck_mainhall_to_tarbeck_west_wing"] = BtnDisabled()
                    btnMods["hamun_tarbeck_mainhall_to_tarbeck_east_wing"] = BtnDisabled()
                    btnMods["btn_hamun_tarbeck_mainhall_watcher"] = BtnJumpLabel(_("Talk to the Watcher"), "qst_TheTarbecks_WatcherMainhall_TurnInTokens")
                elif GetLocID() == "hamun_tarbeck_library":
                    btnMods["btn_hamun_tarbeck_library_lady_tarbeck"] = BtnJumpLabel(_("Talk to Lady Tarbeck"), "qst_TheTarbecks_TalkToLady")
                    btnMods["hamun_tarbeck_library_to_tarbeck_dining"] = BtnJumpLabel(STR_LOC.HAMUN_TARBECK_DINING, "qst_TheTarbecks_CantGoThere")
                elif GetLocID() == "hamun_tarbeck_garden_east":
                    if self.IngridProgress in [2, 3, 4]:
                        btnMods["btn_hamun_tarbeck_garden_east_ingrid"] = BtnJumpLabel(_("Talk to Lady Ingrid"), "qst_TheTarbecks_TalkToIngrid")
                elif GetLocID() == "hamun_tarbeck_playhallway":
                    btnMods["hamun_tarbeck_playhallway_to_tarbeck_room_maidmaster"] = BtnJumpLabel(STR_LOC.HAMUN_TARBECK_ROOM_MAIDMASTER, "qst_TheTarbecks_Room_Maid_main")
                    btnMods["hamun_tarbeck_playhallway_to_tarbeck_room_temptations"]= BtnJumpLabel(STR_LOC.HAMUN_TARBECK_ROOM_TEMPTATIONS,"qst_TheTarbecks_Room_Temptations_main")
                    btnMods["hamun_tarbeck_playhallway_to_tarbeck_room_mirrors"]     =BtnJumpLabel(STR_LOC.HAMUN_TARBECK_ROOM_MIRRORS,    "qst_TheTarbecks_Room_Mirrors_main")
                    btnMods["hamun_tarbeck_playhallway_to_tarbeck_room_femdom"]     = BtnJumpLabel(STR_LOC.HAMUN_TARBECK_ROOM_FEMDOM,     "qst_TheTarbecks_Room_Femdom_main")
                    btnMods["hamun_tarbeck_playhallway_to_tarbeck_room_orgy"]       = BtnJumpLabel(STR_LOC.HAMUN_TARBECK_ROOM_ORGY,       "qst_TheTarbecks_Room_Orgy_main")
                    btnMods["hamun_tarbeck_playhallway_to_tarbeck_room_tentacle"]   = BtnJumpLabel(STR_LOC.HAMUN_TARBECK_ROOM_TENTACLE,   "qst_TheTarbecks_Room_Tentacle_main")
            return LocButtonMod(directMods = btnMods, priority = 1)

        def RemoveNonCompanionChars(self):
            self.StashedPartyChars = copy.copy(player_party)
            for CharID in ["markus", "ves", "esme", "kiara", "sypha"]:
                if CharGetVar(CharID, "IsCompanion") == True:
                    if self.PartyCompanion != CharID:
                        PartyRemChar(CharID)

        def CalcGoldTokens(self):
            if self.progress == 8:
                if PlayerItemQty("qst_tarbeck_golden_token") >= 5:
                    GoalComplete(self, 8)
                    QstSetProgress(self, 9)
                    GoalShow(self, 101)

        def onComplete(self):
            QstStart(PrimerTheTarbecks2)
            QstSetDelay(PrimerTheTarbecks2, 1)
            return

image cg_corpse_eater:
    "cg_corpse_eater_base"
    zoom 0.7


label qst_TheTarbecks_CantGoThere:
    MC "(I can't go there, not now.)"
    $ LocEnterQ()

label qst_TheTarbecks_ArriveToParty_AtDay:
    MC "(I should come after dark, that's when the party starts.)"
    $ LocEnterQ()