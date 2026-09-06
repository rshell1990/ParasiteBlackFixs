# for debug purposes to set up battle quickly
default DEBUG_InstaBattle = False
# label main_menu:
#     if DEBUG_InstaBattle:
#         call screen InstaBattleStater()
#     else:
#         call screen main_menu()

screen InstaBattleStater():
    timer 0.000001 action Start("insta_battle")

label insta_battle:
    $ PlayMusicRandom("mus_battle_generic")
    if PlayerItemQty("potion_heal_minor") < 10:
        $ DEBUG_PlayerAddAllItems(10)
    $ QstStart(InfectionModule)
    $ InfectionModule().isActive = True
    $ InfectionModule().CurrentValue = 40

    $ tmpvar = BattleSetup_GetAllCharsWithSkin()

    $ DEBUG_INSTA_BATTLE_TYPE = "random_4"

    if DEBUG_INSTA_BATTLE_TYPE == "party":
        $ DEBUG_SetAllStatsTo(19)
        $ DEBUG_AddOneToAllClassSkills()
        $ TransformMarkus(True)
        $ StartBattle(BattleData(BackgroundImage = renpy.random.choice(battle_setup_battle_maps),
                            CharIDList_Left = ["mc", "markus", "elena", "ves"],
                            CharIDList_Right = ["e_slimelark", "e_slimelark", "e_slimelark", "e_slimelark"]))
        $ TransformMarkus(False)
    if DEBUG_INSTA_BATTLE_TYPE == "soundtest":
        $ DEBUG_SetAllStatsTo(19)
        $ DEBUG_AddOneToAllClassSkills()
        $ TransformMarkus(True)
        $ StartBattle(BattleData(BackgroundImage = renpy.random.choice(battle_setup_battle_maps),
                            CharIDList_Left = ["mc", "markus", "e_bear", "myu"],
                            CharIDList_Right = [tmpvar[renpy.random.choice(list(tmpvar.keys()))]["char_id"] for x in range(RngInt(2, 4))]))
        $ TransformMarkus(False)

    if DEBUG_INSTA_BATTLE_TYPE == "debug_ghouls":
        $ StartBattle(BattleData(BackgroundImage = renpy.random.choice(battle_setup_battle_maps),
                            CharIDList_Left = ["e_debug_neutral", "e_debug_neutral", "e_debug_neutral", "e_debug_neutral"],
                            CharIDList_Right = ["e_debug_neutral", "e_debug_neutral", "e_debug_neutral", "e_debug_neutral"]))

    if DEBUG_INSTA_BATTLE_TYPE == "random_4":
        $ DEBUG_AddOneToAllClassSkills()
        if renpy.random.randint(1, 2) == 1:
            $ TransformMC(True)
        if renpy.random.randint(1, 2) == 1:
            $ TransformMarkus(True)
        if renpy.random.randint(1, 2) == 1:
            $ TransformElena(True)

        $ StartBattle(BattleData(
                        BackgroundImage = renpy.random.choice(battle_setup_battle_maps),
                        CharIDList_Left = [tmpvar[renpy.random.choice(list(tmpvar.keys()))]["char_id"] for x in range(RngInt(4, 4))],
                        CharIDList_Right = [tmpvar[renpy.random.choice(list(tmpvar.keys()))]["char_id"] for x in range(RngInt(4, 4))],
                        TurnLimit = 50,
                    )
                )
        $ TransformMC(False)
        $ TransformMarkus(False)
        $ TransformElena(False)

    $ InfectionModule().isActive = False
    $ tmpvar = {}

    # if LastBattleOutcome == "defeat":
    #     "(defeat)"
    # elif LastBattleOutcome == "victory":
    #     "(victory)"
    # elif LastBattleOutcome == "retreat":
    #     "(retreat)"

    jump insta_battle
