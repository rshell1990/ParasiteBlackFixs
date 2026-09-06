label gallery_divine_standing:
    $ tmpvar["scene_variants"] = [
        "ling_vag_preg",
        "ling_vag_nopreg",
        "naked_vag_preg",
        "naked_vag_nopreg",
        "naked_anal_preg",
        "naked_anal_nopreg",
        "ling_anal_preg",
        "ling_anal_nopreg"]

########################
    if GalFlag("divine", "standing", "var_first_anal") or GalFlag("divine", "standing", "var_first_vag"):
        if GalFlag("divine", "standing", tmpvar["scene_variants"], anymatch = True):
            "Was it our first time?"
            menu:
                "Yes":
                    $ tmpvar["first_time"] = True
                "No":
                    $ tmpvar["first_time"] = False
        else:
            $ tmpvar["first_time"] = True
    else:
        $ tmpvar["first_time"] = False
#######################
    if tmpvar["first_time"]:
        $ tmpvar["ling"] = True
        $ tmpvar["preg"] = False
    else:
        if GalFlag("divine", "standing", [x for x in tmpvar["scene_variants"] if "naked" in x], anymatch = True) and GalFlag("divine", "standing", [x for x in tmpvar["scene_variants"] if "ling" in x], anymatch = True):
            "Was she wearing her lingerie?"
            menu:
                "Yes":
                    $ tmpvar["ling"] = True
                "No":
                    $ tmpvar["ling"] = False
        elif GalFlag("divine", "standing", [x for x in tmpvar["scene_variants"] if "naked" in x], anymatch = True):
            $ tmpvar["ling"] = False
        else:
            $ tmpvar["ling"] = True
        #######################
        if GalFlag("divine", "standing", [x for x in tmpvar["scene_variants"] if "preg" in x], anymatch = True) and GalFlag("divine", "standing", [x for x in tmpvar["scene_variants"] if "nopreg" in x], anymatch = True):
            "Was she pregnant at the time?"
            menu:
                "Yes":
                    $ tmpvar["preg"] = True
                "No":
                    $ tmpvar["preg"] = False
        elif GalFlag("divine", "standing", [x for x in tmpvar["scene_variants"] if "preg" in x], anymatch = True):
            $ tmpvar["preg"] = True
        else:
            $ tmpvar["preg"] = False
        ########################
    jump gallery_divine_standing_scene

label gallery_divine_standing_scene:
    scene bg_palam_divine_quarters_night
    show divine at cright_f
    show mc_transformed_erect at cleft
    with dissolve
    "Stepping towards Sister Divine, she seemed nervous for a moment as I towered over her, my powerful large hands grabbing at her sides."
    show mc_transformed_erect at center with easeinleft
    DIVINE "M-My... What did you-"
    DIVINE "{i}*Gasp!*{/i}"
    "Spinning her around, I used my hands to bend her forward, her round plump ass now fully exposed for me as it bathed in the moonlight."
    "Beneath her enticing, wet, tight holes dangled her cock, hard with anticipation as she waited for me to take her from behind."
    "I could feel her heart racing beneath my fingertips as she breathed heavily in an intoxicating mix of nervousness and arousal." 
    "As my cock rubbed against the crack of her butt she cooed:"
    if tmpvar["first_time"]:
        DIVINE "So... This is how you want to take me this time, huh?"
    DIVINE "{i}...I’m ready.{/i}"
    "I leaned forward, grunting as I nuzzled at her neck before pulling back."
    if tmpvar["first_time"]:
        if GalFlag("divine", "standing", "var_first_anal") and GalFlag("divine", "standing", "var_first_vag"):
            "Which hole did I take?"
            menu:
                "Her pussy":
                    $ tmpvar["vag"] = True
                "Her ass":
                    $ tmpvar["vag"] = False
        elif GalFlag("divine", "standing", "var_first_anal"):
            $ tmpvar["vag"] = False
    else:
        if GalFlag("divine", "standing", [x for x in tmpvar["scene_variants"] if "vag_" in x], anymatch = True) and GalFlag("divine", "standing", [x for x in tmpvar["scene_variants"] if "anal_" in x], anymatch = True):
            "Which hole did I take?"
            menu:
                "Her pussy":
                    $ tmpvar["vag"] = True
                "Her ass":
                    $ tmpvar["vag"] = False
        elif GalFlag("divine", "standing", [x for x in tmpvar["scene_variants"] if "vag_" in x], anymatch = True):
            $ tmpvar["vag"] = True
        else:
            $ tmpvar["vag"] = False
    
    if tmpvar["vag"]:
        jump gallery_divine_standing_vag
    else:
        jump gallery_divine_standing_anal

label gallery_divine_standing_vag:
    "As I pressed and prodded my member against her wet, tight pussy, I felt Sister Divine tighten up."
    "I pushed my member as far I could into her."
    if tmpvar["first_time"]:
        DIVINE "By the gods!~"
        DIVINE "Wait! Wait! Give me a moment to adjust!"
    else:
        DIVINE "A-Ahh! I almost forgot how big you were!"
        DIVINE "Give me a moment to adjust!"
    "I paused for a moment, letting Sister Divine catch her breath as she trembled beneath my claws, her legs slightly shaking."
    if tmpvar["first_time"]:
        DIVINE "{i}Yes...{/i} It’s been a while since I've had to take a sword quite like yours."
    else:
        DIVINE "I've missed this sword of yours..."
    DIVINE "Come, continue!"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_standing_ling_vag_preg_notent
        else:
            scene divine_standing_ling_vag_nopreg_notent
    else:
        if tmpvar["preg"]:
            scene divine_standing_naked_vag_preg_notent
        else:
            scene divine_standing_naked_vag_nopreg_notent
    with dissolve
    $ Pause()
    DIVINE "Mmmfgh! Yes! That’s it!"
    "Her body tightened around me as we picked up the pace."
    "Sister Divine backed her round, large butt up onto me slowly as she began to moan."
    "Her hard member moved as her large breasts swayed with every thrust."
    DIVINE "Yes ... J-just like that."
    DIVINE "F-Faster ... Go faster!"
    "I did as she asked, the fleshy sounds of her butt slapping against me grew louder and faster as I took her from behind."
    DIVINE "Yes! That's it! YES!"
    DIVINE "Gods, you're huge!"
    "In that moment, the dark desires came bubbling to the surface, and I remembered what my tentacles could do..."
    "Suddenly, as one of tentacles appeared over my shoulder, it slowly made it’s way towards the back of Sister Divine’s head."
    "With the teeth retracted, it began to swallow her head from behind."
    "Sister Divine panicked for a moment, seeking to break away but I held her firmly in place."
    DIVINE "W-What are you-!"
    DIVINE "Mmmfgh?!"
    $ PlaySexFx("audio/sex_sounds/ves69_150.ogg", 1)
    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_standing_ling_vag_preg_tent
        else:
            scene divine_standing_ling_vag_nopreg_tent
    else:
        if tmpvar["preg"]:
            scene divine_standing_naked_vag_preg_tent
        else:
            scene divine_standing_naked_vag_nopreg_tent
    with dissolve
    $ Pause()
    "In that moment, the tentacle swallowed over the top of Sister Divine’s head, and she squirmed in worry for a moment, before she felt the tongue slip deep down her throat." 
    if tmpvar["first_time"]:
        DIVINE "(W-What is this thing?)"
        DIVINE "(I... I can breathe even though it’s-)"
    else:
        DIVINE "(Ahh... T-These again!)"
        DIVINE "(Thank the gods I can still breathe with this thing down my throat!)"
    "Roaring with delight, I began to pump her body from behind furiously."
    "Muffled cries and moans escaped Sister Divine from inside the bulbous head of the tentacle, but her wetness gave away her excitement as I continued to slam against her soft round ass from behind."
    DIVINE "Mmmmfghhh!!"
    if tmpvar["first_time"]:
        DIVINE "(It’s pumping something into me! Is it... Feeding me?)"
        DIVINE "(Gods... {i}It’s wonderful!{/i})"
        DIVINE "(Whatever it’s giving me! My body feels like fire!)"
    else:
        DIVINE "(It’s pumping something into me again... Mhmm!)"
        DIVINE "(Gods... {i}It’s wonderful!{/i})"
        DIVINE "(My body feels like fire!)"
    "Sister Divine’s body continuously tightened, she was now just a play doll for me to use, not a person but a thing for me to mate and have my way with."
    "Continuous grunts and muffled moans escaped her lips uncontrollably as she had her third and fourth orgasms, her juices dripping down onto the floor, but I wasn’t done yet..."
    DIVINE "(Oh gods... How much longer will this last?)"
    DIVINE "(I feel like I am melting!)"
    scene black with dissolve
    $ Pause(0.5)
    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_standing_ling_vag_preg_tent
        else:
            scene divine_standing_ling_vag_nopreg_tent
    else:
        if tmpvar["preg"]:
            scene divine_standing_naked_vag_preg_tent
        else:
            scene divine_standing_naked_vag_nopreg_tent
    with dissolve
    "Before I knew it, an hour had passed."
    "I held tightly onto her soft ass cheeks and sharply pulled her back, shoving my cock in all the way."
    DIVINE "(Oh gods ... I can't even think anymore!)"
    DIVINE "(Mhmm! He's close! I can f-feel he's finally close!)"
    "I dug my claws into Divine's round ass, making her yelp out as I slammed my cock into her the last few times before I forced it inside her and held it there."
    "Emptying myself deeply into her pussy, I roared."
    $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
    play sound2 "audio/cfx/transform.ogg"
    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_standing_ling_vag_preg_finish
        else:
            scene divine_standing_ling_vag_nopreg_finish
    else:
        if tmpvar["preg"]:
            scene divine_standing_naked_vag_preg_finish
        else:
            scene divine_standing_naked_vag_nopreg_finish
    with flash
    $ Pause()
    DIVINE "(T-There's so much of it! H-He's filling me up so much! {image=[ICON.HEART]})"
    DIVINE "(It's so hot! I c-can feel it overflowing!)"
    "Finally satisfied, I slowly unsheathed my cock from her, and as the tentacle loosened and released her head, Sister Divine slumped to the floor deliriously."
    "I watched as my seed poured from her aching, stretched pussy while some of my... chemical poured from the side of her mouth onto the floor."
    "She shook slightly, her body overcome by pleasure as I leaned down to pick her up and rest her on the bed, nuzzling and soothing her."
    DIVINE "Urghh..."
    "After a few moments of slight anxious worry that I had pushed her too far, the murmured, exhausted words escaped her lips:"
    DIVINE "{i}Incredible...{/i} {image=[ICON.HEART]}"
    return

label gallery_divine_standing_anal:
    "With a snort of hot air, I pressed my cock against the rosebud of Sister Divine’s tight asshole."
    "She gasped in surprise at first, before giggling and looking over her shoulder with a playful smirk."
    DIVINE "Oh my..."
    DIVINE "Quite the mischievous beast wanting {i}that{/i} hole, aren’t you?"
    "I grunted in acknowledgment, my raspy voice remarking,"
    MC "Your body belongs to me tonight."
    DIVINE "Ahh~ then do what you must with me..."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_standing_ling_anal_preg_notent
        else:
            scene divine_standing_ling_anal_nopreg_notent
    else:
        if tmpvar["preg"]:
            scene divine_standing_naked_anal_preg_notent
        else:
            scene divine_standing_naked_anal_nopreg_notent
    $ Pause()
    "Sister Divine let out a gasp followed shortly by a loud moan as I forced my cock into her tight ass."
    DIVINE "Gods... You really are-ah! S-Stretching it back there!"
    DIVINE "Mmmfgh... {image=[ICON.HEART]}"
    DIVINE "Don’t stop, k-keep going!"
    "In that moment, the dark desires came bubbling to the surface, and I remembered what my tentacles could do..."
    "Suddenly, as one of tentacles appeared over my shoulder, it slowly made its way towards the back of Sister Divine’s head."
    "With the teeth retracted, it began to swallow her head from behind."
    DIVINE "W-What are you-"
    DIVINE "Mmmfgh?!"
    $ PlaySexFx("audio/sex_sounds/ves69_150.ogg", 1)
    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_standing_ling_anal_preg_tent
        else:
            scene divine_standing_ling_anal_nopreg_tent
    else:
        if tmpvar["preg"]:
            scene divine_standing_naked_anal_preg_tent
        else:
            scene divine_standing_naked_anal_nopreg_tent
    $ Pause()
    "In that moment, the tentacle swallowed up the top of Sister Divine’s head, and she squirmed in worry for a moment before she felt the tongue slip deep down her throat."
    if tmpvar["first_time"]:
        DIVINE "(W-What is this thing?)"
        DIVINE "(I... I can breathe even though it’s-)"
    else:
        DIVINE "(Ahh... T-These again!)"
        DIVINE "(Thank the gods I can still breathe with this thing down my throat!)"
    "Muffled cries and moans escaped Sister Divine from inside the bulbous head of the tentacle, but her tight asshole quivered around my cock as her pussy beneath became soaking wet."
    "Dripping onto the floor, her juices gave away her excitement while I continued to slam against her soft round ass from behind."
    DIVINE "Mmmmfghhh!!"
    if tmpvar["first_time"]:
        DIVINE "(It’s pumping something into me! Is it... Feeding me?)"
        DIVINE "(Gods... {i}It’s wonderful!{/i})"
        DIVINE "(My ass! Oh gods! It’s never felt {i}this{/i} good before!)"
        DIVINE "(Whatever it’s giving me! My body feels like fire!)"
    else:
        DIVINE "(It’s pumping something into me again...Mhmm!)"
        DIVINE "(Gods...{i}It’s wonderful!{/i})"
        DIVINE "(My ass! Oh gods! It’s never felt {i}this{/i} good before!)"
        DIVINE "(My body feels like fire!)"
    
    DIVINE "{i}(Mmmfghh!){/i}"
    "Unable to control herself anymore, I felt Sister Divine’s body continuously tighten and shake around me."
    "She was now just a play doll for me to use, not a person but a thing for me to mate and have my way with."
    "Her asshole gripped me tight, and despite my best efforts not to hurt her, it was next to impossible not to let the pulsating darkness in me thrust furiously into her backdoor."
    "Continuous grunts and muffled moans escaped her lips now, as she had her third and fourth orgasms."
    "A puddle of her juices formed beneath her, but I wasn’t done yet..."
    scene black with dissolve
    $ Pause(0.5)
    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_standing_ling_anal_preg_tent
        else:
            scene divine_standing_ling_anal_nopreg_tent
    else:
        if tmpvar["preg"]:
            scene divine_standing_naked_anal_preg_tent
        else:
            scene divine_standing_naked_anal_nopreg_tent
    with dissolve
    $ Pause()
    "Before I knew it, an hour had passed."
    "I held tightly onto her soft ass cheeks and sharply pulled her back on my cock."
    DIVINE "(Oh gods ... I can't even think anymore!)"
    DIVINE "(Mhmm! He's close! I can f-feel he's finally close!)"
    "I dug my claws into Divine's round ass, making her yelp out, slamming my cock into her the last few times before I forced it all the way in."
    "I pushed the whole length of my cock inside of her ass and held it there."
    "Emptying myself deeply into her asshole, I roared."
    $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
    play sound2 "audio/cfx/transform.ogg"
    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_standing_ling_anal_preg_finish
        else:
            scene divine_standing_ling_anal_nopreg_finish
    else:
        if tmpvar["preg"]:
            scene divine_standing_naked_anal_preg_finish
        else:
            scene divine_standing_naked_anal_nopreg_finish
    with flash
    $ Pause()
    DIVINE "(T-There's so much of it! H-He's filling me up so much! {image=[ICON.HEART]})"
    DIVINE "(It's so hot! I c-can feel it overflowing!)"
    "Finally satisfied, I unsheathed my cock from her, and as the tentacle loosened and released from her head, Sister Divine slumped to the floor deliriously."
    "I watched as my seed poured from her aching, stretched ass while some of the chemical poured from the side of her mouth onto the floor."
    "She shook slightly, her body overcome by pleasure as I leaned down to pick her up and rest her on the bed, nuzzling and soothing her."
    DIVINE "Urghh..."
    "After a few moments of anxious worry that I had pushed her too far, the murmured, exhausted words escaped her lips:"
    DIVINE "{i}Incredible...{/i} {image=[ICON.HEART]}"
    return