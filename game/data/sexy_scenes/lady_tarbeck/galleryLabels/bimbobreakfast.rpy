label gallery_lady_tarbeck_bimbobreakfast:
    scene black with dissolve
    $ tmpvar["pregstate"] = "nopreg"
    $ tmpvar["kind"] = "vag"
    $ tmpvar["rep"] = False
    "Was it our first time?"
    menu:
        "Yes.":
            $ tmpvar["rep"] = False
        "No." if GalFlagCount("lady_tarbeck", "bimbobreakfast") > 0:
            $ tmpvar["rep"] = True
    if tmpvar["rep"]:
        $ SetRepeatVariant(True)
        "Was she pregnant at the time?"
        menu:
            "Not pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "bimbobreakfast", "_nopreg") > 0:
                $ tmpvar["pregstate"] = "nopreg"
            "Pregnant." if GalFlagsWithSubstringAmt("lady_tarbeck", "bimbobreakfast", "_preg") > 0:
                $ tmpvar["pregstate"] = "preg"
        "Was it vaginal or anal?"
        menu:
            "Vaginal." if GalFlagsWithSubstringAmt("lady_tarbeck", "bimbobreakfast", tmpvar["pregstate"] + "_vag") > 0:
                $ tmpvar["kind"] = "vag"
            "Anal."    if GalFlagsWithSubstringAmt("lady_tarbeck", "bimbobreakfast", tmpvar["pregstate"] + "_anal") > 0:
                $ tmpvar["kind"] = "anal"
    else:
        $ tmpvar["pregstate"] = "nopreg"
        $ tmpvar["kind"] = "vag"
    
    if tmpvar["pregstate"] == "preg":
        $ tmpvar["pregstate"] = True
    else:
        $ tmpvar["pregstate"] = False

    if tmpvar["kind"] == "vag":
        $ StartReplay("replay_tarbeck_bimbo_breakfast", Scope = {"Sex_SharedPregFlag":tmpvar["pregstate"], "tmpvar":tmpvar})
    elif tmpvar["kind"] == "anal":
        $ StartReplay("rom_tarbeck_bimbo_breakfast_anal", Scope = {"Sex_SharedPregFlag":tmpvar["pregstate"], "tmpvar":tmpvar})
    scene black with dissolve
    return