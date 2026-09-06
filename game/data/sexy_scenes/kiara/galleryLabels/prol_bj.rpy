label gallery_kiara_prol_bj:
    'With a small smile, Kiara led me away to a quiet spot in one of the rooms of the old huts.'
    'Outside I could hear the nervous chatter of other Scouts as they passed by on patrol as Kiara crouched down and pulled out my member.'
    $ PlayMusicRandom("mus_sex")
    scene kiara_prol_bj_no_hand with dissolve
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg",1)
    $ Pause()
    'Doing her best to keep quiet, Kiara began to tenderly suck my cock.'
    'Her bright wide eyes looked up to me with doe-like innocence as her lips formed a tight seal around my me.'
    'I did my best to hide my grunts of pleasure as her soft mouth moved back and forth along the shaft soothingly.'
    'Her tongue twisted around me, swirling around my head and making me shiver in pleasure as soft moans escaped through her pursed lips.'
    MC 'Ahh... K-Kiara...'

    if GalFlag("kiara", "prol_bj", ["var_hand", "var_no_hand"]):
        menu:
            'Put your hand on the back of her head.':
                scene kiara_prol_bj with dissolve
                'I ran my hands through her short, soft hair, and holding her head in place began to push gently down so she could take my cock even deeper.'
            'Let her continue.': 
                pass

    elif GalFlag("kiara", "prol_bj", ["var_hand"]):
        scene kiara_prol_bj with dissolve
        'I ran my hands through her short, soft hair, and holding her head in place began to push gently down so she could take my cock even deeper.'

    'Sensing my enjoyment Kiara continued enthusiastically, my cock started to throb in her mouth.'
    'Every so often, she would pull away to run her tongue along the shaft and nuzzle at my balls, pulling each of them into her mouth one at a time, delicately surrounding them with her warm, wet mouth.'
    'I ran my hands through her short, soft hair, and holding her head in place began to push gently down so she could take my cock even deeper.'
    'She reached around with her hands and grabbed my ass, pulling me as far into her mouth as she could handle.'
    'For a few moments, I forgot about the nightmarish world outside of this hut and wished I could stay here with her forever.'
    'Knowing I wouldn’t be able to hold on much more, my hands coiled into her hair as I picked up the pace, now thrusting into Kiara.'
    'Unable to hold back, the lewd slurping sounds became louder as Kiara realized I was close to finishing.'
    'As Kiara moaned erotically, my balls began to rise up and tighten as I found myself right on the cusp of losing control.'

    if GalFlag("kiara", "prol_bj", ["var_in","var_out"]):
        "Did I..."
        menu:
            "Cum in Kiara's mouth?":
                $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
                scene kiara_prol_bj_finish_in with flash
                $ Pause()
                'I gripped her head, pushing myself deeper into her eager mouth, Kiara’s eyes widened as she felt my hot seed pouring into her.'
                'She whimpered and moaned with pleasure, when she was sure I was finished she pulled back, swallowing down my seed and opening her mouth to lewdly show me she had done so.'
            "Cum on Kiara's face?":
                $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
                scene kiara_prol_bj_finish_out with flash
                $ Pause()
                "Pulling my cock out of Kiara's mouth, she waited patiently with her mouth and tongue open as after quickly stroking my cock, I covered her face with my hot load."
                "As the thick cum splashed onto Kiara's face, she giggled as she swallowed the part of the load that landed on her tongue."
                KIARA "Fuckin' hells ... Are you sure we're eating the same rations?"

    elif GalFlag("kiara", "prol_bj", "var_in"):
        $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
        scene kiara_prol_bj_finish_in with flash
        $ Pause()
        'I gripped her head, pushing myself deeper into her eager mouth, Kiara’s eyes widened as she felt my hot seed pouring into her.'
        'She whimpered and moaned with pleasure, when she was sure I was finished she pulled back, swallowing down my seed and opening her mouth to lewdly show me she had done so.'

    elif GalFlag("kiara", "prol_bj", "var_out"):
        $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
        scene kiara_prol_bj_finish_out with flash
        $ Pause()
        "Pulling my cock out of Kiara's mouth, she waited patiently with her mouth and tongue open as after quickly stroking my cock, I covered her face with my hot load."
        "As the thick cum splashed onto Kiara's face, she giggled as she swallowed the part of the load that landed on her tongue."
        KIARA "Fuckin' hells ... Are you sure we're eating the same rations?"

    MC '{i}*Huff*{/i} Oh fuck... That was... That was {i}really{/i} good.'
    return
