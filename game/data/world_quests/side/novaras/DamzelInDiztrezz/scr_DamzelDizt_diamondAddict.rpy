label qst_DamzelDizzt_3_RazaAddict:
    RAZA_ADDICT '{i}*Mumbles*{/i}'
    MC "(He's in no fit state to even stand, let alone hold a conversation.)"
    RAZA_ADDICT 'Helloooo friend, could you spare some coin so I might have more Raza?'
    RAZA_ADDICT "The raza here is sooo good, you're in for a treat friend! Haha!"
    RAZA_ADDICT 'Unlike that Vulshan shit.'
    MC "What's wrong with the Vulshan's product?"
    RAZA_ADDICT "Help a friend out, and I'll tell you..."
    if PlayerItemQty("gold") >= 30:
        menu:
            'Here, have some coin.' (Req_Gold = 30):
                $ PlayerRemItem("gold", 30)
                RAZA_ADDICT 'Much obliged friend!'
                RAZA_ADDICT 'The Vulshan are crumbling, their product is more and more impure because the Khazahs are pushing them out of vital territories and resources.'
                RAZA_ADDICT "Now they're in-fighting amongst themselves, won't be long now."
                RAZA_ADDICT "Shittest Raza I've ever had from them these last few months."
                MC @talk 'I see.'
                MC '(I might be able to use this information to my advantage somehow.)'
                $ QstDamzelInDiztrezz().addictInfo = True
                $ GoalShow(QstDamzelInDiztrezz, 5)
                $ LocEnterQ()
            'Nevermind.':
                RAZA_ADDICT 'Suit yourself...'
                $ LocEnterQ()
    else:
        'Perhaps if I had some gold on me...'
        MC "Can't, sorry."
        RAZA_ADDICT 'Suit yourself...'
        $ LocEnterQ()

label qst_DamzelDizzt_3_RazaAddict_gaveMoney:
    RAZA_ADDICT "Friend! You're the best... {i}*Incoherent mumbles*{/i}"
    MC "(He seems to have already spent my humble donation.)"
    $ LocEnterQ()
