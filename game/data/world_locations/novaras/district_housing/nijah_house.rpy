init python:
    # this "unlocks" (enables) clickey house after quest is compl.
    @AppendToAllQuests
    class HouseLockNijah(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_house":
                if IsDaytime():
                    btnMods["btn_nijah_house"] = BtnChangeLoc(STR_LOC.NOV_NIJAH_HOUSE, "nijah_house_lroom")
                else:
                    btnMods["btn_nijah_house"] = BtnJumpLabel(STR_LOC.NOV_NIJAH_HOUSE, "HouseLockLines")
            return LocButtonMod(directMods=btnMods)

init python:
    WorldLocation("nijah_house_lroom", STR_LOC.NOV_NIJAH_HOUSE_LIV, "bg_nijah_livingroom", parent = "novaras_dist_house", WorldMapRootLocTag = "novaras_gates")
    WorldLocation("nijah_house_broom", STR_LOC.NOV_NIJAH_HOUSE_BED, "bg_nijah_bedroom", parent = "nijah_house_lroom", WorldMapRootLocTag = "novaras_gates")
    ##### LIVIN ROOM
    LocDef = wLocs["nijah_house_lroom"]
    LocDef.withBtn("nijah_house_lroom_exit", BtnChangeLoc(STR_NAV.LEAVE, "novaras_dist_house"))
    LocDef.withBtn("to_bedroom", BtnChangeLoc(STR_NAV.TO_BEDROOM, "nijah_house_broom"))
    LocDef.withBtn("nijah_talk_btn", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"nijah_house_lroom_exit": soundLib["woodenDoor"],
                        "to_bedroom": soundLib["woodenDoor"]})
    LocDef.SetDayNightMatrixClass(MxDayNight)

    ##### BEDROOM
    LocDef = wLocs["nijah_house_broom"]
    LocDef.withBtn("nijah_house_broom_exit", BtnChangeLoc(STR_NAV.TO_LIVING_ROOM, "nijah_house_lroom"))
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"nijah_house_broom_exit": soundLib["woodenDoor"]})
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_nijah_house_lroom():
    default locTag = "nijah_house_lroom"

    use locBtn_basic(locTag, "nijah_house_lroom_exit",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)), key = config.keymap["nav_down"])

    use locBtn_basic(locTag, "to_bedroom", 
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.74, 0.5)), key = config.keymap["nav_right"])

    use locBtn_Char(locTag, "nijah_talk_btn",
        "nijah", "nijah",
        Transform(anchor = (0.5, 0.5), pos = (0.35, 0.6), zoom = 0.75))

screen loc_nijah_house_broom():
    default locTag = "nijah_house_broom"

    use locBtn_basic(locTag,"nijah_house_broom_exit",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)), key = config.keymap["nav_down"])
