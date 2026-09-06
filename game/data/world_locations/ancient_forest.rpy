init python:
    WorldLocation("ancient_forest", STR_LOC.ANCIENT_FOREST, "bg_ancient_forest", WorldMapRootLocTag = "ancient_forest")
    LocDef = wLocs["ancient_forest"]
    LocDef.withBtn("ancient_forest_travel", BtnTravel())
    LocDef.withBtn("ancient_forest_dreamhouse", BtnDisabled())
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/forest_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/forest_night.ogg")
    # travel
    LocDef.withWorldMap(STR_LOC.ANCIENT_FOREST,
        ["ancient_forest", "nubarian_tribelands"],
        "images/world_map/ancient_forest.webp",
        (2349, 341))

screen loc_ancient_forest():
    default locTag = "ancient_forest"

    use locBtn_basic(locTag, "ancient_forest_travel",
        "images/gui/buttons_loc/travel.webp",
        Transform(pos = (0.5, 0.85)), 
        key = config.keymap["nav_down"])

    use locBtn_basic(locTag, "ancient_forest_dreamhouse",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.23, 0.25)),
        )
