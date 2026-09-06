init python:
    @AppendToAllQuests
    class DialogueCarina(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_bordello_office":
                btnMods["btn_talk_carina_office"] = BtnJumpLabel(_("Talk to Carina"), "talk_carina_office")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("carina_root", DNode(_("How is the business?"), "talk_carina_hows_stuff"))
            yield ("carina_root", DNode(_("I have to go."), "talk_carina_bye", nextNode = "DNodeExit", order = -100))

# PH
label talk_carina_office:
    show carina at center with dissolve
    CARINA "Yes, [player_name!t]?"
    call processDialogue("carina_root") from _call_processDialogue_55
    $ LocEnter()

label talk_carina_hows_stuff:
    CARINA "Quite good, actually."
    CARINA "Was there something specific you wanted?"
    MC "Not really."
    return

label talk_carina_bye:
    CARINA "Safe travels, [player_name!t]."
    CARINA "Do pay me a visit every now and then, {i}alright?{/i}"
    MC "Sure."
    CARINA "Having you around is... good for business."
    $ LocEnter()
