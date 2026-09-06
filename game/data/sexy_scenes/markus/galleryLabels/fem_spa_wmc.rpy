label gallery_markus_fem_spa_wmc:
    $ AutoMus(False)
    $ AutoAmb(False)
    play ambience "audio/ambience_loc/hamun_spa.ogg" fadein 1.0
    $ PlayMusicRandom("mus_sex")
    if GalFlag("markus", "fem_spa_wmc", ["flag_day", "flag_night"]):
        "Did it happen at day or at night?"
        menu:
            "Day":
                $ tmpvar = "day"
            "Night":
                $ tmpvar = "night"
    elif GalFlag("markus", "fem_spa_wmc", "flag_day"):
        $ tmpvar = "day"
    elif GalFlag("markus", "fem_spa_wmc", "flag_night"):
        $ tmpvar = "night"

    "My own cheeks flushed red, what was this body doing to me?"
    "The changes in this womanly body were not just superficial."
    "Everything felt... {i}different.{/i}"
    if tmpvar == "day":
        scene markus_fem_spa_wmc_day_slow
    else:
        scene markus_fem_spa_wmc_night_slow
    with dissolve
    $ Pause()
    "A nervous Markus clambered into my lap, her heavy breasts pressing against my face as my hands reached back to cup and squeeze at her soft ass."
    "Her hot breath touched my face as she nervously tilted her head forward."
    MARKUS "R-Ready?"
    "I nodded, and her soft lips pressed against mine."
    MARKUS "M-Mmmm...❤️"
    "The two of us sank into the kiss, panic and nervousness giving way to soft pleasure as our tongues entwined."
    if tmpvar == "day":
        scene markus_fem_spa_wmc_day_fast
    else:
        scene markus_fem_spa_wmc_night_fast
    with dissolve
    $ Pause()
    MC "(W-What in the hells are we doing?!)"
    MC "(G-Gods... Why does it feel so nice?)"
    "Our hands explored each other's body, cupping and feeling each other as soft moans escapted our lips."
    "Between kisses, Markus mumbled unconvincingly,"
    MARKUS "T-This is just us - Mhmm... Fooling around, alright?"
    "I nod between kisses, and a few of the women nearby notice and giggle, but say nothing."
    scene black with dissolve
    "For the next half an hour, the two of us are too pre-occupied with each other to really pay any of the other women much attention."
    "When Markus finally managed to pull herself away from me, the two of us were now suddenly unable to look each other in the eyes."
    return