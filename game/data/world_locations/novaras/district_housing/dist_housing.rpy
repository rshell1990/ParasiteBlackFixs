##### mc house ######
image mc_house_t = "images/world_interact/novaras_city/novh_house_mc.webp"
image mc_house_h:
    "mc_house_t"
    matrixcolor MxMapHover()

#### markus house #
image markus_house_t = "images/world_interact/novaras_city/novh_house_markus.webp"
image markus_house_h:
    "markus_house_t"
    matrixcolor MxMapHover()

#### nijah house
image nijah_house_t = "images/world_interact/novaras_city/novh_house_nijah.webp"
image nijah_house_h:
    "nijah_house_t"
    matrixcolor MxMapHover()

### azul safehouse
image azul_safehouse_t = "images/world_interact/novaras_city/novh_house_azul.webp"
image azul_safehouse_h:
    "azul_safehouse_t"
    matrixcolor MxMapHover()

### adara house
image adara_house_t = "images/world_interact/novaras_city/novh_house_adara.webp"
image adara_house_h:
    "adara_house_t"
    matrixcolor MxMapHover()

### tanner house
image tanner_shop_t = "images/world_interact/novaras_city/novh_tanner_shop.webp"
image tanner_shop_h:
    "tanner_shop_t"
    matrixcolor MxMapHover()

init python:
    WorldLocation("novaras_dist_house", STR_LOC.NOV_DIST_HOUSE, "bg_nov_district_housing", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_dist_house"]
    # bridges
    LocDef.withBtn("bridge_novaras_house_to_mage",
        BtnChangeLoc(STR_LOC.NOV_DIST_MAGE, "novaras_dist_mage"))
    LocDef.withBtn("bridge_novaras_house_to_centre",
        BtnChangeLoc(STR_LOC.NOV_DIST_CENTRE, "novaras_dist_centre"))
    LocDef.withBtn("bridge_novaras_house_to_house_south",
        BtnChangeLoc(STR_LOC.NOV_DIST_HOUSE_S, "novaras_dist_house_south"))
    # houses
    LocDef.withBtn("btn_mc_house", BtnChangeLoc(STR_LOC.NOV_MC_HOUSE, "mc_house_kitchen"))
    LocDef.withBtn("btn_markus_house", BtnChangeLoc(STR_LOC.NOV_MARKUS_HOUSE, "markus_house_livingroom"))
    LocDef.withBtn("btn_adara_house", BtnDisabled())
    LocDef.withBtn("btn_azul_safehouse", BtnDisabled())
    LocDef.withBtn("btn_nijah_house", BtnDisabled())
    LocDef.withBtn("btn_tanner_shop", BtnDisabled())
    # quest-bound dealer button BeneathTheShadows
    LocDef.withBtn("btn_novaras_house_dist_dealer", BtnDisabled())
    # shared event clickable
    LocDef.withBtn("btn_shared_clickable_event_house", BtnDisabled())

    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_mc_house": soundLib["woodenDoor"],
                        "btn_markus_house": soundLib["woodenDoor"],
                        "btn_nijah_house": soundLib["woodenDoor"],
                        "btn_adara_house": soundLib["woodenDoor"],
                        "btn_tanner_shop": soundLib["woodenDoor"],
                        "btn_azul_safehouse": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_dist_house_night"] = {
        "lightpost_small":[(310, 112), (310, 175), (299, 354), (280, 470), (281, 576),
                            (298, 656), (614, 67), (862, 66), (1023, 67), (1109, 75),
                            (1434, 60), (647, 962), (813, 963), (1219, 955), (1377, 958),
                            (718, 710), (633, 525), (626, 375), (902, 376), (1086, 737),
                            (1174, 602), (1294, 438), (1180, 207)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_dist_house():
    default locTag = "novaras_dist_house"
    # bridges
    use locBtn_sprite(locTag, "bridge_novaras_house_to_mage",
        "novaras_bridge_housing_north_t", "novaras_bridge_housing_north_h",
        Transform(anchor = (0.5, 0.0), pos = (0.5214, 0.0)), 
        key = config.keymap["nav_up"])
    use locBtn_sprite(locTag, "bridge_novaras_house_to_centre",
        "novaras_bridge_housing_west_t", "novaras_bridge_housing_west_h",
        Transform(anchor = (0.0, 0.5), pos = (0.0, 0.45)), 
        key = config.keymap["nav_left"])
    use locBtn_sprite(locTag, "bridge_novaras_house_to_house_south",
        "novaras_bridge_housing_south_t", "novaras_bridge_housing_south_h",
        Transform(anchor = (0.5, 1.0), pos = (0.5285, 1.0)), 
        key = config.keymap["nav_down"])
    # houses
    use locBtn_sprite(locTag, "btn_mc_house",
        "mc_house_t", "mc_house_h",
        Transform(anchor = (0.0, 0.0), pos = (733, 520)))
    use locBtn_sprite(locTag, "btn_markus_house",
        "markus_house_t", "markus_house_h",
        Transform(anchor = (0.0, 0.0), pos = (962, 501)))
    use locBtn_sprite(locTag, "btn_nijah_house",
        "nijah_house_t", "nijah_house_h",
        Transform(anchor = (0.0, 0.0), pos = (1575, 821)))
    use locBtn_sprite(locTag, "btn_azul_safehouse",
        "azul_safehouse_t", "azul_safehouse_h",
        Transform(anchor = (0.5, 1.0), pos = (1609, 783))) 
    use locBtn_sprite(locTag, "btn_tanner_shop",
        "tanner_shop_t", "tanner_shop_h",
        Transform(anchor = (0.0, 0.0), pos = (398, 25)))
    use locBtn_sprite(locTag, "btn_adara_house",
        "adara_house_t", "adara_house_h",
        Transform(anchor = (0.5, 1.0), pos = (541, 550)))

    # carina's dealer
    use locBtn_basic(locTag, "btn_novaras_house_dist_dealer",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.75, 0.85)))

    use locBtn_basic(locTag, "btn_shared_clickable_event_house",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.462, 0.344)))
