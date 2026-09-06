image novaras_palam_t = "images/world_interact/novaras_city/novh_palam_tower.webp"
image novaras_palam_h:
    "novaras_palam_t"
    matrixcolor MxMapHover()

init python:
    # this allows tower to be locked/unlocked at diff times of day
    @AppendToAllQuests
    class HouseLockPalamTower(LogicModule):
        def __init__(self):
            super().__init__()

            self.CanEnterAtNight = False # toggled true by helping out Divine deal with the frog monster
            self.EnteredAtNightOnce = False # toggled true by talking to a guard, if true - clicking tower at night just enters it, bypassing dialogue

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_mage":
                if IsDaytime():
                    btnMods["btn_novaras_palam_mainhall_door"] = BtnChangeLoc(STR_LOC.NOV_PALAM, "novaras_palam_mainhall")
                else:
                    if self.EnteredAtNightOnce:
                        btnMods["btn_novaras_palam_mainhall_door"] = BtnChangeLoc(STR_LOC.NOV_PALAM, "novaras_palam_mainhall")
                    else:
                        btnMods["btn_novaras_palam_mainhall_door"] = BtnJumpLabel(STR_LOC.NOV_PALAM, "novaras_palam_tower_guard")
            return LocButtonMod(directMods=btnMods)

label novaras_palam_tower_guard:
    show cg_guard at right_f
    if QstIsActive(QstTerminus):
        show mcprologue at left with easeinleft
    else:
        show mc at left with easeinleft
    GUARD "You are not allowed to enter the tower at night, citizen."
    menu:
        "I'm here on business with Sister Divine." if (QstIsActive(QstLittleLies) or QstIsComplete(QstLittleLies)):
            GUARD "Ah, yes… She did mention we should make exception for you."
            GUARD "You may enter… But be on your best behaviour!"
            GUARD "This is a sacred place!"
            hide mc with easeoutright
            $ LocSet("novaras_palam_mainhall")
            $ LocEnter()

        "Show the stone Sister Divine gave you." if HouseLockPalamTower().CanEnterAtNight:
            "The guard saw the stone and nodded."
            $ HouseLockPalamTower().EnteredAtNightOnce = True
            show cg_guard at nod
            GUARD "Alright, you can enter."
            hide mc with easeoutright
            $ LocSet("novaras_palam_mainhall")
            $ LocEnter()
        "Can I enter?":
            show cg_guard at shake
            GUARD "Are you deaf, citizen?"
            GUARD "You are not allowed inside the tower at night."
            GUARD "Get lost."
            MC "Uh. Okay."
            $ LocEnter()
        "Leave.":
            MC "I should go."
            GUARD "Exactly."
            $ LocEnter()

init python:
    WorldLocation("novaras_dist_mage", STR_LOC.NOV_DIST_MAGE, "bg_nov_district_mage", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_dist_mage"]
    # bridges
    LocDef.withBtn("bridge_novaras_mage_to_farm",
        BtnChangeLoc(STR_LOC.NOV_DIST_FARM, "novaras_dist_farm"))
    LocDef.withBtn("bridge_novaras_mage_to_house",
        BtnChangeLoc(STR_LOC.NOV_DIST_HOUSE, "novaras_dist_house"))
    # houses
    LocDef.withBtn("btn_novaras_palam_mainhall_door",
        BtnChangeLoc(STR_LOC.NOV_PALAM, "novaras_palam_mainhall"))
    # dealer
    LocDef.withBtn("btn_novaras_mage_dist_dealer",     BtnDisabled())
    # shared event clickable
    LocDef.withBtn("btn_shared_clickable_event_mage",  BtnDisabled())

    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_novaras_palam_mainhall_door": soundLib["woodenDoor"]})
    # vfx
    vfxLibLights["novaras_dist_mage_night"] = {
        "light_crystal_red":    [(1573, 0)],
        "light_crystal_green":  [(1611, 684)],
        "light_crystal_blue":   [(444,  693)],
        "light_crystal_yellow": [(421,  12)]}
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_novaras_dist_mage():
    default locTag = "novaras_dist_mage"
    # bridges
    use locBtn_sprite(locTag, "bridge_novaras_mage_to_house",
        "novaras_bridge_mage_south_t", "novaras_bridge_mage_south_h",
        Transform(anchor = (0.5, 1.0), pos = (0.489, 1.0)), 
        key = config.keymap["nav_down"])

    use locBtn_sprite(locTag, "bridge_novaras_mage_to_farm",
        "novaras_bridge_mage_west_t", "novaras_bridge_mage_west_h",
        Transform(anchor = (0.0, 0.5), pos = (0.0, 0.5417)), 
        key = config.keymap["nav_left"])
    # houses
    use locBtn_sprite(locTag, "btn_novaras_palam_mainhall_door",
        "novaras_palam_t", "novaras_palam_h",
        Transform(anchor = (0.0, 0.0), pos = (316, 621)))

    # carina's dealer
    use locBtn_basic(locTag, "btn_novaras_mage_dist_dealer",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.75, 0.85)))

    use locBtn_basic(locTag, "btn_shared_clickable_event_mage",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.641, 0.469)))

