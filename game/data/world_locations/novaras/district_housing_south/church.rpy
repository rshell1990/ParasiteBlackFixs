init python:
    WorldLocation("novaras_church", STR_LOC.NOV_CHURCH, "bg_church", parent = "novaras_dist_house_south", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_church"]
    LocDef.withBtn("novaras_church_toCity", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("btn_church_to_graveyard", BtnChangeLoc(STR_LOC.GRAVEYARD, "novaras_graveyard"))
    LocDef.withBtn("btn_kylisa_talk", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/36_Holiness.ogg")
    LocDef.withNightMusic("audio/music/36_Holiness.ogg")
    # vfx
    vfxLibLights["novaras_church_night"] = {
        "lightpost_big":[(642, 325), (700, 330), (759, 311), (1145, 304), (1202, 327), (1262, 319)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)


screen loc_novaras_church():
    default locTag = "novaras_church"
    # exit button
    use locShared_toCityBtn(locTag, "novaras_church_toCity")
    # to graveyard
    use locBtn_basic(locTag, "btn_church_to_graveyard",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.34, 0.54)), key = config.keymap["nav_left"])
    # chars
    use locBtn_Char(locTag, "btn_kylisa_talk",
        "kylisa", "kylisa",
        Transform(anchor = (0.5, 1.0), pos = (0.58, 0.85), zoom = 0.42))

init python:
    WorldLocation("novaras_graveyard", STR_LOC.GRAVEYARD, "bg_graveyard", parent = "novaras_church", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_graveyard"]
    LocDef.withBtn("btn_graveyard_to_church", BtnChangeLoc(STR_LOC.NOV_CHURCH, "novaras_church"))
    LocDef.withBtn("btn_mrswinward", BtnDisabled())

    LocDef.withDayMusic("audio/music/36_Holiness.ogg")
    LocDef.withNightMusic("audio/music/36_Holiness.ogg")

    # vfx
    vfxLibLights["novaras_graveyard_night"] = {
        "lightpost_huge":[(1399, 209)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_graveyard():
    default locTag = "novaras_graveyard"

    use locBtn_basic(locTag, "btn_graveyard_to_church",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)), key = config.keymap["nav_down"])

    use locBtn_Char(locTag, "btn_mrswinward",
        "mrs_winward_funeral_baked", "mrs_winward_funeral_baked",
        Transform(anchor = (0.5, 0.5), pos = (0.3, 0.6), zoom = 0.9))