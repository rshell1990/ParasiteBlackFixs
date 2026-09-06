label travel_node_logic_mine:
    call travel_event_mine from _call_travel_event_mine
    return

label travel_node_logic_enemy:
    if renpy.random.randint(0, 1) == 0:
        call travel_event_battle_demorai from _call_travel_event_battle_demorai 
    else:
        call travel_event_raider from _call_travel_event_raider 
    return

label travel_node_logic_safe:
    call travel_event_set_camp from _call_travel_event_set_camp
    return

# "normal" is actually "random"
label travel_node_logic_normal:
    $ tmpvar = []

    # "default" cases are enemy or lizards with 50/50 chance
    $ tmpvar.append(1)
    $ tmpvar.append(3)
    # vizura caravan (0)
    if QstIsActive(VizuraCaravan):
        $ tmpvar.append(0)
    # lizards (3)
    if GetPlayerLevel() > 6:
        $ tmpvar.append(3)
        $ tmpvar.append(3)
    # wagon wreck (2)
    if Travel_GetCurrentBiome() == "forest":
        $ tmpvar.append(2)
    # ship crash (4)
    if TravelState.RouteID == "novaras_balun":
        if QstIsActive(EventCrashedShipEncounter):
            if RngInt(1, 60) == 1:
                $ tmpvar.append(4)
    # jackal girl (5)
    if Travel_GetCurrentBiome() == "desert":
        if QstIsActive(EventJackalGirlEncounter):
            if RngInt(1, 100) <= 5: # 5%
                $ tmpvar.append(5)
    # fortress inn (6)
    if Travel_GetCurrentBiome() == "forest":
        if QstIsActive(EventFortressInn):
            if RngInt(1, 3) == 1:
                $ tmpvar.append(6)

    $ tmpvar = renpy.random.choice(tmpvar)

    # vizura
    if tmpvar == 0:
        call travel_event_vizura_encounter from _call_travel_event_vizura_encounter
    #  enemy node
    elif tmpvar == 1:
        call travel_node_logic_enemy from _call_travel_node_logic_enemy
    # wreck
    elif tmpvar == 2:
        call travel_event_wagon_wreck from _call_travel_event_wagon_wreck
    # lizards
    elif tmpvar == 3:
        if Travel_GetCurrentBiome() == "desert":
            call travel_event_lizard_red from _call_travel_event_lizard_red
        elif Travel_GetCurrentBiome() == "forest":
            # second roll for either green or blue lizard
            $ tmpvar = renpy.random.randint(0, 1)
            if tmpvar == 0:
                call travel_event_lizard_green from _call_travel_event_lizard_green
            if tmpvar == 1: 
                call travel_event_lizard_blue from _call_travel_event_lizard_blue
    # ship crash
    elif tmpvar == 4:
        call travel_event_crashed_ship from _call_travel_event_crashed_ship
    # jackal girl
    elif tmpvar == 5:
        call travel_event_jackal_girl from _call_travel_event_jackal_girl
    # travel inn
    elif tmpvar == 6:
        call travel_event_fortress_inn from _call_travel_event_fortress_inn
    return

# all 3 tavern nodes map to these 3 here
label travel_node_logic_tavern_frog:
    call travel_event_fortress_inn_frog from _call_travel_event_fortress_inn_frog
    return
label travel_node_logic_tavern_cat:
    call travel_event_fortress_inn_cat from _call_travel_event_fortress_inn_cat
    return
label travel_node_logic_tavern_wench:
    call travel_event_fortress_inn_wench from _call_travel_event_fortress_inn_wench
    return

label travel_node_logic_nature:
    $ tmpvar = []
    if Travel_GetCurrentBiome() == "forest":
        # add deer
        $ tmpvar.append(1)
        # wolves
        if GetPlayerLevel() >= 4: 
            $ tmpvar.append(2)
            $ tmpvar.append(2)
        # generic bear
        if GetPlayerLevel() >= 5: 
            $ tmpvar.append(0)
            $ tmpvar.append(0)
        # white bear
        if GetPlayerLevel() >= 6 or QstIsActive(QstLittleLies):
            $ tmpvar.append(3)
        if QstIsActive(QstLittleLies):
            $ tmpvar.append(3)

    # jackal girl
    if Travel_GetCurrentBiome() == "desert":
        if QstIsActive(EventJackalGirlEncounter):
            if RngInt(1, 100) <= 40:
                $ tmpvar.append(4)

    # in case of no events, return
    if len(tmpvar) == 0:
        "There's nothing here..."
        "(WIP)"
        call travel_node_logic_safe from _call_travel_node_logic_safe
        return

    # in case any events exist, choose
    $ tmpvar = renpy.random.choice(tmpvar)

    if tmpvar == 3:
        call travel_event_white_bear from _call_travel_event_white_bear
    elif tmpvar == 0:
        call travel_event_bear from _call_travel_event_bear
    elif tmpvar == 1:
        call travel_event_deer from _call_travel_event_deer
    elif tmpvar == 2:
        call travel_event_wolves from _call_travel_event_wolves
    elif tmpvar == 4:
        call travel_event_jackal_girl from _call_travel_event_jackal_girl_1
    $ tmpvar = {}
    return
