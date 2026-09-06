label rom_Ves_4_HuntPitch:
    $ NoteLock("VesRomance2")
    show ves at cright_f
    with dissolve
    show mc at cleft 
    with dissolve
    VES @talk '[player_name!t]!'
    MC @talk 'Wow, you remembered my name this time!'
    show ves smile
    'Ves giggled at the comment, hastily adding...'
    VES @smile_talk 'I was wondering perhaps if you wished to attend a hunt with me.'
    MC @surprised 'A hunt?'
    show ves
    VES @talk 'There are some Skorn not far from here.'
    VES @talk 'If you wish to accompany me, we could bring one down together and share in the glory.'
    VES @talk  'That is... if you want to, of course.'
    'Ves played with her hair as she spoke, twirling it between her thumb and forefinger.'
    VES @talk 'Are you ready to begin the hunt?'
    menu:
        "Alright, I’ll join you.":
            $ QstSetProgress(RomanceVes, 9)
            jump qst_ValleyOfPrey # to quest directly
        "I need some time to prepare...":
            VES @talk 'Let me know when you are stocked for the hunt.'
            $ QstSetProgress(RomanceVes, 9)
            $ LocEnter()

label rom_Ves_4_HuntPitchRev:
    VES @talk "Oh, sure!"
    VES @talk 'There are some Skorn not far from here.'
    VES @talk 'If you wish to accompany me, we could bring one down together and share in the glory.'
    VES @talk 'Are you ready?'
    menu:
        "Alright, let's move out.":
            $ QstSetProgress(RomanceVes, 9)
            jump qst_ValleyOfPrey # to quest directly
        "Not quite...":
            VES @talk 'Let me know when you are stocked for the hunt.'
            $ LocEnter()