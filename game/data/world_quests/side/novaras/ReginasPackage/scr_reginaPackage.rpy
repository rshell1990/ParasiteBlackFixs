label blacksmithscene1:
    'As the door of the Blacksmiths creaked open, the heat blast forced me back.'
    'Arlena and her father, Drax, hammered relentlessly at some iron blades.'
    show mc at cleft with dissolve
    'When they looked up and spotted me, Drax placed the hot blade into some water where it sizzled, and the hulking man sauntered over to me.'
    show drax at cright_f with dissolve
    DRAX 'That you, boy?'
    MC @talk 'Good to see you again, Drax.'
    DRAX 'Ahhh! Glad to see you doing so well...'
    'Drax was short, muscular man, sturdy in shape, he reminded me of a bull.'
    'His head was shaved bald and his wiry eyebrows stood out like slugs on his face.'
    'He had a thick handlebar moustache that sat atop his neck hair and grew down to his chest before merging with the dark curly hair that protruded from his shirt.'
    'With his leathery brown gloves, he wiped off any dirt onto his apron as he approached me and reached out to shake my hand with an easy grin.'
    $ CharMeet("drax")
    DRAX 'You and that Markus boy been the talk of the town you know!'
    MC @talk 'We have?'
    DRAX 'Ha! Just ask Arlena here...'
    DRAX 'ARLENA! GET OVER HERE! '
    show arlena at right_f with easeinright
    'Arlena was already throwing off the protective mask and strode over to me, sweat dripping down her face.'
    'Despite sharing classes in school, we never really got on.'
    'Arlena was always more of a rough and ready type person.'
    'To her, me and Markus thought we were better than everyone else with our plans.'
    'To us, we just wanted a chance to never go hungry again.'
    $ CharMeet("arlena")
    'With her arms folded, she stoically remarked as she approached me...'
    ARLENA 'I’ve heard...'
    ARLENA 'So, how’d you both really survive? Hiding under a rock I take it?'
    menu:
        'We fought our way back.':
            ARLENA 'Of course you did.'
            'Arlena rolled her eyes in exaggerated disbelief.'
            DRAX 'Arlena!'
        'Why do you care?':
            ARLENA 'I don’t, I’m just sick of hearing about it.'
            ARLENA 'Not when we both know you probably—'
            DRAX 'Arlena... Watch it, girl.'
            ARLENA 'Tsch!'
        'Nice to see you, too.':
            ARLENA '... Hmph.'
    'Arlena looked me up and down unabashed.'
    ARLENA 'I’ve never seen a Scout come back looking so...'
    ARLENA '{i}Big.{/i}'
    MC @talk 'Uhh, lots of eating and fighting tends to do that.'
    'Arlena offered nothing more than a blank, inexpressive response of ‘Hm’ till her father piped up.'
    DRAX 'So, what can I do for you?'
    MC @talk '[regina_ref_cap!t] ordered something here not long ago, I’m here to pick it up.'
    DRAX 'Hmm... Slight bit of a problem there.'
    MC @talk '... Which is?'
    DRAX 'We’re running low on bronze, still waiting on the ore to arrive.'
    MC @talk '... Great.'
    ARLENA 'If you’re feeling brave though, Hero, most of the weaker Demorai tend to have some small bronze armour pieces stitched together to wear.'
    ARLENA 'Give you a chance to practice all that fighting...'
    ARLENA 'If you bring us some, we can fashion what you need.'
    DRAX 'Aye, we have the mould for it, it’s just the raw material we need.'
    MC @talk 'Not a problem, I’ll see what I can do.'
    ARLENA 'And the best part is! If you get eaten out there...'
    ARLENA 'I never have to see you again!'
    DRAX 'ARLENA!'
    hide arlena with easeoutright
    'Arlena turned to head back towards one of the anvils, humming happily to herself.'
    DRAX 'Girl, you are driving my patience with your attitude! '
    DRAX 'Bah! Ignore her.'
    DRAX 'She’ll make a fine blacksmith one day...'
    DRAX 'But may the gods help whoever ends up marrying her.'
    MC @talk 'She’s a fiery one, for sure.'
    MC @talk 'I’ll be back shortly with the bronze scraps.'
    DRAX 'Good! And send Regina our regards, we hope she is well.'
    MC @talk 'Will do.'
    $ LocSet("novaras_dist_farm")
    return

label qstReginaPackage_DraxCollectedBronze:
    DRAX 'Ah! Good! '
    DRAX 'ARLENAAAAA!'
    ARLENA 'WHATTT!'
    DRAX 'WE HAVE BRONZE! '
    show arlena at right_f with easeinright
    'Arlena emerged once again with her arms folded.'
    ARLENA 'Well, I see you didn’t get yourself killed... '
    ARLENA '{i}Unfortunately.{/i}'
    menu:
        'It takes more than a few Demorai to take me down.':
            ARLENA 'Tough words for someone who was only ever interested on sucking on noble tit.'
            DRAX 'Arlena! That’s enough from you, girl! '
            DRAX 'I don’t see you going out axe in hand to fight Demorai!'
            ARLENA 'Fine! Then give me a blade and I’ll—'
            DRAX 'Pipe down, girl! '
            'Arlena growled.'
        'It wasn’t easy getting it.':
            ARLENA 'I don’t know, prying the armour from corpses of already slain enemies sounds pretty easy to me.'
            DRAX 'Arlena!'
            MC @talk 'I am not some grave robber.'
            MC @talk 'I can assure you, the only corpses I pried from were the ones I killed myself.'
            ARLENA 'If you say so...'

    #BOTH ROUTES CONTINUED:
    DRAX 'I will have Regina’s item ready for her by tomorrow.'
    DRAX 'Feel free to pick it up then.'

    $ QstSetProgress(QstReginaPackage, 2)
    $ QstSetDelay(QstReginaPackage, 1)
    MC @talk 'Thank you, Drax.'
    DRAX 'Remember, if you need some coin, you can always bring me more bronze scraps you find out there and I’ll pay you a fair price.'
    $ NoteUnlock("DraxBronze")
    ARLENA 'Father! '
    DRAX 'No arguing, Arlena!'
    DRAX 'The more metal we can get, the better, you know this, girl.'
    ARLENA 'Hmph, fine.'
    ARLENA 'I guess you might be useful for something at last.'
    hide arlena with easeoutright
    'As Arlena stormed off once again, Drax rolled his eyes, muttering to himself something along the lines of ‘that girl’.'
    DRAX 'I’ll see you soon, lad.'
    MC @talk 'See you soon, Drax.'
    $ LocSet('novaras_dist_farm')
    $ LocEnter()
