label qst_DaughterOfMetal_01:
    show mc at cleft
    show arlena at cright_f
    with dissolve
    ARLENA 'You’ve been busy lately...'
    menu:
        'Here to give me more shit?':
            ARLENA 'See this is what I’m talking about!'
            ARLENA 'You’re such a fucking ass at times.'
            MC @talk 'Oh, yeah, because you’ve been so friendly?'
        'What do you want now, Arlena?':
            ARLENA 'Nice to see you too, asshole.'
    ARLENA 'Well... I actually wanted to know if you were free after dark.'
    MC @talk 'Free? For what?'
    ARLENA 'A few of us are meeting at the {i}Iron Unicorn{/i}.'
    ARLENA 'I figured you might want to join us.'
    ARLENA 'You know, when you’re all done swallowing the swords of noblemen.'
    MC @talk '... You’re inviting me out?'
    ARLENA 'Yes.'
    MC @talk '... To have some drinks?'
    ARLENA 'Yes.'
    MC @talk '... So, you want me and you to—'
    ARLENA 'Gods be fucking damned! YES! I am inviting you out, idiot!'
    ARLENA 'Get that into your thick skull.'
    'I reached out to touch Arlena’s forehead before she slapped my hand away, a look of disgust on her face.'
    ARLENA 'What are you doing?'
    MC @talk 'Just making sure you aren’t suffering a fever right now.'
    ARLENA 'Urgh... Turn up, don’t turn up.'
    ARLENA 'I don’t give a shit.'
    hide arlena with easeoutright
    'With that, Arlena strode back inside, presumably to work out her annoyance at me by hammering the shit out of something on an anvil.'
    MC '... Well... that was unexpected.'
    MC 'It might be worth joining Arlena and the others later if this is her way of holding out an olive branch.'
    MC '... That is, if I even want to accept it.'
    hide mc
    hide arlena
    with dissolve
    return
