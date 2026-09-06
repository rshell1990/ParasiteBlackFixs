init python:
    CharIDPartyDialogueLabelMap["myu"] = "myu_party_talk"

    @AppendToAllQuests
    class DialogueMyu(LogicModule):
        def __init__(self):
            super().__init__()

            self.myuKnowsLang = False

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "azul_safehouse_bedroom":
                btnMods["btn_talk_myu"] = BtnJumpLabel(_("Talk to Myu"), "nov_myu_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("myu_root", DNode(_("Goodbye, Myu."), "nov_myu_bye", nextNode = "DNodeExit", order = -100))
            if self.myuKnowsLang:
                yield ("myu_root", DNode(_("How are you feeling today, Myu?"), "nov_myu_howyoufeel"))

            yield ("myu_party_root", DNode(_("Let's go."), "myu_party_bye", nextNode = "DNodeExit", order = -100))


label myu_party_talk:
    show myu at center with dissolve
    MYU "Myu?"
    call processDialogue("myu_party_root") from _call_processDialogue_68
    $ LocEnter()

label myu_party_bye:
    MYU "Myu!"
    $ LocEnter()

#################################################
label nov_myu_howyoufeel:
    $ rng = RngInt(1,6)
    if rng == 1:
        MYU @talk "Myu is fine, been reading more to try to learn to talk better!"
        MC @smile "That's good to hear, Myu, keep it up!"
    if rng == 2:
        MYU @smile "Myu is good! Myu has been testing body."
        MYU @talk "So far, Myu is able to also make hammers instead of blades."
        MYU @talk "Myu can also make other things too!"
        MC @talk "That could prove very useful."
        MC @talk "Let me know what else you're able to form!"
        MYU @smile "Okay!~"
    if rng == 3:
        MYU @scared "Some people were arguing really loud outside."
        MYU @scared "Scary..."
        MC @talk "I'm sure you could scare them far more than you scare me you if you wanted to."
        MYU @talk "Mmm, Myu doesn't really like scaring people unless she has to."
    if rng == 4:
        if QstIsActive(RomanceMyu):
            MYU @think "Boreddddddddd."
            MYU @think "Myu is so bored."
            MYU @talk "{i}Husband ~ Come have some fun with wifey soon.{/i}"
        else:
            MYU @talk "Myu is fine, been reading more to try to learn to talk better!"
            MC @smile "That's good to hear, Myu, keep it up!"
    if rng == 5:
        if CharIsVisiblyPreg("myu"):
            MYU @smile "Myu can feel the baby moving around!"
            MYU @smile "They're so strong already!"
            "Myu took my hand and placed it onto her belly, where I could feel the child moving around beneath."
            MYU @blush "Fufufu~ We make more soon?"
        else:
            MYU @smile "Myu is good! Myu has been testing body."
            MYU @talk "So far, Myu is able to also make hammers instead of blades."
            MYU @talk "Myu can also make other things too!"
            MC @talk "That could prove very useful."
            MC @talk "Let me know what else you're able to form!"
            MYU @smile "Okay!~"
    if rng == 6:
        if CharIsVisiblyPreg("myu"):
            MYU @talk "So hungry!"
            MYU @smile "But Myu guesses she is eating for two after all now, right?"
        else:
            MYU @scared "Some people were arguing really loud outside."
            MYU @scared "Scary..."
            MC @talk "I'm sure you could scare them far more than you scare me you if you wanted to."
            MYU @talk "Mmm, Myu doesn't really like scaring people unless she has to."
    return

label nov_myu_talk:
    show myu at cright_f with dissolve
    show mc at cleft with easeinleft
    if DialogueMyu().myuKnowsLang:
        MYU @smile "[player_name!t]!"
    else:
        MYU @smile "Myu!"
    call processDialogue("myu_root") from _call_processDialogue_27
    $ LocEnter()

label nov_myu_bye:
    if DialogueMyu().myuKnowsLang:
        MYU @smile "Be safe!"
    else:
        MYU "Myu..."
    $ LocEnter()