# for debug purposes to set up battle quickly
default DEBUG_InstaBattle = False
# label main_menu:
#     if DEBUG_InstaBattle:
#         call screen InstaBattleStater()
#     else:
#         call screen main_menu()

screen InstaBattleStater():
    timer 0.000001 action Jump("insta_battle")

label insta_battle:
    $ PlayMusicRandom("mus_battle_generic")
    
    python:
        if store.PlayerItemQty("potion_heal_minor") < 10:
            if hasattr(store, "DEBUG_PlayerAddAllItems"):
                store.DEBUG_PlayerAddAllItems(10)
        
        if hasattr(store, "QstStart") and hasattr(store, "InfectionModule"):
            store.QstStart(store.InfectionModule)
            inf_mod = store.InfectionModule()
            inf_mod.isActive = True
            inf_mod.CurrentValue = 40

        tmpvar = store.BattleSetup_GetAllCharsWithSkin() if hasattr(store, "BattleSetup_GetAllCharsWithSkin") else {}
        valid_keys = list(tmpvar.keys())

    $ DEBUG_INSTA_BATTLE_TYPE = "random_4"

    if DEBUG_INSTA_BATTLE_TYPE == "party":
        $ DEBUG_SetAllStatsTo(19)
        $ DEBUG_AddOneToAllClassSkills()
        $ TransformMarkus(True)
        $ StartBattle(BattleData(BackgroundImage = renpy.random.choice(battle_setup_battle_maps),
                            CharIDList_Left = ["mc", "markus", "elena", "ves"],
                            CharIDList_Right = ["e_slimelark", "e_slimelark", "e_slimelark", "e_slimelark"]))
        $ TransformMarkus(False)

    elif DEBUG_INSTA_BATTLE_TYPE == "soundtest":
        $ DEBUG_SetAllStatsTo(19)
        $ DEBUG_AddOneToAllClassSkills()
        $ TransformMarkus(True)
        python:
            count = store.RngInt(2, 4) if hasattr(store, "RngInt") else renpy.random.randint(2, 4)
            right_list = [tmpvar[renpy.random.choice(valid_keys)]["char_id"] for _ in range(count)] if valid_keys else []
        $ StartBattle(BattleData(BackgroundImage = renpy.random.choice(battle_setup_battle_maps),
                            CharIDList_Left = ["mc", "markus", "e_bear", "myu"],
                            CharIDList_Right = right_list))
        $ TransformMarkus(False)

    elif DEBUG_INSTA_BATTLE_TYPE == "debug_ghouls":
        $ StartBattle(BattleData(BackgroundImage = renpy.random.choice(battle_setup_battle_maps),
                            CharIDList_Left = ["e_debug_neutral", "e_debug_neutral", "e_debug_neutral", "e_debug_neutral"],
                            CharIDList_Right = ["e_debug_neutral", "e_debug_neutral", "e_debug_neutral", "e_debug_neutral"]))

    elif DEBUG_INSTA_BATTLE_TYPE == "random_4":
        if hasattr(store, "DEBUG_AddOneToAllClassSkills"):
            $ DEBUG_AddOneToAllClassSkills()
            
        if renpy.random.randint(1, 2) == 1 and hasattr(store, "TransformMC"):
            $ TransformMC(True)
        if renpy.random.randint(1, 2) == 1 and hasattr(store, "TransformMarkus"):
            $ TransformMarkus(True)
        if renpy.random.randint(1, 2) == 1 and hasattr(store, "TransformElena"):
            $ TransformElena(True)

        python:
            left_list = [tmpvar[renpy.random.choice(valid_keys)]["char_id"] for _ in range(4)] if valid_keys else []
            right_list = [tmpvar[renpy.random.choice(valid_keys)]["char_id"] for _ in range(4)] if valid_keys else []

        $ StartBattle(BattleData(
                        BackgroundImage = renpy.random.choice(battle_setup_battle_maps),
                        CharIDList_Left = left_list,
                        CharIDList_Right = right_list,
                        TurnLimit = 50,
                    )
                )

        if hasattr(store, "TransformMC"):
            $ TransformMC(False)
        if hasattr(store, "TransformMarkus"):
            $ TransformMarkus(False)
        if hasattr(store, "TransformElena"):
            $ TransformElena(False)

    python:
        if hasattr(store, "InfectionModule"):
            inf_mod = store.InfectionModule()
            inf_mod.isActive = False
        tmpvar = {}

    # if LastBattleOutcome == "defeat":
    #     "(defeat)"
    # elif LastBattleOutcome == "victory":
    #     "(victory)"
    # elif LastBattleOutcome == "retreat":
    #     "(retreat)"

    jump insta_battle