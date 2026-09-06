init python:
    CharIDPartyDialogueLabelMap["elena"] = "elena_party_talk"

    @AppendToAllQuests
    class DialogueElena(LogicModule):
        def __init__(self):
            super().__init__()

            self.PsychoPoints = 0 # if player pulls shit moves, this raises. Effects are dialogue/narrative
            self.FedWolves = False # for travel mode, player can feed wolves, we're trackin this for that other event thing

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "mc_house_bedroom":
                if IsDaytime():
                    btnMods["btn_talkToElena"] = BtnJumpLabel(_("Talk to Elena"), "elena_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("elena_root", DNode(_("I should go."), "elena_bye", nextNode = "DNodeExit", order = -100))

            yield ("elena_party_root", DNode(_("Let's move on."), "elena_party_bye", nextNode = "DNodeExit", order = -100))

label elena_talk:
    show elena at center_f
    MC @talk "Hey there, Elena."
    ELENA @talk "[player_name!t]."
    call processDialogue("elena_root") from _call_processDialogue_28
    $ LocEnter()

label elena_bye:
    ELENA @talk "See ya."
    $ LocEnter()

#############################################
label elena_party_talk:
    show elena at center with dissolve
    ELENA "[player_name!t]."
    call processDialogue("elena_party_root") from _call_processDialogue_24
    $ LocEnter()

label elena_party_bye:
    ELENA "Of course."
    $ LocEnter()