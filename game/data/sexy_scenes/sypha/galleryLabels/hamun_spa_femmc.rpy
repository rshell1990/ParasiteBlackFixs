label gallery_sypha_hamun_spa_femmc:
    $ AutoMus(False)
    $ AutoAmb(False)
    play ambience "audio/ambience_loc/hamun_spa.ogg" fadein 1.0
    $ PlayMusicRandom("mus_sex")
    if GalFlag("sypha", "hamun_spa_femmc", ["flag_day", "flag_night"]):
        "Did it happen at day or at night?"
        menu:
            "Day":
                $ tmpvar = "day"
            "Night":
                $ tmpvar = "night"
    elif GalFlag("sypha", "hamun_spa_femmc", "flag_day"):
        $ tmpvar = "day"
    elif GalFlag("sypha", "hamun_spa_femmc", "flag_night"):
        $ tmpvar = "night"

    $ PlaySexFx("audio/sex_sounds/adara_hj_loop.ogg", 1)
    if tmpvar == "day":
        scene sypha_hamun_spa_femmc_day_slow
    else:
        scene sypha_hamun_spa_femmc_night_slow
    with dissolve
    $ Pause()
    "I gulp, letting Sypha continue as her hand presses itself between my legs."
    "Her soft fingers press and rub against the opening between my legs as her other hand continues to knead at one of my breasts."
    "I let out a soft sigh as she gently kisses and rubs her tongue along my neck, the strange sensations I felt were so different to being a man..."
    "Wet, my body hot and flushed from the teasing, she carefully pushed one, and thjen two, of her fingers into my hole."
    "I let out a gasp that I desperately tried to muffle."
    "By some miracle, Kiara and Markus remained obvious to what was going on as Sypha's fingers slipped deeper inside."
    SYPHA "{i}Are you enjoying your new 'experiences?'{/i}"
    MC "M-Mhmm..."
    MC "It's so strange."
    SYPHA "I'll take that as a yes then."
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x2.ogg", 1)
    if tmpvar == "day":
        scene sypha_hamun_spa_femmc_day_fast
    else:
        scene sypha_hamun_spa_femmc_night_fast
    with dissolve
    $ Pause()
    "As Sypha continued to toy with my body, I felt something inside of, a budding, overwhelming sensation."
    "As though my whole body was twisting itself up from the inside."
    MC "S-Sypha."
    MC "I think I'm gonna-"
    SYPHA "Just relax and let it happen."
    SYPHA "And remember... {i}You can indulge me next time.{/i}"
    "The hot, intense sensation suddenly came all at once, as though my whole body erupted into exstacy."
    "To stop myself from moaning too loudly, Sypha's hand reached aroud to grab my mouth as my eyes rolled to the back of my head."
    $ PlaySexFx("audio/sex_sounds/adara_hj_finish.ogg")
    if tmpvar == "day":
        scene sypha_hamun_spa_femmc_day_idle
    else:
        scene sypha_hamun_spa_femmc_night_idle
    with flash
    $ Pause()
    MC "Mmfmfghhh!! ❤️"
    "The pleasure lasted longer than it did as a man, and it was so much more intense..."
    "As the wave of pleasure slowly began to simmer down, Sypha released her grip as I caught my breath."
    MARKUS "Are you - {i}*Hiccup!*{/i} Alright?"
    MC "Y-Yes..."
    "I say flustered, Sypha grinned at me like a cat that just managed to catch a mouse, saying nothing as she reaches over to sip once more at her wine."
    "With shaky legs, I rise to my feet."
    MC "W-We should go now. Mmm..."
    MARKUS "H-Huhh? So suddenly?"
    MC "Yes, come on."
    return