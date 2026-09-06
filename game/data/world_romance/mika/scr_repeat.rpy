label mika_rom_kiss_repeat:
    MIKA @shock "O-Oh...!"
    MIKA @blush "W-Well, you don't need to ask twice... d-dear." 
    hide mika
    show cg_mc_mika_kiss:
        center
        xzoom -1.0
        yoffset 60
        xoffset 80 
    with dissolve
    "Mika nervously moved into my arms, pressing her lips against mine as I reached around to squeeze and fondle her soft butt." #Kiss - Mika
    "As she moaned softly, despite her usual nervousness, she quickly got into it, slipping her hot tongue into my mouth and entwining it with mine."
    "With hot, trembling breath, she nervously pulled back after a few moments."
    hide cg_mc_mika_kiss
    show mika at center 
    with dissolve
    MIKA @blush "T-That was..."
    MIKA @blush "{i}Mmmmm...{/i}"
    return

label mika_rom_bj_repeat:
    hide mika
    show cg_mc_mika_kiss:
        center
        xzoom -1.0
        yoffset 60
        xoffset 80 
    with dissolve
    "Mika stepped towards me, pressing her lips against mine."
    "After a tender, passionate kiss, she pulled back to look into my eyes."
    hide cg_mc_mika_kiss
    show mika:
        center
    with dissolve
    MIKA @blush "Do you want me to... undress f-for you?"
    menu:
        "Stay dressed.":
            MIKA @blush "As you wish, [player_name!t]..."
        "Undress down to your lingerie..":
            MIKA @blush "As you wish, [player_name!t]..."
            $ CharSetClothes("mika", "ling1")
            $ PlaySoundRandom("tentFlap")
            show mika at blurin, nod
        "Undress completely.":
            MIKA @blush "As you wish, [player_name!t]..."
            $ CharSetClothes("mika", "naked")
            $ PlaySoundRandom("tentFlap")
            show mika at blurin, nod

    MIKA @blush "Now..."
    MIKA @blush "Relax."
    scene black with dissolve
    "With a sharp shove, Mika pushed me down back onto the edge of a bed as she dropped to her knees and began to unbuckle my clothes." #Mika on knees
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    if CharIsVisiblyPreg("mika"):
        if CharGetClothes("mika") == "dress":
            scene mika_bj_preg_dress_idle with dissolve
        elif CharGetClothes("mika") == "naked":
            scene mika_bj_preg_naked_idle with dissolve
        elif CharGetClothes("mika") == "ling1":
            scene mika_bj_preg_ling_idle with dissolve
    else:
        if CharGetClothes("mika") == "dress":
            scene mika_bj_nopreg_dress_idle with dissolve
        elif CharGetClothes("mika") == "naked":
            scene mika_bj_nopreg_naked_idle with dissolve
        elif CharGetClothes("mika") == "ling1":
            scene mika_bj_nopreg_ling_idle with dissolve
    $ Pause()
    MIKA "I- I've been thinking about this b-big cock since last time."
    "Mika's cheeks flushed a light red."
    MIKA "Y-You like it when I talk like that, r-right?"
    MIKA "I've b-been practicing talking like t-that for you."
    "Something was arousing about Mika, in all her innocence, practicing phrases and words to sound more like a whore to please me."
    "But of course, it was far more fun seeing those kinds of things tumble from her mouth when she wasn't even aware of what she was saying."
    if CharIsVisiblyPreg("mika"):
        if CharGetClothes("mika") == "dress":
            scene mika_bj_preg_dress_face with dissolve
        elif CharGetClothes("mika") == "naked":
            scene mika_bj_preg_naked_face with dissolve
        elif CharGetClothes("mika") == "ling1":
            scene mika_bj_preg_ling_face with dissolve
    else:
        if CharGetClothes("mika") == "dress":
            scene mika_bj_nopreg_dress_face with dissolve
        elif CharGetClothes("mika") == "naked":
            scene mika_bj_nopreg_naked_face with dissolve
        elif CharGetClothes("mika") == "ling1":
            scene mika_bj_nopreg_ling_face with dissolve
    $ Pause()
    "With my cock flopped out onto her face, Mika, flushed with nervous excitement, gently licked at the shaft." #Cock resting on Mika's face
    MIKA "It's so - {i}*Huff*{/i} heavy!"
    MIKA "And..."
    MIKA "{i}M-Musky.{/i}"
    "Mika began to breathe excitedly at the hard cock resting on her face."
    "I groaned happily as I felt her tongue continue to prod and glide up and down."
    MIKA "{i}B-Big.{/i}"
    MIKA "You're so big...'"
    "Mika dragged her tongue towards the tip, wrapping her lips around the head of my cock finally." #BJ
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    if CharIsVisiblyPreg("mika"):
        if CharGetClothes("mika") == "dress":
            scene mika_bj_preg_dress_suck with dissolve
        elif CharGetClothes("mika") == "naked":
            scene mika_bj_preg_naked_suck with dissolve
        elif CharGetClothes("mika") == "ling1":
            scene mika_bj_preg_ling_suck with dissolve
    else:
        if CharGetClothes("mika") == "dress":
            scene mika_bj_nopreg_dress_suck with dissolve
        elif CharGetClothes("mika") == "naked":
            scene mika_bj_nopreg_naked_suck with dissolve
        elif CharGetClothes("mika") == "ling1":
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
    MIKA "(What is it about his cock?)"
    MIKA "(I f-feel like I just lose my mind whenever I'm around him now!)"
    MC "Ahh... K-Keep doing that."
    "I reached around to grab the back of Mika's head, gently pulling her head forward."
    MIKA "Mhhfh! {i}*Slurp!*{/i}"
    "Mika's mouth widened and stretched to take another inch, her watering eyes looking up towards me as she continued to try and force my cock deeper into her throat."
    "Occasionally, small choking sounds would escape her lips as she dipped her head slightly too far down."
    MIKA "{i}*Glughh!*{/i} Mhhfhh!"
    "As Mika found herself in a more steady rhythm, her eyes, dazed and full with a mixture of love and lust, met mine as she pressed her tongue against the bottom of my cock and continued to throw her head forward."
    MIKA "Mhfhhh! D-Dhhadhyy! ❤️"
    MC "{i}*Huff*{/i} Mika... That's... Mhmmff!"
    "As Mika continued this steady pattern of back, forth, back, forth with her head and gliding, silk-wet lips, the intense sensation continued to build inside me."
    "The seal around her mouth tightened as she began to feel my member swell and throb in her mouth."
    MIKA "{i}H-He's close! He's so close! I can feel it!{/i}"
    "My hands tightened their grip around Mika's soft hair; the throbbing, building sensation was now painful, desperate for release."
    MC "M-Mika!"
    MC "I'm going to-"
    "Mika, sensing I was on the edge, threw her head forward and held it there in place, choking as deeply as she could on my cock as she thrashed and beat her tongue around my cock."
    "The sudden, sharp sensation was too much, too hot, and grunting loudly, I began to pour my hot load into Mika's warm mouth."
    MC "H-Hrghhhh!!"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    if CharIsVisiblyPreg("mika"):
        if CharGetClothes("mika") == "dress":
            scene mika_bj_preg_dress_suck with flash
            scene mika_bj_preg_dress_suck with flash
        elif CharGetClothes("mika") == "naked":
            scene mika_bj_preg_naked_suck with flash
            scene mika_bj_preg_naked_suck with flash
        elif CharGetClothes("mika") == "ling1":
            scene mika_bj_preg_ling_suck with flash
            scene mika_bj_preg_ling_suck with flash
    else:
        if CharGetClothes("mika") == "dress":
            scene mika_bj_nopreg_dress_suck with flash
            scene mika_bj_nopreg_dress_suck with flash
        elif CharGetClothes("mika") == "naked":
            scene mika_bj_nopreg_naked_suck with flash
            scene mika_bj_nopreg_naked_suck with flash
        elif CharGetClothes("mika") == "ling1":
            scene mika_bj_nopreg_ling_suck with flash
            scene mika_bj_nopreg_ling_suck with flash

    if CharIsVisiblyPreg("mika"):
        if CharGetClothes("mika") == "dress":
            scene mika_bj_preg_dress_finish_in with flash
            scene mika_bj_preg_dress_finish_in with flash
        elif CharGetClothes("mika") == "naked":
            scene mika_bj_preg_naked_finish_in with flash
            scene mika_bj_preg_naked_finish_in with flash
        elif CharGetClothes("mika") == "ling1":
            scene mika_bj_preg_ling_finish_in with flash
            scene mika_bj_preg_ling_finish_in with flash
    else:
        if CharGetClothes("mika") == "dress":
            scene mika_bj_nopreg_dress_finish_in with flash
            scene mika_bj_nopreg_dress_finish_in with flash
        elif CharGetClothes("mika") == "naked":
            scene mika_bj_nopreg_naked_finish_in with flash
            scene mika_bj_nopreg_naked_finish_in with flash
        elif CharGetClothes("mika") == "ling1":
            scene mika_bj_nopreg_ling_finish_in with flash
            scene mika_bj_nopreg_ling_finish_in with flash
    

    $ ReduceInfectionFromSex("mika")
    
    if CharIsVisiblyPreg("mika"):
        if CharGetClothes("mika") == "dress":
            $ UnlockGalFlag("mika", "mika_bj_suck", "var_preg_dress")
        elif CharGetClothes("mika") == "naked":
            $ UnlockGalFlag("mika", "mika_bj_suck", "var_preg_naked")
        elif CharGetClothes("mika") == "ling1":
            $ UnlockGalFlag("mika", "mika_bj_suck", "var_preg_ling1")
    else:
        if CharGetClothes("mika") == "dress":
            $ UnlockGalFlag("mika", "mika_bj_suck", "var_nopreg_dress")
        elif CharGetClothes("mika") == "naked":
            $ UnlockGalFlag("mika", "mika_bj_suck", "var_nopreg_naked")
        elif CharGetClothes("mika") == "ling1":
            $ UnlockGalFlag("mika", "mika_bj_suck", "var_nopreg_ling1")

    $ UnlockGalSceneAndGrantXp("mika", "mika_bj_suck")
    $ Pause()
    MIKA "Mmfghh...!?"
    "As Mika swallowed down the hot load pouring into her body, her sultry eyes looked up to me, loving feeding her my seed, and slowly, once the last drop of my load was spent, she slowly dragged her lips back."
    "With a loud *PLOP,* her lips pulled away from the head of my cock, and with a gentle kiss on the head, she looked up and smiled towards me."
    if CharIsVisiblyPreg("mika"):
        if CharGetClothes("mika") == "dress":
            scene mika_bj_preg_dress_finish_out with flash
            scene mika_bj_preg_dress_finish_out with flash
        elif CharGetClothes("mika") == "naked":
            scene mika_bj_preg_naked_finish_out with flash
            scene mika_bj_preg_naked_finish_out with flash
        elif CharGetClothes("mika") == "ling1":
            scene mika_bj_preg_ling_finish_out with flash
            scene mika_bj_preg_ling_finish_out with flash
    else:
        if CharGetClothes("mika") == "dress":
            scene mika_bj_nopreg_dress_finish_out with flash
            scene mika_bj_nopreg_dress_finish_out with flash
        elif CharGetClothes("mika") == "naked":
            scene mika_bj_nopreg_naked_finish_out with flash
            scene mika_bj_nopreg_naked_finish_out with flash
        elif CharGetClothes("mika") == "ling1":
            scene mika_bj_nopreg_ling_finish_out with flash
            scene mika_bj_nopreg_ling_finish_out with flash
    $ Pause()
    MIKA "W-Was that good?"
    "Mika rose back to her feet, wiping her wet lips with her sleeve as she smiled sheepishly towards me." #BJ scene end 
    $ AutoMus(True)
    $ LocFlush()
    show mika at center
    with dissolve
    MIKA @blush "I - I'm glad all my practice with you is paying off!"
    MIKA @blush "I promise! S-Soon, you'll be as crazy thinking about doing it with me as I am with you!"
    MC @smile "I already am, Mika."
    $ CharSetClothes("mika", "dress")
    $ PlaySoundRandom("tentFlap")
    show mika at blurin, nod
    "Mika beamed with pride as she grabbed at her clothes and began to re-dress herself."
    return

label mika_rom_missionary_repeat:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "Mika awkwardly averted her gaze for a moment."
    MIKA "Y-You can put it... {i}in the other one.{/i}"
    MIKA "I-If you want..."
    "My cock rose upon hearing her sweet words, and gently, stripping her of her clothes, I laid the naked and shy Mika down onto her bed."
    scene black with dissolve
    $ PlaySoundRandom("tentFlap")
    menu:
        "Put it in Mika's pussy":
            "While the thought was tempting, I'd already made up my mind as to what I wanted."
            MIKA "... Please, make love to me again."
            "She waited nervously as I placed myself on top of her, her legs spread as she shyly tried to avoid making eye contact with me."
            MIKA "B-Be gentle, please."

            $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
            if CharIsVisiblyPreg("mika"):
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
            if CharIsVisiblyPreg("mika"):
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

            if CharIsVisiblyPreg("mika"):
                scene mika_missionary_preg_vag_fast with flash
                scene mika_missionary_preg_vag_fast with flash
                scene mika_missionary_preg_vag_finish with flash
                $ UnlockGalFlag("mika", "mika_missionary", "preg_vag")
            else:
                scene mika_missionary_nopreg_vag_fast with flash
                scene mika_missionary_nopreg_vag_fast with flash
                scene mika_missionary_nopreg_vag_finish with flash
                $ UnlockGalFlag("mika", "mika_missionary", "nopreg_vag")

            $ UnlockGalSceneAndGrantXp("mika", "mika_missionary")
            $ ReduceInfectionFromSex("mika")
            $ PregRoll("mika")
            $ Pause()

            "Mika's eyes rolled back as she felt the rush of hot seed fill her up."
            "Her mouth hung agape as she choked on air, another orgasm causing her to tremble as only a single, guttural moan escaped her lips."
            MIKA "Mmmfgghghhhhh!! ❤️"
            "I laid on top of her for a moment, the two of us catching our breath for a moment as I felt my cock slowly begin to soften."
            "Gently, Mika kissed me, pressing her lips against mine before I pulled back and rose to my feet."
            $ CharSetClothes("mika", "naked")
            $ LocFlush(fade)
            $ AutoMus(True)
            show mika at center with dissolve
            MIKA @blush "By Palam's grace... It gets better every time with you."
            "Mika smiled as she dropped back onto her bed, sighing with happy relief."
            "Grabbing my clothes, I got ready to leave."
            "Mika playfully slapped at my butt, giggling."
            MIKA "C- Come see me again soon!"
            MIKA "P-Please?"
            MIKA "I miss you already!"
            hide mika with dissolve
            $ CharSetClothes("mika", "dress")

        "Put it in Mika's ass.": 
            "Too tempting an offer to pass, I gently aligned my cock against her dark, blue, tight back hole."
            "Mika's hands tightened and squeezed at the quilts as she felt the head of my cock prod against her forbidden hole."
            "Mika bit down on her lower lip, gently wiggling her butt for me as though she was nervously trying to encourage me to push it in."

            $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
            if CharIsVisiblyPreg("mika"):
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
            if CharIsVisiblyPreg("mika"):
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

            if CharIsVisiblyPreg("mika"):
                scene mika_missionary_preg_anal_fast with flash
                scene mika_missionary_preg_anal_fast with flash
                scene mika_missionary_preg_anal_finish with flash
                $ UnlockGalFlag("mika", "mika_missionary", "preg_anal")
            else:
                scene mika_missionary_nopreg_anal_fast with flash
                scene mika_missionary_nopreg_anal_fast with flash
                scene mika_missionary_nopreg_anal_finish with flash
                $ UnlockGalFlag("mika", "mika_missionary", "nopreg_anal")

            $ UnlockGalSceneAndGrantXp("mika", "mika_missionary")
            $ ReduceInfectionFromSex("mika")
            $ Pause()

            "Mika's eyes rolled back as she felt the rush of hot seed fill her bowels."
            "Her mouth hung agape as she choked on air, another orgasm causing her to tremble as only a single, guttural moan escaped her lips."
            MIKA "Mmmfgghghhhhh!! ❤️"
            "I laid on top of her for a moment, the two of us catching our breath for a moment as I felt my cock slowly begin to soften in her ass."
            "Gently, Mika kissed me, pressing her lips against mine before I pulled back and rose to my feet."

            $ CharSetClothes("mika", "naked")
            $ LocFlush(fade)
            $ AutoMus(True)
            show mika at center with dissolve
            MIKA @blush "By the gods... {i}I'm not going to be able to sit down properly for weeks after that!{/i}"
            MC @smile "Regretting offering up your ass to me now, huh?"
            "Mika smirked playfully."
            MIKA @blush "{i}I ... I didn't say that... {/i}"
            "Mika smiled as she dropped back onto her bed, sighing with happy relief."
            "Grabbing my clothes, I got ready to leave."
            "Mika playfully slapped at my butt, giggling."
            MIKA "C- Come see me again soon!"
            MIKA "P-Please?"
            MIKA "I miss you already!"
            hide mika with dissolve
            $ CharSetClothes("mika", "dress")

    return

label mika_rom_hallway_repeat:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    MC @smile "You cold stood there like that?"
    "Mika coyly stepped closer towards me, running her hands down onto my chest."
    MIKA @blush "{i}N-Not now you're here to warm me up.{/i}"
    "Mika blushed as she smiled. Her hands ran off my chest, and she gently took my hand."
    MIKA @blush "C-Come on..."
    MIKA @blush "T-The others are busy. Come on, we won't have much time!"
    scene black with dissolve
    "Pulling me out into the hallways once more, Mika giggled as I looked left and right for anyone who might see us." #Cut to the hallway 
    $ LocSet("novaras_palam_e_wing")
    $ LocFlush()
    show mika at center 
    with dissolve
    MC @smile "You {i}really{/i} like it when someone could walk in on us, don't you?"
    MIKA @blush "D-Do you really wanna waste time talking at a time like this?"
    MIKA @blush "H-Hurry up and take your clothes off."
    MIKA @blush "{i}I'm so turned on right now...{/i}"
    "As I began to strip, Mika's eyes greedily looked over the muscles of my body."
    MIKA @blush "... H-How about you put it in my butt this time?"
    "The words caught me off-guard, smirking; I looked up towards Mika, who pouted cutely, averting her eyes."
    MIKA @think "I-If you want to... Of course."
    menu:
        "Put it in her pussy.":
            "As she twisted the heel of her foot slightly and gently swayed her hips with her hands behind her back, I moved closer towards her."
            MC "How much time do you think we have?"
            MIKA "N-Not long enough."
            MIKA "S-So you better make the most of me."
            "Without saying another word, Mika turned towards the ledge overlooking the city, gently bending forward over it as she wiggled her butt towards me."
            MIKA "C-Come on."
            MIKA "We better hurry!"
            scene black with dissolve
            "Not wanting to explain this to Sister Divine or someone else walking in on us, I moved behind Mika's enticing blue ass and stripped as much of my armour as I could." #Sex scene 
            if CharIsVisiblyPreg("mika"):
                # preg ling
                if CharGetClothes("mika") == "ling2":
                    scene mika_doggy_preg_ling_idle with dissolve
                # preg naked
                else:
                    scene mika_doggy_preg_naked_idle with dissolve
            else:
                # nopreg ling
                if CharGetClothes("mika") == "ling2":
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
            if CharIsVisiblyPreg("mika"):
                # preg ling
                if CharGetClothes("mika") == "ling2":
                    scene mika_doggy_preg_ling_vag_slow with dissolve
                # preg naked
                else:
                    scene mika_doggy_preg_naked_vag_slow with dissolve
            else:
                # nopreg ling
                if CharGetClothes("mika") == "ling2":
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
            if CharIsVisiblyPreg("mika"):
                # preg ling
                if CharGetClothes("mika") == "ling2":
                    scene mika_doggy_preg_ling_vag_fast with dissolve
                # preg naked
                else:
                    scene mika_doggy_preg_naked_vag_fast with dissolve
            else:
                # nopreg ling
                if CharGetClothes("mika") == "ling2":
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

            if CharIsVisiblyPreg("mika"):
                # preg ling
                if CharGetClothes("mika") == "ling2":
                    scene mika_doggy_preg_ling_vag_fast with flash
                    scene mika_doggy_preg_ling_vag_fast with flash
                    scene mika_doggy_preg_ling_vag_finish with flash
                    $ UnlockGalFlag("mika", "doggy", "preg_ling_vag")
                # preg naked
                else:
                    scene mika_doggy_preg_naked_vag_fast with flash
                    scene mika_doggy_preg_naked_vag_fast with flash
                    scene mika_doggy_preg_naked_vag_finish with flash
                    $ UnlockGalFlag("mika", "doggy", "preg_naked_vag")
            else:
                # nopreg ling
                if CharGetClothes("mika") == "ling2":
                    scene mika_doggy_nopreg_ling_vag_fast with flash
                    scene mika_doggy_nopreg_ling_vag_fast with flash
                    scene mika_doggy_nopreg_ling_vag_finish with flash
                    $ UnlockGalFlag("mika", "doggy", "nopreg_ling_vag")
                # nopreg naked
                else:
                    scene mika_doggy_nopreg_naked_vag_fast with flash
                    scene mika_doggy_nopreg_naked_vag_fast with flash
                    scene mika_doggy_nopreg_naked_vag_finish with flash
                    $ UnlockGalFlag("mika", "doggy", "nopreg_naked_vag")

            $ ReduceInfectionFromSex("mika")
            $ PregRoll("mika")
            $ UnlockGalSceneAndGrantXp("mika", "doggy")
            $ Pause()

            "As she felt the rush of hot, potent seed flood into her womb, Mika's mouth hung open as she tightened and squeezed around me in a powerful orgasm."
            "She shuddered, letting out a whimpering moan as she seemed to be choking up with pleasure."
            "Finally, fully spent inside of her, the tension slowly eased up as the two of us began to relax, trying to catch our breaths."
            MIKA "That was... {i}Unbelieveable...{/i}"
            scene black with dissolve
            "From down the narrow stretch of hallway, I could hear footsteps slowly approaching, and Mika, having heard it too, frantically pulled herself away from me."
            "Grabbing my hand, she quickly pulled me behind one of the doors."
            "Out of the line of sight, peering around the corner, I watched Sister Divine enter the hallway before making a swift turn."
            "Whether she heard us or not, I wasn't sure, but the thought of nearly being caught sent my heart racing... As did it, Mika's."
            MIKA @scared "Is she gone?"
            MC "Yes."
            "With a sigh of relief, Mika stepped back out."
            $ LocFlush()
            show mika at center
            with dissolve
            MIKA @smile "By Palam's grace... I have no idea what I would do if I was actually caught! Haha!"
            MC @smile "Was it everything you were hoping for?"
            "Mika bit down on her lower lip gently."
            MIKA @lewd "Mmm... I'm not sure."
            MIKA @lewd "{i}We better find new risky places to do it just to be sure.{/i}"
            MC @smile "Is that so?"
            MIKA @blush "I - I should probably get some sleep."
            MIKA @blush "M-Maybe visit me sometime?"
            MC @smile "Of course, Mika."
            "Mika smiled warmly, her eyes filled with...{i}love.{/i}"
            "Or perhaps just adoration, I wasn't quite sure."
            MIKA @blush "I- I'll be waiting..."
            "Nervously, Mika took a few steps back before heading back to her quarters in a hurry."
            $ LocFlush(dissolve)
            MC @smile "(Mika...)"
            MC @smile "(You've come a long way.)"
            $ CharSetClothes("mika", "dress")
            $ AutoMus(True)

        "Put it in her ass.":
            "As she twisted the heel of her foot slightly and gently swayed her hips with her hands behind her back, I moved closer towards her."
            MC "How much time do you think we have?"
            MIKA "N-Not long enough."
            MIKA "S-So you better make the most of me."
            "Without saying another word, Mika turned towards the ledge overlooking the city, gently bending forward over it as she wiggled her butt towards me."
            MIKA "C-Come on."
            MIKA "We better hurry!"
            scene black with dissolve
            "Not wanting to explain this to Sister Divine or someone else walking in on us, I moved behind Mika's enticing blue ass and stripped as much of my armour as I could." #Sex scene 
            if CharIsVisiblyPreg("mika"):
                # preg ling
                if CharGetClothes("mika") == "ling2":
                    scene mika_doggy_preg_ling_idle with dissolve
                # preg naked
                else:
                    scene mika_doggy_preg_naked_idle with dissolve
            else:
                # nopreg ling
                if CharGetClothes("mika") == "ling2":
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
            if CharIsVisiblyPreg("mika"):
                # preg ling
                if CharGetClothes("mika") == "ling2":
                    scene mika_doggy_preg_ling_anal_slow with dissolve
                # preg naked
                else:
                    scene mika_doggy_preg_naked_anal_slow with dissolve
            else:
                # nopreg ling
                if CharGetClothes("mika") == "ling2":
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
            if CharIsVisiblyPreg("mika"):
                # preg ling
                if CharGetClothes("mika") == "ling2":
                    scene mika_doggy_preg_ling_anal_slow with dissolve
                # preg naked
                else:
                    scene mika_doggy_preg_naked_anal_slow with dissolve
            else:
                # nopreg ling
                if CharGetClothes("mika") == "ling2":
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
            if CharIsVisiblyPreg("mika"):
                # preg ling
                if CharGetClothes("mika") == "ling2":
                    scene mika_doggy_preg_ling_anal_fast with dissolve
                # preg naked
                else:
                    scene mika_doggy_preg_naked_anal_fast with dissolve
            else:
                # nopreg ling
                if CharGetClothes("mika") == "ling2":
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

            if CharIsVisiblyPreg("mika"):
                # preg ling
                if CharGetClothes("mika") == "ling2":
                    scene mika_doggy_preg_ling_anal_fast with flash
                    scene mika_doggy_preg_ling_anal_fast with flash
                    scene mika_doggy_preg_ling_anal_finish with flash
                    $ UnlockGalFlag("mika", "doggy", "preg_ling_anal")
                # preg naked
                else:
                    scene mika_doggy_preg_naked_anal_fast with flash
                    scene mika_doggy_preg_naked_anal_fast with flash
                    scene mika_doggy_preg_naked_anal_finish with flash
                    $ UnlockGalFlag("mika", "doggy", "preg_naked_anal")
            else:
                # nopreg ling
                if CharGetClothes("mika") == "ling2":
                    scene mika_doggy_nopreg_ling_anal_fast with flash
                    scene mika_doggy_nopreg_ling_anal_fast with flash
                    scene mika_doggy_nopreg_ling_anal_finish with flash
                    $ UnlockGalFlag("mika", "doggy", "nopreg_ling_anal")
                # nopreg naked
                else:
                    scene mika_doggy_nopreg_naked_anal_fast with flash
                    scene mika_doggy_nopreg_naked_anal_fast with flash
                    scene mika_doggy_nopreg_naked_anal_finish with flash
                    $ UnlockGalFlag("mika", "doggy", "nopreg_naked_anal")

            $ ReduceInfectionFromSex("mika")
            $ UnlockGalSceneAndGrantXp("mika", "doggy")
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
            scene black with dissolve
            "From down the narrow stretch of hallway, I could hear footsteps slowly approaching, and Mika, having heard it too, frantically pulled herself away from me."
            "Grabbing my hand, she quickly pulled me behind one of the doors."
            "Out of the line of sight, peering around the corner, I watched Sister Divine enter the hallway before making a swift turn."
            "Whether she heard us or not, I wasn't sure, but the thought of nearly being caught sent my heart racing... As did it, Mika's."
            MIKA @scared "Is she gone?"
            MC "Yes."
            "With a sigh of relief, Mika stepped back out."
            $ LocFlush()
            show mika at center
            with dissolve
            MIKA @smile "By Palam's grace... I have no idea what I would do if I was actually caught! Haha!"
            MC @smile "Was it everything you were hoping for?"
            "Mika bit down on her lower lip gently."
            MIKA @lewd "Mmm... I'm not sure."
            MIKA @lewd "{i}We better find new risky places to do it just to be sure.{/i}"
            MC @smile "Is that so?"
            MIKA @blush "I - I should probably get some sleep."
            MIKA @blush "M-Maybe visit me sometime?"
            MC @smile "Of course, Mika."
            "Mika smiled warmly, her eyes filled with...{i}love.{/i}"
            "Or perhaps just adoration, I wasn't quite sure."
            MIKA @blush "I- I'll be waiting..."
            "Nervously, Mika took a few steps back before heading back to her quarters in a hurry."
            MC @smile "(Mika...)"
            MC @smile "(You've come a long way.)"
            $ LocFlush(dissolve)
            MC @smile "(Mika...)"
            MC @smile "(You've come a long way.)"
            $ CharSetClothes("mika", "dress")
            $ AutoMus(True)
    return

label mika_rom_divine_bath_repeat():
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ CharSetClothes("mika", "naked")
    $ CharSetClothes("divine", "towel")
    show mika at center with dissolve
    "Mika was once again gently swimming her way up and down the length of the pool almost silently."
    $ CharSetClothes("mika", "water")
    show mika:
        center
        blurin
    "Her wet naked body glistened from the water in the moonlight as she ran her hands through her wet hair and sighed."
    "She looked around for a few moments, her face crestfallen as she swam towards the pool's edge to climb out."
    show divine at left with dissolve
    DIVINE @happy "Room for one more?"
    show mika:
        xzoom -1.0
    with dissolve
    DIVINE @happy "I didn't expect you to summon me again so soon... "
    "Mika splashed as she turned startled towards Sister Divine, smiling above her with a towel wrapped around her."
    MIKA @shock "S-Sister Divine!"
    $ CharSetClothes("divine", "naked")
    show divine:
        left
        blurin
    play sound2 "audio/cfx/cotton_drop.ogg"
    "Sister Divine laughed as she undid the towel around her, allowing it to fall to the floor."
    DIVINE @happy "Why so surprised, dear?"
    DIVINE @happy "You asked for me to come."
    "Mika's cheeks flushed red as her eyes stared at the dangling appendage between Sister Divine's legs."
    MIKA @blush "I - I did."
    MIKA @blush "I j-just wasn't sure if you'd remembered, that is all."
    play sound2 "audio/cfx/divine_mika_water_noise.ogg"
    $ CharSetClothes("divine", "water")
    show divine:
        left
        blurin
    "Sister Divine smiled knowingly as she stepped into the pool, slowly submerging half of her body."
    DIVINE "How long have you been waiting?"
    MIKA "N-Not {i}too{/i} long..."
    show mika:
        xzoom 1.0
    with dissolve
    "Sister Divine ever so tenderly wrapped her arms around Mika, whose breath escaped her in surprise."
    DIVINE "{i}Liar.{/i}"
    "Mika smiled softly, her cheeks blushing red."
    MIKA "M-Maybe a little while..."
    "Mika let out a soft gasp as Divine's hands cupped and fondled at Mika's soft breasts."
    scene mika_divine_hug with dissolve
    $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
    MIKA "M-Mfghh!"
    DIVINE "So, did you come here on your own?"
    DIVINE "Or did {i}he{/i} ask you to come here?"
    MIKA "W-What do you mean?"
    DIVINE "{i}Is he watching us right now?{/i}"
    "Sister Divine's thumbs circled over Mika's hardened nipples."
    MIKA "Ooooh! S-Sister!"
    DIVINE "Perhaps he's wondering about joining us in the warm water, hmm?"
    MIKA "{i}*Huff*{/i} I - I don't know if he's - Mhmm!"
    MIKA "W-Watching..."
    "Sister Divine smiled reassuringly once more."
    DIVINE "And does it excite you, thinking he might be?"
    "Sister Divine's hand reached down beneath the soft water, gently wrapping around Mika's cock as she stroked back and forth."
    MIKA "M-Mhfff!"
    MIKA "{i}Y-Yes... I w-want him to feel the hot blood pouring through him every time he l-looks at me!{/i}"
    DIVINE "You're so pent up, poor thing..."
    "Sister Divine generously applied soft kisses to Mika's neck, who shuddered with pleasure."
    MIKA "S-Sister, {i}*Huff*{/i}"
    MIKA "I can f-feel your ... {i}thing{/i} prodding against my butt."
    "Sister Divine giggled playfully,"
    DIVINE "Are you ready for what's next?"
    "Mika's breath trembled as she lightly nodded, and Sister Divine bent Mika over the pool's edge."
    scene divine_fucking_mika_at_bathhouse_idle with dissolve
    $ StopSexFx()
    "With Mika's round ass waving in front of Sister Divine's face, she stepped up from behind it and grabbed hold of the soft butt."
    "Mika let out another startled gasp as she felt the hard, blue cock wedged between her cheeks, lightly rubbing back and forth."
    MIKA "{i}D-Do it.{/i}"
    "Sister Divine pulled back, aligning the head of her cock against the wet slit opening, and entered into Mika."
    scene divine_fucking_mika_at_bathhouse_slow with dissolve
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    "Mika let out a hot gasp as the member slowly glided inside her womanhood inch by inch."
    MIKA "A-Ahhh...!"
    DIVINE "Hrghh! You're - Mhmm! T-Tight, Mika."
    "As Sister Divine's cock slowly glided in and out of her slowly, Mika groaned in pleasure as she offered a faint smile."
    MIKA "T-Thank you. - Mhfghh!"
    "Divine squeezed the fat flesh of Mika's ass between her fingers as she held on tightly, slowly moving faster as she thrust in and out Mika."
    DIVINE "Mhff! Are you ready for me to move faster, dear?"
    MIKA "{i}*Huff*{/i} Y-Yes ...!"
    scene divine_fucking_mika_at_bathhouse_fast with dissolve
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    "With a light slap across the butt, Mika whelped in surprise as her butt jiggled a little with the motion."
    "Wet sloshing sounds echoed slightly throughout the bathhouse as the flesh collided."
    "Mika moaned hotly as Sister Divine began to slam deeply into her from behind."
    MIKA "M-Mmfhghhh!!"
    DIVINE "Oooh! MIKA!"
    DIVINE "Y-You're squeezing me - Mhfhh! So tight!"
    MIKA "M-More! Don't s-stop!"
    MIKA "Oooh! I can't help it! I've been waiting for this for so long!"
    "The two women's breasts swung back and forth with every motion as their passionate tryst continued for some time."
    DIVINE "{i}*Huff*{/i} You s-silly girl!"
    DIVINE "You should have - Ahh! Offered me this ass sooner!"
    MIKA "Oooooooh! Yes, Miss! It's all yours! My ass is all yours tonight!"
    "Sister Divine gritted her teeth, the two locked and contorted in pleasure as Sister Divine fucked away at Mika's tight hole."
    "Eventually, the heavy, sweet grunts and moans reached their climax as Mika weakly declared,"
    MIKA "I- I'm c-close!"
    DIVINE "Ahh! M-Myself too!"
    "Divine winced, desperately seeming to try and hold on for Mika's sake."
    MIKA "I-It's okay!"
    MIKA "{i}Fill me up!{/i}"
    DIVINE "B-But-"
    MIKA "Mhhfhh! Do it, sister! DO IT!"
    $ UnlockGalSceneAndGrantXp("mika", "divine_fucking_mika_at_bathhouse")
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    show divine_fucking_mika_at_bathhouse_fast with flash
    show divine_fucking_mika_at_bathhouse_fast with flash
    scene divine_fucking_mika_at_bathhouse with flash
    "Unable to hold back any longer, Sister Divine lunged forward, wrapping her arm against Mika's neck into an almost choke hold-like position."
    "Stood upright, Sister Divine pumped against Mika's ass, pulling her lewd body back onto her member as deeply as she could."
    "Grunting loudly and thrusting as deeply as she could into Mika, she poured her hot load into Mika's womanhood."
    "Mika's tongue flopped out of her mouth as her eyes began to roll back."
    "She choked lightly beneath Sister Divine's grip, and her own, exciting, rock-hard cock splurted out a white stream as she was pumped full of Sister Divine's seed."
    "Releasing her grip, Mika dropped forward, barely catching herself on the pool's edge as the two women turned to face each other breathlessly."
    $ LocFlush()
    show mika at left
    show divine:
        center
        xzoom -1.0
    with dissolve
    DIVINE @lewd "{i}*Huff*{/i} How was that - {i}*Huff*{/i} my dear?"
    "Mika smiled, biting down at her lower lip alluringly."
    MIKA @lewd "{i}Incredible.{/i}"
    "Sister Divine laughed."
    DIVINE @happy "You drained me dry, girl."
    "Mika softly chuckled with new-found confidence."
    MIKA @lewd "Bet you are glad to see that my lazy butt is good for something, huh?"
    "The two girls smirked and shared another small laugh."
    MIKA "I, um, think I better get out of the pool and dry off for a bit."
    play sound2 "audio/cfx/divine_mika_water_noise.ogg"
    "As Mika clambered out of the pool, Sister Divine reached out one last time to spank Mika's soft ass."
    play sound2 "audio/cfx/spank.ogg"
    $ CharSetClothes("mika", "towel_water")
    show mika:
        left 
        blurin
    "Mika gasped, and then, grabbing a towel, giggled as she hurried off, her heart beating out of her chest in excitement."
    hide mika with dissolve
    DIVINE @talk "... Did you enjoy the show?"
    show mc at left with dissolve
    MC @smile "Very much."
    DIVINE @happy "You should join us some time..."
    "As she climbed out of the water, giving me an eyeful view of her naked body, Sister Divine gently ran her hand across my crotch as she passed by."
    DIVINE "{i}I'm sure the three of us could have a lot of fun...{/i}"
    MC "Tempting."
    "Sister Divine smirked as she grabbed a towel before leaving the room; looking over my shoulder, I caught a glimpse of her fat, blue ass as she left the bathhouse."
    DIVINE "Goodnight...[player_name!t]."
    $ AutoMus(True)
    $ CharSetClothes("mika", "dress")
    $ CharSetClothes("divine", "normal")
    $ QstSetProgress(RomanceMika, 1)
    $ LocEnter()