init python:
    @AppendToAllQuests
    class DialogueNyx(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_fort_seb_captains_office":
                btnMods["nyx_talk_btn"] = BtnJumpLabel(_("Talk to Captain Nyx"), "nyx_talk")
            return LocButtonMod(directMods=btnMods)

        def extraDialogue(self):
            yield ("nyx_root", DNode(_("I should go."), "nyx_bye", nextNode = "DNodeExit", order = -100))

label nyx_talk:
    show nyx at center_f with dissolve
    NYX "Good day, [player_name!t]."
    $ CharMeet("nyx")
    call processDialogue("nyx_root") from _call_processDialogue_43
    $ LocEnter()

label nyx_bye:
    NYX "Back to work."
