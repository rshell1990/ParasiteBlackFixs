init python:
    WorldLocation("hamun_port", STR_LOC.HAMUN_DOCKS_PORT, "bg_hamun_port", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_port"]

    # clickables
    LocDef.withBtn("hamun_port_to_docks", BtnChangeLoc(STR_LOC.HAMUN_DIST_DOCKS, "hamun_dist_docks")) 

    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    # vfx "small huge big" are default lightposts
    vfxLibLights["hamun_market_night"] = {
        "lightpost_big":[(1795, 570), (1047, 454), (425, 537), (212, 543)],
        "lightpost_small":[(1427, 364), (1307, 364), (869, 453)]}
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_port():
    default locTag = "hamun_port"

    # exit outside
    use locBtn_basic(locTag, "hamun_port_to_docks",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
