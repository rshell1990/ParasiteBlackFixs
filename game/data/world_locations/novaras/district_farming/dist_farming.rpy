image blacksmith_t = "images/world_interact/novaras_city/novh_blacksmith.webp"
image blacksmith_h:
    "blacksmith_t"
    matrixcolor MxMapHover()

init python:
    WorldLocation("novaras_dist_farm", STR_LOC.NOV_DIST_FARM, "bg_nov_district_farmland", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_dist_farm"]
    # bridges
    LocDef.withBtn("bridge_novaras_farm_to_edu",
        BtnChangeLoc(STR_LOC.NOV_DIST_EDU, "novaras_dist_edu"))
    LocDef.withBtn("bridge_novaras_farm_to_centre",
        BtnChangeLoc(STR_LOC.NOV_DIST_CENTRE, "novaras_dist_centre"))
    LocDef.withBtn("bridge_novaras_farm_to_mage",
        BtnChangeLoc(STR_LOC.NOV_DIST_MAGE, "novaras_dist_mage"))
    # houses
    LocDef.withBtn("btn_novaras_blacksmith", BtnChangeLoc(STR_LOC.NOV_BLACKSMITH, "novaras_blacksmith"))
    # shared event clickable
    LocDef.withBtn("btn_shared_clickable_event_farm", BtnDisabled())

    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_novaras_blacksmith": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_dist_farm_night"] = {"lightpost_small":[(786, 361)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

    @AppendToAllQuests
    class HouseLockNovarasSmithy(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_farm":
                if IsDaytime():
                    btnMods["btn_novaras_blacksmith"] = BtnChangeLoc(STR_LOC.NOV_BLACKSMITH, "novaras_blacksmith")
                else:
                    btnMods["btn_novaras_blacksmith"] = BtnJumpLabel(STR_LOC.NOV_BLACKSMITH, "HouseLockLines")
            return LocButtonMod(directMods = btnMods)

screen loc_novaras_dist_farm():
    default locTag = "novaras_dist_farm"
    # bridges
    use locBtn_sprite(locTag, "bridge_novaras_farm_to_centre",
        "novaras_bridge_farmland_south_t", "novaras_bridge_farmland_south_h",
        Transform(anchor = (0.5, 1.0), pos = (0.49, 1.0)), 
        key = config.keymap["nav_down"])
    use locBtn_sprite(locTag, "bridge_novaras_farm_to_edu",
        "novaras_bridge_farmland_west_t", "novaras_bridge_farmland_west_h",
        Transform(anchor = (0.0, 0.5), pos = (0.0, 0.529)), 
        key = config.keymap["nav_left"])
    use locBtn_sprite(locTag, "bridge_novaras_farm_to_mage",
        "novaras_bridge_farmland_east_t", "novaras_bridge_farmland_east_h",
        Transform(anchor = (1.0, 0.5), pos = (1.0, 0.542)), 
        key = config.keymap["nav_right"])
    # houses
    use locBtn_sprite(locTag, "btn_novaras_blacksmith",
        "blacksmith_t", "blacksmith_h",
        Transform(anchor = (0.0, 0.0), pos = (714, 244)))

    use locBtn_basic(locTag, "btn_shared_clickable_event_farm",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.719, 0.33)))

