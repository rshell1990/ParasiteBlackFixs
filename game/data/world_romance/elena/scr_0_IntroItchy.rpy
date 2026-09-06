label rom_Elena_ItchyIntro:
    #Scene 19 - MC Bedroom - Evening
    #Random event 1-2 days later after A WOMANS TOUCH quest
    show elena  at center_f with dissolve
    ELENA @angry 'Itchy... Itchy!'
    MC @talk 'Is something the matter?'
    ELENA @angry 'My fur!'
    ELENA @grumpy 'Gods, its been so long since I bathed.'
    ELENA @grumpy "It's beginning to stick and-"
    'Elena furiously clawed at herself.'
    ELENA @angry 'GAHHH!'
    MC @talk 'Well, we do have a tub in the house...'
    MC @talk "But I'd need to come up with some excuse to have [regina_ref!t] leave the house!"
    ELENA @shock "Gods {i}please!{/i} I beg you!"
    ELENA @angry 'This is insufferable!'
    MC @talk 'Alright, calm yourself.'
    MC @talk 'I will see what I can do.'
    $ NoteUnlock("ElenaRomanceGetReginaOut")
    $ QstSetProgress(RomanceElena, 1)
    $ LocEnter()
