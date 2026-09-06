init python:
##########################################################################################
################# root fort area ###############################################
    WorldLocation("novaras_fort_seb_yard", STR_LOC.NOV_CITY_FORT_YARD, "bg_sebastian_yard", parent = "novaras_dist_army", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_fort_seb_yard"]
    # nav
    LocDef.withBtn("btn_novaras_fort_seb_yard_toCity", BtnChangeLoc(STR_NAV.TO_CITY, "novaras_dist_army"))
    LocDef.withBtn("btn_novaras_fort_seb_yard_to_barracks", BtnChangeLoc(STR_LOC.NOV_CITY_FORT_BARRACKS, "novaras_fort_seb_barracks")) # to nyx office / bedroom
    LocDef.withBtn("btn_novaras_fort_seb_yard_to_medward", BtnChangeLoc(STR_LOC.NOV_CITY_FORT_MEDWARD, "novaras_fort_seb_medward"))
    LocDef.withBtn("btn_novaras_fort_seb_yard_to_train", BtnChangeLoc(STR_LOC.NOV_CITY_FORT_TRAIN, "novaras_fort_seb_train"))
    # char(s)
    # kiara clickey here is handled exclusively by forgedinfire
    LocDef.withBtn("btn_novaras_fort_seb_kiara_talk", BtnDisabled())
    # vfx
    vfxLibLights["novaras_fort_seb_yard_night"] = {
        "lightpost_big":[(297, 483), (1893, 507), (1441, 480)],
        "lightpost_small":[(862, 393)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)
    # action sfx
    LocDef.withActionSFXs({"btn_novaras_fort_seb_yard_toCity": "audio/interactables/gate_drop.ogg"})
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/sebastian.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")

    @AppendToAllQuests
    class HouseLockFortSebastian(LogicModule):
        def __init__(self):
            super().__init__()

            self.CanEnterFreely = False # <- set to true in dark knight quest

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_army":
                if self.CanEnterFreely:
                    btnMods["btn_novaras_fort_seb"] = BtnChangeLoc(STR_LOC.NOV_CITY_FORT, "novaras_fort_seb_yard")
                else:
                    btnMods["btn_novaras_fort_seb"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT, "HouseLock_SebastianGuard")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("dialogue_sebastian_guard_root", DNode(_("None, really."), "HouseLock_SebastianGuard_bye", nextNode = "DNodeExit", order = -100))

# actually fired by terminus prologue prog 4
label HouseLock_SebastianGuard:
    show cg_guard at center_f with dissolve
    show cg_guard at shake
    GUARD "Halt!"
    GUARD "What business have you at the fort, citizen?"
    call processDialogue("dialogue_sebastian_guard_root") from _call_processDialogue_48
    $ LocEnter()

label HouseLock_SebastianGuard_bye:
    GUARD "That's right."
    GUARD "Move it, citizen."
    return

screen loc_novaras_fort_seb_yard():
    default locTag = "novaras_fort_seb_yard"
    use locShared_toCityBtn(locTag, "btn_novaras_fort_seb_yard_toCity")

    # only forged in fire quest (prologue)
    use locBtn_Char(locTag, "btn_novaras_fort_seb_kiara_talk", "kiara", "kiara", Transform(anchor =( 0.5, 1.0), pos = (0.38, 0.61), zoom = 0.31))

    use locBtn_basic(locTag, "btn_novaras_fort_seb_yard_to_barracks", "images/gui/buttons_loc/door.webp", Transform(pos = (0.5, 0.4)), key = config.keymap["nav_up"])
    use locBtn_basic(locTag, "btn_novaras_fort_seb_yard_to_medward", "images/gui/buttons_loc/door.webp", Transform(pos = (0.91, 0.44)), key = config.keymap["nav_right"])
    use locBtn_basic(locTag, "btn_novaras_fort_seb_yard_to_train", "images/gui/buttons_loc/door.webp", Transform(pos = (0.13, 0.36)), key = config.keymap["nav_left"])

##########################################################################################
###################### (INSIDE) barracks  ####################################################
init python:
    WorldLocation("novaras_fort_seb_barracks", STR_LOC.NOV_CITY_FORT_BARRACKS, "bg_seb_barracks", parent = "novaras_fort_seb_yard", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_fort_seb_barracks"]
    # nav
    LocDef.withBtn("btn_novaras_fort_seb_barracks_to_main_area", BtnChangeLoc(STR_LOC.NOV_CITY_FORT_YARD, "novaras_fort_seb_yard"))
    LocDef.withBtn("btn_novaras_fort_seb_barracks_to_captain_office", BtnChangeLoc(STR_LOC.NOV_CITY_FORT_CAPTAIN_OFFICE, "novaras_fort_seb_captains_office")) # to nyx office / bedroom
    # vfx
    vfxLibLights["novaras_fort_seb_barracks_night"] = {
        "lightpost_big":[(404, 194), (835, 245)],
        "lightpost_small":[(1309, 323), (1562, 348), (882, 345), (489, 303)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)
    # clickable bed (handled by forged in fire quest)
    LocDef.withBtn("btn_novaras_fort_seb_barracks_bed", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    

screen loc_novaras_fort_seb_barracks():
    default locTag = "novaras_fort_seb_barracks"

    use locShared_toCityBtn(locTag, "btn_novaras_fort_seb_barracks_to_main_area")
    use locBtn_basic(locTag, "btn_novaras_fort_seb_barracks_to_captain_office", "images/gui/buttons_loc/door.webp", Transform(pos = (0.8, 0.45)), key = config.keymap["nav_right"])
    use locBtn_basic(locTag, "btn_novaras_fort_seb_barracks_bed", "images/gui/buttons_loc/sleep.webp", Transform(pos = (0.37, 0.5)))

##########################################################################################
###################### (INSIDE) med ward ###################################################
init python:
    WorldLocation("novaras_fort_seb_medward", STR_LOC.NOV_CITY_FORT_MEDWARD, "bg_medward", parent = "novaras_fort_seb_yard", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_fort_seb_medward"]
    # nav
    LocDef.withBtn("btn_novaras_fort_seb_medward_to_main_area", BtnChangeLoc(STR_LOC.NOV_CITY_FORT_YARD, "novaras_fort_seb_yard"))
    # vfx
    vfxLibLights["novaras_fort_seb_medward_night"] = {
        "lightpost_big":[(350, 133), (1393, 286)],
        "lightpost_small":[(722, 226), (1298, 290)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")

screen loc_novaras_fort_seb_medward():
    default locTag = "novaras_fort_seb_medward"
    use locShared_toCityBtn(locTag, "btn_novaras_fort_seb_medward_to_main_area")
##########################################################################################
###################### (INSIDE) train area ###################################################
init python:
    WorldLocation("novaras_fort_seb_train", STR_LOC.NOV_CITY_FORT_TRAIN, "bg_seb_train_area", parent = "novaras_fort_seb_yard", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_fort_seb_train"]
    # nav
    LocDef.withBtn("btn_novaras_fort_seb_train_to_main_area", BtnChangeLoc(STR_LOC.NOV_CITY_FORT_YARD, "novaras_fort_seb_yard"))
    # train button, handled by forged in fire quest
    LocDef.withBtn("btn_novaras_fort_seb_train_begin", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/sebastian.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # vfx
    vfxLibLights["novaras_fort_seb_train_night"] = {
        "lightpost_big":[(1436, 621), (33, 47), (32, 646), (573, 619), (459, 619), (710, 434), (710, 219)],
        "lightpost_huge":[(1846, 546)],
        "lightpost_small":[(804, 360), (950, 384), (1236, 428), (1148, 137)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_fort_seb_train():
    default locTag = "novaras_fort_seb_train"
    use locShared_toCityBtn(locTag, "btn_novaras_fort_seb_train_to_main_area")

    use locBtn_basic(locTag, "btn_novaras_fort_seb_train_begin", "images/gui/buttons_loc/question.webp", Transform(pos = (0.5, 0.5)), key = config.keymap["nav_up"])
##########################################################################################
######################## (INSIDE) captain's office ################################################
init python:
    WorldLocation("novaras_fort_seb_captains_office", STR_LOC.NOV_CITY_FORT_CAPTAIN_OFFICE, "bg_nyx_office", parent = "novaras_fort_seb_barracks", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_fort_seb_captains_office"]
    LocDef.withBtn("nyx_talk_btn", BtnDisabled())
    # nav
    LocDef.withBtn("btn_novaras_fort_seb_captains_office_to_barracks", BtnChangeLoc(STR_LOC.NOV_CITY_FORT_BARRACKS, "novaras_fort_seb_barracks"))
    LocDef.withBtn("btn_novaras_fort_seb_captains_office_to_bedroom", BtnChangeLoc(STR_LOC.NOV_CITY_FORT_CAPTAIN_BEDROOM, "novaras_fort_seb_captains_bedroom"))
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_novaras_fort_seb_captains_office_to_bedroom"  : soundLib["woodenDoor"],
                        "btn_novaras_fort_seb_captains_office_to_barracks" : soundLib["woodenDoor"]})
    # vfx
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_fort_seb_captains_office():
    default locTag = "novaras_fort_seb_captains_office"
    use locShared_toCityBtn(locTag, "btn_novaras_fort_seb_captains_office_to_barracks")

    # To Nyx's bedroom
    if PlayerItemQty("qst_nyx_room_key") > 0:
        use locBtn_basic(locTag, "btn_novaras_fort_seb_captains_office_to_bedroom", "images/gui/buttons_loc/door.webp", Transform(pos = (0.1, 0.55)), key = config.keymap["nav_left"])
    
    use locBtn_Char(locTag, "nyx_talk_btn", "nyx", "nyx", Transform(anchor = (0.5, 0.5), pos = (0.65, 0.65), xzoom = -1.0, zoom = 0.85))
##########################################################################################
######################## (INSIDE) captain's bedroom ################################################
init python:
    WorldLocation("novaras_fort_seb_captains_bedroom", STR_LOC.NOV_CITY_FORT_CAPTAIN_BEDROOM, "bg_nyx_bedroom", parent = "novaras_fort_seb_captains_office", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_fort_seb_captains_bedroom"]
    # nav
    LocDef.withBtn("btn_novaras_fort_seb_captains_bedroom_to_office", BtnChangeLoc(STR_LOC.NOV_CITY_FORT_CAPTAIN_OFFICE, "novaras_fort_seb_captains_office"))
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_novaras_fort_seb_captains_bedroom_to_office"  : soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_fort_seb_captains_bedroom_night"] = {"lightpost_big":[(1116,301),(1562,266)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_fort_seb_captains_bedroom():
    default locTag = "novaras_fort_seb_captains_bedroom"
    use locShared_toCityBtn(locTag, "btn_novaras_fort_seb_captains_bedroom_to_office")