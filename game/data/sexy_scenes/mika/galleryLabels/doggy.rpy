label gallery_mika_doggy:
    "What was she wearing?"
    menu:
        "Down to her lingerie." if len(GalFlagsWithSubstring("mika", "doggy", "ling")) > 0:
            $ tmpvar["clothes"] = "ling"
        "Completely naked." if len(GalFlagsWithSubstring("mika", "doggy", "naked")) > 0:
            $ tmpvar["clothes"] = "naked"

    "Was she pregnant at the time?"
    menu:
        "Not pregnant." if len(GalFlagsWithSubstring("mika", "doggy", "nopreg" + "_" + tmpvar["clothes"])) > 0:
            $ tmpvar["pregstate"] = "nopreg"
        "Pregnant." if len(GalFlagsWithSubstring("mika", "doggy", "preg" + "_" + tmpvar["clothes"])) > 0:
            $ tmpvar["pregstate"] = "preg"

    "Was it vaginal or anal?"
    menu:
        "Vaginal." if len(GalFlagsWithSubstring("mika", "doggy", tmpvar["pregstate"] + "_" + tmpvar["clothes"] + "_" + "vag")) > 0:
            $ tmpvar["kind"] = "vag"
        "Anal." if len(GalFlagsWithSubstring("mika", "doggy", tmpvar["pregstate"] + "_" + tmpvar["clothes"] + "_" + "anal")) > 0:
            $ tmpvar["kind"] = "anal"

    if tmpvar["kind"] == "vag":
        jump gallery_mika_doggy_vag
    elif tmpvar["kind"] == "anal":
        jump gallery_mika_doggy_anal

label gallery_mika_doggy_vag:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "Not wanting to explain this to Sister Divine or someone else walking in on us, I moved behind Mika's enticing blue ass and stripped as much of my armour as I could."
    if tmpvar["pregstate"] == "preg":
        # preg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_preg_ling_idle with dissolve
        # preg naked
        else:
            scene mika_doggy_preg_naked_idle with dissolve
    else:
        # nopreg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_nopreg_ling_idle with dissolve
        # nopreg naked
        else:
            scene mika_doggy_nopreg_naked_idle with dissolve
    $ Pause()
    "Mika cooed happily as my hands gently slid off the red panties down to her ankles; I couldn't tell what was the more impressive view..."
    "Novaras so high up illuminated at night, or the bubbly, tight, blue ass inviting and currently rubbing up against my hard cock."
    "Mika's breathing increased as she felt the large cock rub up against her ass; enticingly, she wiggled her butt against me whilst she continued to look ahead over the city."
    MIKA "S-Such a lovely view, isn't it?"
    MC "Oh yes..."
    MC "{i}I think I have the best view in the city right now.{/i}"
    "Mika giggled, but as she did so, I gently aligned my cock against her wet opening."
    "She froze up slightly, letting out a little gasp as she felt the head penetrate and enter into her wet, tight womanhood."
    "Mika's hands coiled and squeezed over the edge of the stone ledge as I slowly began to push my member in and out of her."
    "She squeezed me effortlessly as she began to slowly push her round, blue butt back against me."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    if tmpvar["pregstate"] == "preg":
        # preg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_preg_ling_vag_slow with dissolve
        # preg naked
        else:
            scene mika_doggy_preg_naked_vag_slow with dissolve
    else:
        # nopreg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_nopreg_ling_vag_slow with dissolve
        # nopreg naked
        else:
            scene mika_doggy_nopreg_naked_vag_slow with dissolve
    $ Pause()
    MIKA "M-Mmmfghh!"
    MIKA "Y-You're so - Ahh!"
    MIKA "B-Big!"
    "As Mika's flesh collided with mine, hot groans escaped her lips as I continued to glance left and right, making sure no one was walking in on our little dalliance."
    MC "Ahh! M-Mika!"
    MIKA "Mfghhh...!"
    MIKA "M-More! Please! I need - Ah!"
    MIKA "{i}M-More!{/i}"
    "Her hot breath filled the night air as the two of us quickly became hot."
    MC "{i}*Huff*{/i} Mika... Ahh...!"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    if tmpvar["pregstate"] == "preg":
        # preg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_preg_ling_vag_fast with dissolve
        # preg naked
        else:
            scene mika_doggy_preg_naked_vag_fast with dissolve
    else:
        # nopreg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_nopreg_ling_vag_fast with dissolve
        # nopreg naked
        else:
            scene mika_doggy_nopreg_naked_vag_fast with dissolve
    $ Pause()
    "I grunted, and further incensed by her actions, I began to move faster, slamming my cock in and out of her tight, wet hole."
    "Mika's hot moans grew louder, despite her desperate attempts to muffle them, as did the loud sounds of slapping up against her jiggling, soft ass."
    MIKA "M-MMFGHHH!!"
    MIKA "Y-Yes! M-More!"
    MIKA "D-Don't stop! Please! Mhhfhh!"
    "Her hot, sultry cries filled the air and echoed lightly through the halls."
    "I wondered for a moment if someone down in the city below might hear her lewd, passionate pleas, but as the sweat poured from the two of us, I cared not if they did."
    MIKA "G-Grab my hair! Make me yours!"
    MIKA "{i}I want the whole world to know I'm yours!{/i}"
    "Her words set something off deep inside of me, and doing as she asked, I grabbed and pulled on Mika's pigtails as I continued to have my way with her."
    "She let out a shocked gasp and guttural moan as I slammed into her like an animal."
    "Her body belonged to me."
    "Her ass belonged to me and everything with it."
    MIKA "{i}F-Fuck me! Don't stop - Mmfghhh! Fucking me!{/i}"
    MIKA "AHHHHH! It feels so - Mmfghhh! G-Good!"
    MC "{i}*Grunts*{/i} Mika!"
    MC "K-Keep pushing your ass back into me! H-Hrghh! I'm ...Ahh!"
    "Mika did as she was instructed, pushing back her ass as fast and hard as she could, desperately trying to take every inch of my cock as deeply and quickly as possible."
    MIKA "M-My butt belongs to you! M-Mfghhh!"
    MIKA "M-My ass is all yours!"
    MIKA "P-Please...{i}*Huff*{/i}"
    MIKA "F-Fill me up!"
    MIKA "{i}Please, please, please!{/i}"
    "Spurred on by her words, our hot, passionate fuck was finally reaching its end."
    "Mika's breathing grew heavier as the sweat poured from the two of us."
    "My cock, grew more and more sensitive with each passing moment, each hard thrust, as my balls tightened and swelled."
    MIKA "F-Finish in me!"
    MIKA "I'm so close! Please!"
    "Mika's body tightened instinctively around me, her heart was racing, and I could {i}feel{/i} how close she was."
    "Unable to hold back any longer, I finally slammed my cock deeply into her, burying it to the hilt as I let out a guttural cry of her name."
    MC "H-HRGHHHHH...!"
    MC "M-MIKAAAA!" 
    MIKA "{i}*Whimpers*{/i}"

    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")

    if tmpvar["pregstate"] == "preg":
        # preg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_preg_ling_vag_fast with flash
            scene mika_doggy_preg_ling_vag_fast with flash
            scene mika_doggy_preg_ling_vag_finish with flash
        # preg naked
        else:
            scene mika_doggy_preg_naked_vag_fast with flash
            scene mika_doggy_preg_naked_vag_fast with flash
            scene mika_doggy_preg_naked_vag_finish with flash
    else:
        # nopreg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_nopreg_ling_vag_fast with flash
            scene mika_doggy_nopreg_ling_vag_fast with flash
            scene mika_doggy_nopreg_ling_vag_finish with flash
        # nopreg naked
        else:
            scene mika_doggy_nopreg_naked_vag_fast with flash
            scene mika_doggy_nopreg_naked_vag_fast with flash
            scene mika_doggy_nopreg_naked_vag_finish with flash

    $ Pause()

    "As she felt the rush of hot, potent seed flood into her womb, Mika's mouth hung open as she tightened and squeezed around me in a powerful orgasm."
    "She shuddered, letting out a whimpering moan as she seemed to be choking up with pleasure."
    "Finally, fully spent inside of her, the tension slowly eased up as the two of us began to relax, trying to catch our breaths."
    MIKA "That was... {i}Unbelieveable...{/i}"
    return

label gallery_mika_doggy_anal:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    "Not wanting to explain this to Sister Divine or someone else walking in on us, I moved behind Mika's enticing blue ass and stripped as much of my armour as I could." #Sex scene 
    if tmpvar["pregstate"] == "preg":
        # preg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_preg_ling_idle with dissolve
        # preg naked
        else:
            scene mika_doggy_preg_naked_idle with dissolve
    else:
        # nopreg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_nopreg_ling_idle with dissolve
        # nopreg naked
        else:
            scene mika_doggy_nopreg_naked_idle with dissolve
    $ Pause()
    "Mika cooed happily as my hands gently slid off the red panties down to her ankles; I couldn't tell what was the more impressive view..."
    "Novaras so high up illuminated at night, or the bubbly, tight, blue ass inviting and currently rubbing up against my hard cock."
    "Mika's breathing increased as she felt the large cock rub up against her ass; enticingly, she wiggled her butt against me whilst she continued to look ahead over the city."
    MIKA "S-Such a lovely view, isn't it?"
    MC "Oh yes..."
    MC "{i}I think I have the best view in the city right now.{/i}"
    "Mika giggled nervously, but then, as she felt the head of my cock push against her tight, dark blue rosebud, she froze and let out a little gasp."
    MIKA "{i}Y-You're really going t-to...{/i}"
    MIKA "{i}Put it in there?{/i}"
    "Mika froze up slightly as she felt the head of my cock push and prod against her hole."
    MC "{i}Yes.{/i}"
    "Mika gulped."
    MIKA "I-If... If my b-butt is what you really want."
    MIKA "T-Then alright!"
    MIKA "...S-Start slow though."
    MIKA "{i}... P-Please?{/i}"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)

    if tmpvar["pregstate"] == "preg":
        # preg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_preg_ling_anal_slow with dissolve
        # preg naked
        else:
            scene mika_doggy_preg_naked_anal_slow with dissolve
    else:
        # nopreg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_nopreg_ling_anal_slow with dissolve
        # nopreg naked
        else:
            scene mika_doggy_nopreg_naked_anal_slow with dissolve
    $ Pause()

    "With one push against her tight hole, it gave way and opened to me, spreading and wrapping around the head of my cock."
    "Mika whimpered as she felt her ass stretch over the member, wincing slightly in pain as she felt the huge, thick member slowly push into her ass."
    MIKA "G-Gods!"
    MIKA "You'll t-tear my ass apart!"
    "Mika's hands coiled and squeezed over the edge of the stone ledge as I slowly began to push my member in and out of her."
    "She squeezed me effortlessly as she began to slowly push her round, blue butt back against me."

    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    if tmpvar["pregstate"] == "preg":
        # preg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_preg_ling_anal_slow with dissolve
        # preg naked
        else:
            scene mika_doggy_preg_naked_anal_slow with dissolve
    else:
        # nopreg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_nopreg_ling_anal_slow with dissolve
        # nopreg naked
        else:
            scene mika_doggy_nopreg_naked_anal_slow with dissolve
    $ Pause()

    MIKA "M-Mmmfghh!"
    MIKA "Y-You're so - Ahh!"
    MIKA "B-Big!"
    MC "Your ass feels - {i}*Grunts*{/i} Amazing, Mika."
    MIKA "P-Please! Mhmm!"
    MIKA "Y-You're stretching me so much back there! Ahh!"
    MIKA "You're making me feel so... {i}So strange.{/i} ❤️"
    "As Mika's flesh collided with mine, hot groans escaped her lips as I continued to glance left and right, making sure no one was walking in on our little dalliance."
    "Mika began to push her ass back towards me, grunting and moaning hotly as she took my cock deeper and faster into her ass."
    MC "Ahh! M-Mika!"
    MIKA "Mfghhh...!"
    MIKA "T-That's it!"
    MIKA "Hrghhh! F-Fuck it!"
    MIKA "{i}Fuck my ass!{/i}"
    MIKA "I-It's starting to f-feel so good! Mhhhfhh!"
    MIKA "M-My butt! It feels good s-stuffed!"
    "Her hot breath filled the night air as the two of us quickly became hot, beads of sweat pouring down from the two of us."
    MC "{i}*Huff*{/i} Mika... Ahh...!"

    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    if tmpvar["pregstate"] == "preg":
        # preg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_preg_ling_anal_fast with dissolve
        # preg naked
        else:
            scene mika_doggy_preg_naked_anal_fast with dissolve
    else:
        # nopreg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_nopreg_ling_anal_fast with dissolve
        # nopreg naked
        else:
            scene mika_doggy_nopreg_naked_anal_fast with dissolve
    $ Pause()

    "I grunted, and further incensed by her actions, I began to move faster, slamming my cock in and out of her tight, now stretched, ass."
    "Mika's hot moans grew louder, despite her desperate attempts to muffle them, as did the loud sounds of slapping up against her jiggling, soft ass."
    MIKA "M-MMFGHHH!!"
    MIKA "Y-Yes! M-More!"
    MIKA "D-Don't stop! Please! Mhhfhh!"
    "Her hot, sultry cries filled the air and echoed lightly through the halls."
    "I wondered for a moment if someone down in the city below might hear her lewd, passionate pleas, but as the sweat poured from the two of us, I cared not if they did."
    MIKA "G-Grab my hair! Make me yours!"
    MIKA "{i}I want the whole world to know I'm yours!{/i}"
    "Her words set something off deep inside of me, and doing as she asked, I grabbed and pulled on Mika's pigtails as I continued to have my way with her."
    "She let out a shocked gasp and guttural moan as I slammed into her like an animal."
    "Her body belonged to me."
    "Her ass belonged to me and everything with it."
    MIKA "{i}F-Fuck me! Don't stop - Mmfghhh! Fucking me!{/i}"
    MIKA "AHHHHH! It feels so - Mmfghhh! G-Good!"
    MC "{i}*Grunts*{/i} Mika!"
    MC "K-Keep pushing your ass back into me! H-Hrghh! I'm ...Ahh!"
    "Mika did as she was instructed, pushing back her ass as fast and hard as she could, desperately trying to take every inch of my cock as deeply and quickly as possible."
    MIKA "M-My butt belongs to you! M-Mfghhh!"
    MIKA "M-My ass is all yours!"
    MIKA "I - I'm a little anal whore for you tonight! Mhhhfhh!"
    MIKA "P-Please...{i}*Huff*{/i}"
    MIKA "F-Fill me up!"
    MIKA "{i}Please, please, please!{/i}"
    "Spurred on by her words, our hot, passionate fuck was finally reaching its end."
    "Mika's breathing grew heavier as the sweat poured from the two of us."
    "My cock, grew more and more sensitive with each passing moment, each hard thrust, as my balls tightened and swelled."
    MIKA "F-Finish in me!"
    MIKA "I'm so close! Please!"
    MIKA "Flood my ass! I want to be unable to walk straight for a week! ❤️"
    "Mika's body tightened instinctively around me, her heart was racing, and I could {i}feel{/i} how close she was."
    "Unable to hold back any longer, I finally slammed my cock deeply into her, burying it to the hilt as I let out a guttural cry of her name."
    MC "H-HRGHHHHH...!"
    MC "M-MIKAAAA!" 
    MIKA "{i}*Whimpers*{/i}"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")

    if tmpvar["pregstate"] == "preg":
        # preg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_preg_ling_anal_fast with flash
            scene mika_doggy_preg_ling_anal_fast with flash
            scene mika_doggy_preg_ling_anal_finish with flash
        # preg naked
        else:
            scene mika_doggy_preg_naked_anal_fast with flash
            scene mika_doggy_preg_naked_anal_fast with flash
            scene mika_doggy_preg_naked_anal_finish with flash
    else:
        # nopreg ling
        if tmpvar["clothes"] == "ling":
            scene mika_doggy_nopreg_ling_anal_fast with flash
            scene mika_doggy_nopreg_ling_anal_fast with flash
            scene mika_doggy_nopreg_ling_anal_finish with flash
        # nopreg naked
        else:
            scene mika_doggy_nopreg_naked_anal_fast with flash
            scene mika_doggy_nopreg_naked_anal_fast with flash
            scene mika_doggy_nopreg_naked_anal_finish with flash
    $ Pause()

    "As she felt the rush of hot, potent seed flood into her ass, Mika's mouth hung open as she tightened and squeezed around me in a powerful orgasm."
    "She shuddered, letting out a whimpering moan as she seemed to be choking up with pleasure."
    "Finally, fully spent inside of her, the tension slowly eased up as the two of us began to relax, trying to catch our breaths."
    MIKA "That was... {i}Unbelieveable...{/i}"
    MIKA "Oh gods..."
    MIKA "My poor little ass is going to be aching for days after that pounding!"
    "I smirked playfully."
    MC "Do you think the other girls might notice you {i}wobbling{/i} when you walk?"
    MIKA "M-Maybe..."
    "Mika smiled back teasingly."
    MIKA "P-Probably be jealous it's me and not them."
    return