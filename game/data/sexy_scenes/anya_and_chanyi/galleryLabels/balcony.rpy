label gallery_faymore_balcony:
    scene black with dissolve
    $ tmpvar["pregstate"] = "nopreg"
    $ tmpvar["clothes"] = "naked"
    
    "Were they pregnant at the time?"
    menu:
        "Not pregnant." if GalFlagsWithSubstringAmt("anya_and_chanyi", "balcony", "_nopreg_") > 0:
            $ tmpvar["pregstate"] = "nopreg"
        "Pregnant." if GalFlagsWithSubstringAmt("anya_and_chanyi", "balcony", "_preg_") > 0:
            $ tmpvar["pregstate"] = "preg"
    "What were they wearing?"
    menu:
        "Down to their lingerie." if GalFlagsWithSubstringAmt("anya_and_chanyi", "balcony", tmpvar["pregstate"] + "_ling") > 0:
            $ tmpvar["clothes"] = "ling"
        "Completely naked." if GalFlagsWithSubstringAmt("anya_and_chanyi", "balcony", tmpvar["pregstate"] + "_naked") > 0:
            $ tmpvar["clothes"] = "naked"

    if tmpvar["pregstate"] == "nopreg":
        $ tmpvar["pregstate"] = False
    elif tmpvar["pregstate"] == "preg":
        $ tmpvar["pregstate"] = True

    # that scene refers tmpvar, who cares
    $ StartReplay("replay_faymore_balcony", Scope = {"Sex_SharedPregFlag":tmpvar["pregstate"], "tmpvar":tmpvar})
    scene black with dissolve
    return