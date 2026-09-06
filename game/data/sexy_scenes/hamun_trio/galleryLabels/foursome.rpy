label gallery_hamun_trio_foursome:
    $ tmpvar = {}
    $ tmpvar["rep"] = False
    $ tmpvar["preg"] = False
    # if first time?
    if GalFlag("hamun_trio", "foursome", "var_rep"):
        "Was it our first time?"
        menu:
            "Yes":
                $ tmpvar["rep"] = False
            "No":
                $ tmpvar["rep"] = True
    if tmpvar["rep"] == True:
        if GalFlag("hamun_trio", "foursome", "var_preg"):
            "Were the women pregnant at the time?"
            menu:
                "Yes":
                    $ tmpvar["preg"] = True
                "No":
                    $ tmpvar["preg"] = False

    $ SetRepeatVariant(tmpvar["rep"])
    $ StartReplay("replay_trio_foursome", Scope = {"Sex_SharedPregFlag":tmpvar["preg"]})
    return