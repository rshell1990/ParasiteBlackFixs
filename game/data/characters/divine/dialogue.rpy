init python:
    @AppendToAllQuests
    # this is jury-rigged from a weird quest it was into a dialogue object
    class DialogueDivine(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_palam_mainhall":
                if IsDaytime():
                    btnMods["btn_palam_mainhall_talk_divine"] = BtnJumpLabel(_("Talk to Divine"), "divine_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("divine_root",DNode(_("Can you tell me more about the goddess Palam?"), "divine_questions1"))
            yield ("divine_root",DNode(_("How many of you are there?"), "divine_questions2"))
            # Disabled for now since it's non-functional anyway
            #yield ("divine_root",DNode("I am in need of healing, sister. (WIP)", "divine_heal"))
            yield ("divine_root",DNode(_("That is all. Thank you, sister."), "divine_bye", nextNode = "DNodeExit", order = -100))

        def onEnter(self):  
            if GetLocID() == "novaras_palam_mainhall":
                if IsDaytime():
                    if self.progress == 0:
                        return TriggeredEvent("divine_firstmeet")

### divine talk labels
label divine_talk:
    show divine at center with dissolve
    DIVINE 'How can I help you, child?'
    call processDialogue("divine_root") from _call_processDialogue
    $ LocEnter()

label divine_bye:
    DIVINE 'Be well, child.'
    $ LocEnter()
#######################
### questions
label divine_questions1:
    DIVINE 'You’ve come here for a lesson?'
    MC 'I know the basics...'
    DIVINE '... It is said the great goddess Palam was born Palon, God of Love.'
    DIVINE 'Palon watched and meddled in the romantic affairs of both our realm and the realm of the gods. '
    DIVINE 'Uniting couples rarely thought a good match by many, but he always knew better.'
    DIVINE '... But Palon was displeased with his form... He wanted his outer beauty to reflect the inner love he lavished upon us Alderians.'
    DIVINE 'Envious of the female forms around him and feeling trapped in despair at the male form he occupied, he cast himself into the Great Blue Lagoon, emerging as the beautiful goddess Palam.'
    DIVINE 'The great goddess Palam bestows upon those born with her favour the greatest powers of healing in the realm.'
    DIVINE 'Through her wisdom and guidance, our bodies are also changed to her desired form.'
    MC 'Is that why all the mages under her blessing were born as... born as...'
    DIVINE '... Men?'
    MC 'Yes.'
    DIVINE 'We all were once... But once the change has begun there is little difference.'
    MC 'But you have... {i}*Cough*{/i}'
    'Sister Divine raised an eyebrow and smirked as I tripped over the words. '
    DIVINE '{i}Both sets?{/i}'
    MC 'U-Uhh... Well...'
    MC 'That... must be difficult.'
    'Sister Divine smiled mischievously as she leaned forward.'
    DIVINE 'If you’re that curious, why don’t you ask one of our mages?'
    DIVINE 'Our goddess, unlike most, demands we take no vows of chastity, you know...'
    'Sister Divine playfully winked before her back straightened once again.'
    menu:
        'I think I’d rather ask you, Sister Divine...':
            'She laughed at the comment.'
            DIVINE '{i}Interesting...{/i}'
            'Her eyes scanned over me, almost dismissively.'
        'I... Uh, right...':
            pass
    return

label divine_questions2:
    DIVINE 'There is only ever a few hundred of us at one time... As the goddess wills...'
    MC 'Why?'
    DIVINE 'We do not know... Only some are chosen, it’s not our place to question her decisions.'
    return

##############################
label divine_firstmeet:
    'The beautiful Mages of Palam, for all accounts were still human, though no cursory glance would make this obvious.'
    'Born with the blessings of the goddess Palam, their bodies were morphed and now bore a blue complexion the goddess’ divine will moulds those chosen into her most desired form and then blesses them with her gift of divine healing.'
    'It is a place of ancient tradition, libraries of books piled high and strange hieroglyphs and runes on the floor in chalk that glowed different shades. '
    'Taking centre stage was a great statue of the goddess Palam, her arms and wings outstretched. Here and there I glimpsed robed figures, their soft, blue faces barely visible before they quickly shuffled away with their spell books. '
    'A voice called out, sultry, but mature with age. '
    UNKNOWN '... Quite the sight, is it not?'
    show divine at center with dissolve
    'I turned to look at the beautiful figure before me.'
    MC 'Oh, I’m sorry I didn’t see you there, sister.'
    DIVINE 'You may call me Sister Divine... Now...'
    $ CharMeet("divine")
    $ QstSetProgress(DialogueDivine, 1)
    call processDialogue("divine_root") from _call_processDialogue_5
