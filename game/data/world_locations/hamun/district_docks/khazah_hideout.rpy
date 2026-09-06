init python:
    @AppendToAllQuests
    class DialogueHamunKhazahLeader(LogicModule):
        def __init__(self):
            super().__init__()
            self.Rel = 0 # zero is basic, 1 is 'better' relationship after doing the face hunt for them

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_khazah_hideout":
                btnMods["btn_hamun_khazah_hideout_leader_talk"] = BtnJumpLabel(_("Talk to Khazah leader"), "hamun_khazah_leader_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("hamun_khazah_leader_root", DNode(_("I should go."), "hamun_khazah_leader_bye", nextNode = "DNodeExit", order = -100))


label hamun_khazah_leader_talk:
    show cg_bandit at center with dissolve
    if DialogueHamunKhazahLeader().Rel == 0:
        KHAZAH_LEADER "Well, what business do you have with the Khazah?"
    else:
        KHAZAH_LEADER "Ah, can I help you with something, friend?"
    call processDialogue("hamun_khazah_leader_root") from _call_processDialogue_76
    $ LocEnter()

label hamun_khazah_leader_bye:
    if DialogueHamunKhazahLeader().Rel == 1:
        KHAZAH_LEADER "Then I wish you safe travels."
    $ LocEnter()

init python:
    # enabled by bigtrouble quest
    @AppendToAllQuests
    class HouseLockHamunKhazahHideout(LogicModule):
        def __init__(self):
            super().__init__()
            self.State = None # "no_biz", "cleaned", "operating"

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_dist_docks":
                if self.State == "no_biz":
                    btnMods["hamun_docks_to_khazah_hideout"] = BtnJumpLabel(STR_LOC.HAMUN_KHAZAH_HIDEOUT, "hamun_khazah_nobusiness")
                elif self.State == "operating":
                    btnMods["hamun_docks_to_khazah_hideout"] = BtnChangeLoc(STR_LOC.HAMUN_KHAZAH_HIDEOUT, "hamun_khazah_hideout")
                elif self.State == "cleaned":
                    btnMods["hamun_docks_to_khazah_hideout"] = BtnJumpLabel(STR_LOC.HAMUN_KHAZAH_HIDEOUT, "hamun_khazah_cleaned")
            return LocButtonMod(directMods = btnMods)

        def onStart(self):
            QstStart(DialogueHamunKhazahLeader)

    WorldLocation("hamun_khazah_hideout", STR_LOC.HAMUN_KHAZAH_HIDEOUT, "bg_hamun_khazah_hideout", WorldMapRootLocTag = "hamun_gates")
    LocDef = wLocs["hamun_khazah_hideout"]
    LocDef.CanWait = False
    # clickables
    LocDef.withBtn("hamun_khazah_hideout_to_docks", BtnChangeLoc(STR_LOC.HAMUN_DIST_DOCKS, "hamun_dist_docks")) 
    LocDef.withBtn("btn_hamun_khazah_hideout_leader_talk", BtnDisabled())
    # action sfx
    LocDef.withActionSFXs({"hamun_khazah_hideout_to_docks": soundLib["tentFlap"]})
    # music
    LocDef.withDayMusic("audio/music/43_Hamun_day.ogg")
    LocDef.withNightMusic("audio/music/44_Hamun_night.ogg")
    # vfx
    vfxLibLights["hamun_khazah_hideout_night"] = {
        "lightpost_big":[(875, 571), (1153, 534)],
    }

    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

label hamun_khazah_cleaned:
    MC "(There's no one in or around.)"
    $ LocEnterQ()

screen loc_hamun_khazah_hideout():
    default locTag = "hamun_khazah_hideout"

    # exit outside
    use locBtn_basic(locTag, "hamun_khazah_hideout_to_docks",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.74, 0.51)),
        key = config.keymap["nav_right"])
    
    use locBtn_Char(locTag, "btn_hamun_khazah_hideout_leader_talk",
        "cg_bandit", "cg_bandit",
        Transform(anchor = (0.5, 1.0), pos = (0.33, 1.08), zoom = 0.74))

label hamun_khazah_nobusiness:
    MC "(I have no business here.)"
    $ LocEnterQ()