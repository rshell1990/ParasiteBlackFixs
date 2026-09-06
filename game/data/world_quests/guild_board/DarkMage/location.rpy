init python:
    WorldLocation("novaras_darkmage_room", STR_LOC.ABANDONED_HOUSE, "bg_darkmage_room", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_darkmage_room"]
    # music
    LocDef.withDayMusic("audio/music/15_Experiments.ogg")
    LocDef.withNightMusic("audio/music/15_Experiments.ogg")

screen loc_novaras_darkmage_room():
    default locTag = "novaras_darkmage_room"

    use locBtn_basic(locTag, "btn_darkmage_shelf", 
        "images/gui/buttons_loc/question.webp", 
        Transform(pos = (0.5, 0.5)))