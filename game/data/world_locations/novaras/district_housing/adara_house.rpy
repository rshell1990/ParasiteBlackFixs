init python:
    @AppendToAllQuests
    class HouseLockAdara(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_house":
                if IsDaytime():
                    btnMods["btn_adara_house"] = BtnChangeLoc(STR_LOC.NOV_ADARA_HOUSE, "adara_house_living_room")
                else:
                    btnMods["btn_adara_house"] = BtnJumpLabel(STR_LOC.NOV_ADARA_HOUSE, "HouseLockLines")
            return LocButtonMod(directMods = btnMods)

    WorldLocation("adara_house_living_room", STR_LOC.NOV_ADARA_HOUSE_LIV, "bg_adara_living_room", parent = "novaras_dist_house", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["adara_house_living_room"]
    LocDef.withBtn("btn_adara_house_living_room_toCity", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("btn_adara_house_living_room_to_bedroom", 
        BtnChangeLoc(STR_NAV.TO_BEDROOM, "adara_house_bedroom"))
    # chars
    LocDef.withBtn("btn_talk_gerard", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({
        "btn_adara_house_living_room_toCity":       soundLib["woodenDoor"],
        "btn_adara_house_living_room_to_bedroom":   soundLib["woodenDoor"],
        })
    # VFX
    vfxLibLights["adara_house_living_room_night"] = {
        "lightpost_big":  [(747, 110), (777, 97), (854, 85), (913, 86), (976, 91), (1020, 107)],
        "lightpost_huge": [(1477, 638)],
    }
    LocDef.SetDayNightMatrixClass(MxDayNight)


    WorldLocation("adara_house_bedroom", STR_LOC.NOV_ADARA_HOUSE_BED, "bg_adara_bedroom", parent = "novaras_dist_house", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["adara_house_bedroom"]
    LocDef.withBtn("btn_adara_house_bedroom_to_living_room", 
        BtnChangeLoc(STR_NAV.TO_LIVING_ROOM, "adara_house_living_room"))
    # chars
    LocDef.withBtn("btn_talk_adara", BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_adara_house_bedroom_to_living_room": soundLib["woodenDoor"]})
    # VFX
    vfxLibLights["adara_house_bedroom_night"] = {
        "lightpost_big":  [(963, 181), (867, 198), (773, 235), (734, 250)],
    }
    LocDef.SetDayNightMatrixClass(MxDayNight)
    
    
screen loc_adara_house_living_room():
    default locTag = "adara_house_living_room"

    use locBtn_basic(locTag, "btn_adara_house_living_room_to_bedroom",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.27, 0.19)), 
        key = config.keymap["nav_left"])

    use locBtn_Char(locTag, "btn_talk_gerard",
        "gerard sleep", "gerard sleep", Transform(zoom = 0.6, pos = (0.6, 0.5)))

    # exit button
    #use locShared_toCityBtn(locTag, "btn_adara_house_living_room_toCity")
    use locBtn_basic(locTag, "btn_adara_house_living_room_toCity",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.93, 0.37)), 
        key = config.keymap["nav_right"])

    
screen loc_adara_house_bedroom():
    default locTag = "adara_house_bedroom"

    use locBtn_basic(locTag, "btn_adara_house_bedroom_to_living_room",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.7, 0.5)), 
        key = config.keymap["nav_right"])

    use locBtn_Char(locTag, "btn_talk_adara",
        "adara", "adara", Transform(pos = (0.3, 0.65), zoom = 0.9))