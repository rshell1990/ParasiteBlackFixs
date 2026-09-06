label gallery_vivian_bj:
    $ tmpvar["preg"] = False
    scene black with dissolve   
    "Was she pregnant at the time?"
    menu:
        "Not pregnant." if GalFlagsWithSubstringAmt("vivian", "bj", "_nopreg") > 0:
            $ tmpvar["preg"] = False
        "Pregnant." if GalFlagsWithSubstringAmt("vivian", "bj", "_preg") > 0:
            $ tmpvar["preg"] = True
    $ StartReplay("replay_vivian_bj", Scope = {"Sex_SharedPregFlag":tmpvar["preg"]})
    scene black with dissolve
    return
