# main devroom label
label devroom:
    $ QstStart(DevroomMenuQuest)
#################
    # this is like "test scope", you can add shit within these 
    $ PartyAddChar("kiara")
    $ CharAltFormUnlock("kiara")
    $ PartyAddChar("erika")
    $ TransformKiara(True)
    $ DEBUG_AddOneToAllClassSkills()
#################
    $ gui_parts = dict.fromkeys(gui_parts, True)
    $ LocSet("devroom")

    # instantly call kylisa diag
    call processDialogue("dev_root") from _call_processDialogue_46
    $ LocEnter()

# specific labels you jump to from kylisa dialogue
label dev_barati_test:
    $ Barati_GameStartPopup("someplayer")
    if Barati_LastGameResult == "victory":
        DEBUG "Last barati game won"
    elif Barati_LastGameResult == "defeat":
        DEBUG "Last barati game lost"
    return

label test_script_choice:
    menu:
        "test_script1":
            jump test_script1
        "test_script2":
            jump test_script2
        "test_script3":
            jump test_script3
        "test_script4":
            jump test_script4
        "return":
            return

label dev_battle_setup:
    if not PlayerItemQty("potion_heal_minor") >= 1:
        $ PlayerAddItem("potion_heal_minor", 4)
    if not PlayerItemQty("potion_heal_regular") >= 1:
        $ PlayerAddItem("potion_heal_regular", 4)
    if not PlayerItemQty("potion_lowrevival") >= 1:
        $ PlayerAddItem("potion_lowrevival", 4)
    if not PlayerItemQty("potion_medrevival") >= 1:
        $ PlayerAddItem("potion_medrevival", 4)
    if not PlayerItemQty("potion_highrevival") >= 1:
        $ PlayerAddItem("potion_highrevival", 4)
    $ BattleSetup_ParseBattleMaps()
    call screen battle_setup()
    if _return is not True:
        # this statement is here only to ensure that a hot-reload won't undo your chars/gear setup
        "(good people of the imperial city, welcome to the arena!)"

        $ TransformMC(True)
        $ TransformMarkus(True)

        $ renpy.block_rollback() # <- stops you from fucking up your saved chars list
        $ InfectionModule().isActive = True
        $ InfectionModule().CurrentValue = 40
        $ StartBattle(BattleData(BackgroundImage = _return[0], CharIDList_Left = _return[1], CharIDList_Right = _return[2], AutoNightBackground = False))
        $ InfectionModule().isActive = False
        if LastBattleOutcome == "defeat":
            "(defeat)"
        if LastBattleOutcome == "victory":
            "(victory)"
        if LastBattleOutcome == "retreat":
            "(retreat)"
        jump dev_battle_setup
    $ LocEnter()

# dev loc defs 
init python:
    @AppendToAllQuests
    class DevroomMenuQuest(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "devroom":
                btnMods["talkDevroom"] = BtnJumpLabel("Talk to Kylisa","dev_talk")
            return LocButtonMod(directMods = btnMods)
        def extraDialogue(self):
            yield ("dev_root", DNode("Barati test",     "dev_barati_test"))
            yield ("dev_root", DNode("'Test script'",   "test_script_choice"))
            yield ("dev_root", DNode("Combat setup",    "dev_battle_setup"))
            yield ("dev_root", DNode("That'd be all.",  "dev_goodbye",  nextNode = "DNodeExit", order = -100))
    WorldLocation("devroom", STR_LOC.DEVROOM, "bg_weeping_heart_brothel_room")
    wLocs["devroom"].withBtn("talkDevroom", BtnDisabled())
    wLocs["devroom"].withDayMusic("audio/music/22_Space_Odyssey.ogg")
    wLocs["devroom"].withDayMusic("audio/music/15_Experiments.ogg")
    vfxLibLights["devroom"] = {"lightpost_big":[(763, 528), (1169, 521)]}
    vfxLibLights["devroom_night"] = {"lightpost_big":[(763, 528), (1169, 521)]}

screen loc_devroom():
    default locTag = "devroom"
    use locBtn_Char(locTag, "talkDevroom", "kylisa", "kylisa",
        Transform(pos = (0.5, 0.5), zoom = 0.6))

# fluff
label dev_talk:
    show kylisa at center with dissolve
    KYLISA "What is it, child?"
    call processDialogue("dev_root") from _call_processDialogue_4
    $ LocEnter()

label dev_goodbye:
    $ rng = RngInt(1, 3)
    if rng == 1:
        KYLISA "It doesn't matter who we are..."
        KYLISA "What matters is our plan."
    if rng == 2:
        KYLISA "Stay thirsty, child."
    if rng == 3:
        KYLISA "May the starlets guide you."
    return
