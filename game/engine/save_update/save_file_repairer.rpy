# these are for development
# !!! all these should be false in public builds
define DEBUG_SkipSaveUpdate         = False # on: save update will be skipped
define DEBUG_ForceSaveUpdate        = False # on: save update will happen regardless of version
define DEBUG_ShowSaveUpdateMessages = False # on: debug 'say' messages will be spammed around
define DEBUG_BypassDevFixup         = False # on: will bypass dev-only fixup-part
define DEBUG_ShowCheatMenu          = False # on: will show cheat menu regardless of whether cheat was entered
define DEBUG_AllowRollbackAfterLoad = (True if config.developer else False) # on: rollback after load will be allowed


default SaveGameVersion = config.version
# for pre-0.162 saves mostly, tells if the save went thru the update cycle at least once
default SaveGameWasNeverUpdated = True
default GameStartedOnVersion = "pre-0.168"

label after_load:
    if DEBUG_ShowSaveUpdateMessages:
        "DEBUG: Entering after_load label"
        "DEBUG: Save version [SaveGameVersion], game version [config.version]"
        if SaveGameWasNeverUpdated == True:
            "DEBUG: Save was never updated before"
    if DEBUG_SkipSaveUpdate:
        return

    # case 0 dev mode, do some stuff EARLIER
    if config.developer:
        if DEBUG_BypassDevFixup == False:
            call save_state_update_shared from _call_save_state_update_shared# from _call_save_state_update

    # case 1, thats a save that never went thru the update process (pre-0.162)
    if SaveGameWasNeverUpdated == True:
        if DEBUG_ShowSaveUpdateMessages:
            "DEBUG: Since save was never updated before, setting version to 0.000 and entering update procedure"
        $ SaveGameVersion = "0.000"
        call save_state_update from _call_save_state_update_1
    # case 2, the save has legitimate SaveGameVersion we can use
    else:
        if SaveGameVersion < config.version:
            if DEBUG_ShowSaveUpdateMessages:
                "DEBUG: Save game has a version and it is less than current game version, entering update procedure"
            call save_state_update from _call_save_state_update_2

        elif SaveGameVersion > config.version:
            "(WARNING: This save was made on a newer version of the game. Continue at your own risk as it might cause unexpected behaviour.)"
            # if we're here, save needs no updatin based on stored version        


    $ SaveGameWasNeverUpdated = False

    if not DEBUG_AllowRollbackAfterLoad:
        $ renpy.block_rollback()

    if DEBUG_ShowSaveUpdateMessages:
        "DEBUG: Returning from after_load label"
    return

label save_state_update:
    $ cheat_menu_bool = False

    $ SaveFileRepairerTmpScope = {}
    $ SaveFileRepairerTmpScope["ScheduledTeleportToCityGates"] = False

    if DEBUG_ShowSaveUpdateMessages:
        "DEBUG: In save update routine"
    #################
###### for all saves prior to 0.162
    if SaveGameVersion < "0.162" or DEBUG_ForceSaveUpdate:
        if DEBUG_ShowSaveUpdateMessages:
            "DEBUG: Doing pre-0.162 update section"

        # this will refresh ves to her "level 7" stats for old saves, 10/12/2024
        if not CharInParty("ves"):
            $ SaveFileRepairerTmpScope["ves_relation"] = worldChars["ves"]["relation"]
            $ worldChars["ves"] = PBCharacter("ves")
            # if ves was a lover, re-add her to lovers
            if QstIsActive(RomanceVes) and QstGetProgress(RomanceVes) >= 10:
                $ CharSetLover("ves", Silent = True)
                $ worldChars["ves"]["relation"] = SaveFileRepairerTmpScope["ves_relation"]

        # drax crafting
        if not hasattr(store, "DraxCraftRecipesAndIngredientsContainer"):
            $ setattr(store, "DraxCraftRecipesAndIngredientsContainer", {})

        # fixes thea not being present due to missing charmeet
        if QstIsOver(EventAdventureGuildShowUp):
            if worldChars["thea"]["relstatus"] == "rel_lover":
                $ CharMeet("thea", Silent = True, DefaultRel = "rel_lover")
            else:
                $ CharMeet("thea", Silent = True)

        # charmeets for callie & trayan based on quest completion
        if QstGuildPriceLife().times_completed > 0:
            $ CharMeet("callie", Silent = True)
            if QstGuildPriceLife().times_completed > 1:
                $ CharMeet("trayan", Silent = True)

        # add kiara rooftop vag flag if player saw her rooftop scene
        if "kiara" in persistent.galleryUnlocks:
            if "rooftop" in persistent.galleryUnlocks["kiara"]:
                if persistent.galleryUnlocks["kiara"]["rooftop"]["unlocked"] == True:
                    $ UnlockGalFlag("kiara", "rooftop", "vag")

        # delete unused variable
        if hasattr(store, "CanExplore"):
            $ delattr(store, "CanExplore")

        # deleting nav-related variables 
        if hasattr(store, "Routes"):
            $ delattr(store, "Routes")

        if hasattr(store, "current_node_loc"):
            $ delattr(store, "allow_quit_navigation_menu")
            $ delattr(store, "auto_navigation_until")
            $ delattr(store, "stop_auto_navigating")
            $ delattr(store, "selected_node")
            $ delattr(store, "current_route_random_locs")
            $ delattr(store, "current_node_loc")

            if getattr(store, "current_route", None) is not None:
                # fingers crossed
                if hasattr(store, "loc"):
                    if loc.goalTag in ["travel_node_mine", "travel_node_vizura_caravan", "travel_node_generic"]:
                        $ SaveFileRepairerTmpScope["ScheduledTeleportToCityGates"] = True
                else:
                    if GetLocID() in ["travel_node_mine", "travel_node_vizura_caravan", "travel_node_generic"]:
                        $ SaveFileRepairerTmpScope["ScheduledTeleportToCityGates"] = True
            $ delattr(store, "current_route")

        if not hasattr(store, "shop_hamun_general"):
            # add new store
            $ setattr(store, "shop_hamun_general", {"discount":0.0, "items":{}})

        # add another new store (carina's dealer)
        if not hasattr(store, "shop_novaras_dealer"):
            $ setattr(store, "shop_novaras_dealer", {"discount":0.0, "items":{}})

        # add FinishOrder to all quests
        $ SAVEFIX_AddFinishOrderFieldToAllQuests()

        # quest hooks
        if QstIsOver(QstHighFasion) and QstIsOver(QstTwoEmperors):
            if not QstIsOver(PrimerBeneathTheShadows):
                $ QstStart(PrimerBeneathTheShadows)

        if QstIsOver(EventNovarasMarkusTavernTwoEmps):
            if not QstIsOver(PrimerTheComingStorm):
                $ QstStart(PrimerTheComingStorm)

        # missing field
        # canon is, alysha lives
        if not hasattr(QstTheSlavemaster(), "AlyshaDead"):
            $ QstTheSlavemaster().AlyshaDead = False

        # dev-only missing fields
        if not hasattr(QstJudgementDay(), "CharactersWhoWereAtTheWall"):
            $ QstJudgementDay().CharactersWhoWereAtTheWall = set()
        if not hasattr(QstJudgementDay(), "ImprisonedCharacters"):
            $ QstJudgementDay().ImprisonedCharacters = set()

        # regina char-related vars
        if "hood" not in worldChars["regina"]:
            # hopefully they did not save during a robe scene
            $ worldChars["regina"].props["hood"] = False
        
        if "clothes" not in worldChars["drax"]:
            $ worldChars["drax"].props["clothes"] = "normal"

        if "story_form" not in worldChars["kiara"]:
            $ worldChars["kiara"].props["story_form"] = "normal"

        # kiara
        if worldChars["kiara"]["HasAltForm"] == False:
            $ worldChars["kiara"]["HasAltForm"] = True

            $ worldChars["kiara"]["AltForm_BattleClass"] = "banshee"
            $ worldChars["kiara"]["AltForm_CharSkills"] = {"BansheeMoonlightDance": 1, "BansheeASongOfPain":1}
            $ worldChars["kiara"]["AltForm_BattleSkin"] = "kiara_banshee"
            $ worldChars["kiara"]["AltForm_TransformSkill"] = "KiaraTransform"
            $ worldChars["kiara"]["AltForm_UnTransformSkill"] = "KiaraUnTransform"

            $ worldChars["kiara"]["AltForm_SkillPoints"] = ClampValue(GetCharLevelFromID("kiara") - 4, 1, 666)


        if QstIsOver(QstJudgementDay):
            $ worldChars["kiara"]["AltForm_Unlocked"] = True
        else:
            $ worldChars["kiara"]["AltForm_Unlocked"] = False

        # dev-missing dialogue init
        if QstIsOver(QstJudgementDay):
            if not QstIsActive(DialogueNuma):
                $ QstStart(DialogueNuma)

        # missing rel-char
        $ CharAddRelEntry("marion", "initial")

        # missing erika class
        if worldChars["erika"]["BattleClass"] != "inquisitor":
            $ worldChars["erika"]["BattleClass"] = "inquisitor"
            $ worldChars["erika"]["CharSkills"] = {"InquisitorBurningJudgement": 1, "InquisitorFirewall":1}

        $ SaveGameVersion = "0.162"
    #################
###### 0.162 to 0.163
    if SaveGameVersion == "0.162":
        if DEBUG_ShowSaveUpdateMessages:
            "DEBUG: Doing 0.162-0.163 update section"

        # missing erika skin
        $ worldChars["erika"]["BattleSkin"] = "erika"

        # try brute-force pers. gallery unlocks into a dict
        if not isinstance(persistent.galleryUnlocks, dict):
            $ persistent.galleryUnlocks = dict()

        $ SaveGameVersion = "0.163"
    #################
###### 0.163 to 0.164
    if SaveGameVersion == "0.163":
        if DEBUG_ShowSaveUpdateMessages:
            "DEBUG: Doing 0.163-0.164 update section"

        # mika quest force end
        if IsGoalComplete(QstGirlTroubles, 3):
            if QstIsActive(QstGirlTroubles):
                $ QstComplete(QstGirlTroubles, Silent = True)

        if QstIsComplete(QstLetsCelebrate):
            if not QstIsActive(RomanceMika): 
                $ QstStart(RomanceMika, Silent = True)

        # brute-force pers. gallery unlocks into a dict
        # (should already be a dict because same shit happens on startup)
        if not isinstance(persistent.galleryUnlocks, dict):
            $ persistent.galleryUnlocks = dict()

        # new qst field
        $ SAVEFIX_AddQuestOverShowInHistoryToAllQuests()

        # lovers path + lets celebrate OR friends' path in mika qst autocompleting the other w/o rewards
        if QstIsComplete(QstLetsCelebrate):
            $ QstABestFriendsPath().isOver = True
            $ QstABestFriendsPath().isComplete = True
            $ QstABestFriendsPath().FinishOrder = store.QuestsFinished
            $ QstABestFriendsPath().QuestOverShowInHistory = False
            $ store.QuestsFinished += 1

        elif QstIsComplete(QstABestFriendsPath):
            $ QstLetsCelebrate().isOver = True
            $ QstLetsCelebrate().isComplete = True
            $ QstLetsCelebrate().FinishOrder = store.QuestsFinished
            $ QstLetsCelebrate().QuestOverShowInHistory = False
            $ store.QuestsFinished += 1
            $ QstTheLoversPath().isOver = True
            $ QstTheLoversPath().isComplete = True
            $ QstTheLoversPath().FinishOrder = store.QuestsFinished
            $ QstTheLoversPath().QuestOverShowInHistory = False
            $ store.QuestsFinished += 1

        # duct-tape for non-locked note
        if QstIsOver(QstLittleLies):
            $ NoteLock("LittleLiesNote")

        $ SaveGameVersion = "0.164"

    #################
###### 0.164 to 0.165
    if SaveGameVersion == "0.164":
        if DEBUG_ShowSaveUpdateMessages:
            "DEBUG: Doing 0.164-0.165 update section"

        # adara dream event 
        # & ship thing 
        # & alysha meet
        if QstIsOver(QstJudgementDay):
            # adara dream
            $ QstStart(EventAdaraDreamAct2Start)
            # ship crashed
            $ QstStart(EventCrashedShipEncounter)

            # alysha
            if QstIsOver(QstTheSlavemaster):
                if not QstTheSlavemaster().AlyshaDead:
                    $ worldChars["alysha"] = PBCharacter("alysha")
                    $ CharMeet("alysha", Silent = True)

            # marion meet
            $ CharMeet("marion", Silent = True, DefaultRel = "rel_enemy")

            # sophira killed during siege
            if not CharIsAlive("sophira"):
                $ CharAddRelEntry("sophira", "died_during_siege")

        # borras, duprey, kiara prologue
        if not CharIsAlive("borras"):
            $ CharAddRelEntry("borras", "prol_killed")

        if not CharIsAlive("duprey"):
            $ CharAddRelEntry("duprey", "prol_killed")

        if QstIsOver(QstTheDarkPass):
            $ CharAddRelEntry("kiara", "prol_killed")

        # kiara revive missing entry
        if QstIsOver(EventNovarasMarkusTavernTwoEmps):
            if not CharIsAlive("kiara"):
                $ CharUnKill("kiara")
                if worldChars["kiara"]["romanced"]:
                    $ CharAddRelEntry("kiara", "revive_romance")
                else:
                    $ CharAddRelEntry("kiara", "revive_no_romance")

        # add "killed by tarek", checks if nijah dead AND NOT because of siege
        if not CharIsAlive("nijah"):
            if "died_during_siege" not in worldChars["nijah"]["RelTextIDs"]:
                $ CharAddRelEntry("nijah", "killed_by_tarek")

        # mr winward killed during jackpot
        if not CharIsAlive("mr_winward"):
            $ CharAddRelEntry("mr_winward", "killed_by_mc_jackpot")

        # missing locks & chars (smithy, miningco)
        if QstIsOver(QstJudgementDay):
            if not QstIsActive(DialogueMarbella):
                $ QstStart(DialogueMarbella)
            if not QstIsActive(HouseLockHamunSmithy):
                $ QstStart(HouseLockHamunSmithy)
                $ QstStart(DialogueBeshar)

        # beshar shop
        if not hasattr(store, "shop_hamun_smithy"):
            $ setattr(store, "shop_hamun_smithy", {"discount":0.0, "items":{}})

        # beshar crafting
        if not hasattr(store, "HamunSmithyCraftRecipesAndIngredientsContainer"):
            $ setattr(store, "HamunSmithyCraftRecipesAndIngredientsContainer", {})

        # both recipes lists get overwritten with sets    
        $ DraxCraftRecipes = {
            "reinforced_leather_armor", 
            "chainmail", 
            "bronze_armor", 
            "iron_armor", 
            "steel_armor", 
            "syaxian_armor", 
            "steel_sword", 
            "iron_sword", 
            "bronze_sword"}

        $ HamunSmithyCraftRecipes = {
            "chainmail", 
            "bronze_armor", 
            "iron_armor", 
            "iron_sword", 
            "bronze_sword", 
            "bronlite_armor", 
            "bronlite_dagger", 
            "bronlite_sword", 
            "reinf_desert_robes", 
            "ring_of_wealth"}

        # adding missing fields to comingstorm qst
        # vala investigation route
        $ QstTheComingStorm().ValaInvestigationOpenedSpecialBookshelf = False 
        $ QstTheComingStorm().ValaInvestigationDistractedBanditsDuringChase = False 
        $ QstTheComingStorm().ValaInvestigationGoldStashDayPassed = False 
        $ QstTheComingStorm().ValaInvestigationPath = False 
        $ QstTheComingStorm().SpecialBooksContainer = {}

        # valchek route
        $ QstTheComingStorm().ValchekSawMarketEnterScene = False 
        $ QstTheComingStorm().ValchekLuciusMalArrangeCost = 300
        $ QstTheComingStorm().ValchekMetLuciusOnce = False

        # mika bj flag unfuck
        if "mika" in persistent.galleryUnlocks:
            if "mika_bj_suck" in persistent.galleryUnlocks:
                $ UnlockGalFlag("mika", "mika_bj_suck", "var_nopreg_dress", notify = False)

            if "mika_missionary" in persistent.galleryUnlocks:
                $ UnlockGalFlag("mika", "mika_missionary", "nopreg_vag")

        # kiara bat form to normal form
        if QstIsOver(QstJudgementDay):
            if worldChars["kiara"]["story_form"] == "demorai":
                $ worldChars["kiara"]["story_form"] = "normal"

        $ SaveGameVersion = "0.165"

### yes we could just set it to conf. ver but that way we get clear control of save update sequence
    #################
    if SaveGameVersion == "0.165":
        if DEBUG_ShowSaveUpdateMessages:
            "DEBUG: Doing 0.165-0.166 update section"
        $ SaveGameVersion = "0.166"
    #################
    if SaveGameVersion == "0.166":
        if DEBUG_ShowSaveUpdateMessages:
            "DEBUG: Doing 0.166-0.167 update section"
        $ SaveGameVersion = "0.167"
    #################
    if SaveGameVersion == "0.167": # that was nosteam-only
        if DEBUG_ShowSaveUpdateMessages:
            "DEBUG: Doing 0.167-0.168 update section"
        # SOME reported errors with this missing
        if not hasattr(PregMika(), "told_about_preg_two"):
            $ PregMika().told_about_preg_two = False
        $ SaveGameVersion = "0.168"
    #################
    if SaveGameVersion == "0.168": # < that was steam-only
        if DEBUG_ShowSaveUpdateMessages:
            "DEBUG: Doing 0.168-0.169 update section"

        # on all these old saves, they could enter cheats in main menu 
        # and that would disable achievements in next new game
        # so we re-enable regardless
        $ store._enable_achievements = True

        # pers. note on winward leather
        if QstIsActive(DialogueMrsWinward) and QstGetProgress(DialogueMrsWinward) > 0:
            $ NoteUnlock("winward_leather_bring", Silent = True)

        # pers. note on income
        if DialogueMarbella().InvestLevel > 0:
            $ NoteUnlock("MiningCoIncome", Silent = True)

        $ SaveGameVersion = "0.169"
    #################
    if SaveGameVersion == "0.169": # < steam and nosteam
        # update hangings event
        $ EventNovarasHangings().progress = 0
        $ EventNovarasHangings().IntervalInDays = 7  # < - how many days between each event happening
        $ EventNovarasHangings().ClickableLocID = LocEvent_GetFreeNovarasDistrict()
        $ EventNovarasHangings().VariantsListOriginal = [1, 2, 3, 4, 5]
        $ EventNovarasHangings().VariantsListDynamic = []
        $ EventNovarasHangings().SeenToday = False

        # update prophet
        $ EventMadProphet().IntervalInDays = 8
        $ EventMadProphet().ClickableLocID = LocEvent_GetFreeNovarasDistrict()
        $ EventMadProphet().SeenToday = False

        # finish prophetizing
        if QstIsOver(QstJudgementDay):
            $ QstComplete(EventMadProphet)

        $ SaveGameVersion = "0.170"
    #################
    if SaveGameVersion == "0.170": # < steam

        if worldChars["kiara"]["story_form"] == "normal":
            $ worldChars["kiara"]["story_form"] = "human"

        if worldChars["kiara"]["clothes"] == "scout":
            $ worldChars["kiara"].props["default_look"] = "scout"
            $ worldChars["kiara"]["clothes"] = "normal"
        elif worldChars["kiara"]["clothes"] == "hooded":
            $ worldChars["kiara"].props["default_look"] = "hooded"
            $ worldChars["kiara"]["clothes"] = "normal"

        if QstIsOver(EventNovarasMarkusTavernTwoEmps):
            $ worldChars["kiara"].props["default_look"] = "hooded"
        else:
            $ worldChars["kiara"].props["default_look"] = "scout"

        if worldChars["kiara"]["default_look"] == "hooded":
            $ worldChars["kiara"]["portrait"] = "images/characters/kiara/portrait_hooded.webp"

        # these 'build' calls are to reset character data in save, which in turn will update their portrait
        $ CreateWorldCharFromID("zara")

        if CharIsAlive("alysha"):
            $ CreateWorldCharFromID("alysha")
        else:
            $ CreateWorldCharFromID("alysha")
            $ CharKill("alysha")
        
        $ CreateWorldCharFromID("marbella")
        $ CreateWorldCharFromID("numa")

        # add missing field
        $ HouseLockFortSebastian().CanEnterFreely = False
        # and set it
        if QstIsOver(QstDarkKnight):
            $ HouseLockFortSebastian().CanEnterFreely = True
        else:
            if QstIsActive(QstDarkKnight):
                if QstDarkKnight().wasBriefed:
                    $ HouseLockFortSebastian().CanEnterFreely = True

        if hasattr(store, "notifyM"):
            $ delattr(store, "notifyM")

        $ SaveGameVersion = "0.171"
    #################
    if SaveGameVersion == "0.171":
        $ SaveGameVersion = "0.172"
    #################
    if SaveGameVersion == "0.172":
        $ setattr(store, "bookshelf_library_novaras", dict())
        $ DialogueVala().AddBooks()
        if hasattr(DialogueVala(), "bookshelf"):
            $ delattr(DialogueVala(), "bookshelf")

        $ setattr(store, "bookshelf_library_hamun", dict())
        $ DialogueNuma().AddBooks()
        if hasattr(DialogueNuma(), "Books"):
            $ delattr(DialogueNuma(), "Books")

        $ setattr(store, "bookshelf_comingstorm_special", dict())
        $ AddItemTo(bookshelf_comingstorm_special, "book_dreams_of_astatar")
        $ AddItemTo(bookshelf_comingstorm_special, "book_the_first_darkness")
        $ AddItemTo(bookshelf_comingstorm_special, "book_loving_ophelia")
        if hasattr(QstTheComingStorm(), "SpecialBooksContainer"):
            $ delattr(QstTheComingStorm(), "SpecialBooksContainer")

        $ SaveGameVersion = "0.173"

    #################
    if SaveGameVersion == "0.173":
        
        if QstIsOver(QstDarkKnight):
            $ HouseLockFortSebastian().CanEnterFreely = True
        else:
            if QstIsActive(QstDarkKnight):
                if QstDarkKnight().wasBriefed or QstGetProgress(QstDarkKnight) >= 1:
                    $ HouseLockFortSebastian().CanEnterFreely = True

        $ SaveGameVersion = "0.174"

    #################
    if SaveGameVersion == "0.174":
        if QstIsOver(QstJudgementDay):
            if not QstIsActive(DialogueLuna):
                $ QstStart(DialogueLuna)

            if not QstIsActive(DialogueKiara):
                $ QstStart(DialogueKiara)

            $ QstStart(PrimerTheBeastOfNovaras)
            $ QstStart(HamunArena)

            # adding pontetially missing image definition
            $ ZANZIBAT =    Character(_("Zanzibat"),    image = "zanzibat")
            $ DRAMORA =     Character(_("Dramora"),     image = "dramora")

            if "zanzibat" in worldChars:
                if "summary_initial" not in worldChars["zanzibat"]["RelTextIDs"]:
                    $ CharAddRelEntry("zanzibat", "summary_initial")

        if "sypha" in worldChars:
            $ worldChars["sypha"]["BattleSkin"] = "sypha"

            $ worldChars["sypha"]["BattleClass"] = "assassin"
            $ worldChars["sypha"]["CharSkills"] = {"AssassinDeathByAThousandCuts":1, "AssassinADarkGift":1}

        $ SaveGameVersion = "0.175"
    #################
    if SaveGameVersion == "0.175":

        if QstGetProgress(QstTheBeastOfNovaras) >= 5:
            $ TransformMC(False)
            $ TransformMarkus(False)

        if QstIsOver(QstTheDarkPass):
            if "directly_added_attribute_points" not in worldChars["mc"].props:
                $ worldChars["mc"].props["directly_added_attribute_points"] = 0
            $ worldChars["mc"].props["directly_added_attribute_points"] += 8
            if "directly_added_attribute_points" not in worldChars["markus"].props:
                $ worldChars["markus"].props["directly_added_attribute_points"] = 0
            $ worldChars["markus"].props["directly_added_attribute_points"] += 6

        if QstIsOver(RomanceNyx) == False:
            if QstIsActive(RomanceNyx) == False:
                if QstIsFailed(QstTheSlavemaster):
                    $ QstStart(RomanceNyx)

        if "zanzibat" in worldChars:
            if "summary_initial" not in worldChars["zanzibat"]["RelTextIDs"]:
                $ CharAddRelEntry("zanzibat", "summary_initial")

        $ SaveGameVersion = "0.176"
    #################
    if SaveGameVersion == "0.176":
        if hasattr(store, "DEV_VARS"):
            $ del DEV_VARS

        ### preg myu
        if hasattr(store, "myu_child_name"):
            $ PregMyu().LastBornBabyName = myu_child_name
            $ del myu_child_name
        if hasattr(store, "mika_child_name"):
            $ PregMika().LastBornBabyName = mika_child_name
            $ del mika_child_name
        if hasattr(store, "nijah_childname"):
            $ PregNijah().LastBornBabyName = nijah_childname
            $ del nijah_childname

        $ SAVEFIX_UpdateCharPregModules0176()
        
        if hasattr(store, "loc"):
            $ store.PlayerPos = loc
            $ store.PlayerPos.DoExitCheck = False
            $ del loc
            #else:
            #    $ store.PlayerPos = WorldPosition()

        if QstIsOver(QstJudgementDay):
            $ QstStart(DialogueGiselra)

        if QstIsOver(QstTheBeastOfNovaras):
            $ QstStart(PrimerTheTarbecks)
            $ QstSetDelay(PrimerTheTarbecks, 2)

        $ SaveGameVersion = "0.177"

    ##################
    if SaveGameVersion == "0.177":
        if QstIsOver(QstJudgementDay):
            $ QstStart(DialogueGiselra)

        $ SaveGameVersion = "0.178"
    ##################
    if SaveGameVersion in ["0.178", "0.179", "0.180", "0.181"]:
        # (did a skip of few empty blocks here tee-hee)
        $ SaveGameVersion = "0.182"
    ##################
    if SaveGameVersion == "0.182":
        if QstIsOver(QstJudgementDay):
            if not QstIsActive(DialogueKatiya):
                $ QstStart(DialogueKatiya)

        if hasattr(store, "shop_hamun_smithy"):
            if QstIsActive(DialogueBeshar):
                $ ShopHamunSmithy().Items = copy.deepcopy(shop_hamun_smithy["items"])
                $ ShopHamunSmithy().Discount = shop_hamun_smithy["discount"]
                $ ShopHamunSmithy().isActive = True
                $ QstSetProgress(ShopHamunSmithy, 0)
            $ del shop_hamun_smithy

        if hasattr(store, "shop_novaras_general"):
            if QstIsActive(DialogueLuciusMal):
                $ ShopNovarasGeneral().Items = copy.deepcopy(shop_novaras_general["items"])
                $ ShopNovarasGeneral().Discount = shop_novaras_general["discount"]
                $ ShopNovarasGeneral().isActive = True # <- careful manual direct start
                $ QstSetProgress(ShopNovarasGeneral, 0)
            $ del shop_novaras_general

        if hasattr(store, "shop_novaras_dealer"):
            if QstIsActive(NovarasDealer):
                $ ShopNovarasDealer().Items = copy.deepcopy(shop_novaras_dealer["items"])
                $ ShopNovarasDealer().Discount = shop_novaras_dealer["discount"]
                $ ShopNovarasDealer().isActive = True
                $ QstSetProgress(ShopNovarasDealer, 0)
            $ del shop_novaras_dealer

        if hasattr(store, "shop_hamun_general"):
            if QstIsActive(DialogueKatiya):
                $ ShopHamunGeneral().Items = copy.deepcopy(shop_hamun_general["items"])
                $ ShopHamunGeneral().Discount = shop_hamun_general["discount"]
                $ ShopHamunGeneral().isActive = True
                $ QstSetProgress(ShopHamunGeneral, 0)
            $ del shop_hamun_general

        if hasattr(store, "shop_vizura_general"):
            if QstIsActive(VizuraCaravan):
                $ ShopVizuraCaravan().Items = copy.deepcopy(shop_vizura_general["items"])
                $ ShopVizuraCaravan().Discount = shop_vizura_general["discount"]
                # manual start, scary
                $ ShopVizuraCaravan().isActive = True
                $ QstSetProgress(ShopVizuraCaravan, 0)
            $ del shop_vizura_general

        if hasattr(store, "shop_drax_smithy"):
            if QstIsActive(DialogueDrax):
                $ ShopNovarasSmithy().Items = copy.deepcopy(shop_drax_smithy["items"])
                $ ShopNovarasSmithy().Discount = shop_drax_smithy["discount"]
                $ ShopNovarasSmithy().isActive = True
                $ QstSetProgress(ShopNovarasSmithy, 0)
            $ del shop_drax_smithy

        if QstIsActive(DialogueVala):
            $ QstStart(ShopNovarasLibrary)
        if QstIsActive(RomanceNijah):
            if RomanceNijah().investBusiness == True:
                $ QstStart(ShopNijahStall)
        if QstIsActive(DialogueButcher):
            $ QstStart(ShopNovarasButcher)
        if QstIsActive(DialogueNuma):
            $ QstStart(ShopHamunLibrary)

        if QstIsOver(QstTheBeastOfNovaras):
            $ QstStart(PrimerBigTroubleLH)
            $ QstStart(DialogueZanzibat)

        $ BuildAllItemContainers()
        $ SAVEFIX_ConvertItemsFromIndexesToIDs()
        if hasattr(store, "world_items"):
            $ del world_items

        $ SaveGameVersion = "0.183"

    if SaveGameVersion == "0.183":
        $ SaveGameVersion = "0.184"

    if SaveGameVersion == "0.184":
        # reinit for proper new font
        $ BABAZHUL_MAD = Character(_("Babazhul"), what_color = "#69ffe3", what_style = "babazhul_mad_text", image = "babazhul")
        if DialogueNuma().SeenFirstMeet == True:
            $ CharMeet("numa", Silent = True)
        if QstGetProgress(DialogueMarbella) > 0:
            $ CharMeet("marbella", Silent = True)
        if QstIsOver(QstTheBeastOfNovaras):
            $ QstSetProgress(DialogueGiselra, 1)

        $ SaveGameVersion = "0.185"

    if SaveGameVersion in ["0.185", "0.186", "0.187", "0.188", "0.189"]:
        $ SaveGameVersion = "0.190"

    if SaveGameVersion == "0.190":
        $ SaveGameVersion = "0.191"

    if SaveGameVersion == "0.191":
        if QstIsOver(QstTheBeastOfNovaras):
            $ QstStart(PrimerDreamhouse)
        $ SaveGameVersion = "0.192"

    if SaveGameVersion == "0.192":
        if QstIsActive(QstNewMyu):
            if QstGetProgress(QstNewMyu) == 0:
                while GetItemQty(ShopNovarasGeneral().Items, "qst_sweet_roll") < 3:
                    $ AddItemTo(ShopNovarasGeneral().Items, "qst_sweet_roll", 1)
        # duct tape for likely bug w/regina name
        if CharGetVar("regina", "name") == erika_ref_cap:
            $ CharSetName("regina", store.regina_ref_cap)
        $ SaveGameVersion = "0.193"

    if SaveGameVersion == "0.193":
        if QstIsOver(QstTheTarbecks):
            $ QstStart(PrimerTheTarbecks2)
            $ QstSetDelay(PrimerTheTarbecks2, 1)
        $ MARKUS_FEM = Character(_("Marcia"), image = "markus_fem")
        $ SaveGameVersion = "0.194"

    if SaveGameVersion == "0.194":
        if QstIsOver(QstFromAnotherWorld):
            $ QstStart(EventFortressInn)
        $ SaveGameVersion = "0.195"

    if SaveGameVersion == "0.195":
        $ SaveGameVersion = "0.196"

    if SaveGameVersion == "0.196":
        if QstIsOver(QstTheTarbecks2):
            $ QstStart(RomanceLadyTarbeck)
        # patch up preg events
        if PregHamunTrio().NumImpregs == 1:
            $ PregHamunTrio().ShowPostImpreg_First = True
        elif PregHamunTrio().NumImpregs >= 2:
            $ PregHamunTrio().ShowPostImpreg_Rep = True
        if PregHamunTrio().NumBirths == 1:
            $ PregHamunTrio().ShowPostBirth_First = True
        elif PregHamunTrio().NumBirths >= 2:
            $ PregHamunTrio().ShowPostBirth_Rep = True
        $ SaveGameVersion = "0.197"

    if SaveGameVersion == "0.197":
        $ SAVEFIX_InitializeMissingWorldChars()
        $ worldChars["lady_tarbeck"].props["variant"] = "normal"
        $ worldChars["lady_tarbeck"].props["darkmage_mask"] = False
        if QstIsActive(RomanceLadyTarbeck):
            if QstGetProgress(RomanceLadyTarbeck) >= 5:
                $ CharSetLover("lady_tarbeck", Silent = True)
        $ SaveGameVersion = "0.198"

    if SaveGameVersion == "0.198":
        $ SaveGameVersion = "0.199"

    if SaveGameVersion == "0.199":
        if QstIsOver(QstFromAnotherWorld):
            $ QstStart(TravelNodesRandomizer)
        # Fix: Add Python prefix '$' and reference the class safely via ItemActionLib or the global store
        $ store.BattleItemAction_PotionHealMinor = ItemActionLib.get("potion_heal_minor")
        $ SaveGameVersion = "0.200"

    # after a build, add a new block ~up here
###### SAVE_UPDATE_ANCHOR ^

    call save_state_update_shared from _call_save_state_update_shared_1

    if SaveFileRepairerTmpScope["ScheduledTeleportToCityGates"] == True:
        call screen ok_popup(label = _("Developers note"), text = _("Due to changes made to the travel system since your save was made,\nthe game will try to teleport you to the Novaras City gates as a bug prevention measure."))
        $ LocSet("novaras_gates")
        $ LocFlush(dissolve)

    $ SaveFileRepairerTmpScope = {}
    $ NotifHardClear()

    $ AddNotif(tra(_("Your save has been updated to version %s!")) % SaveGameVersion, Kind = "save_related")
    return


label save_state_update_shared:
    ### WARNING: order here kinda matters, be wary swapping shit around (chars vs items mostly)
    $ SAVEFIX_InitializeMissingWorldChars()
    $ SAVEFIX_UpdateCharTemplateRefAndDeleteObsoleteChars()
    $ SAVEFIX_AddMissingCharPropsFromTemplate()
    $ SAVEFIX_UnequipAllItemsForAwayCompanions()
    $ SAVEFIX_RecalcAttrSkillPointsForPartyChars()
    $ SAVEFIX_QstDeleteObsolete()
    $ SAVEFIX_QstCreateMissing()
    #### items
    $ BuildAllItemContainers()          # creates all the variables like "house chest" or "hamun store"
    $ SAVEFIX_UpdateAllLogicModuleFields()
    $ RelSet_Regina()
    $ RelSet_Erika()
    return

init python:
    # for that rare case where people had galleyUnlocks as different type
    if not isinstance(persistent.galleryUnlocks, dict):
        persistent.galleryUnlocks = dict()

    # to find fucked up (in rel. screen sense) world chars on old saves
    def DEBUG_PrintCharsThatHaveMCFaceAsPortrait():
        for CharID, CharData in worldChars.items():
            if CharID == "mc":
                continue
            if CharData["portrait"] == "characters/mc/portrait.webp":
                print("DEBUG: world char %s has mc face as portrait" % CharID)
        return

###############################################
    def SAVEFIX_AddFinishOrderFieldToAllQuests():
        for Quest in GetAllQuests():
            if not hasattr(Quest, "FinishOrder"):
                setattr(Quest, "FinishOrder", 0)
        return

    def SAVEFIX_AddQuestOverShowInHistoryToAllQuests():
        for Quest in GetAllQuests():
            Quest.QuestOverShowInHistory = True

    def SAVEFIX_QstDeleteObsolete():
        ## delete obso
        QuestNamesToDelete = []
        for QuestClassName, QuestObj in questObjs.items():
            if QuestObj.__class__ not in allQuests:
                QuestNamesToDelete.append(QuestClassName)
        
        for QstName in QuestNamesToDelete:
            questObjs.pop(QstName)

    def SAVEFIX_QstCreateMissing():
        ## new instances
        for QuestClass in allQuests:
            if QuestClass.__name__ not in questObjs or not isinstance(questObjs[QuestClass.__name__], QuestClass):
                questObjs[QuestClass.__name__] = QuestClass()
        return

    def SAVEFIX_InitializeMissingWorldChars():
        # #1 is "kind" (for variables) #2 is message.
        # inside it should do
        # funcname = sys._getframe().f_code.co_name
        # DEBUG_ConsLog("savefix", "save update: doing a missing world chars pass (SAVEFIX_InitializeMissingWorldChars)")
        CharsRebuilt = 0
        for CharID in CharDefs:
            if CharDefs[CharID]["IsMob"] == False:
                if CharID not in getattr(store, "worldChars"):
                    # print("save update: initializing missing char %s" % CharID)
                    CreateWorldCharFromID(CharID)
                    CharsRebuilt += 1
        # if CharsRebuilt != 0:
            # if DEBUG_ConsoleOutput_Savefix_General:
                # print("save update: initialized %s missing characters (SAVEFIX_InitializeMissingWorldChars)" % CharsRebuilt)
        return

    def SAVEFIX_UpdateCharTemplateRefAndDeleteObsoleteChars():
        VerboseLog_General = False
        # when save is loaded, TemplateRefs in characters are actually copies
        # theres some other crap goin on there too, 
        # tl;dr is this will make templateRef point to actual CharDef not the shadow-copy
        ObsoleteWorldCharIDs = []
        for CharID, CharData in worldChars.items():
            if CharID in CharDefs:
                worldChars[CharID].TemplateRef = CharDefs[CharID]
            else:
                ObsoleteWorldCharIDs.append(CharID)

        # also remove obsolete chars
        for CharID in ObsoleteWorldCharIDs:
            worldChars.pop(CharID)
            if VerboseLog_General: 
                print("save update: deleted obsolete character %s from worldChars" % CharID)
        return

    def SAVEFIX_AddMissingCharPropsFromTemplate():
        ### update props
        for CharID in worldChars:
            worldChars[CharID].AddMissingPropsFromTemplate()
        return

    def SAVEFIX_UnequipAllItemsForAwayCompanions():
        for CharID in worldChars:
            if not CharInParty(CharID):
                for SlotID in EQP_SLOTS.ALL:
                    UnequipItem_CharID(CharID, SlotID)

    # recalc/unfuck attribute/skill points
    def SAVEFIX_RecalcAttrSkillPointsForPartyChars():
        for CharID in player_party:
            RecalcSkillAndAttrPoints(CharID)
        return

    # CRAZY, if this works we're 9999x saner
    def SAVEFIX_UpdateAllLogicModuleFields():
        VerboseLog_General = False
        for LMClass in getattr(store, "allQuests"):

            LMTemporaryNewInstance = LMClass.__new__(LMClass)
            LMTemporaryNewInstance.__init__()

            LMActualObject = LMClass()
            for Var, Value in vars(LMTemporaryNewInstance).items():
                if not hasattr(LMActualObject, Var):
                    setattr(LMActualObject, Var, copy.deepcopy(Value))
                    if config.developer:
                        if VerboseLog_General:
                            print("save update: added missing field  %s  to logic module  %s" % (Var, LMClass.__name__))
            for GoalID, GoalContent in LMClass.GOALS.items():
                if GoalID not in LMActualObject.GoalStates:
                    LMActualObject.GoalStates[GoalID] = GoalState.HIDDEN
            # remove obsolete goalstates
            for GoalID in list(LMActualObject.GoalStates):
                if GoalID not in LMActualObject.GOALS:
                    LMActualObject.GoalStates.pop(GoalID)

                
    def SAVEFIX_UpdateCharPregModules0176():
        VerboseLog_General = False

        PregClassList = [
            PregJackalGirl,
            PregLizardRed,
            PregLizardGreen,
            PregLizardBlue,
            PregVizura,
            PregDivine,
            PregMika,
            PregWinward,
            PregMyu,
            PregNijah,
        ]
        
        for PregClass in PregClassList:
            PregClassTempNewInstance = PregClass.__new__(PregClass)
            PregClassTempNewInstance.__init__()

            PregClassObj = PregClass()
            for Var, Value in vars(PregClassTempNewInstance).items():
                if not hasattr(PregClassObj, Var):
                    setattr(PregClassObj, Var, copy.deepcopy(Value))
                    if config.developer:
                        if VerboseLog_General:
                            print("save update: added missing field  %s  to preg module  %s" % (Var, PregClass.__name__))

            if QstIsActive(PregClass):
                if PregClass().progress == 1:
                    PregClass().NumImpregs += 1
                    PregClass().IsInPregMode = True
                    PregClass().IsPreg = True
                    if CharGetPreg(PregClass().CharID) == 4:
                        PregClass().IsPreg = False
        for PregClass in PregClassList:
            if QstIsActive(PregClass):
                PregClass().onMidnight()
        return

    # bruteforce gal unlocks fix for some old ass versions (ON STARTUP)
    if not isinstance(persistent.galleryUnlocks, dict):
        persistent.galleryUnlocks = dict()

    def SAVEFIX_ConvertItemsFromIndexesToIDs():
        IdxIDMap = {} # <- for laters, to replace equipment with ids
        for ContainerID, ContainerItems in AllContainers.items():
            for ItemIndex in list(ContainerItems):
                # this check because logic modules with shops with IDs might have already been initialized (yea fucked but WHAT YOU GOONNA DOO HUH)
                if isinstance(ItemIndex, str):
                    continue
                else:
                    ItemID = world_items[ItemIndex]["template_ID"]
                    IdxIDMap[ItemIndex] = ItemID
                    ContainerItems[ItemID] = ContainerItems[ItemIndex]
                    ContainerItems.pop(ItemIndex)

        for CharID, CharData in worldChars.items():
            for SlotID in EQP_SLOTS.ALL:
                if CharData[SlotID] in IdxIDMap:
                    CharData[SlotID] = IdxIDMap[CharData[SlotID]]
