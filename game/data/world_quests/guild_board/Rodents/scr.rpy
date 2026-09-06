label qst_guild_rodents:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusic("audio/music/15_Experiments.ogg")
    $ TimeAdvBy(TIME_1H)
    if GetPartySize() > 1:
        "...After putting our names down on the sheet, we made our way down into the darkness of the sewers and traversed deeper with torches lit."
        $ LocNameSetTemp(_("Novaras Sewers"))
        scene pbat_sewer
        show mc at left
        with dissolve
        "We walked alongside the stagnant waters which flowed quietly through the main grates of the complex network of tunnels beneath Novaras."
        "Every now and then, we heard the scurrying of feet as shadows moved across the walls fleeing from the light."
        "The wretched smell of rotting flesh grew stronger and stronger, the repulsive scent almost forcing me to hurl from its stench."
        "Finally, as we turned one of the corners, we were confronted by the hideous sight of a mound of corpses, festering and rotting as one of the large rats dragged by it's teeth a corpse to add to the pile."
        "The dozens of rats feasting and gnawing at the flesh, turned their heads to look up towards us and snarled."
    else:
        "...After putting my name down on the sheet, I made my way down into the darkness of the sewers and traversed deeper with torches lit."
        $ LocNameSetTemp(_("Novaras Sewers"))
        scene pbat_sewer with dissolve
        show mc at left
        with dissolve
        "I walked alongside the stagnant waters which flowed quietly through the main grates of the complex network of tunnels beneath Novaras."
        "Every now and then, I heard the scurrying of feet as shadows moved across the walls fleeing from the light."
        "The wretched smell of rotting flesh grew stronger and stronger, the repulsive scent almost forcing me to hurl from its stench."
        "Finally, as I turned one of the corners, I was confronted by the hideous sight of a mound of corpses, festering and rotting as one of the large rats dragged by it's teeth a corpse to add to the pile."
        "The dozens of rats feasting and gnawing at the flesh, turned their heads to look up towards me and snarled."    
    $ PlayMusicRandom("mus_battle_generic")
    if CharInParty("elena"):
        show elena at center with easeinleft
        ELENA @shock "Oh gods ..." 
        ELENA @shock "There's so many of them!"
        hide elena with easeoutright
    if CharInParty("myu"):
        show cg_myu_monster at center with easeinleft
        MYU @scared "M-Myu!"
        hide cg_myu_monster with easeoutright
    if CharInParty("markus"):
        show markus_transformed at center with easeinleft
        MARKUS "[player_name!t]!"
        hide markus_transformed with easeoutright
    $ QstSetProgress(QstGuildRodents, 1)
    MC "(Fuck!)"
    if GetPartySize() > 1:
        MC "STAND READY TO FIGHT!"
    scene black with dissolve
    play sound2 "audio/cfx/transform.ogg"
    $ TransformMC(True)
    $ TransformMarkus(True)
     
    $ StartBattle(BattleData(BackgroundImage = "pbat_sewer", CharIDList_Right = ["e_crazy_rat", "e_crazy_rat", "e_crazy_rat", "e_crazy_rat"]))

    "Atop their slain kins corpses, more clambered their way towards us, frothing at the mouth."
    scene pbat_sewer
    show mc_transformed at left
    with dissolve
    MC "(They just keep coming!)"
     
    $ StartBattle(BattleData(BackgroundImage = "pbat_sewer", CharIDList_Right = ["e_crazy_rat", "e_crazy_rat", "e_crazy_rat", "e_crazy_rat"]))

    "The sewer became a haze of red and blood as I tore my way through dozens more of the creatures."
    scene pbat_sewer
    show mc_transformed at left
    with dissolve
    "The red mist enveloped me as the rage swept over, digging my hands into the guts of one of the creatures before tearing it in two."
    if CharInParty("elena"):
        show elena at cleft with easeinleft
        ELENA @shock "How many more of them are there?!"
        hide elena with easeoutright
    if CharInParty("markus"):
        show markus_transformed at center with easeinleft
        MARKUS @angry "Grghh! Burn! FUCKING BURN YOU RODENT FUCKS!"
        hide markus with easeoutright
    scene black with dissolve
    "The next wave came hurtling over, leaping onto me where they gnashed and mauled trying to force their way through my armor."
     
    $ StartBattle(BattleData(BackgroundImage = "pbat_sewer", CharIDList_Right = ["e_crazy_rat", "e_crazy_rat", "e_crazy_rat", "e_crazy_rat"]))

    "Throwing them off me, I stomped down on one beneath my feet, crushing its skull before I saw once again, another wave charging towards us..."
    if GetPartySize() > 1:
        MC "They're thinning out! Just a little more!"
     
    $ StartBattle(BattleData(BackgroundImage = "pbat_sewer", CharIDList_Right = ["e_crazy_rat", "e_crazy_rat", "e_crazy_rat", "e_crazy_rat"]))

    "Slaying the last of this wave, the remaining rats turned and fled deeper into the darkness of the sewers."
    $ QstSetProgress(QstGuildRodents, 2)
    scene pbat_sewer
    show mc_transformed at left
    with dissolve
    MC "{i}*Huff* *Huff*{/i}"
    MC "(I thought they'd never stop coming...)"
    if CharInParty("markus"):
        show markus_transformed at center with easeinleft
        MARKUS "Well, job well done I guess." 
        MARKUS @shock "Now can we get out of here now before they decide they'd like to give eating us another go?"
        hide markus_transformed with easeoutright
    if CharInParty("myu"):
        show myu at cleft with easeinleft
        MYU @scared "Myu isn't very tasty!"
        hide myu with easeoutright
    if GetPartySize() > 1:
        MC "Let's take a head or two for proof and be done with this quest already!"
    scene black with dissolve
    $ TransformMC(False)
    $ TransformMarkus(False)
    $ AutoMus(True)
    $ LocNameReset()
    $ TimeAdvBy(TIME_1H)
    if GetPartySize() > 1:
        "Shortly after, exhausted from the gruelling experience, we made our way back to the surface and after presenting a few heads of the rats, took our reward."
    else:
        "Shortly after, exhausted from the gruelling experience, I made my way back to the surface and after presenting a few heads of the rats, took my reward."
    $ QstComplete(QstGuildRodents)
    $ LocEnter()
