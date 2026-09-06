init python:
    WorldLocation("hamun_giselra_store", STR_LOC.HAMUN_GISELRA_STORE, "bg_hamun_giselra_tailor", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_giselra_store"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_giselra_store_to_docks", BtnChangeLoc(STR_LOC.HAMUN_DIST_DOCKS, "hamun_dist_docks")) 
    LocDef.withBtn("btn_talk_giselra_store", BtnDisabled())
    # action sfx
    LocDef.withActionSFXs({"hamun_giselra_store_to_docks": soundLib["tentFlap"]})
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_giselra_store():
    default locTag = "hamun_giselra_store"

    # exit outside
    use locBtn_basic(locTag, "hamun_giselra_store_to_docks",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    # giselra clickable
    use locBtn_Char(locTag, "btn_talk_giselra_store",
        "giselra", "giselra",
        Transform(anchor = (0.5, 1.0), pos = (0.77, 0.91), zoom = 0.55, xzoom = -1.0))