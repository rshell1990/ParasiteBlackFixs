label gallery_lady_tarbeck_quarters_missionary:
    scene black with dissolve
    $ tmpvar["pregstate"] = "nopreg"
    $ tmpvar["kind"] = "vag"
    $ tmpvar["rep"] = False
    "Was it our first time?"
    menu:
        "Yes.":
            $ tmpvar["rep"] = False
        "No." if GalFlagCount("lady_tarbeck", "quarters_missionary") > 0:
            $ tmpvar["rep"] = True
    if tmpvar["rep"]:
        $ SetRepeatVariant(True)
        "Was she pregnant at the time?"
        menu:
            "Not pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "quarters_missionary", "_nopreg_") > 0:
                $ tmpvar["pregstate"] = "nopreg"
            "Pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "quarters_missionary", "_preg_") > 0:
                $ tmpvar["pregstate"] = "preg"
        "Was it vaginal or anal?"
        menu:
            "Vaginal." if GalFlagsWithSubstringAmt("lady_tarbeck", "quarters_missionary", tmpvar["pregstate"] + "_vag") > 0:
                $ tmpvar["kind"] = "vag"
            "Anal."    if GalFlagsWithSubstringAmt("lady_tarbeck", "quarters_missionary", tmpvar["pregstate"] + "_anal") > 0:
                $ tmpvar["kind"] = "anal"
    else:
        $ tmpvar["pregstate"] = "nopreg"
        $ tmpvar["kind"] = "vag"  
    
    if tmpvar["pregstate"] == "preg":
        $ tmpvar["pregstate"] = True
    else:
        $ tmpvar["pregstate"] = False

    if tmpvar["kind"] == "vag":
        $ StartReplay("replay_tarbeck_romance_quarters_missionary_vag", Scope = {"Sex_SharedPregFlag":tmpvar["pregstate"], "tmpvar":tmpvar})
    elif tmpvar["kind"] == "anal":
        $ StartReplay("replay_tarbeck_romance_quarters_missionary_anal", Scope = {"Sex_SharedPregFlag":tmpvar["pregstate"], "tmpvar":tmpvar})
    scene black with dissolve
    return


    