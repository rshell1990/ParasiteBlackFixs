init python:
    # this is enabled by starting Tarbecks quest
    @AppendToAllQuests
    class HouseLockTarbeckHouse(LogicModule):
        # prog 0, 1 cant enter bc guard
        # prog 2 is mainhall-lib-dining
        # prog 3 is mainhall-lib-dining PLUS east wing
        # prog 4 is mainhall-lib-dining-eastwing PLUS garden
        # prog 5 is mainhall-lib-dining-eastwing-garden PLUS west wing MINUS treasury
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_dist_merch_lord":
                btnMods["hamun_dist_merch_lord_to_tarbeck_mainhall"] = BtnJumpLabel(STR_LOC.HAMUN_TARBECK_ESTATE, "hamun_tarbeck_entry")
            # disables room buttons except the allowed ones
            #elif GetLocID() == "hamun_tarbeck_mainhall":
            if self.progress == 2:
                btnMods["hamun_tarbeck_mainhall_to_tarbeck_ballroom"]    = BtnDisabled()
                btnMods["hamun_tarbeck_mainhall_to_tarbeck_west_wing"]   = BtnDisabled()
                btnMods["hamun_tarbeck_mainhall_to_tarbeck_east_wing"]   = BtnDisabled()
                btnMods["hamun_tarbeck_mainhall_to_tarbeck_playhallway"] = BtnDisabled()
            if self.progress == 3:
                btnMods["hamun_tarbeck_mainhall_to_tarbeck_ballroom"]    = BtnDisabled()
                btnMods["hamun_tarbeck_mainhall_to_tarbeck_west_wing"]   = BtnDisabled()
                btnMods["hamun_tarbeck_mainhall_to_tarbeck_playhallway"] = BtnDisabled()
            if self.progress == 4:
                btnMods["hamun_tarbeck_mainhall_to_tarbeck_west_wing"]   = BtnDisabled()
                btnMods["hamun_tarbeck_mainhall_to_tarbeck_playhallway"] = BtnDisabled()
            if self.progress == 5:
                btnMods["hamun_tarbeck_mainhall_to_tarbeck_playhallway"] = BtnDisabled()
                btnMods["hamun_tarbeck_west_wing_to_tarbeck_treasure"] = BtnDisabled()

            return LocButtonMod(directMods = btnMods)

label hamun_tarbeck_entry:
    if QstGetProgress(HouseLockTarbeckHouse) in [0, 1]:
        show cg_guard_hamun at cright_f with dissolve
        show mc at cleft with easeinleft
        GUARD "What business do you have with Lord Tarbeck?"
        menu:
            "I have no business.":
                GUARD "Then leave."
                $ LocEnter()               
    elif QstGetProgress(HouseLockTarbeckHouse) >= 2:
        show cg_guard_hamun at cright_f with dissolve
        show mc at cleft with easeinleft
        hide mc with easeoutright
        scene black with dissolve
        $ LocSet("hamun_tarbeck_mainhall")
        $ LocEnter()

image hamun_dist_merch_lord = "images/world_bgs/hamun_city/hamun_dist_merch_lord.webp"

####################################################################################
# clickables:
image hamun_dist_merch_lord_exit_south_t = "images/world_interact/hamun_city/ham_merch_exit_south.webp"
image hamun_dist_merch_lord_exit_south_h:
    "hamun_dist_merch_lord_exit_south_t"
    matrixcolor MxMapHover()

image hamun_dist_merch_lord_exit_north_t = "images/world_interact/hamun_city/ham_merch_exit_north.webp"
image hamun_dist_merch_lord_exit_north_h:
    "hamun_dist_merch_lord_exit_north_t"
    matrixcolor MxMapHover()
# library
image hamun_library_t = "images/world_interact/hamun_city/hamun_library.webp"
image hamun_library_h:
    "hamun_library_t"
    matrixcolor MxMapHover()
# spa
image hamun_spa_t = "images/world_interact/hamun_city/hamun_spa.webp"
image hamun_spa_h:
    "hamun_spa_t"
    matrixcolor MxMapHover()
# lord zanzibat
image hamun_zanzibat_house_t = "images/world_interact/hamun_city/hamun_zanzibat_house.webp"
image hamun_zanzibat_house_h:
    "hamun_zanzibat_house_t"
    matrixcolor MxMapHover()
# lord zanzibat
image hamun_tarbeck_house_t = "images/world_interact/hamun_city/hamun_tarbeck_house.webp"
image hamun_tarbeck_house_h:
    "hamun_tarbeck_house_t"
    matrixcolor MxMapHover()
# faymore manor
image hamun_faymore_manor_t = "images/world_interact/hamun_city/hamun_faymore_manor.webp"
image hamun_faymore_manor_h:
    "hamun_faymore_manor_t"
    matrixcolor MxMapHover()
# castle
image hamun_castle_t = "images/world_interact/hamun_city/hamun_castle.webp"
image hamun_castle_h:
    "hamun_castle_t"
    matrixcolor MxMapHover()
####################################################################################

init python:
    WorldLocation("hamun_dist_merch_lord", STR_LOC.HAMUN_DIST_MERCH_LORD, "hamun_dist_merch_lord", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_dist_merch_lord"]
    ###### clickables ######
    LocDef.withBtn("hamun_dist_merch_lord_to_dist_docks",   BtnChangeLoc(STR_LOC.HAMUN_DIST_DOCKS,  "hamun_dist_docks"))
    LocDef.withBtn("hamun_dist_merch_lord_to_dist_arena",   BtnChangeLoc(STR_LOC.HAMUN_DIST_ARENA,  "hamun_dist_arena"))
    LocDef.withBtn("hamun_dist_merch_lord_to_library",      BtnChangeLoc(STR_LOC.HAMUN_LIBRARY,     "hamun_library"))
    LocDef.withBtn("hamun_dist_merch_lord_to_spa",          BtnChangeLoc(STR_LOC.HAMUN_SPA,         "hamun_spa"))
    # these house locks are handled by quests/lms
    LocDef.withBtn("hamun_dist_merch_lord_to_castle",       BtnDisabled())
    LocDef.withBtn("hamun_dist_merch_lord_to_zanzibat_house", BtnDisabled())
    LocDef.withBtn("hamun_dist_merch_lord_to_tarbeck_mainhall", BtnDisabled())
    LocDef.withBtn("hamun_dist_merch_lord_to_faymore_manor", BtnDisabled())

    LocDef.withBtn("btn_hamun_dist_merch_lord_to_sewers", BtnDisabled())
    ########################
    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    # action sfx
    LocDef.withActionSFXs({
        "hamun_dist_merch_lord_to_library":          soundLib["tentFlap"],
        "hamun_dist_merch_lord_to_spa":              soundLib["tentFlap"],
        "hamun_dist_merch_lord_to_zanzibat_house":   soundLib["tentFlap"],
        "hamun_dist_merch_lord_to_tarbeck_mainhall": soundLib["tentFlap"],
        "hamun_dist_merch_lord_to_faymore_manor":    soundLib["tentFlap"],
        })
    # vfx
    vfxLibLights["hamun_dist_merch_lord_night"] = {
        "lightpost_big":[
            (1190, 991), (1266, 930), (1398, 765), (1449, 727),
            (1483, 659), (1508, 478), (1506, 382), (1519, 203),
            (1523, 96),  (938, 35),   (819, 32),   (1030, 408),
            (724, 591),  (537, 405),  (740, 304),  (1265, 927),
            (1190, 991), (769, 938),  (644, 944),  (320, 377),
            (403, 323),  (1122, 1060)]}
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

screen loc_hamun_dist_merch_lord():
    default locTag = "hamun_dist_merch_lord"
    use locBtn_sprite(locTag, "hamun_dist_merch_lord_to_dist_arena", 
        "hamun_dist_merch_lord_exit_north_t",
        "hamun_dist_merch_lord_exit_north_h",
        Transform(anchor = (0, 0), pos = (690, 0)), key = config.keymap["nav_up"])
    
    use locBtn_sprite(locTag, "hamun_dist_merch_lord_to_dist_docks", 
        "hamun_dist_merch_lord_exit_south_t",
        "hamun_dist_merch_lord_exit_south_h",
        Transform(anchor = (0, 0), pos = (520, 865)), key = config.keymap["nav_down"])

    use locBtn_sprite(locTag, "hamun_dist_merch_lord_to_library", 
        "hamun_library_t",
        "hamun_library_h",
        Transform(anchor = (0, 0), pos = (757, 612)))

    use locBtn_sprite(locTag, "hamun_dist_merch_lord_to_spa", 
        "hamun_spa_t",
        "hamun_spa_h",
        Transform(anchor = (0, 0), pos = (1073, 335)))

    use locBtn_sprite(locTag, "hamun_dist_merch_lord_to_zanzibat_house", 
        "hamun_zanzibat_house_t",
        "hamun_zanzibat_house_h",
        Transform(anchor = (0, 0), pos = (274, 503)))

    use locBtn_sprite(locTag, "hamun_dist_merch_lord_to_tarbeck_mainhall", 
        "hamun_tarbeck_house_t",
        "hamun_tarbeck_house_h",
        Transform(anchor = (0, 0), pos = (892, 45)))

    use locBtn_sprite(locTag, "hamun_dist_merch_lord_to_faymore_manor", 
        "hamun_faymore_manor_t",
        "hamun_faymore_manor_h",
        Transform(anchor = (0.0, 1.0), pos = (0.0, 1.0)))

    use locBtn_sprite(locTag, "hamun_dist_merch_lord_to_castle", 
        "hamun_castle_t",
        "hamun_castle_h",
        Transform(anchor = (0.0, 0.0), pos = (0.0, 0.0)))

    # exit to entrance
    use locBtn_basic(locTag, "btn_hamun_dist_merch_lord_to_sewers",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.33, 0.22)))

