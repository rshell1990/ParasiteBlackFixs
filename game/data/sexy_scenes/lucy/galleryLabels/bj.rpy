label gallery_lucy_bj:
    scene black with dissolve   
    $ tmpvar["preg"] = False
    "Was she pregnant at the time?"
    menu:
        "Not pregnant." if GalFlagsWithSubstringAmt("lucy", "bj", "_nopreg") > 0:
            $ tmpvar["preg"] = False
        "Pregnant." if GalFlagsWithSubstringAmt("lucy", "bj", "_preg") > 0:
            $ tmpvar["preg"] = True
    $ StartReplay("replay_lucy_bj", Scope = {"Sex_SharedPregFlag":tmpvar["preg"]})
    scene black with dissolve
    return
