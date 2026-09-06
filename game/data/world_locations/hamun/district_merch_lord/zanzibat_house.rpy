init python:
    # this starts disabled all the way till the Beast quest
    @AppendToAllQuests
    class HouseLockZanzibatHouse(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_dist_merch_lord":
                btnMods["hamun_dist_merch_lord_to_zanzibat_house"] = BtnJumpLabel(STR_LOC.HAMUN_ZANZIBAT_HOUSE, "hamun_zanzibat_nobusiness")
            return LocButtonMod(directMods = btnMods)

label hamun_zanzibat_nobusiness:
    show cg_guard_hamun at cright_f with dissolve
    show mc at cleft with easeinleft
    GUARD "What business do you have with Lord Zanzibat?"
    menu:
        "None, really.":
            GUARD "Then leave."
            $ LocEnter()

init python:
    WorldLocation("hamun_zanzibat_house", STR_LOC.HAMUN_ZANZIBAT_HOUSE, "bg_hamun_zanzibat_house", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_zanzibat_house"]

    LocDef.CanWait = False

    # clickables
    LocDef.withBtn("hamun_zanzibat_house_to_dist_merch_lord", BtnChangeLoc(STR_LOC.HAMUN_DIST_MERCH_LORD, "hamun_dist_merch_lord"))
    LocDef.withBtn("hamun_zanzibat_house_talk_to_zanzibat", BtnDisabled())

    # action sfx
    LocDef.withActionSFXs({"hamun_zanzibat_house_to_dist_merch_lord": soundLib["tentFlap"]})

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    # vfx "small huge big" are default lightposts
    vfxLibLights["hamun_zanzibat_house_night"] = {
        "lightpost_huge":[(1218, 485), (706, 486)]}
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_zanzibat_house():
    default locTag = "hamun_zanzibat_house"

    # exit outside
    use locBtn_basic(locTag, "hamun_zanzibat_house_to_dist_merch_lord",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
    
    use locBtn_Char(locTag, "hamun_zanzibat_house_talk_to_zanzibat",
        "zanzibat", "zanzibat",
        Transform(anchor = (0.5, 1.0), pos = (0.59, 0.82), zoom = 0.27, xzoom = -1.0))
