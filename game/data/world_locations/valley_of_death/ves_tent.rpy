init python:
    WorldLocation("ves_tent_int", STR_LOC.VES_TENT_INT, "bg_ves_tent", parent = "ves_camp", WorldMapRootLocTag = "ves_camp")
    LocDef = wLocs["ves_tent_int"]
    LocDef.withBtn("ves_tent_int_leave",
        BtnChangeLoc(STR_NAV.LEAVE, "ves_camp"))
    # ves
    LocDef.withBtn("talkVes", BtnDisabled())
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    # music
    LocDef.withDayMusic("audio/music/20_Orc_Camp.ogg")
    LocDef.withNightMusic("audio/music/20_Orc_Camp.ogg")
    # sfx
    LocDef.withActionSFXs({"ves_tent_int_leave": soundLib["tentFlap"]})
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_ves_tent_int():
    default locTag = "ves_tent_int"
    use locBtn_basic(locTag,"ves_tent_int_leave",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)), 
        key = config.keymap["nav_down"])
    use locBtn_Char(locTag, "talkVes",
        "ves", "ves",
        Transform(anchor = (0.5, 0.5), pos = (0.3, 0.65), zoom = 0.9))
