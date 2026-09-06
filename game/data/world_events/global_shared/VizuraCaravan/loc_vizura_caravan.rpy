init python:
    WorldLocation("travel_node_vizura_caravan", STR_LOC.VIZURA_CARAVAN, "pbat_desert")
    LocDef = wLocs["travel_node_vizura_caravan"]
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    # music
    LocDef.withDayMusic("audio/music/40_Wander.ogg")
    LocDef.withNightMusic("audio/music/40_Wander.ogg")

    # WARNING this should never be reached
    LocDef.withBtn("btn_test_button", BtnChangeLoc(STR_NAV.LEAVE, "mc_house_kitchen"))

screen loc_travel_node_vizura_caravan():
    default locTag = "travel_node_vizura_caravan"

    use locBtn_basic(locTag, "btn_test_button",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.70, 0.88)))