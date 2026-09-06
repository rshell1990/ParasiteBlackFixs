# anal/vag vars
label gallery_vivian_missionary:
    scene black with dissolve

    $ tmpvar["preg"] = "nopreg"
    $ tmpvar["kind"] = "vag"

    "Was she pregnant at the time?"
    menu:
        "Not pregnant." if GalFlagsWithSubstringAmt("vivian", "missionary", "_nopreg_") > 0:
            $ tmpvar["preg"] = "nopreg"
        "Pregnant." if GalFlagsWithSubstringAmt("vivian", "missionary", "_preg_") > 0:
            $ tmpvar["preg"] = "preg"

    "Was it vaginal or anal?"
    menu:
        "Vaginal." if GalFlagsWithSubstringAmt("vivian", "missionary", tmpvar["preg"] + "_vag") > 0:
            $ tmpvar["kind"] = "vag"
        "Anal."    if GalFlagsWithSubstringAmt("vivian", "missionary", tmpvar["preg"] + "_anal") > 0:
            $ tmpvar["kind"] = "anal"

    if tmpvar["preg"] == "preg":
        $ tmpvar["preg"] = True
    else:
        $ tmpvar["preg"] = False

    # that scene refers tmpvar, who cares
    if tmpvar["kind"] == "vag":
        $ StartReplay("replay_vivian_missionary_vag", Scope = {"Sex_SharedPregFlag":tmpvar["preg"], "tmpvar":tmpvar})
    elif tmpvar["kind"] == "anal":
        $ StartReplay("replay_vivian_missionary_anal", Scope = {"Sex_SharedPregFlag":tmpvar["preg"], "tmpvar":tmpvar})
    scene black with dissolve

    return