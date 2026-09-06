label rom_Dros_store_sex_cooldown:
    #If player tries to fuck them again straight away 
    DROS @talk "{i}Again?{/i}"
    DROS @talk 'I do need to actually run this place you know.'
    DROS @lewd 'Besides... I think my butt needs a little time to recover.'
    return

label rom_Dros_closeTheStore:
    $ RomanceDros().fuckedToday = True
    if CharGetVar("dros", "Transformed") == True:
        jump dros_store_sex_postTf
    else:
        jump dros_store_sex_preTf

label dros_store_sex_postTf:
    'Draya blushed at the comment.'
    DROS @shock 'Y-You... W-What?'
    MC @smile 'Close. The. Store.'
    'Draya stuttered as they leaned in to whisper, looking around the empty store for anyone who might be listening.'
    DROS @lewd 'N-Now?'
    DROS @shock "Can't it wait? People might-"
    MC @talk "No... It can't wait."
    'Draya bit down on her lower lip as she sheepishly headed towards the door to lock it, drawing what blinds she could.'
    DROS @lewd 'O-Okay... We just need to be quick.'
    DROS @lewd 'S-Should I... Get dressed?'
    menu:
        'Make it slutty.':
            $ CharSetClothes("dros", "dress")
            show dros at nod
            DROS @lewd 'A-Ah... Okay.'
        'Just take off your clothes.':
            $ CharSetClothes("dros", "naked")
            show dros at nod
            DROS @lewd "If that's what you want."
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    'Draya bent over the counter and waited with bated breath as I stripped down and lined up behind her.'
    'Draya breathed heavily as she looked over her shoulder at the massive cock which prodded and pressed against her tight rosebud.'
    DROS 'J-Just hurry up and-'
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg",1)
    if CharGetClothes("dros") == "dress":
        scene draya_anal_dress
    if CharGetClothes("dros") == "naked":
        scene draya_anal_naked
    with dissolve
    $ Pause()
    'As my cock pushed into her tight ass, Draya gasped and moaned as I began to fuck her from behind.'
    'The soft flesh of her bubbly ass bounced against my cock as she moaned with each thrust, her tight asshole squeezing down desperately on me.'
    DROS 'Ah! Ah! Gods! F-Fuck!' 
    MC "Bet your glad you - {i}*Huff*{/i} closed up now, huh?"
    DROS "S-Shuddup! I'm gonna open again after you-"
    DROS 'Oooooh! Gods, I love your fucking huge cock!'
    DROS 'This feels so good!'
    "I slapped Draya's ass playfully, leaving a pink hand print mark behind which she grunted to as I continued to defile her backdoor."
    if CharGetClothes("dros") == "dress":
        scene draya_anal_dress_alt
    if CharGetClothes("dros") == "naked":
        scene draya_anal_naked_alt
    with dissolve
    $ Pause()
    MC 'Who owns this tight ass slut?'
    DROS "AHH! You do [dros_player_ref!t]! You own this slut's fat ass!"
    'As I continued to slam against her soft, bubbly butt, Draya grunted and moaned lewdly as I felt my balls tighten and rise.'
    DROS 'Mmmfghh! C-Cum [dros_player_ref!t]! Fucking give it to me!'
    'Unable to hold back any longer, I gripped the soft flesh of her ass and grunted animalistically,'
    MC "H-Hrghh! I'm gonna fill your ass up!" 
    "Flooding Draya's tight ass, her eyes rolled back as I pumped her ass full of warm, thick seed."
    if CharGetClothes("dros") == "dress":
        scene draya_anal_dress_finish
        $ UnlockGalFlag("dros","store_anal","var_posttf_dress")
    if CharGetClothes("dros") == "naked":
        $ UnlockGalFlag("dros","store_anal","var_posttf_naked")
        scene draya_anal_naked_finish
    with flash
    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    $ ReduceInfectionFromSex("dros")
    $ UnlockGalSceneAndGrantXp("dros","store_anal")
    $ Pause()
    DROS "Urghhhh...!"
    "As Draya's ass swallowed my load, I held her there for a few moments as we caught our breath."
    MC "{i}*Huff*{/i} Fuck... Your ass is amazing."
    DROS "{i}S-So fucking full.{/i}"
    scene black with dissolve
    "Slowly, I unsheathed my cock from Draya's ass, watching as the excess seed poured out of her tight hole and dripped down onto the floor."
    DROS "(My legs are shaking so much! How am I supposed to go back to work after that?)"
    $ LocFlush()
    show dros at center
    with dissolve
    $ AutoMus(True)
    DROS @lewd "Phew!"
    DROS @smile "That was intense!"
    MC @smile "Worth the risk?"
    DROS @smile 'Without a doubt.'
    DROS @smile "Well, I best get changed again..."
    DROS @smile "Thanks for showing an elf a good time!"
    $ CharChangeRel("dros", 1)
    $ CharSetClothes("dros", "normal")
    $ LocEnter()

label dros_store_sex_preTf:
    'Dros blushed at the comment.'
    DROS @shock 'Y-You... W-What?'
    MC @smile 'Close. The. Store.'
    'Dros stuttered as he leaned in to whisper, looking around the empty store for anyone who might be listening.'
    DROS @lewd 'N-Now?'
    DROS @shock "Can't it wait? People might-"
    MC @talk "No. It can't wait."
    'Dros bit on his lower lip as he sheepishly headed towards the door to lock it, drawing what blinds he could.'
    DROS @lewd 'O-Okay... We just need to be quick.'
    DROS @lewd 'S-Should I... Get dressed?'
    menu:
        'Make it slutty.':
            $ CharSetClothes("dros", "dress")
            show dros at nod
            DROS @lewd 'A-Ah... Okay.'
        'Just take off your clothes.':
            $ CharSetClothes("dros", "naked")
            show dros at nod
            DROS @lewd "If that's what you want."
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    'Dros bent over the counter and waited with bated breath as I stripped down and lined up behind him.'
    'He breathed heavily as he looked over his shoulder at the massive cock which prodded and pressed against his tight rosebud.'
    DROS 'J-Just hurry up and-'
    $ PlaySexFx("audio/sex_sounds/no_voice.ogg",1)
    if CharGetClothes("dros") == "dress":
        scene dros_anal_dress
    if CharGetClothes("dros") == "naked":
        scene dros_anal_naked
    with dissolve
    $ Pause()
    'As my cock pushed into his tight ass, Dros gasped and moaned as I began to fuck him from behind.'
    'The soft flesh of his bubbly ass bounced against my cock as he moaned witch each thrust, his tight asshole squeezing down desperately on me.'
    DROS 'Ah! Ah! Gods! F-Fuck!' 
    MC "Bet your glad you - {i}*Huff*{/i} closed up now, huh?"
    DROS "S-Shuddup! I'm gonna open again after you-"
    DROS 'Oooooh! Gods, I love your fucking huge cock!'
    DROS 'This feels so good!'
    "I slapped Dros's ass playfully, leaving a pink hand print mark behind which he grunted to as I continued to defile his backdoor."
    MC 'Who owns this tight ass slut?'
    if CharGetClothes("dros") == "dress":
        scene dros_anal_dress_alt
    if CharGetClothes("dros") == "naked":
        scene dros_anal_naked_alt
    with dissolve
    $ Pause()
    DROS "AHH! You do [dros_player_ref!t]! You own this slut's ass!"
    'As I continued to slam against his soft, bubbly butt, Dros grunted and moaned lewdly as I felt my balls tighten and rise.'
    DROS 'Mmmfghh! C-Cum [dros_player_ref!t]! Fucking give it to me!'
    'Unable to hold back any longer, I gripped the soft flesh of his ass and grunted animalistically.'
    MC "H-Hrghh! I'm gonna fill your ass up!" 
    "Flooding Dros's tight ass, his eyes rolled back as I pumped his ass full of warm, thick seed."
    if CharGetClothes("dros") == "dress":
        scene dros_anal_dress_finish
        $ UnlockGalFlag("dros","store_anal","var_pretf_dress")
    if CharGetClothes("dros") == "naked":
        scene dros_anal_naked_finish
        $ UnlockGalFlag("dros","store_anal","var_pretf_naked")
    with flash
    $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
    $ ReduceInfectionFromSex("dros")
    $ UnlockGalSceneAndGrantXp("dros","store_anal")
    $ Pause()
    DROS "Urghhhh...!"
    "As Dros's ass swallowed my load, I held him there for a few moments as we caught our breath."
    MC "{i}*Huff*{/i} Fuck... Your ass is amazing."
    DROS "{i}S-So fucking full.{/i}"
    scene black with dissolve
    "Slowly, I unsheathed my cock from Dros's ass, watching as the excess seed poured out of his tight hole and dripped down onto the floor."
    DROS "(My legs are shaking so much! How am I supposed to go back to work after that?)"
    $ LocFlush()
    show dros at center
    with dissolve
    $ AutoMus(True)
    DROS @lewd "Phew!"
    DROS @smile "That was intense!"
    MC @smile "Worth the risk?"
    DROS @talk 'Without a doubt.'
    DROS @smile "Well, I best get changed again..."
    DROS @smile "Thanks for showing an elf a good time!"
    $ CharChangeRel("dros", 1)
    $ CharSetClothes("dros", "normal")
    $ LocEnter()