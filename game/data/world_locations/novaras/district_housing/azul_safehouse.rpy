init python:
    @AppendToAllQuests
    class HouseLockAzul(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_house":
                if QstIsComplete(QstRavenousJelly):
                    btnMods["btn_azul_safehouse"] = BtnChangeLoc(STR_LOC.NOV_MYU_HIDEOUT, "azul_safehouse")
                else:
                    btnMods["btn_azul_safehouse"] = BtnChangeLoc(STR_LOC.NOV_AZUL_SH, "azul_safehouse")
            return LocButtonMod(directMods=btnMods)

    WorldLocation("azul_safehouse", STR_LOC.NOV_AZUL_SH, "bg_azul_room_clean", parent = "novaras_dist_house", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["azul_safehouse"]
    LocDef.withBtn("azul_safehouse_toCity", 
        BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("btn_azul_to_bedroom", 
        BtnChangeLoc(STR_NAV.TO_BEDROOM, "azul_safehouse_bedroom"))
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"azul_safehouse_toCity": soundLib["woodenDoor"]})
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_azul_safehouse():
    default locTag = "azul_safehouse"
    # exit button
    use locShared_toCityBtn(locTag, "azul_safehouse_toCity")
    use locBtn_basic(locTag, "btn_azul_to_bedroom",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.9, 0.5)), 
        key = config.keymap["nav_right"])
    use locBtn_basic(locTag, "btn_azul_to_basement",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.6)), 
        key = config.keymap["nav_up"])
    use locBtn_basic(locTag, "btn_azul_fireplace",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.2, 0.65)))
    use locBtn_basic(locTag, "btn_azul_rug",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.58, 0.68)))