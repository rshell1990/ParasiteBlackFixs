# anal/vag vars
label gallery_betty_missionary:
    scene black with dissolve

    $ tmpvar["pregstate"] = "nopreg"
    $ tmpvar["kind"] = "vag"

    "Was she pregnant at the time?"
    menu:
        "Not pregnant." if GalFlagsWithSubstringAmt("betty", "missionary", "_nopreg_") > 0:
            $ tmpvar["pregstate"] = "nopreg"
        "Pregnant." if GalFlagsWithSubstringAmt("betty", "missionary", "_preg_") > 0:
            $ tmpvar["pregstate"] = "preg"

    "Was it vaginal or anal?"
    menu:
        "Vaginal." if GalFlagsWithSubstringAmt("betty", "missionary", tmpvar["pregstate"] + "_vag") > 0:
            $ tmpvar["kind"] = "vag"
        "Anal."    if GalFlagsWithSubstringAmt("betty", "missionary", tmpvar["pregstate"] + "_anal") > 0:
            $ tmpvar["kind"] = "anal"

    if tmpvar["pregstate"] == "preg":
        $ tmpvar["pregstate"] = True
    else:
        $ tmpvar["pregstate"] = False

    if tmpvar["kind"] == "vag":
        $ StartReplay("replay_betty_missionary_vag", Scope = {"Sex_SharedPregFlag":tmpvar["pregstate"], "tmpvar":tmpvar})
    elif tmpvar["kind"] == "anal":
        $ StartReplay("replay_betty_missionary_anal", Scope = {"Sex_SharedPregFlag":tmpvar["pregstate"], "tmpvar":tmpvar})
    scene black with dissolve

    return