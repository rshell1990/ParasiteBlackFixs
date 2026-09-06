label gallery_lady_tarbeck_darkmage_portal:
    scene black with dissolve
    $ tmpvar["kind"] = "vag"
    $ tmpvar["rep"] = False
    "Was it our first time?"
    menu:
        "Yes.":
            $ tmpvar["rep"] = False
        "No." if GalFlagCount("lady_tarbeck", "portal") > 0:
            $ tmpvar["rep"] = True
    if tmpvar["rep"]:
        $ SetRepeatVariant(True)
        "Was it vaginal or anal?"
        menu:
            "Vaginal." if GalFlagsWithSubstringAmt("lady_tarbeck", "quarters_missionary", "_vag") > 0:
                $ tmpvar["kind"] = "vag"
            "Anal."    if GalFlagsWithSubstringAmt("lady_tarbeck", "quarters_missionary", "_anal") > 0:
                $ tmpvar["kind"] = "anal"
    else:
        $ tmpvar["kind"] = "vag"  
    if tmpvar["kind"] == "vag":
        $ StartReplay("replay_tarbeck_darkmage_portal_vag", Scope = {"tmpvar":tmpvar})
    elif tmpvar["kind"] == "anal":
        $ StartReplay("replay_tarbeck_darkmage_portal_anal", Scope = {"tmpvar":tmpvar})
    return


    

