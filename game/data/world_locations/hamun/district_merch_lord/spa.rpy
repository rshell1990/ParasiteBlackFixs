init python:
################# main room, reception
    WorldLocation("hamun_spa", STR_LOC.HAMUN_SPA, "bg_hamun_spa_main", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_spa"]

    LocDef.CanWait = False

    # clickables
    LocDef.withBtn("hamun_spa_to_male",    BtnChangeLoc(STR_LOC.HAMUN_SPA_MALE, "hamun_spa_male")) 
    LocDef.withBtn("hamun_spa_to_female",  BtnChangeLoc(STR_LOC.HAMUN_SPA_FEMALE, "hamun_spa_female"))
    LocDef.withBtn("hamun_spa_to_dist_merch_lord", BtnChangeLoc(STR_LOC.HAMUN_DIST_MERCH_LORD, "hamun_dist_merch_lord"))

    # action sfx
    LocDef.withActionSFXs({
        "hamun_spa_to_dist_merch_lord": soundLib["tentFlap"],
        "hamun_spa_to_male":            soundLib["tentFlap"],
        "hamun_spa_to_female":          soundLib["tentFlap"]
    })

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    # vfx "small big huge" lightposts exist
    vfxLibLights["hamun_spa_night"] = {
        "lightpost_huge":[(1008, 204)],
        }
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

################# fem section
    WorldLocation("hamun_spa_female", STR_LOC.HAMUN_SPA_FEMALE, "bg_hamun_spa_fem", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_spa_female"]

    LocDef.CanWait = False

    # clickables
    LocDef.withBtn("hamun_spa_fem_to_main", BtnChangeLoc(STR_LOC.HAMUN_SPA, "hamun_spa")) 

    # action sfx
    LocDef.withActionSFXs({
        "hamun_spa_fem_to_main": soundLib["tentFlap"],
    })

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/hamun_spa.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/hamun_spa.ogg")

    # vfx "small big huge" are default lightposts
    vfxLibLights["hamun_spa_female_night"] = {
        "lightpost_big":[(1019, 688)],
        "lightpost_huge":[(330, 727)],
        }
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

################# male section
    WorldLocation("hamun_spa_male", STR_LOC.HAMUN_SPA_MALE, "bg_hamun_spa_male", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_spa_male"]

    LocDef.CanWait = False

    # clickables
    LocDef.withBtn("hamun_spa_male_to_main", BtnChangeLoc(STR_LOC.HAMUN_SPA, "hamun_spa")) 
    LocDef.withBtn("btn_talk_luna", BtnDisabled())

    # action sfx
    LocDef.withActionSFXs({
        "hamun_spa_male_to_main": soundLib["tentFlap"],
    })

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/hamun_spa.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/hamun_spa.ogg")

    # vfx "small big huge" are default lightposts
    vfxLibLights["hamun_spa_male_night"] = {
        "lightpost_big":[(942, 692)],
        "lightpost_huge":[(1795, 744)],
        }
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_spa():
    default LocationTag = "hamun_spa"

    # exit outside
    use locBtn_basic(LocationTag, "hamun_spa_to_dist_merch_lord",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    # to men
    use locBtn_basic(LocationTag, "hamun_spa_to_male",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.829, 0.662)),
        key = config.keymap["nav_right"])

    # to fem
    use locBtn_basic(LocationTag, "hamun_spa_to_female",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.208, 0.669)),
        key = config.keymap["nav_left"])

    # luna
    use locBtn_Char(LocationTag, "btn_talk_luna",
        "luna", "luna",
        Transform(anchor = (0.5, 1.0), pos = (0.35, 0.866), zoom = 0.4))

screen loc_hamun_spa_female():
    default LocationTag = "hamun_spa_female"

    # exit outside
    use locBtn_basic(LocationTag, "hamun_spa_fem_to_main",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.9, 0.6)),
        key = config.keymap["nav_right"])
    
screen loc_hamun_spa_male():
    default LocationTag = "hamun_spa_male"

    # exit outside
    use locBtn_basic(LocationTag, "hamun_spa_male_to_main",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.1, 0.6)),
        key = config.keymap["nav_left"])
