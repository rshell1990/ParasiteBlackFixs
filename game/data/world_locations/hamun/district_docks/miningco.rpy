init python:    
    WorldLocation("hamun_miningco", STR_LOC.HAMUN_MININGCO, "bg_hamun_miningco", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_miningco"]
    # clickables
    LocDef.withBtn("hamun_miningco_to_docks", BtnChangeLoc(STR_LOC.HAMUN_DIST_DOCKS, "hamun_dist_docks")) 
    LocDef.withBtn("btn_talk_marbella", BtnDisabled())
    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    # vfx
    vfxLibLights["hamun_miningco_night"] = {
        "lightpost_huge":[(1030, 659)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_hamun_miningco():
    default locTag = "hamun_miningco"

    # exit outside
    use locBtn_basic(locTag, "hamun_miningco_to_docks",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.78, 0.51)),
        key = config.keymap["nav_right"])

    use locBtn_Char(locTag, "btn_talk_marbella",
        "marbella", "marbella",
        Transform(anchor = (0.5, 1.0), pos = (0.35, 0.74), zoom = 0.4))