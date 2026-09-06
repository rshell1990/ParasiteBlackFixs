# gate
image nov_gate_t = "images/world_interact/novaras_city/novh_gate.webp"
image nov_gate_h:
    "nov_gate_t"
    matrixcolor MxMapHover()

# kennels
image nov_kennels_t = "images/world_interact/novaras_city/novh_kennels.webp"
image nov_kennels_h:
    "nov_kennels_t"
    matrixcolor MxMapHover()

# fort
image nov_fort_t = "images/world_interact/novaras_city/novh_fort.webp"
image nov_fort_h:
    "nov_fort_t"
    matrixcolor MxMapHover()

init python:
    WorldLocation("novaras_dist_army", STR_LOC.NOV_DIST_ARMY, "bg_nov_district_army", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_dist_army"]
    # bridges
    LocDef.withBtn("bridge_novaras_army_to_house_south", 
        BtnChangeLoc(STR_LOC.NOV_DIST_HOUSE_S, "novaras_dist_house_south"))
    LocDef.withBtn("bridge_novaras_army_to_centre", 
        BtnChangeLoc(STR_LOC.NOV_DIST_CENTRE, "novaras_dist_centre"))
    LocDef.withBtn("bridge_novaras_army_to_market", 
        BtnChangeLoc(STR_LOC.NOV_DIST_MARKET, "novaras_dist_market"))
    # houses
    LocDef.withBtn("btn_novaras_gates_exit_city", BtnChangeLoc(STR_LOC.NOV_GATES, "novaras_gates"))
    LocDef.withBtn("btn_kennels", BtnDisabled())
    LocDef.withBtn("btn_novaras_fort_seb", BtnDisabled())#BtnChangeLoc(STR_LOC.NOV_CITY_FORT, "novaras_fort_seb_yard"))
    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_novaras_gates_exit_city": "audio/interactables/gate_drop.ogg", 
                        "btn_novaras_fort_seb":         "audio/interactables/gate_drop.ogg",
                        "btn_kennels": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_dist_army_night"] = {
        "lightpost_big":[(656, 75), (823, 75), (1036, 79), (1220, 79),
                        (284, 198), (284, 332), (289, 496), (287, 637),
                        (1544, 178), (1545, 497), (1544, 659), (735, 483)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_dist_army():
    default locTag = "novaras_dist_army"
    # bridges
    use locBtn_sprite(locTag, "bridge_novaras_army_to_centre",
        "novaras_bridge_army_north_t", "novaras_bridge_army_north_h",
        Transform(anchor = (0.5, 0.0), pos = (0.4915, 0.0)), 
        key = config.keymap["nav_up"])
    use locBtn_sprite(locTag, "bridge_novaras_army_to_house_south",
        "novaras_bridge_army_east_t", "novaras_bridge_army_east_h",
        Transform(anchor = (1.0, 0.5), pos = (1.0, 0.4475)), 
        key = config.keymap["nav_right"])
    use locBtn_sprite(locTag, "bridge_novaras_army_to_market",
        "novaras_bridge_army_west_t", "novaras_bridge_army_west_h",
        Transform(anchor = (0.0, 0.5), pos = (0.0, 0.44)), 
        key = config.keymap["nav_left"])
    # gates
    use locBtn_sprite(locTag, "btn_novaras_gates_exit_city",
        "nov_gate_t", "nov_gate_h",
        Transform(anchor = (0.5, 1.0), pos = (0.4751, 1.0)),
        key = config.keymap["nav_down"])
    # kennels
    use locBtn_sprite(locTag, "btn_kennels",
        "nov_kennels_t", "nov_kennels_h",
        Transform(anchor = (0.5, 1.0), pos = (0.511, 0.311)))
    # fort
    use locBtn_sprite(locTag, "btn_novaras_fort_seb",
        "nov_fort_t", "nov_fort_h",
        Transform(anchor = (0.5, 1.0), pos = (0.326, 0.38)))
