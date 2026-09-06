label start:
    # save compat-related vars
    $ SaveGameWasNeverUpdated   = False
    $ GameStartedOnVersion      = config.version

    # difficulty
    scene black
    with dissolve

    $ HideUI(True)
    $ ShowDialogueHistoryButton = False

    $ PlayMusic("audio/music/8_ValleyofDeath.ogg")

    if not config.developer:
        call screen ok_popup(
            label = _("Disclaimer"), 
            text = _("Please be aware Parasite Black is still in development. Enjoy."),
            timer = 1.5)

    call screen BattleDifficultySelection() with dissolve

    # intro vid
    $ renpy.movie_cutscene("video/prologue_intro.webm", stop_music = False)

    # init vars
    $ MARKUS.image_tag = "markusprologue"
    $ MC.image_tag = "mcprologue"

    $ CharAltFormLock("mc")
    $ CharAltFormLock("kiara")
    $ CharAltFormLock("markus")

    $ CharSetBattleSkinID("mc", "mc_p")
    $ CharSetBattleSkinID("markus", "markus_p")

    # char creation
    scene black with dissolve
    $ Pause(0.1)

    $ ShowTutorialPopup("character_creation")

    $ Pause(0.1)
    call screen StartCharacterMenu() with Dissolve(0.5)
    
    $ HideUI(False)

    # jump to actual narrative start
    jump qst_Terminus_intro

label dev_quickstart:
    $ DEBUG_SupressNotifs(True)
    $ SaveGameWasNeverUpdated = False
    $ QstStart(QstTerminus, Silent = True)
    $ QstComplete(QstTerminus, Silent = True)

    $ QstStart(QstForgedInFire, Silent = True)
    $ QstComplete(QstForgedInFire, Silent = True)

    $ QstStart(QstTheDarkPass, Silent = True)
    $ QstComplete(QstTheDarkPass, Silent = True)

    $ QstStart(QstFromAnotherWorld, Silent = True)
    $ QstComplete(QstFromAnotherWorld, Silent = True)

    $ QstStart(EventNovarasMarkusTavernPostFaw, Silent = True)
    $ QstComplete(EventNovarasMarkusTavernPostFaw, Silent = True)

    $ QstStart(EventAdventureGuildShowUp, Silent = True)
    $ QstComplete(EventAdventureGuildShowUp, Silent = True)

    $ QstStart(QstReginaPackage, Silent = True)

    $ QstStart(InfectionModule)

    $ gui_parts["characters"] = True

    # ves quest rewards
    $ PlayerAddItem("potion_heal_minor",2)
    $ PlayerAddItem("potion_heal_regular",1)
    $ PlayerAddItem("gold",125)
    # rusty shit joakim gave
    $ PlayerAddItem("leather_armor")
    $ PlayerAddItem("scout_sword_rusty")
    $ PlayerPartyCharEquipItem("mc", "leather_armor")
    $ PlayerPartyCharEquipItem("mc", "scout_sword_rusty")

    #############################################################
    # these are all to fast-forward us to TheComingStorm

    # which quests do we need again?...
    $ QstComplete(QstReginaPackage, Silent = True)

    $ QstStart(QstProperReunion, Silent = True)
    $ QstComplete(QstProperReunion, Silent = True)
    $ QstComplete(PrimerQstProperReunion, Silent = True)

    $ QstStart(QstDarkKnight, Silent = True)
    $ QstComplete(QstDarkKnight, Silent = True)
    $ QstComplete(PrimerDarkKnight, Silent = True)

    $ QstStart(QstTheBloodhound, Silent = True)
    $ QstComplete(QstTheBloodhound, Silent = True)

    $ QstComplete(PrimerTheSlavemaster, Silent = True)
    $ QstStart(QstTheSlavemaster, Silent = True)
    $ QstComplete(QstTheSlavemaster, Silent = True)

    $ NoteLock("romanceNyxStart")

    $ QstComplete(EventMcNewArmor, Silent = True)

    $ QstSetProgress(DialogueDros, 1)
    $ QstStart(QstHighFasion,   Silent = True)
    $ QstComplete(QstHighFasion,  Silent = True)

    $ QstStart(QstTwoEmperors, Silent = True)
    $ QstComplete(QstTwoEmperors, Silent = True)

    $ QstStart(EventNovarasMarkusTavernTwoEmps, Silent = True)
    $ QstComplete(EventNovarasMarkusTavernTwoEmps, Silent = True)

    ####### girl troubles section
    $ QstComplete(PrimerGirlTroubles, Silent = True)
    $ QstStart(QstGirlTroubles, Silent = True)
    $ QstComplete(QstLittleLies, Silent = True)
    $ QstComplete(QstTheMagesPath, Silent = True)

    $ QstStart(QstTheLoversPath, Silent = True)
    $ QstComplete(QstTheLoversPath, Silent = True)

    $ QstStart(QstLetsCelebrate, Silent = True)
    $ QstComplete(QstLetsCelebrate, Silent = True)

    $ QstComplete(QstGirlTroubles, Silent = True)

    $ NoteLock("visit_mika_post_celebration")
    ##########

    # this event is skipped bc it grabs focus
    $ QstComplete(EventKrishanaDay, Silent = True)

    $ QstStart(QstBeneathTheShadows, Silent = True)
    $ QstComplete(QstBeneathTheShadows, Silent = True)

    $ QstStart(QstDamzelInDiztrezz,     Silent = True)
    $ QstComplete(QstDamzelInDiztrezz,    Silent = True)
    $ QstComplete(PrimerDamzelInDiztrezz, Silent = True)
    $ QstComplete(EventNijahRescue,       Silent = True)

    $ CharSetVar("kiara", "romanced", True)

    $ WorldMapLocAdd("lake_peacing")
    $ WorldMapLocAdd("lake_balun")
    $ WorldMapLocAdd("hamun_gates")

    $ PlayerAddItem("gold", 3000)

    $ TimeAdvTo(TIME_DUSK)

    $ QstSetProgress(RomanceNyx, 4)
    $ QstComplete(PrimerTheComingStorm)

    $ QstStart(QstTheComingStorm)
    $ QstComplete(QstTheComingStorm)

    $ QstComplete(QstJudgementDay)
    $ QstJudgementDay().ImprisonedCharacters.add("myu")
    $ QstJudgementDay().ImprisonedCharacters.add("elena")

    $ PartyAddChar("kiara")
    $ PartyAddChar("ves")

    $ PlayerAddItem("orc_tribal_wear", Silent = True)
    $ PlayerAddItem("orc_tribal_axe",  Silent = True)
    $ PlayerAddItem("ves_family_axe",  Silent = True)
    $ PlayerAddItem("orc_tribal_necklace", Silent = True)
    $ PlayerPartyCharEquipItem("ves", "orc_tribal_wear")
    $ PlayerPartyCharEquipItem("ves", "orc_tribal_axe")
    $ PlayerPartyCharEquipItem("ves", "ves_family_axe")
    $ PlayerPartyCharEquipItem("ves", "orc_tribal_necklace")

    $ PlayerAddItem("corrupted_blade", Silent = True)
    $ PlayerAddItem("duskshroud_raiment", Silent = True)
    $ PlayerAddItem("shadow_ring", Silent = True)
    $ PlayerPartyCharEquipItem("kiara", "corrupted_blade")
    $ PlayerPartyCharEquipItem("kiara", "duskshroud_raiment")
    $ PlayerPartyCharEquipItem("kiara", "shadow_ring")
    
    $ QstStart(DialogueVes, Silent = True)

    $ QstStart(QstTheBeastOfNovaras,  Silent = True)
    $ QstComplete(QstTheBeastOfNovaras, Silent = True)

    $ QstStart(PrimerTheTarbecks, Silent = True)
    $ QstComplete(PrimerTheTarbecks, Silent = True)
    $ QstStart(QstTheTarbecks, Silent = True)
    $ QstComplete(QstTheTarbecks, Silent = True)

    $ QstStart(PrimerDreamhouse, Silent = True)
    $ QstComplete(PrimerDreamhouse, Silent = True)
    $ QstStart(QstDreamhouse, Silent = True)
    $ QstComplete(QstDreamhouse, Silent = True)

    $ LocSet("hamun_dist_docks")
    $ DEBUG_SupressNotifs(False)
    $ LocEnter()

label dev_quickstart_hamun:
    $ DEBUG_SupressNotifs(True)
    $ SaveGameWasNeverUpdated = False
    $ QstStart(QstTerminus, Silent = True)
    $ QstComplete(QstTerminus, Silent = True)

    $ QstStart(QstForgedInFire, Silent = True)
    $ QstComplete(QstForgedInFire, Silent = True)

    $ QstStart(QstTheDarkPass, Silent = True)
    $ QstComplete(QstTheDarkPass, Silent = True)

    $ QstStart(QstFromAnotherWorld, Silent = True)
    $ QstComplete(QstFromAnotherWorld, Silent = True)

    $ QstStart(EventNovarasMarkusTavernPostFaw, Silent = True)
    $ QstComplete(EventNovarasMarkusTavernPostFaw, Silent = True)

    $ QstStart(EventAdventureGuildShowUp, Silent = True)
    $ QstComplete(EventAdventureGuildShowUp, Silent = True)

    $ QstStart(QstReginaPackage, Silent = True)

    $ QstStart(InfectionModule)

    $ gui_parts["characters"] = True

    # ves quest rewards
    $ PlayerAddItem("potion_heal_minor",2)
    $ PlayerAddItem("potion_heal_regular",1)
    $ PlayerAddItem("gold",125)
    # rusty shit joakim gave
    $ PlayerAddItem("leather_armor")
    $ PlayerAddItem("scout_sword_rusty")
    $ PlayerPartyCharEquipItem("mc", "leather_armor")
    $ PlayerPartyCharEquipItem("mc", "scout_sword_rusty")

    #############################################################
    # these are all to fast-forward us to TheComingStorm

    # which quests do we need again?...
    $ QstComplete(QstReginaPackage, Silent = True)

    $ QstStart(QstProperReunion, Silent = True)
    $ QstComplete(QstProperReunion, Silent = True)
    $ QstComplete(PrimerQstProperReunion, Silent = True)

    $ QstStart(QstDarkKnight, Silent = True)
    $ QstComplete(QstDarkKnight, Silent = True)
    $ QstComplete(PrimerDarkKnight, Silent = True)

    $ QstStart(QstTheBloodhound, Silent = True)
    $ QstComplete(QstTheBloodhound, Silent = True)

    $ QstComplete(PrimerTheSlavemaster, Silent = True)
    $ QstStart(QstTheSlavemaster, Silent = True)
    $ QstComplete(QstTheSlavemaster, Silent = True)

    $ NoteLock("romanceNyxStart")

    $ QstComplete(EventMcNewArmor, Silent = True)

    $ QstSetProgress(DialogueDros, 1)
    $ QstStart(QstHighFasion,   Silent = True)
    $ QstComplete(QstHighFasion,  Silent = True)

    $ QstStart(QstTwoEmperors, Silent = True)
    $ QstComplete(QstTwoEmperors, Silent = True)

    $ QstStart(EventNovarasMarkusTavernTwoEmps, Silent = True)
    $ QstComplete(EventNovarasMarkusTavernTwoEmps, Silent = True)

    ####### girl troubles section
    $ QstComplete(PrimerGirlTroubles, Silent = True)
    $ QstStart(QstGirlTroubles, Silent = True)
    $ QstComplete(QstLittleLies, Silent = True)
    $ QstComplete(QstTheMagesPath, Silent = True)

    $ QstStart(QstTheLoversPath, Silent = True)
    $ QstComplete(QstTheLoversPath, Silent = True)

    $ QstStart(QstLetsCelebrate, Silent = True)
    $ QstComplete(QstLetsCelebrate, Silent = True)

    $ QstComplete(QstGirlTroubles, Silent = True)

    $ NoteLock("visit_mika_post_celebration")
    ##########

    # this event is skipped bc it grabs focus
    $ QstComplete(EventKrishanaDay, Silent = True)

    $ QstStart(QstBeneathTheShadows, Silent = True)
    $ QstComplete(QstBeneathTheShadows, Silent = True)

    $ QstStart(QstDamzelInDiztrezz,     Silent = True)
    $ QstComplete(QstDamzelInDiztrezz,    Silent = True)
    $ QstComplete(PrimerDamzelInDiztrezz, Silent = True)
    $ QstComplete(EventNijahRescue,       Silent = True)

    $ CharSetVar("kiara", "romanced", True)

    $ WorldMapLocAdd("lake_peacing")
    $ WorldMapLocAdd("lake_balun")
    $ WorldMapLocAdd("hamun_gates")

    $ PlayerAddItem("gold", 3000)

    $ TimeAdvTo(TIME_DUSK)

    $ QstSetProgress(RomanceNyx, 4)
    $ QstComplete(PrimerTheComingStorm)

    $ QstStart(QstTheComingStorm)
    $ QstComplete(QstTheComingStorm)

    $ QstComplete(QstJudgementDay)
    $ QstJudgementDay().ImprisonedCharacters.add("myu")
    $ QstJudgementDay().ImprisonedCharacters.add("elena")

    $ PartyAddChar("kiara")
    $ PartyAddChar("ves")

    $ PlayerAddItem("orc_tribal_wear", Silent = True)
    $ PlayerAddItem("orc_tribal_axe",  Silent = True)
    $ PlayerAddItem("ves_family_axe",  Silent = True)
    $ PlayerAddItem("orc_tribal_necklace", Silent = True)
    $ PlayerPartyCharEquipItem("ves", "orc_tribal_wear")
    $ PlayerPartyCharEquipItem("ves", "orc_tribal_axe")
    $ PlayerPartyCharEquipItem("ves", "ves_family_axe")
    $ PlayerPartyCharEquipItem("ves", "orc_tribal_necklace")

    $ PlayerAddItem("corrupted_blade", Silent = True)
    $ PlayerAddItem("duskshroud_raiment", Silent = True)
    $ PlayerAddItem("shadow_ring", Silent = True)
    $ PlayerPartyCharEquipItem("kiara", "corrupted_blade")
    $ PlayerPartyCharEquipItem("kiara", "duskshroud_raiment")
    $ PlayerPartyCharEquipItem("kiara", "shadow_ring")

    $ LocSet("hamun_gates")
    $ DEBUG_SupressNotifs(False)
    $ LocEnter()



################## 
label dev_quickstart_postprologue:
    $ DEBUG_SupressNotifs(True)
    $ SaveGameWasNeverUpdated = False
    $ LocSet("novaras_dist_centre")
    $ QstStart(QstTerminus, Silent = True)
    $ QstComplete(QstTerminus, Silent = True)

    $ QstStart(QstForgedInFire, Silent = True)
    $ QstComplete(QstForgedInFire, Silent = True)

    $ QstStart(QstTheDarkPass, Silent = True)
    $ QstComplete(QstTheDarkPass, Silent = True)

    $ QstStart(QstFromAnotherWorld, Silent = True)
    $ QstComplete(QstFromAnotherWorld, Silent = True)


    $ QstStart(InfectionModule)
    $ gui_parts["characters"] = True

    # ves quest rewards
    $ PlayerAddItem("potion_heal_minor", 2)
    $ PlayerAddItem("potion_heal_regular", 1)
    $ PlayerAddItem("gold", 125)
    # rusty shit joakim gave
    $ PlayerAddItem("leather_armor")
    $ PlayerAddItem("scout_sword_rusty")

    $ PlayerPartyCharEquipItem("mc", "leather_armor")
    $ PlayerPartyCharEquipItem("mc", "scout_sword_rusty")

    $ PlayerAddItem("gold", 3000)
    $ TimeAdvTo(TIME_MIDNIGHT)

    $ HouseLockBlackDiamond().canBeAccessed = True
    $ QstStart(BlackDiamondArena)
    $ QstStart(DoorBlackDiamondArena)

    $ DEBUG_SupressNotifs(False)

    $ LocEnter()