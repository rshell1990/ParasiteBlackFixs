##### church ######
image novaras_church_t = "images/world_interact/novaras_city/novh_church.webp"
image novaras_church_h:
    "novaras_church_t"
    matrixcolor MxMapHover()
##### poltrik estate ######
image novaras_poltrik_estate_t = "images/world_interact/novaras_city/novh_poltrik_estate.webp"
image novaras_poltrik_estate_h:
    "novaras_poltrik_estate_t"
    matrixcolor MxMapHover()

init python:
    WorldLocation("novaras_dist_house_south", STR_LOC.NOV_DIST_HOUSE_S, "bg_nov_district_housing2", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_dist_house_south"]
    # bridges
    LocDef.withBtn("bridge_novaras_house_south_to_house", 
        BtnChangeLoc(STR_LOC.NOV_DIST_HOUSE, "novaras_dist_house"))
    LocDef.withBtn("bridge_novaras_house_south_to_army", 
        BtnChangeLoc(STR_LOC.NOV_DIST_ARMY, "novaras_dist_army"))
    # houses
    LocDef.withBtn("btn_novaras_church", 
        BtnChangeLoc(STR_LOC.NOV_CHURCH, "novaras_church"))
    # poltrik/mc estate
    LocDef.withBtn("btn_novaras_poltrik_family_estate", BtnDisabled())
    # shared event clickable
    LocDef.withBtn("btn_shared_clickable_event_house_south", BtnDisabled())

    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # vfx
    vfxLibLights["novaras_dist_house_south_night"] = {
        "lightpost_small":[(336, 159), (335, 320), (326, 555), (331, 708),
                            (617, 110), (831, 110), (1052, 122), (1246, 119),
                            (519, 373), (693, 239), (705, 357), (975, 240),
                            (1223, 269), (680, 484), (560, 591), (758, 606),
                            (898, 621), (1066, 729), (1098, 619), (988, 475), (1296, 679), (1279, 444)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_dist_house_south():
    default locTag = "novaras_dist_house_south"
    # bridges
    use locBtn_sprite(locTag,"bridge_novaras_house_south_to_house", 
        "novaras_bridge_housing2_north_t","novaras_bridge_housing2_north_h",
        Transform(anchor = (0.5, 0.0), pos = (0.4915, 0.0)), 
        key = config.keymap["nav_up"])
    use locBtn_sprite(locTag, "bridge_novaras_house_south_to_army", 
        "novaras_bridge_housing2_west_t", "novaras_bridge_housing2_west_h",
        Transform(anchor = (0.0, 0.5), pos = (0.0, 0.462)), 
        key = config.keymap["nav_left"])
    # houses
    use locBtn_sprite(locTag, "btn_novaras_church",
        "novaras_church_t", "novaras_church_h",
        Transform(anchor = (0.5, 1.0), pos = (1436, 879)))    
    use locBtn_sprite(locTag, "btn_novaras_poltrik_family_estate",
        "novaras_poltrik_estate_t", "novaras_poltrik_estate_h",
        Transform(anchor = (0.0, 0.0), pos = (380, 70)))

    use locBtn_basic(locTag, "btn_shared_clickable_event_house_south",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.495, 0.485)))


