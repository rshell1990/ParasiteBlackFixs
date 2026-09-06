#### palace gates #
image palace_gates_t = "images/world_interact/novaras_city/novh_palace.webp"
image palace_gates_h:
    "palace_gates_t"
    matrixcolor MxMapHover()

init python:
    WorldLocation("novaras_dist_centre", STR_LOC.NOV_DIST_CENTRE, "bg_nov_district_centre", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_dist_centre"]
    # bridges
    LocDef.withBtn("bridge_novaras_centre_to_farm", 
        BtnChangeLoc(STR_LOC.NOV_DIST_FARM, "novaras_dist_farm"))
    LocDef.withBtn("bridge_novaras_centre_to_army", 
        BtnChangeLoc(STR_LOC.NOV_DIST_ARMY, "novaras_dist_army"))
    LocDef.withBtn("bridge_novaras_centre_to_house", 
        BtnChangeLoc(STR_LOC.NOV_DIST_HOUSE, "novaras_dist_house"))
    LocDef.withBtn("bridge_novaras_centre_to_pleasure", 
        BtnChangeLoc(STR_LOC.NOV_DIST_PLEASURE, "novaras_dist_pleasure"))
    # clickables
    LocDef.withBtn("btn_nov_palace_gates", BtnDisabled())
    # shared event clickable
    LocDef.withBtn("btn_shared_clickable_event_centre", BtnDisabled())
    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # vfx
    vfxLibLights["novaras_dist_centre_night"] = {
        "light_crystal_red":[(707, 76), (492, 303), (549, 484), (1215, 550), (1429, 320), (1341, 170)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

    @AppendToAllQuests
    class HouseLockNovPalace(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_centre":
                btnMods["btn_nov_palace_gates"] = BtnJumpLabel(
                    STR_LOC.NOV_ROYAL_PALACE, "lockedLines_novaras_palace_guards")
            return LocButtonMod(directMods = btnMods)

label lockedLines_novaras_palace_guards:
    "As I approached the Royal Palace, a couple of guards blocked my path."
    show cg_guard at left
    show cg_guard at right_f as guard2
    with dissolve
    show cg_guard at shake
    GUARD "Halt!"
    GUARD "State your business at the Royal Palace, citizen."
    MC "I... don't really have any."
    "The other guard asked, in a surprisingly friendly tone:"
    GUARD "Sightseeing, eh?"
    show cg_guard at shake as guard2
    GUARD "Move on."
    $ LocFlush(dissolve)
    "The guards clanged their way back to the immense gate."
    MC "Well, guess I'm not entering that place."
    $ LocEnterQ()

screen loc_novaras_dist_centre():
    default locTag = "novaras_dist_centre"
    # bridges
    use locBtn_sprite(locTag, "bridge_novaras_centre_to_farm",
        "novaras_bridge_centre_north_t", "novaras_bridge_centre_north_h",
        Transform(anchor = (0.5, 0.0), pos = (0.484, 0.0)), 
        key = config.keymap["nav_up"])
    use locBtn_sprite(locTag, "bridge_novaras_centre_to_house",
        "novaras_bridge_centre_east_t", "novaras_bridge_centre_east_h",
        Transform(anchor = (1.0, 0.5), pos = (1.0, 0.507)),
        key = config.keymap["nav_right"])
    use locBtn_sprite(locTag, "bridge_novaras_centre_to_army",
        "novaras_bridge_centre_south_t", "novaras_bridge_centre_south_h",
        Transform(anchor = (0.5, 1.0), pos = (0.4835, 1.0)), 
        key = config.keymap["nav_down"])
    use locBtn_sprite(locTag, "bridge_novaras_centre_to_pleasure",
        "novaras_bridge_centre_west_t", "novaras_bridge_centre_west_h",
        Transform(anchor = (0.0, 0.5), pos = (0.0, 0.45)), 
        key = config.keymap["nav_left"])

    use locBtn_sprite(locTag, "btn_nov_palace_gates",
        "palace_gates_t", "palace_gates_h",
        Transform(anchor = (0.5, 1.0), pos = (953, 849)))

    use locBtn_basic(locTag, "btn_shared_clickable_event_centre",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.358, 0.746)))


################################################
init python:
    # WARNING: stub
    WorldLocation("novaras_royal_palace", STR_LOC.NOV_ROYAL_PALACE, "black", parent = "novaras_dist_centre", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_royal_palace"]

    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/4_Royal_T.ogg")
    LocDef.withNightMusic("audio/music/4_Royal_T.ogg")

    LocDef.withBtn("btn_tocity_novaras_royal_palace", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))

screen loc_novaras_royal_palace():
    default locTag = "novaras_royal_palace"
    use locShared_toCityBtn(locTag, "btn_tocity_novaras_royal_palace")
