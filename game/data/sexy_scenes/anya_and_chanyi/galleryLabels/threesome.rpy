label gallery_faymore_threesome:
    scene black with dissolve
### rep flag
    $ tmpvar["rep"] = False
    $ tmpvar["preg"] = "nopreg"
    $ tmpvar["kind"] = "vag"
    $ tmpvar["clothes"] = "naked"
    if GalFlag("anya_and_chanyi", "threesome", ["var_first", "var_rep"]):
        "Was it our first time?"
        menu:
            "Yes":
                $ tmpvar["rep"] = False
            "No":
                $ tmpvar["rep"] = True
    elif GalFlag("anya_and_chanyi", "threesome", "var_first"):
        $ tmpvar["rep"] = False
############
    if tmpvar["rep"] == True:
        "Were they pregnant at the time?"
        menu:
            "Not pregnant." if GalFlagsWithSubstringAmt("anya_and_chanyi", "threesome", "_nopreg_") > 0:
                $ tmpvar["preg"] = "nopreg"
            "Pregnant." if GalFlagsWithSubstringAmt("anya_and_chanyi", "threesome", "_preg_") > 0:
                $ tmpvar["preg"] = "preg"

        "Was it vaginal or anal?"
        menu:
            "Vaginal." if GalFlagsWithSubstringAmt("anya_and_chanyi", "threesome", tmpvar["preg"] + "_" + "vag") > 0:
                $ tmpvar["kind"] = "vag"
            "Anal." if GalFlagsWithSubstringAmt("anya_and_chanyi", "threesome", tmpvar["preg"] + "_" + "anal") > 0:
                $ tmpvar["kind"] = "anal"

        "What were they wearing?"
        menu:
            "Down to their lingerie." if GalFlagsWithSubstringAmt("anya_and_chanyi", "threesome", tmpvar["preg"] + "_" + tmpvar["kind"] + "_ling") > 0:
                $ tmpvar["clothes"] = "ling"
            "Completely naked." if GalFlagsWithSubstringAmt("anya_and_chanyi", "threesome", tmpvar["preg"] + "_" + tmpvar["kind"] + "_naked") > 0:
                $ tmpvar["clothes"] = "naked"

    if tmpvar["preg"] == "preg":
        $ tmpvar["preg"] = True
    else:
        $ tmpvar["preg"] = False

    $ SetRepeatVariant(tmpvar["rep"])

    $ tmpvar["variant"] = tmpvar["kind"]
    # that scene refers tmpvar, who cares
    $ StartReplay("replay_faymore_threesome", Scope = {"Sex_SharedPregFlag":tmpvar["preg"], "tmpvar":tmpvar})
    scene black with dissolve
    return