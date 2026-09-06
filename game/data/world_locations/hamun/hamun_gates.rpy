init python:
    WorldLocation("hamun_gates", STR_LOC.HAMUN_CITY_GATES, "bg_hamun_gates", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_gates"]
    LocDef.withBtn("hamun_gates_to_city", BtnChangeLoc(STR_NAV.ENTER_CITY, "hamun_dist_docks"))
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    # 
    LocDef.withBtn("btn_hamun_gates_spy", BtnDisabled())
    # vfx
    vfxLibLights["hamun_gates_night"] = {
        "lightpost_huge":[(411, 140), (1187, 309), (1632, 431)],
        "lightpost_big":[(1906, 607)],
        "lightpost_small":[(449, 457), (556, 588), (580, 659), (551, 662)],
        "light_crystal_yellow":[(227, 583), (963, 667)]}
    vfxLibLights["hamun_gates"] = {
        "light_crystal_yellow":[(227, 583), (963, 667)]
    }
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

    # travel
    LocDef.withBtn("hamun_gates_travel", BtnTravel())
    LocDef.withWorldMap(STR_LOC.HAMUN_CITY,
        ["lake_peacing", "demorai_temple", "nubarian_tribelands"],
        "images/world_map/hamun.webp",
        (2349, 1008))
    # sfx
    LocDef.withActionSFXs({"hamun_gates_to_city": "audio/interactables/gate_drop.ogg"})

screen loc_hamun_gates():
    default locTag = "hamun_gates"

    use locBtn_basic(locTag, "hamun_gates_to_city",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.296, 0.661)),
        key = config.keymap["nav_up"])

    use locBtn_basic(locTag,"hamun_gates_travel",
        "images/gui/buttons_loc/travel.webp",
        Transform(pos = (0.5, 0.85)), 
        key = config.keymap["nav_down"])
    use locBtn_Char(locTag, "btn_hamun_gates_spy",
        "cg_assassin", "cg_assassin",
        Transform(anchor = (0.5, 1.0), pos = (0.69, 0.97), zoom = 0.25, xzoom = -1.0))
