init python:
    WorldLocation("mc_house_bedroom", STR_LOC.NOV_MC_HOUSE_BED, "bg_mc_house_bedroom", parent = "mc_house_kitchen", WorldMapRootLocTag = "novaras_gates")
    LocDef = wLocs["mc_house_bedroom"]
    LocDef.withBtn("btn_mc_house_chest",   BtnDisabled()) # handled via separate logicmodule CAUSE INIT LEVELS FIGHTING
    LocDef.withBtn("btn_mc_house_trainsword", BtnFluffTxt(_("Training Sword"), _("Father bought me these to practice with in case there’s a siege... Me and Markus mostly just mess around with them in private though.")))
    LocDef.withBtn("btn_mc_house_bed",     BtnJumpLabel(_("Bed"), "bed_choice_mc_house"))
    LocDef.withBtn("btn_mc_house_bedroom_exit", BtnChangeLoc(STR_NAV.LEAVE, "mc_house_kitchen"))
    LocDef.withBtn("btn_talkToElena",      BtnDisabled())
    LocDef.withBtn("btn_slime_jar",        BtnDisabled())
    # music
    LocDef.withDayMusic("audio/music/3_Novaras_L.ogg")
    LocDef.withNightMusic("audio/music/7_novaras_d.ogg")
    # action sfx
    LocDef.withActionSFXs({"btn_mc_house_bedroom_exit": soundLib["woodenDoor"]})
    # nijah during rescue sequence
    LocDef.withBtn("btn_talkNijahMcHouse", BtnDisabled())
    # vfx
    vfxLibLights["mc_house_bedroom_night"] = {
        "lightpost_huge":   [(684,  628)], 
        "lightpost_small":  [(1447, 458)],
    }
    LocDef.SetDayNightMatrixClass(MxDayNight)

    @AppendToAllQuests
    class ContainerMCHouseChest(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "mc_house_bedroom":
                btnMods["btn_mc_house_chest"] =         BtnShowScreen(_("Your stash"), "container", chest_mc_house, HideOnTakeAll = True)
            elif GetLocID() == "hamun_hookah_bar_room":
                btnMods["btn_hamun_hookah_bar_chest"] = BtnShowScreen(_("Your stash"), "container", chest_mc_house, HideOnTakeAll = True)
            return LocButtonMod(directMods = btnMods)

label bed_choice_mc_house:
    "My bed."
    menu:
        "Go to sleep.":
            if not IsInTimeFrame(TIME_DAWN, TIME_AFTERNOON):
                scene black with dissolve
                call ProcessLocEvent("PreSleepMcHouse") from _call_ProcessLocEvent_1
                call shared_bed_sleep_logic from _call_shared_bed_sleep_logic_2
                call ProcessLocEvent("PostSleepMcHouse") from _call_ProcessLocEvent_2
            else:
                MC "(I am not tired enough to sleep right now.)"
                MC "({i}And I won't be until afternoon.{/i})"
        "On a second thought, not now.":
            pass
    $ LocEnter()

label shared_bed_sleep_logic:
    $ Pause(0.5)
    $ TimeAdvTo(TIME_VISUAL_DAWN)
    $ BlockWaitDynamic(False)
    $ HealParty()
    return

screen loc_mc_house_bedroom():
    default locTag = "mc_house_bedroom"

    # nijah during rescue sequence
    use locBtn_Char(locTag, "btn_talkNijahMcHouse",
        "nijah", "nijah",
        Transform(anchor = (0.5, 0.5), pos = (0.45, 0.6), zoom = 0.75))
        
    use locBtn_Char(locTag, "btn_talkToElena",
        "elena", "elena", 
        Transform(anchor = (0.5, 0.5), pos = (0.62, 0.68), xzoom = -1.0, zoom = 1.0))

    use locBtn_basic(locTag, "btn_mc_house_chest",
        "images/gui/buttons_loc/chest.webp",
        Transform(pos = (0.1, 0.55)),
        key = config.keymap["nav_left"])
    use locBtn_basic(locTag, "btn_mc_house_trainsword",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.83, 0.23)))
    use locBtn_basic(locTag, "btn_mc_house_bed",
        "images/gui/buttons_loc/sleep.webp",
        Transform(pos = (0.74, 0.65)),
        key = config.keymap["nav_right"])
    use locBtn_basic(locTag, "btn_mc_house_bedroom_exit",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.3, 0.85)), 
        key = config.keymap["nav_down"])

    
    # slime jar 
    use locBtn_basic(locTag, "btn_slime_jar",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.70, 0.88)))