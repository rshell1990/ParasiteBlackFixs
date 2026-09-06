init python:
    WorldLocation("hamun_library", STR_LOC.HAMUN_LIBRARY, "bg_hamun_library", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_library"]

    # clickables
    LocDef.withBtn("hamun_library_to_dist_merch_lord", BtnChangeLoc(STR_LOC.HAMUN_DIST_MERCH_LORD, "hamun_dist_merch_lord")) 
    LocDef.withBtn("btn_hamun_library_numa_talk", BtnDisabled())

    # action sfx
    LocDef.withActionSFXs({"hamun_library_to_dist_merch_lord": soundLib["tentFlap"]})

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    # vfx "small huge big" are default lightposts
    vfxLibLights["hamun_library_night"] = {
        "lightpost_big":[(1722, 388), (1484, 413), (1204, 407), (722, 411), (436, 414), (199, 399)],
        }
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_library():
    default locTag = "hamun_library"

    # exit outside
    use locBtn_basic(locTag, "hamun_library_to_dist_merch_lord",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
    
    use locBtn_Char(locTag, "btn_hamun_library_numa_talk",
        "numa", "numa",
        Transform(anchor = (0.5, 1.0), pos = (0.35, 1.2)))

    use locBtn_basic(locTag, "btn_hamun_library_bookshelves",
        "images/gui/buttons_loc/chest.webp", 
        Transform(pos = (0.84, 0.48)))