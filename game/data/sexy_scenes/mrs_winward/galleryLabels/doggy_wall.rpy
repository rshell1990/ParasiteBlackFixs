label gallery_winward_doggy_wall:
    $ tmpvar = {}

########
    if GalFlag("mrs_winward", "doggy_wall", ["dress", "cow"]):
        "Was she wearing her cow outfit?"
        menu:
            "Yes":
                $ tmpvar["cow"] = True
            "No":
                $ tmpvar["cow"] = False

    elif GalFlag("mrs_winward", "doggy_wall", "dress"):
        $ tmpvar["cow"] = False
    elif GalFlag("mrs_winward", "doggy_wall", "cow"):
        $ tmpvar["cow"] = True


########
    if GalFlag("mrs_winward", "doggy_wall", ["preg", "nopreg"]):
        "Was she pregnant at the time?"
        menu:
            "Yes":
                $ tmpvar["preg"] = True
            "No":
                $ tmpvar["preg"] = False

    elif GalFlag("mrs_winward", "doggy_wall", "preg"):
        $ tmpvar["preg"] = True
    elif GalFlag("mrs_winward", "doggy_wall", "nopreg"):
        $ tmpvar["preg"] = False


########
    if GalFlag("mrs_winward", "doggy_wall", ["vag", "anal"]):
        "Was the encounter vaginal or anal?"
        menu:
            "Vaginal":
                $ tmpvar["vag"] = True
            "Anal":
                $ tmpvar["vag"] = False

    elif GalFlag("mrs_winward", "doggy_wall", "vag"):
        $ tmpvar["vag"] = True
    elif GalFlag("mrs_winward", "doggy_wall", "anal"):
        $ tmpvar["vag"] = False

########
    if GalFlag("mrs_winward", "doggy_wall", ["cuck", "no_cuck"]):
        "Was Mr. Winward around?"
        menu:
            "Yes":
                $ tmpvar["cuck"] = True
            "No":
                $ tmpvar["cuck"] = False

    elif GalFlag("mrs_winward", "doggy_wall", "cuck"):
        $ tmpvar["cuck"] = True
    elif GalFlag("mrs_winward", "doggy_wall", "no_cuck"):
        $ tmpvar["cuck"] = False

########
    if tmpvar["cuck"] == True:
        if tmpvar["vag"] == True:
            jump gallery_winward_doggy_wall_cuck_vag
        else:
            jump gallery_winward_doggy_wall_cuck_anal
    else:
        if tmpvar["vag"] == True:
            jump gallery_winward_doggy_wall_nocuck_vag
        else:
            jump gallery_winward_doggy_wall_nocuck_anal

########################
label gallery_winward_doggy_wall_nocuck_vag:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg",1)
    if tmpvar["cow"] == True:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_cow_preg_slow_solo with dissolve
        else:
            scene mrs_winward_doggywall_cow_nopreg_slow_solo with dissolve

    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_nude_preg_slow_solo with dissolve
        else:
            scene mrs_winward_doggywall_nude_nopreg_slow_solo with dissolve
    $ Pause()

    "As her wetness brushed up against me along with her pubic hair, I knew what Mrs Winward needed, and I wasn't going to waste anytime giving it to her!"
    "Grabbing her hair and pulling, she gasped as she felt my cock plunge deeply into her tight, wet hole."
    MRS_WINWARD "H-HMhmmffhhh!!"
    "Slowly, I began to thrust my cock in and out of Mrs Winward's pussy."
    "Her ass rippled with every thrust as I squeezed my free hand on her round ass for better grip, feeling the fat slip between my fingers."
    MRS_WINWARD "D-Dear! Ahh!"
    MRS_WINWARD "You feel so - Mhmm! Big!"
    "Hot moans escaped Mrs Winward's lips as her legs began to tremble whilst my cock continued to plunge in and out of her tight clutching hole."
    "As her wet pussy grew more accustomed to my member, I began to move faster."
    "The sounds of sweet flesh colliding grew louder and more frequent as Mrs Winward's guttural moans filled the room."
    MRS_WINWARD "Ahh! Ahh! Mhmfghh! C-Careful! You're-"
    MRS_WINWARD "Oooooooooh!! {image=[ICON.HEART]}"

    if tmpvar["cow"] == True:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_cow_preg_fast_solo with dissolve
        else:
            scene mrs_winward_doggywall_cow_nopreg_fast_solo with dissolve

    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_nude_preg_fast_solo with dissolve
        else:
            scene mrs_winward_doggywall_nude_nopreg_fast_solo with dissolve
    $ Pause()

    "Her sweet groans of pleasure became more frequent as I took Mrs Winward from behind."
    "I wondered what Mr Winward would think if he ever saw his wife's lewd expressions as she felt my cock fill her up properly?"
    MC "Have you ever been fucked this deeply, Mrs Winward?"
    MRS_WINWARD "M-Mhhfhhhgh!"
    MRS_WINWARD "I-It's like you're - Hrghhh! Re-shaping all my insides!"
    MC "That doesn't answer the question!"
    MRS_WINWARD "A-Ahhh! N-No! I've never even SEEN anyone bigger than you!"
    "Satisfied with her answer, I slammed my cock to the hilt, determined to fuck her senseless so she'd know for sure {i}who{/i} her body belonged to from now on..."
    MRS_WINWARD "M-MHHHHHHHHHFFFHH!"
    MRS_WINWARD "P-Please! {i}*Huff*{/i} Mhfghhh!"
    MRS_WINWARD "F-Fill me up!"
    MRS_WINWARD "I don't know how much more I can - Mhhhfhh! Take!"
    "I continued to have my way with her for a little while longer, enjoying the feeling of her pussy squeezing my member with desperation to bring me to climax."
    "Eventually, she got her wish."
    "As my balls began to tighten and rise, my cock, still plunging mercilessly in and out of her now trembling body, began to feel increasingly ready for release."
    MRS_WINWARD "{i}*Huff*{/i} F-Finish dear! {i}*Huff*{/i} I beg you! P-Please!!"
    "Giving her what she wanted, I dug my hand deep into the soft flesh of her large, round ass and slammed deeply into her."
    "Grunting loudly, I flooded Mrs Winward's womb with my hot, thick seed."

    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")

    if tmpvar["cow"] == True:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_cow_preg_finish_solo with flash
        else:
            scene mrs_winward_doggywall_cow_nopreg_finish_solo with flash
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_nude_preg_finish_solo with flash
        else:
            scene mrs_winward_doggywall_nude_nopreg_finish_solo with flash
    $ Pause()

    MC "H-HRGHHHHH!!"
    "Mrs Winward gasped as she felt the rush of warm fluid pouring into her."
    "Her eyes rolled back as she trembled and nearly collapsed back into my arms."
    "I held her up as I continued to pump my load into her body."
    "Only a soft whimpered escaped her lips as I held her body upright in my arms."
    MRS_WINWARD "M-Mhmmm..."
    MRS_WINWARD "Oh gods...That was..."
    MRS_WINWARD "...{i}Oh my...{/i}"
    return

label gallery_winward_doggy_wall_nocuck_anal:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg",1)

    if tmpvar["cow"] == True:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_cow_preg_slow_solo with dissolve
        else:
            scene mrs_winward_doggywall_cow_nopreg_slow_solo with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_nude_preg_slow_solo with dissolve
        else:
            scene mrs_winward_doggywall_nude_nopreg_slow_solo with dissolve
    $ Pause()

    "Moving my cock slightly higher, I lightly prodded against her forbidden back door."
    MRS_WINWARD "{i}*Gasp!*{/i}"
    MRS_WINWARD "If... If you're going to try and put it {i}there,{/i} p-please."
    MRS_WINWARD "Start slowly?"
    "Grabbing a fist full of her hair, she let out another short gasp as she felt the head of my cock sink into her tight, clutching asshole."
    MRS_WINWARD "A-AHHHH!!"
    "Slowly, I began to thrust my cock in and out of Mrs Winward's ass."
    "Her ass rippled with every thrust as I squeezed my free hand on her round ass for better grip, feeling the fat slip between my fingers."
    MRS_WINWARD "M-MMFGHHH!"
    MRS_WINWARD "C-Careful! My - A-Ass! - Mhmm! You're so - Big!"
    MRS_WINWARD "I-It's burning from how much you're - ahhh! Stretching!"
    "Hot moans escaped Mrs Winward's lips as her legs began to tremble whilst my cock continued to plunge in and out of her forbidden back door."
    "As her now loosened asshole stretched and slowly grew more accustomed to my member, I began to move faster."
    "The sounds of sweet flesh colliding grew louder and more frequent as Mrs Winward's guttural moans filled the room."
    MRS_WINWARD "Ahh! Ahh! Mhmfghh! C-Careful! You're-"
    MRS_WINWARD "Oooooooooh!! {image=[ICON.HEART]}"
    "Her sweet groans of pleasure became more frequent as I took Mrs Winward from behind."
    "I wondered what Mr Winward would think if he ever saw his wife with my cock stretching out her ass?"
    MC "Does Mr Winward get to fuck this hole?"
    MRS_WINWARD "M-Mhhfhhhgh!"
    MRS_WINWARD "M-My assshhh! - Hrghhh! You're - Ahh! Re-shaping all my insides!"
    MC "That doesn't answer the question!"
    MRS_WINWARD "A-Ahhh! N-No! He doesn't get to put it my ass!!"
    "Satisfied with her answer, I slammed my cock to the hilt, determined to claim this hole just for myself..."
    MRS_WINWARD "M-MHHHHHHHHHFFFHH!"
    MRS_WINWARD "P-Please! {i}*Huff*{/i} Mhfghhh!"
    MRS_WINWARD "C-Cum already!"
    MRS_WINWARD "I don't know how much more my poor ass can - Ahh! Take!"
    "I continued to have my way with her for a little while longer, enjoying the feeling of her pussy squeezing my member with desperation to bring me to climax."
    "Eventually, she got her wish."
    "As my balls began to tighten and rise, my cock, still plunging mercilessly in and out of her now trembling body, began to feel increasingly ready for release."
    MRS_WINWARD "{i}*Huff*{/i} F-Finish dear! {i}*Huff*{/i} I beg you! P-Please!!"
    "Giving her what she wanted, I dug my hand deep into the soft flesh of her large, round ass and slammed deeply into her."
    "Grunting loudly, I flooded Mrs Winward's ass with my hot, thick seed."
    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")

    if tmpvar["cow"] == True:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_cow_preg_finish_solo with flash
        else:
            scene mrs_winward_doggywall_cow_nopreg_finish_solo with flash

    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_nude_preg_finish_solo with flash
        else:
            scene mrs_winward_doggywall_nude_nopreg_finish_solo with flash
    $ Pause()

    MC "H-HRGHHHHH!!"
    "Mrs Winward gasped as she felt the rush of warm fluid pouring into her."
    "Her eyes rolled back as she trembled and nearly collapsed back into my arms."
    "I held her up as I continued to pump my load into her now limp body."
    "Only a soft whimpered escaped her lips as I held her body upright in my arms."
    MRS_WINWARD "M-Mhmmm..."
    MRS_WINWARD "Oh gods...That was..."
    MRS_WINWARD "...{i}Oh my...{/i}"
    return

label gallery_winward_doggy_wall_cuck_vag:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg",1)
    if tmpvar["cow"] == True:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_cow_preg_slow_watched with dissolve
        else:
            scene mrs_winward_doggywall_cow_nopreg_slow_watched with dissolve

    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_nude_preg_slow_watched with dissolve
        else:
            scene mrs_winward_doggywall_nude_nopreg_slow_watched with dissolve
    $ Pause()

    "As her wetness brushed up against me along with her pubic hair, I knew what Mrs Winward needed, and I wasn't going to waste any time giving it to her!"
    "Grabbing her hair and pulling, she gasped as she felt my cock plunge deeply into her tight, wet hole."
    MRS_WINWARD "H-HMhmmffhhh!!"
    "Slowly, I began to thrust my cock in and out of Mrs Winward's pussy."
    "Her ass rippled with every thrust as I squeezed both hands on her round ass for better grip, feeling the fat slip between my fingers."
    MRS_WINWARD "D-Dear! Ahh!"
    MRS_WINWARD "You feel so - Mhmm! Big!"
    "Mr Winward watched in pure shock as his wife's womanhood spread and clung around my cock, ramming in and out of her."
    "Hot moans escaped Mrs Winward's lips as her legs began to tremble whilst my cock continued to plunge in and out of her tight clutching hole."
    "As her wet pussy grew more accustomed to my member, I began to move faster."
    "The sounds of sweet flesh colliding grew louder and more frequent as Mrs Winward's guttural moans filled the room."
    MRS_WINWARD "Ahh! Ahh! Mhmfghh! C-Careful! You're-"
    MRS_WINWARD "Oooooooooh!! {image=[ICON.HEART]}"

    if tmpvar["cow"] == True:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_cow_preg_fast_watched with dissolve
        else:
            scene mrs_winward_doggywall_cow_nopreg_fast_watched with dissolve

    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_nude_preg_fast_watched with dissolve
        else:
            scene mrs_winward_doggywall_nude_nopreg_fast_watched with dissolve
    $ Pause()
    
    MR_WINWARD "Ahh! Yes! That's it! Give it to her, lad!"
    MR_WINWARD "Give it to her good!"
    "Her sweet groans of pleasure became more frequent as I took Mrs Winward from behind."
    MC "Have you ever been fucked this deeply, Mrs Winward?"
    MRS_WINWARD "M-Mhhfhhhgh!"
    MRS_WINWARD "I-It's like you're - Hrghhh! Re-shaping all my insides!"
    MC "That doesn't answer the question!"
    MRS_WINWARD "A-Ahhh! N-No! I've never even SEEN anyone bigger than you!"
    "Satisfied with her answer, I slammed my cock to the hilt, determined to fuck her senseless so she'd know for sure {i}who{/i} her body belonged to from now on..."
    MRS_WINWARD "M-MHHHHHHHHHFFFHH!"
    MRS_WINWARD "P-Please! {i}*Huff*{/i} Mhfghhh!"
    MRS_WINWARD "F-Fill me up!"
    MRS_WINWARD "I don't know how much more I can - Mhhhfhh! Take!"
    "I continued to have my way with her for a little while longer, enjoying the feeling of her pussy squeezing my member with desperation to bring me to climax."
    "Eventually, she got her wish."
    "As my balls began to tighten and rise, my cock, still plunging mercilessly in and out of her now trembling body, began to feel increasingly ready for release."
    MRS_WINWARD "{i}*Huff*{/i} F-Finish dear! {i}*Huff*{/i} I beg you! P-Please!!"
    "Giving her what she wanted, I dug my hands deep into the soft flesh of her large, round ass and slammed deeply into her."
    "Grunting loudly, I flooded Mrs Winward's womb with my hot, thick seed."

    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")

    if tmpvar["cow"] == True:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_cow_preg_finish_watched with flash
        else:
            scene mrs_winward_doggywall_cow_nopreg_finish_watched with flash

    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_nude_preg_finish_watched with flash
        else:
            scene mrs_winward_doggywall_nude_nopreg_finish_watched with flash
    $ Pause()

    MC "H-HRGHHHHH!!"
    "Mrs Winward gasped as she felt the rush of warm fluid pouring into her."
    "Her eyes rolled back as she trembled and nearly collapsed back into my arms."
    "I held her up as I continued to pump my load into her body."
    "Only a soft whimper escaped her lips as I held her body upright in my arms."
    MRS_WINWARD "M-Mhmmm..."
    MRS_WINWARD "Oh gods...That was..."
    MRS_WINWARD "...{i}Oh my...{/i}"
    return

label gallery_winward_doggy_wall_cuck_anal:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg",1)
    if tmpvar["cow"] == True:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_cow_preg_slow_watched with dissolve
        else:
            scene mrs_winward_doggywall_cow_nopreg_slow_watched with dissolve

    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_nude_preg_slow_watched with dissolve
        else:
            scene mrs_winward_doggywall_nude_nopreg_slow_watched with dissolve
    $ Pause()

    "Moving my cock slightly higher, I lightly prodded against her forbidden back door."
    MRS_WINWARD "{i}*Gasp!*{/i}"
    MRS_WINWARD "If... If you're going to try put it {i}there,{/i} p-please."
    MRS_WINWARD "Start slowly?"
    "Grabbing a fist full of her hair, she let out another short gasp as she felt the head of my cock sink into her tight, clutching asshole."
    MRS_WINWARD "A-AHHHH!!"
    "Slowly, I began to thrust my cock in and out of Mrs Winward's ass."
    "Her ass rippled with every thrust as I squeezed both hands on her round ass for better grip, feeling the fat slip between my fingers."
    MRS_WINWARD "M-MMFGHHH!"
    MRS_WINWARD "C-Careful! My - A-Ass! - Mhmm! You're so - Big!"
    MRS_WINWARD "I-It's burning from how much you're - ahhh! Stretching!"
    "Hot moans escaped Mrs Winward's lips as her legs began to tremble whilst my cock continued to plunge in and out of her forbidden back door."
    MR_WINWARD "D-Dear!"
    "Mr Winward watched in pure shock as his wife's asshole spread and clung around my cock ramming in and out of her."
    MR_WINWARD "He's... He's in your-"
    MRS_WINWARD "H-Hrghh! Watch carefully you pathetic excuse for a husband!"
    MRS_WINWARD "T-This hole - Ahhh! Belongs to him now! Are we clear?"
    "Mr Winward whimpered in acknowledgement as he stroked his cock furiously watching us."
    "As her now loosened asshole stretched and slowly grew more accustomed to my member, I began to move faster."
    "The sounds of sweet flesh colliding grew louder and more frequent as Mrs Winward's guttural moans filled the room."
    MRS_WINWARD "Ahh! Ahh! Mhmfghh! C-Careful! You're-"
    MRS_WINWARD "Oooooooooh!! {image=[ICON.HEART]}"
    "Her sweet groans of pleasure became more frequent as I took Mrs Winward from behind."
    MC "Ah! What do you think Mr Winward?"
    MC "Do you like seeing your wife's asshole stretched out around my cock like this?"
    "Mr Winward didn't answer, he was too busy staring intently at us as he stroked his cock desperately."
    MRS_WINWARD "M-Mhhfhhhgh!"
    MRS_WINWARD "M-My assshhh! - Hrghhh! You're - Ahh! Re-shaping all my insides!"
    MRS_WINWARD "A-Ahhh! H-He feels so good dear! He feels so good in my ass!!"
    "I slammed my cock to the hilt, determined to leave her exhausted and breathless when I was done."
    MRS_WINWARD "M-MHHHHHHHHHFFFHH!"
    MRS_WINWARD "P-Please! {i}*Huff*{/i} Mhfghhh!"
    MRS_WINWARD "C-Cum already!"
    MRS_WINWARD "I don't know how much more my poor ass can - Ahh! Take!"
    "I continued to have my way with her for a little while longer, enjoying the feeling of her ass squeezing my member with desperation to bring me to climax."
    "Eventually, she got her wish."
    "As my balls began to tighten and rise, my cock, still plunging mercilessly in and out of her now trembling body, began to feel increasingly ready for release."
    MRS_WINWARD "{i}*Huff*{/i} F-Finish dear! {i}*Huff*{/i} I beg you! P-Please!!"
    "Giving her what she wanted, I dug my hands deep into the soft flesh of her large, round ass and slammed deeply into her."
    "Grunting loudly, I flooded Mrs Winward's ass with my hot, thick seed."

    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")

    if tmpvar["cow"] == True:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_cow_preg_finish_watched with flash
        else:
            scene mrs_winward_doggywall_cow_nopreg_finish_watched with flash
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_doggywall_nude_preg_finish_watched with flash
        else:
            scene mrs_winward_doggywall_nude_nopreg_finish_watched with flash
    $ Pause()

    MC "H-HRGHHHHH!!"
    "Mrs Winward gasped as she felt the rush of warm fluid pouring into her."
    "Her eyes rolled back as she trembled and nearly collapsed back into my arms."
    "I held her up as I continued to pump my load into her now limp body."
    "Only a soft whimper escaped her lips as I held her body upright in my arms."
    MRS_WINWARD "M-Mhmmm..."
    MRS_WINWARD "Oh gods...That was..."
    MRS_WINWARD "...{i}Oh my...{/i}"
    "Pitifully, Mr Winward also finished behind us, emitting a low grunt as a couple of drops from his inferior side trickled onto the floor.."
    MR_WINWARD "Ahhh! That was incredible!"
    MR_WINWARD "I sure am glad I never took that hole for myself now and gave it to you! It makes it all feel extra special!"
    "The two of us ignored the old man, Mrs Winward was far too dazed out from the fuck to care about any silly words tumbling out of the cuckolds mouth."
    "Slowly, As I unsheathed my cock from Mrs Winward's now loosened asshole, she shuddered as my seed spilled out of her onto the floor." 
    "Letting go of her hair, her legs shook and buckled as she slid down onto the floor in a puddle of our cum."

    return
