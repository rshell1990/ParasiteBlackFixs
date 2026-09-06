label travel_event_white_bear:
    show mc at left with easeinleft
    "While making my way along the path, a loud bestial grunt was followed by a defiant roar."
    $ AutoMus(False)
    if GetPartySize() > 0:
        "Every hair on my body stood up as I turned, hand ready on my blade to see a huge bear charging towards us!"
        MC @angry "BEARRRRRRRRRR!"
        hide mc with dissolve
    else:
        "Every hair on my body stood up as I turned, hand ready on my blade to see a huge bear charging towards me!"
        MC "(A bear!)"
    $ PlayMusicRandom("mus_battle_generic")

    $ StartBattle(BattleData(BackgroundImage = TravelRoutes[TravelState.RouteID]["image_battle_bg"], CharIDList_Right = ["e_bear_white"]))
    "With a loud thud, the bear finally collapsed to the floor, its chest rising and falling slowly with every wheezing breath."
    "Eventually, after one final exhale, the thing lay silent and motionless on the floor."
    $ AutoMus(True)
    return