label qst_DamzelDizzt_3_sellNijah:
    MC @talk 'How much for the girl?'
    TAREK 'Oh, you have to collect a reward?'
    MC @talk "I can always just leave with her if you don't want her."
    TAREK @angry 'And I can just kill you and take her for free.'
    MC @talk 'Try it.'
    TAREK @smile '...Hahaha!'
    TAREK @smile 'Well, I am a fair man.'
    TAREK 'I shall give you a thousand coins for her.'
    MC @talk 'Deal.'
    MC 'Markus turned to look dumbfounded at me, somewhere between disbelief and uncertainty as to what was happening but he stayed quiet.'
    $ PlayerAddItem("gold", 1000)
    MC 'After Tarek handed me over the gold, he reached and pulled Nijah towards him, who suddenly became aghast in horror once she realized she had been betrayed.'
    NIJAH @sad 'You... You lie to me!'
    MC @talk "Sorry Nijah, it's just business."
    NIJAH @angry 'YOU BASTARDS!'
    TAREK @angry 'Quiet girl!'
    TAREK 'You two leave us now, our business is concluded.'
    NIJAH @sad "No... Please... Don't do this!"
    scene black with dissolve
    NIJAH "Please! PLEASE DON'T GO!"
    NIJAH 'PLEASEEEEEEEEE!'
    $ Pause()
    $ LocSet("novaras_dist_pleasure")
    $ LocFlush(dissolve)
    $ QstComplete(PrimerDamzelInDiztrezz)
    $ QstDamzelInDiztrezz().PlayerSoldNijah = True
    $ QstComplete(QstDamzelInDiztrezz)
    $ QstComplete(EventNijahRescue)
    $ NoteLock("NijahStayingAtMCs")
    $ CharAddRelEntry("nijah", "sold_to_tarek")
    $ HouseLockBlackDiamond().canExit = True
    $ BlockWaitDynamic(False)
    show mc at cleft
    show markus at cright_f
    with dissolve
    #Scene cut to outside the Black Diamond
    MC "As we left the Black Diamond, I felt Markus' hands grip around me as he pushed me against a wall."
    MARKUS @angry 'What the fuck was that back there?'
    MC @talk 'What?'
    MARKUS @angry 'All that bullshit about saving her and you just sell her out?!'
    MC @talk 'I did what I had to do, we need the coin.'
    'Markus loosened his grip.'
    MARKUS @angry 'Next time you plan on doing something like that, you do it without me, understand?'
    MARKUS @angry "I won't be a part of enslaving people."
    MC @angry "We'll need to do terrible things sometimes if we're going to survive."
    MARKUS @angry "Tsch, some 'heroes' we are..."
    MARKUS @angry 'Just leave me alone, I need some time to think on this...'
    hide markus with dissolve
    #Markus leaves
    MC '...'
    $ CharChangeRel("markus", -1)
    $ LocEnter()
