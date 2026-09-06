init python:
    WorldLocation("mc_house_kitchen", STR_LOC.NOV_MC_HOUSE_KITCHEN, "bg_mc_house_kitchen", parent = "novaras_dist_house", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["mc_house_kitchen"]
    LocDef.withBtn("talkRegina", BtnDisabled())
    LocDef.withBtn("bedroom", 
        BtnChangeLoc(STR_NAV.TO_BEDROOM, "mc_house_bedroom"))
    LocDef.withBtn("mc_house_kitchen_exit",
        BtnChangeLoc(STR_NAV.LEAVE, "novaras_dist_house"))

    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")

    # action sfx
    LocDef.withActionSFXs({"bedroom": soundLib["woodenDoor"],
                        "mc_house_kitchen_exit": soundLib["woodenDoor"]})
    LocDef.SetDayNightMatrixClass(MxDayNight)


screen loc_mc_house_kitchen():
    default locTag = "mc_house_kitchen"
    if not CharGetVar("regina", "hide"):
        use locBtn_Char(locTag, "talkRegina",
            "regina", "regina",
            Transform(anchor = (0.5, 0.5), pos = (0.3, 0.6), zoom = 0.8))
    use locBtn_basic(locTag, "bedroom",
        "images/gui/buttons_loc/arrow_d.webp",
        Transform(pos = (0.5, 0.85)), 
        key = config.keymap["nav_down"])
    use locBtn_basic(locTag, "mc_house_kitchen_exit",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.85, 0.35)), 
        key = config.keymap["nav_right"])
