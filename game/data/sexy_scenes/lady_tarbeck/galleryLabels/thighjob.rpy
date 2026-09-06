label gallery_lady_tarbeck_thighjob:
    scene black with dissolve
    $ tmpvar["preg"] = False
    $ tmpvar["rep"] = False
    "Was it our first time?"
    menu:
        "Yes.":
            $ tmpvar["rep"] = False
        "No." if GalFlagCount("lady_tarbeck", "thighjob") > 0:
            $ tmpvar["rep"] = True
    $ SetRepeatVariant(tmpvar["rep"])
    $ StartReplay("replay_tarbeck_darkmage_thighjob", Scope = {"Sex_SharedPregFlag":tmpvar["preg"], "tmpvar":tmpvar})
    scene black with dissolve
    return
