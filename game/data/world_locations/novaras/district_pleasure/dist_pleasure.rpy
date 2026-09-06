# shani"s place
image novaras_bordello_t = "images/world_interact/novaras_city/novh_bordello.webp"
image novaras_bordello_h:
    "novaras_bordello_t"
    matrixcolor MxMapHover()

# teller cabin
image novaras_teller_t = "images/world_interact/novaras_city/novh_teller.webp"
image novaras_teller_h:
    "novaras_teller_t"
    matrixcolor MxMapHover()

# diamond
image novaras_diamond_t = "images/world_interact/novaras_city/novh_diamond.webp"
image novaras_diamond_h:
    "novaras_diamond_t"
    matrixcolor MxMapHover()

init python:
    WorldLocation("novaras_dist_pleasure", STR_LOC.NOV_DIST_PLEASURE, "bg_nov_district_pleasure", WorldMapRootLocTag = "novaras_gates")
    # pleasure district
    LocDef = wLocs["novaras_dist_pleasure"]
    # bridges
    LocDef.withBtn("bridge_novaras_pleasure_to_edu",
        BtnChangeLoc(STR_LOC.NOV_DIST_EDU, "novaras_dist_edu"))
    LocDef.withBtn("bridge_novaras_pleasure_to_centre",
        BtnChangeLoc(STR_LOC.NOV_DIST_CENTRE, "novaras_dist_centre"))
    LocDef.withBtn("bridge_novaras_pleasure_to_market",
        BtnChangeLoc(STR_LOC.NOV_DIST_MARKET, "novaras_dist_market"))
    # houses
    LocDef.withBtn("btn_novaras_bordello", BtnDisabled())
    LocDef.withBtn("btn_novaras_soothsayer_cabin", 
        BtnChangeLoc(STR_LOC.NOV_WITCH_HOUSE, "novaras_soothsayer_cabin"))
    LocDef.withBtn("novaras_diamond", BtnDisabled())
    # shared event clickable
    LocDef.withBtn("btn_shared_clickable_event_pleasure", BtnDisabled())

    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_novaras_soothsayer_cabin": soundLib["woodenDoor"]})
    # logic
    LocDef.withBtn("btn_nijah_rescue", BtnDisabled()) # nijah rescue event popup
    # vfx
    vfxLibLights["novaras_dist_pleasure_night"] = {
        "lightpost_big":[(246, 208), (246, 400), (253, 730), (847, 352), (847, 609), (1071, 358),
                        (1071, 615), (1572, 123), (1590, 466), (1569, 775), (953, 118)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_dist_pleasure():
    default locTag = "novaras_dist_pleasure"
    # bridges
    use locBtn_sprite(locTag, "bridge_novaras_pleasure_to_edu",
        "novaras_bridge_pl_north_t", "novaras_bridge_pl_north_h",
        Transform(anchor = (0.5, 0.0), pos = (0.4875, 0.0)), 
        key = config.keymap["nav_up"])
    use locBtn_sprite(locTag, "bridge_novaras_pleasure_to_centre",
        "novaras_bridge_pl_east_t", "novaras_bridge_pl_east_h",
        Transform(anchor = (1.0, 0.5), pos = (1.0, 0.458)), 
        key = config.keymap["nav_right"])
    use locBtn_sprite(locTag, "bridge_novaras_pleasure_to_market",
        "novaras_bridge_pl_south_t", "novaras_bridge_pl_south_h",
        Transform(anchor = (0.5, 1.0), pos = (0.494, 1.0)), 
        key = config.keymap["nav_down"])
    #### houses
    # bordello
    use locBtn_sprite(locTag, "btn_novaras_bordello",
        "novaras_bordello_t", "novaras_bordello_h",
        Transform(anchor = (0.5, 1.0), pos = (0.3475, 0.506)))
    # witchhouse
    use locBtn_sprite(locTag, "btn_novaras_soothsayer_cabin",
        "novaras_teller_t", "novaras_teller_h",
        Transform(anchor = (0.0, 0.0), pos = (1428, 457)))
    # diamond
    use locBtn_sprite(locTag, "novaras_diamond",
        "novaras_diamond_t", "novaras_diamond_h",
        Transform(anchor = (0.0, 0.0), pos = (213, 36)))
    # nijah rescue event button displayable
    use locBtn_basic(locTag, "btn_nijah_rescue",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.55, 0.25)))

    use locBtn_basic(locTag, "btn_shared_clickable_event_pleasure",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.729, 0.287)))
