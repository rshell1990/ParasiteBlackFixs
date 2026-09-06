init python:    
    @AppendToAllQuests
    class HouseLockHamunStore(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_dist_docks":
                if IsDaytime():
                    btnMods["hamun_docks_to_store"] = BtnChangeLoc(STR_LOC.HAMUN_GENERAL_STORE, "hamun_general_store")
                else:
                    btnMods["hamun_docks_to_store"] = BtnJumpLabel(STR_LOC.HAMUN_GENERAL_STORE, "HouseLockLines_JustClosed")
            return LocButtonMod(directMods = btnMods)

    WorldLocation("hamun_general_store", STR_LOC.HAMUN_GENERAL_STORE, "bg_hamun_store", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_general_store"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_general_store_to_docks", BtnChangeLoc(STR_LOC.HAMUN_DIST_DOCKS, "hamun_dist_docks")) 
    LocDef.withBtn("btn_talk_katiya_store", BtnDisabled())
    # action sfx
    LocDef.withActionSFXs({"hamun_general_store_to_docks": soundLib["tentFlap"]})
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    # vfx
    vfxLibLights["hamun_general_store_night"] = {
        "lightpost_huge":[(1298, 210)],
        "lightpost_big":[(99, 576), (244, 446), (441, 377)]}
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_general_store():
    default locTag = "hamun_general_store"

    # exit outside
    use locBtn_basic(locTag, "hamun_general_store_to_docks",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    use locBtn_Char(locTag, "btn_talk_katiya_store",
        "katiya", "katiya",
        Transform(anchor = (0.5, 1.0), pos = (0.3, 0.8), zoom = 0.54))