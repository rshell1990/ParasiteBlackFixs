init python:
    WorldLocation("novaras_market_stalls", STR_LOC.NOV_MARKET_STALLS, "bg_novaras_market_stalls", parent = "novaras_dist_market", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_market_stalls"]
    LocDef.withBtn("novaras_market_stalls_toCity", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    # Ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # vfx
    vfxLibLights["novaras_market_stalls_night"] = {
        "lightpost_big":[(272, 618), (619, 606), (1791, 642)],
        "lightpost_small":[(803, 583), (289, 99), (627, 95), (874, 99), (1122, 102), (1755, 99)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)
    # butcher
    LocDef.withBtn("btn_novaras_market_stalls_butcher", BtnDisabled())

screen loc_novaras_market_stalls():
    default locTag = "novaras_market_stalls"
    use locShared_toCityBtn(locTag, "novaras_market_stalls_toCity")

    # nijah & her market stall overlay
    if RomanceNijah().storeOpen == True:
        if IsDaytime():
            add "bg_novaras_market_stalls_open_under_day":
                align (1.0, 1.0)
                matrixcolor wLocs[locTag].DayNightMatrixClass(GetDaytimeTintFactor())
            use locBtn_Char(locTag, "nijah_market_stalls_btn",
                "nijah", "nijah",
                Transform(anchor = (0.5, 0.5), pos = (0.82, 0.67), xzoom = -1.0, zoom = 0.35),
                NightTint = False)
            add "bg_novaras_market_stalls_open_over_day":
                align (1.0, 1.0)
                matrixcolor wLocs[locTag].DayNightMatrixClass(GetDaytimeTintFactor())
        else:
            add "bg_novaras_market_stalls_open_under_night":
                align (1.0, 1.0)
            use locBtn_Char(locTag, "nijah_market_stalls_btn",
                "nijah", "nijah",
                Transform(anchor = (0.5, 0.5), pos = (0.82, 0.67), xzoom = -1.0, zoom = 0.35),
                NightTint = False)
            add "bg_novaras_market_stalls_open_over_night":
                align (1.0, 1.0)
    # interactable trader button (for wolf quest & slime feed)
    use locBtn_basic(locTag, "btn_novaras_market_stalls_butcher",
        "images/gui/buttons_loc/dialogue.webp",
        Transform(pos = (0.35, 0.5)))
