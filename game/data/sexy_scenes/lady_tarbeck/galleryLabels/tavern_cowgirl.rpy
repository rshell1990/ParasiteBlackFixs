label gallery_lady_tarbeck_tavern_cowgirl:
    scene black with dissolve
    $ tmpvar["pregstate"] = "nopreg"

    "Was she pregnant at the time?"
    menu:
        "Not pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "tavern_cowgirl", "_nopreg") > 0:
            $ tmpvar["pregstate"] = "nopreg"
        "Pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "tavern_cowgirl", "_preg") > 0:
            $ tmpvar["pregstate"] = "preg"

    if tmpvar["pregstate"] == "preg":
        $ tmpvar["pregstate"] = True
    else:
        $ tmpvar["pregstate"] = False
    $ StartReplay("replay_tarbeck_romance_cowgirl", Scope = {"Sex_SharedPregFlag":tmpvar["pregstate"], "tmpvar":tmpvar})
    scene black with dissolve
    return
