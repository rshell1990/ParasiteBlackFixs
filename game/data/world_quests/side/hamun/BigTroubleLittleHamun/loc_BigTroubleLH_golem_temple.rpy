####### bridge area
init python:
    # theres three rooms: bridge, dials (left) and pods (right)
    WorldLocation("qst_bigtrouble_temple_bridge", _("The Temple of Arakan"), "bg_arakan_temple_bridge")
    LocDef = wLocs["qst_bigtrouble_temple_bridge"]
    # music
    LocDef.withDayMusic("audio/music/15_Experiments.ogg")
    LocDef.withNightMusic("audio/music/15_Experiments.ogg")
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/cave.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/cave.ogg")
    # btns
    LocDef.withBtn("btn_bigtrouble_temple_bridge", BtnJumpLabel(_("The bridge"), "qst_BigTroubleLHamun_temple_bridge_cantcross"))
    LocDef.withBtn("btn_bigtrouble_temple_bridge_to_dials", BtnChangeLoc(_("Go left"), "qst_bigtrouble_temple_dials"))
    LocDef.withBtn("btn_bigtrouble_temple_bridge_to_pods", BtnChangeLoc(_("Go right"), "qst_bigtrouble_temple_pods"))


screen loc_qst_bigtrouble_temple_bridge():
    default locTag = "qst_bigtrouble_temple_bridge"

    use locBtn_basic(locTag, "btn_bigtrouble_temple_bridge_to_dials", "images/gui/buttons_loc/arrow_l.webp", Transform(pos = (0.067, 0.64)), key = config.keymap["nav_left"])
    use locBtn_basic(locTag, "btn_bigtrouble_temple_bridge_to_pods", "images/gui/buttons_loc/arrow_r.webp", Transform(pos = (0.942, 0.609)), key = config.keymap["nav_right"])
    use locBtn_basic(locTag, "btn_bigtrouble_temple_bridge", "images/gui/buttons_loc/question.webp", Transform(pos = (0.52, 0.42)), key = config.keymap["nav_up"])



####### dials area
init python:
    WorldLocation("qst_bigtrouble_temple_dials", _("The Temple of Arakan, sacrificial chamber"), "bg_arakan_temple_dials")
    LocDef = wLocs["qst_bigtrouble_temple_dials"]
    # music
    LocDef.withDayMusic("audio/music/15_Experiments.ogg")
    LocDef.withNightMusic("audio/music/15_Experiments.ogg")
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/cave.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/cave.ogg")
    # btns
    LocDef.withBtn("btn_bigtrouble_temple_dials_to_bridge", BtnChangeLoc(_("To bridge"), "qst_bigtrouble_temple_bridge"))
    LocDef.withBtn("btn_bigtrouble_temple_dials", BtnJumpLabel(_("An altar"), "qst_BigTroubleLHamun_dial_altar"))
    # shrines
    LocDef.withBtn("btn_bigtrouble_temple_dials_shrine_1", BtnJumpLabel(_("Jester shrine"), "qst_BigTroubleLHamun_temple_dials_shrines_1"))
    LocDef.withBtn("btn_bigtrouble_temple_dials_shrine_2", BtnJumpLabel(_("Crowned shrine"), "qst_BigTroubleLHamun_temple_dials_shrines_2"))
    LocDef.withBtn("btn_bigtrouble_temple_dials_shrine_3", BtnJumpLabel(_("Weeping shrine"), "qst_BigTroubleLHamun_temple_dials_shrines_3"))
    LocDef.withBtn("btn_bigtrouble_temple_dials_shrine_4", BtnJumpLabel(_("Sleeping shrine"), "qst_BigTroubleLHamun_temple_dials_shrines_4"))
    LocDef.withBtn("btn_bigtrouble_temple_dials_shrine_5", BtnJumpLabel(_("Sea shrine"), "qst_BigTroubleLHamun_temple_dials_shrines_5"))
    LocDef.withBtn("btn_bigtrouble_temple_dials_shrine_6", BtnJumpLabel(_("Wolf shrine"), "qst_BigTroubleLHamun_temple_dials_shrines_6"))

screen loc_qst_bigtrouble_temple_dials():
    default locTag = "qst_bigtrouble_temple_dials"

    use locBtn_basic(locTag, "btn_bigtrouble_temple_dials_to_bridge", "images/gui/buttons_loc/arrow_d.webp", Transform(pos = (0.62, 0.88)), key = config.keymap["nav_down"])
    
    # shrines
    use locBtn_basic(locTag, "btn_bigtrouble_temple_dials_shrine_1", "images/gui/buttons_loc/question.webp", Transform(pos = (0.085, 0.665)))
    use locBtn_basic(locTag, "btn_bigtrouble_temple_dials_shrine_2", "images/gui/buttons_loc/question.webp", Transform(pos = (0.211, 0.642)))
    use locBtn_basic(locTag, "btn_bigtrouble_temple_dials_shrine_3", "images/gui/buttons_loc/question.webp", Transform(pos = (0.303, 0.633)))
    use locBtn_basic(locTag, "btn_bigtrouble_temple_dials_shrine_4", "images/gui/buttons_loc/question.webp", Transform(pos = (0.691, 0.627)))
    use locBtn_basic(locTag, "btn_bigtrouble_temple_dials_shrine_5", "images/gui/buttons_loc/question.webp", Transform(pos = (0.772, 0.631)))
    use locBtn_basic(locTag, "btn_bigtrouble_temple_dials_shrine_6", "images/gui/buttons_loc/question.webp", Transform(pos = (0.908, 0.642)))
    
    use locBtn_basic(locTag, "btn_bigtrouble_temple_dials", "images/gui/buttons_loc/question.webp", Transform(pos = (0.496, 0.681)))



####### pods area
init python:
    WorldLocation("qst_bigtrouble_temple_pods", _("The Temple of Arakan, obelisk room"), "bg_arakan_temple_pods")
    LocDef = wLocs["qst_bigtrouble_temple_pods"]
    # music
    LocDef.withDayMusic("audio/music/15_Experiments.ogg")
    LocDef.withNightMusic("audio/music/15_Experiments.ogg")
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/cave.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/cave.ogg")
    # btns
    LocDef.withBtn("btn_bigtrouble_temple_pods_to_bridge", BtnChangeLoc(_("To bridge"), "qst_bigtrouble_temple_bridge"))
    LocDef.withBtn("btn_bigtrouble_temple_pods_obelisk", BtnJumpLabel(_("A strange obelisk"), "qst_BigTroubleLHamun_temple_obelisk"))

screen loc_qst_bigtrouble_temple_pods():
    default locTag = "qst_bigtrouble_temple_pods"

    use locBtn_basic(locTag, "btn_bigtrouble_temple_pods_to_bridge", "images/gui/buttons_loc/arrow_d.webp", Transform(pos = (0.5, 0.85)), key = config.keymap["nav_down"])
    use locBtn_basic(locTag, "btn_bigtrouble_temple_pods_obelisk", "images/gui/buttons_loc/question.webp", Transform(pos = (0.62, 0.41)), key = config.keymap["nav_up"])