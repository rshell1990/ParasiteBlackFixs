label rom_Ves_SpendNight:
    VES @talk 'Oh? Were you hoping to just keep me company?'
    VES @talk 'Or perhaps...'
    menu:
        "Just company.":
            jump rom_Ves_SpendNightCuddles
        "Let's take a bath together.":
            jump rom_Ves_TakeBathAndBjToo
        "On second thought...":
            return

label rom_Ves_SpendNightWrong:
    VES @smile_talk "You humans plan so far ahead..."
    VES @talk "Isn't it a bit early for that?"
    MC "(I should ask her later today.)"
    # company (cuddles) or sex (one of two, 69 vs bath) options
    return

label rom_Ves_SpendNightCuddles:
    VES @talk 'That sounds nice...'
    VES @talk 'I will prepare us some food.'
    #SCENE FADES TO BLACK.
    scene black with dissolve
    "We have spent the evening talking and sharing a meal."
    #SCENE CUTS TO MC AND VES IN BED CUDDLING BEFORE FADING TO THE NEXT MORNING.
    scene cg_ves_cuddling with dissolve
    $ Pause()
    VES @talk '{i}*Yawn*{/i} That was nice...'
    $ CharChangeRel("ves", 1)
    VES 'Come by again soon...'
    scene black with dissolve
    $ PlaySoundRandom("clockWind", Channel = "guisfx", Volume = 0.7)
    $ rng = 8 # reusing a var just coz I can here
    while rpTime < TIME_DAY_START or rng > 0:
        $ TimeAdvBy(TIME_1H)
        $ rng -= 1
        $ Pause(0.1)
    $ LocSet("ves_camp")
    $ HealParty()
    $ LocEnter()

label rom_Ves_TakeBathAndBjToo:
    VES @talk 'Yes... That sounds quite nice.'
    VES @talk "I'll set everything up."
    scene black with dissolve
    "After a short while..."
    play sound "audio/cfx/water_splash_bath.ogg"
    $ Pause(0.5)
    $ TimeAdvBy(TIME_05H)
    jump ves_bathRepeat
