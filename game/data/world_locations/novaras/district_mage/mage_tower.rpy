init python:
    @AppendToAllQuests
    # logicmodule that controls access to all the tower rooms
    class HouseLockPalamTowerRooms(LogicModule):
        def __init__(self):
            super().__init__()

            self.DEBUG_MasterKey = False

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_palam_e_wing":
                if QstIsActive(QstLittleLies) or QstIsComplete(QstLittleLies):
                    if not QstLittleLies().isDormBlocked():
                        btnMods["btn_palam_e_wing_to_dorm"] = BtnChangeLoc(
                            STR_LOC.NOV_PALAM_DORM, "novaras_palam_dorm")
                else:
                    btnMods["btn_palam_e_wing_to_dorm"] = BtnJumpLabel(
                        STR_LOC.NOV_PALAM_DORM, "palam_divine_dorm_refuse")

                if QstGetProgress(QstLittleLies) >= 5:
                    btnMods["btn_palam_e_wing_to_class"] = BtnChangeLoc(
                        STR_LOC.NOV_PALAM_CLASS, "novaras_palam_class")
                else:
                    btnMods["btn_palam_e_wing_to_class"] = BtnJumpLabel(
                        STR_LOC.NOV_PALAM_CLASS, "palam_divine_class_refuse")
                if QstGetProgress(PrimerGirlTroubles) == 1 and QstIsActive(PrimerGirlTroubles):
                    btnMods["btn_palam_e_wing_to_divine_office"] = BtnChangeLoc(
                        STR_LOC.NOV_PALAM_DIVINE_OFFICE, "novaras_palam_divine_office")
                else:
                    btnMods["btn_palam_e_wing_to_divine_office"] = BtnJumpLabel(
                        STR_LOC.NOV_PALAM_DIVINE_OFFICE, "palam_divine_divine_office_refuse")
            elif GetLocID() == "novaras_palam_w_wing":
                if QstIsActive(QstLittleLies) or QstIsComplete(QstLittleLies):
                    btnMods["btn_palam_w_wing_to_garden"] = BtnChangeLoc(
                        STR_LOC.NOV_PALAM_GARDEN, "novaras_palam_garden")
                    btnMods["btn_palam_w_wing_to_bath"] = BtnChangeLoc(
                        STR_LOC.NOV_PALAM_BATH, "novaras_palam_bath")
                else:
                    btnMods["btn_palam_w_wing_to_garden"] = BtnJumpLabel(
                        STR_LOC.NOV_PALAM_GARDEN, "palam_divine_garden_refuse")
                    btnMods["btn_palam_w_wing_to_bath"] = BtnJumpLabel(
                        STR_LOC.NOV_PALAM_BATH, "palam_divine_bath_refuse")
                
                if IsDaytime():
                    btnMods["btn_palam_w_wing_to_divine_quarters"] = BtnJumpLabel(
                        STR_LOC.NOV_PALAM_DIVINE_QUARTERS, "palam_divine_quarters_refuse")
                else:
                    ### this assumes the only way player can be at w_wing at night is if they romanced SD
                    if QstIsActive(RomanceDivine):
                        btnMods["btn_palam_w_wing_to_divine_quarters"] = BtnChangeLoc(
                            STR_LOC.NOV_PALAM_DIVINE_QUARTERS, "novaras_palam_divine_quarters")
                    else:
                        btnMods["btn_palam_w_wing_to_divine_quarters"] = BtnJumpLabel(
                            STR_LOC.NOV_PALAM_DIVINE_QUARTERS, "palam_divine_quarters_refuse")

            if QstGetProgress(QstLittleLies) >= 6:
                    btnMods["btn_palam_garden_to_arena"] = BtnChangeLoc(
                        STR_LOC.NOV_PALAM_ARENA, "novaras_palam_arena")

            return LocButtonMod(directMods=btnMods)

label palam_divine_divine_office_refuse:
    MC "(I don't think Divine will like me snooping around in there...)"
    $ LocEnterQ()

label palam_divine_class_refuse:
    MC "(I don't think Divine will like me snooping around in there...)"
    $ LocEnterQ()

label palam_divine_bath_refuse:
    MC "(I don't think Divine will like me snooping around in there...)"
    $ LocEnterQ()

label palam_divine_garden_refuse:
    MC "(I don't think Divine will like me snooping around in there...)"
    $ LocEnterQ()

label palam_divine_dorm_refuse:
    MC "(I don't think Divine will like me snooping around in there...)"
    $ LocEnterQ()

label palam_divine_quarters_refuse:
    MC "(I don't think Divine will like me snooping around in there...)"
    $ LocEnterQ()

# shared label called on player trying to access palam rooms we dont want em to
label palam_i_shouldnt_go_there:
    $ rng = RngInt(1, 3)
    if rng == 1:
        BLACK "Stop."
        MC "Why?"
        BLACK "I can sense the content behind that door is still in production."
        MC "Wha...?"
        BLACK "Don't. Go. In."
        MC "Fine, whatever..."

    if rng == 2:
        BLACK "We can't go in there."
        MC "Why?"
        BLACK "There's nothing behind that door."
        BLACK "Emptiness."
        BLACK "Void."
        BLACK "{i}WIP stuff.{/i}"
        MC "Well, whatever you mean by that, I guess I'll trust you on that one..."

    if rng == 3:
        BLACK "Do not enter."
        BLACK "What you see, you will not be able to un-see."
        MC "Why?"
        BLACK "There's work-in-progress content behind that door."
        MC "Like, people working?"
        BLACK "Not people."
        BLACK "{b}Gods.{/b}"
        MC "..."
        MC "Okay, whatever."
    $ LocEnterQ()

init python:
# the tower is split into plenty locations, below are code sections for each loc
########### Main hall #############
    WorldLocation("novaras_palam_mainhall", STR_LOC.NOV_PALAM_MAINHALL, "bg_palam_mainhall", parent = "novaras_dist_mage", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_palam_mainhall"]
    LocDef.CanWait = False

    LocDef.withBtn("novaras_palam_mainhall_toCity", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("btn_palam_mainhall_talk_divine", BtnDisabled())
    LocDef.withBtn("btn_palam_mainhall_to_e_wing", BtnChangeLoc(STR_LOC.NOV_PALAM_E_WING, "novaras_palam_e_wing"))
    LocDef.withBtn("btn_palam_mainhall_to_w_wing", BtnChangeLoc(STR_LOC.NOV_PALAM_W_WING, "novaras_palam_w_wing"))
    # music
    LocDef.withDayMusic("audio/music/26_Palam.ogg")
    LocDef.withNightMusic("audio/music/34_PalamNight.ogg")
    # action sfx
    LocDef.withActionSFXs({"novaras_palam_mainhall_toCity": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_palam_mainhall_night"] = {"lightpost_huge":[(559, 558), (1362, 561)]}
    vfxLibLights["novaras_palam_mainhall"] = {"lightpost_huge":[(559, 558), (1362, 561)]}


########### West wing ###################
    WorldLocation("novaras_palam_w_wing", STR_LOC.NOV_PALAM_W_WING, "bg_palam_w_wing", parent = "novaras_palam_mainhall", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_palam_w_wing"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_palam_w_wing_to_mainhall", BtnChangeLoc(STR_LOC.NOV_PALAM_MAINHALL, "novaras_palam_mainhall"))

    LocDef.withBtn("btn_palam_w_wing_to_bath", BtnDisabled())
    LocDef.withBtn("btn_palam_w_wing_to_garden", BtnDisabled())
    LocDef.withBtn("btn_palam_w_wing_to_divine_quarters", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/26_Palam.ogg")
    LocDef.withNightMusic("audio/music/34_PalamNight.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_palam_w_wing_to_bath": soundLib["woodenDoor"],
                        "btn_palam_w_wing_to_garden": soundLib["woodenDoor"],
                        "btn_palam_w_wing_to_divine_quarters": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_palam_w_wing_night"] = {
        "lightpost_huge":[(112, 706), (1832, 711)],
        "lightpost_big":[(290, 311), (561, 405), (1599, 315), (1325, 407), (719, 474), (1168, 475)],
        "lightpost_small":[(1076, 512), (1023, 530), (1025, 580), (864, 580), (863, 531), (813, 511)],
        }
    LocDef.SetDayNightMatrixClass(MxDayNight)

########### Girls' bathroom #############
    WorldLocation("novaras_palam_bath", STR_LOC.NOV_PALAM_BATH, "bg_palam_bath", parent = "novaras_palam_w_wing", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_palam_bath"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_palam_bath_to_w_wing", 
        BtnChangeLoc(STR_LOC.NOV_PALAM_W_WING, "novaras_palam_w_wing"))
    # music
    LocDef.withDayMusic("audio/music/26_Palam.ogg")
    LocDef.withNightMusic("audio/music/34_PalamNight.ogg")
    LocDef.withGenAmbience("audio/ambience_loc/novaras_palam_bath.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_palam_bath_to_w_wing": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_palam_bath_night"] = {
        "lightpost_big":[(634, 299), (1237, 298)],
        "lightpost_small":[(13, 244), (332, 271), (1515, 286), (1590, 267), (1663, 250), (1678, 274), (1785, 232), (1889, 237)],
        }
    LocDef.SetDayNightMatrixClass(MxDayNight)

########### Rooftop garden #############
    WorldLocation("novaras_palam_garden", STR_LOC.NOV_PALAM_GARDEN, "bg_palam_garden", parent = "novaras_palam_w_wing", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_palam_garden"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_palam_garden_to_w_wing", BtnChangeLoc(STR_LOC.NOV_PALAM_W_WING, "novaras_palam_w_wing"))
    LocDef.withBtn("btn_palam_garden_to_arena", BtnDisabled())
    LocDef.withBtn("btn_palam_arena_mika_talk", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/26_Palam.ogg")
    LocDef.withNightMusic("audio/music/34_PalamNight.ogg")

    LocDef.withGenAmbience("audio/ambience_loc/garden_amb.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_palam_garden_to_w_wing": soundLib["woodenDoor"]})
    # mika talk btn
    LocDef.withBtn("btn_palam_garden_mika_talk_btn", BtnDisabled())
    # vfx
    vfxLibLights["novaras_palam_garden_night"] = {
        "lightpost_huge":[(1610, 562), (1013, 527)],
        "lightpost_big":[(690, 549), (469, 572), (549, 528), (273, 532), (168, 348), (269, 350)],
        }
    LocDef.SetDayNightMatrixClass(MxDayNight)

########### Arena #############
    WorldLocation("novaras_palam_arena", STR_LOC.NOV_PALAM_ARENA, "bg_palam_arena", parent = "novaras_palam_garden", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_palam_arena"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_palam_arena_to_garden", BtnChangeLoc(STR_LOC.NOV_PALAM_GARDEN, "novaras_palam_garden"))
    # music
    LocDef.withDayMusic("audio/music/26_Palam.ogg")
    LocDef.withNightMusic("audio/music/34_PalamNight.ogg")
    # vfx
    vfxLibLights["novaras_palam_arena_night"] = {
        "lightpost_big":[(214, 480), (596, 480), (1350, 495), (1794, 480)],
        "lightpost_small":[(1538, 619), (1556, 637), (1521, 668)],
        }
    LocDef.SetDayNightMatrixClass(MxDayNight)

########### Sister Divine's private quarters ##########
    WorldLocation("novaras_palam_divine_quarters", STR_LOC.NOV_PALAM_DIVINE_QUARTERS, "bg_palam_divine_quarters", parent = "novaras_palam_w_wing", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_palam_divine_quarters"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_palam_divine_quarters_to_w_wing", 
        BtnChangeLoc(STR_LOC.NOV_PALAM_W_WING, "novaras_palam_w_wing"))
    LocDef.withBtn("btn_talk_divine_quarters", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/26_Palam.ogg")
    LocDef.withNightMusic("audio/music/34_PalamNight.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_palam_divine_quarters_to_w_wing": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_palam_divine_quarters_night"] = {
        "lightpost_small":[(1501, 546), (1562, 536), (1603, 546), (1763, 203), (1847, 424), (1888, 600), (1775, 644)],
        "light_crystal_teal":[(1713, 565)],
        "light_haze_fiery":[(753, 577)],
        }
    LocDef.SetDayNightMatrixClass(MxDayNight)

########### East wing #############
    WorldLocation("novaras_palam_e_wing", STR_LOC.NOV_PALAM_E_WING, "bg_palam_e_wing", parent = "novaras_palam_mainhall", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_palam_e_wing"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_palam_e_wing_to_mainhall", 
        BtnChangeLoc(STR_LOC.NOV_PALAM_MAINHALL, "novaras_palam_mainhall"))

    LocDef.withBtn("btn_palam_e_wing_to_dorm", BtnDisabled())
    LocDef.withBtn("btn_palam_e_wing_to_class", BtnDisabled())
    LocDef.withBtn("btn_palam_e_wing_to_divine_office", BtnDisabled())

    # for markus x mika rep scenes
    LocDef.withBtn("btn_palam_e_wing_investigate_sounds", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/26_Palam.ogg")
    LocDef.withNightMusic("audio/music/34_PalamNight.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_palam_e_wing_to_dorm": soundLib["woodenDoor"],
                        "btn_palam_e_wing_to_class": soundLib["woodenDoor"],
                        "btn_palam_e_wing_to_divine_office": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_palam_e_wing_night"] = {
        "lightpost_huge":[(1808, 706), (88, 711)],
        "lightpost_big":[(1630, 311), (1359, 405), (321, 315), (595, 407), (1201, 474), (752, 475)],
        "lightpost_small":[(844, 512), (897, 530), (895, 580), (1056, 580), (1057, 531), (1107, 511)],
        }
    LocDef.SetDayNightMatrixClass(MxDayNight)

########### Girls' dormitory #############
    WorldLocation("novaras_palam_dorm", STR_LOC.NOV_PALAM_DORM, "bg_palam_dorm", parent = "novaras_palam_e_wing", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_palam_dorm"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_palam_dorm_to_e_wing", BtnChangeLoc(STR_LOC.NOV_PALAM_E_WING, "novaras_palam_e_wing"))
    # music
    LocDef.withDayMusic("audio/music/26_Palam.ogg")
    LocDef.withNightMusic("audio/music/34_PalamNight.ogg")

    LocDef.withGenAmbience("audio/ambience_loc/fireplace.ogg")

    # action sfx
    LocDef.withActionSFXs({"btn_palam_dorm_to_e_wing": soundLib["woodenDoor"]})
    # mika talk
    LocDef.withBtn("btn_palam_dorm_mika_talk_btn", BtnDisabled())

    # vfx
    vfxLibLights["novaras_palam_dorm_night"] = {
        "light_crystal_teal":[(1666, 351)],
        "light_haze_fiery":[(1185, 520)],
        "light_haze_pink_magical":[(105, 348)]
        }
    vfxLibLights["novaras_palam_dorm"] = {
        "light_crystal_teal":[(1666, 351)],
        "light_haze_fiery":[(1185, 520)],
        "light_haze_pink_magical":[(105, 348)]
        }



########### Mages' classroom #############
    WorldLocation("novaras_palam_class", STR_LOC.NOV_PALAM_CLASS, "bg_palam_class", parent = "novaras_palam_e_wing", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_palam_class"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_palam_class_to_e_wing", 
        BtnChangeLoc(STR_LOC.NOV_PALAM_E_WING, "novaras_palam_e_wing"))
    # music
    LocDef.withDayMusic("audio/music/26_Palam.ogg")
    LocDef.withNightMusic("audio/music/34_PalamNight.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_palam_class_to_e_wing": soundLib["woodenDoor"]})

    # vfx
    vfxLibLights["novaras_palam_class_night"] = {
        "light_haze_teal_magical":[(920, 611)],
        }
    # vfx
    vfxLibLights["novaras_palam_class"] = {
        "light_haze_teal_magical":[(920, 611)],
        }
    LocDef.SetDayNightMatrixClass(MxDayNight)

########### Sister Divine's office ##########
    WorldLocation("novaras_palam_divine_office", STR_LOC.NOV_PALAM_DIVINE_OFFICE, "bg_palam_divine_office", parent = "novaras_palam_e_wing", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_palam_divine_office"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_palam_divine_office_to_e_wing", BtnChangeLoc(STR_LOC.NOV_PALAM_E_WING, "novaras_palam_e_wing"))
    # music
    LocDef.withDayMusic("audio/music/26_Palam.ogg")
    LocDef.withNightMusic("audio/music/34_PalamNight.ogg")

    LocDef.withGenAmbience("audio/ambience_loc/novaras_palam_bath.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_palam_divine_office_to_e_wing": soundLib["woodenDoor"]})

    # vfx
    vfxLibLights["novaras_palam_divine_office_night"] = {
        "lightpost_big":[(1691, 77), (1701, 394), (366, 284), (405, 301), (446, 297), (493, 280), (764, 291), (791, 298), (830, 305), (870, 289)],
        }



######## below are loc screens that correspond to each sub-location:
########### Main hall #############
screen loc_novaras_palam_mainhall():
    default locTag = "novaras_palam_mainhall"
    use locShared_toCityBtn(locTag, "novaras_palam_mainhall_toCity")
    use locBtn_Char(locTag, "btn_palam_mainhall_talk_divine", 
        "divine", "divine", 
        Transform(anchor = (0.5, 0.5), pos = (0.18, 0.65), zoom = 0.9))

    use locBtn_basic(locTag, "btn_palam_mainhall_to_e_wing", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.78, 0.1)),
        key = config.keymap["nav_right"])
    use locBtn_basic(locTag, "btn_palam_mainhall_to_w_wing", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.22, 0.1)),
        key = config.keymap["nav_left"])

########### West wing ###################
screen loc_novaras_palam_w_wing():
    default locTag = "novaras_palam_w_wing"
    use locBtn_basic(locTag, "btn_palam_w_wing_to_mainhall", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    use locBtn_basic(locTag, "btn_palam_w_wing_to_bath", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.31, 0.53)))
    use locBtn_basic(locTag, "btn_palam_w_wing_to_garden", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.17, 0.52)))
    use locBtn_basic(locTag, "btn_palam_w_wing_to_divine_quarters", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.49, 0.53)))

########### Girls' bath #############
screen loc_novaras_palam_bath():
    default locTag = "novaras_palam_bath"
    use locBtn_basic(locTag, "btn_palam_bath_to_w_wing", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.5, 0.85)), key = config.keymap["nav_down"])

########### Rooftop garden #############
screen loc_novaras_palam_garden():
    default locTag = "novaras_palam_garden"
    use locBtn_basic(locTag, "btn_palam_garden_to_w_wing", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.5, 0.85)), key = config.keymap["nav_down"])

    use locBtn_basic(locTag, "btn_palam_garden_to_arena", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.17, 0.52)), key = config.keymap["nav_left"])

    use locBtn_Char(locTag, "btn_palam_garden_mika_talk_btn", 
        "mika", "mika", 
        Transform(anchor = (0.5, 0.5), pos = (0.3, 0.65), zoom = 0.9))

screen loc_novaras_palam_arena():
    default locTag = "novaras_palam_arena"
    use locBtn_basic(locTag, "btn_palam_arena_to_garden", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.5, 0.85)), key = config.keymap["nav_down"])

    use locBtn_Char(locTag, "btn_palam_arena_mika_talk", 
        "mika", "mika", 
        Transform(anchor = (0.5, 0.5), pos = (0.3, 0.65), zoom = 0.9))

########### Sister Divine's private quarters ##########
screen loc_novaras_palam_divine_quarters():
    default locTag = "novaras_palam_divine_quarters"
    use locBtn_basic(locTag, "btn_palam_divine_quarters_to_w_wing", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.5, 0.85)), key = config.keymap["nav_down"])
    use locBtn_Char(locTag, "btn_talk_divine_quarters", 
        "divine", "divine", 
        Transform(anchor = (0.5, 0.5), pos = (0.7, 0.65), zoom = 0.9))

########### East wing #############
screen loc_novaras_palam_e_wing():
    default locTag = "novaras_palam_e_wing"
    use locBtn_basic(locTag, "btn_palam_e_wing_to_mainhall", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    use locBtn_basic(locTag, "btn_palam_e_wing_to_dorm", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.69, 0.53)))
    use locBtn_basic(locTag, "btn_palam_e_wing_to_class", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.82, 0.52)))
    use locBtn_basic(locTag, "btn_palam_e_wing_to_divine_office", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.51, 0.53)))
    
    # for mika / markus rep scenes
    use locBtn_basic(locTag, "btn_palam_e_wing_investigate_sounds", 
        "images/gui/buttons_loc/heart.webp", 
        Transform(pos = (0.6, 0.53)),
        IconAllTheTime = True)


########### Girls' dormitory #############
screen loc_novaras_palam_dorm():
    default locTag = "novaras_palam_dorm"
    use locBtn_basic(locTag, "btn_palam_dorm_to_e_wing", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.5, 0.85)), key = config.keymap["nav_down"])

    use locBtn_Char(locTag, "btn_palam_dorm_mika_talk_btn", 
        "mika", "mika", 
        Transform(anchor = (0.5, 0.5), pos = (0.3, 0.65), zoom = 0.9))

########### Mages' classroom #############
screen loc_novaras_palam_class():
    default locTag = "novaras_palam_class"
    use locBtn_basic(locTag, "btn_palam_class_to_e_wing", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.5, 0.85)), key = config.keymap["nav_down"])

    use locBtn_Char(locTag, "btn_palam_class_mika_talk", 
        "mika", "mika", 
        Transform(anchor = (0.5, 0.5), pos = (0.3, 0.65), zoom = 0.9))

########### Sister Divine's office ##########
screen loc_novaras_palam_divine_office():
    default locTag = "novaras_palam_divine_office"
    use locBtn_basic(locTag, "btn_palam_divine_office_to_e_wing", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.5, 0.85)), key = config.keymap["nav_down"])
