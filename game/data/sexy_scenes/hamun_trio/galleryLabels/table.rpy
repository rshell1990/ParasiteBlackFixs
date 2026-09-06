label gallery_hamun_trio_table:
    $ tmpvar = {}
    $ tmpvar["rep"] = False
    $ tmpvar["preg"] = False
    $ tmpvar["anal"] = False
    $ tmpvar["target_label"] = "replay_trio_table_firsttime"

    if GalFlag("hamun_trio", "table", "var_rep"):
        ### first-rep
        "Was it our first time?"
        menu:
            "Yes":
                $ tmpvar["rep"] = False
            "No":
                $ tmpvar["rep"] = True
    if tmpvar["rep"]:
        ### preg/nopreg
        if GalFlagsWithSubstringAmt("hamun_trio", "table", "_preg_") > 0 and GalFlagsWithSubstringAmt("hamun_trio", "table", "_nopreg_") > 0:
            "Were the women pregnant at the time?"
            menu:
                "Yes":
                    $ tmpvar["preg"] = True
                "No":
                    $ tmpvar["preg"] = False
        elif GalFlagsWithSubstringAmt("hamun_trio", "table", "_preg_") > 0:
            $ tmpvar["preg"] = True
        else:
            $ tmpvar["preg"] = False
        
        ### vag/anal
        if GalFlagsWithSubstringAmt("hamun_trio", "table", "_vag") > 0 and GalFlagsWithSubstringAmt("hamun_trio", "table", "_anal") > 0:
            "Was it vaginal or anal?"
            menu:
                "Vaginal":
                    $ tmpvar["anal"] = False
                "Anal":
                    $ tmpvar["anal"] = True
        elif GalFlagsWithSubstringAmt("hamun_trio", "table", "_vag") > 0:
            $ tmpvar["anal"] = False
        else:
            $ tmpvar["anal"] = True

    if tmpvar["rep"]:
        if tmpvar["anal"]:
            $ tmpvar["target_label"] = "rom_hamun_trio_table_anal"
        else:
            $ tmpvar["target_label"] = "rom_hamun_trio_table_vag"
    else:
        $ tmpvar["target_label"] = "replay_trio_table_firsttime"

    $ SetRepeatVariant(tmpvar["rep"])
    $ StartReplay(tmpvar["target_label"], Scope = {"Sex_SharedPregFlag":tmpvar["preg"]})
    return