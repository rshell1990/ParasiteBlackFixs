init python:
    @AppendToAllQuests
    class DialogueRegina(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "mc_house_kitchen":
                if IsDaytime():
                    btnMods["talkRegina"] = BtnJumpLabel(tra(_("Talk to %s")) % tra(regina_ref), "regina_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("regina_root",   DNode(_("Is everything alright?"), "regina_askAllRight"))
            yield ("regina_root",   DNode(_("I wanted to ask you about something..."), "regina_askSubMenu", nextNode = "regina_subAsk"))
            yield ("regina_subAsk", DNode(_("Have you heard from Father?"), "regina_askFather"))
            yield ("regina_subAsk", DNode(_("Tell me more about how Erika is doing..."), "regina_askErika"))
            yield ("regina_subAsk", DNode(_("Adara came by every day?"), "regina_askAdara"))
            yield ("regina_subAsk", DNode(_("That’s all the questions I had..."), "dialogue_nothing", nextNode = "_root"))
            yield ("regina_root",   DNode(_("I’ve got to get going."), "regina_goodbye", nextNode = "DNodeExit", order = -100))


label regina_talk:
    show regina at cleft
    with dissolve
    show mc at cright_f with easeinright
    REGINA @talk 'Ah! There you are!'
    call processDialogue("regina_root") from _call_processDialogue_3
    $ LocEnter()

label regina_askAllRight:
    #RANDOM RESPONSES
    $ rng = RngInt(1, 4)
    if rng == 1:
        REGINA @talk 'Hm? Everything’s fine, dear! '
    if rng == 2:
        REGINA @talk 'I’m just about to put some food on, will you be staying long?'
    if rng == 3:
        REGINA @talk 'That Town Crier is still ranting about how Newheart will save us all... Doesn’t he ever give up?'
    if rng == 4:
        REGINA @talk 'Have you been to a temple recently? It might be a good idea to receive some blessings from the Gods after what’s happened...'
    return

label regina_askSubMenu:
    REGINA @talk 'What do you want to ask?'
    return

label regina_askFather:
    REGINA @talk 'Yes, apparently he’s working on some kind of excavation, with Lord Psydon’s blessing...'
    REGINA @talk 'No idea what it’s all about but he’s alright, dear.'
    return

label regina_askErika:
    REGINA @talk 'Erika is just fine, like I said, she’s off galivanting around with those Inquisitors doing God only knows what.'
    MC @talk 'That’s all you know?'
    REGINA @talk 'I’m afraid she doesn’t share much else, not even with me.'
    REGINA @talk 'Very top secret and all that. '
    return

label regina_askAdara:
    REGINA @talk 'Oh yes, you should see her if you haven’t already.'
    REGINA @talk 'The girl has been quite frantic without you.'
    REGINA @talk 'And maybe just a tad bit annoying...'
    MC @talk '[regina_ref_cap!t]!'
    REGINA @talk 'What? She came by ALL the time, it was sweet, but it got old after the hundredth time...'
    return

label regina_goodbye:
    REGINA @talk 'Be safe!'
    return
