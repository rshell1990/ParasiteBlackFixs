init python:
    WorldLocation("novaras_adv_guild", STR_LOC.NOV_ADV_GUILD, "bg_guild", parent = "novaras_dist_market", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_adv_guild"]
    LocDef.withBtn("btn_novaras_adv_guild_toCity", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("visitThea", BtnDisabled())
    LocDef.withBtn("btn_thea_talk", BtnDisabled())
    LocDef.withBtn("btn_novaras_guild_board", BtnDisabled())

    # the coming storm qst 
    LocDef.withBtn("btn_thecomingstorm_attend_meeting", BtnDisabled())

    # music
    LocDef.withDayMusic("audio/music/17_Guild.ogg")
    LocDef.withNightMusic("audio/music/17_Guild.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_novaras_adv_guild_toCity": soundLib["woodenDoor"],
                        "visitThea": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["guild_night"] = {
        "lightpost_big":[(463, 420), (620, 301), (817, 273), (904, 299), (954, 431),
                        (1070, 403), (1214, 453), (1354, 324), (1456, 418), (1609, 370)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_adv_guild():
    default locTag = "novaras_adv_guild"
    use locShared_toCityBtn(locTag, "btn_novaras_adv_guild_toCity")
    use locBtn_Char(locTag, "btn_thea_talk",
        "thea", "thea",
        Transform(anchor = (0.5, 0.5), pos = (0.7, 0.5), zoom = 0.6, xzoom = -1.0))
    use locBtn_basic(locTag, "btn_novaras_guild_board", 
        "images/gui/buttons_loc/question.webp", 
        Transform(pos = (0.24, 0.33)))
    use locBtn_basic(locTag,"visitThea",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.56, 0.31))) # 1067,339

    # coming storm quest button
    use locBtn_basic(locTag, "btn_thecomingstorm_attend_meeting",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.44, 0.62)))