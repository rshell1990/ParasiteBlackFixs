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
        keysym ["K_SPACE", "K_RETURN", 
            config.keymap.get("inventory", ["K_i"])[0], 
            config.keymap.get("characters", ["K_c"])[0],
            config.keymap.get("relations", ["K_r"])[0], 
            config.keymap.get("map", ["K_m"])[0], 
            config.keymap.get("journal", ["K_j"])[0], 
            config.keymap.get("gui_rest_menu", ["K_g"])[0], 
            config.keymap.get("dialogue_history", ["K_d"])[0], 
            config.keymap.get("game_menu", ["K_ESCAPE"])[0],
            config.keymap.get("nav_up", ["K_UP"])[0], 
            config.keymap.get("nav_down", ["K_DOWN"])[0], 
            config.keymap.get("nav_right", ["K_RIGHT"])[0], 
            config.keymap.get("nav_left", ["K_LEFT"])[0]]

        action [SetDict(tmpvar, "wait_hours", 0), Hide("WaitClickToStop")]