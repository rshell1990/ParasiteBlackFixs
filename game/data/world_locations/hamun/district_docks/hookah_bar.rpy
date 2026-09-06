# main room
init python:
    WorldLocation("hamun_hookah_bar", STR_LOC.HAMUN_HOOKAH_BAR, "bg_hamun_hookah_bar", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_hookah_bar"]

    # clickables
    LocDef.withBtn("hamun_hookah_bar_to_docks", BtnChangeLoc(STR_LOC.HAMUN_DIST_DOCKS, "hamun_dist_docks")) 
    LocDef.withBtn("hamun_hookah_bar_to_room", BtnChangeLoc(STR_LOC.HAMUN_HOOKAH_BAR_ROOM, "hamun_hookah_bar_room")) 
    LocDef.withBtn("btn_hamun_hookah_bar_rania", BtnDisabled())
    LocDef.withBtn("btn_hamun_hookah_bar_garen", BtnDisabled())

    LocDef.withBtn("btn_hamun_hookah_bar_lady_tarbeck", BtnDisabled())
    LocDef.withBtn("btn_hamun_hookah_bar_drown_sorrows", BtnDisabled())

    # action sfx
    LocDef.withActionSFXs({"hamun_hookah_bar_to_docks": soundLib["tentFlap"],
                        "hamun_hookah_bar_to_room": soundLib["tentFlap"]})
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    # vfx "small huge big" are default lightposts
    vfxLibLights["hamun_hookah_bar_night"] = {
        "lightpost_huge":[(1499, 594)],
        "lightpost_big":[(1704, 552), (1510, 527), (1171, 527), (1122, 733),
                        (913, 798), (833, 694), (594, 729), (611, 512)],
        "lightpost_small":[(718, 491), (449, 493), (334, 484)]}
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_hookah_bar():
    default locTag = "hamun_hookah_bar"

    # exit outside
    use locBtn_basic(locTag, "hamun_hookah_bar_to_docks",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    # to room
    use locBtn_basic(locTag, "hamun_hookah_bar_to_room",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.432, 0.408)),
        key = config.keymap["nav_up"])

    use locBtn_Char(locTag, "btn_hamun_hookah_bar_rania",
        "rania", "rania",
        Transform(anchor = (0.5, 1.0), pos = (0.1, 0.9), zoom = 0.63))
    
    # for beast quest
    use locBtn_Char(locTag, "btn_hamun_hookah_bar_garen",
        "garen", "garen",
        Transform(anchor = (0.5, 1.0), pos = (0.85, 0.9), zoom = 0.63, xzoom = -1.0))
    
    # for beast quest
    use locBtn_Char(locTag, "btn_hamun_hookah_bar_lady_tarbeck",
        "lady_tarbeck", "lady_tarbeck",
        Transform(anchor = (0.5, 1.0), pos = (0.742, 0.923), zoom = 0.63, xzoom = -1.0))
    
    use locBtn_basic(locTag, "btn_hamun_hookah_bar_drown_sorrows",
        "images/gui/buttons_loc/sleep.webp",
        Transform(pos = (0.5, 0.5)))


# inn room
init python:
    WorldLocation("hamun_hookah_bar_room", STR_LOC.HAMUN_HOOKAH_BAR_ROOM, "bg_hamun_hookah_bar_room", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_hookah_bar_room"]

    LocDef.withBtn("hamun_hookah_bar_room_to_bar", BtnChangeLoc(STR_LOC.HAMUN_HOOKAH_BAR, "hamun_hookah_bar")) 
    LocDef.withBtn("btn_hamun_hookah_bar_bed", BtnJumpLabel(_("Bed"), "bed_choice_hamun_hookah_bar"))
    # handled via separate logicmodule CAUSE INIT LEVELS FIGHTING
    LocDef.withBtn("btn_hamun_hookah_bar_chest", BtnDisabled()) 

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    # vfx "small huge big" are default lightposts
    vfxLibLights["hamun_hookah_bar_room_night"] = {
        "lightpost_huge":[(1647, 252)],
        "lightpost_big":[(655, 482), (1849, 464), (951, 331)]}

# this is split because different OnX call for the adara dream quest
label bed_choice_hamun_hookah_bar:
    "My bed."
    menu:
        "Go to sleep.":
            if not IsInTimeFrame(TIME_DAWN, TIME_AFTERNOON):
                call ProcessLocEvent("PreSleepHamunHookahBar") from _call_ProcessLocEvent
                call shared_bed_sleep_logic from _call_shared_bed_sleep_logic_1
                call ProcessLocEvent("PostSleepHamunHookahBar") from _call_ProcessLocEvent_4
                $ LocFlush()
                with dissolve
            else:
                MC "(I am not tired enough to sleep right now.)"
                MC "({i}And I won't be until afternoon.{/i})"
        "On a second thought, not now.":
            pass
    $ LocEnterQ()

screen loc_hamun_hookah_bar_room():
    default locTag = "hamun_hookah_bar_room"

    # exit outside
    use locBtn_basic(locTag, "hamun_hookah_bar_room_to_bar",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
    use locBtn_basic(locTag, "btn_hamun_hookah_bar_bed",
        "images/gui/buttons_loc/sleep.webp",
        Transform(pos = (0.77, 0.53)))
    use locBtn_basic(locTag, "btn_hamun_hookah_bar_chest",
        "images/gui/buttons_loc/chest.webp",
        Transform(pos = (0.48, 0.46)))
