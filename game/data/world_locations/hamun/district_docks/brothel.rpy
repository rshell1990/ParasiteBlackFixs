init python:
    @AppendToAllQuests
    class HouseLockHamunBrothel(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_dist_docks":
                if IsDaytime():
                    btnMods["hamun_docks_to_brothel"] = BtnJumpLabel(STR_LOC.HAMUN_BROTHEL, "HouseLockLines_JustClosed")
                else:
                    btnMods["hamun_docks_to_brothel"] = BtnChangeLoc(STR_LOC.HAMUN_BROTHEL, "hamun_brothel")
            return LocButtonMod(directMods = btnMods)

    WorldLocation("hamun_brothel", STR_LOC.HAMUN_BROTHEL, "bg_hamun_brothel", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_brothel"]
    LocDef.CanWait = False
    # clickables ######
    LocDef.withBtn("hamun_brothel_to_docks",   BtnChangeLoc(STR_LOC.HAMUN_DIST_DOCKS,   "hamun_dist_docks")) 
    LocDef.withBtn("hamun_brothel_to_room",    BtnDisabled())
    LocDef.withBtn("btn_hamun_brothel_esme_talk",    BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    # action sfx
    LocDef.withActionSFXs({"hamun_brothel_to_docks": soundLib["tentFlap"], 
                        "hamun_brothel_to_room": soundLib["woodenDoor"]})
    # vfx "small huge big" are default lightposts
    vfxLibLights["hamun_brothel_night"] = {
        "lightpost_huge":[(1442, 26), (445, 25)],
        "lightpost_big":[(1614, 354), (1466, 363), (1546, 538), (1371, 562),
                        (1318, 594), (1100, 602), (966, 584), (909, 578),
                        (567, 584), (380, 590), (464, 299), (233, 257)]}
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_brothel():
    default locTag = "hamun_brothel"

    # exit outside
    use locBtn_basic(locTag, "hamun_brothel_to_docks",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    # to brothel room
    use locBtn_basic(locTag, "hamun_brothel_to_room",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.166, 0.256)),
        key = config.keymap["nav_left"])

    
    use locBtn_Char(locTag, "btn_hamun_brothel_esme_talk",
        "esme", "esme",
        Transform(anchor = (0.5, 1.0), pos = (0.88, 0.8), zoom = 0.65, xzoom = -1.0))

######################################################
######################################################
######################################################
init python:
    @AppendToAllQuests
    class HouseLockHamunBrothelRoom(LogicModule):
        def locationMod(self):
            btnMods = {}
            ### currently just hidden
            # BtnChangeLoc(STR_LOC.HAMUN_BROTHEL_ROOM, "hamun_brothel_room"))
            return LocButtonMod(directMods = btnMods)

    WorldLocation("hamun_brothel_room", STR_LOC.HAMUN_BROTHEL_ROOM, "bg_hamun_brothel_room", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_brothel_room"]

    # clickables
    LocDef.withBtn("hamun_brothel_room_to_brothel", BtnChangeLoc(STR_LOC.HAMUN_BROTHEL, "hamun_brothel")) 

    # action sfx
    LocDef.withActionSFXs({"hamun_brothel_room_to_brothel": soundLib["woodenDoor"]})

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    # vfx "small huge big" are default lightposts
    vfxLibLights["hamun_brothel_room_night"] = {
        "lightpost_huge":[(1416, 25)]}
    vfxLibLights["hamun_brothel_room"] = {
        "lightpost_huge":[(1416, 25)]}

screen loc_hamun_brothel_room():
    default locTag = "hamun_brothel_room"

    # exit to brothel
    use locBtn_basic(locTag, "hamun_brothel_room_to_brothel",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])