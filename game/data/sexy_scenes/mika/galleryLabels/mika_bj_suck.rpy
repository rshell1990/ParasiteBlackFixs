label gallery_mika_bj_suck:
    "What was she wearing?"
    menu:
        "Wearing her dress." if len(GalFlagsWithSubstring("mika", "mika_bj_suck", "_dress")) > 0:
            $ tmpvar["clothes"] = "dress"
        "Down to her lingerie." if len(GalFlagsWithSubstring("mika", "mika_bj_suck", "_ling1")) > 0:
            $ tmpvar["clothes"] = "ling1"
        "Completely naked." if len(GalFlagsWithSubstring("mika", "mika_bj_suck", "_naked")) > 0:
            $ tmpvar["clothes"] = "naked"

    "Was she pregnant at the time?"
    menu:
        "Not pregnant." if len(GalFlagsWithSubstring("mika", "mika_bj_suck", "_nopreg_" + tmpvar["clothes"])) > 0:
            $ tmpvar["preg"] = False
        "Pregnant." if len(GalFlagsWithSubstring("mika", "mika_bj_suck", "_preg_" + tmpvar["clothes"])) > 0:
            $ tmpvar["preg"] = True

    scene black with dissolve
    "With a sharp shove, Mika pushed me down back onto the edge of a bed as she dropped to her knees and began to unbuckle my clothes." #Mika on knees
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    if tmpvar["preg"] == True:
        if tmpvar["clothes"] == "dress":
            scene mika_bj_preg_dress_idle with dissolve
        elif tmpvar["clothes"] == "naked":
            scene mika_bj_preg_naked_idle with dissolve
        elif tmpvar["clothes"] == "ling1":
            scene mika_bj_preg_ling_idle with dissolve
    elif tmpvar["preg"] == False:
        if tmpvar["clothes"] == "dress":
            scene mika_bj_nopreg_dress_idle with dissolve
        elif tmpvar["clothes"] == "naked":
            scene mika_bj_nopreg_naked_idle with dissolve
        elif tmpvar["clothes"] == "ling1":
            scene mika_bj_nopreg_ling_idle with dissolve

    $ Pause()
    MIKA "D-Don't think I'm like this with everyone!"
    MIKA "There's something so... {i}different{/i} about you."
    MIKA "It's like it drives me crazy just being near you!"
    BLACK "({i}Interesting ... Her magecraft sensitivity has allowed her to mildly detect my pheromones.{/i})"
    MC "(Is that a bad thing?)"
    BLACK "({i}No ... But against potential threats it will be worth remembering they may be able to detect it.{/i})"
    MIKA "Is something the matter?"
    MC "Oh, sorry, just uh, got lost in thought a moment there."
    MIKA "A-Ah! Don't worry! You won't be able to focus on anything else soon!"
    if tmpvar["preg"] == True:
        if tmpvar["clothes"] == "dress":
            scene mika_bj_preg_dress_face with dissolve
        elif tmpvar["clothes"] == "naked":
            scene mika_bj_preg_naked_face with dissolve
        elif tmpvar["clothes"] == "ling1":
            scene mika_bj_preg_ling_face with dissolve
    else:
        if tmpvar["clothes"] == "dress":
            scene mika_bj_nopreg_dress_face with dissolve
        elif tmpvar["clothes"] == "naked":
            scene mika_bj_nopreg_naked_face with dissolve
        elif tmpvar["clothes"] == "ling1":
            scene mika_bj_nopreg_ling_face with dissolve
    $ Pause()
    "With my cock flopped out onto her face, Mika, flushed with nervous excitement, gently licked at the shaft." #Cock resting on Mika's face
    MIKA "It's so - {i}*Huff*{/i} heavy!"
    MIKA "And..."
    "I groaned happily as I felt her tongue continue to prod and glide up and down."
    MIKA "{i}B-Big.{/i}"
    MIKA "You sure you're human and not part horse?"
    "I laughed, but as I did so, Mika dragged her tongue towards the tip, wrapping her lips around the head of my cock finally." #BJ
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    if tmpvar["preg"] == True:
        if tmpvar["clothes"] == "dress":
            scene mika_bj_preg_dress_suck with dissolve
        elif tmpvar["clothes"] == "naked":
            scene mika_bj_preg_naked_suck with dissolve
        elif tmpvar["clothes"] == "ling1":
            scene mika_bj_preg_ling_suck with dissolve
    else:
        if tmpvar["clothes"] == "dress":
            scene mika_bj_nopreg_dress_suck with dissolve
        elif tmpvar["clothes"] == "naked":
            scene mika_bj_nopreg_naked_suck with dissolve
        elif tmpvar["clothes"] == "ling1":
            scene mika_bj_nopreg_ling_suck with dissolve
    $ Pause()
    MC "Ahh!"
    MIKA "Mhmm..."
    MIKA "(This thing's gonna give my jaw one hell of a workout!)" 
    "Mika glided her head back and forth, moaning softly as she did so."
    MIKA "{i}*Slurp*{/i} Mhfhhh..."
    "It was clear she lacked experience but didn't lack enthusiasm."
    "Clumsily, she beat and wrapped her tongue around my member, groaning hotly as she did her best to please me."
    "Mika's head rocked back and forth as she did her best to swallow down inch after inch of the cock in front of her."
    MIKA "(Gods... And I thought some of the other sisters were big!)"
    MIKA "(I wonder if the others know how {i}'equipped'{/i} he is?)"
    MC "Ahh... K-Keep doing that."
    "I reached around to grab the back of Mika's head, gently pulling her head forward."
    MIKA "Mhhfh! {i}*Slurp!*{/i}"
    "Mika's mouth widened and stretched to take another inch, her watering eyes looking up towards me as she continued to try and force my cock deeper into her throat."
    "Occasionally, small choking sounds would escape her lips as she dipped her head slightly too far down."
    MIKA "{i}*Glughh!*{/i} Mhhfhh!"
    "As Mika found herself in a more steady rhythm, her eyes, dazed and full with a mixture of love and lust, met mine as she pressed her tongue against the bottom of my cock and continued to throw her head forward."
    MIKA "Mhfhhh! D-Dhhadhyy! ❤️"
    MC "{i}*Huff*{/i} Mika... That's... Mhmmff!"
    "As Mika continued this steady pattern of back, forth, back, forth with her head and gliding, silk-wet lips, the intense sensation continued to build inside of me."
    "The seal around her mouth tightened as she began to feel my member swell and throb in her mouth."
    MIKA "{i}H-He's close! He's so close! I can feel it!{/i}"
    "My hands tightened their grip around Mika's soft hair; the throbbing, building sensation was now painful, desperate for release."
    MC "M-Mika!"
    MC "I'm going to-"
    "Mika, sensing I was on the edge, threw her head forward and held it there in place, choking as deeply as she could on my cock as she thrashed and beat her tongue around my cock."
    "The sudden, sharp sensation was too much, too hot, and grunting loudly, I began to pour my hot load into Mika's warm mouth."
    MC "H-Hrghhhh!!"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    if tmpvar["preg"] == True:
        if tmpvar["clothes"] == "dress":
            scene mika_bj_preg_dress_suck with flash
            scene mika_bj_preg_dress_suck with flash
        elif tmpvar["clothes"] == "naked":
            scene mika_bj_preg_naked_suck with flash
            scene mika_bj_preg_naked_suck with flash
        elif tmpvar["clothes"] == "ling1":
            scene mika_bj_preg_ling_suck with flash
            scene mika_bj_preg_ling_suck with flash
    else:
        if tmpvar["clothes"] == "dress":
            scene mika_bj_nopreg_dress_suck with flash
            scene mika_bj_nopreg_dress_suck with flash
        elif tmpvar["clothes"] == "naked":
            scene mika_bj_nopreg_naked_suck with flash
            scene mika_bj_nopreg_naked_suck with flash
        elif tmpvar["clothes"] == "ling1":
            scene mika_bj_nopreg_ling_suck with flash
            scene mika_bj_nopreg_ling_suck with flash

    if tmpvar["preg"] == True:
        if tmpvar["clothes"] == "dress":
            scene mika_bj_preg_dress_finish_in with flash
            scene mika_bj_preg_dress_finish_in with flash
        elif tmpvar["clothes"] == "naked":
            scene mika_bj_preg_naked_finish_in with flash
            scene mika_bj_preg_naked_finish_in with flash
        elif tmpvar["clothes"] == "ling1":
            scene mika_bj_preg_ling_finish_in with flash
            scene mika_bj_preg_ling_finish_in with flash
    else:
        if tmpvar["clothes"] == "dress":
            scene mika_bj_nopreg_dress_finish_in with flash
            scene mika_bj_nopreg_dress_finish_in with flash
        elif tmpvar["clothes"] == "naked":
            scene mika_bj_nopreg_naked_finish_in with flash
            scene mika_bj_nopreg_naked_finish_in with flash
        elif tmpvar["clothes"] == "ling1":
            scene mika_bj_nopreg_ling_finish_in with flash
            scene mika_bj_nopreg_ling_finish_in with flash

    $ Pause()
    MIKA "Mmfghh...!?"
    "As Mika swallowed down the hot load pouring into her body, her sultry eyes looked up to me, loving feeding her my seed, and slowly, once the last drop of my load was spent, she slowly dragged her lips back."
    "With a loud *PLOP,* her lips pulled away from the head of my cock, and with a gentle kiss on the head, she looked up and smiled towards me."
    if tmpvar["preg"] == True:
        if tmpvar["clothes"] == "dress":
            scene mika_bj_preg_dress_finish_out with flash
            scene mika_bj_preg_dress_finish_out with flash
        elif tmpvar["clothes"] == "naked":
            scene mika_bj_preg_naked_finish_out with flash
            scene mika_bj_preg_naked_finish_out with flash
        elif tmpvar["clothes"] == "ling1":
            scene mika_bj_preg_ling_finish_out with flash
            scene mika_bj_preg_ling_finish_out with flash
    else:
        if tmpvar["clothes"] == "dress":
            scene mika_bj_nopreg_dress_finish_out with flash
            scene mika_bj_nopreg_dress_finish_out with flash
        elif tmpvar["clothes"] == "naked":
            scene mika_bj_nopreg_naked_finish_out with flash
            scene mika_bj_nopreg_naked_finish_out with flash
        elif tmpvar["clothes"] == "ling1":
            scene mika_bj_nopreg_ling_finish_out with flash
            scene mika_bj_nopreg_ling_finish_out with flash

    $ Pause()
    MIKA "W-Was that good?"
    "Mika rose back to her feet, wiping her wet lips with her sleeve as she smiled sheepishly towards me." #Sex scene end 
    scene black with dissolve
    MC @embarr "That was ..."
    MC @smile "{i}Very impressive.{/i}"
    return





