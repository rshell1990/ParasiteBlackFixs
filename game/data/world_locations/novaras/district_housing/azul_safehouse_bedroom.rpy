init python:
    WorldLocation("azul_safehouse_bedroom", STR_LOC.NOV_AZUL_SH_BEDROOM, "bg_azul_bedroom_clean", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["azul_safehouse_bedroom"]
    LocDef.withBtn("btn_azul_to_living_room",
        BtnChangeLoc(STR_LOC.NOV_AZUL_SH, "azul_safehouse"))
    LocDef.withBtn("btn_talk_myu", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_azul_to_living_room": soundLib["woodenDoor"]})

screen loc_azul_safehouse_bedroom():
    default locTag = "azul_safehouse_bedroom"
    # exit button
    use locBtn_basic(locTag, "btn_azul_to_living_room",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.1, 0.76)), 
        key = config.keymap["nav_left"])
    use locBtn_basic(locTag, "btn_azul_monster_drawing",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.64, 0.4)))
    use locBtn_basic(locTag, "btn_azul_mad_ramblings",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.5, 0.45)))
    use locBtn_basic(locTag, "btn_azul_bed",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.2, 0.5)))
    if not CharGetVar("myu", "hide"):
        use locBtn_Char(locTag, "btn_talk_myu",
            "myu", "myu",
            Transform(anchor = (0.5, 0.5), pos = (0.5, 0.6), xzoom = -1.0, zoom = 0.8))
    if not QstTheBloodhound().basementOpen:
        use locBtn_basic(locTag, "btn_azul_strange_book",
            "images/gui/buttons_loc/question.webp",
            Transform(pos = (0.04, 0.43)))
