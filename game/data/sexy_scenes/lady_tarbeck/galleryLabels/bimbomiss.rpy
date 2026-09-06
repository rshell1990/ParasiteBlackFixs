label gallery_lady_tarbeck_bimbomiss:
    scene black with dissolve
    $ tmpvar["pregstate"] = "nopreg"
    $ tmpvar["rep"] = False
    "Was it our first time?"
    menu:
        "Yes.":
            $ tmpvar["rep"] = False
        "No." if GalFlagCount("lady_tarbeck", "bimbomiss") > 0:
            $ tmpvar["rep"] = True
    if tmpvar["rep"]:
        $ SetRepeatVariant(True)
        "Was she pregnant at the time?"
        menu:
            "Not pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "bimbomiss", "_nopreg") > 0:
                $ tmpvar["pregstate"] = "nopreg"
            "Pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "bimbomiss", "_preg") > 0:
                $ tmpvar["pregstate"] = "preg"
    else:
        $ tmpvar["pregstate"] = "nopreg"
    
    if tmpvar["pregstate"] == "preg":
        $ tmpvar["pregstate"] = True
    else:
        $ tmpvar["pregstate"] = False

    $ StartReplay("replay_tarbeck_bimbo_miss", Scope = {"Sex_SharedPregFlag":tmpvar["pregstate"], "tmpvar":tmpvar})
    scene black with dissolve
    return