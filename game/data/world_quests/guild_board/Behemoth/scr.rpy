label qst_guild_behemoth:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusic("audio/music/15_Experiments.ogg")
    $ LocNameSetTemp(_("Novaras Sewers"))
    'Below the city of Novaras, an infinite labyrinth of sewers sprawled, a black abyss dreaded by many.'
    if GetPartySize() > 1:
        "As we embarked into the maw of the dark maze, we couldn't help but become mesmerized by the abysmal magnificience of the sewer system."
        'Every now and then, we saw festering corpses captured in haunting stillness.'
    else:
        "As I embarked into the maw of the dark maze, I couldn't help but become mesmerized by the abysmal magnificience of the sewer system."
        'Every now and then, I saw festering corpses captured in haunting stillness.'
    "Adventurers who had made their perilous descent in search of fame or ancient treasure,"
    "...miscreants who had accumulated enough resentment up in the city, lowlifes and refugees seeking shelter from whatever accursed path their lives had ended up on."
    "This far down, little to no light reached to illuminate their motionless agony of untimely demise."
    $ TimeAdvBy(TIME_1H)
    if GetPartySize() > 1:
        "Navigating these putrid halls of decay for what felt like an eternity, we were eventually welcomed by a deafening screech..."
    else:
        "Navigating these putrid halls of decay for what felt like an eternity, I was eventually welcomed by a deafening screech..."
    scene pbat_sewer
    show mc at left
    with dissolve
    if GetPartySize() > 1:
        MC "That must be our contract."
    "For a moment, my torch had carved out a silhouette in the dark tunnels ahead."
    "A hideous creature the size of a bull scurried across the tunnel with otherworldly swiftness and disappeared amidst rusty, moss-covered drain pipes."
    "There, focusing my gaze, I saw it in all its repulsive glory: an enormous white rat, its numerous red eyes twitching chaotically before fixing on me..."
    MC "What in the name of..."
    if GetPartySize() > 1:
        "In a screeching wave, group of smaller rats flooded our path."
    else:
        "In a screeching wave, group of smaller rats flooded my path."
    show mc at shake
    $ PlayMusicRandom("mus_battle_generic")
    MC "Shit!"
    MC "They're trying to protect their mother!"
    if GetPartySize() > 1:
        MC "To arms!"
    scene black with dissolve
    play sound2 "audio/cfx/transform.ogg"

    $ TransformMC(True)
    $ TransformMarkus(True)
     
    $ StartBattle(BattleData(BackgroundImage = "pbat_sewer", CharIDList_Right = ["e_crazy_rat", "e_crazy_rat", "e_crazy_rat"]))

    scene pbat_sewer
    show mc_transformed at cleft
    with dissolve
    if GetPartySize() > 1:
        MC "After it! Its getting away!"
    else:
        "Carving my way through hideous rodents, I saw their 'mother' scurrying away."
        MC "{i}You're not getting away from me.{/i}"
    hide mc_transformed with easeoutright
    scene black with dissolve
    if GetPartySize() > 1:
        'Tearing our way through the ocean of rats, we gave chase to the great behemoth.'
        'Eventually, we found our way to its lair.'
        scene cg_ratmother with dissolve
        'Piles upon piles of bones and rotten corpses littered around, the scent so strong they could make a normal man pass out.'
        'The great rat snarled and hissed at us from its throne of bones, bellowing out as its children came rushing out of every crevice to protect her.'
    else:
        'I chased the great behemoth to what seemed to be its lair.'
        scene cg_ratmother with dissolve
        'Piles upon piles of bones and rotten corpses littered around, the scent so strong they could make a normal man pass out.'
        'The great rat snarled and hissed at me from its throne of bones, bellowing out as its children came rushing out of every crevice to protect her.'
    scene pbat_sewer
    show mc_transformed at cleft
    with dissolve
    $ QstSetProgress(QstGuildBehemoth, 1)
    if GetPartySize() > 1:
        MC "The rest of you hold off the rats!"
        MC "{i}I'll take the queen!{/i}"
    else:
        MC "Let's end this now!"
    "As I charged at the great rat, it hissed and leapt down to face me!"
    $ StartBattle(BattleData(BackgroundImage = "pbat_sewer", CharIDList_Right = ["e_crazy_rat", "e_crazy_rat_mother", "e_crazy_rat"]))
    "The great behemoth committed itself to one last desperate charge towards me."
    "With one great swipe of my tail, I dropped the thing sliding lifelessly across the floor."
    "Its head rolled off to the side somewhere with a thud."
    "Seeing what had happened to their 'mother,' the rats screamed and scurried off through the dark holes they came from."
    scene pbat_sewer
    show mc_transformed at cleft
    with dissolve
    MC "{i}*Huff* *Huff...*{/i}"
    MC "Fucking rats ...!"
    $ PlayMusic("audio/music/15_Experiments.ogg")
    if CharInParty("elena"):
        ELENA @shock "Eww! I think I stepped on ones eye!"
    if CharInParty("markus"):
        MARKUS "Why can't you pick a quest where we investigate a brothel or something? Why does every quest need to involve horrifying monsters?"
    if CharInParty("myu"):
        MYU @scared "Myu want go now ... Dark place scary."
    if GetPartySize() > 1:
        MC "Lets just take some proof and bring it back to the guild!"
        MC "I don't want to spend a minute down here longer than I have to ..."
    else:
        "I've found the mother rat's head and grabbed it, still warm, as a proof."
        MC "Time to leave this place, hopefully for good."
    hide mc_transformed with easeoutright
    scene black with dissolve
    $ QstSetProgress(QstGuildBehemoth, 2)
    $ TransformMC(False)
    $ TransformMarkus(False)
    $ TimeAdvBy(TIME_1H)
    $ LocNameReset()
    $ AutoMus(True)
    if GetPartySize() > 1:
        "...We returned to the guild and were met by a thunderous applause."
        "Guild members raised glasses in our name."
    else:
        "...I returned to the guild and was met by a thunderous applause."
        "Guild members raised glasses in my name."
    $ LocFlush()
    show mc at cleft
    with dissolve
    "A cheerful Thea approached with a cup in her hand."
    show thea at cright_f with easeinright
    THEA @smile "Congratulations!"
    THEA @smile "You made it to C-tier!"
    if GetPartySize() > 1:
        THEA @smile "Welcome to the real deal, Seasoned Adventurers!"
    else:
        THEA @smile "Welcome to the real deal, Seasoned Adventurer!"
    show thea at center_f with easeinright
    THEA @smile2 "Maybe when you get a chance ... We could talk a little more in {i}private{/i} when you're done celebrating."
    MC @smile "I'll keep that in mind."
    scene black with dissolve
    $ QstComplete(QstGuildBehemoth)
    if GetPartySize() > 1:
        "As Thea hurried off to fetch more drinks for a rowdy table, we were swamped by various adventurers asking us to recount every vivid detail of what went down."
    else:
        "As Thea hurried off to fetch more drinks for a rowdy table, I was swamped by various adventurers asking me to recount every vivid detail of what went down."
    $ LocSet("novaras_adv_guild")
    $ LocEnter()