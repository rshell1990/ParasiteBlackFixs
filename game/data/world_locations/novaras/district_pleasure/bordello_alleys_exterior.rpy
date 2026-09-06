image novaras_bordello_door_t = "images/world_interact/novaras_city/nov_bord_door.webp"
image novaras_bordello_door_h:
    "novaras_bordello_door_t"
    matrixcolor MxMapHover()

init python:
    # this controls what happens if ya click the clickey house
    @AppendToAllQuests
    class HouseLockNovarasBordelloExt(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_pleasure":
                if IsDaytime():
                    btnMods["btn_novaras_bordello"] = BtnJumpLabel(
                        STR_LOC.NOV_BORDELLO, "lockedLines_novarasBordelloExt")
                else:
                    btnMods["btn_novaras_bordello"] = BtnChangeLoc(
                        STR_LOC.NOV_BORDELLO, "novaras_bordello_ext")
            return LocButtonMod(directMods = btnMods)

    WorldLocation("novaras_bordello_ext", STR_LOC.NOV_BORDELLO_EXT, "bg_weeping_heart_brothel_ext", parent = "novaras_dist_pleasure", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["novaras_bordello_ext"]
    LocDef.withBtn("novaras_bordello_ext_toCity", BtnGotoRootFrom(STR_NAV.TO_CITY, LocDef))
    LocDef.withBtn("shani_talk_btn", BtnDisabled())
    # coming storm vala stash spot
    LocDef.withBtn("btn_comingstorm_assassin_gold_stash_spot", BtnDisabled())
    LocDef.CanWait = False

    # enter door
    LocDef.withBtn("novaras_bordello_door", BtnDisabled())
    # ambience sfx
    LocDef.withDayAmbience("audio/ambience_loc/crowd_city.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/citynight.ogg")
    # music
    LocDef.withNightMusic("audio/music/24_Brothel.ogg")
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    # vfx
    vfxLibLights["novaras_bordello_ext_night"] = {"lightpost_big":[(272, 464), (743, 509)]}
    # sfx
    LocDef.withActionSFXs({"novaras_bordello_door": soundLib["woodenDoor"]})

label lockedLines_novarasBordelloExt:
    MC "Nothing of {i}interest{/i} is happening here right now."
    MC "Perhaps I should visit the place when the night falls..."
    $ LocEnterQ()

screen loc_novaras_bordello_ext():
    default locTag = "novaras_bordello_ext"
    use locShared_toCityBtn(locTag, "novaras_bordello_ext_toCity")

    use locBtn_Char(locTag, "shani_talk_btn",
        "shani", "shani",
        Transform(anchor = (0.5, 0.5), pos = (0.35, 0.67), zoom = 0.55))

    use locBtn_sprite(locTag, "novaras_bordello_door",
        "novaras_bordello_door_t", "novaras_bordello_door_h",
        # bordello door
        Transform(anchor = (0.5, 1.0), pos = (0.201, 0.975)), key = config.keymap["nav_left"], NightTint = False)

    use locBtn_basic(locTag, "btn_comingstorm_assassin_gold_stash_spot",
        "images/gui/buttons_loc/chest.webp",
        Transform(pos = (0.81, 0.54)))

    