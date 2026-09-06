label qst_guild_caravan:
    scene black with dissolve
    $ LocNameSetTemp(_("Road to the City of Hamun"))
    'Upon meeting with the Traders convoy, we set out along the arduous journey, traveling along the outskirts of the Valley of death along the dirt roads before we planned to plunge through the shortest path of the desert.'
    'We stopped at the few fortress inns that we could when the land became dark, but the Traders were keen at the first break of light to keep us moving through the valley as quickly as possible.'
    $ PlaySoundRandom("clockWind", Channel = "guisfx", Volume = 0.7)
    $ TimeAdvTo(TIME_VISUAL_DAWN)
    scene cg_forest_caravan with dissolve
    'Along the way, the convoy was suddenly halted by a woman stood in the middle of the road holding what seemed to be a baby cradled in her one arm as she did her best to wave us down.'
    $ AutoMus(False)
    'As the caravan slowed down though, she tossed the bundle of rags aside, revealing a crossbow beneath that she fired straight towards one of the coachmen, piercing him straight through the eye as he slumped over dead.'
    $ PlayMusicRandom("mus_battle_generic")
    'Panic and screams arose all around as the horses with the dead coachmen rose up onto their hind legs and bolted, sending the caravan hurdling off-course and crashing it against a rock before they fled across the fields.'
    
    CARAVAN_MASTER "BANDITS!"
    show cg_bandit_dark onlayer characters as bandit1:
        xcenter 0.2
        zoom 1.0
    with dissolve
    show cg_bandit_dark onlayer characters as bandit2:
        xcenter 0.8
        zoom 0.9
        xzoom -1.0
    with dissolve
    show cg_bandit_dark onlayer characters as bandit3:
        xcenter 0.7
        zoom 0.8
        yoffset 50
        xzoom -1.0
    with dissolve
    "A hurl of arrows hit into the sides of some of the caravans as frantically people reached to grab whatever weapons they could to defend themselves."
    "I drew my blade as I heard a resolute cry:"
    scene black with dissolve
    CARAVAN_MASTER "PROTECT THE CARAVAN!"
    $ QstSetProgress(QstGuildCaravan, 1)
    $ StartBattle(BattleData(BackgroundImage = "pbat_forest", CharIDList_Right = ["e_raider", "e_raider"], CanTransform = False))
    "After slicing down another one of the bandits with my blade, a loud horn was sounded as the remaining bandits fled, dragging their wounded with them."
    "The Caravan wasted no time, quickly hurried away from the scene before the bandits could try again, horses bolting as fast as they could along the road."
    $ AutoMus(True)
    $ QstSetProgress(QstGuildCaravan, 2)
    "Eventually, after a few more hours travel, we arrived at the outskirts of Hamun safely at last."
    "The traders thanked me for my protection, and I was rewarded there and then with payment."
    $ QstComplete(QstGuildCaravan)
    MC "{i}*Sigh*{/i}"
    $ LocNameReset()

    scene black with dissolve
    $ LocSet("novaras_gates")
    $ TimeAdvTo(TIME_VISUAL_DUSK)
    $ LocEnter()