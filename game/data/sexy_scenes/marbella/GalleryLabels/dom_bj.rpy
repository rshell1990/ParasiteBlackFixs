label gallery_marbella_dom_bj:
    scene black with dissolve
    # replay_marbella_dom_bj_rep
    # replay_marbella_dom_bj
    if GalFlag("marbella", "dom_bj", "var_repeat"):
        "Was it our first time?"
        menu:
            "Yes":
                $ StartReplay("replay_marbella_dom_bj_rep")
                scene black with dissolve
                return
            "No":
                $ StartReplay("replay_marbella_dom_bj")
                scene black with dissolve
                return
    else:
        $ StartReplay("replay_marbella_dom_bj")
        scene black with dissolve
        return
