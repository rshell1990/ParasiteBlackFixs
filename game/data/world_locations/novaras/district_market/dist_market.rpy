image novaras_adv_guild_t = "images/world_interact/novaras_city/novh_guild.webp"
image novaras_adv_guild_h:
    "novaras_adv_guild_t"
    matrixcolor MxMapHover()

image tavern_t = "images/world_interact/novaras_city/novh_tavern.webp"
image tavern_h:
    "tavern_t"
    matrixcolor MxMapHover()

image novaras_store_t = "images/world_interact/novaras_city/novh_general_store.webp"
image novaras_store_h:
    "novaras_store_t"
    matrixcolor MxMapHover()

image novaras_clstore_t = "images/world_interact/novaras_city/novh_lingerie_store.webp"
image novaras_clstore_h:
    "novaras_clstore_t"
    matrixcolor MxMapHover()

#### market stalls
image novaras_marketstalls_t = "images/world_interact/novaras_city/novh_marketstalls.webp"
image novaras_marketstalls_h:
    "novaras_marketstalls_t"
    matrixcolor MxMapHover()

init python:
    WorldLocation("novaras_dist_market", STR_LOC.NOV_DIST_MARKET, "bg_nov_district_market", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_dist_market"]
    # bridges
    LocDef.withBtn("bridge_novaras_market_to_army",
        BtnChangeLoc(STR_LOC.NOV_DIST_ARMY, "novaras_dist_army"))
    LocDef.withBtn("bridge_novaras_market_to_pleasure",
        BtnChangeLoc(STR_LOC.NOV_DIST_PLEASURE, "novaras_dist_pleasure"))
    # houses
    LocDef.withBtn("btn_novaras_tavern",
        BtnChangeLoc(STR_LOC.NOV_TAVERN, "novaras_tavern"))
    LocDef.withBtn("btn_novaras_adv_guild",
        BtnChangeLoc(STR_LOC.NOV_ADV_GUILD, "novaras_adv_guild"))
    LocDef.withBtn("btn_novaras_store_int",
        BtnChangeLoc(STR_LOC.NOV_GENERAL_STORE, "novaras_store_int"))
    LocDef.withBtn("btn_novaras_clothes",
        BtnChangeLoc(STR_LOC.NOV_CLOTHES_STORE, "novaras_clothes_int"))
    LocDef.withBtn("btn_novaras_market_stalls",
        BtnChangeLoc(STR_LOC.NOV_MARKET_STALLS, "novaras_market_stalls"))
    # quest-bound dealer button BeneathTheShadows
    LocDef.withBtn("btn_novaras_market_dist_dealer", BtnDisabled())
    # shared event clickable
    LocDef.withBtn("btn_shared_clickable_event_market", BtnDisabled())


    # Ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_novaras_tavern": soundLib["woodenDoor"],
                        "btn_novaras_adv_guild": soundLib["woodenDoor"],
                        "btn_novaras_store_int": soundLib["woodenDoor"],
                        "btn_novaras_clothes": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_dist_market_night"] = {
        "lightpost_big":[(228, 139), (228, 314), (227, 497), (225, 658), (225, 825),
                        (743, 113), (969, 113), (1484, 148), (1484, 465), (1484, 665),
                        (1495, 895), (861, 273), (698, 382), (1065, 402), (923, 565)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_dist_market(): # initialized on "scene_objects" layer
    default locTag = "novaras_dist_market"
    # bridges
    use locBtn_sprite(locTag, "bridge_novaras_market_to_army",
        "novaras_bridge_market_east_t", "novaras_bridge_market_east_h",
        Transform(anchor = (1.0, 0.5), pos = (1.0, 0.573)), 
        key = config.keymap["nav_right"])
    use locBtn_sprite(locTag,"bridge_novaras_market_to_pleasure",
        "novaras_bridge_market_north_t", "novaras_bridge_market_north_h",
        Transform(anchor = (0.5, 0.0), pos = (0.4492, 0.0)), 
        key = config.keymap["nav_up"])

    use locBtn_sprite(locTag, "btn_novaras_tavern",
        "tavern_t", "tavern_h",
        Transform(anchor = (0, 0), pos = (1164, 62)))
    use locBtn_sprite(locTag, "btn_novaras_adv_guild",
        "novaras_adv_guild_t", "novaras_adv_guild_h",
        Transform(anchor = (0, 0), pos = (966, 669)))
    use locBtn_sprite(locTag, "btn_novaras_store_int",
        "novaras_store_t", "novaras_store_h",
        Transform(anchor = (0, 0), pos = (301, 73)))
    use locBtn_sprite(locTag, "btn_novaras_clothes",
        "novaras_clstore_t", "novaras_clstore_h",
        Transform(pos = (0.2814, 0.764)))
    use locBtn_sprite(locTag, "btn_novaras_market_stalls",
        "novaras_marketstalls_t", "novaras_marketstalls_h",
        Transform(pos = (0.458, 0.471)))


    # carina's dealer
    use locBtn_basic(locTag, "btn_novaras_market_dist_dealer",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.75, 0.85)))

    use locBtn_basic(locTag, "btn_shared_clickable_event_market",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.443, 0.753)))

