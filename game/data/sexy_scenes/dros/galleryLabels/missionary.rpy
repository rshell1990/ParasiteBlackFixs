label gallery_dros_miss:
    scene black with dissolve
    if ((GalFlag("dros","miss","var_pretf_naked") or 
        GalFlag("dros","miss","var_pretf_dress")) and 
        (GalFlag("dros","miss","var_posttf_naked") or 
        GalFlag("dros","miss","var_posttf_dress"))):
            "Was it Dros or Draya?"
            menu:
                "Dros":
                    jump gallery_dros_miss_pretf
                "Draya":
                    jump gallery_dros_miss_posttf
    elif GalFlag("dros","miss",["var_pretf_naked","var_pretf_dress"]):
        jump gallery_dros_miss_pretf
    elif GalFlag("dros","miss",["var_prostf_naked","var_posttf_dress"]):
        jump gallery_dros_miss_posttf
    
    elif GalFlag("dros","miss","var_pretf_naked"):
        jump gallery_dros_missionary_preTf_naked
    elif GalFlag("dros","miss","var_pretf_dress"):
        jump gallery_dros_missionary_preTf_dress
    elif GalFlag("dros","miss","var_posttf_naked"):
        jump gallery_dros_missionary_postTf_naked
    elif GalFlag("dros","miss","var_posttf_dress"):
        jump gallery_dros_missionary_postTf_dress

label gallery_dros_miss_pretf:
    if GalFlag("dros","miss",["var_pretf_naked","var_pretf_dress"]):
        "What was he wearing?"
        menu:
            "Not much.":
                jump gallery_dros_missionary_preTf_naked
            "That slutty outfit of his.":
                jump gallery_dros_missionary_preTf_dress
    elif GalFlag("dros","miss","var_pretf_naked"):
        jump gallery_dros_missionary_preTf_naked
    elif GalFlag("dros","miss","var_pretf_dress"):
        jump gallery_dros_missionary_preTf_dress

label gallery_dros_miss_posttf:
    if GalFlag("dros","miss",["var_posttf_naked","var_posttf_dress"]):
        "What was she wearing?"
        menu:
            "Not much.":
                jump gallery_dros_missionary_postTf_naked
            "That slutty outfit of hers.":
                jump gallery_dros_missionary_postTf_dress
    elif GalFlag("dros","miss","var_posttf_naked"):
        jump gallery_dros_missionary_postTf_naked
    elif GalFlag("dros","miss","var_posttf_dress"):
        jump gallery_dros_missionary_postTf_dress

label gallery_dros_missionary_preTf_naked:
    MC "Get onto the bed... {i}I need you now.{/i}"
    $ PlayMusicRandom("mus_sex")
    'Dros blushed at the comment, but he quickly did as he was told and crawled over onto the bed.'
    'Laying on his back, he spread his legs as he waited for me to join him.'
    DROS "I'm... {i}I'm ready.{/i}"
    $ PlaySexFx("audio/sex_sounds/no_voice.ogg",1)
    scene dros_miss_naked with dissolve
    $ Pause()
    'As my cock prodded against the tight rosebud hole he had lubed in preparation for me, his chest rose and dropped in excitement.'
    DROS "Gods... You're so-"
    'His asshole spread and widened as it swallowed my cock.'
    DROS 'BIGGGG!'
    'Dros flushed red from arousal as I began to thrust into his tight, warm ass.'
    'Inch by inch his butt swallowed me as he squeezed me tightly.'
    DROS 'F-Fuck...!'
    DROS "Fuck me! You f-feel i-incredibleee!"
    MC 'Ah! Your ass feels so tight!'
    'Dros briefly flashed a smile as his eyes watered slightly.'
    DROS 'E-Elvish ass is always tighter!'
    "Whether that was true or not didn't matter, what did matter was the sensation right now was extraordinary."
    "Soon, the two of us were dripping with sweat as his body welcomed me greedily, swallowing every inch as he tried to milk me dry."
    'Dros went wild as his body seemed to squeeze and release around me.'
    DROS '{i}F-Fuck me! Make me your elvish bitch!{/i}'
    DROS 'C-Cum! Please! I NEED to m-make you cum!'
    'The incredible intoxicating feeling was too much, and soon, my balls were rising as I could hold on no longer.'
    MC "Grghh! I'm cumming you little whore!"
    DROS "Oh fuck yes, [dros_player_ref!t]! I'm cumming too! I'm cumming so hard!"
    $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
    scene dros_miss_naked_finish with flash
    $ Pause()
    'Bottoming out into him, I grunted as I pumped his ass full of my seed.'
    DROS '{i}*Gasp!*{/i}'
    'Dros whimpered as his mouth hung open, feeling the seed pour into him.'
    DROS 'S-Soo... {i}much...{/i}'
    MC '{i}*Huff*{/i} Are you okay?'
    'Dros giggled weakly.'
    DROS 'S-Soo... full... and...'
    DROS "{i}Good.{/i}"
    return

label gallery_dros_missionary_preTf_dress:
    MC "Get onto the bed... {i}I need you now.{/i}"
    $ PlayMusicRandom("mus_sex")
    'Dros blushed at the comment, but he quickly did as he was told and crawled over onto the bed.'
    'Laying on his back, he spread his legs as he waited for me to join him.'
    DROS "I'm... {i}I'm ready.{/i}"
    $ PlaySexFx("audio/sex_sounds/no_voice.ogg",1)
    scene dros_miss_dress with dissolve
    $ Pause()
    'As my cock prodded against the tight rosebud hole he had lubed in preparation for me, his chest rose and dropped in excitement.'
    DROS "Gods... You're so-"
    'His asshole spread and widened as it swallowed my cock.'
    DROS 'BIGGGG!'
    'Dros flushed red from arousal as I began to thrust into his tight, warm ass.'
    'Inch by inch his butt swallowed me as he squeezed me tightly.'
    DROS 'F-Fuck...!'
    DROS "Fuck me! You f-feel i-incredibleee!"
    MC 'Ah! Your ass feels so tight!'
    'Dros briefly flashed a smile as his eyes watered slightly.'
    DROS 'E-Elvish ass is always tighter!'
    "Whether that was true or not didn't matter, what did matter was the sensation right now was extraordinary."
    "Soon, the two of us were dripping with sweat as his body welcomed me greedily, swallowing every inch as he tried to milk me dry."
    'Dros went wild as his body seemed to squeeze and release around me.'
    DROS '{i}F-Fuck me! Make me your elvish bitch!{/i}'
    DROS 'C-Cum! Please! I NEED to m-make you cum!'
    'The incredible intoxicating feeling was too much, and soon, my balls were rising as I could hold on no longer.'
    MC "Grghh! I'm cumming you little whore!"
    DROS "Oh fuck yes, [dros_player_ref!t]! I'm cumming too! I'm cumming so hard!"
    $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
    scene dros_miss_dress_finish with flash
    $ Pause()
    'Bottoming out into him, I grunted as I pumped his ass full of my seed.'
    DROS '{i}*Gasp!*{/i}'
    'Dros whimpered as his mouth hung open, feeling the seed pour into him.'
    DROS 'S-Soo... {i}much...{/i}'
    MC '{i}*Huff*{/i} Are you okay?'
    'Dros giggled weakly.'
    DROS 'S-Soo... full... and...'
    DROS "{i}Good.{/i}"
    return

label gallery_dros_missionary_postTf_naked:
    MC "Get onto the bed... {i}I need you now.{/i}"
    $ PlayMusicRandom("mus_sex")
    'Draya blushed at the comment, but she quickly did as she was told and crawled over onto the bed.'
    'Laying on her back, she spread her legs as she waited for me to join her.'
    DROS "I'm... {i}I'm ready.{/i}"
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg",1)
    scene draya_miss_naked with dissolve
    $ Pause()
    'As my cock prodded against the tight rosebud hole she had lubed in preparation for me, her chest rose and dropped in excitement.'
    DROS "Gods... You're so-"
    'Her asshole spread and widened as it swallowed my cock.'
    DROS 'BIGGGG!'
    'Draya flushed red from arousal as I began to thrust into their tight, warm ass.'
    'Inch by inch her butt swallowed me as she squeezed me tightly.'
    DROS 'F-Fuck...!'
    DROS "Fuck me! You f-feel i-incredibleee!"
    MC 'Ah! Your ass feels so tight!'
    'Draya briefly flashed a smile as her eyes watered slightly.'
    DROS 'E-Elvish ass is always tighter!'
    "Whether that was true or not didn't matter, what did matter was the sensation right now was extraordinary."
    "Soon, the two of us were dripping with sweat as her body welcomed me greedily, swallowing every inch as she tried to milk me dry."
    'Draya went wild as her body seemed to squeeze and release around me.'
    DROS '{i}F-Fuck me! Make me your elvish bitch!{/i}'
    DROS 'C-Cum! Please! I NEED to m-make you cum!'
    'The incredible intoxicating feeling was too much, and soon, my balls were rising as I could hold on no longer.'
    MC "Grghh! I'm cumming you little whore!"
    DROS "Oh fuck yes, [dros_player_ref!t]! I'm cumming too! I'm cumming so hard!"
    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    scene draya_miss_naked_finish with flash
    $ Pause()
    'Bottoming out into her, I grunted as I pumped her ass full of my seed.'
    DROS '{i}*Gasp!*{/i}'
    'Draya whimpered as her mouth hung open, feeling the seed pour into her.'
    DROS 'S-Soo... {i}much...{/i}'
    MC '{i}*Huff*{/i} Are you okay?'
    'Draya giggled weakly.'
    DROS 'S-Soo... full... and...'
    DROS "{i}Good.{/i}"
    return

label gallery_dros_missionary_postTf_dress:
    MC "Get onto the bed... {i}I need you now.{/i}"
    $ PlayMusicRandom("mus_sex")
    'Draya blushed at the comment, but she quickly did as she was told and crawled over onto the bed.'
    'Laying on her back, she spread her legs as she waited for me to join her.'
    DROS "I'm... {i}I'm ready.{/i}"
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg",1)
    scene draya_miss_dress with dissolve
    $ Pause()
    'As my cock prodded against the tight rosebud hole she had lubed in preparation for me, her chest rose and dropped in excitement.'
    DROS "Gods... You're so-"
    'Her asshole spread and widened as it swallowed my cock.'
    DROS 'BIGGGG!'
    'Draya flushed red from arousal as I began to thrust into their tight, warm ass.'
    'Inch by inch her butt swallowed me as she squeezed me tightly.'
    DROS 'F-Fuck...!'
    DROS "Fuck me! You f-feel i-incredibleee!"
    MC 'Ah! Your ass feels so tight!'
    'Draya briefly flashed a smile as her eyes watered slightly.'
    DROS 'E-Elvish ass is always tighter!'
    "Whether that was true or not didn't matter, what did matter was the sensation right now was extraordinary."
    "Soon, the two of us were dripping with sweat as her body welcomed me greedily, swallowing every inch as she tried to milk me dry."
    'Draya went wild as her body seemed to squeeze and release around me.'
    DROS '{i}F-Fuck me! Make me your elvish bitch!{/i}'
    DROS 'C-Cum! Please! I NEED to m-make you cum!'
    'The incredible intoxicating feeling was too much, and soon, my balls were rising as I could hold on no longer.'
    MC "Grghh! I'm cumming you little whore!"
    DROS "Oh fuck yes, [dros_player_ref!t]! I'm cumming too! I'm cumming so hard!"
    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    scene draya_miss_dress_finish with flash
    $ Pause()
    'Bottoming out into her, I grunted as I pumped her ass full of my seed.'
    DROS '{i}*Gasp!*{/i}'
    'Draya whimpered as her mouth hung open, feeling the seed pour into her.'
    DROS 'S-Soo... {i}much...{/i}'
    MC '{i}*Huff*{/i} Are you okay?'
    'Draya giggled weakly.'
    DROS 'S-Soo... full... and...'
    DROS "{i}Good.{/i}"
    return