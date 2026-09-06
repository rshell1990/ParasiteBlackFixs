image hamun_dist_arena = "images/world_bgs/hamun_city/hamun_dist_arena.webp"

####################################################################################
# clickables:
image hamun_dist_arena_exit_south_t = "images/world_interact/hamun_city/ham_arena_dist_exit_south.webp"
image hamun_dist_arena_exit_south_h:
    "hamun_dist_arena_exit_south_t"
    matrixcolor MxMapHover()
# arena
image hamun_arena_gate_t = "images/world_interact/hamun_city/hamun_arena.webp"
image hamun_arena_gate_h:
    "hamun_arena_gate_t"
    matrixcolor MxMapHover()
####################################################################################

init python:
    WorldLocation("hamun_dist_arena", STR_LOC.HAMUN_DIST_ARENA, "hamun_dist_arena", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_dist_arena"]
    ###### clickables ######
    LocDef.withBtn("hamun_dist_arena_to_dist_merch_lord", BtnChangeLoc(STR_LOC.HAMUN_DIST_MERCH_LORD, "hamun_dist_merch_lord"))
    LocDef.withBtn("hamun_dist_arena_to_arena_exterior", BtnChangeLoc(STR_LOC.HAMUN_ARENA, "hamun_arena_ext"))
    ########################
    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    # vfx
    vfxLibLights["hamun_dist_arena_night"] = {
        "lightpost_small":[(13, 49), (113, 97), (234, 157), (1338, 157),
                        (1440, 118), (1544, 56), (1638, 15)],
        "lightpost_big":[(657, 345), (0.342, 0.319), (903, 339), (0.47, 0.314),
                        (732, 1001), (0.381, 0.927), (899, 1006), (0.468, 0.931)]}
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_dist_arena():
    default locTag = "hamun_dist_arena"
    use locBtn_sprite(locTag, "hamun_dist_arena_to_dist_merch_lord", 
        "hamun_dist_arena_exit_south_t",
        "hamun_dist_arena_exit_south_h",
        Transform(anchor = (0, 0), pos = (632, 865)), 
        key = config.keymap["nav_down"],
        )
    use locBtn_sprite(locTag, "hamun_dist_arena_to_arena_exterior", 
        "hamun_arena_gate_t",
        "hamun_arena_gate_h",
        Transform(anchor = (0, 0), pos = (0, 0)), 
        key = config.keymap["nav_up"],
        )
    

