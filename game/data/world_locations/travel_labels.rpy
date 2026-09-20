### generic travel label currently just skips time
label travel(travelHours = 3, targetTag = None):
    $ BlockWaitDynamic(True)
    scene expression Solid("#000000") with dissolve
    $ PlaySoundRandom("clockWind", Channel = "guisfx", Volume = 0.7)
    while travelHours > 0:
        $ TimeAdvBy(TIME_1H)
        $ travelHours -= 1
        $ Pause(0.11)
    $ BlockWaitDynamic(False)
    if targetTag is not None:
        $ LocSet(targetTag)
    $ LocEnter()