init python:
    # this controls what happens if ya click the clickey house
    @AppendToAllQuests
    class HouseLockNovarasBordelloDoor(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_bordello_ext":
                btnMods["novaras_bordello_door"] = BtnChangeLoc(
                    STR_NAV.ENTER, "novaras_bordello_interior")
            return LocButtonMod(directMods = btnMods)


########################################################################################################
########################################################################################################
################ main hall
    WorldLocation("novaras_bordello_interior", STR_LOC.NOV_BORDELLO, "bg_novaras_bordello_interior", parent = "novaras_dist_pleasure", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_bordello_interior"]
    LocDef.CanWait = False

    LocDef.withBtn("novaras_bordello_interior_leave", BtnChangeLoc(STR_NAV.LEAVE, "novaras_bordello_ext"))
    LocDef.withBtn("btn_novaras_bordello_mainhall_to_office", BtnDisabled())#BtnChangeLoc(STR_LOC.NOV_BORDELLO_OFFICE, "novaras_bordello_office"))
    LocDef.withBtn("btn_novaras_bordello_mainhall_to_dungeon", BtnDisabled())#BtnChangeLoc(STR_LOC.NOV_BORDELLO_DUNGEON, "novaras_bordello_sex_dungeon"))
    # handled by their logic modules
    LocDef.withBtn("btn_talk_arwen", BtnDisabled())
    LocDef.withBtn("dros_bordello_talk_btn", BtnDisabled())

    #LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    #LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withNightMusic("audio/music/24_Brothel.ogg")
    LocDef.withDayMusic("audio/music/24_Brothel.ogg")
    # vfx
    vfxLibLights["novaras_bordello_interior_night"] = {
        "lightpost_small":[(1622, 198), (1423, 221), (1216, 243), (1085, 273)],
        "lightpost_big":[(234, 497)]}
    # sfx
    LocDef.withActionSFXs({"novaras_bordello_interior_leave": soundLib["woodenDoor"],
                    "btn_novaras_bordello_mainhall_to_office": soundLib["woodenDoor"],
                    "btn_novaras_bordello_mainhall_to_dungeon": soundLib["woodenDoor"]})


########################################################################################################
########################################################################################################
################ office
    # door, enabled by completing the primer to beneaththeshadows quest
    @AppendToAllQuests
    class DoorNovarasBordelloOffice(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_bordello_interior":
                btnMods["btn_novaras_bordello_mainhall_to_office"] = BtnChangeLoc(STR_LOC.NOV_BORDELLO_OFFICE, "novaras_bordello_office")
            return LocButtonMod(directMods = btnMods)

    ## loc itself
    WorldLocation("novaras_bordello_office", STR_LOC.NOV_BORDELLO_OFFICE, "bg_weeping_heart_brothel_office", parent = "novaras_bordello_interior", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_bordello_office"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_novaras_bordello_office_to_mainhall", BtnChangeLoc(STR_LOC.NOV_BORDELLO, "novaras_bordello_interior"))
    LocDef.withBtn("btn_talk_carina_office", BtnDisabled())

    # music
    LocDef.withNightMusic("audio/music/24_Brothel.ogg")
    LocDef.withDayMusic("audio/music/24_Brothel.ogg")
    # vfx
    vfxLibLights["novaras_bordello_office_night"] = {
        "lightpost_small":[(192, 240), (1861, 233)],
        "lightpost_big":[(1250, 311), (752, 400), (672, 482)]
        }
    LocDef.SetDayNightMatrixClass(MxDayNight)
    # sfx
    LocDef.withActionSFXs({"btn_novaras_bordello_office_to_mainhall": soundLib["woodenDoor"]})


########################################################################################################
########################################################################################################
################ dungeon
    # door only, enabled by NovarasSexDungeon
    @AppendToAllQuests
    class DoorNovarasSexDungeon(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_bordello_interior":
                btnMods["btn_novaras_bordello_mainhall_to_dungeon"] = BtnChangeLoc(STR_LOC.NOV_BORDELLO_DUNGEON, "novaras_bordello_sex_dungeon")
            return LocButtonMod(directMods = btnMods)

    ## loc itself
    WorldLocation("novaras_bordello_sex_dungeon", STR_LOC.NOV_BORDELLO_DUNGEON, "bg_weeping_heart_brothel_sex_dungeon", parent = "novaras_bordello_interior", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_bordello_sex_dungeon"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_novaras_bordello_dungeon_to_mainhall", BtnChangeLoc(STR_LOC.NOV_BORDELLO, "novaras_bordello_interior"))
    LocDef.withBtn("btn_novaras_bordello_dungeon_summon", BtnDisabled())

    # music
    LocDef.withNightMusic("audio/music/24_Brothel.ogg")
    LocDef.withDayMusic("audio/music/24_Brothel.ogg")
    # vfx
    vfxLibLights["novaras_bordello_sex_dungeon_night"] = {
        "lightpost_small":[(368, 49), (445, 54), (554, 77), (589, 97)],
        "lightpost_big":[(1489, 216), (1599, 195), (1693, 191), (1757, 168), (1820, 183), (1881, 162)]
        }
    vfxLibLights["novaras_bordello_sex_dungeon"] = {
        "lightpost_small":[(368, 49), (445, 54), (554, 77), (589, 97)],
        "lightpost_big":[(1489, 216), (1599, 195), (1693, 191), (1757, 168), (1820, 183), (1881, 162)]
        }
    # sfx
    LocDef.withActionSFXs({"btn_novaras_bordello_dungeon_to_mainhall": soundLib["woodenDoor"]})


screen loc_novaras_bordello_interior():
    default locTag = "novaras_bordello_interior"

    # exit
    use locShared_toCityBtn(locTag, "novaras_bordello_interior_leave")
    # chars
    use locBtn_Char(locTag,"helena_talk_btn",
        "helena", "helena",
        Transform(anchor = (0.5, 0.5), pos = (0.25, 0.5)))
    use locBtn_Char(locTag, "btn_talk_arwen",
        "arwen", "arwen",
        Transform(anchor = (0.5, 0.5), pos = (0.68, 0.6), xzoom = -1.0, zoom = 0.85))
    use locBtn_Char(locTag, "dros_bordello_talk_btn",
        "dros", "dros",
        Transform(anchor = (0.5, 0.5), pos = (0.9, 0.55), zoom = 0.75, xzoom = -1.0))
    # to office
    use locBtn_basic(locTag, "btn_novaras_bordello_mainhall_to_office",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.8, 0.3)),
        key = config.keymap["nav_right"])
    use locBtn_basic(locTag, "btn_novaras_bordello_mainhall_to_dungeon",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.131, 0.328)),
        key = config.keymap["nav_left"])
    add "novaras_bordello_overlay"

screen loc_novaras_bordello_office():
    default locTag = "novaras_bordello_office"

    # exit
    use locBtn_basic(locTag, "btn_novaras_bordello_office_to_mainhall",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.829, 0.405)),
        key = config.keymap["nav_right"])

    # carina
    use locBtn_Char(locTag, "btn_talk_carina_office", 
        "carina", "carina", 
        Transform(anchor = (0.5, 0.5), pos = (0.3, 0.44), zoom = 0.40))

screen loc_novaras_bordello_sex_dungeon():
    default locTag = "novaras_bordello_sex_dungeon"

    # exit
    use locBtn_basic(locTag, "btn_novaras_bordello_dungeon_to_mainhall",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.268, 0.38)),
        key = config.keymap["nav_left"])
    use locBtn_basic(locTag, "btn_novaras_bordello_dungeon_summon",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.66, 0.823)))
