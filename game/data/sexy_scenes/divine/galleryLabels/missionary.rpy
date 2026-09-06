label gallery_divine_missionary:
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
    if GalFlag("divine", "missionary", "var_first_anal") or GalFlag("divine", "missionary", "var_first_vag"):
        if GalFlag("divine", "missionary", tmpvar["scene_variants"], anymatch = True):
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
        if GalFlag("divine", "missionary", [x for x in tmpvar["scene_variants"] if "naked" in x], anymatch = True) and GalFlag("divine", "missionary", [x for x in tmpvar["scene_variants"] if "ling" in x], anymatch = True):
            "Was she wearing her lingerie?"
            menu:
                "Yes":
                    $ tmpvar["ling"] = True
                "No":
                    $ tmpvar["ling"] = False
        elif GalFlag("divine", "missionary", [x for x in tmpvar["scene_variants"] if "naked" in x], anymatch = True):
            $ tmpvar["ling"] = False
        else:
            $ tmpvar["ling"] = True
        #######################
        if GalFlag("divine", "missionary", [x for x in tmpvar["scene_variants"] if "preg" in x], anymatch = True) and GalFlag("divine", "missionary", [x for x in tmpvar["scene_variants"] if "nopreg" in x], anymatch = True):
            "Was she pregnant at the time?"
            menu:
                "Yes":
                    $ tmpvar["preg"] = True
                "No":
                    $ tmpvar["preg"] = False
        elif GalFlag("divine", "missionary", [x for x in tmpvar["scene_variants"] if "preg" in x], anymatch = True):
            $ tmpvar["preg"] = True
        else:
            $ tmpvar["preg"] = False
        ########################
    jump gallery_divine_missionary_scene

label gallery_divine_missionary_scene:
    scene bg_palam_divine_quarters_night
    show divine at cright_f
    show mc_transformed_erect at cleft
    with dissolve
    DIVINE "Oh, I never took you for a romantic."
    "I let some hot air from my snout as Sister Divine giggled, sitting down on the bed as she grabbed hold of both her legs and raised them into the air."
    "She exposed both of her holes and gave me a passionate look."
    DIVINE "Very well {i}lover...{/i}"
    DIVINE "Take what you will..."
    if tmpvar["first_time"]:
        if GalFlag("divine", "missionary", "var_first_anal") and GalFlag("divine", "missionary", "var_first_vag"):
            "Which hole did I take?"
            menu:
                "Her pussy":
                    $ tmpvar["vag"] = True
                "Her ass":
                    $ tmpvar["vag"] = False
        elif GalFlag("divine", "missionary", "var_first_anal"):
            $ tmpvar["vag"] = False
        else:
            $ tmpvar["vag"] = True

    else:
        if GalFlag("divine", "missionary", [x for x in tmpvar["scene_variants"] if "vag_" in x], anymatch = True) and GalFlag("divine", "missionary", [x for x in tmpvar["scene_variants"] if "anal_" in x], anymatch = True):
            "Which hole did I take?"
            menu:
                "Her pussy":
                    $ tmpvar["vag"] = True
                "Her ass":
                    $ tmpvar["vag"] = False
        elif GalFlag("divine", "missionary", [x for x in tmpvar["scene_variants"] if "vag_" in x], anymatch = True):
            $ tmpvar["vag"] = True
        else:
            $ tmpvar["vag"] = False

    if tmpvar["vag"]:
        jump gallery_divine_missionary_vag
    else:
        jump gallery_divine_missionary_anal

label gallery_divine_missionary_vag:
    "Placing the bulbous head of my cock against Sister Divine’s already wet pussy, I gently pushed the head into her."
    "As her pussy gave way to the head and spread around it, Sister Divine moaned softly, closing her eyes as she felt my cock pushing into her."
    DIVINE "Ooooh~"
    DIVINE "That’s quite the {i}weapon{/i} you have there."
    "Sister Divine giggled, but as I forced the last few inches in abruptly, she gasped in shock, reaching forward to grab me to steady herself."
    DIVINE "W-Wait a moment!"
    DIVINE "By the gods... I need a minute to get used to it!"
    "Heeding her words, I paused for a moment or two while she caught her breath."
    DIVINE "..O-Okay..."
    DIVINE "{i}Continue.{/i}"
    "Slowly, I began to thrust in and out of Sister Divine’s eager body."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)

    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_missionary_ling_vag_preg_notent
        else:
            scene divine_missionary_ling_vag_nopreg_notent
    else:
        if tmpvar["preg"]:
            scene divine_missionary_naked_vag_preg_notent
        else:
            scene divine_missionary_naked_vag_nopreg_notent
    with dissolve

    $ Pause()
    "Hot, sultry breaths escaped her pursed lips as she felt my cock sink in and out of her velvety grip."
    "Between her hot moans, she playfully goaded me on, softly muttering:"
    if tmpvar["first_time"]:
        DIVINE "{i}Don’t stop, lover...{/i}"
        DIVINE "{i}Keep going...{/i}"
        DIVINE "Ahh! {image=[ICON.HEART]}"
        DIVINE "It’s so d-different than anything I’ve felt before!"
    else:
        DIVINE "Mmmfgh! I've missed this!"
        DIVINE "Ahh {image=[ICON.HEART]}"
        DIVINE "I can feel the power coursing through you... It’s..."
    DIVINE "I can feel the power coursing inside you... It’s..."
    DIVINE "{i}Incredible...{/i}"
    "Encouraged, I began to move faster, rutting with her like an animal as I thrusted into her tight body."
    "Responding in kind, Sister Divine moaned as I felt her tighten around me greedily."
    DIVINE "Y-Yes! So good!"
    DIVINE "D-Don’t stop! Gods please!"
    DIVINE "Fuck me harder!"
    "I continued to force my cock deep into her when I felt the dark impulses of the parasite surfacing."
    "As if a dark veil had covered my mind..."
    "I gave in, two tentacles sliding from over my shoulders, their teeth retracted as they snaked their way up past Sister Divine’s stomach, towards her breasts."
    DIVINE "W-What are you-"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)

    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_missionary_ling_vag_preg_tent
        else:
            scene divine_missionary_ling_vag_nopreg_tent
    else:
        if tmpvar["preg"]:
            scene divine_missionary_naked_vag_preg_tent
        else:
            scene divine_missionary_naked_vag_nopreg_tent
    with dissolve

    $ Pause()
    "Suddenly, the two tentacles attached to her breasts and began to suckle at them." 
    DIVINE "Ooooooh!~"
    if tmpvar["first_time"]:
        DIVINE "Ah! I didn’t know you could – Mmmhm! D-Do that!"
    else:
        DIVINE "These things?!"
    DIVINE "Ah... ~They sure are – Oooh!~"
    DIVINE "Hungry...aren’t they? Ah! {image=[ICON.HEART]}"
    DIVINE "Mmmfgh! Yes!"
    DIVINE "You’re so deep inside me... so hot... so..."
    DIVINE "A-Ahh! {image=[ICON.HEART]}"
    "Sister Divine’s body tightened around me as I continued to thrust into her, my body burning with primal desire as I breathed heavily."
    "I rolled out my tongue to lick at her hardened nipples."
    DIVINE "{i}*Giggles!*{/i} That tickles!"
    DIVINE "Ooooh! I can feel how hard you are in me..."
    DIVINE "Are you close, my beast?"
    DIVINE "Yes!... YES! I can feel you throbbing!"
    DIVINE "You’re so c-close!"
    DIVINE "Do it! Finish inside me and claim me, you beast!"
    "Unable to hold back any longer, I dragged Sister Divine towards me, forcing myself as deeply as I could into her."
    "Her eyes widened as she moaned, trembling beneath my claws as she felt the hot seed pour into her."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    play sound2 "audio/cfx/transform.ogg"

    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_missionary_ling_vag_preg_finish
        else:
            scene divine_missionary_ling_vag_nopreg_finish
    else:
        if tmpvar["preg"]:
            scene divine_missionary_naked_vag_preg_finish
        else:
            scene divine_missionary_naked_vag_nopreg_finish
    with flash
    $ Pause()
    DIVINE "Mmmfghh! {image=[ICON.HEART]}"
    DIVINE "There’s... so much of it!"
    if tmpvar["first_time"]:
        DIVINE "Just like before!"
    DIVINE "Ahh...!~"
    "Breathing heavily, I slowly unsheathed my softening member from her."
    "As I pulled out, Sister Divine shuddered slightly, loads of hot seed flowing out of her onto the bed quilts."
    DIVINE "O-Oooh~"
    DIVINE "That was..."
    "Sister Divine licked her lips."
    DIVINE "{i}Wonderful.{/i} {image=[ICON.HEART]}"
    return

label gallery_divine_missionary_anal:
    "Staring at her tight, button like asshole, I gently prodded my cock against her backdoor, and Sister Divine laughed a little before remarking playfully."
    DIVINE "Oh my...!"
    DIVINE "Well...You better start gentle if you’re going to take me like that~"
    "I pushed in, {b}hard.{/b}"
    "Sister Divine’s asshole stretched to accommodate the dripping head of my cock."
    "She winced in pain, closing her eyes as she gritted her teeth while I forced myself deeper into her ass."
    DIVINE "G-Grghh!"
    DIVINE "E-Easy! Ah!"
    "I tilted my head quizzically for a few moments, watching her breathing outward as she tried to relax."
    DIVINE "Ahhh... It’s a good thing your {i}weapon{/i} is self-lubricating, isn’t it?"
    "I waited for a few moments to let Sister Divine get comfortable, before she finally said,"
    DIVINE "Slowly... Go slowly."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)

    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_missionary_ling_anal_preg_notent
        else:
            scene divine_missionary_ling_anal_nopreg_notent
    else:
        if tmpvar["preg"]:
            scene divine_missionary_naked_anal_preg_notent
        else:
            scene divine_missionary_naked_anal_nopreg_notent
    with dissolve

    $ Pause()
    "I began to inch my cock deeper into her tight ass."
    "Sister Divine moved between winces of pain and soft moans..."
    "Finally, with the last jolt forward, the final inch bottomed out in her ass, and Sister Divine gasped in surprise before cooing softly."
    DIVINE "Ooooh~"
    DIVINE "What is it you’re secreting?"
    DIVINE "It’s... Mmmhmm... Wonderful!"
    "After a few thrusts, Sister Divine’s sultry moans and hot breaths had let me know she was eager for me to continue pounding her tight ass."
    DIVINE "Ah! Yes! T-That’s it!"
    DIVINE "Fuck me... Fuck me harder!"
    "In that moment, I felt a primal urge..."
    "Two tentacles appeared over my shoulders, their teeth retracted as they snaked their way up past Sister Divine’s stomach towards her breasts."
    DIVINE "W-What are you-"
    "Suddenly, the two tentacles attached to her breasts and began to suckle at them."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)

    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_missionary_ling_anal_preg_tent
        else:
            scene divine_missionary_ling_anal_nopreg_tent
    else:
        if tmpvar["preg"]:
            scene divine_missionary_naked_anal_preg_tent
        else:
            scene divine_missionary_naked_anal_nopreg_tent
    with dissolve

    $ Pause()
    DIVINE "Ooooooh!~"
    if tmpvar["first_time"]:
        DIVINE "Ah! I didn’t know you could – Mmmhm! D-Do that!"
    else:
        DIVINE "These things?!"
    DIVINE "Ah... They sure are – Oooh!~"
    DIVINE "Hungry...aren’t they? Ah! {image=[ICON.HEART]}"
    DIVINE "Mmmfgh! Yes!"
    DIVINE "Oh gods! Yes! Pound that little ass!"
    DIVINE "Your cock is... is..."
    DIVINE "{i}So different!{/i}"
    DIVINE "Ahh {image=[ICON.HEART]}"
    DIVINE "I can feel the power coursing inside you... It’s..."
    DIVINE "{i}Incredible...{/i}"
    "Encouraged, I began to move faster, rutting with her like an animal, thrusting into her tight body."
    "Sister Divine moaned as I felt her asshole tighten around me greedily."
    DIVINE "Yes! So good!"
    DIVINE "My ass! You’re stretching it so much!"
    DIVINE "Are you trying to make it so that I – Ah! Can’t sit down properly for the next few weeks?"
    DIVINE "D-Don’t stop! Gods please! Fuck me harder!"
    DIVINE "P-Please, I can feel you throbbing...!"
    DIVINE "D-Do it! Finish inside me already! I want to feel you pour it into me!"
    "Thrusting in and out of Sister Divine’s ass, she grunted and moaned with every sudden thrust deep into her."
    "She let out pleading moans, urging me not to stop till I had finished inside of her."
    "As my cock began to ache, I knew I couldn’t hold on any longer, and promptly forced my cock deeply into her."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    play sound2 "audio/cfx/transform.ogg"

    if tmpvar["ling"]:
        if tmpvar["preg"]:
            scene divine_missionary_ling_anal_preg_finish
        else:
            scene divine_missionary_ling_anal_nopreg_finish
    else:
        if tmpvar["preg"]:
            scene divine_missionary_naked_anal_preg_finish
        else:
            scene divine_missionary_naked_anal_nopreg_finish
    with flash

    $ Pause()
    "I bottomed out all the way inside her and held her in place as I roared while pouring my seed into her ass."
    "Sister Divine trembled beneath my claws, her eyes wide and mouth agape as she shuddered, whimpering from the overwhelming pleasure."
    "Slowly, unsheathing my cock from her ass, I watched Sister Divine shudder when the head finally popped out, the overflowing cum poured from her stretched hole."
    DIVINE "O-Oooh...!"
    DIVINE "My butt... Mhmm!"
    DIVINE "That was..."
    "Sister Divine licked her lips."
    DIVINE "{i}Wonderful...{/i} {image=[ICON.HEART]}"
    return