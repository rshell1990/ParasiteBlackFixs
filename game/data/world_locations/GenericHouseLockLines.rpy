label HouseLockLines:
    $ rng = RngInt(1, 3)
    if rng == 1:
        MC "(The door won't budge.)"
    if rng == 2:
        MC "(It's locked.)"
    if rng == 3:
        MC "(Locked.)"
    $ LocEnterQ()

label HouseLockLines_JustClosed:
    $ rng = RngInt(1, 3)
    if rng == 1:
        MC "(It is closed at this time of day.)"
    if rng == 2:
        MC "(It's closed.)"
    if rng == 3:
        MC "(It's closed, I should try another time.)"
    $ LocEnterQ()
