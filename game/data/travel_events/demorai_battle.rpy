label travel_event_battle_demorai:
    show mc at left with easeinleft
    "While making my way along the roads, I suddenly heard what sounded like a roar, followed by rumbling drawing quickly closer."
    "Suddenly, teeth and claws were gnashing all around me as the hideous demorai launched their attack!"
    show mc angry
    show cg_demorai_brute_highrez:
        xcenter 0.85
        xzoom -1.0
    with moveinright
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    MC "(SHIT!)"
    MC "DEMORAI!"
    $ tmpvar = {}
    $ tmpvar = ["e_demorai_brute"]
    if GetPartySize() > 1:
        $ tmpvar.append("e_demorai_scout")
    if GetPartySize() > 2:
        $ tmpvar.append("e_demorai_brute")
    if GetPartySize() > 3:
        $ tmpvar.append("e_demorai_scout")

    $ StartBattle(BattleData(BackgroundImage = TravelRoutes[TravelState.RouteID]["image_battle_bg"], CharIDList_Right = tmpvar))
    $ tmpvar = {}
    "Slaying the last of the demorai, I sighed and wiped the blood from myself before moving forward."
    $ AutoMus(True)
    MC "(Need to be careful travelling these roads ... I should make sure I'm prepared for whatever may come my way.)"
    return
