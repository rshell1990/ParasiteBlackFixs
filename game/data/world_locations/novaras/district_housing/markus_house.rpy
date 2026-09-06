############# 'living room' or sth like that
init python:
    WorldLocation("markus_house_livingroom", STR_LOC.NOV_MARKUS_HOUSE, "bg_markus_house_livingroom", parent = "novaras_dist_house", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["markus_house_livingroom"]
    LocDef.withBtn("markus_house_livingroom_toCity", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({
        "markus_house_livingroom_toCity": soundLib["woodenDoor"],
        "btn_markus_house_livingroom_to_bedroom": soundLib["woodenDoor"]})
    # to bedroom
    LocDef.withBtn("btn_markus_house_livingroom_to_bedroom", BtnChangeLoc(STR_NAV.TO_BEDROOM, "markus_house_bedroom"))
    # VFX
    vfxLibLights["markus_house_livingroom_night"] = {
        "lightpost_huge":[(390, 582)], "lightpost_big":[(682, 459), (1199, 714)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)
    
    @AppendToAllQuests
    class HouseLockMarkusHouse(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_house":
                if CharInParty("markus") or IsDaytime():
                    btnMods["btn_markus_house"] = BtnChangeLoc(STR_LOC.NOV_MARKUS_HOUSE, "markus_house_livingroom")
                else:
                    btnMods["btn_markus_house"] = BtnJumpLabel(STR_LOC.NOV_MARKUS_HOUSE, "HouseLockLines")
            return LocButtonMod(directMods = btnMods)

screen loc_markus_house_livingroom():
    default locTag = "markus_house_livingroom"

    # exit button
    use locShared_toCityBtn(locTag, "markus_house_livingroom_toCity")

    # to bedroom
    use locBtn_basic(locTag, "btn_markus_house_livingroom_to_bedroom", "images/gui/buttons_loc/door.webp", Transform(pos = (0.08, 0.58)), key = config.keymap["nav_left"])

############# bedroom 
init python:
    WorldLocation("markus_house_bedroom", STR_LOC.NOV_MARKUS_HOUSE_BEDROOM, "bg_markus_bedroom", parent = "markus_house_livingroom", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["markus_house_bedroom"]
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({
        "btn_markus_house_bedroom_to_livingroom": soundLib["woodenDoor"]})
    # VFX
    vfxLibLights["markus_house_bedroom_night"] = {
        "lightpost_big":[(290, 355)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)
    # to living room
    LocDef.withBtn("btn_markus_house_bedroom_to_livingroom", BtnChangeLoc(STR_NAV.TO_LIVING_ROOM, "markus_house_livingroom"))

screen loc_markus_house_bedroom():
    default locTag = "markus_house_bedroom"

    # to living room
    use locBtn_basic(locTag, "btn_markus_house_bedroom_to_livingroom", "images/gui/buttons_loc/door.webp", Transform(pos = (0.9, 0.46)), key = config.keymap["nav_right"])