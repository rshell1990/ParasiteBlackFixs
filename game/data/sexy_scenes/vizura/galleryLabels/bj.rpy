label gallery_vizura_bj:
    scene black with dissolve
    if GalFlag("vizura", "bj", ["var_preg", "var_nopreg"]):
        "Was she pregnant at the time?"
        menu:
            "Yes":
                $ tmpvar["preg"] = True
            "No":
                $ tmpvar["preg"] = False
    elif GalFlag("vizura", "bj", "var_preg"):
        $ tmpvar["preg"] = True
    elif GalFlag("vizura", "bj", "var_nopreg"):
        $ tmpvar["preg"] = False

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "Grabbing the goblin by the hair and pulling her towards my member, she wrapped her hands around it and cooed happily."
    "With both of her small hands wrapped around stroking it, she teased,"
    VIZURA "You wanna shove this {i}big, hard, fat{/i} human cock down my throat, don't you?" 
    VIZURA "Bet you wanna see it bulging out in my throat fufu!"
    if tmpvar["preg"]:
        MC "I hesitated for a moment, looking at Vizura's round belly protruding out." #####
        VIZURA "Don't worry about the bun in the oven, fufu." #####
        VIZURA "Us goblins are sturdy! I'll stop if there's a problem." ####
        VIZURA "Go on now, weren't you about to call me your slutty little green whore or something?" ####
        "Encouraged by her words, I smiled and carried on." ####
    MC "You sure like to talk ... But I'm not seeing enough cock down your throat for all that lip flapping your doing."
    VIZURA "Mhmmm, come here!"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    if tmpvar["preg"]:
        scene ss_vizura_bj_preg_slow 
    else:
        scene ss_vizura_bj_normal_slow 
    with dissolve
    $ Pause()
    "Vizura wrapped her wet lips around my cock, forming a tight seal as her head bopped back and forth."
    VIZURA "{i}*Slurp! Slurp!*{/i} Mmfghh...!"
    "I groaned in pleasure as her wet, silk like tongue thrashed and wrapped around my cock as her mouth glided back and forth over my member."
    "Vizura giggled as she took inch after inch of my cock deeper into her throat, cooing and moaning as her tongue beat against my cock."
    if tmpvar["preg"]:
        scene ss_vizura_bj_preg_fast
    else:
        scene ss_vizura_bj_normal_fast
    with dissolve
    $ Pause()
    MC "{i}*Huff*{/i} Ahhh...! How are you taking it so deep?"
    VIZURA "Mmfghh! {i}*Slurp!*{/i}"
    VIZURA "Fufu!"
    "Vizura's eyes looked up towards me, filled with desire as she knew she had me exactly where she wanted."
    "Wet slurping sounds escaped her lips as her continued to tease out the increasingly close climax wanting to flood into her mouth."
    VIZURA "(He's so cute breathing like that, I can't wait to feel that warm load inside of me!)"
    VIZURA "(Come on now handsome, give it to me!)"
    "My grip around Vizura's hair tightened as I moved my hand back and forth faster, grunting with pleasure as no matter how deep I forced my cock into Vizura's mouth, she eagerly took it."
    MC "F-Fuck! Suck that cock you little goblin whore!"
    VIZURA "{i}*Slurp! Slurp!*{/i} Mmfghhhh!! {i}*Slurp!*{/i}"
    "I continued to let Vizura work her magic for some time, until finally, I felt the growing need to finish becoming almost unbearable..."
    VIZURA "(I can feel his cock throbbin!' He's getting close!)"
    VIZURA "(Hehe! Come on! Lemme taste that thick seed!)"
    MC "Vizura ... {i}*Huff*{/i} I'm c-close to-"
    "Vizura didn't even let me finish my sentence, the front of her tongue suddely moved to the end of my cock and swirled and pushed rapidly."
    "The sudden intense sensation finally pushed me over the edge as I pulled Vizura's head forward."
    MC "HRGHHHHHH!!" #Cum 
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    if tmpvar["preg"]:
        scene ss_vizura_bj_preg_cum
    else:
        scene ss_vizura_bj_normal_cum
    with flash
    $ Pause()
    VIZURA "Mmfghh?!"
    "Vizura's eyes widened as she felt the rushing stream of hot, thick cum pouring down into her throat."
    "Vizura's eyes half closed as her cheeks flushed red in arousal."
    "I watched as Vizura swallowed down load after load of thick cum greedily, making sure to clean my cock thoroughly with her tongue afterwards."
    "With sultry eyes, as she dragged her lips slowly off of my cock, they pulled off the head with a loud {i}*PLOP!*{/i} sound and she giggled, showing me her open mouth to show she had swallowed all of my load." #Brief fade to black 
    VIZURA "Fufu, how was that?"
    MC "{i}*Huff*{/i} Draining."
    VIZURA "That's what I like to hear handsome."
    "Vizura wiped her lips and burped."
    if tmpvar["preg"]:
        VIZURA "Well, looks like me and the littlun won't have to worry about dinner this afternoon! Hehe!"
        VIZURA "{i}Nutritious!{/i}"
    else:
        VIZURA "Well, looks like I won't have to worry about dinner this afternoon! Hehe!"
        VIZURA "When you're cleaned up and ready, I'll be outside."
    scene black with dissolve
    "Vizura wiggled her butt playfully as she left the caravan, happily humming to herself."
    "Once re-dressed, and re-composed, I too joined her and left the caravan."
    return