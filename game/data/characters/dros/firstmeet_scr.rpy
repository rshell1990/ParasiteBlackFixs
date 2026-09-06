label scr_first_meet_dros:
    show mc at left
    show dros angry at cright_f
    with dissolve
    UNKNOWN 'No, no, NO!'
    show dros angry
    UNKNOWN 'This is entirely unacceptable!'
    MC surprised '...'
    show dros angry
    UNKNOWN 'Tsch! What the hell do you want?'
    show mc
    MC @talk 'That’s no way to speak to a potential customer.'
    show dros angry
    UNKNOWN 'Bah! The rags store is that way.'
    menu:
        'Fuck off, you pointy eared cunt.':
            show dros angry
            UNKNOWN  'The human tongue showing how elegant it is, as ever, I see...'
        'What’s your problem?':
            show dros angry
            UNKNOWN 'My problem is I am surrounded by idiots and uncultured swine!'
        'Fine, I’m leaving.':
            pass
    show dros
    UNKNOWN '...'
    show dros talk
    UNKNOWN '... Wait, wait!'
    show dros talk
    UNKNOWN 'You look like a man who could do some dirty work—'
    show dros talk
    UNKNOWN 'I mean, the ‘hard, noble’ work... Yes, that’s what you humans like to hear, right?'
    MC @talk 'Would you just get on with telling me what you want?'
    DROS @talk 'My name is Dros Ulvrak, the LEGENDARY tailor of Synmaria!'
    MC '...'
    DROS '...'
    MC @talk 'Never heard of you.'
    DROS @angry 'OF COURSE YOU HAVEN’T YOU UNCULTURED—'
    DROS @talk 'Ahem! Okay, human... Allow me to speak plainly.'
    DROS @talk 'I need your help.'
    $ CharMeet("dros")
    $ choicemenu = ["a", "b"]
label scr_first_meet_dros_menu:
    menu:
        'What is an elf like yourself doing in Novaras?' if 'a' in choicemenu:
            $ choicemenu.remove("a")
            DROS @talk 'I was sent here by King Maran as part of a new trade initiative Emperor Alcott secured.'
            DROS @talk 'I’ve been sent to this backwater specifically, to help streamline production of tunics and such.'
            DROS @talk 'But that’s not where the real gold is...'
            jump scr_first_meet_dros_menu
        'What’s in it for me?' if "b" in choicemenu:
            $ choicemenu.remove("b")
            DROS @talk 'Does the promise of immediate gold sound gratifying?'
            MC @talk    'Depends on how heavy the sack is...'
            DROS @talk 'How about three hundred gold pieces?'
            MC '... Hmm...'
            DROS @talk 'Then how about I guarantee to make EVERY woman in this godforsaken realm more... appealing?'
            MC @talk '... If this is some weird black magic potion—'
            DROS @angry 'IT’S NOT BLACK MAGIC YOU—'
            DROS @talk 'Ahem. No... Get your mind out of the gutter.'
            DROS @talk 'It is perfectly legal and of a much higher class than any wretched perverse spell by one of your gods.'
            jump scr_first_meet_dros_menu
        'What’s do you want?' if choicemenu == []:
            pass
    DROS @talk 'Have you noticed what the women of these lands wear?'
    MC  '...'
    DROS @talk '... If you say—'
    MC @talk '... Clothes?'
    DROS @angry 'OF COURSE THEY WEAR—'
    DROS @talk 'No... No... You can’t help it, it’s fine...'
    DROS @talk 'Okay, yes... The women of this land wear clothes.'
    DROS @talk 'Unstylish, dull, drab clothes.'
    DROS @talk 'And gods can only imagine the abominations they wear beneath.'
    MC @talk 'Is this going somewhere?'
    DROS @talk 'Yes, it is, so pay close attention... Now, while elvish women wouldn’t be seen dead in half of the clothes you and your kin wear...'
    DROS @talk 'I believe the women here have at least a vague idea of what good clothes ought to look like!'
    MC @talk '... Right.'
    DROS @talk 'Now... I am capable of producing high quality wears for women that are far superior the potato sacks they currently find themselves wearing.'
    DROS @talk 'I believe a lot of women would be interested in such clothes... They’re immensely popular in Synmaria, especially the lingerie.'
    MC @talk 'The what?'
    DROS @talk 'It’s... Never mind, your primitive brain would no doubt explode if I were to describe it.'
    DROS @talk 'Let’s just say you’ll enjoy it when you see it.'
    MC @talk 'I’m going to hit you very hard in a moment.'
    DROS @talk 'SHOULD you assist me, not only will you get gold, but I’ll give you a discount on some of our more private wears that you can gift to your whore— I mean, uh, ‘beloved’.'
    MC @talk 'So, where do I come into this?'
    DROS @talk 'It’s quite simple really...'
    DROS @talk 'Some of my machines are a little... ‘twitchy’, to say the least.'
    DROS @talk 'Without an adequate power source, they can’t function properly.'
    DROS @talk 'So, I am in need of some assistance to keep this place running...'
    MC @talk 'Okay... And?'
    DROS @talk 'The Mages Guild is able to provide a power crystal I can use to charge this place.'
    MC @talk 'Then why don’t you just go and ask them? Why me?'
    DROS @angry 'BECAUSE...'
    DROS @angry 'Apparently, they cannot sell them directly to foreign emissaries! Can you believe that?'
    DROS @talk '... And, uh, I may or may not be welcome there any longer after a little mishap where I tried to break in and, uh...'
    MC '...'
    DROS @talk 'Never mind! I’m sure all is forgiven!'
    DROS @talk 'Just return when you have one of the crystals.'
    MC @talk 'Okay, got it.'
    return
