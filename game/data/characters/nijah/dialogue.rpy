init python:
    @AppendToAllQuests
    class DialogueNijah(LogicModule):
        def extraDialogue(self):
            yield ("nijah_root", DNode(_("I should go."), "nijah_bye", nextNode = "DNodeExit", order = -100))

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "nijah_house_lroom":
                if IsDaytime():
                    if not RomanceNijah().storeOpen:
                        btnMods["nijah_talk_btn"] = BtnJumpLabel(_("Talk to Nijah"), "nijah_talk")
            return LocButtonMod(directMods = btnMods)

# general talk label
label nijah_talk:
    show nijah at center
    with dissolve
    NIJAH '[player_name!t]!'
    MC @talk 'Hey Nijah.'
    call processDialogue("nijah_root") from _call_processDialogue_22
    $ LocEnter()

label nijah_bye:
    NIJAH "I will be here, [player_name!t]."
    $ LocEnter()
