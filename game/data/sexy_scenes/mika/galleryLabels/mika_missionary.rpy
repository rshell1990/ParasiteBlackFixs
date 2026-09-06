label gallery_mika_missionary:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "Was she pregnant at the time?"
    menu:
        "Not pregnant." if len(GalFlagsWithSubstring("mika", "mika_missionary", "nopreg")) > 0:
            $ tmpvar["pregstate"] = "nopreg"
        "Pregnant." if len(GalFlagsWithSubstring("mika", "mika_missionary", "preg")) > 0:
            $ tmpvar["pregstate"] = "preg"

    "Was it vaginal or anal?"
    menu:
        "Vaginal." if len(GalFlagsWithSubstring("mika", "mika_missionary", tmpvar["pregstate"] + "_" + "vag")) > 0:
            $ tmpvar["kind"] = "vag"
        "Anal." if len(GalFlagsWithSubstring("mika", "mika_missionary", tmpvar["pregstate"] + "_" + "anal")) > 0:
            $ tmpvar["kind"] = "anal"

    scene black with dissolve

    if tmpvar["kind"] == "vag":
        jump gallery_mika_missionary_vag
    elif tmpvar["kind"] == "anal":
        jump gallery_mika_missionary_anal
    return

label gallery_mika_missionary_vag:
    MIKA "... Please, make love to me again."
    "She waited nervously as I placed myself on top of her, her legs spread as she shyly tried to avoid making eye contact with me."
    MIKA "B-Be gentle, please."

    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    if tmpvar["pregstate"] == "preg":
        scene mika_missionary_preg_vag_slow with dissolve
    else:
        scene mika_missionary_nopreg_vag_slow with dissolve
    $ Pause()

    "As I aligned my cock against her wet slit, her cock above twitched in excitement as I gently pushed the head inside of her."
    "She let out a hot gasp as her pussy tightened around me."
    MIKA "O-Oh goddess!"
    "With her hands pinned back down onto the soft bed, she did her best to wrap her legs around me to give me easier access."
    "Slowly at first, I began to glide my cock in and out of her tight hole."        
    MIKA "M-Mmfhghh!"
    MIKA "Y-Yes! Mmhmm! It f-feels..."
    "Mika bit down on her lower lip as I reached to fondle and squeeze at one of her breasts."
    MIKA "A-Ahhh!"
    MIKA "So good! ❤️"
    "Soon, our breathing became heavier as I slammed harder into Mika."
    
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    if tmpvar["pregstate"] == "preg":
        scene mika_missionary_preg_vag_fast with dissolve
    else:
        scene mika_missionary_nopreg_vag_fast with dissolve
    $ Pause()

    "Her eyes widened as her legs squeezed tighter around me."
    MC "Are you okay, Mika?"
    MIKA "Mhmm! N-No..."
    MIKA "So please..."
    MIKA "Don't stop!"
    "Her eyes watered slightly as I thrust deeper into her, her mouth hanging open in pleasure as her nails tightened and pressed into my skin."
    "A hot groan escaped her parted lips as I slammed into her."
    MIKA "Mhhh!"
    MIKA "I love you! I love you! I love you! ❤️"
    "The words came tumbling out of Mika's mouth as her eyes began to roll back; her soaking womanhood tightened and squeezed me desperately as I stretched out her hole."
    "Her hot moans became louder and louder as sweat poured from the two of us."
    "Mika's eyes are filled with a mixture of pain and love and lust as she looks up adoringly towards me."
    MIKA "P-Please..."
    MIKA "Give it to me, give me every part of you!"
    "As time ticked on, eventually, I began to feel the bubbling desire finally reaching its climax."
    MC "Urghhh... M-Mika...!"
    MIKA "M-Mmmfghh! Do it!"
    MIKA "F-Finish inside of me!"
    "Unable to hold back any longer, I slammed my cock to the hilt inside of Mika, grunting as I flooded her womb with my seed."
    MC "H-HRGHHHH...!!"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")

    if tmpvar["pregstate"] == "preg":
        scene mika_missionary_preg_vag_fast with flash
        scene mika_missionary_preg_vag_fast with flash
        scene mika_missionary_preg_vag_finish with flash
    else:
        scene mika_missionary_nopreg_vag_fast with flash
        scene mika_missionary_nopreg_vag_fast with flash
        scene mika_missionary_nopreg_vag_finish with flash

    $ Pause()

    "Mika's eyes rolled back as she felt the rush of hot seed fill her up."
    "Her mouth hung agape as she choked on air, another orgasm causing her to tremble as only a single, guttural moan escaped her lips."
    MIKA "Mmmfgghghhhhh!! ❤️"
    "I laid on top of her for a moment, the two of us catching our breath for a moment as I felt my cock slowly begin to soften."
    scene black with dissolve
    "Gently, Mika kissed me, pressing her lips against mine before I pulled back and rose to my feet."
    return

label gallery_mika_missionary_anal:
    MIKA "... Please, make love to me again."
    "I gently aligned my cock against her dark, blue, tight back hole."
    "Mika's hands tightened and squeezed at the quilts as she felt the head of my cock prod against her forbidden hole."
    "Mika bit down on her lower lip, gently wiggling her butt for me as though she was nervously trying to encourage me to push it in."

    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    if tmpvar["pregstate"] == "preg":
        scene mika_missionary_preg_anal_slow with dissolve
    else:
        scene mika_missionary_nopreg_anal_slow with dissolve
    $ Pause()

    "Pushing against the hole, eventually, Mika let out a soft gasp as her hole gave way, spreading and wrapping around the head of my cock."
    MIKA "A-Ahhh!"
    MIKA "M-My ass!"
    MIKA "Mhmm..."
    MIKA "Y-You're in m-my-"
    MIKA "{i}Ass.{/i}"
    "She almost purred the last word as I slowly, inch by inch, pushed my cock deeper into her bowels."
    MIKA "M-Mmfghhhh!! ❤️"
    "With my cock now buried inside of Mika's ass, her trembling breathing grew heavier as I slowly pushed my cock in and out of her tight hole."

    "She seemed to be struggling with my size but was determined to take it all the same."
    "Her tight ass squeezed my cock intensely, but her doe-like eyes seemed to gaze into mine with a desperate desire to know she was pleasing me."
    MC "Ahh...!"
    MC "Your ass feels so good!"
    MC "Mhmmffhh!"
    MC "Mika!"
    MIKA "F-Faster..."
    MIKA "{i}*Huff*{/i} It's okay..."
    MIKA "M-Mhmm! Y-You can go faster!"
    "I grunted in approval, quickly building speed as I began to slam my cock into her round, cute ass."

    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    if tmpvar["pregstate"] == "preg":
        scene mika_missionary_preg_anal_fast with dissolve
    else:
        scene mika_missionary_nopreg_anal_fast with dissolve
    $ Pause()
    
    MIKA "Mhhfhhh! T-That's it!"
    MIKA "F-Fuck my ass!"
    MIKA "Don't stop! Please!"
    "Her eyes watered slightly as I thrust deeper into her, her mouth hanging open in pleasure as her nails tightened and pressed into my skin."
    "A hot groan escaped her parted lips as I slammed into her now poor, abused asshole."
    MIKA "Mhhh!"
    MIKA "{i}M-My ashhhh!{/i}"
    MIKA "{i}Y-Your destroying my poor little ashhhh!{/i} ❤️"
    MIKA "Thrusting in and out of her tight hole, Mika's moans of pleasure and grunts of pain were interwoven in a sweet ecstasy."
    MC "Ahhh! MIKA!"
    MC "Your ass is so- Mhhfhhh!"
    MIKA "I-It's all yours! Mhmm!"
    MIKA "{i}My ass is all yours!{/i} ❤️"
    "As time ticked on, eventually, I began to feel the bubbling desire finally reaching its climax."
    MC "Urghhh... M-Mika...!"
    MIKA "M-Mmmfghh! Do it!"
    MIKA "F-Finish inside of me!"
    "Unable to hold back any longer, I slammed my cock to the hilt inside of Mika, grunting as I flooded her ass."
    MC "H-HRGHHHH...!!"

    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")

    if tmpvar["pregstate"] == "preg":
        scene mika_missionary_preg_anal_fast with flash
        scene mika_missionary_preg_anal_fast with flash
        scene mika_missionary_preg_anal_finish with flash        
    else:
        scene mika_missionary_nopreg_anal_fast with flash
        scene mika_missionary_nopreg_anal_fast with flash
        scene mika_missionary_nopreg_anal_finish with flash

    $ Pause()

    "Mika's eyes rolled back as she felt the rush of hot seed fill her bowels."
    "Her mouth hung agape as she choked on air, another orgasm causing her to tremble as only a single, guttural moan escaped her lips."
    MIKA "Mmmfgghghhhhh!! ❤️"
    "I laid on top of her for a moment, the two of us catching our breath for a moment as I felt my cock slowly begin to soften in her ass."
    scene black with dissolve
    "Gently, Mika kissed me, pressing her lips against mine before I pulled back and rose to my feet."
    return