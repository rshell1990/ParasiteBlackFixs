label gallery_marbella_gang_bj:
    scene black with dissolve
    if GalFlagCount("marbella", "gang_bj") == 0:
        $ StartReplay("replay_marbella_gang_bj_first")
        scene black with dissolve
        return
    else:
        "Was it our first time?"
        menu:
            "Yes":
                $ StartReplay("replay_marbella_gang_bj_first")
                scene black with dissolve
                return  
            "No":
                if GalFlag("marbella", "gang_bj", ["var_rep_preg", "var_rep_nopreg"]):
                    "Was she pregnant at the time?"
                    menu:
                        "Yes":
                            $ tmpvar["preg"] = True
                        "No":
                            $ tmpvar["preg"] = False
                elif GalFlag("marbella", "gang_bj", "var_rep_preg"):
                    $ tmpvar["preg"] = True
                else:
                    $ tmpvar["preg"] = False

    $ AutoMus(False)
    $ AutoAmb(False)
    stop ambience fadeout 0.5
    $ PlayMusicRandom("mus_sex")
    if tmpvar["preg"] == True:
        scene marbella_gang_bj_preg_1 with dissolve
    else:
        scene marbella_gang_bj_nopreg_1 with dissolve
    $ Pause()
    "Marbella's eyes widened as she stared at the cock hanging in front of her."
    MARBELLA "Gods... You're hung like a fuckin' horse."
    KHAZAH "What iz hold up?"
    MARBELLA "In a minute!"
    MARBELLA "A girl's just appreciating the goods, is all."
    KHAZAH "Appreciate while sucking!"
    $ PlaySexFx(audio.ves69_100, 1)
    if tmpvar["preg"] == True:
        scene marbella_gang_bj_preg_2 with dissolve
    else:
        scene marbella_gang_bj_nopreg_2 with dissolve
    $ Pause()
    "Eagerly, Marbella leaned forward, wrapping her soft lips around my cock as she stroked the Khazah's cock."
    "I groaned as her tongue worked against the head."
    MC "Ahhh... Mfghh!"
    MARBELLA "{i}*Slurp... Slurp*{/i}"
    "Her mouth inched forward, taking more as she sucked."
    MARBELLA "Mmfghh..."
    MARBELLA "Yhourhh rheallhy bhighh! {i}*Slurp!*{/i}"
    "I smirked at the comment, her mouth still working."
    KHAZAH "Over here, girl."
    KHAZAH "Before I get lonely."
    $ PlaySexFx(audio.ves69_100, 1)
    if tmpvar["preg"] == True:
        scene marbella_gang_bj_preg_3 with dissolve
    else:
        scene marbella_gang_bj_nopreg_3 with dissolve
    $ Pause()
    "Marbella pulled away with a soft *plop* before wrapping her lips around the Khazah's cock."
    "He groaned as she moved her head back and forth."
    KHAZAH "Ahhh! That's it, girl!"
    $ PlaySexFx(audio.ves69_150, 1)
    if tmpvar["preg"] == True:
        scene marbella_gang_bj_preg_5 with dissolve
    else:
        scene marbella_gang_bj_nopreg_5 with dissolve
    $ Pause()
    "Marbella moved faster, swallowing a few more inches of the Khazah's cock greedily."
    KHAZAH "Ooh! That's it!"
    "Her hand stroked furiously at my cock as her lips glided back and forth servicing the Khazah."
    KHAZAH "You know how to pleasure cock."
    KHAZAH "I'm sure the other Khazah are going to love you, heh..."
    "After a few moments, she pulled away once more,"
    $ PlaySexFx(audio.ves69_150, 1)
    if tmpvar["preg"] == True:
        scene marbella_gang_bj_preg_4 with dissolve
    else:
        scene marbella_gang_bj_nopreg_4 with dissolve
    $ Pause()
    "pressing her lips back onto me as her pace quickened."
    "As she stroked the other faster, her eyes lifted pleadingly toward me."
    "There was a shy, desperate need for approval as she continued,"
    "and every soft moan I gave only encouraged her further."
    MARBELLA "(Oh gods, I'm far too comfortable being— ahh! —their plaything!)"
    MARBELLA "(Fuck... Was I really this desperate all along?)"
    MARBELLA "(I just hope Gavkat or the others never find out.)"
    MARBELLA "(... At least as long as I keep this part of my life separate.)"
    MARBELLA "(Mhmm... It could be worse.)"
    MARBELLA "(Mmmfghh... This could...)"
    MC "Ahh! Marbella!"
    MC "I'm getting close!"
    MARBELLA "(G-Get a little addictive!)"
    KHAZAH "Ahh! Me too!"
    KHAZAH "Come on!"
    "Marbella lips remained firmly on my cock."
    MARBELLA "(Come on, come on!)"
    MARBELLA "(GIVE ME THAT THICK LOAD!)"
    $ PlaySexFx(audio.kiara_bj_finish)
    if tmpvar["preg"] == True:
        scene marbella_gang_bj_preg_finish with flash
    else:
        scene marbella_gang_bj_nopreg_finish with flash
    $ Pause()
    "I finished first, shortly followed by the Khazah who plastered her tits and face in his seed."
    "Marbella gasped slightly in surprise,"
    "swallowing down as much of the thick load as possible that spilled from the sides of her mouth,"
    "Marbella could only groan in appreciation, stroking out the last drops of the Khazah's cum with her hand."
    "And then, once she was satisfied our balls were drained she dragged her lips forward, cleaning up my cock submissively before pulling her lips away with a loud *PLOP* sound."
    scene black with dissolve
    return