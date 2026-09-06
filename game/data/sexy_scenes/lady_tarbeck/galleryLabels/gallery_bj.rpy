label gallery_lady_tarbeck_garden_bj:
    scene black with dissolve

    $ tmpvar["preg"] = False
    $ tmpvar["rep"] = False
    "Was it our first time?"
    menu:
        "Yes.":
            $ tmpvar["rep"] = False
        "No." if GalFlagCount("lady_tarbeck", "garden_bj") > 0:
            $ tmpvar["rep"] = True
    if tmpvar["rep"]:
        $ SetRepeatVariant(True)
        "Was she pregnant at the time?"
        menu:
            "Not pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "garden_bj", "_nopreg") > 0:
                $ tmpvar["preg"] = False
            "Pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "garden_bj", "_preg") > 0:
                $ tmpvar["preg"] = True
    else:
        $ tmpvar["preg"] = False

    $ StartReplay("replay_tarbeck_romance_garden_bj", Scope = {"Sex_SharedPregFlag":tmpvar["preg"], "tmpvar":tmpvar})
    scene black with dissolve
    return
