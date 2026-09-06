init python:
    @AppendToAllQuests
    class DialogueZanzibat(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_zanzibat_house":
                btnMods["hamun_zanzibat_house_talk_to_zanzibat"] = BtnJumpLabel(_("Talk to Lord Zanzibat"), "dialogue_zanzibat_talk")
            return LocButtonMod(directMods = btnMods)
        def extraDialogue(self):
            yield ("zanzibat_root", DNode(_("I should be going..."), "dialogue_zanzibat_bye", nextNode = "DNodeExit", order = -100))

label dialogue_zanzibat_talk:
    show zanzibat at cright_f with dissolve
    ZANZIBAT "Speak, [player_name!t]."
    call processDialogue("zanzibat_root") from _call_processDialogue_75
    $ LocEnter()

label dialogue_zanzibat_bye:
    ZANZIBAT @talk "May the desert winds blow in your favor."
    return