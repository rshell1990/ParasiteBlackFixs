label gallery_lady_tarbeck_library_hj:
    scene black with dissolve

    $ tmpvar["preg"] = False
    $ tmpvar["rep"] = False
    "Was it our first time?"
    menu:
        "Yes.":
            $ tmpvar["rep"] = False
        "No." if GalFlagCount("lady_tarbeck", "library_hj") > 0:
            $ tmpvar["rep"] = True

    if tmpvar["rep"]:
        $ SetRepeatVariant(True)
        "Was she pregnant at the time?"
        menu:
            "Not pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "library_hj", "_nopreg") > 0:
                $ tmpvar["preg"] = False
            "Pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "library_hj", "_preg") > 0:
                $ tmpvar["preg"] = True
    else:
        $ tmpvar["preg"] = False

    $ StartReplay("replay_tarbeck_romance_library_hj", Scope = {"Sex_SharedPregFlag":tmpvar["preg"], "tmpvar":tmpvar})
    scene black with dissolve
    return
