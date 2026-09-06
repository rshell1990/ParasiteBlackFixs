# anal/vag vars
label gallery_lucy_sidefuck:
    scene black with dissolve

    $ tmpvar["preg"] = "nopreg"
    $ tmpvar["kind"] = "vag"

    "Was she pregnant at the time?"
    menu:
        "Not pregnant." if GalFlagsWithSubstringAmt("lucy", "sidefuck", "_nopreg_") > 0:
            $ tmpvar["preg"] = "nopreg"
        "Pregnant." if GalFlagsWithSubstringAmt("lucy", "sidefuck", "_preg_") > 0:
            $ tmpvar["preg"] = "preg"

    "Was it vaginal or anal?"
    menu:
        "Vaginal." if GalFlagsWithSubstringAmt("lucy", "sidefuck", tmpvar["preg"] + "_vag") > 0:
            $ tmpvar["kind"] = "vag"
        "Anal."    if GalFlagsWithSubstringAmt("lucy", "sidefuck", tmpvar["preg"] + "_anal") > 0:
            $ tmpvar["kind"] = "anal"

    if tmpvar["preg"] == "preg":
        $ tmpvar["preg"] = True
    else:
        $ tmpvar["preg"] = False

    if tmpvar["kind"] == "vag":
        $ StartReplay("replay_lucy_sidefuck_vag", Scope = {"Sex_SharedPregFlag":tmpvar["preg"], "tmpvar":tmpvar})
    elif tmpvar["kind"] == "anal":
        $ StartReplay("replay_lucy_sidefuck_anal", Scope = {"Sex_SharedPregFlag":tmpvar["preg"], "tmpvar":tmpvar})
    scene black with dissolve
    return