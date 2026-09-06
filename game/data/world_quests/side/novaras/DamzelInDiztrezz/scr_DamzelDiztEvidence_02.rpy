label scr_nijah_damzelDizztrezz_evidenceFollowTheMan:
    'You notice a suspiciously-looking man, no doubt a Vulshan, head off down one of the many winding back alleyways through the marketplace.'
    'Do you follow him? You have a strong sense it will be dangerous...'
    menu:
        'Follow the man...': #Continues
            jump scr_nijah_damzelDizztrezz_evidenceFollowTheMan_cont
        'Do nothing.':
            $ LocEnterQ()

label scr_nijah_damzelDizztrezz_evidenceFollowTheMan_cont:
    scene black with dissolve
    'Stalking the man through the many winding alleyways, I nearly lost him multiple times through the labyrinth like turns as we descended deeper into the bowels of the city.'
    'Finally, I hide behind a wall as the man arrived upon some upon some small opening where the buildings converged.'
    'From the shadows, the Khazahs and Vulshan appeared.'
    scene cg_spy with dissolve
    KHAZAH_LEADER 'So... Have you thought more on our terms?'
    VULSHAN_LEADER 'We have, yet there is still much to be discussed.'
    KHAZAH_LEADER 'What is the problem now?'
    KHAZAH_LEADER 'This is the problem with you Vulshans, so... hesitant.'
    VULSHAN_LEADER 'Our will is as strong as yours, do not doubt that.'
    VULSHAN_LEADER 'But we are not so reckless as to throw ourselves to any cause for short term coin... Like a Khazhah.'
    KHAZAH_LEADER "Tsch, fool."
    KHAZAH_LEADER "Tarek's days are numbered, the Boshu, the Tumak, even the Zatsu are turning."
    KHAZAH_LEADER 'They stand with us as long as we are willing to absorb them into our ranks.'
    VULSHAN_LEADER 'He has done much for us, without him, you and I would still be spilling each others blood right now...'
    KHAZAH_LEADER 'He will be the death of us.'
    KHAZAH_LEADER 'He knows we are the biggest threat to his power and he seeks to weaken us.'
    VULSHAN_LEADER 'Your proof? The Vulshan made a vow, we are honor bound to-'
    KHAZAH_LEADER 'There is no time for honor Vulshan.'
    KHAZAH_LEADER 'He plans to split our territories further with the lesser factions, with us further fractured, he believes he will be able to control us easier.'
    VULSHAN_LEADER 'And your proof of this?'
    'The Khazah pulled from his robes a scroll which he tossed over towards the Vulshan leader who picked it up and began reading it.'
    KHAZAH_LEADER 'One of our spies stole this from his office, a letter he sent secretly to the Yahvom.'
    KHAZAH_LEADER 'Satisfied?'
    VULSHAN_LEADER '...Yes, this will suffice.'
    MC "(That's the proof I need.)"
    KHAZAH_LEADER 'Good, then in the next three days, we shall-'
    'Stepping onto a piece of glass accidentally beneath my feet, the loud crunching sound alerting the men to my presence.'
    play sound "audio/cfx/mgs_alert.ogg"
    MC '(Fuck!)'
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusic("audio/music/31_Encounter.ogg")
    KHAZAH_LEADER 'A SPY! QUICKLY!'

    $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys", CharIDList_Right = ["e_bandit", "e_thug"]))

    'With the last of the men bloodied and dead on the ground, I reached down to pluck the bloodied scroll from one of their hands.'
    $ LocFlush(dissolve)
    $ PlayerAddItem("qst_tarek_bloody_scroll", 1)
    MC '(I just hope this suffices enough for evidence...)'
    $ AutoMus(True)
    $ QstSetProgress(QstDamzelInDiztrezz, 3)
    $ GoalComplete(QstDamzelInDiztrezz, 8)
    $ GoalShow(QstDamzelInDiztrezz, 9)
    $ LocEnterQ()