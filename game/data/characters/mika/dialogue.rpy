init python:
    @AppendToAllQuests
    class DialogueMika(LogicModule):
        def locationMod(self):
            btnMods = {}
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("mika_root", DNode(_("I should go."), "mika_bye", nextNode = "DNodeExit", order = -100))

label mika_talk:
    show mika with dissolve:
        xcenter 0.5
    MIKA "..." # empty
    $ CharMeet("mika")
    call processDialogue("mika_root") from _call_processDialogue_54
    $ LocEnter()

label mika_bye:
    MIKA "..." # empty
    $ LocEnter()
