# extras (husbnados)
define BRYHER   = Character(_("Bryher"))
define MOHARIUS = Character(_("Moharius"))
define JOHAN    = Character(_("Johan"))

init python:
    @AppendToAllQuests
    class EventFortressInn(LogicModule):
        def __init__(self):
            super().__init__()
            self.VariantID = "frog" # <- by default
            self.BoughtKey = False
            # warning this doesnt mean it will 100% happen
            # it just means the chick will approach you
            self.ScheduledFuntime = False

            self.SeenFirstTimes = {
                "cat":   False, # lucy
                "wench": False, # betty
                "frog":  False, # vivian
            }

            self.FirstTimeLabels = {
                "cat":   "fortress_inn_lucy_firsttime",
                "wench": "fortress_inn_betty_firsttime",
                "frog":  "fortress_inn_vivian_firsttime",
            }

        # this is called on ENTRY so it resets stuff
        def SetVariant(self, VariantID):
            Assert(VariantID in ["cat", "wench", "frog"], "fuck u!")
            self.VariantID = VariantID
            self.BoughtKey = False
            self.ScheduledFuntime = False
            if self.VariantID == "cat":
                LocNameSetTemp(_("The Cat at Sundown"))
            elif self.VariantID == "wench":
                LocNameSetTemp(_("The Naughty Wench"))
            elif self.VariantID == "frog":
                LocNameSetTemp(_("The Dancing Frog"))
            return

        def OverrideLocBg(self):
            Result = {}
            if self.VariantID == "cat":
                Result["fortress_inn"] = "bg_inn_interior_cat"
            elif self.VariantID == "wench":
                Result["fortress_inn"] = "bg_inn_interior_wench"
            else:
                Result["fortress_inn"] = "bg_inn_interior_frog"
            return Result

        def onEnter(self):
            if GetLocID() == "fortress_inn":
                if self.SeenFirstTimes[self.VariantID] == False:
                    return TriggeredEvent(self.FirstTimeLabels[self.VariantID])

                if self.VariantID == "cat":
                    if PregFortressInnLucy().ShareImpregNews:
                        return TriggeredEvent("fortress_inn_lucy_impreg")
                    elif PregFortressInnLucy().DoBabyScene:
                        return TriggeredEvent("fortress_inn_lucy_postbirth")
                elif self.VariantID == "wench":    
                    if PregFortressInnBetty().ShareImpregNews:
                        return TriggeredEvent("fortress_inn_betty_impreg")
                    elif PregFortressInnBetty().DoBabyScene:
                        return TriggeredEvent("fortress_inn_betty_postbirth")
                elif self.VariantID == "frog":
                    if PregFortressInnVivian().ShareImpregNews:
                        return TriggeredEvent("fortress_inn_vivian_impreg")
                    elif PregFortressInnVivian().DoBabyScene:
                        return TriggeredEvent("fortress_inn_vivian_postbirth")

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "fortress_inn":
                if self.VariantID == "cat":
                    btnMods["btn_fortress_inn_talk_chick"] = BtnJumpLabel(_("Talk to Lucy"), "fortress_inn_lucy_talk")
                    btnMods["btn_fortress_inn_talk_dude"] = BtnJumpLabel(_("Talk to Johan"), "fortress_inn_johan_talk")
                    if self.BoughtKey == True:
                        btnMods["btn_fortress_inn_stairs_right"] = BtnJumpLabel(_("Go upstairs"), "fortress_inn_to_room")
                elif self.VariantID == "wench":
                    btnMods["btn_fortress_inn_talk_chick"] = BtnJumpLabel(_("Talk to Betty"), "fortress_inn_betty_talk")
                    btnMods["btn_fortress_inn_talk_dude"] = BtnJumpLabel(_("Talk to Bryher"), "fortress_inn_bryher_talk")
                    if self.BoughtKey == True:
                        btnMods["btn_fortress_inn_stairs_right"] = BtnJumpLabel(_("Go upstairs"), "fortress_inn_to_room")
                elif self.VariantID == "frog":
                    btnMods["btn_fortress_inn_talk_chick"] = BtnJumpLabel(_("Talk to Vivian"), "fortress_inn_vivian_talk")
                    btnMods["btn_fortress_inn_talk_dude"] = BtnJumpLabel(_("Talk to Moharius"), "fortress_inn_moharius_talk")
                    if self.BoughtKey == True:
                        btnMods["btn_fortress_inn_stairs_left"] = BtnJumpLabel(_("Go upstairs"), "fortress_inn_to_room")

            return LocButtonMod(directMods = btnMods)

####### quest-specifics
        def GetDrink(self):
            for CharID in player_party:
                CharHeal(CharID, worldChars[CharID]["HealthMax"] * 0.1)
                if CharID in StoryStatusEffects:
                    StoryStatusEffects.pop(CharID)
            AddNotif(_("Your party have been healed by 10%."), Kind = "heal_party")
            return

        def GetFood(self):
            for CharID in player_party:
                CharHeal(CharID, worldChars[CharID]["HealthMax"] * 0.5)
                if CharID in StoryStatusEffects:
                    StoryStatusEffects.pop(CharID)
            AddNotif(_("Your party have been healed by 50%."), Kind = "heal_party")
            return


init python:
    WorldLocation("fortress_inn", STR_LOC.FORTRESS_INN_FROG, "bg_inn_interior_frog")
    LocDef = wLocs["fortress_inn"]
    LocDef.withBtn("btn_fortress_inn_leave", BtnJumpLabel(_("Leave"), "travel_fortress_inn_leave"))
    LocDef.withBtn("btn_fortress_inn_talk_chick", BtnDisabled())
    LocDef.withBtn("btn_fortress_inn_talk_dude",  BtnDisabled())
    LocDef.withBtn("btn_fortress_inn_stairs_right",  BtnDisabled())
    LocDef.withBtn("btn_fortress_inn_stairs_left",  BtnDisabled())
    # ambience fx
    LocDef.withDayAmbience("audio/ambience_loc/tavern_fireplace.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/tavern_fireplace.ogg")
    # music
    LocDef.withDayMusic("audio/music/6_Tavern.ogg")
    LocDef.withNightMusic("audio/music/6_Tavern.ogg")

    LocDef.CanWait = False

    vfxLibLights["fortress_inn"] = {
        "lightpost_big":[
            (245, 430), (707, 157), (852, 59), (1035, 28), (1243, 534),
            (1059, 86), (1010, 199), (1451, 124), (1615, 425), 
            (1780, 419), (1879, 418), (772, 499), (1016, 532), 
        ],
        "lightpost_small":[
            (1115, 54)
        ],
        "lightpost_huge":[
            (1832, 687)
        ],
    }
    vfxLibLights["fortress_inn_night"] = vfxLibLights["fortress_inn"]

screen loc_fortress_inn():
    default locTag = "fortress_inn"
    use locBtn_basic(locTag, "btn_fortress_inn_leave", 
        "images/gui/buttons_loc/door.webp", 
        Transform(pos = (0.5, 0.85)), 
        key = config.keymap["nav_down"],
    )

    # chars talk
    if EventFortressInn().VariantID == "cat":
        use locBtn_Char(locTag, "btn_fortress_inn_talk_chick",
            "lucy", "lucy",
            Transform(anchor = (0.5, 1.0), pos = (0.23, 0.85), zoom = 0.35))
        use locBtn_Char(locTag, "btn_fortress_inn_talk_dude",
            "cg_johan", "cg_johan",
            Transform(anchor = (0.5, 1.0), pos = (0.82, 0.76), zoom = 0.35, xzoom = -1.0))
        use locBtn_basic(locTag, "btn_fortress_inn_stairs_right",
            "images/gui/buttons_loc/door.webp",
            Transform(pos = (0.735, 0.537)),
            key = config.keymap["nav_right"],
        )
    elif EventFortressInn().VariantID == "wench":
        use locBtn_Char(locTag, "btn_fortress_inn_talk_chick",
            "betty", "betty",
            Transform(anchor = (0.5, 1.0), pos = (0.23, 0.85), zoom = 0.35))
        use locBtn_Char(locTag, "btn_fortress_inn_talk_dude",
            "cg_bryher", "cg_bryher",
            Transform(anchor = (0.5, 1.0), pos = (0.82, 0.76), zoom = 0.35, xzoom = -1.0))
        use locBtn_basic(locTag, "btn_fortress_inn_stairs_right", 
            "images/gui/buttons_loc/door.webp", 
            Transform(pos = (0.735, 0.537)), 
            key = config.keymap["nav_right"],
        )


    elif EventFortressInn().VariantID == "frog":
        use locBtn_Char(locTag, "btn_fortress_inn_talk_chick",
            "vivian", "vivian",
            Transform(anchor = (0.5, 1.0), pos = (0.23, 0.85), zoom = 0.35))
        use locBtn_Char(locTag, "btn_fortress_inn_talk_dude",
            "cg_moharius", "cg_moharius",
            Transform(anchor = (0.5, 1.0), pos = (0.82, 0.76), zoom = 0.35, xzoom = -1.0))
        use locBtn_basic(locTag, "btn_fortress_inn_stairs_left",
            "images/gui/buttons_loc/door.webp",
            Transform(pos = (0.328, 0.544)),
            key = config.keymap["nav_left"],
        )




init python:
    WorldLocation("fortress_inn_room", STR_LOC.FORTRESS_INN_ROOM, "bg_inn_room")
    LocDef = wLocs["fortress_inn_room"]
    # music
    LocDef.withDayMusic("audio/music/6_Tavern.ogg")
    LocDef.withNightMusic("audio/music/6_Tavern.ogg")

    LocDef.CanWait = False

    vfxLibLights["fortress_inn"] = {
        "lightpost_big":[
            (245, 430), (707, 157), (852, 59), (1035, 28), (1243, 534),
            (1059, 86), (1010, 199), (1451, 124), (1615, 425), 
            (1780, 419), (1879, 418), (772, 499), (1016, 532), 
        ],
        "lightpost_small":[
            (1115, 54)
        ],
        "lightpost_huge":[
            (1832, 687)
        ],
    }
    vfxLibLights["fortress_inn_room"] = {
        "lightpost_big":[
            (245, 430), (707, 157), (852, 59), (1035, 28), (1243, 534),
            (1059, 86), (1010, 199), (1451, 124), (1615, 425), 
            (1780, 419), (1879, 418), (772, 499), (1016, 532), 
        ],
    }

screen loc_fortress_inn_room():
    default locTag = "fortress_inn_room"
    