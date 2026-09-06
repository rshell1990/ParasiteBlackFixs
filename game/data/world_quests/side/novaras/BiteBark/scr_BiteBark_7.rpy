#Scene 8 Elven shop
#New dialogue option for Dros
label qst_BiteBark_7_DrosLines:
    show dros at cright_f with dissolve
    show mc at cleft with easeinleft
    DROS @angry "Hm? Well light armour isn't really my thing... speak to a blacksmith or something."
    MC @talk "I'm afraid the situation is quite delicate."
    MC @talk "And I don't think I could trust another human with the matter."
    'Dros raised a curious eyebrow.'
    DROS @talk "...Well don't leave me in suspense."
    MC @talk 'I think it would be better if you just saw.'
    MC @talk "Elena! It's safe to enter."
    #Elena enters into the shop in her wolf form.
    show elena_w with easeinleft:
        xcenter 0.2
    DROS @angry "...Oh no, I don't do pet armour, certainly not."
    play sound "audio/cfx/detect_magic.ogg"
    scene black with flash
    'As Elena transformed before Dros, he jumped backwards in surprise, his eyes wide at the wolf girl before him.'
    $ LocFlush()
    show mc:
        xcenter 0.15
    show dros at cright_f
    show elena:
        xcenter 0.3
    with dissolve
    ELENA @grumpy 'Then it is good that I am no pet Elf.'
    'Dros looked over to me in bewilderment as I shrugged.'
    DROS @shock 'How in all the fucking gods wills did you find a Lycanite?'
    MC @surprised 'Lycanite?'
    ELENA @shock 'Is that what my people are called?'
    DROS @talk "You mean you don't actually know?"
    ELENA @sad "I've never seen another of my own kind."
    DROS @talk "I'm not surprised, secretive bunch."
    ELENA @sad 'Wait, you know where to find my people?'
    DROS @talk 'Nope.'
    ELENA @talk 'But you-'
    DROS @talk 'I am an elf dear, centuries old.'
    DROS @talk 'The last one of your kind I ran into was over a century and a half ago.'
    DROS @talk 'Interesting fellow, never saw him again.'
    "Elena's face dropped sullenly, some brief hope in her eyes dimming once again."
    ELENA @sad 'I see.'
    DROS @talk '...So, you need some type of outfit I suppose if you intend to be traipsing around with this one?'
    ELENA @grumpy 'Yes.'
    DROS @talk '...Hm, well, come back here and let me take your measurements then.' #Brief fade to black
    hide elena
    hide dros
    with easeoutright
    'Elena followed Dros over to some corner where he began to take her measurements, jotting down the details as he went.'

    show dros at cright_f with easeinright
    DROS @talk 'All done.'
    DROS @talk 'Yes, I think I can draft up some simple armour for her.'
    DROS @smile 'Six hundred coins.'
    MC @surprised 'Are you mad?!'
    DROS @angry 'You are the one who came to me!'
    DROS @angry 'Armour is not my speciality! The materials I need along with the time needed to produce this thing are quite intense!'
    DROS @angry 'Now either fuck off and find someone else to do it or pay me my coin!'
    MC @talk 'Hmph, fine elf, this better be worth it.'
    DROS @talk 'Of that, I can assure you.'
    if PlayerItemQty('gold') >= 600:
        menu:
            'Here, I have the coin.':
                DROS @talk 'Excellent! I will begin work shortly... Check back in a few days.'
                $ PlayerRemItem("gold", 600)
                $ QstSetProgress(QstBiteBark, 7)
                $ QstBiteBark().DrosArmorDayToComplete = GetGameDay() + 2
                $ LocEnter()
            'I will return with the coin when I have it.':
                DROS @talk "Don't take too long, I have a growing client list you know..."
                $ QstBiteBark().DrosRevisit = True
                $ LocEnter()
    MC '(Gonna find six hundred now...)'
    $ QstBiteBark().DrosRevisit = True
    $ LocEnter()

label qst_BiteBark_7_DrosLinesRevisit:
    $ tmpvar = int(600 / 100 * (100 - DialogueDros().discount))
    DROS @talk "Coin first... Work after, [tmpvar] coins."
    if PlayerItemQty("gold") >= tmpvar:
        menu:
            'Here, I have the coin.':
                DROS @talk 'Excellent! I will begin work shortly... Check back in a few days.'
                $ PlayerRemItem('gold', tmpvar)
                $ tmpvar = {}
                $ QstSetProgress(QstBiteBark, 7)
                $ QstBiteBark().DrosArmorDayToComplete = GetGameDay() + 2
                $ LocEnter()
            'I will return with the coin when I have it.':
                $ tmpvar = {}
                DROS @talk "Don't take too long, I have a growing client list you know..."
                $ LocEnter()
    $ tmpvar = {}
    MC @talk 'Got it.'
    $ LocEnter()

label qst_BiteBark_7_DrosNeedCrystal:
    DROS @talk "Look, I can't work without the power crystal!"
    DROS @angry "{b}Get it!{/b}"
    return

label qst_BiteBark_7_DrosLinesComeBackLater:
    DROS @talk "Her armour isn't ready yet, come back later."
    MC @talk 'Alright.'
    DROS @talk "Anything else?"
    return

label qst_BiteBark_7_DrosLinesArmourDone:
    #Once armour is ready
    $ CharSetClothes("elena", "naked")
    DROS @talk 'Ah yes, here you go.'
    DROS @talk 'Would the young... Uh... Wolf lady like to try it on?'
    show elena with easeinleft:
        xcenter 0.15
    ELENA @talk '...If I must.'
    scene black with dissolve
    #Cuts to black, camera pan from feet to head shot of Elena in her new outfit.
    $ CharSetClothes("elena", "normal")
    show elena at sexy_flyby_upwards(-100) with dissolve:
        xcenter 0.5
    $ Pause()
    $ LocFlush()
    show dros at cright_f
    show mc:
        xcenter 0.15
    show elena:
        xcenter 0.35
    with dissolve
    DROS @smile "I must say, I've done remarkably well!"
    DROS @talk 'Well, what do you both think?'
    MC @smile "It's perfect."
    ELENA @talk "It's... surprisingly comfortable."
    DROS @talk "Yes well, you're both very welcome."
    DROS @talk "Now if you don't mind, I have other works to attend to."
    hide dros with dissolve
    ELENA @talk "I'll be waiting at your home, [player_name!t]."
    MC @talk "Okay, I'll catch up with you soon."
    hide elena with easeoutright
    "As Elena left in her new outfit, I couldn't help but admire the elf's work."
    "He did made her look beautiful."
    $ CharChangeRel("elena", 1)
    $ QstComplete(QstBiteBark)
    $ QstStart(DialogueElena)
    $ LocEnter()
