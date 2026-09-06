label gallery_lady_tarbeck_bimbotj:
    scene black with dissolve
    $ tmpvar["preg"] = False
    $ tmpvar["rep"] = False
    "Was it our first time?"
    menu:
        "Yes.":
            $ tmpvar["rep"] = False
        "No." if GalFlagCount("lady_tarbeck", "bimbotj") > 0:
            $ tmpvar["rep"] = True
    if tmpvar["rep"]:
        $ SetRepeatVariant(True)
        "Was she pregnant at the time?"
        menu:
            "Not pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "bimbotj", "_nopreg") > 0:
                $ tmpvar["preg"] = False
            "Pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "bimbotj", "_preg") > 0:
                $ tmpvar["preg"] = True
    else:
        $ tmpvar["preg"] = False

    $ StartReplay("replay_tarbeck_bimbo_tj", Scope = {"Sex_SharedPregFlag":tmpvar["preg"], "tmpvar":tmpvar})
    return