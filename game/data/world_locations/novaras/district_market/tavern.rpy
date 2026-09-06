init python:
    WorldLocation("novaras_tavern", STR_LOC.NOV_TAVERN, "bg_tavern", parent = "novaras_dist_market", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_tavern"]
    LocDef.withBtn("novaras_tavern_toCity",     BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("btn_talk_shay",             BtnDisabled())
    LocDef.withBtn("lukkan_tavern_talk_btn",    BtnDisabled())
    LocDef.withBtn("btn_mr_winward_gambling",   BtnDisabled())
    # mika talk
    LocDef.withBtn("btn_novaras_tavern_mika_talk", BtnDisabled())
    # ambience fx
    LocDef.withDayAmbience("audio/ambience_loc/tavern.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/tavern.ogg")
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/6_Tavern.ogg")
    # action sfx
    LocDef.withActionSFXs({"novaras_tavern_toCity": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_tavern_night"] = {
        "lightpost_huge":   [(1661, 606)],
        "lightpost_big":    [(222, 675)],
        "lightpost_small":  [(1124, 584), (985, 640), (966, 675), (802, 506), (460, 616)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_tavern():
    default locTag = "novaras_tavern"
    use locShared_toCityBtn(locTag, "novaras_tavern_toCity")
    
    # lukkan appears sometimes
    use locBtn_Char(locTag, "lukkan_tavern_talk_btn", 
        "lukkan", "lukkan", 
        Transform(anchor = (0.5, 0.5), pos = (0.73, 0.7), xzoom = -1.0, zoom = 0.8))

    # graceful rebirth quest
    use locBtn_Char(locTag, "jurgen_tavern_talk_btn", 
        "cg_guard_base", "cg_guard_base", 
        Transform(anchor = (0.5, 0.5), pos = (0.35, 0.55), zoom = 0.7, xzoom = -1.0))
    
    # the jackpot quest
    use locBtn_Char(locTag, "btn_mr_winward_gambling", 
        "mr_winward", "mr_winward", 
        Transform(anchor = (0.5, 0.5), pos = (0.7, 0.65), zoom = 0.7, xzoom = -1.0))

    # shay
    use locBtn_Char(locTag,"btn_talk_shay",
        "shay", "shay",
        Transform(anchor = (0.5, 0.5), pos = (0.15, 0.72), zoom = 1.1))

    # Thea romance - Step 1
    use locBtn_Char(locTag,"thea_romance_btn",
        "thea", "thea",
        Transform(anchor = (0.0, 0.0), pos = (1758, 352), zoom = 0.32, xzoom = -1.0))

    use locBtn_basic(locTag,"unicorn_date_btn",
        "images/gui/buttons_loc/heart.webp",
        Transform(pos = (0.4, 0.6)))

    #mika
    use locBtn_Char(locTag, "btn_novaras_tavern_mika_talk", 
        "mika", "mika", 
        Transform(anchor = (0.5, 0.5), pos = (0.4, 0.7), zoom = 0.8))
