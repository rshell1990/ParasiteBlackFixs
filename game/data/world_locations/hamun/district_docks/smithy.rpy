init python:    
    @AppendToAllQuests
    class HouseLockHamunSmithy(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_dist_docks":
                if IsDaytime():
                    btnMods["hamun_docks_to_smithy"] = BtnChangeLoc(STR_LOC.HAMUN_SMITHY, "hamun_smithy")
                else:
                    btnMods["hamun_docks_to_smithy"] = BtnJumpLabel(STR_LOC.HAMUN_SMITHY, "HouseLockLines_JustClosed")
            return LocButtonMod(directMods = btnMods)

    WorldLocation("hamun_smithy", STR_LOC.HAMUN_SMITHY, "bg_hamun_smithy", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_smithy"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_smithy_to_docks", BtnChangeLoc(STR_LOC.HAMUN_DIST_DOCKS, "hamun_dist_docks")) 
    LocDef.withBtn("btn_talk_beshar", BtnDisabled())
    # action sfx
    LocDef.withActionSFXs({"hamun_smithy_to_docks": soundLib["tentFlap"]})
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/blacksmith.ogg")
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    # vfx
    vfxLibLights["hamun_smithy_night"] = {
        "lightpost_huge":[(1050, 523)]}
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_smithy():
    default locTag = "hamun_smithy"

    # exit outside
    use locBtn_basic(locTag, "hamun_smithy_to_docks",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    use locBtn_Char(locTag, "btn_talk_beshar",
        "beshar", "beshar",
        Transform(anchor = (0.5, 1.0), pos = (0.78, 0.84), xzoom = -1.0, zoom = 0.57))