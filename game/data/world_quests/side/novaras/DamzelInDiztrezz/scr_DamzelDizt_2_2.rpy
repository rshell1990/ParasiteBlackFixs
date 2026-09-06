label qst_DamzelDizzt_2_frontal_postScout:
    #1.) Continued - Fade to black
    #SCENE 5- NIJAH QUEST - (FRONTAL ASSAULT CHOICE)- THE BLACK DIAMOND - NIGHT
    $ GoalComplete(QstDamzelInDiztrezz, 1.5)
    $ GoalShow(QstDamzelInDiztrezz, 2)
    $ QstDamzelInDiztrezz().PlayerChoseFrontalAssault = True
    scene black with dissolve
    $ LocSet("novaras_dist_pleasure")
    $ LocFlush()
    with dissolve
    show mc_transformed:
        xcenter 0.0
    show markus_transformed:
        xcenter 1.0
        xzoom -1.0
    with dissolve
    'We clambered onto a rooftop of a building near the Black Diamond as soon as night fell across Novaras.'
    'Both me and Markus waited in position in our {i}‘other’{/i} forms as we listened out for the loud whizzing sounds of the fire sticks.'
    'Explosions loudly began to boom as they began blossoming into pretty color patterns, lighting up the night sky.'

    MC 'Looks like Nijah came through...'
    'Markus turned to me and nodded.'
    hide mc_transformed
    hide markus_transformed
    scene black
    with dissolve
    'Clambering down, we moved swiftly over towards the doors of the Black Diamond, and together,'
    'We wasted no time bashing our way through inside.'
    $ AutoMus(False)
    $ PlayMusic("audio/music/31_Encounter.ogg")
    $ LocSet("novaras_black_diamond")
    'Screams and shouts erupted as half naked dancers fled for the nearest exits.'
    'Tables filled with coin and cards were flipped as the guards drew their sabres onto us in a frenzied panic, shouting to each other about monsters.'
    'Those in the drug induced haze of the opium turn to look at us from their beds with confusion in their eyes,'
    'Unsure if what they saw were seeing was some illusion from chasing the dragon.'
    play sound2 "audio/cfx/transform.ogg"

    BANDIT @talk 'Monsters! MONSTERS! Kill them! Kill them now!'
    MC "(We don't have long! We have to finish this before the guards arrive!)"
    #TIMED BATTLE BEGINS: - THE PLAYER MUST DEFEAT ALL THE GUARDS AND TAREK IN THE TIMER OR IT’S GAME OVER DUE TO THE CITY GUARDS ARRIVING.
    #ONCE THE PLAYERS KILL ALL THE ENEMIES (2 WAVES).
    $ TransformMC(True)
    $ TransformMarkus(True)
     
    $ StartBattle(BattleData(BackgroundImage = "pbat_diamond", CharIDList_Right = ["e_bandit", "e_thug", "e_bandit"]))

    scene bg_diamond_blood
    MC "{i}*Huff* *Huff*{/i}"
    MC "(Hell, there's more!)"
     
    $ StartBattle(BattleData(BackgroundImage = "pbat_diamond", CharIDList_Right = ["e_thug", "e_bandit", "e_thug"]))

    $ TransformMC(False)
    $ TransformMarkus(False)

    'The Black Diamond became a fury of red mist and screams as the two of us cut down man after man as they came for us.'
    'Limb from limb we tore and slashed, the walls painted in long streaks of red blood as the adrenaline coursed through me.'
    'I could hardly control myself anymore, the dark impulses inside of me seemed to steer my every move as my claws stained with blood dripped onto the cold floor.'
    'Fear, panic, {i}fury{/i} the emotions run a gauntlet as we turned the place into a kind of nightmare scarely read about only in the darkest of tales.'
    'Finally, I heard a whistle and twisted my body to look towards the sound.'
    scene bg_diamond_blood with dissolve
    show markus_transformed at left
    show mc_transformed at cleft
    show tarek at right_f
    with dissolve
    TAREK @angry 'So... The inquisitors have finally made their move I see.'
    TAREK @angry 'And they send monsters to slay me!'
    'I growled and began to step towards Tarek as he drew his blade.'
    'Markus followed behind as we snarled towards him, ready to leap forward and slash and tear him to pieces!'
    TAREK @angry 'NOW!'
    scene black with dissolve
    'Suddenly, from the upper floors poured out more men to surround us, and beneath us we felt the floor open up and swallow us whole.'
    "I tried to use my tentacles to grip into the walls, but they coated in a thick black like slime that I couldn't get any grip into."
    'Markus tried to fly upwards but I collided against him, sending us tumbling down in freefall.'
    'Faling deep into the darkness, we finally slammed into the concrete ground below.'
    'Slightly dazed, I rose from my feet to see we had fallen into some section of the sewers below.'
    #MC and Markus have fallen into the sewer trap
    scene pbat_sewer with dissolve
    show markus_transformed:
        xcenter 0.2
    show mc_transformed:
        xcenter 0.8
        xzoom -1.0
    with dissolve
    "Looking up towards the opening of the trap door above us, I could hear Tarek's men laugh as he crouched down over the hole to torment us."
    TAREK @smile 'I know not what beasts you are, but did you truly think you could just walk in here and kill me?'
    'From the darkness I could hear feet loudly scuttering towards us.'
    TAREK @smile "Took us weeks to capture her, they've been turning up all over the Valley of Death recently."
    TAREK 'Took out a few of our best to take her in, but I think it was worth it in the end!'
    MARKUS '(Fuck! [player_name!t]! What do we do?)'
    MC "(Shit! He can't mean-)"
    TAREK 'Ever heard of Choza? Its like the opposite to Raza... They used to give it to Ramonian warriors before battle, make sure they would fucking slaughter anything in their path.'
    TAREK 'They stopped using it when the men went insane.'
    TAREK @smile "So we figured, {i}'why not feed it some of that with every meal?'{/i}"
    
    UNKNOWN '{i}*Clatter! Clatter! Clatter!*{/i}'
    "In that moment, from the darkness it appears, snapping it's claws as it scurried out from the darkness."
    scene black with dissolve
    TAREK @angry 'Dinner time Betsy!'
    $ PlayMusic("audio/music/27_Sands_Boss.ogg")
    MC '(FUCK!)'
    jump qst_DamzelDizzt_2_frontal_pit
