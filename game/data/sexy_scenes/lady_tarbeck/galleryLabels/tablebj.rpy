label gallery_lady_tarbeck_tablebj:
    scene black with dissolve
    $ tmpvar["preg"] = False
    $ tmpvar["rep"] = False
    "Was it our first time?"
    menu:
        "Yes.":
            $ tmpvar["rep"] = False
        "No." if GalFlagCount("lady_tarbeck", "tablebj") > 0:
            $ tmpvar["rep"] = True
    $ SetRepeatVariant(tmpvar["rep"])
    $ StartReplay("replay_tarbeck_darkmage_tablebj", Scope = {"Sex_SharedPregFlag":tmpvar["preg"], "tmpvar":tmpvar})
    scene black with dissolve
    return

