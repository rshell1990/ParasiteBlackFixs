label rom_Elena_WaterCold:
    "Elena's eyes seemed to dim slightly, her whole body slumping slightly as she awkwardly looked away in rejection."
    ELENA @sad 'Oh...'
    ELENA @sad 'I understand.'
    ELENA @grumpy 'Umm, I shall be out shortly.'
    "With that Elena headed into [regina_ref!t]'s room, where I heard the continuous pouring of water."
    hide elena with dissolve
    MC '(Hm... Perhaps I need to set some boundaries with Elena.)'
    MC '(That is... {i}If I want boundaries{/i}.)'
    'A short while later, a mostly dried off Elena re-emerged.'
    show elena at left with dissolve
    ELENA @talk 'Thank you for that [player_name!t].'
    ELENA @talk "I'll go back to reading my book now..."
    menu:
        'Elena, wait!':
            'Elena turned to look at me.'
            ELENA @sad 'Huh?'
            "Suddenly moving forward, I placed my lips onto Elena's."
            hide mc
            hide elena
            with dissolve
            show cg_mc_elena_kiss_armor with dissolve
            "Elena's eyes widened in shock as her cheeks blushed."
            ELENA "Mhmm?!"
            'Pulling back from her, Elena broke free from my grasp.'
            hide cg_mc_elena_kiss_armor with dissolve
            show mc at cright_f
            show elena at cleft
            with dissolve
            ELENA @shock 'You... Why did you do that?!'
            MC @talk 'Because I wanted to.'
            ELENA @lewd "You... I don't understand."
            ELENA @shock "You... You didn't join me earlier!"
            ELENA @grumpy 'I... I thought...'
            'Elena shook her head and hurried off into my room, slamming the door behind her.'
            hide elena
            with dissolve
            MC 'Elena!'
            ELENA 'Leave me alone!'
            MC @sad '(What was I thinking?)'
            MC @sad "(Now I've just given her mixed messages... Damn it, I really need to make my mind up on what {i}we{/i} are.)"
            $ CharSetLover("elena")
            $ CharAddRelEntry("elena", "romance")
            $ CharChangeRel("elena", 1)
            $ LocEnter()
        '{image=[ICON.HEART_CROSS]} Enjoy your book, Elena.':
            ELENA @talk 'Mmm, will do.'
            'Elena gently closed the door to my room behind her.'
            MC "(Yes, it's best not to over-complicate things.)"
            MC "(Remaining just friends and allies is the best course... for the both of us.)"
            $ QstComplete(RomanceElena)
            $ LocEnter()