init python:
    WorldLocation("thea_room", STR_LOC.NOV_ADV_GUILD_THEA_ROOM, "bg_thea_room", parent = "novaras_adv_guild", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["thea_room"]
    LocDef.CanWait = False

    LocDef.withBtn("thea_room_exit", BtnChangeLoc(STR_NAV.LEAVE, "novaras_adv_guild"))
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # ambience fx
    LocDef.withDayAmbience("audio/ambience_scenes/campfire.ogg")
    LocDef.withNightAmbience("audio/ambience_scenes/campfire.ogg")
    # action sfx
    LocDef.withActionSFXs({"thea_room_exit": soundLib["woodenDoor"]})

screen loc_thea_room():
    default locTag = "thea_room"

    use locBtn_basic(locTag,"thea_room_exit",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.2, 0.9)))
