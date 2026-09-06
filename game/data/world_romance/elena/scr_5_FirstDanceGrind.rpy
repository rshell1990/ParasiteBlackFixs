label rom_FirstDanceGrind:
    #Scene 23 - Regina room- Evening
    #Player selects to enter Regina's room
    $ LocNameSetTemp(_("Regina's Room"))
    'Come dusk I entered the room, Elena smiled as she rose up from the bed and stepped towards me.'
    scene bg_regina_room_night with dissolve
    $ CharSetClothes("elena", "ling")
    show elena at cright_f
    with dissolve
    show mc at left with easeinleft
    ELENA @lewd "I'm so glad you came..."
    'She said softly, my eyes wandering up and down her body and the lingerie she wore.'
    ELENA @lewd 'Umm, do you like it?'
    menu:
        'Turn around, I want to look at the back first':
            hide elena with dissolve
            show elena_back_ling at cright with dissolve
            $ Pause()
            'Elena did as she was asked, turning away as my eyes stared at her cute ass.'
            ELENA '...Satisfied?'
            MC @smile 'Very, you can turn back around now.'
            hide elena_back_ling with dissolve
            show elena at cright_f with dissolve
            'Elena turned back to face me, cheeks red as she did so.'
        'You look amazing.':
            ELENA @lewd 'Ah, thank you.'
            ELENA @talk 'I really like how it looks on me.'
            'For a moment, there was an awkward pause between us before Elena, blushing and eyes still avoiding mine, stepped forward.'
    ELENA @lewd 'Sit... Sit down on the bed for me.'
    MC @surprised 'Elena, are we-'
    ELENA @talk "You'll see, just trust me."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    scene elena_grind_ling_1 with dissolve
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
    scene elena_grind_ling_2 with dissolve
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
    scene elena_grind_ling_3 with dissolve
    $ Pause()
    #Cut to dance animation 3 (lingerie version)
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
    $ Pause()
    #Cut to black
    ELENA "Well... This just won't do, will it?"
    MC 'Elena? What are you-'
    MC '...!'
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop.ogg",1)
    #Cut to Elena grind animation
    scene elena_grind_ling_4 with dissolve:
        zoom 1.1
        yoffset -50
    $ Pause()
    ELENA 'How about {i}*Huff*{/i} this?'
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
    #Cut to MC climax art(s)
    $ ReduceInfectionFromSex("elena")
    $ PlaySexFx("audio/sex_sounds/adara_hj_finish.ogg")
    scene elena_grind_ling_finish_1 with dissolve
    scene elena_grind_ling_finish_2 with dissolve
    MC 'G-Grghh!'
    scene elena_grind_ling_finish_3 with dissolve
    scene elena_grind_ling_finish_4 with dissolve
    $ UnlockGalFlag("elena","grind","var_ling")
    $ UnlockGalSceneAndGrantXp("elena","grind")
    $ Pause()
    'After being totally drained by Elena, I began to feel myself sink into the comforts of the beds quilts.'
    ELENA "{i}*Huff*{/i} Yes... That's it."
    ELENA "Just like that..."
    ELENA "Oh my, I really did all that?"
    MC "{i}*Huff*{/i} Elena..."
    ELENA 'Mmmm, we should {i}definitely{/i} do this again sometime.'
    #Cut to black
    scene black with dissolve
    'After that, I slowly rose back to my feet as Elena beamed pridefully at her handywork.'
    $ AutoMus(True)
    scene bg_regina_room_night with dissolve
    show mc at left
    show elena at cright_f
    ELENA @talk 'Soooo...'
    ELENA @talk 'Was it worth it?'
    MC @talk 'Very much so.'
    ELENA @talk "I know you want more, but..."
    ELENA @talk 'I still need to wrap my head around all that, okay?'
    MC @talk "That's alright Elena... When you're ready, I'll be here."
    'Elena smiled at the comment, leaping forward to once again kiss me excitedly.'
    hide mc
    hide elena
    with dissolve
    show cg_mc_elena_kiss_lingerie at center
    with dissolve
    ELENA 'Mmh!'
    'Elena quickly pulled away.'
    ELENA @talk "Can... I maybe cuddle in the bed with you tonight instead of sleeping on the floor?"
    MC @talk 'Of course, Elena...'
    'Elena smiled, and the warmth and love radiating from her, so infectious, made me smile too.'
    $ CharChangeRel("elena", 1)
    $ CharSetClothes("elena", "normal")
    $ LocNameReset()
    $ TimeAdvTo(TIME_DAY_START)
    $ QstSetProgress(RomanceElena, 8)
    $ QstSetDelay(RomanceArlena, 2)
    $ LocEnter()