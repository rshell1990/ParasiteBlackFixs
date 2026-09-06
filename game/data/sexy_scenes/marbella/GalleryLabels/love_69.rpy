label gallery_marbella_love_69:
    $ tmpvar["rep"] = False
    if GalFlag("marbella", "love_69", ["var_first", "var_rep"]):
        "Was it our first time?"
        menu:
            "Yes":
                $ tmpvar["rep"] = True
            "No":
                $ tmpvar["rep"] = False
    elif GalFlag("marbella", "love_69", "var_first"):
        $ tmpvar["rep"] = False
    elif GalFlag("marbella", "love_69", "var_rep"):
        $ tmpvar["rep"] = True
    $ StartReplay("replay_marbella_love_69", Scope = {"Sex_SharedRepeatFlag":tmpvar["rep"]})
    scene black with dissolve
    return
