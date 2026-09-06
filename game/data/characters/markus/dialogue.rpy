init python:
    CharIDPartyDialogueLabelMap["markus"] = "markus_party_talk"

    @AppendToAllQuests
    class DialogueMarkus(LogicModule):
        def extraDialogue(self):
            yield ("markus_party_root", DNode(_("Let's move on."), "markus_party_bye", nextNode = "DNodeExit", order = -100))

label markus_party_talk:
    show markus at center
    with dissolve
    MARKUS "[player_name!t]?"
    call processDialogue("markus_party_root") from _call_processDialogue_67
    $ LocEnter()

# goodbye
label markus_party_bye:
    $ tmpvar = {}
    $ tmpvar = RngInt(1, 3)
    if tmpvar == 1:
        MARKUS "Let's go, [player_name!t]."
    if tmpvar == 2:
        MARKUS "Of course, [player_name!t]."
    if tmpvar == 3:
        MARKUS "Alright, let's move out."
    $ tmpvar = {}
    return
