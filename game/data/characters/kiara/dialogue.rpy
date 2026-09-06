init python:
    CharIDPartyDialogueLabelMap["kiara"] = "kiara_party_talk"

    @AppendToAllQuests
    class DialogueKiara(LogicModule):
        def extraDialogue(self):
            yield ("kiara_party_root", DNode(_("Let's go."), "kiara_party_bye", nextNode = "DNodeExit", order = -100))

label kiara_party_talk:
    show kiara at center
    with dissolve
    KIARA "Yes, [player_name!t]?"
    call processDialogue("kiara_party_root") from _call_processDialogue_66
    $ LocEnter()

# goodbye
label kiara_party_bye:
    $ tmpvar = RngInt(1, 3)
    if tmpvar == 1:
        KIARA "Let's go, [player_name!t]."
    if tmpvar == 2:
        KIARA "Of course, [player_name!t]."
    if tmpvar == 3:
        KIARA "Alright, let's move out."
    $ tmpvar = {}
    $ LocEnter()