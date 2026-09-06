init python:
    WorldLocation("lake_peacing", STR_LOC.LAKE_PEACING, "bg_lake_peacing", WorldMapRootLocTag = "lake_peacing")
    LocDef = wLocs["lake_peacing"]
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    # music
    LocDef.withDayMusic("audio/music/13_AbandFort.ogg")
    LocDef.withNightMusic("audio/music/13_AbandFort.ogg")
    # accessible via map
    LocDef.withBtn("lake_peacing_travel", BtnTravel())
    LocDef.withWorldMap(STR_LOC.LAKE_PEACING,
        ["novaras_gates", "hamun_gates"],
        "images/world_map/lake_peacing.webp",
        (1977, 816))
    # vfx
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_lake_peacing():
    default locTag = "lake_peacing"
    use locBtn_basic(locTag, "lake_peacing_travel",
        "images/gui/buttons_loc/travel.webp",
        Transform(pos = (0.5, 0.85)), 
        key = config.keymap["nav_down"])