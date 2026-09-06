label gallery_ves_69:
    scene black with dissolve
    if GalFlag("ves","69",["var_ling","var_naked"]):
        "Was she wearing lingerie?"
        menu:
            "Yes":
                jump gallery_ves_69_ling
            "No, she was naked":
                jump gallery_ves_69_naked
    elif GalFlag("ves","69","var_ling"):
        jump gallery_ves_69_ling
    elif GalFlag("ves","69","var_naked"):
        jump gallery_ves_69_naked

label gallery_ves_69_naked:
    MC @talk 'Ves!—'
    $ PlayMusicRandom("mus_sex")
    MC @talk 'Mmmff!'
    scene ves_69_naked_slow with dissolve
    $ PlaySexFx("audio/sex_sounds/ves69_100.ogg",1)
    'Ves pushed her round butt against my face, and my tongue instinctively proded against her sweet hole.'
    VES @talk 'A-Ahhh!'
    "Ves' warm mouth wrapped around my member and her soft, delicate lips began to glide back and forth along the shaft."
    VES @talk 'Mmmfghh!'
    "With both hands on her soft butt, I continued to thrash my tongue around Ves' wet hole, occasionally prodding at the rim of her asshole making her tremble and let out another soft moan."
    scene ves_69_naked_normal with dissolve
    $ PlaySexFx("audio/sex_sounds/ves69_125.ogg",1)
    $ Pause()
    VES '(H-He keeps prodding at my other hole!)'
    VES '(D-Does he plan to try take me {i}there{/i} too?!)'
    VES '(A-Ah! It feels q-quite nice when his tongue hits there though...)'
    "Ves' body tightened and shook beneath my fingertips, I could feel her heart racing as she tried to take my cock deeper and faster into her throat."
    'Letting out a series of lewd wet slurping sounds while she did so, her soft moans between her desire to finish me only left me harder.'
    VES '(His tool is so thick, it feels like I can hardly fit it around my mouth...)'
    'Beneath my skin, once again I could feel the creature inside of me desperate to mate, to throw her down and shove my cock into her, see her filled with my seed and listen to her moan while she sired my children.'
    'But I held back, pushing the thought aside for now.'
    scene ves_69_naked_fast with dissolve
    $ PlaySexFx("audio/sex_sounds/ves69_150.ogg",1)
    $ Pause()
    VES '{i}*Glug!* *Glug!*{/i} Mmmmmfgh! {image=[ICON.HEART]}'
    VES "(So good... This feeling... It's... It's incredible! Ahh! I'm so close, I... I think I might-)"
    VES "(...!)"
    'Suddenly, Ves mouth threw itself forward with such passion, I was caught off guard as her body shook, and I knew then that she was cumming.'
    scene ves_69_naked_finish with flash
    $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
    $ Pause()
    'The sudden sensation was too much for me to bear, and Ves groaned as I unleashed a flood of my hot seed down her throat.'
    VES @talk 'Mmmfghhh!?'
    VES "(There's so much of it!)"
    'Ves did her best to swallow down as much of it as she could, before finally, she pulled her head away and gasped for air, rolling off to my side while laughing exhaustedly.'
    $ StopSexFx()
    scene black with dissolve
    VES @talk '{i}*Huff*{/i} That was... very good...'
    VES @talk '[player_name!t]? Are you okay?'
    MC @talk 'I think {i}*Huff*{/i} I’m just going to lay here for a bit...'
    return

label gallery_ves_69_ling:
    MC @talk 'Ves!—'
    $ PlayMusicRandom("mus_sex")
    MC @talk 'Mmmff!'
    scene ves_69_ling_slow with dissolve
    $ PlaySexFx("audio/sex_sounds/ves69_100.ogg",1)
    'Ves pushed her round butt against my face, and my tongue instinctively proded against her sweet hole.'
    VES @talk 'A-Ahhh!'
    "Ves' warm mouth wrapped around my member and her soft, delicate lips began to glide back and forth along the shaft."
    VES @talk 'Mmmfghh!'
    "With both hands on her soft butt, I continued to thrash my tongue around Ves' wet hole, occasionally prodding at the rim of her asshole making her tremble and let out another soft moan."
    scene ves_69_ling_normal with dissolve
    $ PlaySexFx("audio/sex_sounds/ves69_125.ogg",1)
    $ Pause()
    VES '(H-He keeps prodding at my other hole!)'
    VES '(D-Does he plan to try take me {i}there{/i} too?!)'
    VES '(A-Ah! It feels q-quite nice when his tongue hits there though...)'
    "Ves' body tightened and shook beneath my fingertips, I could feel her heart racing as she tried to take my cock deeper and faster into her throat."
    'Letting out a series of lewd wet slurping sounds while she did so, her soft moans between her desire to finish me only left me harder.'
    VES '(His tool is so thick, it feels like I can hardly fit it around my mouth...)'
    'Beneath my skin, once again I could feel the creature inside of me desperate to mate, to throw her down and shove my cock into her, see her filled with my seed and listen to her moan while she sired my children.'
    'But I held back, pushing the thought aside for now.'
    scene ves_69_ling_fast with dissolve
    $ PlaySexFx("audio/sex_sounds/ves69_150.ogg",1)
    $ Pause()
    VES '{i}*Glug!* *Glug!*{/i} Mmmmmfgh! {image=[ICON.HEART]}'
    VES "(So good... This feeling... It's... It's incredible! Ahh! I'm so close, I... I think I might-)"
    VES "(...!)"
    'Suddenly, Ves mouth threw itself forward with such passion, I was caught off guard as her body shook, and I knew then that she was cumming.'
    scene ves_69_ling_finish with flash
    $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
    $ Pause()
    'The sudden sensation was too much for me to bear, and Ves groaned as I unleashed a flood of my hot seed down her throat.'
    VES @talk 'Mmmfghhh!?'
    VES "(There's so much of it!)"
    'Ves did her best to swallow down as much of it as she could, before finally, she pulled her head away and gasped for air, rolling off to my side while laughing exhaustedly.'

    $ StopSexFx()
    scene black with dissolve
    VES @talk '{i}*Huff*{/i} That was... very good...'
    VES @talk '[player_name!t]? Are you okay?'
    MC @talk 'I think {i}*Huff*{/i} I’m just going to lay here for a bit...'
    return
