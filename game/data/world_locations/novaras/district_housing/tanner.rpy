init python:
    WorldLocation("novaras_tanner_shop", STR_LOC.NOV_TANNER_SHOP, "bg_tanner_shop", parent = "novaras_dist_house", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_tanner_shop"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_tanner_shop_toCity", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("btn_tanner_shop_to_bedroom", BtnChangeLoc(STR_NAV.TO_BEDROOM, "novaras_tanner_shop_bedroom"))
    LocDef.withBtn("btn_talk_mrs_winward", BtnDisabled())
    LocDef.withBtn("btn_talk_mr_winward", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")

    # vfx
    vfxLibLights["novaras_tanner_shop_night"] = {
        "lightpost_huge":[(377, 211), (1756, 255)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

    # action sfx
    LocDef.withActionSFXs({
        "btn_tanner_shop_toCity": soundLib["woodenDoor"],
        "btn_tanner_shop_to_bedroom": soundLib["woodenDoor"]})
    
    # engaged by finishing prologue I guess?
    @AppendToAllQuests
    class HouseLockTannerShop(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_house":
                if IsDaytime() or RomanceWinward().CanEnterHouseAtNight:
                    btnMods["btn_tanner_shop"] = BtnChangeLoc(STR_LOC.NOV_TANNER_SHOP, "novaras_tanner_shop")
                else:
                    btnMods["btn_tanner_shop"] = BtnJumpLabel(STR_LOC.NOV_TANNER_SHOP, "HouseLockLines")

            return LocButtonMod(directMods = btnMods)

screen loc_novaras_tanner_shop():
    default locTag = "novaras_tanner_shop"

    # exit button
    use locShared_toCityBtn(locTag, "btn_tanner_shop_toCity")

    # to bedroom
    use locBtn_basic(locTag, "btn_tanner_shop_to_bedroom",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.9, 0.5)), 
        key = config.keymap["nav_right"])

    # winward
    use locBtn_Char(locTag, "btn_talk_mrs_winward",
        "mrs_winward", "mrs_winward",
        Transform(anchor = (0.5, 0.5), pos = (0.75, 0.65), xzoom = -1.0))

    # mr winward (invest)
    use locBtn_Char(locTag, "btn_talk_mr_winward",
        "mr_winward", "mr_winward",
        Transform(anchor = (0.5, 0.5), pos = (0.25, 0.65)))

init python:
    WorldLocation("novaras_tanner_shop_bedroom", STR_LOC.NOV_TANNER_SHOP, "bg_tanner_shop_bedroom", parent = "novaras_tanner_shop", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_tanner_shop_bedroom"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_tanner_shop_to_main", BtnChangeLoc(STR_NAV.LEAVE, "novaras_tanner_shop"))

    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")

    # vfx
    vfxLibLights["novaras_tanner_shop_bedroom_night"] = {
        "lightpost_big":[(300, 271), (1646, 222), (1392, 353)],
        "lightpost_huge":[(998, 63)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

    # action sfx
    LocDef.withActionSFXs({"btn_tanner_shop_to_main": soundLib["woodenDoor"]})

screen loc_novaras_tanner_shop_bedroom():
    default locTag = "novaras_tanner_shop_bedroom"

    use locBtn_basic(locTag, "btn_tanner_shop_to_main",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.53, 0.45)), 
        key = config.keymap["nav_up"])