image ves_tent_t = "images/world_interact/vescamp_tent.webp"
image ves_tent_h:
    "ves_tent_t"
    matrixcolor MxMapHover()

init python:
    WorldLocation("ves_camp", STR_LOC.VES_CAMP, "bg_vescamp", WorldMapRootLocTag = "ves_camp")
    LocDef = wLocs["ves_camp"]
    # houses
    LocDef.withBtn("ves_tent_int_button",
        BtnChangeLoc(STR_LOC.VES_TENT_INT, "ves_tent_int"))
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    # music
    LocDef.withDayMusic("audio/music/20_Orc_Camp.ogg")
    LocDef.withNightMusic("audio/music/20_Orc_Camp.ogg")
    # sfx
    LocDef.withActionSFXs({"ves_tent_int_button": soundLib["tentFlap"]})
    # travel
    LocDef.withBtn("ves_camp_travel", BtnTravel())
    LocDef.withWorldMap(STR_LOC.VES_CAMP,
        ["valley_of_death"],
        "images/world_map/ves_camp.webp", (1124, 1208))
    LocDef.SetDayNightMatrixClass(MxDayNight)


screen loc_ves_camp():
    default locTag = "ves_camp"
    use locBtn_basic(locTag,"ves_camp_travel",
        "images/gui/buttons_loc/travel.webp",
        Transform(pos = (0.5, 0.85)), 
        key = config.keymap["nav_down"])
    # tent
    use locBtn_basic(locTag,"ves_tent_int_button",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.25, 0.75)), 
        key = config.keymap["nav_left"])
