init python:
    CharIDPartyDialogueLabelMap["sypha"] = "sypha_party_talk"

    @AppendToAllQuests
    class DialogueSypha(LogicModule):
        def extraDialogue(self):
            yield ("sypha_party_root", DNode(_("Let's go."), "sypha_party_bye", nextNode = "DNodeExit", order = -100))

label sypha_party_talk:
    show sypha at center
    with dissolve
    SYPHA "Yes, [player_name!t]?"
    call processDialogue("sypha_party_root") from _call_processDialogue_72
    $ LocEnter()

# goodbye
label sypha_party_bye:
    SYPHA "Of course."
    $ LocEnter()