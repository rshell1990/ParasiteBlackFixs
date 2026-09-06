init python:
    # this "unlocks" (enables) clickey house
    @AppendToAllQuests
    class HouseLockBlackDiamond(LogicModule):
        def __init__(self):
            super().__init__()

            # so that you can see it, enabled during or after damzel quest
            self.canBeAccessed = False
            # so that you cant leave during damzel quest
            self.canExit = True

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_pleasure":
                if self.canBeAccessed == True:
                    if not QstIsActive(EventBlackDiamondPostMassacre):
                        if IsDaytime():
                            btnMods["novaras_diamond"] = BtnJumpLabel(STR_LOC.NOV_BDIAMOND, "lockedLines_novarasBordelloExt")
                        else:
                            btnMods["novaras_diamond"] = BtnChangeLoc(STR_LOC.NOV_BDIAMOND, "novaras_black_diamond")
                    else:
                        if QstGetProgress(EventBlackDiamondPostMassacre) == 0:
                            btnMods["novaras_diamond"] = BtnJumpLabel(STR_LOC.NOV_BDIAMOND,"black_diamond_post_massacre")
                        if QstGetProgress(EventBlackDiamondPostMassacre) == 1:
                            btnMods["novaras_diamond"] = BtnJumpLabel(STR_LOC.NOV_BDIAMOND,"black_diamond_post_massacre_lock_line")
                else:
                    btnMods["novaras_diamond"] = BtnJumpLabel(STR_LOC.NOV_BDIAMOND, "Locked_BlackDiamond_WontEnter")
            elif GetLocID() == "novaras_black_diamond":
                if self.canExit == True:
                    btnMods["novaras_black_diamond_toCity"] = BtnChangeLoc(
                        STR_NAV.TO_CITY, "novaras_dist_pleasure")
            return LocButtonMod(directMods = btnMods)

    # controls post-damzel & fawha stuff
    @AppendToAllQuests
    class BlackDiamondLogic(LogicModule):
        def __init__(self):
            super().__init__()
    
            # these are set via damzel quest
            self.tarekFate = None # legit variants ["died","diedVulshan","walked"]
            self.freeRide = False # set via post-damzel visit (vulshan route)
        
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_black_diamond":
                btnMods["talkServer"] = BtnJumpLabel(SERVANT_GIRL, "fawha_talk")
            return LocButtonMod(directMods = btnMods)

        def onEnter(self):  
            if GetLocID() == "novaras_black_diamond":
                if self.progress == 0:
                    return TriggeredEvent("ev_blackDiamondFawhaOnReturn")

        def onStart(self):
            QstStart(BlackDiamondArena)
            QstStart(DoorBlackDiamondArena)
            return

    # controls clickey access button
    @AppendToAllQuests
    class DoorBlackDiamondArena(LogicModule):
        def locationMod(self):
            btnMods = {}
            if not QstIsActive(QstDamzelInDiztrezz):
                btnMods["btn_black_diamond_ToArena"] = BtnChangeLoc(STR_LOC.NOV_BDIAMOND_ARENA, "novaras_black_diamond_arena")
            return LocButtonMod(directMods = btnMods)

    #### black diamond arena ####
    WorldLocation("novaras_black_diamond_arena", STR_LOC.NOV_BDIAMOND_ARENA, "cg_arena_empty", parent = "novaras_black_diamond", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_black_diamond_arena"]
    LocDef.CanWait = False
    LocDef.withBtn("novaras_black_diamond_arena_leave",
        BtnChangeLoc(STR_NAV.LEAVE, "novaras_black_diamond"))
    LocDef.withBtn("btn_bkeeper_talk", BtnDisabled())
    # music
    LocDef.withNightMusic("audio/music/30_Black_Diamond.ogg")
    LocDef.withDayMusic("audio/music/30_Black_Diamond.ogg")
    # amb
    LocDef.withDayAmbience("audio/ambience_loc/bd_arena.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/bd_arena.ogg")
    # action sfx
    LocDef.withActionSFXs({"novaras_black_diamond_arena_leave": soundLib["woodenDoor"]})

    #### black diamond interior ####
    WorldLocation("novaras_black_diamond", STR_LOC.NOV_BDIAMOND, "bg_diamond", parent = "novaras_dist_pleasure", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_black_diamond"]
    LocDef.CanWait = False
    LocDef.withBtn("novaras_black_diamond_toCity", BtnDisabled())
    LocDef.withBtn("toOffice", BtnDisabled())
    LocDef.withBtn("btn_black_diamond_ToArena", BtnDisabled())
    # Damzel In Diztrezz talk buttons
    LocDef.withBtn("talkGuard", BtnDisabled())
    LocDef.withBtn("talkAddict", BtnDisabled())
    LocDef.withBtn("talkServer", BtnDisabled())
    LocDef.withBtn("toTarekOffice", BtnDisabled())
    # the jackpot mr winward
    LocDef.withBtn("btn_jackpot_winward", BtnDisabled())
    # the jackpot vulshan route btns
    LocDef.withBtn("btn_jackpot_vulshan_guard", BtnDisabled())
    LocDef.withBtn("btn_jackpot_vulshan_vip", BtnDisabled())
    LocDef.withBtn("btn_jackpot_vulshan_checkup", BtnDisabled())
    LocDef.withBtn("btn_jackpot_vulshan_couch", BtnDisabled())
    # music
    LocDef.withNightMusic("audio/music/30_Black_Diamond.ogg")
    LocDef.withDayMusic("audio/music/30_Black_Diamond.ogg")
    # action sfx
    LocDef.withActionSFXs({"novaras_black_diamond_toCity": soundLib["woodenDoor"]})
    LocDef.withActionSFXs({"btn_black_diamond_ToArena": soundLib["woodenDoor"]})

    #### black diamond office ####
    WorldLocation("novaras_black_diamond_office", STR_LOC.NOV_BDIAMOND_OFFICE, "bg_diamond_office", parent = "novaras_black_diamond", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_black_diamond_office"]
    LocDef.withBtn("novaras_black_diamond_office_leave", 
        BtnChangeLoc(STR_NAV.LEAVE, "novaras_black_diamond"))
    # music
    LocDef.withNightMusic("audio/music/30_Black_Diamond.ogg")
    LocDef.withDayMusic("audio/music/30_Black_Diamond.ogg")
    # action sfx
    LocDef.withActionSFXs({"novaras_black_diamond_office_leave": soundLib["woodenDoor"]})

screen loc_novaras_black_diamond():
    default locTag = "novaras_black_diamond"
    use locShared_toCityBtn(locTag, "novaras_black_diamond_toCity")
    use locBtn_basic(locTag, "toOffice",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.65, 0.4)))
    use locBtn_basic(locTag, "btn_black_diamond_ToArena",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.29, 0.45)))

    # Damzel in Diztrezz quest buttons
    use locBtn_basic(locTag, "talkGuard",
        "images/gui/buttons_loc/dialogue.webp",
        Transform(pos = (0.80, 0.28)))
    use locBtn_basic(locTag, "talkAddict",
        "images/gui/buttons_loc/dialogue.webp",
        Transform(pos = (0.22, 0.62)))
    use locBtn_basic(locTag, "talkServer",
        "images/gui/buttons_loc/dialogue.webp",
        Transform(pos = (0.4, 0.47)))
    use locBtn_basic(locTag, "toTarekOffice",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.65, 0.4)))

    # The Jackpot mr winward
    use locBtn_Char(locTag, "btn_jackpot_winward",
        "mr_winward", "mr_winward",
        Transform(anchor = (0.5, 1.0), pos = (0.72, 0.91), zoom = 0.6, xzoom = -1.0))

    # The Jackpot vulshan route 
    # guard
    use locBtn_basic(locTag, "btn_jackpot_vulshan_guard",
        "images/gui/buttons_loc/dialogue.webp",
        Transform(pos = (0.86, 0.33)))
    # vip area
    use locBtn_basic(locTag, "btn_jackpot_vulshan_vip",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.56, 0.2)))
    # check up on winward
    use locBtn_basic(locTag, "btn_jackpot_vulshan_checkup",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.71, 0.45)))
    # skip time
    use locBtn_basic(locTag, "btn_jackpot_vulshan_couch",
        "images/gui/buttons_loc/sleep.webp",
        Transform(pos = (0.2, 0.62)))

screen loc_novaras_black_diamond_office():
    default locTag = "novaras_black_diamond_office"
    use locBtn_basic(locTag, "novaras_black_diamond_office_leave",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.28, 0.81)))

screen loc_novaras_black_diamond_arena():
    default locTag = "novaras_black_diamond_arena"
    use locShared_toCityBtn(locTag, "novaras_black_diamond_arena_leave")
    use locBtn_Char(locTag, "btn_bkeeper_talk",
        "cg_bandit", "cg_bandit",
        Transform(anchor = (0.5, 0.5), pos = (0.75, 0.7), zoom = 0.6, xzoom = -1.0))

label Locked_BlackDiamond_WontEnter:
    MC "This place is a den of criminals."
    MC "Thankfully, I don't have a reason to enter."
    $ LocEnterQ()