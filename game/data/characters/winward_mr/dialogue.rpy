init python:
    @AppendToAllQuests
    class DialogueMrWinward(LogicModule):
        def extraDialogue(self):
            yield ("mr_winward_root", DNode(_("Farewell."), "dialogue_mr_winward_farewell", nextNode = "DNodeExit", order = -100))

label nov_mr_winward_talk:
    show mr_winward at center_f with dissolve
    MR_WINWARD "Is there something you need, lad?"
    call processDialogue("mr_winward_root") from _call_processDialogue_49
    $ LocEnter()

label dialogue_mr_winward_farewell:
    MR_WINWARD  "On your way then!"
    return