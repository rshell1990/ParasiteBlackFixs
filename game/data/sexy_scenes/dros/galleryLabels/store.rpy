label gallery_dros_store_anal:
    scene black with dissolve
    if ((GalFlag("dros","store_anal","var_pretf_naked") or 
        GalFlag("dros","store_anal","var_pretf_dress")) and 
        (GalFlag("dros","store_anal","var_posttf_naked") or 
        GalFlag("dros","store_anal","var_posttf_dress"))):
            "Was it Dros or Draya?"
            menu:
                "Dros":
                    jump gallery_dros_store_anal_pretf
                "Draya":
                    jump gallery_dros_store_anal_posttf
    elif GalFlag("dros","store_anal",["var_pretf_naked","var_pretf_dress"]):
        jump gallery_dros_store_anal_pretf
    elif GalFlag("dros","store_anal",["var_prostf_naked","var_posttf_dress"]):
        jump gallery_dros_store_anal_posttf
    
    elif GalFlag("dros","store_anal","var_pretf_naked"):
        jump gallery_dros_shop_preTf_naked
    elif GalFlag("dros","store_anal","var_pretf_dress"):
        jump gallery_dros_shop_preTf_dress
    elif GalFlag("dros","store_anal","var_posttf_naked"):
        jump gallery_dros_shop_postTf_naked
    elif GalFlag("dros","store_anal","var_posttf_dress"):
        jump gallery_dros_shop_postTf_dress

label gallery_dros_store_anal_pretf:
    if GalFlag("dros","store_anal",["var_pretf_naked","var_pretf_dress"]):
        "What was he wearing?"
        menu:
            "Not much.":
                jump gallery_dros_shop_preTf_naked
            "That slutty outfit of his.":
                jump gallery_dros_shop_preTf_dress
    elif GalFlag("dros","store_anal","var_pretf_naked"):
        jump gallery_dros_shop_preTf_naked
    elif GalFlag("dros","store_anal","var_pretf_dress"):
        jump gallery_dros_shop_preTf_dress

label gallery_dros_store_anal_posttf:
    if GalFlag("dros","store_anal",["var_posttf_naked","var_posttf_dress"]):
        "What was she wearing?"
        menu:
            "Not much.":
                jump gallery_dros_shop_postTf_naked
            "That slutty outfit of hers.":
                jump gallery_dros_shop_postTf_dress
    elif GalFlag("dros","store_anal","var_postTf_naked"):
        jump gallery_dros_shop_postTf_naked
    elif GalFlag("dros","store_anal","var_postTf_dress"):
        jump gallery_dros_shop_postTf_dress

label gallery_dros_shop_preTf_naked:
    'Dros bent over the counter and waited with bated breath as I stripped down and lined up behind him.'
    'He breathed heavily as he looked over his shoulder at the massive cock which prodded and pressed against his tight rosebud.'
    DROS 'J-Just hurry up and-'
    $ PlaySexFx("audio/sex_sounds/no_voice.ogg",1)
    scene dros_anal_naked with dissolve
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
    scene dros_anal_naked_alt with dissolve
    $ Pause()
    DROS "AHH! You do [dros_player_ref!t]! You own this slut's ass!"
    'As I continued to slam against his soft, bubbly butt, Dros grunted and moaned lewdly as I felt my balls tighten and rise.'
    DROS 'Mmmfghh! C-Cum [dros_player_ref!t]! Fucking give it to me!'
    'Unable to hold back any longer, I gripped the soft flesh of his ass and grunted animalistically.'
    MC "H-Hrghh! I'm gonna fill your ass up!" 
    "Flooding Dros's tight ass, his eyes rolled back as I pumped his ass full of warm, thick seed."
    scene dros_anal_naked_finish with flash
    $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
    $ Pause()
    DROS "Urghhhh...!"
    "As Dros's ass swallowed my load, I held him there for a few moments as we caught our breath."
    MC "{i}*Huff*{/i} Fuck... Your ass is amazing."
    DROS "{i}S-So fucking full.{/i}"
    scene black with dissolve
    "Slowly, I unsheathed my cock from Dros's ass, watching as the excess seed poured out of his tight hole and dripped down onto the floor."
    DROS "(My legs are shaking so much! How am I supposed to go back to work after that?)"
    return

label gallery_dros_shop_preTf_dress:
    'Dros bent over the counter and waited with bated breath as I stripped down and lined up behind him.'
    'He breathed heavily as he looked over his shoulder at the massive cock which prodded and pressed against his tight rosebud.'
    DROS 'J-Just hurry up and-'
    $ PlaySexFx("audio/sex_sounds/no_voice.ogg",1)
    scene dros_anal_dress with dissolve
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
    scene dros_anal_dress_alt with dissolve
    $ Pause()
    DROS "AHH! You do [dros_player_ref!t]! You own this slut's ass!"
    'As I continued to slam against his soft, bubbly butt, Dros grunted and moaned lewdly as I felt my balls tighten and rise.'
    DROS 'Mmmfghh! C-Cum [dros_player_ref!t]! Fucking give it to me!'
    'Unable to hold back any longer, I gripped the soft flesh of his ass and grunted animalistically.'
    MC "H-Hrghh! I'm gonna fill your ass up!" 
    "Flooding Dros's tight ass, his eyes rolled back as I pumped his ass full of warm, thick seed."
    scene dros_anal_dress_finish with flash
    $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
    $ Pause()
    DROS "Urghhhh...!"
    "As Dros's ass swallowed my load, I held him there for a few moments as we caught our breath."
    MC "{i}*Huff*{/i} Fuck... Your ass is amazing."
    DROS "{i}S-So fucking full.{/i}"
    scene black with dissolve
    "Slowly, I unsheathed my cock from Dros's ass, watching as the excess seed poured out of his tight hole and dripped down onto the floor."
    DROS "(My legs are shaking so much! How am I supposed to go back to work after that?)"
    return

label gallery_dros_shop_postTf_naked:
    'Draya bent over the counter and waited with bated breath as I stripped down and lined up behind her.'
    'Draya breathed heavily as she looked over her shoulder at the massive cock which prodded and pressed against her tight rosebud.'
    DROS 'J-Just hurry up and-'
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg",1)
    scene draya_anal_naked with dissolve
    $ Pause()
    'As my cock pushed into her tight ass, Draya gasped and moaned as I began to fuck her from behind.'
    'The soft flesh of her bubbly ass bounced against my cock as she moaned with each thrust, her tight asshole squeezing down desperately on me.'
    DROS 'Ah! Ah! Gods! F-Fuck!' 
    MC "Bet your glad you - {i}*Huff*{/i} closed up now, huh?"
    DROS "S-Shuddup! I'm gonna open again after you-"
    DROS 'Oooooh! Gods, I love your fucking huge cock!'
    DROS 'This feels so good!'
    "I slapped Draya's ass playfully, leaving a pink hand print mark behind which she grunted to as I continued to defile her backdoor."
    scene draya_anal_naked_alt with dissolve
    $ Pause()
    MC 'Who owns this tight ass slut?'
    DROS "AHH! You do [dros_player_ref!t]! You own this slut's fat ass!"
    'As I continued to slam against her soft, bubbly butt, Draya grunted and moaned lewdly as I felt my balls tighten and rise.'
    DROS 'Mmmfghh! C-Cum [dros_player_ref!t]! Fucking give it to me!'
    'Unable to hold back any longer, I gripped the soft flesh of her ass and grunted animalistically,'
    MC "H-Hrghh! I'm gonna fill your ass up!" 
    "Flooding Draya's tight ass, her eyes rolled back as I pumped her ass full of warm, thick seed."
    scene draya_anal_naked_finish with flash
    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    $ Pause()
    DROS "Urghhhh...!"
    "As Draya's ass swallowed my load, I held her there for a few moments as we caught our breath."
    MC "{i}*Huff*{/i} Fuck... Your ass is amazing."
    DROS "{i}S-So fucking full.{/i}"
    scene black with dissolve
    "Slowly, I unsheathed my cock from Draya's ass, watching as the excess seed poured out of her tight hole and dripped down onto the floor."
    DROS "(My legs are shaking so much! How am I supposed to go back to work after that?)"
    return

label gallery_dros_shop_postTf_dress:
    'Draya bent over the counter and waited with bated breath as I stripped down and lined up behind her.'
    'Draya breathed heavily as she looked over her shoulder at the massive cock which prodded and pressed against her tight rosebud.'
    DROS 'J-Just hurry up and-'
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg",1)
    scene draya_anal_dress with dissolve
    $ Pause()
    'As my cock pushed into her tight ass, Draya gasped and moaned as I began to fuck her from behind.'
    'The soft flesh of her bubbly ass bounced against my cock as she moaned with each thrust, her tight asshole squeezing down desperately on me.'
    DROS 'Ah! Ah! Gods! F-Fuck!' 
    MC "Bet your glad you - {i}*Huff*{/i} closed up now, huh?"
    DROS "S-Shuddup! I'm gonna open again after you-"
    DROS 'Oooooh! Gods, I love your fucking huge cock!'
    DROS 'This feels so good!'
    "I slapped Draya's ass playfully, leaving a pink hand print mark behind which she grunted to as I continued to defile her backdoor."
    scene draya_anal_dress_alt with dissolve
    $ Pause()
    MC 'Who owns this tight ass slut?'
    DROS "AHH! You do [dros_player_ref!t]! You own this slut's fat ass!"
    'As I continued to slam against her soft, bubbly butt, Draya grunted and moaned lewdly as I felt my balls tighten and rise.'
    DROS 'Mmmfghh! C-Cum [dros_player_ref!t]! Fucking give it to me!'
    'Unable to hold back any longer, I gripped the soft flesh of her ass and grunted animalistically,'
    MC "H-Hrghh! I'm gonna fill your ass up!" 
    "Flooding Draya's tight ass, her eyes rolled back as I pumped her ass full of warm, thick seed."
    scene draya_anal_dress_finish with flash
    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    $ Pause()
    DROS "Urghhhh...!"
    "As Draya's ass swallowed my load, I held her there for a few moments as we caught our breath."
    MC "{i}*Huff*{/i} Fuck... Your ass is amazing."
    DROS "{i}S-So fucking full.{/i}"
    scene black with dissolve
    "Slowly, I unsheathed my cock from Draya's ass, watching as the excess seed poured out of her tight hole and dripped down onto the floor."
    DROS "(My legs are shaking so much! How am I supposed to go back to work after that?)"
    return