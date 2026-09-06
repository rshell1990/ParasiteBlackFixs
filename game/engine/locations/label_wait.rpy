
label wait:
    $ BlockWaitDynamic(True)
    $ PlaySoundRandom("clockWind", Channel = "guisfx", Volume = 0.7)

    $ LocFlush() # < not having this makes weird error happen
    if not DEBUG_FastMode:
        with dissolve

    $ tmpvar = {}
    $ tmpvar["wait_hours"] = rest_menu_wait_hours
    show screen WaitClickToStop()
    while tmpvar["wait_hours"] > 0:
        # loop unwind :brain:
        $ TimeAdvBy(TIME_025H)
        $ LocFlush()
        if not DEBUG_FastMode:
            $ Pause(0.03)
        $ TimeAdvBy(TIME_05H)
        $ LocFlush()
        if not DEBUG_FastMode:
            $ Pause(0.03)
        $ TimeAdvBy(TIME_025H)
        $ LocFlush()
        if not DEBUG_FastMode:
            $ Pause(0.03)
        else:
            $ Pause(0.001)

        call ProcessLocEvent("Enter") from _call_ProcessLocEvent_3

        $ BlockWaitDynamic(True)
        $ tmpvar["wait_hours"] -= 1
    hide screen WaitClickToStop
    $ BlockWaitDynamic(False)
    $ tmpvar = {}
    $ LocEnterQ()

screen WaitClickToStop():
    on "hide" action TooltipClearUI()
    button:
        background Null()
        xsize 1920
        ysize 1080
        mouse "default"
        hovered TooltipSetUI(_("Waiting.\n(Click to stop)"))
        keysym ["K_SPACE", "K_RETURN", config.keymap["inventory"][0], config.keymap["characters"][0], 
            config.keymap["relations"][0], config.keymap["map"][0], config.keymap["journal"][0], 
            config.keymap["gui_rest_menu"][0], config.keymap["dialogue_history"][0], config.keymap["game_menu"][0],
            config.keymap["nav_up"][0], config.keymap["nav_down"][0], config.keymap["nav_right"][0], config.keymap["nav_left"][0]]

        action [SetDict(tmpvar, "wait_hours", 0), Hide("WaitClickToStop")]