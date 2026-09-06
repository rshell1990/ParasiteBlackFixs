label qst_TheTarbecks_Room_Mirrors_main:
    if "mirrors" in QstTheTarbecks().PlayedInRooms:
        if config.developer:
            "DEBUG: already been to this room. override the block and go again?"
            menu:
                "yes":
                    pass
                "no":
                    jump qst_TheTarbecks_AlreadyPlayedInThisRoom
        else:
            jump qst_TheTarbecks_AlreadyPlayedInThisRoom

    "Etched into the door was a single phrase."
    "{i}True love is a sight for all to see.{/i}"
    show mc at cleft with easeinleft
    MC "(What does that mean?)"
    scene black with dissolve
    $ LocSet("hamun_tarbeck_room_mirrors")
    $ LocFlush(dissolve)
    "Inside the chamber were several beds, surrounded by hanging glass mirrors."
    "Masked watchers stood along the walls, carefully observing."
    "Couples writhed in pleasure atop the beds."
    "I watched as a woman let out a heated moan while her lover's seed splashed across her ass."
    "The watchers applauded."
    "The naked, sweat-soaked couple shakily left the bed and were handed a single golden token."
    show mc at cleft with easeinleft
    MC @surprised "Uh..."
    MC @surprised "I guess they want us to put on a show?"

    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_4

    if QstTheTarbecks().PartyCompanion == "ves":
        jump qst_TheTarbecks_Room_Mirrors_ves
    elif QstTheTarbecks().PartyCompanion == "markus":
        jump qst_TheTarbecks_Room_Mirrors_markus
    elif QstTheTarbecks().PartyCompanion == "kiara":
        jump qst_TheTarbecks_Room_Mirrors_kiara
    elif QstTheTarbecks().PartyCompanion == "esme":
        jump qst_TheTarbecks_Room_Mirrors_esme

label qst_TheTarbecks_Room_Mirrors_ves:
    show ves at left with easeinleft
    VES @blush "N-No! I am not doing such a thing!"
    VES @blush "I don't want my first time to be..."
    VES @blush "{i}Watched{/i} by everyone."
    MC @surprised "Your... {i}first time?{/i}"
    VES @blush "L-Let's try another room!"
    VES @blush "I can't do this!"
    show ves at blurin, left_f
    hide ves with easeoutleft
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    $ LocEnter()

label qst_TheTarbecks_Room_Mirrors_markus:
    show markus_fem at left with easeinleft
    MARKUS_FEM @talk "[player_name!t]..."
    MARKUS_FEM @happy "Y-You can't seriously expect me to—"
    show mc at blurin, cleft_f
    MC "..."
    MARKUS_FEM @angry "No, don't give me that look!"
    MARKUS_FEM @angry "Damn it, man!"
    MARKUS_FEM @angry "Let's find a different room. We're not doing this."
    show markus_fem at blurin, left_f
    hide markus_fem with easeoutleft
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    $ LocEnter()

label qst_TheTarbecks_Room_Mirrors_kiara:
    show kiara at left with easeinleft
    KIARA @smile "Ooooh!"
    KIARA @smile "Now this looks like fun to me!"
    "Kiara nudged me playfully, eyes glinting as she looked around the mirrored chamber."
    KIARA @blush "How about it then?"
    KIARA @blush "Why don't we show these rich bastards what it really means to fuck?"
    menu:
        "Let's give them a show.":
            pass
        "Not now.":
            KIARA @angry "Tsch..."
            KIARA @angry "Well, that's bloody boring."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    KIARA @smile "Now we're talking!"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
    scene kiara_tarbeck_mirrors_idle_2 with dissolve
    $ Pause()
    "Grinning, Kiara grabbed my hand and shoved me down onto one of the beds, straddling me as she tugged and tore at my clothes."
    MC "Ahh! Easy now—eas—"
    "Her panties were flung aside as she settled herself over me, hands sliding down my chest while she teased the head of my cock against her slick slit."
    KIARA "Sorry, love..."
    KIARA "Mmmm... this place has me all worked up."
    "With a soft gasp she lowered herself onto me, heat enveloping me as her tight cunt squeezed down and she moaned."
    KIARA "M-Mmfghhh!"
    MC "Ahh—Kiara!"
    MC "Gods, you're tight!"
    $ PlaySexFx2("audio/sex_sounds/bed_creaking_1.ogg", 1)
    scene kiara_tarbeck_mirrors_1 with dissolve
    $ Pause()
    "She laughed breathlessly and began to ride me, her freckled ass bouncing as the mirrors reflected writhing bodies all around us."
    "Two men fucking a greedy woman to my right while a group of four devoured each other to my left, the glass fogging as moans filled the room."
    KIARA "Don't—{i}*huff*{/i}"
    KIARA "Don't focus on them too much, love..."
    KIARA "Not when you've got my tight cunt wrapped around you."
    $ PlaySexFx2("audio/sex_sounds/bed_creaking_3.ogg", 1)
    scene kiara_tarbeck_mirrors_2 with dissolve
    $ Pause()
    "She picked up the pace, pushing me deeper as her ass slapped down harder."
    KIARA "Ooooh—f-fuck!"
    MC "Ahh!"
    KIARA "Do you think—ahhh!"
    KIARA "Mistress will let us—"
    MC "Stop talking about Sypha and keep riding my cock!"
    KIARA "Y-Yes...!"
    KIARA "Mmmfghh! This feels so good!"
    "Her eyes rolled back as her movements grew frantic," 
    KIARA "C-Cum in me!"
    KIARA "Fill me up good! Please!"
    MC "Kiara - {i}*Huff*{/i} I-"
    "Perhaps it was her enthusiasm, or the intoxication of the air smelling thick with sweat and sex..."
    "I found myself abruptly unable to hold on any longer, flooding her tight pussy with my eager, hot seed."
    $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
    $ StopSexFx2()
    scene kiara_tarbeck_mirrors_finish_1 with flash
    $ Pause()
    MC "GRGHHHHHH!"
    KIARA "Ooooh! That's it! Mhmm!"
    KIARA "Gimme every drop you got."
    MC "Gods, Kiara."
    MC "You ride like a woman possessed!"
    KIARA "Haha!"
    KIARA "... We're not done yet love!"
    MC "Huh?"
    scene kiara_tarbeck_mirrors_idle_1 with dissolve
    $ Pause()
    "Turning around on the bed, Kiara presented her ass to me, glancing back over her shoulder with her mouth parted."
    KIARA "Different angle, love..."
    KIARA "Come on, I bet it'll feel incredible like this!"
    MC "Still hungry for more?"
    KIARA "Bloody right I am!"
    KIARA "Can never tired of you and that big cock!"
    $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
    $ PlaySexFx2("audio/sex_sounds/bed_creaking_1.ogg", 1)
    scene kiara_tarbeck_mirrors_3 with dissolve
    $ Pause()
    "She guided my cock back into her and slid down onto it again, her freckled ass filling my view as she began to ride me from above."
    "Masked watchers rolled mirrors closer, blocking out the surrounding orgy and replacing it with endless reflections of Kiara's body from every angle."
    KIARA "Mmmfghhh!"
    KIARA "It feels different when it hits from this angle!"
    $ PlaySexFx2("audio/sex_sounds/bed_creaking_3.ogg", 1)
    scene kiara_tarbeck_mirrors_4 with dissolve
    $ Pause()
    "{i}*Phap! Phap! Phap!*{/i}"
    "Her ass slammed back against me as the sounds of flesh filled the chamber, the world narrowing to heat, motion, and glass."
    "It all felt surreal, like a dream folding in on itself."
    KIARA "O-Ooooh!"
    KIARA "Mmmfghh!"
    KIARA "I'm getting close!"
    "She rode harder, faster, her moans growing louder as need took over."
    MC "K-Kiara!"
    MC "I'm clo—"
    KIARA "{i}Cum in me! Cum in me!{/i}"
    "She slammed herself down to the hilt, grinding her ass back as release tore through me."
    $ StopSexFx2()
    $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
    scene kiara_tarbeck_mirrors_finish_2 with flash
    $ UnlockGalSceneAndGrantXp("kiara", "tarbeck_mirrors")
    $ ReduceInfectionFromSex("kiara")
    $ Pause()
    MC "H-HRGHHHH!"
    KIARA "{i}G-Gods!{/i}"
    "She shuddered, riding it out before slowly lifting herself off me, breathless and flushed."
    $ AutoMus(True)
    scene black with dissolve
    $ Pause(0.5)
    $ LocFlush()
    show kiara at cright_f
    show mc at cleft
    with dissolve
    KIARA "Fuck... {i}*huff*{/i}"
    KIARA "Bloody hells..."
    KIARA "You're going to have me walking bow-legged."
    "She laughed, satisfied, climbing to her feet and stretching."
    KIARA @smile "Phew! Now {i}that{/i} was fun."
    KIARA @smile "Come on, lover."
    KIARA @smile "There are plenty more games to play."
    "One of the watchers, seeing we were finished, approached and handed us a gold token."
    show cg_tarbeck_watcher at left with easeinleft
    $ PlayerAddItem("qst_tarbeck_golden_token")
    show cg_tarbeck_watcher at nod
    WATCHER "Your performance was... exceptional."
    WATCHER "We hope to see you again in the remaining games."
    hide cg_tarbeck_watcher with easeoutright
    show kiara at center_f with ease
    KIARA @smile "That's one more token down!"
    KIARA @smile "Let's see what else that old fart has planned!"
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Mirrors_over

label qst_TheTarbecks_Room_Mirrors_esme:
    show esme at left with easeinleft
    ESME @smile "For such a legendary pervert, I'm almost disappointed."
    ESME @smile "So—ready to show these amateurs how to properly fuck, {i}dear?{/i}"
    menu:
        "Let's do it.":
            pass
        "Soon.":
            ESME @sad "Urghh... boring."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    ESME @smile "Perrrrfect."
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "Esme wasted no time, crawling onto the bed and pushing her huge ass toward me."
    "She wiggled her hips, her tail swishing hypnotically."
    ESME "Like what you see?"
    MC "Who wouldn't?"
    "With a smug grin—one fang visible—Esme began to clap her cheeks together."
    ESME "...Like my trick?"
    MC "...You little—"
    "Esme laughed as I grabbed her ass, pressing my cock against the tight entrance of her pussy."
    $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
    $ PlaySexFx2("audio/sex_sounds/bed_creaking_1.ogg", 1)
    scene esme_tarbeck_mirrors_1 with dissolve
    $ Pause()
    "Her laughter turned into a sharp gasp, then a soft, purring moan as I slid inside her."
    ESME "Mmmmmfhhh..."
    ESME "Just couldn't wait, huh?"
    MC "Does any man wait long when you wave your ass in his face like that?"
    ESME "No, but..."
    ESME "They rarely have a cock like yours, either."
    $ PlaySexFx2("audio/sex_sounds/bed_creaking_2.ogg", 1)
    scene esme_tarbeck_mirrors_2 with dissolve
    $ Pause()
    "She gasped again as I began to thrust faster into her, her thick cheeks folding around my cock."
    "Her tight pussy squeezed eagerly as she purred and moaned."
    ESME "Mmmfghhh! That's it!"
    ESME "Slam that—hrfghh!—big thing into me!"
    MC "F-Fuck! How is it so—"
    ESME "Pull my tail!"
    MC "Wait—"
    ESME "P-Pull my tail and call me a good kitty!"
    MC "...What?"
    ESME "Ahh! Just do it!"
    $ PlaySexFx2("audio/sex_sounds/bed_creaking_1.ogg", 1)
    scene esme_tarbeck_mirrors_3 with dissolve
    $ Pause()
    "I yanked her tail."
    "Esme's mouth fell open in delight as she slammed her ass back against me."
    MC "Who's a good little kitty?"
    $ PlaySexFx2("audio/sex_sounds/bed_creaking_2.ogg", 1)
    scene esme_tarbeck_mirrors_4 with dissolve
    $ Pause()
    ESME "M-Mmfghh! ❤️"
    "With every tug, her cunt tightened around me."
    ESME "I am!"
    ESME "I'M A GOOD KITTY!"
    "I almost laughed—but as she ground back against me, the heat and intensity drowned out everything else."
    MC "F-Fuckkk!"
    ESME "Fufufu... ❤️"
    ESME "How are you—{i}*huff*{/i}—doing back there?"
    MC "Hrghh! D-Doing just f-fine!"
    ESME "Hahaha!"
    ESME "Is that why I can feel your cock throbbing already?"
    ESME "Mmmm...!"
    ESME "Sounds like you're barely holding on!"
    "I tugged her tail again, drawing another involuntary moan from her."
    "Her tight cunt pulsed around me with every pull."
    ESME "E-EHHHHMM! ❤️"
    MC "Want me to stop?"
    ESME "N-Nooooo...!"
    ESME "Esme will be a good kitty!"
    ESME "Mmmfghh!"
    ESME "J-Just keep slamming that—{i}*huff*{/i}—"
    ESME "HUGE cock into me until those massive balls fill me up!"
    "As my balls slapped against her, I felt them tighten and ache."
    "Sweat glistened on Esme's back and ass as she pushed and wiggled herself onto me."
    "She muttered filthy encouragements to herself, only growing more aroused."
    MC "{i}*Huff*{/i} You little—"
    MC "{i}Mmfghh!{/i}"
    MC "I-I'm close!"
    ESME "Ooooooh!"
    ESME "Don't stop!"
    ESME "Slap those balls against me and don't stop till you cum!"
    "Surrounded by mirrors reflecting every obscene angle, the moans and cries of the room pushed it all past the edge."
    $ StopSexFx2()
    $ PlaySexFx("audio/sex_sounds/nijah_doggy_finish.ogg")
    scene esme_tarbeck_mirrors_finish with flash
    $ ReduceInfectionFromSex("esme")
    $ UnlockGalSceneAndGrantXp("esme", "tarbeck_mirrors")
    $ Pause()
    "I pulled hard on her tail, burying myself to the hilt as release tore through me."
    MC "G-GRGHHHHH!"
    ESME "{i}*GASP!*{/i}"
    ESME "O-OOOOOH!"
    ESME "S-So much cum!"
    "Slowly, Esme pulled herself off me."
    scene black with dissolve
    "With a soft {i}*pop!*{/i}, I slid free, watching my seed spill from her tight cunt as she purred."
    $ AutoMus(True)
    $ LocFlush()
    show esme at cleft
    show mc at cright_f
    with dissolve
    ESME "Purrrrr..."
    ESME "You really know how to show a lady a good time!"
    #"Once we had finished up, one of the scantily dressed servers approached and handed us a gold token."
    show cg_tarbeck_watcher at right_f with easeinright
    WATCHER "Your performance was... exceptional."
    show cg_tarbeck_watcher at nod
    $ PlayerAddItem("qst_tarbeck_golden_token")
    WATCHER "We hope to see you both in the rest of the games."
    show cg_tarbeck_watcher at blurin, right
    hide cg_tarbeck_watcher with easeoutright
    ESME @smile "Mmm... child's play."
    show esme at center with ease
    ESME @smile "Come on, let's see what other {i}games{/i} there are to enjoy!"
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Mirrors_over

label qst_TheTarbecks_Room_Mirrors_over:
    $ QstTheTarbecks().CalcGoldTokens()
    $ QstTheTarbecks().PlayedInRooms.add("mirrors")
    $ LocEnter()