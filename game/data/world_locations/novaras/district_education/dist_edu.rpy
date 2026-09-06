image novaras_library_t = "images/world_interact/novaras_city/novh_library.webp"
image novaras_library_h:
    "novaras_library_t"
    matrixcolor MxMapHover()

init python:
    WorldLocation("novaras_dist_edu", STR_LOC.NOV_DIST_EDU, "bg_nov_district_education", WorldMapRootLocTag = "novaras_gates")
    # education district
    LocDef = wLocs["novaras_dist_edu"]
    # bridges
    LocDef.withBtn("bridge_novaras_edu_to_farm",
        BtnChangeLoc(STR_LOC.NOV_DIST_FARM, "novaras_dist_farm"))
    LocDef.withBtn("bridge_novaras_edu_to_pleasure",
        BtnChangeLoc(STR_LOC.NOV_DIST_PLEASURE, "novaras_dist_pleasure"))
    # houses
    LocDef.withBtn("btn_novaras_library",
        BtnChangeLoc(STR_LOC.NOV_LIBRARY_INT, "novaras_library_int"))
    # shared event clickable
    LocDef.withBtn("btn_shared_clickable_event_edu", BtnDisabled())

    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_novaras_library": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_dist_edu_night"] = {
        "lightpost_big":[(465, 694), (607, 737), (1044, 734), (1245, 628),
                        (1169, 295), (915, 201), (783, 236), (551, 375)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_dist_edu():
    default locTag = "novaras_dist_edu"
    # bridges
    use locBtn_sprite(locTag, "bridge_novaras_edu_to_farm", 
        "novaras_bridge_edu_east_t", "novaras_bridge_edu_east_h", 
        Transform(anchor = (1.0, 0.5), pos = (1.0, 0.56)), 
        key = config.keymap["nav_right"])
    use locBtn_sprite(locTag, "bridge_novaras_edu_to_pleasure", 
        "novaras_bridge_edu_south_t", "novaras_bridge_edu_south_h", 
        Transform(anchor = (0.5, 1.0), pos = (0.461, 1.0)), 
        key = config.keymap["nav_down"])
    # houses
    use locBtn_sprite(locTag, "btn_novaras_library",
        "novaras_library_t", "novaras_library_h",
        Transform(anchor = (0.0, 0.0), pos = (876, 72)))

    use locBtn_basic(locTag, "btn_shared_clickable_event_edu",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.683, 0.331)))


