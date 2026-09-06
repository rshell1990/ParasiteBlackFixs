init python:
    WorldLocation("novaras_gates", STR_LOC.NOV_GATES, "bg_citywall", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_gates"]
    LocDef.withBtn("btn_novaras_gates_enter_city",  BtnChangeLoc(STR_NAV.ENTER_CITY, "novaras_dist_army"))
    LocDef.withBtn("btn_twoEmperorsTalkMarkus", BtnDisabled())
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    # vfx
    vfxLibLights["novaras_gates_night"] = {
        "lightpost_huge":[(70, 575)], "lightpost_big":[(848, 703)],
        "lightpost_small":[(575, 704), (628, 104), (738, 133)]}
    # travel
    LocDef.withBtn("novaras_gates_travel", BtnTravel())
    LocDef.withWorldMap(STR_LOC.NOV_CITY,
        ["valley_of_death", "lake_balun", "lake_peacing"],
        "images/world_map/novaras_city.webp", (1265, 821))
    # sfx
    LocDef.withActionSFXs({"btn_novaras_gates_enter_city": "audio/interactables/gate_drop.ogg"})
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_gates():
    default locTag = "novaras_gates"

    use locBtn_basic(locTag, "btn_novaras_gates_enter_city",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.155, 0.52)), 
        key = config.keymap["nav_left"])

    use locBtn_basic(locTag, "novaras_gates_travel",
        "images/gui/buttons_loc/travel.webp",
        Transform(pos = (0.85, 0.6)), 
        key = config.keymap["nav_right"])

    use locBtn_sprite(locTag, "btn_twoEmperorsTalkMarkus",
        "markus", "markus",
        Transform(anchor = (0.5, 0.5), pos = (0.65, 0.8), zoom = 0.2), NightTint = True)
