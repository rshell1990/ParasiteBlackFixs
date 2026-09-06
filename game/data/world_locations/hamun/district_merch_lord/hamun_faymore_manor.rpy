label hamun_faymore_manor_doors_blocked:
    show cg_guard_hamun at cright_f with dissolve
    show mc at cleft with easeinleft
    GUARD "The Faymore women have barred you from entry."
    GUARD "They want nothing more to do with you."
    GUARD "Leave."
    $ LocEnter()

label hamun_faymore_manor_doors:
    show cg_guard_hamun at cright_f with dissolve
    show mc at cleft with easeinleft
    GUARD "Halt! Who goes there?"
    GUARD "What business do you have with the Faymore family?"
    call processDialogue("faymore_guard_root") from _call_processDialogue_83
    $ LocEnter()

label hamun_faymore_manor_can_come_in:    
    GUARD "Not unless the Lady Faymores have invited you in."
    GUARD "Given you are asking, I'm going to say you don't."
    $ LocEnter()

label hamun_faymore_manor_leave:
    GUARD "Then leave."
    $ LocEnter()

init python:
    # this is enabled by dreamhouse quest
    # also handles inner rooms
    @AppendToAllQuests
    class HouseLockFaymoreManor(LogicModule):
        def __init__(self):
            super().__init__()
            self.UnlockedChanyAnyaBedroom = False
            self.UnlockedSerafinaRoom = False

        def locationMod(self):
            btnMods = {}
            # prog 0 is "can i come in"
            # prog 1 is you can just come in
            # prog 2 is you cant come in (due to dreamhouse outcome)
            if GetLocID() == "hamun_dist_merch_lord":
                if QstGetProgress(HouseLockFaymoreManor) == 0:
                    btnMods["hamun_dist_merch_lord_to_faymore_manor"] = BtnJumpLabel(STR_LOC.FAYMORE_MANOR, "hamun_faymore_manor_doors")
                elif QstGetProgress(HouseLockFaymoreManor) == 2:
                    btnMods["hamun_dist_merch_lord_to_faymore_manor"] = BtnJumpLabel(STR_LOC.FAYMORE_MANOR, "hamun_faymore_manor_doors_blocked")
                else:
                    btnMods["hamun_dist_merch_lord_to_faymore_manor"] = BtnChangeLoc(STR_LOC.FAYMORE_MANOR, "hamun_faymore_manor")
            elif GetLocID() == "hamun_faymore_manor":
                if self.UnlockedChanyAnyaBedroom:
                    btnMods["hamun_faymore_manor_to_chanyianya_bedroom"] = BtnChangeLoc(STR_LOC.FAYMORE_MANOR_CHANYI_ANYA_ROOM, "hamun_faymore_manor_chanyianya_bedroom")
                if self.UnlockedSerafinaRoom:
                    btnMods["hamun_faymore_manor_to_serafina_room"] = BtnChangeLoc(STR_LOC.FAYMORE_MANOR_SERAFINA_ROOM, "hamun_faymore_manor_serafina_room")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("faymore_guard_root", DNode(_("Can I come in?"), "hamun_faymore_manor_can_come_in"))
            yield ("faymore_guard_root", DNode(_("None, really."), "hamun_faymore_manor_leave"))

    WorldLocation("hamun_faymore_manor", STR_LOC.FAYMORE_MANOR, "bg_faymore_manor_mainhall", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_faymore_manor"]
    LocDef.CanWait = False

    # clickables
    LocDef.withBtn("hamun_faymore_manor_to_dist_merch_lord", BtnChangeLoc(STR_LOC.HAMUN_DIST_MERCH_LORD, "hamun_dist_merch_lord")) 

    LocDef.withBtn("hamun_faymore_manor_to_chanyianya_bedroom", BtnDisabled())
    LocDef.withBtn("hamun_faymore_manor_to_serafina_room", BtnDisabled())

    LocDef.withBtn("hamun_faymore_manor_talk_anya", BtnDisabled()) 
    LocDef.withBtn("hamun_faymore_manor_talk_chanyi", BtnDisabled())

    # action sfx
    LocDef.withActionSFXs({"hamun_faymore_manor_to_dist_merch_lord": soundLib["tentFlap"]})

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    # vfx "small huge big" are default lightposts
    vfxLibLights["hamun_faymore_manor"] = {
        "lightpost_big":[
            (59, 685),  (654, 682), (818, 703), (1103, 705), (1783, 394),
            (1605, 399), (1292, 389), (1066, 433), (859, 430), (800, 382),
            (376, 397), (324, 391), (158, 391), (72, 369)
        ],
    }
    vfxLibLights["hamun_faymore_manor_night"] = vfxLibLights["hamun_faymore_manor"]

    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_faymore_manor():
    default locTag = "hamun_faymore_manor"

    # chany anya bedroom
    use locBtn_basic(locTag, "hamun_faymore_manor_to_chanyianya_bedroom",
        "images/gui/buttons_loc/arrow_u.webp",
        Transform(pos = (0.848, 0.569)),
        key = config.keymap["nav_right"])
    # chany anya bedroom
    use locBtn_basic(locTag, "hamun_faymore_manor_to_serafina_room",
        "images/gui/buttons_loc/arrow_u.webp",
        Transform(pos = (0.15, 0.569)),
        key = config.keymap["nav_left"])

    # chars talk
    use locBtn_Char(locTag, "hamun_faymore_manor_talk_chanyi",
        "chanyi", "chanyi",
        Transform(anchor = (0.5, 1.0), pos = (0.3, 0.9), zoom = 0.35))
    use locBtn_Char(locTag, "hamun_faymore_manor_talk_anya",
        "anya", "anya",
        Transform(anchor = (0.5, 1.0), pos = (0.7, 0.9), zoom = 0.35))

    # exit outside
    use locBtn_basic(locTag, "hamun_faymore_manor_to_dist_merch_lord",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])


################################################################
init python:
    WorldLocation("hamun_faymore_manor_chanyianya_bedroom", STR_LOC.FAYMORE_MANOR_CHANYI_ANYA_ROOM, "bg_faymore_manor_chanyianya_bedroom", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_faymore_manor_chanyianya_bedroom"]
    LocDef.CanWait = False

    # clickables
    LocDef.withBtn("hamun_faymore_manor_chanyianya_bedroom_to_mainhall", BtnChangeLoc(STR_LOC.FAYMORE_MANOR, "hamun_faymore_manor")) 

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    
    # vfx 
    vfxLibLights["hamun_faymore_manor_chanyianya_bedroom"] = {
        "lightpost_big":[(622, 670), (668, 587), (699, 626), (748, 152), 
            (804, 155), (867, 154), (1244, 699), (1336, 560)
        ],
    }
    vfxLibLights["hamun_faymore_manor_chanyianya_bedroom_night"] = vfxLibLights["hamun_faymore_manor_chanyianya_bedroom"]

    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_faymore_manor_chanyianya_bedroom():
    default locTag = "hamun_faymore_manor_chanyianya_bedroom"

    # exit outside
    use locBtn_basic(locTag, "hamun_faymore_manor_chanyianya_bedroom_to_mainhall",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.095, 0.562)),
        key = config.keymap["nav_left"])

################################################################

init python:
    WorldLocation("hamun_faymore_manor_serafina_room", STR_LOC.FAYMORE_MANOR_SERAFINA_ROOM, "bg_faymore_serafina_bedroom", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_faymore_manor_serafina_room"]
    LocDef.CanWait = False

    # clickables
    LocDef.withBtn("hamun_faymore_manor_serafina_room_to_mainhall", BtnChangeLoc(STR_LOC.FAYMORE_MANOR, "hamun_faymore_manor")) 
    LocDef.withBtn("hamun_faymore_manor_talk_serafina", BtnDisabled())
    LocDef.withBtn("hamun_faymore_manor_talk_virgo", BtnDisabled())

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    # vfx 
    vfxLibLights["hamun_faymore_manor_serafina_room"] = {
        "lightpost_huge":[(283, 696)],
        "lightpost_small":[(747, 545), (768, 538), (794, 544), (1051, 75), (1129, 64), (1238, 65), (1320, 75), (1304, 95)],
    }

    


    vfxLibLights["hamun_faymore_manor_serafina_room_night"] = vfxLibLights["hamun_faymore_manor_serafina_room"]
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_faymore_manor_serafina_room():
    default locTag = "hamun_faymore_manor_serafina_room"

    # exit outside
    use locBtn_basic(locTag, "hamun_faymore_manor_serafina_room_to_mainhall",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    # serafina
    use locBtn_Char(locTag, "hamun_faymore_manor_talk_serafina",
        "serafina", "serafina",
        Transform(anchor = (0.5, 1.0), pos = (0.34, 0.75), zoom = 0.30))
    # virgo
    use locBtn_Char(locTag, "hamun_faymore_manor_talk_virgo",
        "cg_virgo", "cg_virgo",
        Transform(anchor = (0.5, 1.0), pos = (0.8, 0.9), zoom = 0.35, xzoom = -1.0))
