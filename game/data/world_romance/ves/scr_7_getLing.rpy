label rom_Ves_7_GetLing:
    if not DialogueDros().shopWorks:
        DROS @talk 'I need that crystal before I can make any outfits!'
        DROS @talk 'Get it!'
        return
    DROS @talk 'You want lingerie for... an orc?'
    MC '...'
    DROS @talk 'Well... I can’t imagine why you’d want to sleep with such brutish women but—'
    DROS @talk 'Us elves try not to judge... more base desires.'
    $ tmpvar = int(200 / 100 * (100 - DialogueDros().discount))
    if tmpvar == 200:
        DROS @talk "Two hundred coins."
    elif tmpvar == 160:
        DROS @talk "A hundred-sixty coin."
    menu:
        "There you go" (Req_Gold = tmpvar):
            $ PlayerRemItem("gold", tmpvar)
            $ tmpvar = {}
            DROS @talk 'Good, come back in a couple days to pick it up.'
            $ NoteLock("VesLingerie")
            $ NoteUnlock("VesLingerieInProg")
            $ RomanceVes().cooldownDay = GetGameDay()+ 2
            $ RomanceVes().lingerie += 1
            return
        "On second thought...":
            $ tmpvar = {}
            return

label rom_Ves_7_GetLingInProgress:
    DROS @talk "Still working on it."
    DROS @talk "Come back later."
    return

label rom_Ves_7_GetLingReady:
    DROS @talk "Ahh, yes, it's ready."
    $ NoteLock("VesLingerieInProg")
    $ NoteUnlock("VesLingerieReady")
    DROS @talk "There you go..."
    $ RomanceVes().lingerie += 1
    return

label rom_Ves_7_GetLingGive:
    $ RomanceVes().lingerie += 1
    $ NoteLock("VesLingerieReady")
    VES @talk 'E-Eh?!'
    VES @talk 'What... What is this?'
    MC @talk 'It’s called lingerie.'
    VES @talk '{i}You...{/i} want me to wear this?'
    MC @talk 'Well, I think you’d look great in it but—'
    VES @talk 'How much did you spend on this?'
    MC @talk 'Does it matter?'
    VES @talk 'You shouldn’t spend your gold on me like this...'
    MC @talk '{i}I wanted to.{/i}'
    VES @talk '... W-Well... I... I could try it on sometime, I suppose.'
    $ CharChangeRel("ves", 1)
    VES @talk 'Alright... Just... Wait outside the tent while I get changed.'
    #SCENE FADES TO BLACK – TEXT APPEARS ON SCREEN –
    scene black with dissolve
    "Ten minutes later..."
    VES @talk 'You can come in now!'
    $ CharSetClothes("ves", "ling")
    $ LocFlush()
    with dissolve
    show ves:
        xcenter 0.5
    with dissolve
    'As I stepped into the tent, Ves stood there nervously, awkwardly shifting her weight from one foot to the other in the black lingerie as she struggled to maintain eye contact.'
    VES @talk 'Does this... look good?'
    VES @talk 'Orcs don’t really wear garments such as this...'
    "Ves’ eyes widened when she saw my hard-on standing to attention, my eyes hungrily looking her up and down."
    VES @talk 'Well... I guess that answers that.'
    VES @talk 'I had this idea for a position that I think we’ll both like.'
    VES @talk 'Come, lie down on the floor.'
    scene black with dissolve
    #SCENE FADES TO BLACK.
    VES @talk 'Hold still! Don’t move!'
    MC @talk 'Ves, are you—'
    MC @talk 'Mmmff!'
    $ RomanceVes().wearsLing = True
    call ves_sex69 from _call_ves_sex69
