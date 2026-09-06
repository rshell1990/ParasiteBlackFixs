init python:
    CharIDPartyDialogueLabelMap["erika"] = "erika_party_talk"

    # note this is disabled and needs 2be activated 
    @AppendToAllQuests
    class DialogueErika(LogicModule):
        def extraDialogue(self):
            yield ("erika_party_root", DNode(_("Let's move on."), "erika_party_bye", nextNode = "DNodeExit", order = -100))

label erika_party_talk:
    show erika at center with dissolve
    ERIKA "[player_name!t]?"
    call processDialogue("erika_party_root") from _call_processDialogue_65
    $ LocEnter()

label erika_party_bye:
    $ tmpvar = RngInt(1, 3)
    if tmpvar == 1:
        MARKUS "Let's go, [player_name!t]."
    if tmpvar == 2:
        MARKUS "Of course, [player_name!t]."
    if tmpvar == 3:
        MARKUS "Alright, let's move out."
    $ tmpvar = {}
    $ LocEnter()