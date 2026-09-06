init python:
    @AppendToAllQuests
    class DialogueShay(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_tavern":
                btnMods["btn_talk_shay"] = BtnJumpLabel(_("Talk to Shay"), "shay_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("shay_root", DNode(_("Nothing for now, thank you."), "shay_bye", nextNode = "DNodeExit", order = -100))

label shay_talk:
    show shay at center with dissolve:
        zoom 1.1
    SHAY @smile 'Welcome!'
    $ CharMeet("shay")
    SHAY @talk 'Anything I can do for you?'
    call processDialogue("shay_root") from _call_processDialogue_45

label shay_bye:
    SHAY @smile2 'Mmm, you just call when you want something!'
    $ LocEnter()