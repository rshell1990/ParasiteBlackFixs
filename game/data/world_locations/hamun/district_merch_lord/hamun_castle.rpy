############################################################################################################
####### castle
init python:
    @AppendToAllQuests
    class HouseLockHamunCastle(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_dist_merch_lord":
                btnMods["hamun_dist_merch_lord_to_castle"] = BtnChangeLoc(STR_LOC.HAMUN_CASTLE, "hamun_castle_entrance")
            return LocButtonMod(directMods = btnMods)

    WorldLocation("hamun_castle_entrance", STR_LOC.HAMUN_CASTLE_ENTRANCE, "bg_hamun_castle_entrance", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_castle_entrance"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_castle_to_dist_merch_lord", BtnChangeLoc(STR_LOC.HAMUN_DIST_MERCH_LORD, "hamun_dist_merch_lord"))
    LocDef.withBtn("hamun_castle_to_tea_room", BtnChangeLoc(STR_LOC.HAMUN_CASTLE_TEA_ROOM, "hamun_castle_tea_room"))
    # ld tarbeck during pt 2 quest
    LocDef.withBtn("btn_hamun_castle_entrance_lady_tarbeck", BtnDisabled())

    vfxLibLights["hamun_castle_entrance_night"] = {
        "lightpost_huge":[(284, 691), (1640, 688)],
        "lightpost_big":[(699, 621), (1220, 620), (832, 577), (1089, 575)],
    }

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_castle_entrance():
    default locTag = "hamun_castle_entrance"

    # exit outside
    use locBtn_basic(locTag, "hamun_castle_to_dist_merch_lord",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    # tea room
    use locBtn_basic(locTag, "hamun_castle_to_tea_room",
        "images/gui/buttons_loc/arrow_l.webp",
        Transform(pos = (0.2, 0.5)),
        key = config.keymap["nav_left"])

    # lady tarbeck
    use locBtn_Char(locTag, "btn_hamun_castle_entrance_lady_tarbeck",
        "lady_tarbeck", "lady_tarbeck",
        Transform(anchor = (0.5, 1.0), pos = (0.75, 0.78), xzoom = -1.0, zoom = 0.24))

init python:
    WorldLocation("hamun_castle_tea_room", STR_LOC.HAMUN_CASTLE_TEA_ROOM, "bg_hamun_castle_tea_room", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_castle_tea_room"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_castle_tea_room_to_entrance",     BtnChangeLoc(STR_LOC.HAMUN_CASTLE_ENTRANCE, "hamun_castle_entrance"))
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)
    
    vfxLibLights["hamun_castle_tea_room_night"] = {
        "lightpost_small":[(1813, 516), (1646, 603), (899, 532), (208, 580)],
    }

screen loc_hamun_castle_tea_room():
    default locTag = "hamun_castle_tea_room"

    # exit to entrance
    use locBtn_basic(locTag, "hamun_castle_tea_room_to_entrance",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
