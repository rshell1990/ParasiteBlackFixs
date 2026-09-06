init python:
    WorldLocation("novaras_store_int", STR_LOC.NOV_GENERAL_STORE, "bg_novaras_general_store", parent = "novaras_dist_market", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_store_int"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_novaras_store_int_toCity", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("talkNovarasStorekeep", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/25_Shopkeep.ogg")
    LocDef.withNightMusic("audio/music/25_Shopkeep.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_novaras_store_int_toCity": soundLib["woodenDoor"]})
    # vfx
    LocDef.SetDayNightMatrixClass(MxDayNight)

    @AppendToAllQuests
    class HouseLockNovarasGeneralStore(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_market":
                if IsDaytime():
                    btnMods["btn_novaras_store_int"] = BtnChangeLoc(STR_LOC.NOV_GENERAL_STORE, "novaras_store_int")
                else:
                    btnMods["btn_novaras_store_int"] = BtnJumpLabel(STR_LOC.NOV_GENERAL_STORE, "HouseLockLines")
            return LocButtonMod(directMods = btnMods)

screen loc_novaras_store_int():
    default locTag = "novaras_store_int"
    use locShared_toCityBtn(locTag, "btn_novaras_store_int_toCity")
    if IsDaytime():
        use locBtn_Char(locTag,"talkNovarasStorekeep",
            "luciusmal", "luciusmal",
            Transform(anchor = (0.5, 0.5), pos = (0.4, 0.4), zoom = 0.5))
        add "bg_novaras_general_store_over":
            matrixcolor wLocs[locTag].DayNightMatrixClass(GetDaytimeTintFactor())
