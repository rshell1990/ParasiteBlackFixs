image hamun_dist_docks = "images/world_bgs/hamun_city/hamun_dist_docks.webp"

####################################################################################
# clickables:
# north exit
image hamun_dist_docks_exit_north_t = "images/world_interact/hamun_city/ham_docks_exit_north.webp"
image hamun_dist_docks_exit_north_h:
    "hamun_dist_docks_exit_north_t"
    matrixcolor MxMapHover()
# south exit
image hamun_dist_docks_exit_south_t = "images/world_interact/hamun_city/ham_docks_exit_south.webp"
image hamun_dist_docks_exit_south_h:
    "hamun_dist_docks_exit_south_t"
    matrixcolor MxMapHover()

# market
image hamun_market_t = "images/world_interact/hamun_city/ham_market.webp"
image hamun_market_h:
    "hamun_market_t"
    matrixcolor MxMapHover()

# docks store
image hamun_docks_store_t = "images/world_interact/hamun_city/ham_docks_store.webp"
image hamun_docks_store_h:
    "hamun_docks_store_t"
    matrixcolor MxMapHover()
# brothel
image hamun_brothel_t = "images/world_interact/hamun_city/ham_brothel.webp"
image hamun_brothel_h:
    "hamun_brothel_t"
    matrixcolor MxMapHover()
# hookah bar
image hamun_hookah_bar_t = "images/world_interact/hamun_city/ham_hookah_bar.webp"
image hamun_hookah_bar_h:
    "hamun_hookah_bar_t"
    matrixcolor MxMapHover()
# witch house
image hamun_witch_house_t = "images/world_interact/hamun_city/ham_witch_house.webp"
image hamun_witch_house_h:
    "hamun_witch_house_t"
    matrixcolor MxMapHover()
# smith
image hamun_smithy_t = "images/world_interact/hamun_city/ham_smithy.webp"
image hamun_smithy_h:
    "hamun_smithy_t"
    matrixcolor MxMapHover()
# miningco
image hamun_miningco_t = "images/world_interact/hamun_city/ham_miningco.webp"
image hamun_miningco_h:
    "hamun_miningco_t"
    matrixcolor MxMapHover()
# giselra store
image hamun_giselra_store_t = "images/world_interact/hamun_city/hamun_giselra_store.webp"
image hamun_giselra_store_h:
    "hamun_giselra_store_t"
    matrixcolor MxMapHover()
# khazah hideout
image hamun_khazah_hideout_t = "images/world_interact/hamun_city/ham_khazah_hideout.webp"
image hamun_khazah_hideout_h:
    "hamun_khazah_hideout_t"
    matrixcolor MxMapHover()

# docks clickable
image hamun_docks_port_t = "images/world_interact/hamun_city/ham_docks_port.webp"
image hamun_docks_port_h:
    "hamun_docks_port_t"
    matrixcolor MxMapHover()

####################################################################################
init python:
    WorldLocation("hamun_dist_docks", STR_LOC.HAMUN_DIST_DOCKS, "hamun_dist_docks", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_dist_docks"]
    ###### clickables ######
    LocDef.withBtn("hamun_dist_docks_to_dist_merch_lord", BtnChangeLoc(STR_LOC.HAMUN_DIST_MERCH_LORD, "hamun_dist_merch_lord"))
    LocDef.withBtn("hamun_docks_to_market",        BtnChangeLoc(STR_LOC.HAMUN_MARKET,        "hamun_market")) 
    LocDef.withBtn("hamun_docks_to_witch_house",   BtnChangeLoc(STR_LOC.HAMUN_WITCH_HOUSE,   "hamun_witch_house"))
    LocDef.withBtn("hamun_docks_to_store",         BtnDisabled())
    LocDef.withBtn("hamun_docks_to_smithy",        BtnDisabled())
    LocDef.withBtn("hamun_docks_to_miningco",      BtnChangeLoc(STR_LOC.HAMUN_MININGCO,      "hamun_miningco"))
    LocDef.withBtn("hamun_docks_to_brothel",       BtnDisabled())
    LocDef.withBtn("hamun_docks_to_hookah_bar",    BtnChangeLoc(STR_LOC.HAMUN_HOOKAH_BAR,    "hamun_hookah_bar"))
    LocDef.withBtn("hamun_docks_to_gates",         BtnChangeLoc(STR_LOC.HAMUN_CITY_GATES,    "hamun_gates"))
    LocDef.withBtn("hamun_docks_to_khazah_hideout", BtnDisabled())

    LocDef.withBtn("hamun_docks_to_port",          BtnChangeLoc(STR_LOC.HAMUN_DOCKS_PORT,    "hamun_port"))
    LocDef.withBtn("hamun_docks_to_giselra_store", BtnChangeLoc(STR_LOC.HAMUN_GISELRA_STORE, "hamun_giselra_store"))
    #if config.developer:
    #    LocDef.withBtn("debug_jump_to_tavern",     BtnJumpLabel("DEBUG: Jump to Tavern", "debug_fortress_in_teleport"))

    ########################
    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    # action sfx
    LocDef.withActionSFXs({"hamun_docks_to_witch_house": soundLib["tentFlap"], 
                        "hamun_docks_to_store":       soundLib["tentFlap"],
                        "hamun_docks_to_giselra_store":       soundLib["tentFlap"],
                        "hamun_docks_to_smithy":      soundLib["tentFlap"],
                        "hamun_docks_to_brothel":     soundLib["tentFlap"],
                        "hamun_docks_to_hookah_bar":  soundLib["tentFlap"],
                        "hamun_docks_to_gates":       "audio/interactables/gate_drop.ogg",
                        })

    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)
    # vfx "small huge big" are default lightposts
    vfxLibLights["hamun_dist_docks_night"] = {
        "lightpost_huge":[(1690, 817)],
        "lightpost_big":[
            (1529, 1061), (1825, 619), (1641, 580),
            (1416, 262), (1364, 157), (1337, 58), (1038, 424),
            (866, 521), (707, 416), (742, 971), (603, 969),
            (672, -26), (808, -26)]}

screen loc_hamun_dist_docks():
    default locTag = "hamun_dist_docks"

    # north exit
    use locBtn_sprite(locTag, "hamun_dist_docks_to_dist_merch_lord", 
        "hamun_dist_docks_exit_north_t",
        "hamun_dist_docks_exit_north_h",
        Transform(anchor = (0, 0), pos = (558, 0)), 
        key = config.keymap["nav_up"],
        )

    # market
    use locBtn_sprite(locTag, "hamun_docks_to_market", 
        "hamun_market_t",
        "hamun_market_h",
        Transform(anchor = (1.0, 1.0), pos = (1.0, 1.0)), 
        )

    # witch house
    use locBtn_sprite(locTag, "hamun_docks_to_witch_house",
        "hamun_witch_house_t",
        "hamun_witch_house_h",
        Transform(anchor = (0.0, 0.0), pos = (1100, 139)),
        )

    # docks store
    use locBtn_sprite(locTag, "hamun_docks_to_store",
        "hamun_docks_store_t",
        "hamun_docks_store_h",
        Transform(anchor = (0.0, 0.0), pos = (475, 66)),
        )

    # brothel
    use locBtn_sprite(locTag, "hamun_docks_to_brothel",
        "hamun_brothel_t",
        "hamun_brothel_h",
        Transform(anchor = (0.0, 0.0), pos = (746, 548)),
        )

    # hookah bar
    use locBtn_sprite(locTag, "hamun_docks_to_hookah_bar",
        "hamun_hookah_bar_t",
        "hamun_hookah_bar_h",
        Transform(anchor = (0.0, 0.0), pos = (372, 481)),
        )

    # smithy
    use locBtn_sprite(locTag, "hamun_docks_to_smithy",
        "hamun_smithy_t",
        "hamun_smithy_h",
        Transform(anchor = (0.0, 0.0), pos = (105, 149)),
        )

    # miningco
    use locBtn_sprite(locTag, "hamun_docks_to_miningco",
        "hamun_miningco_t",
        "hamun_miningco_h",
        Transform(anchor = (0.0, 0.0), pos = (46, 433)),
        )
    # giselra store
    use locBtn_sprite(locTag, "hamun_docks_to_giselra_store",
        "hamun_giselra_store_t",
        "hamun_giselra_store_h",
        Transform(anchor = (0, 0), pos = (0, 677)),
        )

    # khazah hideout
    use locBtn_sprite(locTag, "hamun_docks_to_khazah_hideout",
        "hamun_khazah_hideout_t",
        "hamun_khazah_hideout_h",
        Transform(anchor = (0.0, 0.0), pos = (827, 55)),
        )
        
    # south exit
    use locBtn_sprite(locTag, "hamun_docks_to_gates",
        "hamun_dist_docks_exit_south_t",
        "hamun_dist_docks_exit_south_h",
        Transform(anchor = (0.0, 0.0), pos = (488, 865)),
        key = config.keymap["nav_down"],
        )
    
    # docks
    use locBtn_sprite(locTag, "hamun_docks_to_port",
        "hamun_docks_port_t",
        "hamun_docks_port_h",
        Transform(anchor = (0.0, 0.0), pos = (1346, 295)),
        )

    #if config.developer:          
        # fortress_inn_frog
    #    use locBtn_basic(
    #        locTag,
    #        "debug_jump_to_tavern",
    #        "images/gui/buttons_loc/travel.webp",
    #        Transform(pos = (0.6, 0.8))
    #    )
