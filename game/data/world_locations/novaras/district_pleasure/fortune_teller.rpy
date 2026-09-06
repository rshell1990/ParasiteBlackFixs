init python:
    WorldLocation("novaras_soothsayer_cabin", STR_LOC.NOV_WITCH_HOUSE, "cg_nov_witch", parent = "novaras_dist_pleasure", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_soothsayer_cabin"]
    LocDef.CanWait = False

    LocDef.withBtn("btn_novaras_soothsayer_cabin_toCity", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("btn_novaras_talk_to_babazhul", BtnDisabled())
    # music
    LocDef.withNightMusic("audio/music/32_Mind_of_Mysteries.ogg")
    LocDef.withDayMusic("audio/music/32_Mind_of_Mysteries.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_novaras_soothsayer_cabin_toCity": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_soothsayer_cabin_night"] = {"lightpost_huge":[(1384, 498)]}
    vfxLibLights["novaras_soothsayer_cabin"] = {"lightpost_huge":[(1384, 498)]}


screen loc_novaras_soothsayer_cabin():
    default locTag = "novaras_soothsayer_cabin"

    use locShared_toCityBtn(locTag, "btn_novaras_soothsayer_cabin_toCity")

    use locBtn_basic(locTag, "btn_novaras_talk_to_babazhul",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.5, 0.5)))

    add "babazhul_blink_cond":
        pos (0.0, 0.0)
