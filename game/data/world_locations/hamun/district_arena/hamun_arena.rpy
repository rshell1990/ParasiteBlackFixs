init python:
############# exterior (looking at gates)
    WorldLocation("hamun_arena_ext", STR_LOC.HAMUN_ARENA_EXT, "bg_hamun_arena_exterior", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_arena_ext"]

    # clickables
    LocDef.withBtn("hamun_arena_ext_to_int",           BtnChangeLoc(STR_LOC.HAMUN_ARENA_INT, "hamun_arena_int"))
    LocDef.withBtn("hamun_arena_ext_to_dist_arena",    BtnChangeLoc(STR_LOC.HAMUN_DIST_ARENA, "hamun_dist_arena"))
    LocDef.withBtn("btn_hamun_arena_ext_yarrick_talk", BtnDisabled())

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")

    # vfx "small huge big" are default lightposts
    vfxLibLights["hamun_arena_ext_night"] = {
        "lightpost_huge":[(893, 605), (1239, 606)],
        "lightpost_small":[(1695, 512), (1716, 535)],}
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

    # action sfx
    LocDef.withActionSFXs({"hamun_arena_ext_to_int": "audio/interactables/gate_drop.ogg"})

############# interior 
    WorldLocation("hamun_arena_int", STR_LOC.HAMUN_ARENA_INT, "bg_hamun_arena_interior", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_arena_int"]

    LocDef.CanWait = False

    # clickables
    LocDef.withBtn("hamun_arena_int_to_ext", BtnChangeLoc(STR_LOC.HAMUN_ARENA_EXT, "hamun_arena_ext"))
    LocDef.withBtn("btn_hamun_arena_master_talk", BtnDisabled())

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    # vfx "small huge big" are default lightposts
    vfxLibLights["hamun_arena_int_night"] = {
        "lightpost_big":[(450, 705), (1420, 703)]}
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

    # action sfx
    LocDef.withActionSFXs({"hamun_arena_int_to_ext": "audio/interactables/gate_drop.ogg"})

screen loc_hamun_arena_ext():
    default locTag = "hamun_arena_ext"

    # enter gates
    use locBtn_basic(locTag, "hamun_arena_ext_to_int",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.53, 0.58)),
        key = config.keymap["nav_up"])
    # return to dist
    use locBtn_basic(locTag, "hamun_arena_ext_to_dist_arena",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
    
    use locBtn_Char(locTag, "btn_hamun_arena_ext_yarrick_talk",
        "yarrick", "yarrick",
        Transform(anchor = (0.5, 1.0), pos = (0.169, 0.843), zoom = 0.3))

screen loc_hamun_arena_int():
    default locTag = "hamun_arena_int"

    # return to ext
    use locBtn_basic(locTag, "hamun_arena_int_to_ext",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    use locBtn_Char(locTag, "btn_hamun_arena_master_talk",
        "cg_dealer", "cg_dealer",
        Transform(anchor = (0.5, 1.0), pos = (0.37, 0.85), zoom = 0.19))
