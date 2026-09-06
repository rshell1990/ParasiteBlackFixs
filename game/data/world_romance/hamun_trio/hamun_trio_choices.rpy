label rom_tarbeck_hamun_trio_choices:
    $ NoteLock("tarbeck_rom_romance_scheduledtrio")
    $ RomanceLadyTarbeck().Romance_ScheduledTrio = False
    show lady_narisha at cright
    show lady_bargore at right
    show lady_belamore at center
    with dissolve
    show mc at cleft with easeinleft
    LADY_NARISHA @smile "MY KNIGHT!"
    LADY_NARISHA @smile "I knew you would come again!"
    LADY_BARGORE @think "Gods, girl, settle down."
    LADY_BARGORE @smile "He's here to fuck our brains out, not carry you off in his arms."
    "A cautious Lady Belamore inched forward, more reserved than the other two, but as she played with her hair, she waited expectantly."
    LADY_BELAMORE @talk "... Well, what did you have in mind tonight?"
    menu:
        "The three of you in bed... Now.":
            LADY_NARISHA @smile "H-How ROMANTIC!"
            LADY_BARGORE @talk "Gods, you're a fucking idiot sometimes, Narisha."
            LADY_BELAMORE @talk "... Fine."
            LADY_BELAMORE @smile "{i}... Make it fun.{/i}"
            scene black with dissolve
            $ PlaySound("audio/cfx/transform.ogg")
            $ SetRepeatVariant(True)
            $ Pause(0.5)
            jump rom_hamun_trio_foursome
        "The table...":
            LADY_NARISHA @smile "Oooh! That was so fun last time!"
            LADY_BARGORE @smile "Well, I can't argue with that."
            LADY_BELAMORE @talk "Degrading, more like."
            LADY_NARISHA @talk "You're just jealous because he doesn't look at you when he does you."
            LADY_BELAMORE @shock "I... I AM NOT!"
            LADY_BARGORE @smile "Stop arguing, ladies, and do what we came here for..."
            LADY_BARGORE @lewd "... Get some {i}cock.{/i}"
            LADY_BELAMORE @sad "{i}*Sigh*{/i}"
            scene black with dissolve
            $ SetRepeatVariant(True)
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            jump rom_hamun_trio_table_vag
        "The table... But I'm putting it in your asses.":
            LADY_NARISHA @shock "O-Our butts?!"
            LADY_NARISHA @embar "... W-Well, i-if it makes you feel closer to me, my knight..."
            LADY_BARGORE @think "Do you really need to coat everything in romance?"
            LADY_BARGORE @smile "Can't a man just want to fuck some whores in the ass for the fun of it?"
            LADY_NARISHA @embar "But..."
            LADY_BELAMORE @angry "You're getting off on this little power trip, aren't you?"
            MC @smile "Yes, and you know what the best part is?"
            MC @smile "You'll be begging me for more next week as well."
            "Lady Belamore paused, her cheeks flushed red."
            LADY_BELAMORE @emb "... F-Fine."
            LADY_BELAMORE @angry "Gods, I hate how much you make me cum!"
            LADY_NARISHA @smile "Yayyy! To the table we go!"
            LADY_BARGORE @smile "This will be fun..."
            scene black with dissolve
            $ SetRepeatVariant(True)
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            jump rom_hamun_trio_table_anal