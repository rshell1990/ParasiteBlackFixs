############################################################################################################
####### lord tarbek's estate, mainhall
init python:
    WorldLocation("hamun_tarbeck_mainhall", STR_LOC.HAMUN_TARBECK_MAINHALL, "bg_tarbeck_main_hall", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_mainhall"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_mainhall_to_dist_merch_lord",     BtnChangeLoc(STR_LOC.HAMUN_DIST_MERCH_LORD, "hamun_dist_merch_lord")) 
    LocDef.withBtn("hamun_tarbeck_mainhall_to_tarbeck_library",     BtnChangeLoc(STR_LOC.HAMUN_TARBECK_LIBRARY, "hamun_tarbeck_library")) 
    LocDef.withBtn("hamun_tarbeck_mainhall_to_tarbeck_ballroom",    BtnChangeLoc(STR_LOC.HAMUN_TARBECK_BALLROOM, "hamun_tarbeck_ballroom")) 
    LocDef.withBtn("hamun_tarbeck_mainhall_to_tarbeck_west_wing",   BtnChangeLoc(STR_LOC.HAMUN_TARBECK_WEST_WING, "hamun_tarbeck_west_wing")) 
    LocDef.withBtn("hamun_tarbeck_mainhall_to_tarbeck_east_wing",   BtnChangeLoc(STR_LOC.HAMUN_TARBECK_EAST_WING, "hamun_tarbeck_east_wing")) 
    LocDef.withBtn("hamun_tarbeck_mainhall_to_tarbeck_playhallway", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_PLAYHALLWAY, "hamun_tarbeck_playhallway")) 

    LocDef.withBtn("btn_hamun_tarbeck_mainhall_watcher", BtnDisabled()) 
    LocDef.withBtn("btn_hamun_tarbeck_mainhall_lady_tarbeck", BtnDisabled()) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_tarbeck_mainhall():
    default locTag = "hamun_tarbeck_mainhall"

    # exit outside
    use locBtn_basic(locTag, "hamun_tarbeck_mainhall_to_dist_merch_lord",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    # left-library
    use locBtn_basic(locTag, "hamun_tarbeck_mainhall_to_tarbeck_library",
        "images/gui/buttons_loc/arrow_l.webp",
        Transform(pos = (0.1, 0.6)),
        key = config.keymap["nav_left"])
    # right-ball room
    use locBtn_basic(locTag, "hamun_tarbeck_mainhall_to_tarbeck_ballroom",
        "images/gui/buttons_loc/arrow_r.webp",
        Transform(pos = (0.9, 0.6)),
        key = config.keymap["nav_right"])
    # up-stairs west wing
    use locBtn_basic(locTag, "hamun_tarbeck_mainhall_to_tarbeck_west_wing",
        "images/gui/buttons_loc/arrow_u.webp",
        Transform(pos = (0.32, 0.38)))
    # up-stairs east wing
    use locBtn_basic(locTag, "hamun_tarbeck_mainhall_to_tarbeck_east_wing",
        "images/gui/buttons_loc/arrow_u.webp",
        Transform(pos = (0.7, 0.37)))
    # forward to play hallway
    use locBtn_basic(locTag, "hamun_tarbeck_mainhall_to_tarbeck_playhallway",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.54, 0.57)),
        key = config.keymap["nav_up"]
        )
    # watcher
    use locBtn_Char(locTag, "btn_hamun_tarbeck_mainhall_watcher",
        "cg_tarbeck_watcher", "cg_tarbeck_watcher",
        Transform(anchor = (0.5, 1.0), pos = (0.6, 0.86), xzoom = -1.0, zoom = 0.24))
    # lady tarbeck
    use locBtn_Char(locTag, "btn_hamun_tarbeck_mainhall_lady_tarbeck",
        "lady_tarbeck", "lady_tarbeck",
        Transform(anchor = (0.5, 1.0), pos = (0.6, 0.86), xzoom = -1.0, zoom = 0.24))

############################################################################################################
####### lord tarbek's estate, library
init python:
    WorldLocation("hamun_tarbeck_library", STR_LOC.HAMUN_TARBECK_LIBRARY, "bg_tarbeck_library", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_library"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_library_to_tarbeck_mainhall", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_MAINHALL, "hamun_tarbeck_mainhall")) 
    LocDef.withBtn("btn_hamun_tarbeck_library_lady_tarbeck",    BtnDisabled()) 
    LocDef.withBtn("hamun_tarbeck_library_to_tarbeck_dining",   BtnChangeLoc(STR_LOC.HAMUN_TARBECK_DINING, "hamun_tarbeck_dining")) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)
    # vfx
    vfxLibLights["hamun_tarbeck_library_night"] = {
        "lightpost_big":[(457, 381), (237, 506), (87, 479), (133, 332),
            (1627, 501), (1542, 501), (1333, 377),
            (829, 345)],
        "lightpost_small":[(671, 654), (797, 655), (708, 609), (731, 610), (750, 496), (1137, 656), (1053, 677), (1008, 656), (1073, 610), (1030, 517), (1057, 495)],
    }

screen loc_hamun_tarbeck_library():
    default locTag = "hamun_tarbeck_library"

    # back to mh
    use locBtn_basic(locTag, "hamun_tarbeck_library_to_tarbeck_mainhall",
        "images/gui/buttons_loc/arrow_d.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
    # to dining
    use locBtn_basic(locTag, "hamun_tarbeck_library_to_tarbeck_dining",
        "images/gui/buttons_loc/arrow_r.webp",
        Transform(pos = (0.92, 0.56)),
        key = config.keymap["nav_right"])
    # lady tarbeck
    use locBtn_Char(locTag, "btn_hamun_tarbeck_library_lady_tarbeck",
        "lady_tarbeck", "lady_tarbeck",
        Transform(anchor = (0.5, 1.0), pos = (0.29, 0.74), xzoom = 1.0, zoom = 0.35))
############################################################################################################
####### lord tarbek's estate, playhallway
init python:
    WorldLocation("hamun_tarbeck_playhallway", STR_LOC.HAMUN_TARBECK_PLAYHALLWAY, "bg_tarbeck_playroom_hallway", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_playhallway"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_playhallway_to_tarbeck_mainhall", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_MAINHALL, "hamun_tarbeck_mainhall")) 
    
    LocDef.withBtn("hamun_tarbeck_playhallway_to_tarbeck_room_maidmaster",  BtnChangeLoc(STR_LOC.HAMUN_TARBECK_ROOM_MAIDMASTER, "hamun_tarbeck_room_maidmaster")) 
    LocDef.withBtn("hamun_tarbeck_playhallway_to_tarbeck_room_temptations", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_ROOM_TEMPTATIONS,"hamun_tarbeck_room_temptations")) 
    LocDef.withBtn("hamun_tarbeck_playhallway_to_tarbeck_room_mirrors",      BtnChangeLoc(STR_LOC.HAMUN_TARBECK_ROOM_MIRRORS,    "hamun_tarbeck_room_mirrors")) 
    LocDef.withBtn("hamun_tarbeck_playhallway_to_tarbeck_room_femdom",      BtnChangeLoc(STR_LOC.HAMUN_TARBECK_ROOM_FEMDOM,     "hamun_tarbeck_room_femdom")) 
    LocDef.withBtn("hamun_tarbeck_playhallway_to_tarbeck_room_orgy",        BtnChangeLoc(STR_LOC.HAMUN_TARBECK_ROOM_ORGY,       "hamun_tarbeck_room_orgy")) 
    LocDef.withBtn("hamun_tarbeck_playhallway_to_tarbeck_room_tentacle",    BtnChangeLoc(STR_LOC.HAMUN_TARBECK_ROOM_TENTACLE,   "hamun_tarbeck_room_tentacle")) 

    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    # vfx
    vfxLibLights["hamun_tarbeck_playhallway_night"] = {
        "lightpost_big_indigo":[(921, 238), (950, 230), (982, 245), (957, 52), (908, 52), (997, 51), (1846, 283), (70, 280), (521, 421), (1386, 419)],
        "lightpost_small_indigo":[(671, 463), (746, 481), (1150, 482), (1228, 466)],
    }


screen loc_hamun_tarbeck_playhallway():
    default locTag = "hamun_tarbeck_playhallway"

    # back to mh
    use locBtn_basic(locTag, "hamun_tarbeck_playhallway_to_tarbeck_mainhall",
        "images/gui/buttons_loc/arrow_d.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    use locBtn_basic(locTag, "hamun_tarbeck_playhallway_to_tarbeck_room_maidmaster",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.168, 0.52)),)
    use locBtn_basic(locTag, "hamun_tarbeck_playhallway_to_tarbeck_room_temptations",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.312, 0.51)),)
    use locBtn_basic(locTag, "hamun_tarbeck_playhallway_to_tarbeck_room_mirrors",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.382, 0.5)),)
    use locBtn_basic(locTag, "hamun_tarbeck_playhallway_to_tarbeck_room_femdom",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.613, 0.5)),)
    use locBtn_basic(locTag, "hamun_tarbeck_playhallway_to_tarbeck_room_orgy",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.69, 0.51)),)
    use locBtn_basic(locTag, "hamun_tarbeck_playhallway_to_tarbeck_room_tentacle",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.833, 0.52)),)
############################################################################################################
####### lord tarbek's estate, ball room
init python:
    WorldLocation("hamun_tarbeck_ballroom", STR_LOC.HAMUN_TARBECK_BALLROOM, "bg_tarbeck_ballroom", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_ballroom"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_ballroom_to_tarbeck_mainhall",    BtnChangeLoc(STR_LOC.HAMUN_TARBECK_MAINHALL, "hamun_tarbeck_mainhall")) 
    LocDef.withBtn("hamun_tarbeck_ballroom_to_tarbeck_garden_main", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_GARDEN, "hamun_tarbeck_garden_main")) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)
    # vfx
    vfxLibLights["hamun_tarbeck_ballroom_night"] = {
        "lightpost_big":[(1381, 168), (1310, 93), (1230, 101), (1191, 192), (1054, 329), (1015, 279), (909, 319), (935, 271), (1511, 508), (1280, 521), (1129, 527), (931, 569), (753, 571), (355, 514), (312, 503), (223, 475)],
    }



screen loc_hamun_tarbeck_ballroom():
    default locTag = "hamun_tarbeck_ballroom"

    # back to mh
    use locBtn_basic(locTag, "hamun_tarbeck_ballroom_to_tarbeck_mainhall",
        "images/gui/buttons_loc/arrow_d.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
    # to gardens
    use locBtn_basic(locTag, "hamun_tarbeck_ballroom_to_tarbeck_garden_main",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.3, 0.5)),
        key = config.keymap["nav_up"])
############################################################################################################
####### lord tarbek's estate, garden
init python:
    WorldLocation("hamun_tarbeck_garden_main", STR_LOC.HAMUN_TARBECK_GARDEN, "bg_tarbeck_garden_main", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_garden_main"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_garden_main_to_tarbeck_ballroom",     BtnChangeLoc(STR_LOC.HAMUN_TARBECK_BALLROOM, "hamun_tarbeck_ballroom")) 
    LocDef.withBtn("hamun_tarbeck_garden_main_to_tarbeck_garden_east",  BtnChangeLoc(STR_LOC.HAMUN_TARBECK_GARDEN_EAST, "hamun_tarbeck_garden_east")) 
    LocDef.withBtn("btn_hamun_tarbeck_garden_sypha", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    # amb
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_tarbeck_garden_main():
    default locTag = "hamun_tarbeck_garden_main"

    # back to ballroom
    use locBtn_basic(locTag, "hamun_tarbeck_garden_main_to_tarbeck_ballroom",
        "images/gui/buttons_loc/arrow_u.webp",
        Transform(pos = (0.5, 0.53)),
        key = config.keymap["nav_up"])
    # to eastern garden
    use locBtn_basic(locTag, "hamun_tarbeck_garden_main_to_tarbeck_garden_east",
        "images/gui/buttons_loc/arrow_r.webp",
        Transform(pos = (0.8, 0.54)),
        key = config.keymap["nav_right"])
    # sypha    
    use locBtn_Char(locTag, "btn_hamun_tarbeck_garden_sypha",
        "sypha", "sypha",
        Transform(anchor = (0.5, 1.0), pos = (0.66, 0.81), xzoom = -1.0, zoom = 0.27))
############################################################################################################
####### lord tarbek's estate, garden, eastern part
init python:
    WorldLocation("hamun_tarbeck_garden_east", STR_LOC.HAMUN_TARBECK_GARDEN_EAST, "bg_tarbeck_garden_east", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_garden_east"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_garden_east_to_tarbeck_garden_main", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_GARDEN, "hamun_tarbeck_garden_main")) 
    LocDef.withBtn("btn_hamun_tarbeck_garden_east_ingrid", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    # amb
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_tarbeck_garden_east():
    default locTag = "hamun_tarbeck_garden_east"

    # back to ballroom
    use locBtn_basic(locTag, "hamun_tarbeck_garden_east_to_tarbeck_garden_main",
        "images/gui/buttons_loc/arrow_d.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
    # ingrid
    use locBtn_Char(locTag, "btn_hamun_tarbeck_garden_east_ingrid",
        "ingrid", "ingrid",
        Transform(anchor = (0.5, 1.0), pos = (0.76, 0.80), xzoom = -1.0, zoom = 0.23))

############################################################################################################
####### lord tarbek's estate, west wing
init python:
    WorldLocation("hamun_tarbeck_west_wing", STR_LOC.HAMUN_TARBECK_WEST_WING, "bg_tarbeck_west_wing", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_west_wing"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_west_wing_to_tarbeck_mainhall", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_MAINHALL, "hamun_tarbeck_mainhall")) 
    LocDef.withBtn("hamun_tarbeck_west_wing_to_tarbeck_quarters_lord", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_QUARTERS_LORD, "hamun_tarbeck_quarters_lord")) 
    LocDef.withBtn("hamun_tarbeck_west_wing_to_tarbeck_treasure", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_TREASURY, "hamun_tarbeck_treasury")) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    LocDef.SetDayNightMatrixClass(None)

screen loc_hamun_tarbeck_west_wing():
    default locTag = "hamun_tarbeck_west_wing"

    # back to main
    use locBtn_basic(locTag, "hamun_tarbeck_west_wing_to_tarbeck_mainhall",
        "images/gui/buttons_loc/arrow_d.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
    # to lord quarters (left)
    use locBtn_basic(locTag, "hamun_tarbeck_west_wing_to_tarbeck_quarters_lord",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.2, 0.5)),
        key = config.keymap["nav_right"])
    # to treasurey (top)
    use locBtn_basic(locTag, "hamun_tarbeck_west_wing_to_tarbeck_treasure",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.57)),
        key = config.keymap["nav_up"])

    
############################################################################################################
####### lord tarbek's estate, east wing
init python:
    WorldLocation("hamun_tarbeck_east_wing", STR_LOC.HAMUN_TARBECK_EAST_WING, "bg_tarbeck_east_wing", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_east_wing"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_east_wing_to_tarbeck_mainhall", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_MAINHALL, "hamun_tarbeck_mainhall")) 
    LocDef.withBtn("hamun_tarbeck_east_wing_to_tarbeck_quarters_lady", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_QUARTERS_LADY, "hamun_tarbeck_quarters_lady")) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    LocDef.SetDayNightMatrixClass(None)

screen loc_hamun_tarbeck_east_wing():
    default locTag = "hamun_tarbeck_east_wing"

    # back to mainhall
    use locBtn_basic(locTag, "hamun_tarbeck_east_wing_to_tarbeck_mainhall",
        "images/gui/buttons_loc/arrow_d.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
    # to lady q (right)
    use locBtn_basic(locTag, "hamun_tarbeck_east_wing_to_tarbeck_quarters_lady",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.8, 0.5)),
        key = config.keymap["nav_right"])

    
############################################################################################################
####### lord tarbek's estate, lord quarters
init python:
    WorldLocation("hamun_tarbeck_quarters_lord", STR_LOC.HAMUN_TARBECK_QUARTERS_LORD, "bg_tarbeck_lord_quarters", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_quarters_lord"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_quarters_lord_to_tarbeck_west_wing", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_WEST_WING, "hamun_tarbeck_west_wing")) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)
    # vfx
    vfxLibLights["hamun_tarbeck_quarters_lord_night"] = {
        "lightpost_big":[(1545, 680), (1021, 113), (973, 93), (910, 82), (852, 93), (801, 122)],
    }

screen loc_hamun_tarbeck_quarters_lord():
    default locTag = "hamun_tarbeck_quarters_lord"

    # back to west wing
    use locBtn_basic(locTag, "hamun_tarbeck_quarters_lord_to_tarbeck_west_wing",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.74, 0.49)),
        key = config.keymap["nav_right"])

    
############################################################################################################
####### lord tarbek's estate, treasury
init python:
    WorldLocation("hamun_tarbeck_treasury", STR_LOC.HAMUN_TARBECK_TREASURY, "bg_tarbeck_treasury", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_treasury"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_treasury_to_west_wing", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_WEST_WING, "hamun_tarbeck_west_wing")) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    # vfx
    vfxLibLights["hamun_tarbeck_treasury_night"] = {
        "lightpost_big":[(873, 82), (915, 63), (978, 67), (1015, 88)],
    }


screen loc_hamun_tarbeck_treasury():
    default locTag = "hamun_tarbeck_treasury"

    # back to west wing
    use locBtn_basic(locTag, "hamun_tarbeck_treasury_to_west_wing",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.49, 0.44)),
        key = config.keymap["nav_up"])

############################################################################################################
####### lord tarbek's estate, lady quarters
init python:
    WorldLocation("hamun_tarbeck_quarters_lady", STR_LOC.HAMUN_TARBECK_QUARTERS_LADY, "bg_tarbeck_lady_quarters", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_quarters_lady"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_quarters_lady_to_tarbeck_east_wing", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_EAST_WING, "hamun_tarbeck_east_wing")) 
    LocDef.withBtn("btn_hamun_tarbeck_quarters_lady_lady_tarbeck", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)
    # vfx
    vfxLibLights["hamun_tarbeck_quarters_lady_night"] = {
        "lightpost_small":[(1635, 131), (1558, 157), (1500, 168), (1464, 183), (1329, 319), (1324, 234), (1220, 213), (1132, 193), (1036, 166), (919, 135), (818, 106), (718, 83), (613, 51), (490, 20)],
    }

screen loc_hamun_tarbeck_quarters_lady():
    default locTag = "hamun_tarbeck_quarters_lady"

    # back to west wing
    use locBtn_basic(locTag, "hamun_tarbeck_quarters_lady_to_tarbeck_east_wing",
        "images/gui/buttons_loc/arrow_d.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
    use locBtn_Char(locTag, "btn_hamun_tarbeck_quarters_lady_lady_tarbeck",
        "lady_tarbeck", "lady_tarbeck",
        Transform(anchor = (0.5, 1.0), pos = (0.25, 0.8), zoom = 0.65))
############################################################################################################
####### lord tarbek's estate, room maid-masters
init python:
    WorldLocation("hamun_tarbeck_room_maidmaster", STR_LOC.HAMUN_TARBECK_ROOM_MAIDMASTER, "bg_tarbeck_master_maid_room", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_room_maidmaster"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_room_maidmaster_to_tarbeck_playhallway", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_PLAYHALLWAY, "hamun_tarbeck_playhallway")) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

screen loc_hamun_tarbeck_room_maidmaster():
    default locTag = "hamun_tarbeck_room_maidmaster"

    # back to hall
    use locBtn_basic(locTag, "hamun_tarbeck_room_maidmaster_to_tarbeck_playhallway",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
############################################################################################################
####### lord tarbek's estate, room temptations
init python:
    WorldLocation("hamun_tarbeck_room_temptations", STR_LOC.HAMUN_TARBECK_ROOM_TEMPTATIONS, "bg_tarbeck_tempt_room", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_room_temptations"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_room_temptations_to_tarbeck_playhallway", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_PLAYHALLWAY, "hamun_tarbeck_playhallway")) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    LocDef.SetDayNightMatrixClass(None)

screen loc_hamun_tarbeck_room_temptations():
    default locTag = "hamun_tarbeck_room_temptations"

    # back to hall
    use locBtn_basic(locTag, "hamun_tarbeck_room_temptations_to_tarbeck_playhallway",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
############################################################################################################
####### lord tarbek's estate, room mirros
init python:
    WorldLocation("hamun_tarbeck_room_mirrors", STR_LOC.HAMUN_TARBECK_ROOM_MIRRORS, "bg_tarbeck_mirrors", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_room_mirrors"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_room_mirrors_to_tarbeck_playhallway", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_PLAYHALLWAY, "hamun_tarbeck_playhallway")) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    LocDef.SetDayNightMatrixClass(None)

screen loc_hamun_tarbeck_room_mirrors():
    default locTag = "hamun_tarbeck_room_mirrors"

    # back to hall
    use locBtn_basic(locTag, "hamun_tarbeck_room_mirrors_to_tarbeck_playhallway",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
############################################################################################################
####### lord tarbek's estate, room femdom
init python:
    WorldLocation("hamun_tarbeck_room_femdom", STR_LOC.HAMUN_TARBECK_ROOM_FEMDOM, "bg_tarbeck_femdom_dungeon", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_room_femdom"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_room_femdom_to_tarbeck_playhallway", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_PLAYHALLWAY, "hamun_tarbeck_playhallway")) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

screen loc_hamun_tarbeck_room_femdom():
    default locTag = "hamun_tarbeck_room_femdom"

    # back to hall
    use locBtn_basic(locTag, "hamun_tarbeck_room_femdom_to_tarbeck_playhallway",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
############################################################################################################
####### lord tarbek's estate, room orgy
init python:
    WorldLocation("hamun_tarbeck_room_orgy", STR_LOC.HAMUN_TARBECK_ROOM_ORGY, "bg_tarbeck_orgy_room", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_room_orgy"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_room_orgy_to_tarbeck_playhallway", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_PLAYHALLWAY, "hamun_tarbeck_playhallway")) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

screen loc_hamun_tarbeck_room_orgy():
    default locTag = "hamun_tarbeck_room_orgy"

    # back to hall
    use locBtn_basic(locTag, "hamun_tarbeck_room_orgy_to_tarbeck_playhallway",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
############################################################################################################
####### lord tarbek's estate, room tentacle
init python:
    WorldLocation("hamun_tarbeck_room_tentacle", STR_LOC.HAMUN_TARBECK_ROOM_TENTACLE, "bg_tarbeck_tent_room_empty", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_room_tentacle"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_room_tentacle_to_tarbeck_playhallway", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_PLAYHALLWAY, "hamun_tarbeck_playhallway")) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")

screen loc_hamun_tarbeck_room_tentacle():
    default locTag = "hamun_tarbeck_room_tentacle"

    # back to hall
    use locBtn_basic(locTag, "hamun_tarbeck_room_tentacle_to_tarbeck_playhallway",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

############################################################################################################
####### lord tarbek's estate, dining room
init python:
    WorldLocation("hamun_tarbeck_dining", STR_LOC.HAMUN_TARBECK_DINING, "bg_tarbeck_dining", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_tarbeck_dining"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_tarbeck_dining_to_library", BtnChangeLoc(STR_LOC.HAMUN_TARBECK_LIBRARY, "hamun_tarbeck_library")) 
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    # vfx
    vfxLibLights["hamun_tarbeck_dining_night"] = {
        "lightpost_big":[
            (799, 515), (842, 513), (823, 473), (1109, 511), 
            (1088, 470), (1066, 509), (1054, 537), (1024, 535), 
            (1039, 510), (1003, 541), (923, 542), (894, 538), 
            (866, 541), (883, 512)
        ],
    }

screen loc_hamun_tarbeck_dining():
    default locTag = "hamun_tarbeck_dining"

    # back to library
    use locBtn_basic(locTag, "hamun_tarbeck_dining_to_library",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])