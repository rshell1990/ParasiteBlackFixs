init python:
    WorldLocation("demorai_temple_interior", STR_LOC.DEMORAI_TEMPLE_INT, "bg_demorai_temple_interior", WorldMapRootLocTag = "demorai_temple")
    LocDef = wLocs["demorai_temple_interior"]
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/cave.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/cave.ogg")
    # music
    LocDef.withDayMusic("audio/music/8_ValleyofDeath.ogg")
    LocDef.withNightMusic("audio/music/8_ValleyofDeath.ogg")
    # fluffy clickables
    LocDef.withBtn("BtnFluffRuins",    BtnFluffTxt(_("Ruins"),     _("These ruins look like they were some kind of a temple. A {b}long{/b} time ago.")))
    LocDef.withBtn("BtnFluffStatue",   BtnFluffTxt(_("Statue"),    _("This statue... Clearly not one of {i}our{/i} goddesses.")))
    LocDef.withBtn("BtnKrakenWater",   BtnFluffTxt(_("Water"),     _("Splash!")))
    # leave
    LocDef.withBtn("demoraiTempleLeave",BtnChangeLoc(STR_NAV.LEAVE, "demorai_temple"))

screen loc_demorai_temple_interior():
    default locTag = "demorai_temple_interior"

    use locBtn_basic(locTag,"BtnFluffRuins",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.17, 0.42)))
    use locBtn_basic(locTag,"BtnFluffStatue",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.67, 0.34)))
    use locBtn_basic(locTag,"BtnKrakenWater",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.74, 0.84)))

    use locBtn_basic(locTag,"demoraiTempleLeave",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.13, 0.85)))