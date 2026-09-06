init python:
    WorldLocation("novaras_kennels", STR_LOC.NOV_KENNELS, "bg_novaras_kennels", parent = "novaras_dist_army", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_kennels"]
    LocDef.CanWait = False

    LocDef.withBtn("novaras_kennels_tocity",    BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("kennelmaster_talk_btn",     BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"novaras_kennels_tocity": soundLib["woodenDoor"]})
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_kennels():
    default locTag = "novaras_kennels"
    use locShared_toCityBtn(locTag, "novaras_kennels_tocity")
    use locBtn_Char(locTag, "kennelmaster_talk_btn", 
        "kennelmaster", "kennelmaster",
        Transform(anchor = (0.5, 0.5), pos = (0.65, 0.70), xzoom = -1.0, zoom = 0.85))
