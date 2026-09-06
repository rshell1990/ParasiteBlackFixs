##### desert camp 
init python:
####### main area 
    WorldLocation("qst_darkpass_desertcamp", STR_LOC.DESERT_CAMP, "bg_camp")
    LocDef = wLocs["qst_darkpass_desertcamp"]
    # music
    LocDef.withDayMusic("audio/music/8_ValleyofDeath.ogg")
    LocDef.withNightMusic("audio/music/8_ValleyofDeath.ogg")
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    # btns
    LocDef.withBtn("btn_darkpass_camp_to_my_tent", BtnChangeLoc(STR_LOC.MY_TENT, "qst_darkpass_desertcamp_mc_tent"))
    LocDef.withBtn("btn_darkpass_camp_to_fireplace", BtnChangeLoc(STR_LOC.DESERT_CAMP_FIRE, "qst_darkpass_desertcamp_fireplace_area"))
    LocDef.withBtn("btn_darkpass_camp_talk_kiara", BtnDisabled())
    LocDef.withBtn("btn_darkpass_camp_talk_markus", BtnDisabled())
    # sfx
    LocDef.withActionSFXs({
        "btn_darkpass_camp_to_my_tent": soundLib["tentFlap"]
        })
    # vfx
    vfxLibLights["qst_darkpass_desertcamp_night"] = {
        "lightpost_big":[(395, 633)],
        "lightpost_small":[(1127, 711), (678, 597), (980, 726)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

####### fireplace area 
    WorldLocation("qst_darkpass_desertcamp_fireplace_area", STR_LOC.DESERT_CAMP, "bg_camp_fireplace_area")
    LocDef = wLocs["qst_darkpass_desertcamp_fireplace_area"]
    # music
    LocDef.withDayMusic("audio/music/8_ValleyofDeath.ogg")
    LocDef.withNightMusic("audio/music/8_ValleyofDeath.ogg")
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night_campfire.ogg")
    # btns
    LocDef.withBtn("btn_darkpass_camp_fireplace_to_main_area", BtnChangeLoc(STR_LOC.DESERT_CAMP, "qst_darkpass_desertcamp"))
    LocDef.withBtn("btn_darkpass_camp_fireplace_play_cards", BtnDisabled())
    LocDef.withBtn("btn_darkpass_camp_fireplace_talk_duprey", BtnDisabled())
    LocDef.withBtn("btn_darkpass_camp_fireplace_talk_borras", BtnDisabled())
    # vfx
    vfxLibLights["qst_darkpass_desertcamp_fireplace_area_night"] = {
        "lightpost_huge":   [(1469, 610), (814, 815)],
        "lightpost_big":    [(171, 786), (431, 671), (973, 534)],
        "lightpost_small":  [(528, 676)],
        }
    LocDef.SetDayNightMatrixClass(MxDayNight)

######### mc tent
    WorldLocation("qst_darkpass_desertcamp_mc_tent", STR_LOC.MY_TENT, "bg_player_camp_tent")
    LocDef = wLocs["qst_darkpass_desertcamp_mc_tent"]
    # music
    LocDef.withDayMusic("audio/music/8_ValleyofDeath.ogg")
    LocDef.withNightMusic("audio/music/8_ValleyofDeath.ogg")
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    # btns
    LocDef.withBtn("btn_darkpass_camp_tent_to_camp", BtnChangeLoc(STR_LOC.DESERT_CAMP, "qst_darkpass_desertcamp"))
    LocDef.withBtn("btn_darkpass_camp_tent_sleep", BtnJumpLabel(_("Bedroll"), "qst_TheDarkPass_ClickedSleepInTent"))
    # sfx
    LocDef.withActionSFXs({
        "btn_darkpass_camp_tent_to_camp": soundLib["tentFlap"]
        })
    # vfx
    vfxLibLights["qst_darkpass_desertcamp_mc_tent_night"] = {
        "lightpost_big":[(183, 814), (1604, 740), (1749, 839)],
    }
    vfxLibLights["qst_darkpass_desertcamp_mc_tent"] = {
        "lightpost_big":[(183, 814), (1604, 740), (1749, 839)],
    }
    



    

screen loc_qst_darkpass_desertcamp():
    default locTag = "qst_darkpass_desertcamp"

    use locBtn_basic(locTag, "btn_darkpass_camp_to_my_tent", "images/gui/buttons_loc/door.webp", Transform(pos = (0.17, 0.64)))
    use locBtn_basic(locTag, "btn_darkpass_camp_to_fireplace", "images/gui/buttons_loc/arrow_u.webp", Transform(pos = (0.37, 0.59)))

    use locBtn_Char(locTag, "btn_darkpass_camp_talk_kiara", 
        "kiara", "kiara", 
        Transform(anchor = (0.5, 1.0), pos = (0.78, 0.805), zoom = 0.36, xzoom = -1.0))
    use locBtn_Char(locTag, "btn_darkpass_camp_talk_markus", 
        "markusprologue", "markusprologue", 
        Transform(anchor = (0.5, 1.0), pos = (0.63, 0.8), zoom = 0.31))

screen loc_qst_darkpass_desertcamp_fireplace_area():
    default locTag = "qst_darkpass_desertcamp_fireplace_area"

    use locBtn_basic(locTag, "btn_darkpass_camp_fireplace_to_main_area", "images/gui/buttons_loc/arrow_u.webp", Transform(pos = (0.34, 0.63)))
    use locBtn_basic(locTag, "btn_darkpass_camp_fireplace_play_cards", "images/gui/buttons_loc/dialogue.webp", Transform(pos = (0.92, 0.62)))

    use locBtn_Char(locTag, "btn_darkpass_camp_fireplace_talk_duprey", 
        "duprey", "duprey", Transform(anchor = (0.5, 1.0), pos = (0.54, 0.71), zoom = 0.25, xzoom = -1.0, yoffset = 0))
    use locBtn_Char(locTag, "btn_darkpass_camp_fireplace_talk_borras", 
        "borras", "borras", Transform(anchor = (0.5, 1.0), pos = (0.17, 0.89), zoom = 0.33))

screen loc_qst_darkpass_desertcamp_mc_tent():
    default locTag = "qst_darkpass_desertcamp_mc_tent"

    use locBtn_basic(locTag, "btn_darkpass_camp_tent_to_camp", "images/gui/buttons_loc/door.webp", Transform(pos = (0.5, 0.37)))
    use locBtn_basic(locTag, "btn_darkpass_camp_tent_sleep", "images/gui/buttons_loc/sleep.webp", Transform(pos = (0.5, 0.75)))

#############################################
##### abandoned fort
init python:
####### main area 
    WorldLocation("qst_darkpass_abandoned_fort", STR_LOC.ABANDONED_FORT, "bg_abandoned_fort")
    LocDef = wLocs["qst_darkpass_abandoned_fort"]
    # music
    LocDef.withDayMusic("audio/music/13_AbandFort.ogg")
    LocDef.withNightMusic("audio/music/13_AbandFort.ogg")
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    # btns
    LocDef.withBtn("btn_darkpass_aband_fort_talk_markus",      BtnDisabled())
    LocDef.withBtn("btn_darkpass_aband_fort_talk_kiara",       BtnDisabled())
    LocDef.withBtn("btn_darkpass_aband_fort_cave_entrance",    BtnDisabled())
    # vfx
    vfxLibLights["qst_darkpass_abandoned_fort_night"] = {
        "lightpost_big":  [(1172, 419)],
    }
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_qst_darkpass_abandoned_fort():
    default locTag = "qst_darkpass_abandoned_fort"

    use locBtn_basic(locTag, "btn_darkpass_aband_fort_cave_entrance", "images/gui/buttons_loc/question.webp", Transform(pos = (0.67, 0.48)))

    use locBtn_Char(locTag, "btn_darkpass_aband_fort_talk_kiara", 
        "kiara", "kiara", Transform(anchor = (0.5, 1.0), pos = (0.5, 0.7), zoom = 0.26))
    use locBtn_Char(locTag, "btn_darkpass_aband_fort_talk_markus", 
        "markusprologue", "markusprologue", Transform(anchor = (0.5, 1.0), pos = (0.21, 0.77), zoom = 0.27))

#############################################
##### obelisks room
init python:
####### main area 
    WorldLocation("qst_darkpass_obelisks", STR_LOC.THE_DEEP_CHAMBER, "bg_obelisks_room")
    LocDef = wLocs["qst_darkpass_obelisks"]
    # music
    LocDef.withDayMusic("audio/music/15_Experiments.ogg")
    LocDef.withNightMusic("audio/music/15_Experiments.ogg")
    # btns
    LocDef.withBtn("btn_darkpass_obeliskroom_papers", BtnDisabled())
    LocDef.withBtn("btn_darkpass_obeliskroom_potions", BtnDisabled())
    LocDef.withBtn("btn_darkpass_obeliskroom_skeleton", BtnDisabled())
    LocDef.withBtn("btn_darkpass_obeliskroom_obelisks", BtnDisabled())
    # vfx
    vfxLibLights["qst_darkpass_obelisks_night"] = {
        "lightpost_huge":[(329, 583)]}

screen loc_qst_darkpass_obelisks():
    default locTag = "qst_darkpass_obelisks"

    use locBtn_basic(locTag, "btn_darkpass_obeliskroom_papers", "images/gui/buttons_loc/question.webp", Transform(pos = (0.38, 0.81)))
    use locBtn_basic(locTag, "btn_darkpass_obeliskroom_potions", "images/gui/buttons_loc/question.webp", Transform(pos = (0.28, 0.57)))
    use locBtn_basic(locTag, "btn_darkpass_obeliskroom_skeleton", "images/gui/buttons_loc/question.webp", Transform(pos = (0.80, 0.77)))
    use locBtn_basic(locTag, "btn_darkpass_obeliskroom_obelisks", "images/gui/buttons_loc/question.webp", Transform(pos = (0.53, 0.51)))

#############################################
