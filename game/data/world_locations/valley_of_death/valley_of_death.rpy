init python:
    WorldLocation("valley_of_death", STR_LOC.VALLEY_OF_DEATH, "bg_valley_of_death", WorldMapRootLocTag = "valley_of_death")
    LocDef = wLocs["valley_of_death"]
    LocDef.withBtn("btn_demoraiHunt", BtnDisabled())
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    # music
    LocDef.withDayMusic("audio/music/8_ValleyofDeath.ogg")
    LocDef.withNightMusic("audio/music/8_ValleyofDeath.ogg")
    # sfx
    # 
    # travel
    LocDef.withBtn("valley_of_death_travel", BtnTravel())
    LocDef.withWorldMap(STR_LOC.VALLEY_OF_DEATH,
        ["ves_camp", "demorai_temple", "novaras_gates"],
        "images/world_map/valley_of_death.webp", (1291, 1212))
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_valley_of_death():
    default locTag = "valley_of_death"

    use locBtn_basic(locTag,"valley_of_death_travel",
        "images/gui/buttons_loc/travel.webp",
        Transform(pos = (0.5, 0.85)), 
        key = config.keymap["nav_down"])
    use locBtn_basic(locTag, "btn_demoraiHunt",
        "images/gui/buttons_loc/fight.webp",
        Transform(pos = (0.65, 0.55)))