init python:
    WorldLocation("hamun_market", STR_LOC.HAMUN_MARKET, "bg_hamun_market", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_market"]

    # clickables
    LocDef.withBtn("hamun_market_to_docks", BtnChangeLoc(STR_LOC.HAMUN_DIST_DOCKS, "hamun_dist_docks")) 

    LocDef.withBtn("btn_hamun_market_marbella_dom_disguise", BtnDisabled())
    LocDef.withBtn("btn_hamun_market_lady_tarbeck", BtnDisabled())

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

screen loc_hamun_market():
    default locTag = "hamun_market"

    # exit outside
    use locBtn_basic(locTag, "hamun_market_to_docks",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    use locBtn_Char(locTag, "btn_hamun_market_marbella_dom_disguise",
        "marbella_robe", "marbella_robe", 
        Transform(anchor = (0.5, 1.0), pos = (0.6, 0.8), zoom = 0.6, xzoom = -1.0))
    
    use locBtn_Char(locTag, "btn_hamun_market_lady_tarbeck", 
        "lady_tarbeck", "lady_tarbeck", 
        Transform(anchor = (0.5, 1.0), pos = (0.3, 0.86), zoom = 0.54))
   