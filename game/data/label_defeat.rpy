label defeat_generic:
    hide screen WaitClickToStop
    $ InfectionModule().DailyGain = False # <- if this aint disabled, causes a loop on death due to inf
    $ HideUI(True)
    $ AutoMus(False)
    stop music fadeout 0.1
    stop ambience fadeout 0.1
    play sound "audio/cfx/gameover.ogg" volume 0.6
    scene cg_lose
    with flash
    $ tmpvar = {}
    "Your adventure has come to an end."
    menu Generic_Defeat_Menu:    
        "Load game":
            call screen save_load(HideOnReturnBtn = True, BlockSave = True)
            jump Generic_Defeat_Menu

        "Quit to main menu":
            call screen confirm("Leave to main menu?", yes_action = Function(renpy.full_restart), no_action = Jump("Generic_Defeat_Menu"))    