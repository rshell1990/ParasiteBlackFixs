init python:
    # both smithy & arlena room created here
    WorldLocation("novaras_blacksmith", STR_LOC.NOV_BLACKSMITH, "bg_blacksmith", parent = "novaras_dist_farm", WorldMapRootLocTag = "novaras_gates")
    WorldLocation("arlena_room", STR_LOC.NOV_ARLENA_ROOM, "bg_arlena_bedroom", parent = "novaras_blacksmith", WorldMapRootLocTag = "novaras_gates")
    ### smithy
    LocDef = wLocs["novaras_blacksmith"]
    LocDef.CanWait = False

    LocDef.withBtn("novaras_blacksmith_toCity", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("btn_nov_talk_drax", BtnDisabled())
    LocDef.withBtn("visitArlena", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/blacksmith.ogg")
    # action sfx
    LocDef.withActionSFXs({"novaras_blacksmith_toCity": soundLib["woodenDoor"],
                        "visitArlena": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_blacksmith_night"] = {"lightpost_huge":[(252, 464)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

    ### arlena room upstairs
    LocDef = wLocs["arlena_room"]
    LocDef.CanWait = False

    LocDef.withBtn("arlena_room_exit", BtnChangeLoc(STR_NAV.LEAVE, "novaras_blacksmith"))
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"arlena_room_exit": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["arlena_room_night"] = {"lightpost_big":[(602, 357)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_blacksmith():
    default locTag = "novaras_blacksmith"
    use locShared_toCityBtn(locTag, "novaras_blacksmith_toCity")

    use locBtn_Char(locTag, "btn_nov_talk_drax",
        "drax", "drax",
        Transform(anchor = (0.5, 0.5), pos = (0.3, 0.65), zoom = 0.9))
    use locBtn_basic(locTag, "visitArlena",
        "images/gui/buttons_loc/door.webp", Transform(pos = (0.75, 0.18)))


screen loc_arlena_room():
    default locTag = "arlena_room"

    use locBtn_basic(locTag, "arlena_room_exit",
        "images/gui/buttons_loc/door.webp", Transform(pos = (0.1, 0.45)))

    use locBtn_Char(locTag, "talkArlena",
        "arlena", "arlena", 
        Transform(anchor = (0.5, 0.5), pos = (0.7, 0.52), xzoom = -1.0, zoom = 0.8))
