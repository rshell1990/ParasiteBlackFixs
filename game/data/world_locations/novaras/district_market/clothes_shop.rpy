init python:
    WorldLocation("novaras_clothes_int", STR_LOC.NOV_CLOTHES_STORE, "bg_clothes_shop_off", parent = "novaras_dist_market", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_clothes_int"]
    LocDef.CanWait = False

    LocDef.withBtn("novaras_clothes_int_toCity", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("talkdros", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"novaras_clothes_int_toCity": soundLib["woodenDoor"]})


    @AppendToAllQuests
    class HouseLockNovarasClothesStore(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_market":
                if IsDaytime():
                    btnMods["btn_novaras_clothes"] = BtnChangeLoc(STR_LOC.NOV_CLOTHES_STORE, "novaras_clothes_int")
                else:
                    btnMods["btn_novaras_clothes"] = BtnJumpLabel(STR_LOC.NOV_CLOTHES_STORE, "HouseLockLines")
            return LocButtonMod(directMods = btnMods)

screen loc_novaras_clothes_int():
    default locTag = "novaras_clothes_int"
    use locShared_toCityBtn(locTag, "novaras_clothes_int_toCity")
    if IsDaytime():
        use locBtn_Char(locTag, "talkdros",
            "dros", "dros",
            Transform(anchor = (0.5, 1.0), pos = (0.68, 0.75), xzoom = -1.0, zoom = 0.5))
