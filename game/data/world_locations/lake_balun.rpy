init python:
    WorldLocation("lake_balun", STR_LOC.LAKE_BALUN, "bg_lake_balun", WorldMapRootLocTag = "lake_balun")
    LocDef = wLocs["lake_balun"]
    LocDef.withBtn("btn_lake_balun_explore", BtnDisabled())
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    # music
    LocDef.withDayMusic("audio/music/13_AbandFort.ogg")
    LocDef.withNightMusic("audio/music/13_AbandFort.ogg")
    # accessible via map
    LocDef.withBtn("lake_balun_travel", BtnTravel())
    LocDef.withWorldMap(STR_LOC.LAKE_BALUN, # wmap location name on hover
        ["novaras_gates"], # wmap connections as [wloc id, wloc id, wloc id]
        "images/world_map/lake_balun.webp", # wmap image
        (914, 856)) # wmap coords in px rel to total map size
    # vfx
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_lake_balun():
    default locTag = "lake_balun"
    use locBtn_basic(locTag, "lake_balun_travel",
        "images/gui/buttons_loc/travel.webp",
        Transform(pos = (0.15, 0.75)), 
        key = config.keymap["nav_left"])
    # bloodhound quest buttons
    use locBtn_basic(locTag, "lake_balun_camp",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.5, 0.75)))
    use locBtn_basic(locTag, "lake_balun_water",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.7, 0.7)))
    # explore button
    use locBtn_basic(locTag, "btn_lake_balun_explore",
        "images/gui/buttons_loc/explore.webp",
        Transform(pos = (0.85, 0.75)))