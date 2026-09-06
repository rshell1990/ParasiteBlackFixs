label gallery_mika_wet_dream:
    scene mika_wet_dream_slow with slowflash
    $ AutoMus(False)
    $ AutoAmb(False)
    stop ambience
    stop ambience2
    $ PlayMusicRandom("mus_sex")
    $ Pause()
    "Suddenly, lewd images of Mika sprawled out on a bed came surging through my mind."
    $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
    "Like watching a vision, she ran her hands up her body and smiled alluringly, leaving nothing to the imagination."
    scene mika_wet_dream_fast with dissolve
    "Overwhelmingly so, not only could I see her, I could {i}feel{/i} her desires and intent as though they were my own."
    scene mika_wet_dream_fast_nude with flash
    "In a moment, there was a second image of her, now naked on the bed as she continued to rub her body teasingly with her hands."
    MIKA "{i}I want you ... I want you so much.{/i}"
    MIKA "{i}Like I've never wanted anyone before.{/i}"
    $ StopSexFx()
    $ tmpvar = []
    if GalFlag("mika", "mika_wet_dream", "day"):
        $ tmpvar.append("day")
    if GalFlag("mika", "mika_wet_dream", "night"):
        $ tmpvar.append("night")
    $ tmpvar = renpy.random.choice(tmpvar)
    if tmpvar == "day":
        scene bg_alleyway
    else:
        scene bg_alleyway_night
    with slowflash
    "As soon as the vision began, it ended, and I stood once more in the same alleyway."
    MC "(Gods ... It felt like I was {i}there{/i} with her just now.)"
    return