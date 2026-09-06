init python:
    notesLib["dreamhouse_primer"] = Note(
        # a note added when player is approached by a guard with quest invite
        _("Head to the Faymore Estate and meet with the Faymores."),
        _("Approached by a guard carrying a letter from the wealthy Faymores, I was asked to visit them at once... I wonder what this is about?"),
        trackTag = "hamun_dist_merch_lord_to_faymore_manor",
    )

    @AppendToAllQuests
    class PrimerDreamhouse(LogicModule):
        # prog 0 is guard-trigger prog 
        # prog 1 is visit faymore estate
        def onEnter(self):
            if self.progress == 0:
                if IsDaytime():
                    if GetLocID() in ["hamun_dist_docks", "hamun_dist_merch_lord"]:
                        return TriggeredEvent("qst_dreamhouse_primer_letter")
            elif self.progress == 1:
                if GetLocID() == "hamun_faymore_manor":
                    return TriggeredEvent("qst_dreamhouse_enter_manor")
            return

        def extraDialogue(self):
            if self.progress == 1:
                yield ("faymore_guard_root", DNode(_("I was summoned here. (Show the document)."), "qst_dreamhouse_primer_approach_estate", order = 100))

        def onComplete(self):
            QstStart(DialogueAnya)
            QstStart(DialogueChanyi)
            return

    @AppendToAllQuests
    class QstDreamhouse(BaseQuest):
        TITLE = _("The Dream House")
        DESCRIPTION = _("The Faymore's daughter has vanished, and I have been tasked with her rescue. The girl seemed to have some kind of unusual power related to her nightmares...")
        GOALS = {
            0: QuestStage(_("Find whereabouts on Serafina's father at the Hamun library"), 
                trackTag = "hamun_dist_merch_lord_to_library",
                hintTxt = _("Serafina's father, an inquisitor, was seen visiting a library shortly before Serafina's disappearance... Perhaps I can find some information there about where he went.")), 
            1: QuestStage(_("Speak to a merchant who may know more."),
                hintTxt = _("Whatever Davik was planning, he was looking to hire sellswords and would have needed to stock up on supplies. He must have approached a merchant...")),
            # goal appears when you talk to katiya about inquisitor
            2: QuestStage(_("Accept Katiya's offer"), 
                trackTag = "hamun_docks_to_store",
                hintTxt = _("Katiya is willing to give me information on the whereabouts of Serafina and her father... But only if I agree to help her.")),
            3: QuestStage(_("Recover Katiya's missing supply wagon"), 
                trackTagWorldMap = "ancient_forest",
                hintTxt = _("Katiya has given me the location of where Serafina and Davik went... In return, she wants me to recover her lost supply wagon... It has to be nearby, right?")), 
            4: QuestStage(_("Escape the Dream House."), 
                hintTxt = _("The door sealed behind us when we entered the strange house and now we cannot leave! There must be a way out of this strange place...")), 

            # shown after you talk to davik on l2 start and he explains the layers thing
            5: QuestStage(_("Head to the master bedroom once you have the key."), 
                hintTxt = _("The master bedroom... It's the only way to escape to the next 'layer' of this nightmare house. We must find the key and escape through the master bedroom to get out of here!")), 
            6: QuestStage(_("Return to the Faymore estate"),
                trackTag = "hamun_dist_merch_lord_to_faymore_manor",
                hintTxt = _("With their daughter rescued, I must now head back to report on what happened.")),
        }
        SIMPLE_GOALS = False

        def __init__(self):
            super().__init__()
            self.XpReward = 2200
            self.suggestedLevel = 12
            ####################################################
            self.ChosenReward = 0 # 0 is ass 1 is coin
            self.KatiyaNegotiatedFor = None # "tits", "discount", "supplies"
            self.ShowPostKatiyaThreat = True
            self.SeenEnterForestOneOff = False
            self.HouseStage = 1 # 1-5 are "layers" and 6 is post-layers 
            ### L1
            self.L1_SeenEnterHouseOneOff = False
            self.L1_SeenDiningHallEnterOneOff = False
            self.L1_SeenKitchenEnterOneOff = False
            self.L1_SeenCellarEnterOneOff = False
            self.L1_SeenLibraryEnterOneOff = False
            self.L1_TookSmallMystKey = False
            self.L1_TookRedSkullKey = False
            self.L1_UnlockedStudy = False
            ### L2
            self.L2_FoughtBathtubZombie = False # <- moonlights as oneoff flag
            self.L2_SeenNurseryOneOff = False
            self.L2_SeenDiningOneOff = False
            self.L2_SeenKitchenOneOff = False
            self.L2_UnlockedCellarDoor = False
            self.L2_TookDullKey = False
            self.L2_TookBlueSkullKey = False
            self.L2_SeenLibraryOneOff = False
            ### L3
            self.L3_StashedCharGear = {} # charID:{slotid:itemid, slotid:itemid, itemid}
            self.L3_TouchedMirror = False
            self.L3_GrannyCounter = 0 # when this reaches 10, she catches up
            self.L3_GrannyActive = False
            self.L3_TookCribKey = False
            self.L3_DiningUnlocked = False
            self.L3_GaveCatPet = False
            self.L3_SeenKitchenPot = False
            self.L3_CheckedPotions = False
            self.L3_StudyUnlocked = False
            self.L3_SeenLibraryShelves2 = False
            self.L3_CheckedWitchShrine = False
            ### L4
            self.L4_TookTotemBath = False
            self.L4_Hallway2Unlocked = False
            self.L4_Toys_ToSee = {"illusion", "liberation", "death"}
            self.L4_SeenCrib = False
            self.L4_Diningroom_StuffToSee = {"food", "wine", "cake"}
            self.L4_Kitchen_TookPotions = False
            self.L4_Kitchen_TastedStew = False
            self.L4_UnlockedCellar = False
            self.L4_BarrelsLeft = {"skull", "eyes", "heart", "wings"}
            self.L4_LibSeenBurningBook = False
            self.L4_LibSeenGreenSkullBook = False
            self.L4_UnlockedLibrary = False
            self.L4_UnlockedMasterBedroom = False
            ### L5
            self.L5_Hallway2Unlocked = False
            self.L5_TookCribKey = False
            self.L5_BedroomUnlocked = False
            self.L5_UnlockedCellar = False
            self.L5_TookCellarKey = False
            self.L5_TookGatorKey = False
            self.L5_GatorCounter = 0
            self.L5_GatorTakenCharsnGear = {}  # charID:{slotid:itemid, slotid:itemid, itemid}
            #######
            self.SerafOutcome = None # "father" or "virgo"

##############################
        # granny bs
        # removes all chars from player party & saves what their gear was for auto-equip
        def SuspendPartyChars(self):
            for CharID in [CharID for CharID in store.player_party if CharID != "mc"]:
                self.L3_StashedCharGear[CharID] = {}
                for SlotID in EQP_SLOTS.ALL:
                    if worldChars[CharID][SlotID] is not None:
                        ItemID = worldChars[CharID][SlotID]
                        self.L3_StashedCharGear[CharID][SlotID] = ItemID
                        PlayerRemItem(ItemID, Silent = True, MuteSfx = True)
                PartyRemChar(CharID, Silent = True)
            return

        def RestorePartyChars(self):
            for CharID, ItemData in self.L3_StashedCharGear.items():
                PartyAddChar(CharID, Silent = True)
                for SlotID, ItemID in ItemData.items():
                    PlayerAddItem(ItemID, Silent = True)
                    PlayerPartyCharEquipItem(CharID, ItemID)
            return

        # gator bs
        def GatorEatsChar(self, CharID):
            self.L5_GatorTakenCharsnGear[CharID] = {}
            for SlotID in EQP_SLOTS.ALL:
                if worldChars[CharID][SlotID] is not None:
                    ItemID = worldChars[CharID][SlotID]
                    self.L5_GatorTakenCharsnGear[CharID][SlotID] = ItemID
                    PlayerRemItem(ItemID, Silent = True, MuteSfx = True)
            PartyRemChar(CharID, Silent = True)
            return

        def RestoreGatorTakenChars(self):
            for CharID, ItemData in self.L5_GatorTakenCharsnGear.items():
                PartyAddChar(CharID, Silent = True)
                for SlotID, ItemID in ItemData.items():
                    PlayerAddItem(ItemID, Silent = True)
                    PlayerPartyCharEquipItem(CharID, ItemID)
            return

##############################

        def extraDialogue(self):
            if IsGoalVisible(self, 0):
                yield ("numa_root", DNode(_("An inquisitor visited here about a month ago..."), "qst_dreamhouse_numa_talk", order = 100))
            elif IsGoalVisible(self, 1):
                yield ("katiya_root", DNode(_("Did an inquisitor named Davik stop by here recently to buy supplies?"), "qst_dreamhouse_talk_katiya", order = 100))
            elif IsGoalVisible(self, 2):
                yield ("katiya_root", DNode(_("About your offer..."), "qst_dreamhouse_talk_katiya", order = 100))

        def OverrideLocBg(self):
            Result = {}
            # L2
            if self.HouseStage == 2:
                if GetLocID() == "dreamhouse_nursery":
                    Result["dreamhouse_nursery"] = "bg_dreamhouse_l2_nursery"
                elif GetLocID() == "dreamhouse_diningroom":
                    Result["dreamhouse_diningroom"] = "bg_dreamhouse_l2_diningroom"
                elif GetLocID() == "dreamhouse_kitchen":
                    Result["dreamhouse_kitchen"] = "bg_dreamhouse_l2_kitchen"
                elif GetLocID() == "dreamhouse_library":
                    Result["dreamhouse_library"] = "bg_dreamhouse_l2_library"
                elif GetLocID() == "dreamhouse_hallway":
                    Result["dreamhouse_hallway"] = "bg_dreamhouse_l2_entrance"
                elif GetLocID() == "dreamhouse_cellar":
                    Result["dreamhouse_cellar"] = "bg_dreamhouse_l2_cellar"
                elif GetLocID() == "dreamhouse_study":
                    Result["dreamhouse_study"] = "bg_dreamhouse_l2_study"
                elif GetLocID() == "dreamhouse_hallway_upstairs":
                    Result["dreamhouse_hallway_upstairs"] = "bg_dreamhouse_l2_hallway_upstairs"
                elif GetLocID() == "dreamhouse_bathroom":
                    Result["dreamhouse_bathroom"] = "bg_dreamhouse_l2_bathroom"
                elif GetLocID() == "dreamhouse_hallway2":
                    Result["dreamhouse_hallway2"] = "bg_dreamhouse_l2_hallway2"

            # L3
            elif self.HouseStage == 3:
                if GetLocID() == "dreamhouse_nursery":
                    Result["dreamhouse_nursery"] = "bg_dreamhouse_l3_nursery"
                elif GetLocID() == "dreamhouse_diningroom":
                    Result["dreamhouse_diningroom"] = "bg_dreamhouse_l3_diningroom"
                elif GetLocID() == "dreamhouse_kitchen":
                    Result["dreamhouse_kitchen"] = "bg_dreamhouse_l3_kitchen"
                elif GetLocID() == "dreamhouse_library":
                    Result["dreamhouse_library"] = "bg_dreamhouse_l3_library"
                elif GetLocID() == "dreamhouse_hallway":
                    Result["dreamhouse_hallway"] = "bg_dreamhouse_l3_entrance"
                elif GetLocID() == "dreamhouse_cellar":
                    Result["dreamhouse_cellar"] = "bg_dreamhouse_l3_cellar"
                elif GetLocID() == "dreamhouse_study":
                    Result["dreamhouse_study"] = "bg_dreamhouse_l3_study"
                elif GetLocID() == "dreamhouse_hallway_upstairs":
                    Result["dreamhouse_hallway_upstairs"] = "bg_dreamhouse_l3_hallway_upstairs"
                elif GetLocID() == "dreamhouse_bathroom":
                    Result["dreamhouse_bathroom"] = "bg_dreamhouse_l3_bathroom"
                elif GetLocID() == "dreamhouse_hallway2":
                    Result["dreamhouse_hallway2"] = "bg_dreamhouse_l3_hallway2"

            # L4
            elif self.HouseStage == 4:
                if GetLocID() == "dreamhouse_nursery":
                    Result["dreamhouse_nursery"] = "bg_dreamhouse_l4_nursery"
                elif GetLocID() == "dreamhouse_diningroom":
                    Result["dreamhouse_diningroom"] = "bg_dreamhouse_l4_diningroom"
                elif GetLocID() == "dreamhouse_kitchen":
                    Result["dreamhouse_kitchen"] = "bg_dreamhouse_l4_kitchen"
                elif GetLocID() == "dreamhouse_library":
                    Result["dreamhouse_library"] = "bg_dreamhouse_l4_library"
                elif GetLocID() == "dreamhouse_hallway":
                    Result["dreamhouse_hallway"] = "bg_dreamhouse_l4_entrance"
                elif GetLocID() == "dreamhouse_cellar":
                    Result["dreamhouse_cellar"] = "bg_dreamhouse_l4_cellar"
                elif GetLocID() == "dreamhouse_study":
                    Result["dreamhouse_study"] = "bg_dreamhouse_l4_study"
                elif GetLocID() == "dreamhouse_hallway_upstairs":
                    Result["dreamhouse_hallway_upstairs"] = "bg_dreamhouse_l4_hallway_upstairs"
                elif GetLocID() == "dreamhouse_bathroom":
                    Result["dreamhouse_bathroom"] = "bg_dreamhouse_l4_bathroom"
                elif GetLocID() == "dreamhouse_hallway2":
                    Result["dreamhouse_hallway2"] = "bg_dreamhouse_l4_hallway2"
            # L5
            elif self.HouseStage == 5:
                if GetLocID() == "dreamhouse_nursery":
                    Result["dreamhouse_nursery"] = "bg_dreamhouse_l5_nursery"
                elif GetLocID() == "dreamhouse_diningroom":
                    Result["dreamhouse_diningroom"] = "bg_dreamhouse_l5_diningroom"
                elif GetLocID() == "dreamhouse_kitchen":
                    Result["dreamhouse_kitchen"] = "bg_dreamhouse_l5_kitchen"
                elif GetLocID() == "dreamhouse_library":
                    Result["dreamhouse_library"] = "bg_dreamhouse_l5_library"
                elif GetLocID() == "dreamhouse_hallway":
                    Result["dreamhouse_hallway"] = "bg_dreamhouse_l5_entrance"
                elif GetLocID() == "dreamhouse_cellar":
                    Result["dreamhouse_cellar"] = "bg_dreamhouse_l5_cellar"
                elif GetLocID() == "dreamhouse_hallway_upstairs":
                    Result["dreamhouse_hallway_upstairs"] = "bg_dreamhouse_l5_hallway_upstairs"
                elif GetLocID() == "dreamhouse_bathroom":
                    Result["dreamhouse_bathroom"] = "bg_dreamhouse_l5_bathroom"
                elif GetLocID() == "dreamhouse_hallway2":
                    Result["dreamhouse_hallway2"] = "bg_dreamhouse_l5_hallway2"

            return Result

        def onEnter(self):
            # getting-to
            if IsGoalVisible(self, 3):
                if GetLocID() == "hamun_dist_docks":
                    if self.ShowPostKatiyaThreat == True:
                        return TriggeredEvent("qst_dreamhouse_after_katiya")
                elif GetLocID() == "ancient_forest":
                    if self.SeenEnterForestOneOff == False:
                        return TriggeredEvent("qst_dreamhouse_enter_forest")

            if self.HouseStage == 1:
                if GetLocID() == "dreamhouse_hallway":
                    if self.L1_SeenEnterHouseOneOff == False:
                        return TriggeredEvent("qst_dreamhouse_enter_house")
                elif GetLocID() == "dreamhouse_diningroom":
                    if self.L1_SeenDiningHallEnterOneOff == False:
                        return TriggeredEvent("qst_dreamhouse_l1_dining_oneoff")
                elif GetLocID() == "dreamhouse_kitchen":
                    if self.L1_SeenKitchenEnterOneOff == False:
                        return TriggeredEvent("qst_dreamhouse_l1_kitchen_oneoff")
                elif GetLocID() == "dreamhouse_cellar":
                    if self.L1_SeenCellarEnterOneOff == False:
                        return TriggeredEvent("qst_dreamhouse_l1_cellar_oneoff")
                elif GetLocID() == "dreamhouse_library":                    
                    if self.L1_SeenLibraryEnterOneOff == False:
                        return TriggeredEvent("qst_dreamhouse_l1_library_oneoff")
            # L2
            elif self.HouseStage == 2:
                if GetLocID() == "dreamhouse_nursery":
                    if self.L2_SeenNurseryOneOff == False:
                        return TriggeredEvent("qst_dreamhouse_l2_nursery_oneoff")
                elif GetLocID() == "dreamhouse_diningroom":
                    if self.L2_SeenDiningOneOff == False:
                        return TriggeredEvent("qst_dreamhouse_l2_dining_oneoff")
                elif GetLocID() == "dreamhouse_kitchen":
                    if self.L2_SeenKitchenOneOff == False:
                        return TriggeredEvent("qst_dreamhouse_l2_kitchen_oneoff")
                elif GetLocID() == "dreamhouse_library":
                    if self.L2_SeenLibraryOneOff == False:
                        return TriggeredEvent("qst_dreamhouse_l2_library_oneoff")
                elif GetLocID() == "dreamhouse_bathroom":
                    if self.L2_FoughtBathtubZombie == False:
                        return TriggeredEvent("qst_dreamhouse_l2_bathroom_oneoff")

            if IsGoalVisible(self, 6):
                if GetLocID() == "hamun_faymore_manor":
                    return TriggeredEvent("qst_dreamhouse_return_after_rescue")

        def onEnterOnce(self):            
            # L3
            if self.HouseStage == 3:
                if self.L3_GrannyActive:
                    return TriggeredEvent("qst_dreamhouse_l3_granny_counter")
            # L5
            elif self.HouseStage == 5:
                return TriggeredEvent("qst_dreamhouse_l5_gator_counter")

        def onStart(self):
            if QstIsActive(PrimerDreamhouse):
                QstComplete(PrimerDreamhouse)
            return

        def onComplete(self):
            # canon is, player romances chanyi and anya (ass chosen)
            WorldMapLocAdd("nubarian_tribelands")
            WorldMapLocAdd("ancient_forest")
            if not QstIsActive(HouseLockDreamhouse):
                QstStart(HouseLockDreamhouse)
            QstSetProgress(HouseLockDreamhouse, 1)
            if not CharIsMet("chanyi"):
                CharMeet("chanyi", Silent = True)
            if not CharIsMet("anya"):
                CharMeet("anya", Silent = True)
            # canon is, negotiated for tits
            if self.KatiyaNegotiatedFor is None:
                self.KatiyaNegotiatedFor = "tits"
                DialogueKatiya().AlwaysShowTits = True

            if self.SerafOutcome is None:
                self.SerafOutcome = "virgo"

            if self.SerafOutcome == "virgo":
                QstStart(DialogueSerafina, Silent = True)
                if not QstIsActive(HouseLockFaymoreManor):
                    QstStart(HouseLockFaymoreManor)
                if QstGetProgress(HouseLockFaymoreManor) != 1:
                    QstSetProgress(HouseLockFaymoreManor, 1)
                HouseLockFaymoreManor().UnlockedSerafinaRoom = True
                if self.ChosenReward == 0:
                    QstStart(RomanceFaymoreGirls, Silent = True)
                    RomanceFaymoreGirls().ScheduledSexEventAt = (GetGameDay() + 1)
                    NoteUnlock("romance_faymore_meet_at_next_night")
            return

        def locationMod(self):
            btnMods = {}
            btnMods["dreamhouse_hallway_to_outside"] = BtnJumpLabel(_("Leave"), "qst_dreamhouse_cant_exit")
            if self.HouseStage == 1:
                # l1 clickables
                btnMods["dreamhouse_bathroom_bathtub"] = BtnJumpLabel(_("Bathtub"), "qst_dreamhouse_l1_bathtub")
                btnMods["dreamhouse_bathroom_mirror"] = BtnJumpLabel(_("Mirror"), "qst_dreamhouse_l1_mirror")
                btnMods["dreamhouse_nursery_toys"] = BtnJumpLabel(_("Toys"), "qst_dreamhouse_l1_toys")
                btnMods["dreamhouse_nursery_crib"] = BtnJumpLabel(_("Crib"), "qst_dreamhouse_l1_crib")
                btnMods["dreamhouse_hallway2_to_bedroom"] = BtnJumpLabel(STR_LOC.DREAMHOUSE_BEDROOM, "qst_dreamhouse_l1_bedroom")
                btnMods["dreamhouse_hallway_candle"] = BtnJumpLabel(_("Candle"), "qst_dreamhouse_l1_candle")
                btnMods["dreamhouse_diningroom_table"] = BtnJumpLabel(_("A set dinner table"), "qst_dreamhouse_l1_table")
                btnMods["dreamhouse_diningroom_wolfhead"] = BtnJumpLabel(_("Mounted wolf head"), "qst_dreamhouse_l1_wolfhead")
                btnMods["dreamhouse_diningroom_portrait"] = BtnJumpLabel(_("Portrait of family"), "qst_dreamhouse_l1_portrait")
                btnMods["dreamhouse_kitchen_cupboards"] = BtnJumpLabel(_("Cupboards"), "qst_dreamhouse_l1_kitchen_cupboards")
                btnMods["dreamhouse_kitchen_pot"] = BtnJumpLabel(_("Cooking pot"), "qst_dreamhouse_l1_kitchen_pot")
                btnMods["dreamhouse_kitchen_table"] = BtnJumpLabel(_("Note on the table"), "qst_dreamhouse_l1_kitchen_table")
                btnMods["dreamhouse_cellar_barrel"] = BtnJumpLabel(_("Wine barrel"), "qst_dreamhouse_l1_cellar_barrel")
                if self.L1_TookSmallMystKey == False:
                    btnMods["dreamhouse_cellar_papers"] = BtnJumpLabel(_("Scattered paperwork"), "qst_dreamhouse_l1_cellar_paper")
                btnMods["dreamhouse_library_portrait"] = BtnJumpLabel(_("Portrait of a smiling hanged man"), "qst_dreamhouse_l1_library_portrait")
                btnMods["dreamhouse_library_books_1"] = BtnJumpLabel(_("Bookshelf"), "qst_dreamhouse_l1_library_bookshelf_1")
                btnMods["dreamhouse_library_books_2"] = BtnJumpLabel(_("Bookshelf"), "qst_dreamhouse_l1_library_bookshelf_2")
                btnMods["dreamhouse_library_fireplace"] = BtnJumpLabel(_("Fireplace"), "qst_dreamhouse_l1_library_fireplace")
                if self.L1_UnlockedStudy == True:
                    btnMods["dreamhouse_library_to_study"] = BtnChangeLoc(STR_LOC.DREAMHOUSE_STUDY, "dreamhouse_study")
                if self.L1_TookRedSkullKey == False:
                    btnMods["dreamhouse_study_desk"] = BtnJumpLabel(_("Desk"), "qst_dreamhouse_l1_study_desk")
            elif self.HouseStage == 2:
                if self.L2_UnlockedCellarDoor == False:
                    if self.L2_TookDullKey == False:
                        btnMods["dreamhouse_bathroom_bathtub"] = BtnJumpLabel(_("Bathtub"), "qst_dreamhouse_l2_bathtub")
                btnMods["dreamhouse_bathroom_mirror"] = BtnJumpLabel(_("Mirror"), "qst_dreamhouse_l2_mirror")
                btnMods["dreamhouse_nursery_toys"] = BtnJumpLabel(_("Toys"), "qst_dreamhouse_l2_toys")
                btnMods["dreamhouse_nursery_crib"] = BtnJumpLabel(_("Crib"), "qst_dreamhouse_l2_crib")
                btnMods["dreamhouse_hallway2_to_bedroom"] = BtnJumpLabel(STR_LOC.DREAMHOUSE_BEDROOM, "qst_dreamhouse_l2_bedroom_door")
                btnMods["dreamhouse_hallway_candle"] = BtnJumpLabel(_("Candle"), "qst_dreamhouse_l2_candle")
                btnMods["dreamhouse_diningroom_table"] = BtnJumpLabel(_("Gore covered dinner table"), "qst_dreamhouse_l2_table")
                btnMods["dreamhouse_diningroom_wolfhead"] = BtnJumpLabel(_("Mounted wolf head"), "qst_dreamhouse_l2_wolfhead")
                btnMods["dreamhouse_diningroom_portrait"] = BtnJumpLabel(_("Portrait of dead family"), "qst_dreamhouse_l2_portrait")
                btnMods["dreamhouse_kitchen_cupboards"] = BtnJumpLabel(_("Bloody cupboards"), "qst_dreamhouse_l2_kitchen_cupboards")
                btnMods["dreamhouse_kitchen_pot"] = BtnJumpLabel(_("Cooking pot"), "qst_dreamhouse_l2_kitchen_pot")
                btnMods["dreamhouse_kitchen_table"] = BtnJumpLabel(_("Child's letter on table"), "qst_dreamhouse_l2_kitchen_table")
                if self.L2_UnlockedCellarDoor == False:
                    btnMods["dreamhouse_kitchen_to_cellar"] = BtnJumpLabel(STR_LOC.DREAMHOUSE_CELLAR, "qst_dreamhouse_l2_kitchen_to_cellar")
                btnMods["dreamhouse_cellar_barrel"] = BtnJumpLabel(_("Blood barrel"), "qst_dreamhouse_l2_cellar_barrel")
                if self.L2_TookBlueSkullKey == False:
                    btnMods["dreamhouse_cellar_mercenary"] = BtnJumpLabel(_("Dead mercenary"), "qst_dreamhouse_l2_dead_mercenary")
                btnMods["dreamhouse_library_portrait"] = BtnJumpLabel(_("Portrait of a smiling hanged man"), "qst_dreamhouse_l2_library_portrait")
                btnMods["dreamhouse_library_books_1"] = BtnJumpLabel(_("Bookshelf"), "qst_dreamhouse_l2_library_bookshelf_1")
                btnMods["dreamhouse_library_books_2"] = BtnJumpLabel(_("Bookshelf"), "qst_dreamhouse_l2_library_bookshelf_2")
                btnMods["dreamhouse_library_fireplace"] = BtnJumpLabel(_("Fireplace"), "qst_dreamhouse_l2_library_fireplace")
            elif self.HouseStage == 3:
                btnMods["dreamhouse_bathroom_bathtub"] = BtnJumpLabel(_("Bathtub"), "qst_dreamhouse_l3_bathtub")
                if self.L3_TouchedMirror == False:
                    btnMods["dreamhouse_bathroom_mirror"] = BtnJumpLabel(_("Mirror"), "qst_dreamhouse_l3_mirror")
                btnMods["dreamhouse_nursery_toys"] = BtnJumpLabel(_("Toys"), "qst_dreamhouse_l3_toys")
                if self.L3_TookCribKey == False:
                    btnMods["dreamhouse_nursery_crib"] = BtnJumpLabel(_("Crib"), "qst_dreamhouse_l3_crib")
                btnMods["dreamhouse_hallway_candle"] = BtnJumpLabel(_("Candle"), "qst_dreamhouse_l3_candle")
                if self.L3_DiningUnlocked == False:
                    btnMods["dreamhouse_hallway_to_diningroom"] = BtnJumpLabel(STR_LOC.DREAMHOUSE_DININGROOM, "qst_dreamhouse_l3_diningdoor")
                btnMods["dreamhouse_diningroom_table"] = BtnJumpLabel(_("Set table with dolls around"), "qst_dreamhouse_l3_table")
                if self.L3_GaveCatPet == False:
                    btnMods["dreamhouse_diningroom_wolfhead"] = BtnJumpLabel(_("Mounted cat head"), "qst_dreamhouse_l3_head")
                btnMods["dreamhouse_diningroom_portrait"] = BtnJumpLabel(_("Portrait of Granny Oh Dreary surrounded by children"), "qst_dreamhouse_l3_portrait")
                btnMods["dreamhouse_kitchen_cupboards"] = BtnJumpLabel(_("Cupboards"), "qst_dreamhouse_l3_kitchen_cupboards")
                if self.L3_SeenKitchenPot == False:
                    btnMods["dreamhouse_kitchen_pot"] = BtnJumpLabel(_("Cooking pot"), "qst_dreamhouse_l3_kitchen_pot")
                
                if self.L3_CheckedPotions == False:
                    btnMods["dreamhouse_cellar_barrel"] = BtnJumpLabel(_("Potions"), "qst_dreamhouse_l3_cellar_barrel")
                if self.L3_StudyUnlocked == False:
                    btnMods["dreamhouse_cellar_papers"] = BtnJumpLabel(_("Key box"), "qst_dreamhouse_l3_cellar_paper")
                #btnMods["dreamhouse_hallway2_to_bedroom"] = BtnJumpLabel(STR_LOC.DREAMHOUSE_BEDROOM, "qst_dreamhouse_l1_bedroom")

                if self.L3_StudyUnlocked == False:
                    btnMods["dreamhouse_library_portrait"] = BtnJumpLabel(_("Portrait of Granny Oh Dreary"), "qst_dreamhouse_l3_library_portrait")
                btnMods["dreamhouse_library_books_1"] = BtnJumpLabel(_("Bookshelf"), "qst_dreamhouse_l3_library_bookshelf_1")
                if self.L3_SeenLibraryShelves2 == False:
                    btnMods["dreamhouse_library_books_2"] = BtnJumpLabel(_("Bookshelf"), "qst_dreamhouse_l3_library_bookshelf_2")
                btnMods["dreamhouse_library_fireplace"] = BtnJumpLabel(_("Fireplace"), "qst_dreamhouse_l3_library_fireplace")
                btnMods["dreamhouse_library_floorstuff"] = BtnJumpLabel(_("Human sacrifice"), "qst_dreamhouse_l3_library_sacrifice")
                if self.L3_StudyUnlocked == True:
                    btnMods["dreamhouse_library_to_study"] = BtnChangeLoc(STR_LOC.DREAMHOUSE_STUDY, "dreamhouse_study")
                if self.L3_CheckedWitchShrine == False:
                    btnMods["dreamhouse_study_desk"] = BtnJumpLabel(_("Witch shrine"), "qst_dreamhouse_l3_study_desk")
                btnMods["dreamhouse_hallway2_to_bedroom"] = BtnJumpLabel(STR_LOC.DREAMHOUSE_BEDROOM, "qst_dreamhouse_l3_bedroom_door")
            elif self.HouseStage == 4:
                if self.L4_TookTotemBath == False:
                    btnMods["dreamhouse_bathroom_bathtub"] = BtnJumpLabel(_("Bathtub"), "qst_dreamhouse_l4_bathtub")
                btnMods["dreamhouse_bathroom_mirror"] = BtnJumpLabel(_("Mirror"), "qst_dreamhouse_l4_mirror")
                if self.L4_Hallway2Unlocked == False:
                    btnMods["dreamhouse_upstairs_to_hallway2"] = BtnJumpLabel(STR_LOC.DREAMHOUSE_HALLWAY2, "qst_dreamhouse_l4_upstairs_to_hallway2")
                if len(self.L4_Toys_ToSee) > 0:
                    btnMods["dreamhouse_nursery_toys"] = BtnJumpLabel(_("Toys"), "qst_dreamhouse_l4_toys")
                if self.L4_SeenCrib == False:
                    btnMods["dreamhouse_nursery_crib"] = BtnJumpLabel(_("Crib"), "qst_dreamhouse_l4_crib")
                btnMods["dreamhouse_hallway_candle"] = BtnJumpLabel(_("Candle"), "qst_dreamhouse_l4_candle")
                if len(self.L4_Diningroom_StuffToSee) > 0:
                    btnMods["dreamhouse_diningroom_table"] = BtnJumpLabel(_("Set dinner table"), "qst_dreamhouse_l4_table")
                btnMods["dreamhouse_diningroom_wolfhead"] = BtnJumpLabel(_("Mounted boar head"), "qst_dreamhouse_l4_boarhead")
                btnMods["dreamhouse_diningroom_portrait"] = BtnJumpLabel(_("A portrait of a family... But it feels eerie somehow."), "qst_dreamhouse_l4_portrait")
                if self.L4_Kitchen_TookPotions == False:
                    btnMods["dreamhouse_kitchen_cupboards"] = BtnJumpLabel(_("Cupboards"), "qst_dreamhouse_l4_kitchen_cupboards")
                if self.L4_Kitchen_TastedStew == False:
                    btnMods["dreamhouse_kitchen_pot"] = BtnJumpLabel(_("Cooking pot"), "qst_dreamhouse_l4_kitchen_pot")
                btnMods["dreamhouse_kitchen_table"] = BtnJumpLabel(_("Letter on the table"), "qst_dreamhouse_l4_kitchen_table")
                if self.L4_UnlockedCellar == False:
                    btnMods["dreamhouse_kitchen_to_cellar"] = BtnJumpLabel(STR_LOC.DREAMHOUSE_CELLAR, "qst_dreamhouse_l4_kitchen_to_cellar")

                if len(self.L4_BarrelsLeft) > 0:
                    btnMods["dreamhouse_cellar_barrel"] = BtnJumpLabel(_("Wine barrels"), "qst_dreamhouse_l4_cellar_barrel")

                btnMods["dreamhouse_cellar_papers"] = BtnJumpLabel(_("Notes"), "qst_dreamhouse_l4_cellar_paper")
                if self.L4_UnlockedLibrary == False:
                    btnMods["dreamhouse_diningroom_to_library"] = BtnJumpLabel(STR_LOC.DREAMHOUSE_LIBRARY, "qst_dreamhouse_l4_diningroom_to_library")

                btnMods["dreamhouse_library_portrait"] = BtnJumpLabel(_("A portrait of a hanged man with a broken neck still smiling..."), "qst_dreamhouse_l4_library_portrait")
                btnMods["dreamhouse_library_books_1"] = BtnJumpLabel(_("Bookshelf"), "qst_dreamhouse_l4_library_bookshelf_1")
                btnMods["dreamhouse_library_books_2"] = BtnJumpLabel(_("Bookshelf"), "qst_dreamhouse_l4_library_bookshelf_2")
                btnMods["dreamhouse_library_fireplace"] = BtnJumpLabel(_("Fireplace"), "qst_dreamhouse_l4_library_fireplace")
                btnMods["dreamhouse_hallway2_to_bedroom"] = BtnJumpLabel(STR_LOC.DREAMHOUSE_BEDROOM, "qst_dreamhouse_l4_bedroom_door")

            elif self.HouseStage == 5:
                btnMods["dreamhouse_bathroom_bathtub"] = BtnJumpLabel(_("Bathtub"), "qst_dreamhouse_l5_bathtub")
                btnMods["dreamhouse_bathroom_mirror"] = BtnJumpLabel(_("Mirror"), "qst_dreamhouse_l5_mirror")
                if self.L5_Hallway2Unlocked == False:
                    btnMods["dreamhouse_upstairs_to_hallway2"] = BtnJumpLabel(STR_LOC.DREAMHOUSE_HALLWAY2, "qst_dreamhouse_l5_upstairs_to_hallway2")
                btnMods["dreamhouse_nursery_toys"] = BtnJumpLabel(_("Destroyed toys"), "qst_dreamhouse_l5_toys")
                if self.L5_TookCribKey == False:
                    btnMods["dreamhouse_nursery_crib"] = BtnJumpLabel(_("Crib"), "qst_dreamhouse_l5_crib")
                if self.L5_BedroomUnlocked == False:
                    btnMods["dreamhouse_hallway2_to_bedroom"] = BtnJumpLabel(STR_LOC.DREAMHOUSE_BEDROOM, "qst_dreamhouse_l5_bedroom_door")
                btnMods["dreamhouse_hallway_candle"] = BtnJumpLabel(_("Candle"), "qst_dreamhouse_l5_candle")
                btnMods["dreamhouse_diningroom_table"] = BtnJumpLabel(_("Ruined table"), "qst_dreamhouse_l5_table")
                btnMods["dreamhouse_diningroom_wolfhead"] = BtnJumpLabel(_("Mounted lizard head"), "qst_dreamhouse_l5_head")
                btnMods["dreamhouse_diningroom_portrait"] = BtnJumpLabel(_("Portrait of house in a swamp"), "qst_dreamhouse_l5_portrait")
                btnMods["dreamhouse_kitchen_cupboards"] = BtnJumpLabel(_("Cupboards"), "qst_dreamhouse_l5_kitchen_cupboards")
                btnMods["dreamhouse_kitchen_pot"] = BtnJumpLabel(_("Cooking pot"), "qst_dreamhouse_l5_kitchen_pot")
                if self.L5_UnlockedCellar == False:
                    btnMods["dreamhouse_kitchen_to_cellar"] = BtnJumpLabel(STR_LOC.DREAMHOUSE_CELLAR, "qst_dreamhouse_l5_kitchen_to_cellar")
                btnMods["dreamhouse_cellar_barrel"] = BtnJumpLabel(_("Destroyed wine barrel"), "qst_dreamhouse_l5_cellar_barrel")
                if self.L5_TookCellarKey == False:
                    btnMods["dreamhouse_cellar_papers"] = BtnJumpLabel(_("Scattered paperwork"), "qst_dreamhouse_l5_cellar_paper")
                if self.L5_TookGatorKey == False:
                    btnMods["dreamhouse_library_fireplace"] = BtnJumpLabel(_("Fireplace"), "qst_dreamhouse_l5_library_fireplace")
                btnMods["dreamhouse_library_portrait"] = BtnJumpLabel(_("Portrait of two yellow eyes above a dark waterline"), "qst_dreamhouse_l5_library_portrait")
                btnMods["dreamhouse_library_books_1"] = BtnJumpLabel(_("Bookshelf"), "qst_dreamhouse_l5_library_bookshelf_1")
                btnMods["dreamhouse_library_books_2"] = BtnJumpLabel(_("Bookshelf"), "qst_dreamhouse_l5_library_bookshelf_2")

            return LocButtonMod(directMods = btnMods)

