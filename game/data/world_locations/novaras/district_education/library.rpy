init python:
    WorldLocation("novaras_library_int", STR_LOC.NOV_LIBRARY_INT, "bg_novaras_library", parent = "novaras_dist_edu", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_library_int"]
    LocDef.CanWait = False

    LocDef.withBtn("novaras_library_int_toCity", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("vala_talk_btn", BtnDisabled())
    LocDef.withBtn("library_bookshelves", BtnDisabled())
    LocDef.withBtn("btn_comingstorm_bookshelves", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"novaras_library_int_toCity": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_library_int_night"] = {
        "lightpost_huge":[(305, 388), (1808, 195)],
        "light_haze_fiery":[(1275, 727), (1113, 699), (992, 704)],
        "lightpost_small":[(745, 725)]}
    vfxLibLights["novaras_library_int"] = {
        "lightpost_huge":[(305, 388), (1808, 195)],
        "light_haze_fiery":[(1275, 727), (1113, 699), (992, 704)],
        "lightpost_small":[(745, 725)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)
    
    @AppendToAllQuests
    class HouseLockNovarasLibrary(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_edu":
                if IsDaytime():
                    btnMods["btn_novaras_library"] = BtnChangeLoc(STR_LOC.NOV_LIBRARY_INT, "novaras_library_int")
                else:
                    btnMods["btn_novaras_library"] = BtnJumpLabel(STR_LOC.NOV_LIBRARY_INT, "HouseLockLines")
            return LocButtonMod(directMods = btnMods)

screen loc_novaras_library_int():
    default locTag = "novaras_library_int"
    use locShared_toCityBtn(locTag, "novaras_library_int_toCity")
    use locBtn_Char(locTag, "vala_talk_btn",
        "vala", "vala",
        Transform(anchor = (0.5, 0.5), pos = (0.75, 0.57), xzoom = -1.0))
    use locBtn_basic(locTag, "library_bookshelves",
        "images/gui/buttons_loc/chest.webp", 
        Transform(pos = (0.12, 0.6)))

    # coming storm quest special shelf
    use locBtn_basic(locTag, "btn_comingstorm_bookshelves",
        "images/gui/buttons_loc/chest.webp", 
        Transform(pos = (0.31, 0.42)))