label ev_AdvGuildShowUpPostFaw_scr:
    show mc at right_f with easeinright
    MC "Yeah, that should be the place..."
    hide mc with easeoutleft

    $ LocSet("novaras_adv_guild")

    $ LocFlush(dissolve)

    show mc at cleft with easeinleft
    show markus at left with easeinleft
    if not CharInParty("markus"):
        $ EventAdventureGuildShowUp().MarkusWasInPartyAlready = False
        MARKUS "Hey there."
        show mc at blurin, shake, cleft_f
        MC @talk "Gosh!!! Were you following me?"
        MARKUS "Haha! No, just walked in myself. Could tell your new imposing figure from miles away."
        show mc at blurin, cleft
    MC @talk "Okay then... Let's get this over with."

    $ NoteLock("ShowUpAtAdventurersGuild")

    MC @talk 'How’s your brother faring?'
    MARKUS 'He’s taking a few days rest from the mines, wants to spend some time with me.'
    MARKUS 'Had some boar prepared for us both, would you believe it?'
    MC @talk 'What? A whole boar?'
    MC @talk "You should 'nearly die' more often."
    MARKUS 'Wouldn’t tell me how he got it, just said he was glad I was back.'
    'I smirked, his brother had always had a few connections with some of the shadier residents of Novaras, so being able to poach a whole boar for himself didn’t come as much of a shock.'
    MC @talk 'Who should we talk to around here?'
    MARKUS 'The girl at the front desk should handle every—'

    RANDOM_MAN 'IT’S CELESTE! EVERYONE! CELESTE HAS RETURNED!'
    'As the entire room began to rumble in anticipation, there was a mad rush to head outside and see the returning Hero.'
    'I glanced uncertainly at Markus who was now beaming with excitement.'
    MC @talk 'Celeste? Here?'
    MARKUS 'Come on! Let’s join the others!'
    scene black with dissolve
    $ HideUI(True)
    $ LocSet("novaras_dist_market")
    $ AutoMus(False)
    $ PlayMusic("audio/music/19_Celeste.ogg")
    $ LocFlush()
    show cg_celeste_return_party:
        yoffset 200
    with dissolve
    'Forcing our way out the front to join the gathering crowds of Heroes and common folk alike, the Hero, Celeste, and her party, ‘The Red Daggers’, returned to rapturous applause.'
    'Celeste and her legend seemed to grow day by day, her feats and accomplishments almost taking on a life of their own as stories of them were scattered through the streets of the city.'
    'In an age where Heroes seemed to either perish or fade away into obfuscation, Celeste was a bright star on the blackest night.'
    'And she was beautiful.'
    'Donning her ornate gold armour, she smiled and waved to the crowds, her soft, short hair hung down just past her chin, and my eyes were drawn curiously to how the color split, half a silvery white, and half black.'
    'Athletic yet graceful, many a young man dreamed of sharing Adventures with her.'
    'Many more fantasised of a budding, if explicit, romance where they no doubt wooed her with incredible feats of heroism.'
    'Behind her slugged the Red Arrows, a small band who seemed wearier than her, more stoic, exhibiting many scars and scratches across their faces and armour.'
    'Despite this, they still offered the occasional wave and faint smile of appreciation for the adoring fans.'
    'One of the Red Arrows, an archer riddled with scars, lingered further back than the rest.'
    'Keeping the hood of her green cloak firmly up, she seemed to offer nothing compared to her fellow warriors, not even a smile.'
    'As I studied her, intrigued, for the briefest of moments, her eyes seemed to meet mine and lock.'
    'Her features broke into what appeared to be a truly genuine smile before it took on an alluring and seductive tone.'
    'She averted her gaze, smiling warmly at the crowds for a second before retreating behind her hood once more.'
    'From between the feet of the crowd, a small child on the verge of tears rushed towards Celeste.'
    'Celeste looked curiously at the child as she crouched down to him.'
    hide cg_celeste_return_party
    show cg_celeste_return_kid
    with dissolve
    'A hush fell over the crowd, eager to hear what was being said.'
    CELESTE @laugh 'Hello there, young master!'
    'Celeste’s voice was soft yet dynamic, seductive yet commanding.'
    'People could listen to her for hours, especially men.'
    
    ERON 'Did you find my father’s ship?'
    CELESTE @talk 'Your father? What was his name child?'
    ERON 'Drona! Captain Drona!'
    'Celeste looked up muttering the name again and again in a theatrical display.'
    CELESTE @talk 'Ahh...'
    'She smiled playfully.'
    CELESTE @talk 'Then that must make you Master Eron.'
    ERON 'You... You know my name? '
    'Celeste smiled ardently and rose to address the crowd.'
    CELESTE @talk 'As some of you may know, we were sent to recover the wreckage of The Prophetic, which has been missing for the last three months.'
    CELESTE @talk 'We were doing this in the hopes of finding any survivors so as to return them to their families.'
    'There were some murmurs of acknowledgement mixed with a sense of unease that ran through the crowd, many had already heard the story of The Prophetic.'
    'Celeste’s smile radiated through the crowd as her voice rose.'
    CELESTE @talk 'We found the crew and they will ALL be returning home shortly!'
    'There was a tumultuous roar and cheers of applause as the child began to weep tears of joy, his grin apparent even from far away.'
    ERON 'My father’s coming home?!'
    CELESTE @talk 'Yes! Your father is coming home, Master Eron!'
    CELESTE @talk 'After being attacked by a pirate vessel, he and his crew washed up on a small island off the coast off Synmaria, surviving only on the fruits and vegetation they could scavenge.'
    CELESTE @talk 'But after a great battle with a Demorai ship, we recovered them all!'
    ERON 'Where is he!? Where is my father!'
    CELESTE @talk 'Why...'
    CELESTE @talk '{i}He’s right here!{/i}'
    'Celeste motioned behind her with her hand and the bedraggled crew of The Prophetic shuffled forward through the crowd.'
    'Upon seeing his father, the boy cried out in elation.'
    scene black with dissolve
    ERON 'FATHER!'
    CAPTAIN_DRONA 'Eron!'
    'As the boy rushed into the Captain’s arms, the crowd erupted into even wilder screams and shouts and Celeste raised both of her arms, revelling in the applause.'
    'Enthralled by what we’d just witnessed, it was impossible to take my eyes off Celeste as she commanded the attention of those around her with the potency of her sheer presence.'
    $ LocFlush()
    show celeste at center
    with dissolve
    CELESTE @talk 'PEOPLE OF NOVARAS!'
    CELESTE @talk 'CITIZENS OF ALDERAY!'
    CELESTE @talk ' HEAR ME NOW!'
    'The crowd fell silent once again as she spoke with fiery passion.'
    CELESTE @talk 'I have felt and shared in your pain these last few years and want you to know I stand not just with you...'
    CELESTE @talk 'BUT FOR YOU!'
    CELESTE @talk 'I will not rest until the plight of the Demorai ends and peace is restored upon our lands!'
    CELESTE @talk 'This nightmare shall end!'
    CELESTE @talk 'Be it against demon or beast my blade is your blade!'
    CELESTE @talk 'My blood is your blood!'
    CELESTE @talk 'And though the night belongs to them...'
    CELESTE @laugh 'I pledge to you; WE SHALL HAVE THE DAY!'
    'The crowd burst into utter jubilation.'
    'In a sea of mediocre Heroes taking about glory and honour that could, at best, gain a passive smirk or nod of approval, Celeste could rally any crowd into total furore.'

    $ LocSet("novaras_adv_guild")

    $ HideUI(False)
    $ LocFlush()

    show mc at left
    show markus at cleft
    with dissolve

    'Alive with excitement, we headed back into the Guild.'
    'As we did, Celeste passed by me, offering the briefest of glances that made my stomach turn in knots before the crowds shuffled in eagerly behind her.'
    MARKUS 'Whoa... she’s...'
    MARKUS '{i}Incredible.{/i}'
    'Shaking my head, I tried to regain some composure.'
    MARKUS 'Hey, do you think there’s maybe a girl down at the Pleasure District who looks a little like her?'

    $ AutoMus(True)    
    scene black with dissolve
    show text _("Half an hour of waiting later...") with dissolve:
        xalign 0.5
        yalign 0.5

    $ TimeAdvBy(TIME_05H)
    $ Pause()
    hide text

    $ LocFlush()

    show markus at left
    show mc at cleft
    with dissolve
    show thea at cright_f with easeinright
    UNKNOWN 'Hello there!'
    THEA 'My name’s Thea, how can I help you both today?'
    $ CharMeet("thea")
    MC @talk 'We’re the new Adventurers, I guess.'
    "Markus chuckled quietly."
    THEA 'Oh! You must be the two we were informed about!'
    THEA 'Let me be the first to welcome you to the Adventurers Guild!'
    THEA 'If you have any questions, now’s the time to ask them.'
    $ choicemenu = ['a','b','c']

    menu act1scene3menu:
        'How do we sign up for a quest?' if 'a' in choicemenu:
            $ choicemenu.remove('a')
            THEA 'Should you wish to embark on a quest, you need only put your name down on the Quest Board for whatever one it is you’re pursuing.'
            THEA 'Quests are ranked by their difficulty.'
            THEA 'The greater the difficulty, the greater the risk... and the reward.'
            jump act1scene3menu
        'Once we put our name down for a quest, are we the only ones who can pursue it?' if 'b' in choicemenu:
            $ choicemenu.remove('b')
            THEA 'Nope! Anyone who puts their name down is eligible to participate.'
            THEA 'Keep in mind that multiple parties may attempt the same quest, we {i}only{/i} reward the successful candidates.'
            THEA 'It’s also up to you to decide how to split any shares between yourselves, we offer a lump sum as reward.'
            jump act1scene3menu
        'How many Heroes are still active?' if 'c' in choicemenu:
            $ choicemenu.remove('c')
            THEA 'Now? Less than five hundred remain...'
            THEA 'I have to admit, it’s a far cry from the glory days of Newheart.'
            THEA 'Back then we nearly had two thousand Guild members running around! Can you believe that?'
            THEA 'But... we make do with what we have!'
            THEA 'And there are still some exciting new names making their own legends!'
            THEA 'Who knows... maybe you two will make a legend of yourselves!'
            jump act1scene3menu
        "That'd be all.":
            pass

    THEA 'Okay, glad to be of assistance!'
    THEA "I've got to return to my work now."
    hide thea with easeoutright
    MC @talk 'Well, at least that’s done now.'

    if EventAdventureGuildShowUp().MarkusWasInPartyAlready:
        MARKUS "Yeah, one headache less..."
    else:
        MARKUS "Yeah. Up for a drink later? Remember, you promised!"
        MC "But I didn't!"
        MARKUS "No, you did!"

    show mc at blurin, cleft_f
    show celeste at left with easeinleft
    'As we turned to leave, I bumped straight into Celeste who was busy dealing with her many adoring fans, regaling them with titillating details of her adventures.'
    show celeste at cright with easeoutright
    show mc at blurin, cleft
    'Spinning around sharply, her eyes met mine and for a moment, they were daggers.'
    'But just as quickly, she relaxed, an easy smile spread across her face.'
    CELESTE @talk 'I know you...'
    CELESTE @talk 'You two are the lone survivors, right?'
    'The crowd formed a captivated circle around us.'
    MARKUS 'That’s us, ma’am!'
    'Celeste laughed delicately.'
    CELESTE @talk 'Very impressive, boys!'
    CELESTE @talk 'You’ll have to tell me all about it the next time we meet.'
    CELESTE @talk 'Tell me...'
    CELESTE @talk 'What are your names?'
    'Her voice had an alluringly hypnotic quality to it.'
    MC @talk 'I’m [player_name!t], and this is my friend Markus.'
    'Celeste said my name, letting her tongue twist and twirl around it.'
    'Something about the way she said it was... {i}appealing{/i}.'
    CELESTE @talk 'Well... {i}I{/i} look forward to meeting you again.'
    CELESTE @talk 'Perhaps we will get to have Adventures with one another soon?'
    'I blushed crimson at the thought, something in her eyes made me feel a tinge of excitement that I hoped no one would notice as it pressed against my trousers.'
    MARKUS 'We’d love to, ma’am! Anytime just let us know!'
    'Celeste laughed once again.'
    CELESTE @talk 'I look forward to it...'
    CELESTE @talk 'Now, if you’ll excuse me.'

    $ CharMeet("celeste")
    hide celeste with easeoutright

    'As Celeste made her way past me, I caught her sweet scent and felt myself turn rock hard almost instinctively.'
    'The crowd followed behind her, calling out her name with questions, begging for her attention.'
    'I traced her strut and bit my lower lip staring at her tightly-armored behind.'
    if EventAdventureGuildShowUp().MarkusWasInPartyAlready:
        MARKUS 'Holy...'
        MARKUS 'I call that one.'
        MC @talk 'What?'
        MC @talk 'You don’t get to call that one!'
        MARKUS 'Yep! Just did.'
        MC @talk 'Nuh-uh.'
        MARKUS 'Uh-uh!'
        MC @talk 'Stop being such a child about it.'
        MC @talk 'She’s probably not even interested in either of us that way anyway.'
        MARKUS 'Well, if she is, I’m just saying, I’ve called that one.'
        MC @talk 'And I’m just saying, your call is rejected.'
        MARKUS 'If I get a chance to pull THAT into bed, no Demorai army could stop me.'
        MC @talk 'Yeah, because that’s gonna happen.'
    else:
        MARKUS "[player_name!t]? Okay, I'll let you 'appreciate the sight' in peace."
        MARKUS "I'll be in the Iron Unicorn."
        hide markus with easeoutleft
        show mc at blurin, cleft_f
        MC @talk "Yeah I..."
        MC @talk "*Sigh*"
    scene black with dissolve

    $ ShowTutorialPopup("guild_board")

    $ QstComplete(EventAdventureGuildShowUp)
    $ LocEnter()