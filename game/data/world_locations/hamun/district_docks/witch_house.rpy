init python:
    WorldLocation("hamun_witch_house", STR_LOC.HAMUN_WITCH_HOUSE, "cg_nov_witch", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_witch_house"]
    LocDef.CanWait = False

    # clickables
    LocDef.withBtn("hamun_witch_house_to_docks", BtnChangeLoc(STR_LOC.HAMUN_DIST_DOCKS, "hamun_dist_docks")) 
    LocDef.withBtn("btn_hamun_talk_to_babazhul", BtnDisabled())
    # music
    LocDef.withNightMusic("audio/music/32_Mind_of_Mysteries.ogg")
    LocDef.withDayMusic("audio/music/32_Mind_of_Mysteries.ogg")
    # action sfx
    LocDef.withActionSFXs({"hamun_witch_house_to_docks": soundLib["tentFlap"]})
    # vfx
    vfxLibLights["hamun_witch_house_night"] =   {"lightpost_huge":[(1384, 498)]}
    vfxLibLights["hamun_witch_house"] =         {"lightpost_huge":[(1384, 498)]}


screen loc_hamun_witch_house():
    default locTag = "hamun_witch_house"

    use locShared_toCityBtn(locTag, "hamun_witch_house_to_docks")

    use locBtn_basic(locTag, "btn_hamun_talk_to_babazhul",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.5, 0.5)))

    add "babazhul_blink_cond":
        pos (0.0, 0.0)
    