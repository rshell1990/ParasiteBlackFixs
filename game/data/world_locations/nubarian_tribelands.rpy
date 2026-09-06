init python:
    WorldLocation("nubarian_tribelands", STR_LOC.NUBARIAN_TRIBELANDS, "bg_crossroads", WorldMapRootLocTag = "nubarian_tribelands")
    LocDef = wLocs["nubarian_tribelands"]

    LocDef.withBtn("nubarian_tribelands_travel", BtnTravel())
    LocDef.withBtn("btn_nubarian_tribelands_otherpath", BtnJumpLabel(_("Wander the path"), "btn_nubarian_tribelands_otherpath_text"))
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    # travel
    LocDef.withWorldMap(STR_LOC.NUBARIAN_TRIBELANDS,
        ["hamun_gates", "ancient_forest"],
        "images/world_map/nubarian_tribelands.webp",
        (2243, 596))

screen loc_nubarian_tribelands():
    default locTag = "nubarian_tribelands"

    use locBtn_basic(locTag, "nubarian_tribelands_travel",
        "images/gui/buttons_loc/travel.webp",
        Transform(pos = (0.9, 0.85)), 
        key = config.keymap["nav_right"])

    use locBtn_basic(locTag, "btn_nubarian_tribelands_otherpath",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.2, 0.8)), 
        key = config.keymap["nav_left"])

label btn_nubarian_tribelands_otherpath_text:
    MC "(I best stay on the main roads for now...)"
    $ LocEnterQ()