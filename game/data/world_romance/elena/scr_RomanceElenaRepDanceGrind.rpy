label rom_ElenaRepDanceGrind:
    #reject version
    #ELENA @talk 'Ahh, perhaps some other time?'
    #ELENA @talk "I don't quite feel up to that tonight."
    #MC @talk 'Of course, some other time then.'
    #Accept version
    ELENA @talk 'Hmm... Is that so?'
    ELENA @talk "Well, that does sound rather fun, doesn't it?"
    ELENA @talk 'But what do you think?'
    ELENA @talk 'Should I come dressed like before... {i}Or maybe not dressed at all?{/i}'
    menu:
        'Wear the lingerie.':
            ELENA @talk 'Mmm, very well.'
            $ RomanceElena().wearLingeriePlease = True
        "Don't wear anything.":
            ELENA @talk "Oh! Well, if that's what you want..."
            $ RomanceElena().wearLingeriePlease = False
            #fade to black then MC joining Elena in the room
    scene black with dissolve
    'A short while later...'
    scene bg_regina_room_night with dissolve
    if RomanceElena().wearLingeriePlease == True:
        $ CharSetClothes("elena", "ling")
    else:
        $ CharSetClothes("elena", "naked")

    show elena at center_f
    with dissolve
    show mc at left with easeinleft
    'As I entered the room, Elena smiled as she rose up from the bed and stepped towards me.'
    ELENA @lewd "Ahh, there you are."
    'She said softly, my eyes wandering up and down her luschious body.'
    ELENA @talk 'So... How should we start?'
    menu:
        'Turn around, I want to look at the back first':
            hide elena with dissolve
            if CharGetClothes("elena") == 'ling':
                show elena_back_ling at center with dissolve
            else:
                show elena_back_naked at center with dissolve
            $ Pause()
            'Elena did as she was asked, turning away as my eyes stared at her cute ass.'
            ELENA '...You like my ass that much huh?'
            MC @smile 'Very, you can turn back around now.'
            hide elena_back_ling
            hide elena_back_naked
            with dissolve
            show elena at center_f with dissolve
            'Elena turned back to face me, cheeks red as she did so.'
        'You look amazing.':
            ELENA @lewd 'Ah, thank you.'
            'For a moment, there was an awkward pause between us before Elena, blushing and eyes still avoiding mine, stepped forward.'
    ELENA @talk 'Sit... Sit down on the bed for me.'
    ELENA @talk "{i}I want to drive you wild again like last time...{/i}"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    if CharGetClothes("elena") == 'ling':
        scene elena_grind_ling_1 with dissolve
        $ Pause()
    else:
        scene elena_grind_naked_1 with dissolve
        $ Pause()
    #Fade to black, cut to dance animation 1 (Lingerie version)
    'Sat down on the bed, I watched as Elena began to slowly dance for me.'
    'Her eyes hungrily looked towards me as she swayed her hips back and forth hypnotically.'
    ELENA '{i}Watch me...{/i}'
    'She said softly, her hot breath against the cool air.'
    "With my cock hardening as I watched her, I reached down and began to stroke myself watching to her, eyes wandering down her body."
    "Her nipples hardened as thin trails of sweat began to drip down off her, glistening in the light."
    "Elena's eyes stared at the hard member in front of her as she continued her hypnotic dance, biting at her lower lip in excitement."
    ELENA "{i}That's it... Keep watching me.{/i}"
    ELENA "Don't look away."
    "Elena let out a hot, nervous moan as she slowly began to turn away from me."
    if CharGetClothes("elena") == 'ling':
        scene elena_grind_ling_2 with dissolve
        $ Pause()
    else:
        scene elena_grind_naked_2 with dissolve
        $ Pause()
    #Cut to dance animation 2 (Lingerie version)
    'Elena turned around, still continuing to sway her hips as my eyes stared at her ass.'
    'Looking over her shoulder to continue watching me, she smiled coyly.'
    ELENA '{i}I like seeing how hard I make you...{/i}'
    'She purred sultrily, gently continuing to sway her hips back and forth.'
    ELENA 'I want you to {i}always{/i} be like that when you see me from now on.'
    ELENA "I want to be able to just brush up against you and you're harder than a rock."
    ELENA '{i}I want just my scent alone to drive you wild...{/i}'
    ELENA '{i}I want to be like this, teasing you even in your dreams~{/i}'
    MC 'Ahh...!'
    MC 'Elena!'
    #Cut to dance animation 3 (lingerie version)
    if CharGetClothes("elena") == 'ling':
        scene elena_grind_ling_3 with dissolve
        $ Pause()
    else:
        scene elena_grind_naked_3 with dissolve
        $ Pause()
    'Elena, encouraged as she watched me stroke myself faster to her, slowly bent forward teasingly for me.'
    'As I furiously stroked at my cock in excitement, eyes transfixed on what was in front of me, Elena continued to tease.'
    ELENA "{i}Y-Yes... K-Keep doing that.{/i}"
    "I felt the rush of adrenaline coursing through me as I stared at Elena's ass, feeling the overwhelming, swelling urge inside of me to leap onto her."
    "My hot blood burned and coursed through me as the darkness inside me longed to pin her down and force my cock deep into her..."
    "And Elena knew, she knew I wanted that and it only excited her more."
    ELENA "{i}Faster! Faster for me!{/i}"
    'Letting out a trembling hot breath, Elena realized I would not last much longer watching her like this.'
    ELENA "Poor thing... How irresponsible of me."
    ELENA 'Getting you so excited like this.'
    scene black with dissolve
    #Cut to black
    ELENA "Well... This just won't do, will it?"
    ELENA "{i}*Giggles*{/i} Time for your favourite part!"
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop.ogg",1)
    if CharGetClothes("elena") == 'ling':
        scene elena_grind_ling_4 with dissolve
        $ Pause()
    else:
        scene elena_grind_naked_4 with dissolve
        $ Pause()
    #Cut to Elena grind animation
    ELENA 'How is {i}*Huff*{/i} this?'
    MC 'G-Grghh! Elena!'
    ELENA 'Shhh, just - {i}*Huff*{/i} enjoy it!'
    ELENA 'Mhmmff!'
    ELENA 'Gods, you feel so good to rub against like this...!'
    "Elena's hot wet cunt continued to slide along my cock, coating it in her juices as she grinded against me."
    "The warm sensation of her felt incredible,  and I soon found myself desperate to reach out and grab her, forcing myself deeply into her tight body."
    ELENA "Y-You need to - {i}*Huff*{/i}"
    ELENA 'Masturbate thinking about this after {i}*Huff*{/i} o-okay?'
    ELENA 'Mmhmfghh...! So good!'
    MC 'E-Elena!'
    MC "I can't - Grghh! Hold back much longer!"
    ELENA 'D-Do it!'
    ELENA 'Just let it go and cum for me!'
    ELENA '{i}I want you to cum for me!{/i}'
    "Unable to hold back any longer, I grunted as I released the first coat of my seed."
    $ ReduceInfectionFromSex("elena")
    $ PlaySexFx("audio/sex_sounds/adara_hj_finish.ogg")
    if CharGetClothes("elena") == 'ling':
        scene elena_grind_ling_finish_1 with dissolve
        scene elena_grind_ling_finish_2 with dissolve
    else:
        scene elena_grind_naked_finish_1 with dissolve
        scene elena_grind_naked_finish_2 with dissolve
    $ Pause()
    MC 'G-Grghh!'
    if CharGetClothes("elena") == 'ling':
        scene elena_grind_ling_finish_3 with dissolve
        scene elena_grind_ling_finish_4 with dissolve
        $ UnlockGalFlag("elena","grind","var_ling")
    else:
        scene elena_grind_naked_finish_3 with dissolve
        scene elena_grind_naked_finish_4 with dissolve
        $ UnlockGalFlag("elena","grind","var_naked")
    $ UnlockGalSceneAndGrantXp("elena","grind")
    $ Pause()
    'After being totally drained by Elena, I began to feel myself sink into the comforts of the beds quilts.'
    ELENA "{i}*Huff*{/i} Yes... That's it."
    ELENA "Just like that..."
    ELENA "Oh my, I really did all that?"
    MC "{i}*Huff*{/i} Elena..."
    ELENA 'Mmmm, I really like it when we do that...'
    #Cut to black
    scene black with dissolve
    'After that, I slowly rose back to my feet as Elena beamed pridefully at her handywork.'
    $ AutoMus(True)
    scene bg_regina_room_night with dissolve
    show mc at cleft
    show elena at cright_f
    ELENA @talk 'Soooo...'
    ELENA @talk 'Was that as good as the first time?'
    MC @talk "Come closer, I'll whisper my answer to you..."
    'Elena smiled at the comment, leaping forward to once again kiss me excitedly.'
    hide mc
    hide elena
    with dissolve
    if CharGetClothes("elena") == 'ling':
        show cg_mc_elena_kiss_lingerie at center with dissolve
    else:
        show cg_mc_elena_kiss_naked at center with dissolve
    ELENA 'Mmh!'
    'Elena quickly pulled away.'
    ELENA @talk "Can... I maybe cuddle in the bed with you tonight again?"
    MC @talk 'Of course, Elena...'
    'Elena smiled, and the warmth and love radiating from her, so infectious, made me smile too.'
    $ CharChangeRel("elena", 1)
    $ CharSetClothes("elena", "normal")
    $ LocEnter()