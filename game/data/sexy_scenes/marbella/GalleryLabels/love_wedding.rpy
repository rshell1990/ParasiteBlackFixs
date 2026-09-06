label gallery_marbella_love_wedding:
    $ tmpvar["preg"] = False
    if GalFlag("marbella", "love_wedding", ["var_preg_anal", "var_preg_vag"], anymatch = True) and GalFlag("marbella", "love_wedding", ["var_nopreg_anal", "var_nopreg_vag"], anymatch = True):
        "Was she pregnant at the time?"
        menu:
            "Yes":
                $ tmpvar["preg"] = True
            "No":
                $ tmpvar["preg"] = False
    elif GalFlag("marbella", "love_wedding", ["var_preg_anal", "var_preg_vag"], anymatch = True):
        $ tmpvar["preg"] = True
    elif GalFlag("marbella", "love_wedding", ["var_nopreg_anal", "var_nopreg_vag"], anymatch = True):
        $ tmpvar["preg"] = False

    $ tmpvar["vag"] = True
    if GalFlag("marbella", "love_wedding", ["var_preg_vag", "var_nopreg_vag"], anymatch = True) and GalFlag("marbella", "love_wedding", ["var_nopreg_anal", "var_preg_anal"], anymatch = True):
        "Was it vaginal or anal?"
        menu:
            "Anal":
                $ tmpvar["vag"] = False
            "Vaginal":
                $ tmpvar["vag"] = True
    elif GalFlag("marbella", "love_wedding", ["var_preg_vag", "var_nopreg_vag"], anymatch = True):
        $ tmpvar["vag"] = True
    elif GalFlag("marbella", "love_wedding", ["var_nopreg_anal", "var_preg_anal"], anymatch = True):
        $ tmpvar["vag"] = False

    if tmpvar["vag"] == True:
        $ StartReplay("rom_marbella_love_wedding_vag", Scope = {"Sex_SharedPregFlag":tmpvar["preg"]})
    elif tmpvar["vag"] == False:
        $ StartReplay("rom_marbella_love_wedding_anal", Scope = {"Sex_SharedPregFlag":tmpvar["preg"]})

    scene black with dissolve
    return
