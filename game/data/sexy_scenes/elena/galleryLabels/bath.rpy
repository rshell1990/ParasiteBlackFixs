label gallery_elena_bath:
    scene black with dissolve
    if GalFlag("elena","bath",["var_firstTime","var_rep"]):
        "We had a bath together more than once."
        "Which was it?"
        menu:
            "The first time.":
                jump gallery_elena_bath_first
            "That one time after the first one.":
                jump gallery_elena_bath_rep
    elif GalFlag("elena","bath","var_firstTime"):
        jump gallery_elena_bath_first
    elif GalFlag("elena","bath","var_rep"):
        jump gallery_elena_bath_rep

label gallery_elena_bath_first:
    "As I headed towards [regina_ref!t]'s room, I opened the door and stepped inside."
    scene elena_bath_solo with dissolve
    $ Pause()
    $ PlayMusic("audio/music/33_Elena.ogg")
    ELENA 'Ahh! [player_name!t]! There you are!'
    "My eyes scanned over her naked body that glistened from the small streams of water that rolled off of her."
    'My cock throbbed with excitement as I stared at her breasts, half submerged in the warm water as her sultry eyes looked hungrily towards me.'
    ELENA "{i}...Do you just intend to stand there and stare at me all Evening?{/i}"
    MC "Watching you all night doesn't sound so bad to me..."
    ELENA "Perhaps you are content just to stand there and watch me, but I need more."
    ELENA "Take your clothes off and get in here."
    MC 'I see your talk with Helena went well!'
    ELENA "If you aren't willing to brave the venture, nothing is gained."
    ELENA "Now don't keep me waiting!"
    scene black with dissolve
    'Stripping down from my clothes, I stepped into the tub with Elena.'
    scene elena_bath_pov with dissolve
    $ Pause()
    'Her wet body slid between my legs as her back rested on my chest.'
    "I can feel my cock harden and throb as it presses between the crack of her butt, I can tell Elena can feel it to, but it doesn't seem to bother her."
    "In fact, it only seems to excite her as she rubs against it lightly, all while looking over her shoulder back towards me."
    ELENA 'H-Hey... Can we talk?'
    MC 'I presumed there would be {i}some{/i} conversation with us both naked in the bath.'
    MC '{i}Unless you had other things on your mind already?{/i}'
    ELENA 'I... want to ask you something.'
    MC 'Ask whatever you wish.'
    ELENA '{i}What am I to you?{/i}'
    ELENA "I mean, it's clear there is {i}something{/i} more between us now than just companionship, right?"
    ELENA 'Why else would you join me like this?'
    ELENA 'So... {i}What are we doing here?{/i}'
    MC 'What do {i}you{/i} want Elena?'
    ELENA 'I-'
    ELENA '{i}...I want you.{/i}'
    MC 'What?'
    ELENA 'I want you!'
    ELENA "I don't know how or, even what kind of relationship we shall have but..."
    ELENA "I want you... I said it."
    ELENA "I'm so tired of never putting myself first, always holding back my desires to serve the whims of others."
    ELENA "But I will say it again so I'm heard loud and clear."
    ELENA "I... {i}want you.{/i}"
    MC '...'
    ELENA 'What do you say to that?'
    if GalFlag("elena","bath","var_line1"):
        MC 'Let us see where things go... But no commitments.'
        ELENA "So... What does that make us?"
        MC "Friends... For now."
        ELENA 'Oh, well...'
        ELENA 'But we can still... {i}test the water?{/i}'
        MC 'Elena... Come closer.' #Cut to animation 3 (kiss)
        scene elena_bath_kiss with dissolve
        $ Pause()
    elif GalFlag("elena","bath","var_line2"):
        MC 'Yes... I want you too Elena.'
        ELENA 'You have no idea how happy that makes me to hear.'
        ELENA "Gods, I've never met anyone like you..."
        ELENA 'You make me feel... {i}so good.{/i}'
        ELENA 'And bubbly, and light like my head is on a cloud.'
        MC 'Elena... Come closer.' #Cut to animation 3 (kiss)
        scene elena_bath_kiss with dissolve
        $ Pause()
    elif GalFlag("elena","bath","var_line3"):
        MC 'Why do we need to decide what we are?'
        MC 'Let us just enjoy ourselves and play it by ear.'
        ELENA "What do you mean by that?"
        MC "I mean, let us see where things go... There's no need to rush, is there?"
        ELENA 'N-No... Of course not.'
        ELENA 'But um, can we still {i}do{/i} things?'
        MC 'Things?'
        ELENA 'You know... Like...'
        'Her hand beneath the water gently brushed up against me.'
        ELENA '{i}Things.{/i}'
        MC 'Elena... Come closer.' #Cut to animation 3 (kiss)
        scene elena_bath_kiss with dissolve
        $ Pause()
    elif GalFlag("elena","bath","var_line4"):
        MC 'I want more than just your friendship Elena... {i}I want all of you.{/i}'
        ELENA 'I... I have no experience with anything like this.'
        ELENA "I don't know what to do, or..."
        ELENA 'You make me feel... {i}so good.{/i}'
        MC 'Elena... Come closer.' #Cut to animation 3 (kiss)
        scene elena_bath_kiss with dissolve
        $ Pause()
        "Tilting Elena's head towards me, I gently pressed my lips against her as my hand moved to cup and lightly fondle one of her breasts."
        "Elena moaned softly in appreciation as I slipped my tongue into her mouth and pressed it against hers."
        ELENA 'Mmmm...'
        ELENA '(My heart is racing so fast.)'
        ELENA '(How... {i}embarrassing{/i}.)'
        ELENA '(But this feels so right...)'
    scene elena_bath_pov with dissolve
    $ Pause()
    ELENA 'Ahh~ That was... So nice.'
    MC 'We should probably get out of here soon.'
    ELENA 'Ahh... Can we not stay just a little longer?'
    MC 'Very well... A little longer.'
    return

label gallery_elena_bath_rep:
    ELENA @talk 'Come then, I will pour the water...'
    $ PlayMusic("audio/music/33_Elena.ogg")
    scene elena_bath_solo with dissolve
    $ Pause()
    ELENA "Ahh, there you are..."
    ELENA "Come... The water's warm."
    "My eyes scanned over her naked body once again, glistening from the small streams of water that rolled off of her body."
    'My cock throbbed with excitement as I stared at her breasts, half submerged in the warm water as her sultry eyes looked hungrily towards me.'
    ELENA "Do you really enjoy just watching me that much sometimes?"
    MC "You're quite beautiful Elena."
    ELENA "Ahh... Stop saying such sweet things."
    ELENA "Take your clothes off already and get in here!"
    scene elena_bath_pov with dissolve
    $ Pause()
    'Stripping down from my clothes, I stepped into the tub with Elena.'
    'Her wet body slid between my legs as her back rested on my chest.'
    "I can feel my cock harden and throb as it presses between the crack of her butt, I can tell Elena can feel it to, but it doesn't seem to bother her."
    "In fact, it only seems to excite her as she rubs against it lightly, all while looking over her shoulder back towards me."
    ELENA 'Ahh... Is the water warm enough for you?'
    MC "The water's fine."
    ELENA "You know, with you, like this."
    ELENA "It's strange but, I can just feel all the dark memories and the worries slip away."
    ELENA "I hope you feel the same with me."
    MC 'I wish it was like that for me sometimes.'
    ELENA 'Please... Let me shoulder some of your worries.'
    ELENA "I'm strong enough to take it."
    MC 'Elena... Come closer.'
    scene elena_bath_kiss with dissolve
    $ Pause()
    "Tilting Elena's head towards me, I gently pressed my lips against her as my hand moved to cup and lightly fondle one of her breasts."
    "Elena moaned softly in appreciation as I slipped my tongue into her mouth and pressed it against hers."
    ELENA 'Mmmm...'
    ELENA '(I love it when he does this.)'
    ELENA '(How... {i}embarrassing{/i}.)'
    ELENA '(But this feels so right...)'
    scene elena_bath_pov with dissolve
    $ Pause()
    ELENA 'Ahh~ That was... So nice.'
    MC 'We should probably get out of here soon.'
    ELENA 'Ahh... Can we not stay just a little longer?'
    scene black with dissolve
    'I smiled at the comment, gently running my hand through her hair.'
    MC 'Very well... A little longer.'
    return