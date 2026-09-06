init python:
    @AppendToAllQuests
    class DialogueRania(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_hookah_bar":
                btnMods["btn_hamun_hookah_bar_rania"] = BtnJumpLabel(_("Talk to Rania"), "hamun_rania_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("rania_root", DNode(_("I should go."), "hamun_rania_bye"))
    

label hamun_rania_talk:
    show rania at center
    with dissolve
    RANIA @talk "Yes? You need anything?"
    call processDialogue("rania_root") from _call_processDialogue_60
    $ LocEnter()

label hamun_rania_bye:
    RANIA @talk "Okay, talk to me if you need anything."
    $ LocEnter()