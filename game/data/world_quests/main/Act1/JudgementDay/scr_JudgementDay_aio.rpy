label qst_JudgementDay_SiegeStart:
    # these commands can actually be dupes, from prev. quest
    # just so that we dont lose track of all the shit
    # and to jump in here via another outcome (timeout)
    scene black with dissolve
    $ LocNameSetTemp(STR_LOC.NOV_CITY)
    $ InfGainDaily(False)
    $ BlockWaitGlobal(True)
    $ AutoMus(False)
    $ AutoAmb(False)
    $ AutoTimeFreeze(True)
    $ TimeAdvTo(TIME_NOON)
    stop music fadeout 1.0
    $ Pause(1.25)
    $ PlayMusic("audio/music/46_Siege_Theme.ogg")
    play ambience "audio/ambience_scenes/battle_cave.ogg" fadein 1.0

    "... The bells rang that day as panic filled the streets of Novaras."
    scene cg_novaras_siege_attack with dissolve
    "The sky turned a red crimson as the dark forces of the Demorai marched to the beat of thousands of war drums that could be heard for miles around."
    "As the Demorai forces slammed against the walls with great catapults and scorched beasts, the Alderian men stationed valiantly fought back."
    "The Demorai had yet to breach the walls, yet from the sheer volume of men heading up towards the top of the great walls of Novaras, and from the screams above and sounds of bolts firing and blades clashing, the battle was an intense one."
    "Every now and then, a loud scream rang out followed by a sharp thud as one of the men high up on the wall fell, coming sharply crashing into the ground and reduced to bloody piles of gore."

    $ LocNameSetTemp(STR_LOC.NOV_DIST_PLEASURE)
    scene nov_district_pleasure_siege
    show mc at cleft
    with dissolve

    show cg_guard at cright_f with easeinright
    GUARD "Captain Nyx has sent me to escort you to her at once!"
    $ GoalShow(QstJudgementDay, 100)
    MC @serious "Lead the way."
    scene black with dissolve
    $ Pause(0.5)
    $ LocNameSetTemp(STR_LOC.NOV_DIST_ARMY)

    $ CharSetClothes("nyx", "normal_ash")
    scene nov_district_army_siege
    show nyx angry at cright_f
    with dissolve

    show mc at cleft with easeinleft
    show cg_guard at left with easeinleft

    MC @surprised "Captain Nyx!"
    show cg_guard at blurin, left_f
    hide cg_guard with easeoutleft
    MC @surprised "What's the situation?"
    NYX @angry "The Demorai force is even larger in scale than we anticipated."

    if QstJudgementDay().PlayerPrepared:
        MC @serious "What about those hives? Have you-"
        NYX @angry "I managed to pull more guards to defend the city, but the inquisitors continued to block searches for more of those foul beasts' nests."
        MC @angry "What about Markus? Where is-"
    else:
        show nyx at shake
        NYX @angry "I need you with me, damn it!"
        MC @angry "Where is Markus? I haven't seen him since the—"

    if QstJudgementDay().PlayerPrepared:
        show nyx at shake
        NYX @angry "[player_name!t]!"
        NYX @angry "I need you to focus and listen to me."
    else:
        show nyx at shake
        NYX @angry "Markus is fine!"
        NYX @angry "I gave him his orders, and now I'm giving you yours!"

    if QstJudgementDay().PlayerPrepared:
        NYX @angry "Head to the Market District."
        NYX @angry "There are reports that people have begun to gather there, and I need you to break up the crowd!"
        $ GoalShow(QstJudgementDay, 10)
        NYX @shock "You need to tell them to go home at once!"
        NYX @shock "It's a fucking slaughter ground to have that many people standing out in the open!"
        MC @angry "What about the inquisitors?"
        NYX @angry "FUCK. THE FUCKING. INQUISITORS."
        NYX @angry "Just go! I need YOU, damn it!"
    else:
        MC @angry "Why in the hells are they just standing around outside?"
        NYX @angry "Fuck if I know! NOW GO!" 
    #
    show nyx at cright
    hide nyx with easeoutright
    "A group of other guards were already escorting Captain Nyx off to deal with some other urgent matter, shoving scrolls and maps in her face."
    show mc at center with ease
    MC "(The Market District... I better head over there at once.)"

    if QstJudgementDay().PlayerPrepared:
        MC "(Markus... Where are you?)"
    else:
        MC "(I hope Markus is okay... wherever he is.)" 

    scene black with dissolve
    $ Pause(0.25)
    $ LocNameSetTemp(STR_LOC.NOV_DIST_MARKET)
    scene nov_district_market_siege with dissolve
    show mc at cright_f with easeinright
    "At the Market District, more and more people seemed to be gathering and huddling together to listen."
    "A loud voice was talking over the murmuring of the crowd, but it was difficult to hear what was being said."
    show mc at shake
    MC "(What in the damn hells is going on here?)"
    hide mc with easeoutleft
    "Making my way through the packed crowds, I arrived upon the makeshift stage by which the mad preacher's voice bellowed."
    show cg_prophet with dissolve
    $ Pause()
    MAD_PROPHET "AS I FORETOLD LONG AGO, THE GREAT NEWHEART WILL RETURN TO US IN OUR DARKEST HOUR OF NEED WHEN THE SKIES TURN RED AND THE STREETS FILL WITH BLOOD!"
    MAD_PROPHET "IN THIS DARKEST HOUR, WE MUST NOT SHOW FEAR!"
    MAD_PROPHET "WE MUST GATHER TO OFFER PRAISE TO THE NEW GODS FOR RESTORING OUR GREAT HERO!"
    "As the madman continued his speech, more and more people began to gather, crying tears of joy, clapping and cheering in the streets."
    play sound "audio/cfx/explosion.ogg"
    show cg_prophet at shake
    "From behind, a fiery ball launched from a catapult slammed into one of the buildings, erupting into a ball of fire and black smoke."
    "For a few moments, the crowd gasped in shock as the spell on them was shaken."
    MAD_PROPHET "CALM YOURSELVES! DON'T LET YOUR FAITH BE SHAKEN!"
    MAD_PROPHET "JOIN ME IN PRAYER AND WORSHIP!"
    "Angrily, I forced my way onto the stage, the crowd briefly turning their attention to me."

    show mc at cleft with easeinleft
    show mc at shake

    MC @surprised "THIS IS MADNESS! ALL OF YOU MUST GO HOME! BOARD UP YOUR WINDOWS AND DOORS AT ONCE!"
    MAD_PROPHET "BEGONE, DECEIVER! OUR FAITH WILL NOT BE SHAKEN!"
    MC @angry "Newheart is dead, you fools! YOU'RE STANDING OUT IN THE OPEN FOR DEMORAI ARTILLERY!"
    "For a moment, the people once again seemed to chat amongst themselves in murmured confusion as fear began to work its way through the rows."

    show cg_prophet at shake

    MAD_PROPHET "DO NOT LET YOUR HEARTS BE TAINTED BY FEAR!"
    MAD_PROPHET "YOU HAVE ALL BEEN GATHERED HERE FOR A REASON!"
    MAD_PROPHET "SEVERAL MOONS AGO, A PALE GOD CAME TO VISIT ME IN THE FLESH WITH HIS DISCIPLES!"
    MAD_PROPHET "HE PROMISED THAT THE GREAT NEWHEART REBORN WOULD REVEAL HIMSELF TO US ONCE WE HAD GATHERED HERE!"
    MC @surprised "(A pale... god?)"
    MAD_PROPHET "JOIN ME IN PRAYER, BROTHERS AND SISTERS!"
    MAD_PROPHET "THE HOUR OF OUR GREAT HERO'S REBIRTH IS UPON US!"
    MAD_PROPHET "THE GODS STILL BLESS US, THEIR MOST FAVORED WORSHIPPERS!"
    "Looking across the sea of people, I noticed large, clumsy, hulking masses of guards stumbling their way towards the huge crowd, surrounding them."
    show mc at left with ease
    show cg_guard_rot onlayer characters as guard1 at right_f with easeinright
    show cg_guard_rot onlayer characters as guard2 at cright_f with easeinright
    if QstJudgementDay().PlayerPrepared:
        "As I looked closer at the disheveled, ghastly-looking figures approaching, the terrible truth hit me."
        MC "(...Oh gods.)"
        BLACK "{i}TRAP.{/i}"
        MC @surprised "RUN! ALL OF YOU! RUN BEFORE IT'S TOO LATE!"
        MC @surprised "THEY'RE NOT GUARDS! THEY'RE-"
        MAD_PROPHET "DO NOT LET YOUR FAITH WILT, MY TRUE BELIEVERS!"
        "At last, shambling within range of the crowd and fully circling the people, the guards began to shake violently in a spasm."
        "The crowd, noticing the strange scene occurring, turned towards the shaking guards."
        "One curious boy stepped out closer towards them."
    else:
        "As I looked closer at the disheveled, ghastly-looking figures approaching, something felt... {i}off.{/i}"
        BLACK "({i}DANGER.{/i})"
        MC "(What? What are you talking about?)"
        BLACK "({i}I sense predators all around us.{/i})"
        MC "(What?)"
        "I looked once more toward the guards who were making their way toward us."
        "There was something strange in the way they shuffled closer, as though they were drunk."
        "And yet, something felt wrong... {i}something felt very wrong.{/i}"
        MC "(...The guards, what are they—)"
        "A sudden, dreadful chill rushed through me, the hairs on my arms standing up."

    #
    show mc at shake
    MC @surprised "GET AWAY FROM THEM!"
    scene black with dissolve
    "As the child stopped in his tracks, he looked back at me for a moment in hesitation, ready to turn back."
    "But before he could, springing from the bloody chest of one of the guards, a pale ghoul slashed at the boy's throat."
    play sound "audio/cfx/prologue_guysnap.ogg"
    "The boy's parents, alongside the now panicking crowd, began to scream and try to flee, but most of them found themselves running straight into the path of more ghouls."
    scene cg_novaras_siege_prophet_dead with dissolve
    $ Pause()
    MAD_PROPHET "STOP! THIS WASN'T SUPPOSED TO HAPPEN!"
    MAD_PROPHET "NEWHEART WILL COME TO-"
    "A ghoul charged onto the stage, and with one sudden swipe of its vicious claws, disemboweled the mad preacher."
    "With a sharp, breathless cry, he dropped to his knees, desperate to push his guts back into his stomach futilely."
    MAD_PROPHET "N-Noo, God! Why have you..."
    MAD_PROPHET "Forsaken us?"
    "With a thud, the mad preacher's head hit the ground, his lifeless eyes staring blankly ahead."
    scene cg_novaras_siege_ghoul_attack with dissolve
    "I reached for my sword as the ghouls moved through the crowd, tearing people limb from limb as the streets ran red with blood."
    MC @angry "(There's too many of them for just my blade!)"
    scene nov_district_market_siege
    show mc at left
    show cg_ghoul at right_f as ghoul1
    with dissolve
    show cg_ghoul at cright_f as ghoul2 with easeinright
    MC @angry "(But... There's so many eyes! If I change-)"
    scene black with dissolve
    "A small child, cowering in her mother's arms, screamed as one of the ghoulish creatures, claws raised, prepared to slash them down."
    play sound "audio/battle/battle_chars/mc_transformed/basic_attack/impact1.ogg"
    play sound2 "audio/cfx/transform.ogg"
    "...As the little girl closed her eyes and waited for the death blow, she must have heard the sound of something razor-sharp, but when no pain came,"
    scene nov_district_market_siege
    show mc_transformed at cleft
    show cg_ghoul at right_f
    with dissolve
    "Her eyes opened to see the hulking tentacle monster in front of her, cutting down the ghoulish beasts!"
    show mc_transformed at shake
    BLACK "{i}Go. Now!{/i}"
    "The little girl, staring in awe, was pulled by her terrified mother as they fled, while the ghouls now turned their attention toward me."
    show mc_transformed at blurin, shake
    play sound2 "audio/battle/battle_chars/mc_transformed/skill_terrifyingscream.ogg" volume 0.9
    "With my blades at the ready, I snarled and roared at the ghoulish monstrosities."

    if QstTheComingStorm().PoltrikEstateLeftPlayerPartyChars == {"markus"}:
        pass
    else:
        if "elena" in QstTheComingStorm().PoltrikEstateLeftPlayerPartyChars:
            $ TransformElena(True)
            show elena_w at center with easeinleft
            "...Just then, before they could set upon me, a blue wolf came charging in to tackle one of the beasts."
            MC "ELENA!"
            "Having knocked the thing back with her body and managing to tear a chunk from one of the creature's hands, she barked defiantly!"
            show elena_w at shake
            ELENA "{i}*BARK!*{/i}"
            $ CharHeal("elena")
            $ PartyAddChar("elena")

        if "myu" in QstTheComingStorm().PoltrikEstateLeftPlayerPartyChars:
            "Suddenly feeling a wetness on my foot, I looked down to see a blue slime slithering past, before rising up to take her full form."
            show cg_myu_monster_blood at left with dissolve
            MYU @angry "B-Bad monsters everywhere!"
            $ CharHeal("myu")
            $ PartyAddChar("myu")

    scene black with dissolve
    if GetPartySize() > 1:
        "Before I could say another word, the ghouls lunged towards us!" 
    else:
        "The remaining ghouls lunged towards me!"

    $ tmpvar = [{"e_ghoul":3}, {"e_ghoul":4}]
    
    if GetPartySize() >= 2:
        $ tmpvar.append({"e_ghoul":5})
    if GetPartySize() >= 3:
        $ tmpvar.append({"e_ghoul":4})
    
    $ renpy.random.shuffle(tmpvar)

    $ PlayMusicRandom("mus_battle_generic")
    $ TransformMC(True)
    $ StartBattle(BattleData(BackgroundImage = "pbat_novaras_alley_fire", CharIDList_Right = tmpvar, CanTransform = False))
    
    scene nov_district_market_siege
    show mc_transformed at center
    with dissolve

    "... As the last of the foul things fell, I looked around at the bloody massacre surrounding me."
    $ GoalComplete(QstJudgementDay, 10)
    $ PlayMusic("audio/music/46_Siege_Theme.ogg")

    "The city was aflame, those things no doubt springing up all across the damn place."
    MC @serious "Markus... I need to find him!"
    if CharInParty("myu"):
        show myu at left with easeinleft
        MYU @sad "M-Myu!"
        show mc_transformed at blurin, center_f
        MC "Myu! Markus—have you seen him?"
        "Myu shook her head."
        MYU @scared "M-Myu scared... Lots of monsters everywhere!"
        hide myu with dissolve
        show mc_transformed at blurin, center

    if CharInParty("elena"):
        ELENA "{i}*BARK!*{/i}"

    MC "(Markus has to be somewhere...)"
    MC "(But where?)"
    $ GoalShow(QstJudgementDay, 20)
    $ Pause(0.2)
    hide mc_transformed with easeoutright
    scene black with dissolve
    $ LocNameSetTemp(STR_LOC.NOV_DIST_PLEASURE)

#######################################################
    scene nov_district_pleasure_siege
    show cg_ghoul at cright
    with dissolve 
    "The streets were awash with blood."
    show cg_ghoul at shake
    "The usual laughter and promise of a good time had been replaced only with screams and cries as bodies littered the cobblestone roads."
    show mc_transformed at left with easeinleft
    "I watched as one of those things held a dead woman in its arms, the huge bloody gash in her stomach having drained the color completely from her body."
    show cg_ghoul at blurin, cright_f
    "Taking a bite, the creature tore away at some of the flesh before looking up towards me and snarling."
    $ CharSetClothes("shani", "normal_ash")
    if QstJudgementDay().PlayerPrepared:
        jump qst_JudgementDay_Siege_ShaniScene_Prepared
    else:
        jump qst_JudgementDay_Siege_ShaniScene_Unprepared

# player prepared
label qst_JudgementDay_Siege_ShaniScene_Prepared:
    hide mc_transformed
    hide cg_ghoul
    with dissolve
    show shani at cright 
    show cg_ghoul at cleft
    with dissolve
    if CharIsMet("shani"):
        "As I readied my claws, my eyes darted up to see a familiar face—Shani, fleeing for her life as one of those things chased her down on all fours!" 
        show shani at shake
        SHANI "AHHHHHHHHH!"
        MC "(DAMN HELLS!)"
        MC "(There's no way I can reach her in time!)"
    else:
        "As I readied my claws, my eyes darted up to see a woman fleeing for her life as one of those things chased her down on all fours!" 
        show shani at shake
        WOMAN "AHHHHHHHHH!"
        MC "(DAMN HELLS!)"
        MC "(There's no way I can reach her in time!)"

    # if player managed to save alysha, use variant 1 below
    # else if alysha aint saved, use variant 2 (with shani dying)
    # variant 1, alysha saved during slavemaster quest
    if QstIsOver(QstTheSlavemaster) and not QstTheSlavemaster().AlyshaDead:
        $ ALYSHA = Character(_("Alysha"), image = "alysha_warrior")
        show alysha_warrior at center_f with easeinright
        "Just then, before the killing blow could land, a recognizable face appeared, swinging a blade that slashed at the beast with a wild, desperate strike!"
        show alysha_warrior at shake
        play sound "audio/cfx/knife_slice.ogg"
        ALYSHA "G-GET BACK!"
        show cg_ghoul at left with ease
        "Her sudden attack caught the beast off guard, the blade cutting across its face and slashing through one of its eyes."
        "The creature shrieked in pain, clutching at the bloody wound as it stumbled back."
        MC "(Alysha?!)"
        $ CharMeet("alysha")
        if CharIsMet("shani"):
            "Shani, wide-eyed and terrified, stared up from the ground at the shaking knight before her."
        else:
            "The woman, wide-eyed and terrified, stared up from the ground at the shaking knight before her."
        ALYSHA "G-GO!"
        ALYSHA "RUN, NOW!"
        hide shani with easeoutright
        if CharIsMet("shani"):
            "Shani scrambled to her feet and sprinted away from the carnage around us."
        else:
            "She scrambled to her feet and sprinted away from the carnage around us."
        hide alysha_warrior
        hide cg_ghoul 
        with dissolve
        show mc_transformed at left
        show cg_ghoul at right_f
        with dissolve
        show cg_ghoul at center with ease
        "Before I could help Alysha, the circling skinwalkers turned their attention to me, lunging forward!"
        show cg_ghoul at shake
        $ tmpvar = [{"e_ghoul":3}, {"e_ghoul":4}]
        if GetPartySize() >= 2:
            $ tmpvar.append({"e_ghoul":5})
        if GetPartySize() >= 3:
            $ tmpvar.append({"e_ghoul":4})
        $ renpy.random.shuffle(tmpvar)
        $ StartBattle(BattleData(BackgroundImage = "pbat_novaras_alley_fire", CharIDList_Right = tmpvar, CanTransform = False))
        "Having slain the last of them, I turned at the sound of a bloodcurdling scream."
        scene nov_district_pleasure_siege
        show cg_alysha_war_no_hand at cleft
        show cg_ghoul at cright_f
        with dissolve
        "Alysha's blade clattered to the floor, her eyes wide as she looked down at the bloody stump where her hand had once been."
        "With tears in her eyes, she collapsed to the ground, clutching at the wound as one of the things moved to finish her off."
        play sound "audio/battle/battle_chars/mc_transformed/char/skilluse5.ogg" volume 0.7
        play sound2 "audio/battle/battle_chars/mc_transformed/basic_attack/impact5.ogg" volume 0.7
        show cg_ghoul at shake
        "With a swipe of my tail, the creature halted mid-strike."
        "Alysha braced herself, expecting the killing blow—but it never came."
        hide cg_ghoul with moveoutbottom
        "Instead, the thing's head rolled across the floor, its lifeless body slumping down next to her."
        show mc_transformed at cright_f with easeinright
        "In a panic, Alysha tried to crawl away, her breath ragged, her body trembling."
        MC "Wait!"
        show cg_alysha_war_no_hand at shake
        ALYSHA "Get back! GET BACK, YOU FUCKING MONSTER!"
        show mc_transformed at center_f with easeinright
        "I instinctively reached for her bleeding stump, my grip firm as she struggled to break free."
        show cg_alysha_war_no_hand at shake
        ALYSHA "LET GO OF ME!"
        "From my palm, the smallest of worm-like creatures slithered onto her wound, sealing it shut within moments."
        
        hide cg_alysha_war_no_hand
        show cg_alysha_war_no_hand2 at cleft 
        with dissolve
        show mc_transformed at cright_f with ease
        "She gasped, eyes locked onto the now-healed wound in confusion and fear."
        ALYSHA "Who... Who are you?"
        MC "Can you still fight with your other hand?"
        show cg_alysha_war_no_hand2 at nod
        "Alysha nodded weakly."
        ALYSHA "I... I'm not as good with this one!"
        ALYSHA "Oh gods... My hand!"
        show mc_transformed at shake
        MC "Focus!"
        MC "The other guards! Where are they?"
        ALYSHA "They... We were ambushed near the academies!"
        ALYSHA "I barely made it out alive!"
        MC "The rest of your men?"
        ALYSHA "Scattered... Some retreated and fled to join the others at the farmlands district!"
        ALYSHA "The students living in the halls... they were running for their lives!"
        MC "Head toward the castle."
        MC "The guards have managed to hold the line on the bridge!"

        ALYSHA "W-Wait!"
        ALYSHA "...W-What are you?"
        ALYSHA "Why do I feel like we've met before?"
        show mc_transformed at shake
        MC "...Go. Now!"
        "Alysha hesitated but grabbed her blade from the ground and hurried to safety."
        show cg_alysha_war_no_hand2 at blurin, cleft_f
        $ Pause(0.25)
        hide cg_alysha_war_no_hand2 with easeoutleft
        $ Pause(0.25)
        show mc_transformed at center_f with ease
        MC "(That girl... When did she join the city guard?)"
        MC "(No time to think on it now, I must keep moving!)"

    # quest was never completed OR it was completed but alysha was not saved
    elif (QstIsOver(QstTheSlavemaster) and QstTheSlavemaster().AlyshaDead) or not QstIsOver(QstTheSlavemaster):
        $ CharKill("shani")
        $ CharAddRelEntry("shani", "died_during_siege")
        $ QstComplete(DialogueShani)
        scene cg_shani_dead_ghoul with flash
        if CharIsMet("shani"):
            "As the creature's claws slashed across Shani's throat, a spray of crimson painted the ground."
        else:
            "As the creature's claws slashed across the woman's throat, a spray of crimson painted the ground."
        
        play sound "audio/battle/battle_chars/ves/BasicAttackImpact.ogg"
        "Her eyes went wide, hands trembling as they clutched at the open wound, desperate to keep the life from pouring out."
        "She choked, spasmed, convulsed in agony."
        if CharIsMet("shani"):
            # if know shani
            MC "SHANI!"
        "Before I could reach her, the circling skinwalkers pounced on me!"
        
        $ tmpvar = [{"e_ghoul":3}, {"e_ghoul":4}]
    
        if GetPartySize() >= 2:
            $ tmpvar.append({"e_ghoul":5})
        if GetPartySize() >= 3:
            $ tmpvar.append({"e_ghoul":4})
        
        $ renpy.random.shuffle(tmpvar)

        $ PlayMusicRandom("mus_battle_generic")
        $ StartBattle(BattleData(BackgroundImage = "pbat_novaras_alley_fire", CharIDList_Right = tmpvar, CanTransform = False))
    
        scene nov_district_pleasure_siege
        show mc_transformed at cleft
        with dissolve
        $ PlayMusic("audio/music/46_Siege_Theme.ogg")

        if CharIsMet("shani"):
            "As the last of them collapsed into a heap of blood and gore, I turned my gaze back toward Shani."
        else:
            "As the last of them collapsed into a heap of blood and gore, I turned my gaze back towards the woman."

        show cg_ghoul at cright with dissolve
        "There, hunched over her lifeless body, that thing gnawed at her flesh."

        play sound "audio/battle/battle_chars/mc_transformed/char/skilluse5.ogg" volume 0.7
        play sound2 "audio/battle/battle_chars/mc_transformed/basic_attack/impact5.ogg" volume 0.7
        show mc_transformed at center with ease
        show cg_ghoul at shake

        "Enraged, I lunged forward with a guttural snarl, my blade flashing as I took the thing's head clean off."
        
        hide cg_ghoul with moveoutbottom
       
        if CharIsMet("shani"):
            "The lifeless body slumped to the floor, and I stared at the silent, bloody mess that had once been Shani."

        MC "(These bastards are going to pay for what they've done!)"
    
    $ Pause(0.25)
    scene black with dissolve
    $ CharSetClothes("shani", "normal")
    jump qst_JudgementDay_GoToEduDistrict

# player unprepared
label qst_JudgementDay_Siege_ShaniScene_Unprepared:
    $ CharKill("shani")
    $ CharAddRelEntry("shani", "died_during_siege")
    $ QstComplete(DialogueShani)

    if CharIsMet("shani"):
        scene cg_shani_dead with flash
        "As I readied my claws, I looked up to see a familiar face—Shani—laid sprawled dead against a wall, her face completely torn off, with a large, red, gaping puncture wound in her chest."
        MC "(By the gods... What is this nightmare?)"
        MC "(Shani... I—)"
        "Before I could think, the circling skin-walkers pounced on me!"
    else:
        scene cg_shani_dead with flash
        "As I readied my claws, I looked up to see a woman laid sprawled dead against a wall, her face completely torn off, with a large, red, gaping puncture wound in her chest."
        MC "(By the gods... What is this nightmare?)"
        "Before I could think, the circling skin-walkers pounced on me!"


    $ tmpvar = [{"e_ghoul":3}, {"e_ghoul":4}]

    if GetPartySize() >= 2:
        $ tmpvar.append({"e_ghoul":5})
    if GetPartySize() >= 3:
        $ tmpvar.append({"e_ghoul":4})
    
    $ renpy.random.shuffle(tmpvar)


    $ PlayMusicRandom("mus_battle_generic")
    $ StartBattle(BattleData(BackgroundImage = "pbat_novaras_alley_fire", CharIDList_Right = tmpvar, CanTransform = False))

    scene nov_district_pleasure_siege
    show mc_transformed at center
    with dissolve
    $ PlayMusic("audio/music/46_Siege_Theme.ogg")
    $ Pause(0.5)
    play sound2 "audio/cfx/transform.ogg"
    show mc_transformed at blurin, shake
    MC "(These bastards are going to pay for what they've done!)"
    hide mc_transformed with easeoutright
    MC "(...If only I'd arrived sooner, if only I—)"
    $ Pause(0.25)
    scene black with dissolve
    jump qst_JudgementDay_GoToEduDistrict

##################################################
# Upon heading up to the government/school district (top left)
label qst_JudgementDay_GoToEduDistrict:
    $ LocNameSetTemp(STR_LOC.NOV_DIST_EDU)
    $ CharSetClothes("vala", "normal_ash")
    scene nov_district_education_siege with dissolve
    "The city continued to burn around me as panicked citizens fled for their lives."
    "Screams echoed from the streets as people were torn apart—limbs ripped from their sockets, throats gnashed by unrelenting teeth."
    "A voice called out amidst the chaos, and my eyes darted toward the library."
    show vala at cright_f with dissolve
    "Vala, the librarian, stood at the entrance, motioning desperately for people to hurry inside."
    show vala at shake
    VALA @scared "IN HERE! QUICKLY!"
    show cg_man_silh as citizen1 onlayer characters at left
    show cg_man_silh as citizen2 onlayer characters at cleft 
    with easeinleft
    #show 
    "A few scattered survivors rushed past her into the supposed safety of the library's thick walls."
    hide citizen1 onlayer characters 
    hide citizen2 onlayer characters 
    #hide citizen2 
    with easeoutright
    "But in doing so, they caught the attention of a pack of ghoulish creatures that lurched toward Vala, their eyes gleaming with hunger."
    show cg_ghoul as ghoul2 onlayer characters at cleft 
    show cg_ghoul as ghoul1 onlayer characters at left
    with easeinleft
    show vala at shake
    VALA @scared "A-Ahhh!"
    "Frantically, she tried to pull the heavy doors shut, but they refused to budge."
    show vala at shake
    VALA @scared "Come on! COME ON!"
    "As she struggled, the creatures inched closer, snarling, their claws poised to strike."
    "Her eyes went wide with terror as she braced herself for death."
    scene black with dissolve
    "And then—I was there."
    play sound2 "audio/cfx/transform.ogg"
    scene nov_district_education_siege
    show vala at right_f
    show mc_transformed at center_f
    show cg_ghoul at left
    with dissolve
    VALA @shock "W-Wha...?"
    show mc_transformed at shake
    MC "GET BACK!"
    "Vala, frozen between awe and terror, stumbled back as I lunged forward, my claws at the ready."

    $ tmpvar = [{"e_ghoul":3}, {"e_ghoul":4}]

    if GetPartySize() >= 2:
        $ tmpvar.append({"e_ghoul":5})
    if GetPartySize() >= 3:
        $ tmpvar.append({"e_ghoul":4})
    
    $ renpy.random.shuffle(tmpvar)

    $ PlayMusicRandom("mus_battle_generic")
    $ StartBattle(BattleData(BackgroundImage = "pbat_novaras_alley_fire", CharIDList_Right = tmpvar, CanTransform = False))
    $ PlayMusic("audio/music/46_Siege_Theme.ogg")
    scene nov_district_education_siege
    show mc_transformed at cleft
    show vala at cright_f
    with dissolve
    "As the last of their bloody bodies crumpled to the ground, I turned toward Vala."
    VALA @scared "You..."
    VALA @scared "{i}What are you?{/i}"
    MC "... Arm yourselves with whatever you can."
    MC "Wait for the guards!"
    show vala at right_f with ease
    show vala at nod
    "Vala nodded, still shaking, and as she stepped back she threw me something: a cloth wrap of vials."
    $ PlayerAddItem("potion_heal_large", Amount = 3)
    VALA @scared "T-Take these!"
    VALA @scared "Looks like you're going to need them more than I am!"
    hide vala with dissolve
    $ PlaySoundRandom("woodenDoor")
    "I nodded, accepting the vials, before sealing the door shut behind her."
    show mc_transformed at center with ease
    "The city burned, screams still echoing through the night."
    MC "(Markus... Where are you?)"
    scene black with dissolve
    $ CharSetClothes("vala", "normal")
    jump qst_JudgementDay_GoToFarmlandDistrict

############################################################################################################
# From here > the player heads to the farmland region
label qst_JudgementDay_GoToFarmlandDistrict:
    $ LocNameSetTemp(STR_LOC.NOV_DIST_FARM)
    scene nov_district_farmland_siege with dissolve
    "The farmlands were ablaze."
    "Cattle shrieked in agony, their burning forms stumbling through the smoke as both guards and farmers alike fought desperately with whatever they had—pitchforks, axes, makeshift weapons."

    if QstJudgementDay().PlayerPrepared == True:
        jump qst_TheJudgementDay_FarmlandDist_Prep
    else:
        jump qst_TheJudgementDay_FarmlandDist_Unprep

# If the player never met her, she's referred to as "the blacksmith's daughter."
label qst_TheJudgementDay_FarmlandDist_Prep:
    $ CharSetClothes("arlena", "normal_ash")
    show arlena at cright_f
    show cg_ghoul as ghoul1 at left
    with dissolve

    if CharIsMet("arlena"):
        "My gaze snapped toward the chaos, where I saw her—Arlena, hammer in hand, drenched in blood as she swung wildly at one of those {i}things{/i}."
    else:
        "My gaze snapped toward the chaos, where I saw a woman-the blacksmith's daughter, hammer in hand, drenched in blood as she swung wildly at one of those {i}things{/i}."

    if not CharIsMet("arlena"):
        $ ARLENA = Character(_("The blacksmith's daughter"), image = "arlena")

    show arlena at shake
    ARLENA "GET THE FUCK AWAY FROM US!"
    show cg_ghoul as ghoul1 at cleft with ease
    show mc_transformed at left with easeinleft
    play sound "audio/battle/battle_chars/mc_transformed/char/skilluse5.ogg" volume 0.7
    play sound2 "audio/battle/battle_chars/mc_transformed/basic_attack/impact5.ogg" volume 0.7
    show mc_transformed at shake
    hide ghoul1 with moveoutbottom
    "As the beast knocked her weapon aside, I lunged forward, grabbing its head in my clawed grip."
    "With a sickening crunch, its skull collapsed beneath my strength."
    if CharIsMet("arlena"):
        "Arlena gasped, stepping back in shock."
    else:
        "The woman gasped, stepping back in shock."
    show arlena at right_f with ease
    ARLENA @shock "F-Fuck...!"
    MC "Is your father safe?"
    ARLENA @shock "What? You can speak?!"
    show mc_transformed at shake
    MC "Your father!"
    ARLENA "One of those things slashed his arm, but he's fine!"
    GUARD "GET AWAY FROM THAT THING, WOMAN!"
    MC "(Shit!)"
    show mc_transformed at blurin, center_f with ease
    show cg_guard at left with easeinleft
    "As I turned, three guards stood before me, spears leveled, their eyes wide with terror."
    show cg_guard at shake
    GUARD "Move now, or I shall pierce you both!"
    ARLENA "Wait! This thing isn't one of—"
    SECOND_GUARD "Sir! I saw that thing killing one of those monsters!"
    show cg_guard at shake
    GUARD "I DON'T FUCKING CARE! THAT THING IS ALL TEETH AND CLAWS!"
    GUARD "KEEP THAT FUCKING WEAPON POINTED, SOLDIER!"
    ARLENA "I just said he saved me, damn it!"
    GUARD "WOMAN, GO INSIDE NOW BEFORE—"
    "Before he could finish, a monstrous shadow loomed over him."
    play sound "audio/cfx/explosion.ogg"
    scene nov_district_farmland_siege
    show cg_ghoul_red at cleft
    with dissolve
    "The abomination landed atop the guard, crushing him into a bloody pulp beneath its weight."
    GUARD "AHHHHGHGHHHH!"
    show cg_ghoul_red at shake
    "A second guard tried to run, but the beast caught him in one immense clawed hand."
    "He kicked and flailed, his screams echoing through the burning streets."
    scene cg_novaras_siege_red_ghoul
    with dissolve
    UNKNOWN "Hoho! Look at you!"
    UNKNOWN "Don't you worry! I have a safe place for all the little boys and girls to hide in!"
    "Cackling, the abomination dragged the writhing man towards the gaping maw in its stomach."
    play sound "audio/cfx/prologue_guysnap.ogg"
    GUARD "OH GODS! NO! LET ME GO! PLEASE! LET ME—GHFRGHHH!"
    play sound2 "audio/cfx/demorai_roar_med.ogg"
    "The creature's stomach-mouth clamped shut, blood spilling between jagged teeth as it swallowed him whole."
    UNKNOWN "Mhmmahaha! Ta-da!"
    UNKNOWN "What did you think of my trick?"
    if CharIsMet("arlena"):
        "Arlena gagged, turning away to retch."
    else:
        "The woman gagged, turning away to retch."
    ARLENA "What in the hells is that thing?"
    scene nov_district_farmland_siege
    show cg_ghoul_red at left
    show mc_transformed at right_f
    with dissolve
    UNKNOWN "The master is here! THE MASTER IS HERE!"
    UNKNOWN "How excited he is to meet you..."
    UNKNOWN "{i}Shyahtan!{/i}"
    stop music fadeout 0.1
    $ Pause(1.0)
    play sound "audio/cfx/detect_magic.ogg"
    scene cg_novaras_siege_shyahtan_flashback with flash
    MC "(I... What?)"
    "A sudden surge of memories rushed through me—memories that weren't my own."
    $ Pause()
    scene nov_district_farmland_siege
    show cg_ghoul_red at left
    show mc_transformed at right_f
    with dissolve
    MC "Grghhh! What in the hells was that?"
    UNKNOWN "Hohoho! Such a shame..."
    UNKNOWN "Now, hurry up and DIE so me and that pretty thing can get more acquainted!"

    $ tmpvar = [{"e_ghoul_red":6}]
    if GetPartySize() >= 2:
        $ tmpvar.append({"e_ghoul":3})
    if GetPartySize() >= 3:
        $ tmpvar.append({"e_ghoul":4})

    $ PlayMusicRandom("mus_battle_generic")
    $ StartBattle(BattleData(BackgroundImage = "pbat_wheatfield_fire", CharIDList_Right = tmpvar, CanTransform = False))
    $ PlayMusic("audio/music/46_Siege_Theme.ogg")

    scene nov_district_farmland_siege
    show cg_ghoul_red at right_f
    show mc_transformed at left
    with dissolve

    show cg_ghoul_red at shake
    UNKNOWN "Grghh! You're stronger than I'd hoped!"
    UNKNOWN "... No matter!"
    UNKNOWN "The master will deal with you shortly!"
    hide cg_ghoul_red with dissolve
    "The monster retreated into the shadows, leaving a trail of viscera in its wake."
    show mc_transformed at center with ease
    "I considered chasing it but knew I had more pressing matters to attend to."
    MC "(Markus!)"

    if CharIsMet("arlena"):
        show arlena at left with easeinleft
        show mc_transformed at blurin, center_f with ease
        "I turned to Arlena."
        MC "Barricade yourself inside! Do not leave until it's safe!"
        show mc_transformed at blurin, cright with ease
        "As I turned to leave, she called after me."
        ARLENA @shock "Wait! Hold on!"
        ARLENA @sad "Why... {i}Why do I feel like I know you?{/i}"
        hide mc_transformed with easeoutright
        show arlena at center with easeinleft
        $ Pause(0.5)

    scene black with dissolve
    $ CharSetClothes("arlena", "normal")
    jump qst_TheJudgementDay_GoToMageDist

label qst_TheJudgementDay_FarmlandDist_Unprep:    
    scene cg_novaras_siege_arlena_dead
    with dissolve
    $ CharKill("arlena")
    if QstIsActive(QstDaughterOfMetal):
        $ QstFail(QstDaughterOfMetal)
    $ CharAddRelEntry("arlena", "died_during_siege")
    $ QstComplete(DialogueArlena)
    $ QstComplete(RomanceArlena)
    if CharIsMet("arlena"):
        "In the corner of my eye, I saw her—Arlena—slouched down against the wall of her home, her skull crushed as she still held the bloodied hammer she'd no doubt tried to use to defend herself."
        "I felt a sickening sensation sink into my stomach."
        MC "Arlena... No...!"
    else:
        "In the corner of my eye, I saw her—the blacksmith's daughter—slouched down against the wall of her home, her skull crushed as she still held the bloodied hammer she'd no doubt tried to use to defend herself."
        "I felt a sickening sensation sink into my stomach."
    scene nov_district_farmland_siege
    show mc_transformed at center
    with dissolve
    GUARD "STOP!"
    show mc_transformed at blurin, cright_f with ease
    show cg_guard at left with easeinleft
    MC "(Shit!)"
    "With their spears at the ready, three guards pointed them nervously toward me—covered in blood, their eyes wide with traumatized fear."
    show cg_guard at shake
    
    GUARD "MONSTER!"
    SECOND_GUARD "Kill it! LET'S KILL IT QUICKLY!"
    MC "Wait! You don't understand! I'm not—"
    
    play sound "audio/cfx/explosion.ogg"
    scene nov_district_farmland_siege
    show cg_ghoul_red at cleft
    with dissolve

    "In that moment, the abominable thing landed on top of the guard, crushing him into a bloody pulp as it swung its arms wildly, tearing apart another with ease."
    "The third guard tried to flee, but the monstrous beast grabbed him with its immense clawed hand as he screamed and flailed."
    GUARD "AHHHHGHGHHHH!"
    scene cg_novaras_siege_red_ghoul
    with dissolve
    UNKNOWN "Hoho! Look at you!"
    UNKNOWN "Don't you worry! I have a safe place for all the little boys and girls to hide in!"
    "Cackling, the thing pulled the man down toward the gaping mouth where its stomach should've been."
    play sound "audio/cfx/prologue_guysnap.ogg"
    GUARD "OH GODS! NO! LET ME GO! PLEASE! LET ME—GHFRGHHH!"
    play sound2 "audio/cfx/demorai_roar_med.ogg"
    "Shoving the guard into the opening, the teeth clamped down as the man was torn apart and devoured by the great maw."
    UNKNOWN "Mhmmahaha! Ta-da!"
    UNKNOWN "What did you think of my trick?"
    scene nov_district_farmland_siege
    show cg_ghoul_red at left
    show mc_transformed at right_f
    with dissolve
    UNKNOWN "The master is here! THE MASTER IS HERE!"
    UNKNOWN "How excited he is to meet you..."
    UNKNOWN "{i}Shyahtan!{/i}"
    stop music fadeout 0.1
    stop ambience fadeout 0.1
    $ Pause(0.25)
    play sound "audio/cfx/detect_magic.ogg"
    scene cg_novaras_siege_shyahtan_flashback at blurin
    MC "(I... What?)"
    "A surge of memories came rushing back—memories that weren't my own."
    $ Pause()
    scene nov_district_farmland_siege
    show cg_ghoul_red at left
    show mc_transformed at right_f
    with dissolve
    MC "Grghhh! What in the hells was that?"
    play ambience "audio/ambience_scenes/battle_cave.ogg" fadein 5.0
    UNKNOWN "Hohoho! Such a shame..."
    UNKNOWN "Now, hurry up and DIE, so me and that pretty thing can get more acquainted!"

    $ tmpvar = [{"e_ghoul_red":6}]
    if GetPartySize() >= 2:
        $ tmpvar.append({"e_ghoul":3})
    if GetPartySize() >= 3:
        $ tmpvar.append({"e_ghoul":4})

    $ PlayMusicRandom("mus_battle_generic")
    $ StartBattle(BattleData(BackgroundImage = "pbat_wheatfield_fire", CharIDList_Right = tmpvar, CanTransform = False))

    $ PlayMusic("audio/music/46_Siege_Theme.ogg")

    scene nov_district_farmland_siege
    show cg_ghoul_red at right_f
    show mc_transformed at left
    with dissolve

    show cg_ghoul_red at shake

    UNKNOWN "Grghh! You're stronger than I'd hoped!"
    UNKNOWN "...No matter!"
    UNKNOWN "The master will deal with you shortly!"
    hide cg_ghoul_red with dissolve
    "As the monstrous thing fled, I thought about chasing after it, but I knew I had more pressing matters to deal with first."
    show mc_transformed at center with ease
    if CharIsMet("arlena"):
        "I glanced back toward Arlena."
        MC "Arlena... I'm so sorry."
    else:
        "I glanced back towards the brutalized woman."
        MC "I must press on."
    scene black with dissolve
    jump qst_TheJudgementDay_GoToMageDist

########################################################################
# From here The player heads to the Mage district
label qst_TheJudgementDay_GoToMageDist:
    $ LocNameSetTemp(STR_LOC.NOV_DIST_MAGE)
    scene nov_district_mage_siege with dissolve
    "The mages' district was a war zone."
    show mc_transformed at cleft with easeinleft
    "Unprepared, many of the mages moved frantically, unleashing magic at anything that moved."
    play sound "audio/cfx/explosion.ogg"
    "I watched in horror as a panicked mage turned and unleashed a firestorm—straight into a fleeing civilian."
    play sound2 "audio/cfx/magic_earthy_cast1.ogg"
    $ Pause(0.3)
    play sound "audio/cfx/magic_earthy_cast1.ogg"
    "The man screamed as flames consumed him, his flesh peeling away in molten sheets."
    "The mage muttered something—'S-sorry'—before running with tears in his eyes."
    "Everywhere, bodies littered the ground—some burned, some shredded apart by those abominations."
    "Amidst the chaos, I heard a frantic cry."
    MAGE "T-There! Another M-Monster!"
    show mc_transformed at left with ease
    show cg_mage at right with easeinright
    MC "(Shit!)"
    play sound "audio/cfx/magic_earthy_cast1.ogg"
    show cg_mage at shake
    $ Pause(0.1)
    show mc_transformed at nod
    "A panicked mage raised her staff and fired."
    hide cg_mage with easeoutright
    "I barely dodged as the blast scorched the ground where I stood."
    "Then, I heard it."
    play sound2 "audio/cfx/transform.ogg"
    MARKUS "{i}*ROARRR!*{/i}"
    show mc_transformed at center with ease
    MC "(Markus!)"
    hide mc_transformed with easeoutright
    "Honing in on the sound, I sprinted through the flames, my lungs burning from the thick smoke."
    "Through the haze, I spotted Markus—his dragon-like wings beating furiously as he wrestled two of the damn things."
    show markus_transformed at right_f
    with dissolve
    show mc_transformed at left with easeinleft
    show mc_transformed at shake
    MC "Markus!"
    MARKUS "A LITTLE HELP, PLEASE!"
    $ GoalComplete(QstJudgementDay, 20)
    "I rushed forward, claws at the ready, and struck!"
    $ PlayMusicRandom("mus_battle_generic")
    $ CharHeal("markus")
    $ PartyAddChar("markus")
    $ TransformMarkus(True)
    $ StartBattle(BattleData(BackgroundImage = "pbat_novaras_alley_fire", CharIDList_Right = [{"e_ghoul":2}, {"e_ghoul":3}, {"e_ghoul":2}, {"e_ghoul":3}], CanTransform = False))
    scene nov_district_mage_siege 
    show mc_transformed at left
    show markus_transformed at right_f
    with dissolve
    $ PlayMusic("audio/music/46_Siege_Theme.ogg")
    "As the last of them fell, Markus turned to me, breathless."

    if QstJudgementDay().PlayerPrepared:
        MC "Are you hurt?"
        MARKUS "Nothing I can't handle."
        MARKUS "I had to change—those damn things were tearing people apart!"
        show markus_transformed at shake
        MARKUS "Now the fucking inquisitors have seen me!"
        MC "We'll deal with that later."
    else:
        MC "Are you alright?"
        MARKUS "Nothing I can't handle."
        MARKUS "I had to change—those damn things were tearing people apart!"
        MARKUS "Captain Nyx ordered me to protect the farmlands..."
        show markus_transformed at shake
        MARKUS "Now the fucking inquisitors have seen me!"
        MARKUS "I was on my way there when the whole city turned to shit!"

    MC "We need to regroup with Nyx before—"
    show markus_transformed at shake
    MARKUS "To hell with that!"
    MARKUS "You think the guards are going to spare us?"
    MARKUS "They see a monster, they stab!"
    MARKUS "Fuck this! We need to leave the city NOW!"
    show markus_transformed at blurin, right
    show markus_transformed at nod
    "As Markus flapped his wings, ready to take off, I grabbed his arm and yanked him back."
    show mc_transformed at center with ease
    show mc_transformed at shake
    MC "THE CITY WILL FALL IF WE LEAVE NOW!"
    MARKUS "The city's already fallen! Look around you!"
    MARKUS "No, fuck this! Scale the walls while I fly over—I'll meet you in Hamun!"
    MC "And what about our friends?"
    MC "Our families, our loved ones?"
    MC "You can't just leave them!"
    MARKUS "They're probably already dead!"
    MARKUS "Even if we stay and help, we're FUCKED!"
    show mc_transformed at left with ease
    MC "...Then go."
    MC "But I'm staying."
    show markus_transformed at blurin, right_f
    MARKUS "What?!"
    MC "I won't abandon my friends."
    MC "I won't abandon this city."
    show markus_transformed at blurin, right
    hide markus_transformed with easeoutright
    show mc_transformed at blurin, cleft_f
    "As I turned to leave, I heard him shout behind me."
    MARKUS "FUCKING—FUCK! FUCK! FUCK! ARE YOU FUCKING KIDDING ME!?"
    "For a moment, I heard the powerful flap of his wings..."
    show markus_transformed at cright_f with easeinright
    MARKUS "...I fucking hate you sometimes!"
    "Despite the carnage, I couldn't help but smirk."
    scene black with dissolve
    $ Pause(0.75)
    "...As we made our way through the burning district, a familiar voice rang out."
    DIVINE "[player_name!t]!"
    scene nov_district_mage_siege 
    show mc_transformed at left
    show cg_mage at cright
    show divine at right_f
    with dissolve
    "I turned to see Sister Divine, flanked by a company of battle-ready mages."
    "Some of them eyed me warily, hands hovering over their staffs—until Divine raised a hand."
    MC "The mage towers—are they still standing?"
    DIVINE "For now."
    DIVINE "We're taking as many wounded as we can into the Tower of Palam."
    MC "What do you need?"
    DIVINE "Some of my girls—they were sent out to help recover the wounded. They haven't returned."
    DIVINE "Please, you must help me!"
    MC "Where were they last sent?"
    DIVINE "South-east, near the ruined chapel. Please... find them if you can!"
    MC "I will see what can be done."
    DIVINE "Wait!"
    show divine at center_f with ease
    "Raising her hands, she muttered a prayer, and a warmth spread through my body."
    "{i}A surge of divine magic washed over me, closing my wounds.{/i}"
    play sound "audio/cfx/detect_magic.ogg"
    $ HealParty(NotifyLine = _("Your party has been healed!"))
    scene nov_district_mage_siege 
    show mc_transformed at left
    show cg_mage at cright
    show divine at center_f
    with dissolve

    "Divine staggered slightly, a mage catching her arm."
    DIVINE "I'm fine... Now go! Find the girls!"
    
    $ GoalShow(QstJudgementDay, 30)
    scene black with dissolve
    jump qst_JudgementDay_GoToHousingDist

################################################
# Upon heading to poor district
label qst_JudgementDay_GoToHousingDist:
    $ LocNameSetTemp(STR_LOC.NOV_DIST_HOUSE)
    scene nov_district_housing_siege with dissolve
    "The houses of so many we'd come to know burned around us."
    show mc_transformed at center with easeinleft
    "Torn apart bodies littered the streets—men, women, children..."
    
    "In that moment, my thoughts turned to [regina_ref!t], to Adara, to Erika — to everyone I loved."
    show mc_transformed at cright with easeinleft
    show markus_transformed at cleft with easeinleft
    MC "Markus, I need to know [regina_ref!t] and the others are safe."
    MARKUS "Then let's move quickly."
    MARKUS "I don't know how long we have before this whole city turns to ash."
    hide mc_transformed
    hide markus_transformed
    with easeoutright
    scene black with dissolve
    $ LocNameSetTemp(STR_LOC.NOV_MC_HOUSE)
    "...We wasted no time, rushing towards my home."
    "By some miracle, the house remained unburned."
    scene bg_mc_house_kitchen
    with dissolve
    "Without hesitation, I burst inside."
    show mc_transformed at cright_f with easeinright
    MC "[regina_ref!t]! Erika!"
    hide mc_transformed with easeoutleft
    "I searched the empty, silent home."
    MC "(No one's here.)"
    show mc_transformed at left with easeinleft
    show markus_transformed at right_f with easeinright
    MARKUS "[player_name!t], we can't stay. We need to go!"
    hide markus_transformed with dissolve
    show mc_transformed at center with ease
    MC "([regina_ref!t]... Erika... Where are you both?)"

    scene black with dissolve
    $ LocNameSetTemp(STR_LOC.NOV_ADARA_HOUSE)

    # Variant 1: The player paid to get Adara and her father out
    if QstTheComingStorm().GaveAdaraMoneyForEscape == True:
        "... A short, frantic trip to Adara's followed."
        scene cg_adara_house_siege with dissolve
        "To my relief, her home was empty—cold, abandoned."
        show mc_transformed at left with easeinleft
        MC "(Thank the gods…)"
        MC "(It looks like they made it out before the lockdown.)"
        show markus_transformed at right_f with easeinright
        MARKUS "Is she here?"
        MC "No. They got out."
        MARKUS "Gods be praised. At least someone is safe."
        MARKUS "Let's keep moving!"
        
    # Variant 2: the player did not pay adara
    else:
        "As we arrived, dread filled my gut."
        $ CharSetClothes("adara", "normal_ash")
        scene cg_adara_house_siege 
        show cg_adara_dead_dad

        with dissolve
        "The door was destroyed, the wood shredded like a beast had raked its claws through it."
        "Inside, blood stained the floors and walls."
        "A monstrous corpse lay sprawled, a knife lodged deep into its back."
        "Adara sat in the center of the carnage, cradling her father's lifeless body, blood pooling beneath her."
        #
        "When she saw me, her eyes went wide—then filled with terror."
        hide cg_adara_dead_dad
        show adara cry at cleft
        with dissolve
        show mc_transformed at right_f with easeinright
        show adara cry at shake
        ADARA "GET BACK! GET AWAY FROM ME!"
        "Her cries twisted into panicked sobs."
        show adara cry at shake
        ADARA "HAVEN'T YOU TAKEN ENOUGH FROM ME?!"
        show mc_transformed at cright_f with easeinright
        "I knelt, reaching for her, but she recoiled violently, scrambling back."
        MC "Adara! It's me!"
        show mc_transformed at shake
        MC "ADARA!"
        "She stopped resisting, staring up at me, her face frozen in confusion and grief."
        MC "It's me… It's [player_name!t]."
        "Tears streamed down her face."
        ADARA "...[player_name!t]."
        ADARA "You're..."
        MC "I came as quickly as I could. I—"
        "Adara shoved me away."
        show adara cry at left with ease
        ADARA "GET AWAY FROM ME!"
        "Snatching a knife, she pointed it at me with trembling hands."
        show mc_transformed at center_f with ease
        ADARA "You're one of them! You've been lying to me this whole time!"
        show markus_transformed at right_f with easeinright
        MARKUS "[player_name!t], what is—?"
        ADARA "Y-You too?!"
        MC "Adara, no! Listen to me!"
        MC "We're trying to save the city! I swear it!"
        ADARA "I… I don't know what to believe!"
        hide adara with easeoutleft
        "Before I could say another word, she bolted."
        ADARA "GET OUT OF MY HOUSE!"
        MC "Adara! Wait!"
        $ PlaySoundRandom("woodenDoor")
        "As she slammed the door, I considered chasing after her—but Markus grabbed my shoulder, yanking me back."
        MARKUS "There will be time to explain later!"
        MARKUS "We CANNOT stay here!"
        show mc_transformed at blurin, cleft with ease
        "As much as it pained me, I knew he was right."
        show markus_transformed at blurin, right
        hide markus_transformed with easeoutright
        "We fled into the burning streets once more."
        hide mc_transformed with easeoutright
    
    scene black with dissolve

    # revert from ashed-up sprite
    $ CharSetClothes("adara", "normal")

    if QstIsActive(RomanceNijah):
        if QstJudgementDay().PlayerPrepared == True:
            $ LocNameSetTemp(STR_LOC.NOV_DIST_HOUSE)
            scene nov_district_housing_siege with dissolve
            
            play sound "audio/cfx/female_long_scream.ogg"
            NIJAH "AHHHHHHHHH!"
            
            show nijah at cleft
            show cg_ghoul at cright_f
            with dissolve

            MC "NIJAH!"
            "A terrified Nijah fended off a snarling skin walker, flinging a pot of steaming broth at it."
            show cg_ghoul at shake
            "The thing shrieked as the scalding liquid sizzled its flesh, but as it smacked the pot aside, it raised its claws to strike."
            scene black with dissolve
            "She closed her eyes, bracing for the blow that never came."
            play sound "audio/battle/battle_chars/mc_transformed/char/skilluse5.ogg" volume 0.7
            play sound2 "audio/battle/battle_chars/mc_transformed/basic_attack/impact5.ogg" volume 0.7
            
            scene nov_district_housing_siege
            
            show mc_transformed at cright_f
            show nijah at cleft
            with dissolve
            "When she opened them, the ghoul was severed in half, and I stood over its corpse."
            NIJAH @shock "{i}*Gasp!*{/i}"
            NIJAH @shock "[player_name!t]!"
            show nijah at center with ease
            "Nijah threw herself at me, arms wrapping tight around my body."
            NIJAH "You came! You saved me!"
            MC "Nijah, what are you doing out here? It's not safe!"
            NIJAH @sad "I let friendz shelter in my home during battle."
            NIJAH @sad "One was hurt, zo I went to find mage or medicine!"
            NIJAH @scared "T-Then those monsters came and I couldn't get back!"
            MC "Can you make it home safely now?"
            MARKUS "[player_name!t]! We don't have time for this!"
            "Nijah gently rested her hand on my chest."
            show nijah at cleft_f with ease
            NIJAH @scared "Go! I will be alright!"
            NIJAH "Hurry! Others will need help!"
            MC "...Be safe."
            show mc_transformed at blurin, cright
            NIJAH @sad "...Be safe, my love."
            hide mc_transformed with easeoutright
            show nijah at center with ease
            $ Pause(0.25)
            scene black with dissolve
        else:
            $ CharKill("nijah")
            $ CharAddRelEntry("nijah", "died_during_siege")
            $ QstComplete(RomanceNijah)
            $ QstComplete(DialogueNijah)
            $ QstComplete(PregNijah)

            $ LocNameSetTemp(STR_LOC.NOV_DIST_HOUSE)
            scene nov_district_housing_siege with dissolve

            show markus_transformed at cleft_f with easeinright
            show mc_transformed at cright_f with easeinright

            MARKUS "The castle district isn't far, we should—"
            "Markus suddenly stopped."
            MC "Markus?"
            MC "What is—"

            hide markus_transformed
            hide mc_transformed
            with dissolve
            "As I turned to look at what he was staring at, I froze."
            show cg_siege_nijah_dead at center with dissolve
            "Nijah's body—each limb torn off and pierced on a bloody, jagged spike—was placed in macabre display for all to see."
            "My knees began to shake as my eyes locked on her lifeless expression."
            
            "Markus reached out, catching me before I collapsed."
            hide cg_siege_nijah_dead
            with dissolve
            show mc_transformed at cleft
            show markus_transformed at cright_f
            with dissolve
            MC "Markus... They've..."
            MARKUS "Don't look at her, [player_name!t]!"
            MC "...She did nothing to them. She—"
            MARKUS "[player_name!t]."
            MC "...How... how could—"
            "Markus grabbed my face, forcing me to look away."
            show markus_transformed at shake
            MARKUS "There are still people alive right now who need us!"
            MARKUS "We have to go—you can mourn later!"
            MC "I... Yes, you're right."
            MARKUS "Come."
            MARKUS "Let us move on from this infernal place, quickly."
            scene black with dissolve
            "As we left, I took one last look over my shoulder at Nijah's body, a deep, tremendous pain echoing through me..."
            "...But the pain quickly gave way to pure rage."
            MC "(I'll kill them... I'LL KILL THEM ALL!)"


    jump qst_JudgementDay_GoToCentreDist

########################################################################
# The Player heads to the royal district
label qst_JudgementDay_GoToCentreDist:
    $ LocNameSetTemp(STR_LOC.NOV_DIST_CENTRE)
    scene nov_district_centre_siege with dissolve
    "The castle was in lockdown."
    "Scorched and battered, its walls remained unbreached."
    "Outside, torn-apart guards and skin walkers littered the grounds."
    "But most horrifying were the corpses stacked against the gate—ordinary people who had pleaded for sanctuary."
    "... And were denied."
    "Their bodies were charred black, the stench of burning flesh and ale heavy in the air."
    "Above, music played softly from within the castle walls."
    "Were they drowning out the slaughter outside?"
    "Were they *celebrating* as we died?"
    "A burning rage welled in my chest."
    MARKUS "We need to keep moving—more guards are bound to reinforce—"
    show cecilia at cleft with easeinleft
    GUARD "Princess, please! It isn't safe!"
    show cg_guard at left with easeinleft
    "My eyes snapped toward her—Princess Cecilia."
    "Clad in royal regalia, she picked her way through the bloodied corpses, a fierce determination in her eyes."
    show cecilia at center with ease
    PRINCESS_CECILIA "My brother is still out in the city!"
    PRINCESS_CECILIA "I cannot leave him!"
    show cg_guard at cleft with easeinleft
    GUARD "Princess Cecilia, please!"
    GUARD "This is too dangerous!"
    "As she looked upon the sea of bodies, I heard her heartbeat quicken."
    PRINCESS_CECILIA "....Gods, there's so many of them."
    GUARD "We must return to the castle—"
    show cg_ghoul as ghoul2 at right_f with easeinright
    "From beneath the corpses, monstrous figures lunged, surrounding her."
    GUARD "PRINCESS! GET BACK!"
    "The guards raised their swords, but they were outnumbered."
    "Without thinking, I leapt forward, claws bared!"
    $ PlayMusicRandom("mus_battle_generic")
    MARKUS "[player_name!t]! Wait!"
    MARKUS "Damn it!"
    $ StartBattle(BattleData(BackgroundImage = "pbat_novaras_alley_fire", CharIDList_Right = [{"e_ghoul":3}, {"e_ghoul":4}, {"e_ghoul":3}], CanTransform = False))
    $ PlayMusic("audio/music/46_Siege_Theme.ogg")
    scene nov_district_centre_siege
    show cg_guard at right_f
    show mc_transformed at cleft
    #show markus_transformed at left
    with dissolve
    "As the last beast fell, the guards turned their swords on *us*."
    show cg_guard at shake
    GUARD "Princess! Stand back!"
    GUARD "Back, fiend!"
    PRINCESS_CECILIA "Wait!"
    show cecilia at cright_f with easeinright
    "She stepped between us."
    GUARD "Princess! What are you doing?!"
    GUARD "Get back!"
    PRINCESS_CECILIA "I do not believe these creatures seek to do us harm!"
    show cg_guard at shake
    GUARD "Princess, return at once!"
    "She turned to me, hesitant but composed."
    PRINCESS_CECILIA "Do you... understand me?"
    MC "...Yes."
    "The guards stiffened as her breath hitched."
    PRINCESS_CECILIA "You speak..."
    PRINCESS_CECILIA "I... Thank you for—"
    "A corpse rolled over—then lunged at her."
    "The guards were too slow."
    play sound "audio/battle/battle_chars/mc_transformed/char/skilluse5.ogg" volume 0.7
    play sound2 "audio/battle/battle_chars/mc_transformed/basic_attack/impact5.ogg" volume 0.7
    show cecilia at center_f with ease
    "I grabbed her, pulling her back as my tail severed the creature's head in one clean strike."
    PRINCESS_CECILIA "..."
    MC "Are you alright, Princess?"
    PRINCESS_CECILIA "Y-Yes..."
    GUARD "PRINCESS!"
    show cecilia at cright_f with ease
    "The guards yanked her away, weapons still drawn."
    PRINCESS_CECILIA "Do not harm them!"
    PRINCESS_CECILIA "They saved my life..."
    GUARD "But, Princess—!"
    PRINCESS_CECILIA "Please... If you truly mean to help us, I beg you."
    PRINCESS_CECILIA "My younger brother, Prince Naran, never returned before the siege."
    PRINCESS_CECILIA "Please... Find him!"
    "I bowed."
    $ CharMeet("cecilia")
    $ GoalShow(QstJudgementDay, 35)
    "As the guards dragged her back inside, she called out."
    PRINCESS_CECILIA "What is your name?"
    MC "...[player_name!t], your grace."
    PRINCESS_CECILIA "[player_name!t]... I shall pray for you."
    hide cg_guard
    hide cecilia
    with easeoutright
    show markus_transformed at cright with easeinleft
    $ Pause(0.25)
    show markus_transformed at blurin, cright_f
    MARKUS "...Nothing."
    MC "What?"
    MARKUS "I said nothing."
    MC "What?!"
    MARKUS "NOTHING!"
    scene black with dissolve
    jump qst_JudgementDay_GoToArmyDist

#############################################################
# Army district
#Main fortress district
label qst_JudgementDay_GoToArmyDist:
    $ LocNameSetTemp(STR_LOC.NOV_DIST_ARMY)
    scene nov_district_army_siege with dissolve
    "All around, soldiers and city guards battled the horde of skinwalkers—slashing, clawing, biting."
    "It seemed the whole city was engulfed in its own separate battles, each one as bloody as the next."
    show nyx at center
    show cg_ghoul at right_f
    show cg_guard at left_f
    with dissolve
    "Captain Nyx, bloodied and wild, furiously slashed her blade into one of the skinwalkers, all while barking orders."
    show nyx at shake
    NYX "FUCK OFF! FUCK OFF! FUCK OFF!"
    hide cg_ghoul with moveoutbottom
    NYX "KEEP THE SUPPLY CHAIN TO THE WALL MOVING!"
    show cg_guard at cleft_f with ease
    show nyx at cright with ease
    "As we made our way toward her, a group of guards turned their weapons toward us."
    "One swung his blade, but I managed to knock him aside without killing him."
    show cg_guard at shake
    GUARD "CAPTAIN! LOOK OUT!"
    show nyx at blurin, cright_f
    "Nyx looked up, saw us, and pushed forward through the chaos."
    NYX "LET THEM THROUGH!"
    GUARD "But... Captain! They're—"
    show cg_guard at shake
    NYX "THAT'S A FUCKING ORDER!"
    GUARD "YOU HEARD HER! LET THEM THROUGH!"
    hide cg_guard with dissolve
    "As the guards relented, the hellfire raged above us, battle cries and steel clanging all around."
    show mc_transformed at cleft with easeinleft
    NYX "What's the status on the other districts?"
    MC "Chaos. But we've been clearing out what we can."
    NYX "Fuck!"
    MC "What are your orders?"
    NYX "The wall... Something's happening on the damn wall to the southeast."
    NYX "None of the supplies are reaching the men up there!"
    NYX "Head to the Southeast District."
    NYX "Use one of the pulley shafts to get to the top of the wall—whatever's up there, fucking kill it!"
    MARKUS "What about the other guards?"
    MARKUS "They'll try to kill us!"
    ERIKA "They will not..."
    show nyx at right_f with ease
    show mc_transformed at blurin, center_f with ease
    show erika at left with easeinleft
    "I turned to see Erika, flanked by inquisitors."
    "Blood splattered across her face, her expression was cold—furious but composed."
    MC "Eri—"
    ERIKA "You have a lot of explaining to do when this is over... [player_name!t]."
    MC "...You know?"
    "She didn't answer."
    "She only glared for a moment before turning to Nyx."
    ERIKA "I can escort them to the top of the wall."
    ERIKA "The rest of the inquisitors will stay and assist here."
    NYX "Where is Inquisitor Lorgar?"
    ERIKA "We were separated during the attack."
    NYX "Then you're in charge?"
    "Erika hesitated, glancing at the others."
    ERIKA "W-We're all the same inquisitor rank..."
    NYX "Fuck it, I don't care."
    NYX "Go with [player_name!t] and Markus."
    NYX "Get to the wall and hurry!"
    NYX "I don't know how much longer they can hold out up there with the lines severed!"
    ERIKA "Yes, Captain."

    $ CharHeal("erika")
    $ PartyAddChar("erika")

    $ GoalShow(QstJudgementDay, 40)

    $ PlayerAddItem("inquisitor_uniform", Silent = True)
    $ PlayerAddItem("sword_inquisitor", Silent = True)
    $ PlayerAddItem("ring_inquisitor", Silent = True)
    $ PlayerPartyCharEquipItem("erika", "inquisitor_uniform")
    $ PlayerPartyCharEquipItem("erika", "sword_inquisitor")
    $ PlayerPartyCharEquipItem("erika", "ring_inquisitor")

    $ Pause(0.25)
    show nyx at blurin, right
    hide nyx with easeoutright
    show mc_transformed at cright_f with ease
    show erika at cleft with ease
    MC "Erika, I—"
    show markus_transformed at right_f with easeinright
    ERIKA "Not a fucking word."
    hide erika with easeoutright
    MARKUS "...Good to see you again too, Erika."
    scene black with dissolve
    $ CharSetClothes("nyx", "normal")
    jump qst_JudgementDay_GoToHousing2

##############################################################
# The player heads to the rich district (South-East)
label qst_JudgementDay_GoToHousing2:
    $ LocNameSetTemp(STR_LOC.NOV_DIST_HOUSE_S)
    scene nov_district_housing2_siege
    with dissolve
    stop ambience fadeout 10.0
    "...The district, like the others, was ablaze, yet there was an ominous, distinct lack of cries or clashing blades, as though the entire place had fallen silent."
    show erika at right with easeinleft
    "The sickening stench of burning flesh filled the air, thick and heavy."
    show mc_transformed at center with easeinleft
    "As we pressed forward, the eerie quiet only made everything more unsettling."
    show markus_transformed at left with easeinleft
    ERIKA "We must keep moving..."
    MARKUS "Sister Divine asked us to find the missing Mages of Palam."
    show erika at blurin, right_f
    ERIKA "There is no time for detours!"
    ERIKA "The city's safety takes priority!"
    menu:
        "I won't abandon the mages.":
            if QstJudgementDay().PlayerPrepared:
                jump qst_JudgementDay_RescueMages_Prep
            else:
                jump qst_JudgementDay_RescueMages_Unprep
    
        "You're right, let's keep moving...":
            $ GoalFail(QstJudgementDay, 30)
            ERIKA "This way... I know a shortcut."
            $ Pause(0.25)
            show erika at blurin, right
            hide erika with easeoutright
            hide mc_transformed with easeoutright
            hide markus_transformed with easeoutright
            jump qst_JudgementDay_RescueMages_MoveOn

label qst_JudgementDay_RescueMages_Prep:
    ERIKA "Fine, but we must hurry!"
    $ Pause(0.25)
    show erika at blurin, right
    hide erika with easeoutright
    
    hide mc_transformed with easeoutright
    hide markus_transformed with easeoutright
    "We scoured the district, but neither I nor Markus could pick up their scent through the thick smoke."

    "Suddenly, a sharp cry echoed through the air."
    show mc_transformed at center with easeinleft
    MC "This way!"
    "We followed the sound, hurrying through the burning streets to find the entrance of a noble's manor."
    "From inside, I could hear muffled cries of pain."
    show mc_transformed at shake
    "Slamming a fist against the bolted door, I called out."
    SOPHIRA "Go away! Be gone, creature!"
    MC "Sister Divine sent us! We're looking for the lost Palam mages who never returned!"
    SOPHIRA "L-Lies! Begone, monster!"
    show erika at cright with easeinleft
    show erika at shake
    "Erika stepped forward, slamming her fist against the door."
    ERIKA "By order of the Inquisition, I demand you open this door!"
    "There was a long pause before a sheepish face peeked through the gap."
    show mc_transformed at left with ease
    show erika at center with ease
    "A woman, disheveled and covered in ash, but distinctly noble, oddly resembled Adara in appearance."
    show sophira at right_f with easeinright
    "Upon seeing me and Markus, she gasped and attempted to slam the door shut, but Erika wedged her foot in before she could."
    show sophira at shake
    SOPHIRA "G-Get back!"
    ERIKA "Hold!"
    ERIKA "They are with me."
    "The woman's wide, fearful eyes darted back and forth between me and Markus before she hesitantly turned back to Erika."
    ERIKA "Who are you?"
    SOPHIRA "...I..."
    SOPHIRA "I am Lady Maringott, but call me Sophira."
    $ CharMeet("sophira")
    ERIKA "The Mages of Palam—are they here?"
    SOPHIRA "Y-Yes... Come quickly."
    scene black with dissolve
    $ LocNameSetTemp(_("Noble manor"))
    scene cg_sophira_mansion_mainhall_hospital with dissolve
    "Sophira led us into the main hall of the manor, now a makeshift infirmary littered with wounded men and women."
    "The air was filled with pained groans as bloodied civilians and soldiers writhed on hastily arranged beds."
    "Exhausted Mages of Palam moved frantically, tending to the wounded."
    show sophira at right with easeinleft
    show sophira at blurin, right_f
    "The chaos of the scene meant few even looked up at us."
    show mc_transformed at left
    show erika at cleft
    with easeinleft
    ERIKA "What is going on here?"
    SOPHIRA "The attack came so suddenly..."
    SOPHIRA "We opened our doors to shelter as many as we could, but the wounded kept piling in."
    "Her face darkened."
    SOPHIRA "...Some of the mages didn't make it."
    SOPHIRA "But those who remain have been a blessing from the gods."
    SOPHIRA "I fear many more would have perished without them."
    ERIKA "Where is your husband?"
    SOPHIRA "My husband lost his legs many years ago."
    SOPHIRA "I've confined him to his room for safety until this nightmare ends."
    MC "What can we do to help?"
    SOPHIRA "Please... We need more medicine. The mages are exhausted."
    ERIKA "Take these people to the main fort. There will be—"
    SOPHIRA "No!"
    SOPHIRA "None of the wounded can fight, and the mages are too drained."
    SOPHIRA "We'd be slaughtered if we tried to move now."
    MC "Then what do you suggest?"
    SOPHIRA "The basement."
    SOPHIRA "There are more medical supplies, food, and water down there."
    ERIKA "Then why haven't you retrieved them already?"
    SOPHIRA "{i}...Something is down there.{/i}"
    SOPHIRA "When everything started, we heard strange noises coming from the basement."
    SOPHIRA "We sent two guards down to check, and then... we heard the most awful sounds."
    ERIKA "Is the basement secure now?"
    SOPHIRA "Yes... We bolted and barricaded it shut."
    SOPHIRA "{i}But we can still hear something moving down there...{/i}"
    MC "Where is this basement?"
    SOPHIRA "Wait...! Before you go."
    SOPHIRA "Take these."

    show sophira at nod
    $ PlayerAddItem("potion_heal_large", Amount = 2)

    SOPHIRA "I can't spare much, but... hopefully, you'll be able to clear out whatever's down there."
    ERIKA "Take us to the basement."
    ERIKA "We don't have much time."
    show sophira at blurin, right_f
    hide sophira
    hide erika
    hide mc_transformed
    with easeoutright
    scene cg_sophira_mansion_hallway_fire with dissolve
    show mc_transformed at left with easeinleft
    show erika at center with easeinleft
    "...The basement door was heavily barricaded, tables and chairs stacked against it in a desperate attempt to keep something locked inside."
    "It took several minutes to clear away the debris before we reached the door itself."
    "Sophira hesitated, stepping back as I reached for the handle."

    scene black with dissolve

    "As the door creaked open, an eerie darkness stretched down into the unknown."

    MARKUS "...You first."
    "Step by step, we descended into the oppressive darkness, the cold stone beneath our feet making every movement feel heavier."
    if CharInParty("elena"):
        "Elena whined nervously behind me."
        show mc_transformed at nod
        MC "Calm, Elena."

    if CharInParty("myu"):
        show myu at left_f with dissolve
        MYU "T-This seems like a bad idea to Myu..."
        hide myu with dissolve

    scene cg_mansion_basement with dissolve

    "Finally, we reached the bottom."
    "Even in the dim light, I could see the place was a mess—broken crates, toppled shelves, and shattered bottles lay scattered across the floor."
    "Food, medicine, and supplies lay in ruined heaps as though some wild beast had rampaged through here."
    "Most disturbing of all was the heavy trail of blood that led deeper into the room... only to suddenly disappear in the middle of the floor."
    "Erika tightened her grip on her sword as a strange dragging sound echoed through the chamber."
    ERIKA "{i}It's still here...{/i}"
    "A sinister, wet slithering noise grew louder, circling us from the shadows."
    "And then, as if the very darkness itself was shifting, everything went still..."

    show cg_snakeman at center with flash
    $ Pause(1.0)
    $ PlayMusicRandom("mus_battle_generic")
    $ StartBattle(BattleData(BackgroundImage = "pbat_mansion_basement", CharIDList_Right = [{"e_snakeman":8}], CanTransform = False))
    $ PlayMusic("audio/music/46_Siege_Theme.ogg")
    scene cg_mansion_basement
    show mc_transformed at left
    with dissolve
    "Writhing in agony, the creature let out a sickening bellow as blood sprayed across the walls."
    show mc_transformed at shake
    "In a final desperate lunge, it attempted to strike—but with a swift swipe of my tail, its head tumbled to the floor, lifeless."
    show markus_transformed at right_f with easeinright
    MARKUS "{i}*Huff*{/i} What in all the gods was that thing?"
    show erika at center with easeinleft
    ERIKA "{i}I've seen creatures like this before...{/i}"
    MARKUS "You have?"
    ERIKA "Dark mages can create many horrors..."
    MARKUS "Wait, are you saying dark mages are working with the Demorai?"
    ERIKA "Who knows? We don't have time to speculate."
    ERIKA "Let's go back and tell Sophira it's safe."
    
    scene black with dissolve
    scene cg_sophira_mansion_mainhall_hospital
    show sophira at left
    with dissolve
    show erika at center_f with easeinright
    show mc_transformed at right_f with easeinright

    SOPHIRA "You're back!"
    SOPHIRA "We heard terrible noises—I feared the worst!"
    ERIKA "It's safe now."
    ERIKA "Though I'm afraid much of the medicine may be lost..."
    SOPHIRA "We'll make do. Thank you."
    "Sophira turned toward me and Markus, her expression softening."
    SOPHIRA "...Thank you."
    SOPHIRA "You may have saved a lot of lives today."

    $ GoalComplete(QstJudgementDay, 30)

    if CharInParty("myu"):
        show myu at cright with dissolve
        MYU "Hooray! Myu did a good!"
        SOPHIRA "A-Ahh... Yes, you did."
        hide myu with dissolve

    ERIKA "We need to go."
    ERIKA "We've wasted enough time."
    SOPHIRA "Wait! Before you leave..."
    SOPHIRA "Let one of the mages tend to your wounds. It's the least we can do."

    scene black with dissolve
    $ HealParty(NotifyLine = _("Your party has been healed!"))
    "...After being healed by one of the mages, we made our way out."
    jump qst_JudgementDay_RescueMages_MoveOn

label qst_JudgementDay_RescueMages_Unprep:
    ERIKA "Fine, but we must hurry!"
    $ Pause(0.25)
    show erika at blurin, right
    hide erika with easeoutright
    
    hide mc_transformed with easeoutright
    hide markus_transformed with easeoutright

    "We scoured the district, but neither I nor Markus could pick up their scent through the thick smoke."
    "Suddenly, a sharp cry echoed through the air."
    show mc_transformed at center with easeinleft
    MC "This way!"
    "We followed the sound, hurrying through the burning streets to find the entrance of a noble's manor."
    "From inside, I could hear muffled cries of pain."
    show mc_transformed at shake
    "Slamming my fist against it I called out to only be met with silence as my answer."
    show mc_transformed at shake
    "Gripping at the door with my tentacles, I tore the thing open with ease and stepped inside."
    scene cg_sophira_mansion_mainhall_massacre
    with dissolve
    $ Pause()
    "The walls were laced in blood, bodies torn to shreds littered the place."
    "Here and there, a bit of bloodied blue flesh and skin as the sickly smell of blood and death filled the air."
    "It appears the mansion had been used as some kind of makeshift hospital."
    "Or at least, it {i}was{/i} before something got in."
    show mc_transformed at left
    show erika at center_f
    "Erika turned a shade of white as she struggled not to throw up."
    ERIKA "Gods... What happened in here?"
    show markus_transformed at right_f
    MARKUS "It doesn't look like they managed to put up much of a fight..."
    "A snapping sound echoed through the halls, followed by another ghastly scream."
    $ CharKill("sophira")
    $ CharAddRelEntry("sophira", "died_during_siege")
    play sound "audio/cfx/female_long_scream.ogg"
    UNKNOWN "AHHHHHHHH!" 
    MC "This way!"
    hide mc_transformed with easeoutright
    scene black with dissolve
    "Chasing the screams led us down a hallway towards a strange entranceway leading underground."
    "With shattered chains around the entranceway, {i}something{/i} must have broken out."
    "A bone-chilling crunching sound was heard as we descended the stairs into that deep and terrible darkness."

    scene cg_mansion_basement with dissolve
    "There... waving a torch around the flooded basement, the water up to our ankles, we looked around for the source of the sound."
    "Slowly moving the light from left to right across the debris, there...{i}we saw it.{/i}"
    show cg_sophira_snakeman_dead at center with dissolve
    "A snake like creature with a humanoid like body, sinking it's teeth once more into the woman in a blue dress."
    "She let out one last raspy cry of pain as the thing chewed on her, the deep red sinking through and overpowering the blue."
    "Pale white, she seemed completely drained of all life as the eyes of her ghastly, skeleton white face rolled up."
    "The creature snarled, tosing her now lifeless body aside, letting it slam against one of the walls as we heard the bones break."

    show cg_snakeman at center with flash
    "It licked at it's bloody fangs before lunging towards us!"
    
    
    $ Pause(1.0)
    $ PlayMusicRandom("mus_battle_generic")
    $ StartBattle(BattleData(BackgroundImage = "pbat_mansion_basement", CharIDList_Right = [{"e_snakeman":8}], CanTransform = False))
    $ PlayMusic("audio/music/46_Siege_Theme.ogg")
    scene cg_mansion_basement with dissolve
    show mc_transformed at left
    with dissolve
    "Slicing my claws across the creature's throat, the snakeman waved back and force, reaching at it's gaping wound where it's throat once was."
    "After letting out a desperate, raspy cry, it collapsed face first into the water, twitching for a few moments before falling completely still."
    MC "What in the hells is this thing?"
    MC "Some kind of... dark magecraft abomination?"
    show erika at center with easeinleft
    ERIKA "I... I've never seen anything like it before."
    ERIKA "It appears to be... {i}part human?{/i}"
    show markus_transformed at right_f with easeinright
    MARKUS "We should leave this place, whatever this {i}thing{/i} is, the inquisitors and whoever can look at the damn thing when we're done."
    scene black with dissolve
    "I nodded in agreement as we made our way back up through the mansion estate."
    scene cg_sophira_mansion_mainhall_massacre with dissolve
    "I took one last look at the dead bodies littered around... Perhaps..."
    show mc_transformed at cright_f with easeinright
    "{i}Perhaps if things were different, I could have saved them.{/i}"
    show erika at center_f with easeinright
    ERIKA "[player_name!t], let's go."
    hide mc_transformed
    hide erika
    with easeoutleft
    jump qst_JudgementDay_RescueMages_MoveOn

label qst_JudgementDay_RescueMages_MoveOn:
    $ LocNameSetTemp(STR_LOC.NOV_DIST_HOUSE_S)
    scene black with dissolve
    "Navigating through the chaotic streets, Erika guided us through a series of alleyways and back routes."
    "Finally, pushing through to the main street, we hurried toward our destination."
    ERIKA "We must move quickly before—"
    scene cg_silver_knight_scene with dissolve
    "There, amidst a heap of mangled corpses, sat the gleaming, towering figure of the Silver Knight."
    "His cape fluttered in the wind as the city burned around him, his presence eerily still in the midst of carnage."
    "Despite the splattering of blood across his armor, his silver plating still shined brilliantly through the filth."
    scene nov_district_housing2_siege
    show cg_silver_knight at right
    with dissolve
    show mc_transformed at left with easeinleft
    SILVER_KNIGHT "..."
    show cg_silver_knight at blurin, right_f
    "Slowly, he tilted his head up, locking his piercing gaze onto us."
    show cg_silver_knight at cright_f with ease
    "His grip on his massive sword tightened as he rose to his feet, advancing in our direction."
    MARKUS "F-Fuck! It's him! It's the Silver Knight himself!"
    "The Silver Knight... A warrior of legend, chosen to serve and die for the royal family of Alderay."
    "Possessing unmatched skill in both blade and magecraft, it was said that he was perhaps the only man who could have challenged Newheart and won."
    "...And now, he was coming straight for us."
    ERIKA "Hold, Sir Knight! HOLD!"
    show erika at center with easeinleft
    "The Silver Knight stopped in his tracks, eyes narrowing as he examined me and Markus."
    "His posture remained unreadable, but his grip on his weapon remained firm."
    show erika at cleft with ease
    SILVER_KNIGHT "…What are they?"
    ERIKA "As of now, these... creatures are under the order of the Inquisition."
    SILVER_KNIGHT "I do not concern myself with the affairs of the Inquisition."
    SILVER_KNIGHT "Only that the royal family remains safe."
    "Erika gulped, the color draining from her face as she likely questioned whether even all of us combined could stop the Silver Knight."
    MC "Princess Cecilia has tasked us with finding her brother, Prince Naran, and returning him to the castle."
    "The Silver Knight studied me carefully before turning his gaze to Erika."
    SILVER_KNIGHT "Princess Cecilia should be in the castle."
    SILVER_KNIGHT "How did this creature approach her?"
    MARKUS "We saved her damn life!"
    "In an instant, the Silver Knight's blade was pointed directly at Markus' throat."
    show cg_silver_knight at shake
    SILVER_KNIGHT "Her 'damn life' is worth far more than yours, creature."
    SILVER_KNIGHT "Remember that when you speak of her."
    "I stepped between Markus and the blade."
    MC "Princess Cecilia attempted to sneak out in search of her brother."
    MC "She was ambushed by Demorai, but we saved her."
    "The Silver Knight paused, seemingly weighing my words."
    SILVER_KNIGHT "…If what you say is true."
    show cg_silver_knight at right_f with ease
    "He withdrew his blade, bringing his gauntleted hand over his chest in a tight salute."
    SILVER_KNIGHT "I owe you my thanks."

    if CharInParty("myu"):
        MYU "Myu helped too!"
        if CharInParty("elena"):
            MYU "As did Elena!"
            "Elena averted her gaze nervously."
            ELENA "H-Hello…"
            SILVER_KNIGHT "…Then you also have my thanks."

    ERIKA "We're heading up the wall. Is the prince safe?"
    "The knight nodded slightly."
    SILVER_KNIGHT "He is safe now, my prince."
    "From behind a narrow alley, a short, timid figure emerged."
    show naran at cright_f with easeinright
    "His features were delicate, almost effeminate."
    "His wide, uncertain eyes flickered between me and my companions."
    SILVER_KNIGHT "They are not a threat, my lord."
    "The young prince hesitated, his voice soft and uncertain."
    PRINCE_NARAN "Volsta… W-What manner of creatures are these?"
    SILVER_KNIGHT "I do not know, my prince."
    SILVER_KNIGHT "But we must return you to the castle at once."
    PRINCE_NARAN "But… those monsters are still everywhere!"
    "The prince clung tightly to the Silver Knight, trembling."
    SILVER_KNIGHT "I will keep you safe, Naran."
    $ GoalComplete(QstJudgementDay, 35)
    SILVER_KNIGHT "But we must move now."
    play sound "audio/cfx/explosion.ogg"
    "Above us, a deafening explosion rocked the sky as a section of the wall burst into flames."
    ERIKA "We need to hurry, quickly!"
    hide erika with easeoutright
    hide mc_transformed with easeoutright
    show cg_silver_knight at cleft_f with ease
    show naran at cright_f with ease
    "Suddenly, from the surrounding buildings and alleyways, a chorus of unnatural growls echoed."
    "More of those monstrous ghouls began to emerge, shambling toward us from every direction."
    PRINCE_NARAN "J-Jaras!"
    "The prince recoiled, hiding behind the Silver Knight as he slowly unsheathed his blade."
    SILVER_KNIGHT "Stay behind me, my prince."
    "The knight briefly glanced toward us."
    SILVER_KNIGHT "Go. Secure the wall."
    SILVER_KNIGHT "{i}I will handle the monsters…{/i}"
    scene black with dissolve
    jump qst_JudgementDay_GotToTheWall

label qst_JudgementDay_GotToTheWall:
    play ambience "audio/ambience_scenes/battle_cave.ogg" fadein 5.0
    "We didn't waste a second, sprinting toward the large wooden lift."
    ERIKA "This should take us straight to the top."
    scene cg_novaras_siege_attack with dissolve
    MARKUS "We'll be completely exposed up there!"
    MARKUS "Does it even still work?"
    ERIKA "We don't have time to take the stairs! We're going up now!"
    "With a sharp pull of the lever, the mechanical gears below groaned as the wooden lift jolted to life, carrying us upward."
    "As we ascended, the devastation of the city became clearer."
    "The once-proud walls of Novaras were engulfed in fire and smoke."
    "From above, Demorai siege weapons continued their relentless assault, launching massive fireballs against the city's defenses."
    MARKUS "By the gods… Will there even be a city left after this?"

    if CharInParty("myu"):
        MYU @sad "…M-Myu."
    if CharInParty("elena"):
        ELENA @grumpy "Cities can be rebuilt."
        ELENA @grumpy "But battles can only be won or lost once."

    ERIKA "Stay focused. We're almost at the top."

    scene pbat_siege_wall
    show mc_transformed at left
    show markus_transformed at right_f
    show erika at center_f
    with dissolve

    "After a few agonizing minutes, the lift finally came to a grinding halt."
    "The scene atop the wall was grim—scattered corpses of Alderian soldiers and Demorai invaders lay piled on top of one another."
    "A few Demorai ladders had made it onto the ramparts, their corpses still clinging to the edges where they had been cut down."
    "Archers and mages fired relentlessly at the invading forces below, doing everything in their power to hold the line."

    $ GoalComplete(QstJudgementDay, 40)
    MC "…Fuck."
    show erika at shake
    ERIKA "Come on. Don't get distracted."
    ERIKA "We need to clear whatever's disrupting the—"
    GUARD "GRAAAGHHHH!"
    "A severed body flew past us, crashing into the stone wall with a sickening crunch."
    "In that instant, I heard it—that terrifying, inhuman screech."
    "The one I had tried so desperately to forget."
    ERIKA "This way! Hurry!"
    scene cg_novaras_siege_zanarak_fight with flash
    $ Pause()
    "We raced forward, just in time to see the last few remaining soldiers fall before… {i}him.{/i}"    
    "A towering figure, his body thick as though it was armor, stood in the center of the carnage."
    "His wicked, jagged spear dripped with fresh blood."
    "His eyes locked onto mine."
    "A grin spread across his face—sharp, cruel, and filled with bloodlust."
    "My heart sank."
    MC "…Zanarak."

    $ GoalShow(QstJudgementDay, 50)
    
    "A suffocating, oppressive darkness seemed to fall over the wall."
    "Even Erika, normally calm and collected, turned pale, her hand trembling over the hilt of her sword."

    if CharInParty("elena"):
        ELENA "{i}*Scared whine*{/i}"
    if CharInParty("myu"):
        MYU @scared "{i}M-Monster…{/i}"
    scene pbat_siege_wall
    show cg_zanarak_char at center
    with flash

    "Zanarak slowly turned, his gaze fixed solely on me."
    "And then, without warning, he lunged."

    $ PlayMusicRandom("mus_battle_generic")
    $ StartBattle(BattleData(BackgroundImage = "pbat_siege_wall", CharIDList_Right = ["zanarak"], CanTransform = False))
    $ PlayMusic("audio/music/46_Siege_Theme.ogg")

    scene pbat_siege_wall
    show cg_zanarak_char at center
    with dissolve

    "The battle was unlike anything I had faced until now."
    "Exhaustion weighed heavily on us. Everyone had already been pushed to their limits."
    "A swipe of my tail tore a deep gash across him, blood seeping from the wound - a blow that should have brought him down."
    "For a breathless moment, we watched as the creature stumbled back several feet..."
    "Then... Zanarak slowly straightened. He ran a finger through the blood and inspected it. His grin widened as he looked toward me."
    MC "... Fuck."
    "In that moment, I realized the horrifying truth: every opening he'd given us, every blow we'd landed - he'd allowed all of it."
    "Zanarak, despite his immense size, moved with unsettling grace—dodging effortlessly, his massive frame reacting as though unhindered by weight."
    "Even when an attack did land, he merely shrugged it off as if it were nothing."
    "I glanced at my companions, exhausted and barely holding on. He'd been holding back simply to enjoy himself."
    "He wasn't struggling."
    "He wasn't even fighting seriously."
    "{i}He was toying with us.{/i}"
    ERIKA "HRGHHH!"
    "With a final desperate cry, Erika launched herself forward, her blade raised high."
    "But Zanarak was too fast."
    "Before she could react, he struck with the wooden end of his spear—sending her sprawling across the ground, knocked unconscious from the sheer force."
    show cg_zanarak_char at shake
    if CharInParty("elena"):
        "Elena snarled, lunging forward with everything she had."
        show cg_zanarak_char at shake
        "But with one swift motion, Zanarak slammed his massive arm downward, smashing her into the ground."
        MC "ELENA!"
        "She let out a weak, pitiful whimper, her body spasming as blood pooled beneath her."
    if CharInParty("myu"):
        MYU "NO HURT FRIENDS!"
        "Myu sprang forward, dissolving her form and wrapping herself around Zanarak's body like a suffocating mass."
        "For the first time, he seemed irritated as Myu stabbed and slashed at him relentlessly."
        show cg_zanarak_char at shake
        "But then, with a wave of his arm, flames erupted from his form, and Myu let out a pained cry."
        "Scorched and weakened, she collapsed to the ground—a melted puddle, unable to reform."
    #

    MARKUS "Together, brother! We strike together!"
    "Markus and I attacked in unison, our combined strength focusing on one final, desperate assault."
    "But it was over before it had even begun."
    "Markus' punch connected—solid and forceful—yet Zanarak barely acknowledged it."
    "With a swift motion, his tail slashed through the air, carving deep into Markus' side."
    MARKUS "G-GAGHHH!"
    "He collapsed onto his knees, clutching at the deep wound."
    "Blood seeped between his fingers, but he couldn't move—he was finished."
    MC "MARKUS! Stay down!"
    MARKUS "[player_name!t]... Go! Run!"
    MARKUS "GAHHHRHH!"
    "I had no time to react."
    "With every swipe of my claws, every desperate slash of my tail, Zanarak effortlessly dodged or deflected each blow."
    "Then, in an instant, I felt it."
    scene cg_novaras_siege_zanarak_tentacle with dissolve
    "His massive hand shot forward, seizing two of my tentacles in a vice-like grip."
    scene cg_novaras_siege_zanarak_tentacle with flash
    "A sharp, sickening *RIP.*"
    "The agony was beyond anything I had ever felt before."
    "My vision blurred as my severed limbs fell to the ground, blood oozing from the torn flesh."
    MC "AAARRRRGHHHHH!"
    MARKUS "NOOOO!"
    MARKUS "S-STOP! JUST RUN! RUN, YOU FOOL!"
    "But it was too late."
    "My body was breaking apart."

    "Each strike that landed sent fresh waves of pain through my already shattered form."
    "Cracks formed beneath my hardened skin as bones snapped, each breath becoming more labored, more painful."
    "I could taste the blood pooling in my mouth, feel it seeping from my eyes."
    "Panic. Desperation. Fear."
    "Death loomed before me, his form taking the shape of Zanarak himself."
    "With one final, desperate swing, I lashed out—"
    "But Zanarak caught my arm effortlessly."
    "Before I could even react, his fingers tightened around my throat."
    "I gasped, my body thrashing uselessly in his grip."
    "He barely needed to exert any force—his strength was so absolute, I could hardly move."
    "He pulled me closer, his sharp teeth gleaming in the firelight, his eyes filled with amusement."
    "A short, cruel snort escaped him."
    ZANARAK "{i}Is that ALL you have?{/i}"
    "I knew this was it."
    "But even if I was going to die here, at the very least—"
    "I wanted to wipe that smug, twisted grin from his face."
    "With the last of my strength, I lunged forward—slamming my forehead into his."
    "For the first time, his expression changed."
    "Not pain. Not fear. But… irritation."
    "Then, with a single swing, he hurled me across the battlefield like a broken doll."
    scene cg_novaras_siege_zanarak_mc with flash
    "I crashed into the stone wall, my body limp, useless."
    "I couldn't move."
    "Even the smallest motion felt impossible."
    "My body was broken—shattered."
    "All I could do was breathe."
    "Breathe in."
    "Breathe out."

    $ GoalFail(QstJudgementDay, 50)

    "Each breath was excruciating."
    "The battlefield faded into white noise."
    scene cg_novaras_siege_zanarak_mc with dissolve:
        blur 8.0
    "Was this really it?"
    "Was this how I was going to die?"
    "My thoughts swirled in a haze as I saw Zanarak approaching."
    "His spear was raised high, glistening in the firelight—ready to deliver the final blow."
    MC "(Adara... everyone... I'm sorry...)"
    scene black with dissolve
    "I closed my eyes, waiting for the end."
    REGINA "{i}*Whistles*{/i}"
    "My eyes fluttered open—just barely."
    scene pbat_siege_wall:
        blur 5.0
    $ CharSetClothes("regina", "robe")
    $ CharSetVar("regina", "hood", True)
    show regina at center:
        blur 15.0
    with dissolve
    "A silhouette stood before me, dressed in flowing black robes."
    "Her piercing gaze…"
    "Her eyes were burning, glowing with an eerie purple light."
    "{i}Regina?{/i}"
    "Zanarak paused, his attention snapping toward her."
    "For the first time, he hesitated."
    REGINA "I'm afraid that one belongs to me."
    REGINA "{i}You{/i} cannot have them, Lord of Death."
    "A low growl rumbled from Zanarak's throat."
    "But then, his body tensed as Regina lifted her hand."
    play sound2 "audio/cfx/magic_earthy_cast1.ogg"
    show regina at shake:
        blur 12.0
    $ Pause(0.25)
    play sound "audio/cfx/magic_earthy_cast1.ogg"
    "A blinding burst of pure energy surged from her palm, slamming into him with the force of a divine hammer."
    show regina at shake:
        blur 8.0
    play sound2 "audio/cfx/magic_earthy_cast1.ogg"
    "Then another."
    show regina at shake:
        blur 6.0
    play sound "audio/cfx/magic_earthy_cast1.ogg"
    play sound2 "audio/cfx/explosion.ogg"
    "And another."
    REGINA "Go back to your master!"
    REGINA "Crawl back to that realm of shadows and LET US BE!"
    "The final explosion of energy was unlike anything I had ever seen."
    play sound2 "audio/cfx/magic_earthy_cast1.ogg"
    play sound "audio/cfx/explosion.ogg"
    scene white with flash
    "A radiant light so brilliant that, for a brief moment, it eclipsed the night itself."
    "It could be seen across the entire battlefield."
    "Zanarak reeled back—his body, for the first time, truly *pushed.*"
    scene cg_novaras_siege_zanarak_down with dissolve
    "And then, like some dark, fallen god, he plummeted from the edge of the city wall."
    "The monstrous figure fell."
    "His enormous wings stretched wide as he tumbled downward—down into the abyss below."
    scene pbat_siege_wall:
        blur 5.0
    show regina at center:
        blur 10.0
    with dissolve
    "My vision blurred again."
    "I barely registered Regina kneeling beside me."
    "Her soft fingers caressed my face, her touch almost… soothing."
    REGINA "Don't worry, dear."
    REGINA "{i}I'll always keep you safe.{/i}"
    hide regina
    with dissolve
    "Then, in an instant, she was gone."
    "Her form melted into a swirling mass of black crows that scattered into the night."
    MC "...[regina_ref!t]."
    scene pbat_siege_wall with dissolve:
        blur 15.0
    show cg_guard at left with easeinleft:
        blur 15.0
    show cg_mage at right with easeinright:
        blur 15.0
    "As my consciousness faded, I saw armored figures rushing toward me."
    "Guards."
    "Inquisitors."
    "Soon, the sharp glint of spearheads surrounded me."
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    scene black with dissolve
    "And then… nothing."
    "Darkness."
    "A deep, endless sleep."
    $ Pause(1.0)
    $ GoalComplete(QstJudgementDay, 100)

### this section removes party chars and adds them to a list of 
# "who were with you at the wall" chars
    $ tmpvar = {}
    $ tmpvar["party_copy"] = copy.deepcopy(player_party)
    $ tmpvar["party_copy"].remove("mc")
    while len(tmpvar["party_copy"]) > 0:
        $ tmpvar["CharID"] = tmpvar["party_copy"].pop()
        $ PartyRemChar(tmpvar["CharID"], Silent = True)
        $ QstJudgementDay().CharactersWhoWereAtTheWall.add(tmpvar["CharID"])

    $ tmpvar = {}
###
    if PlayerItemQty("inquisitor_uniform") > 0:
        $ PlayerRemItem("inquisitor_uniform")

    if PlayerItemQty("sword_inquisitor") > 0:
        $ PlayerRemItem("sword_inquisitor")

    if PlayerItemQty("ring_inquisitor") > 0:
        $ PlayerRemItem("ring_inquisitor")
        

    $ CharSetClothes("regina", "normal")
    $ CharSetVar("regina", "hood", False)
    $ Pause(1.0)
    jump qst_JudgementDay_SiegeOverPrison

########################################################################
label qst_JudgementDay_SiegeOverPrison:
    $ CharSetClothes("mc", "pants")
    $ LocNameSetTemp(_("Prison cell"))
    play ambience "audio/ambience_loc/prison.ogg" fadein 1.0
    "...Once again, I found myself confined to a cell. I waited. Wondered. Hoped for the best."
    "My secret was out, and now, I lay at the mercy of an empire that saw me as just another monster."
    $ tmpvar = 7
    while tmpvar > 0:
        $ TimeAdvBy(TIME_1H * 12)
        $ TimeAdvBy(TIME_1H * 12)
        $ tmpvar -= 1
    $ tmpvar = {}
    scene bg_prison_cell with dissolve
    "Days drifted by in agonizing slowness."
    "A thousand times, I considered escaping, but I knew my fate would be sealed to a lifetime in exile if I tried... or worse."
    "My thoughts wandered to Markus, Adara, the others..."
    "Were they safe? What was happening beyond these walls?"
    "The guards told me nothing."
    "They simply came, delivered bowls of food, and left in silence, leaving me to wait."
    scene bg_prison_cell_night with dissolve
    "And wait."
    scene bg_prison_cell with dissolve
    "And wait."
    scene bg_prison_cell_night with dissolve
    "Each passing moment, my body betrayed me further."
    show mc at cright_f with easeinright
    BLACK "(We must find a mate soon...)"
    show mc at cleft_f with ease
    show mc at blurin, cleft
    MC "(If we leave now, we're finished. We'll never be able to return.)"
    show mc at cright with ease
    show mc at blurin, cright_f
    "I grimaced, feeling the burning sensation coursing through my veins—hot, relentless, growing stronger with each day."
    show mc at cleft_f with ease
    show mc at blurin, cleft
    BLACK "(It matters not... We must find a mate soon.)"
    BLACK "(Or we will die.)"
    show mc at cright with ease
    show mc at blurin, cright_f
    "Sweat dripped from my skin as my body rebelled against me, wracked with an agonizing need that would not subside."
    hide mc with dissolve
    "And then, at last…"
    "Something changed."
    "A distant echo of boots striking stone."
    "A key turning in the heavy lock."
    show alcott at center
    with dissolve
    show cg_guard as guard1 at left
    show cg_guard as guard2 at right_f
    with dissolve
    "Standing before me, flanked by four guards, was Emperor Alcott himself."
    ALCOTT "...Leave us."
    hide guard1 with dissolve
    hide guard2 with dissolve
    "The guards hesitated for only a moment before silently obeying, stepping out of the cell and sealing the door behind them."
    "And so, to my surreal disbelief, I found myself alone in a cell... with the Emperor himself."
    ALCOTT @talk "...So, we meet again."
    ALCOTT @talk "[player_name!t], isn't it?"
    MC "...Yes."
    ALCOTT "Ahh... Yes, I've read the reports."
    # "The Emperor began to pace, his heavy boots clanging with every deliberate step."
    ALCOTT @talk "The reports of your performance during the battle are most impressive."
    ALCOTT @talk "Not only did you save the princess, but many accounts credit you with actively repelling the enemy inside the walls."
    ALCOTT @smile "Even the Silver Knight himself has offered written testimony on your behalf."
    ALCOTT @talk "Quite the feat... for a monster."
    MC @talk "I am no monster."
    "There was a breathless exhaustion in my voice."
    MC @talk "I was born a man."
    ALCOTT @talk "What you were is irrelevant to what you {i}are{/i} now."
    menu qst_JudgementDay_SiegeOverPrison_alcott_menu:
        "Is Erika alright? Markus? The others?":
            ALCOTT @talk "They have all been detained for the time being."
            ALCOTT @talk "But your companions are alive."   
            jump qst_JudgementDay_SiegeOverPrison_alcott_menu

        "I... can't remember what happened after I fell unconscious.":
            ALCOTT @talk "The battle raged on, of course. The city suffered heavy losses..."
            ALCOTT @talk "But with the internal threat dealt with, we were able to refocus on repelling the Demorai."
            ALCOTT @talk "It seems that without you and your companions... this city would have fallen."
            MC @talk "And my thanks is to be bound in chains..."
            ALCOTT @talk "For now, yes."
            jump qst_JudgementDay_SiegeOverPrison_alcott_menu

        "What do you want from me?":
            pass

    ALCOTT @talk "I want answers."
    ALCOTT @talk "And if you speak the truth, I {i}might{/i} spare your life."
    ALCOTT @talk "What are you?"
    ALCOTT @talk "Even Alderay's finest scholars and mages remain clueless as to your nature."
    ALCOTT @talk "So tell me, creature."
    ALCOTT @talk "Are you more man... or beast?"
    menu:
        "I am a man at heart.":
            ALCOTT @talk "Hmm... Interesting."    
        "I'm a monster... but I'm not your enemy.":
            ALCOTT @talk "Is that so?"
        "I'm whatever you pay me to be.":
            ALCOTT @joy "Ha! Coin, is it?"
            ALCOTT @talk "Well, you wouldn't be the first whose allegiance is for sale."
    ALCOTT @talk "You served under Captain Duprey in the scouts, did you not?"
    MC @talk "Yes."
    ALCOTT @talk "And you didn't even finish basic training before you and your division were sent to investigate a fort just beyond the Valley of Death, correct?"
    MC @talk "...Yes."
    "Alcott exhaled sharply, shaking his head with a smirk."
    ALCOTT @smile "{i}It seems the old man still has a few tricks up his sleeve.{/i}"
    MC @think "What?"
    ALCOTT @talk "You and your division were never supposed to head that way."
    ALCOTT @talk "Your orders were to patrol the valley briefly before heading west to Inma for six months."
    ALCOTT @talk "Instead, you were pushed deep into Demorai territory."
    MC @think "What?"
    MC @think "Why...?"
    ALCOTT @angry "The old man has been quietly trying to consolidate power beneath my nose."
    MC @think "The old man?"
    MC @talk "You mean... King Mesamor?"
    ALCOTT @angry "Indeed."
    ALCOTT @angry "The official scouting orders that landed on my desk were a forgery."
    ALCOTT @angry "I had no idea where you had been sent."
    ALCOTT @talk "It seems Mesamor was determined to recover {i}something{/i} from that fortress."
    "His gaze shifted toward me, scrutinizing."
    ALCOTT @talk "And if I were a betting man, I'd wager that you and your friend found whatever he was looking for."

    "Memories flooded back."
    scene cg_citywallsoldiers with flash
    "The journey into that cursed place."
    scene cg_mc_eye with dissolve
    "The fortress."
    "Zanarak."
    "Was that why he pointed at me?"
    "Did he know?"
    scene cg_obelisks_tentacles with dissolve
    "Did he know what lay beneath that ruin?"
    scene bg_prison_cell_night 
    show alcott at left
    show mc at right_f
    with dissolve
    ALCOTT @talk "Don't lie to me now, boy."
    ALCOTT @talk "Tell me everything that happened."
    MC @talk "You've read the reports."
    show alcott at cleft with ease
    show alcott at shake
    ALCOTT @angry "I don't care about the {i}fucking{/i} reports—I care about the truth."
    ALCOTT @talk "Now tell me."
    ALCOTT @talk "{i}What really happened out there?{/i}"
    MC "..."
    scene black with dissolve
    $ Pause(1.0)
    "Over the next hour, I told the Emperor everything."
    "Every detail. Every horror. The worst nightmare of my life laid bare before him."
    "He listened."
    "He asked questions."
    "He watched me intently."
    "And when I was finished, he asked one final question."
    scene bg_prison_cell_night 
    show alcott at right_f
    show mc at left
    with dissolve
    ALCOTT @talk "And if you {i}don't{/i} find a mate… what happens?"
    "For the first time in the past few hours, I heard the voice of my dark passenger whisper to me."
    "Or rather... Shyahtan."
    SHYAHTAN "({i}Lie.{/i})"
    show mc at nod
    "I swallowed hard."
    "And for the first time since this conversation began... I lied."
    MC "I would die, my liege."
    "The Emperor's sharp gaze lingered on me, as if searching for any trace of deceit."
    "And technically, I {i}would{/i} die."
    "But what happened afterward—what the monster inside me would become—I kept that part to myself."
    ALCOTT @talk "...I see."
    "The Emperor exhaled, smirking slightly."
    ALCOTT @smile "So the old man wanted Duprey to recover you and your companions' 'dark gifts.'"
    ALCOTT @smile "Likely hoping to use them against me... to reclaim his power."
    ALCOTT @smile "I must admit, I'm {i}almost{/i} impressed."
    ALCOTT @smile "Had his plan been less reckless, it might have even succeeded."
    "I said nothing."
    "I simply waited."
    ALCOTT @talk "Your trial is scheduled for the morning."
    MC @angry "What am I even charged with?"
    show mc at shake
    MC @angry "We saved this city!"
    ALCOTT @talk "Head Inquisitor Marion has charged you with treason and consorting with dark mages."
    MC @think "What?!"
    ALCOTT @talk "You have been accused of spying for the Demorai."
    MC @angry "That's absurd! I fought against them! I saved {i}hundreds!{/i}"
    ALCOTT @talk "It does not matter."
    ALCOTT @talk "Marion doesn't need to be {i}right{/i}—she only needs to convince the lords that you are too great a threat to keep alive."
    MC @talk "...So, will you speak on my behalf?"
    ALCOTT @talk "I cannot."
    ALCOTT @talk "I must remain impartial."
    MC @angry "Then why are you here?"
    ALCOTT @talk "...Because you can still win this trial."
    ALCOTT @talk "Marion will prey on their fear."
    ALCOTT @talk "So {i}you{/i} must prey on their {i}greed.{/i}"
    $ GoalShow(QstJudgementDay, 110)
    show alcott at center_f with ease
    hide alcott with dissolve
    "The Emperor turned away, calling for the guards."
    show mc at center with ease
    MC "...Prey on their hope."
    MC "(Prey on their greed...)"
    scene black with dissolve
    $ CharSetClothes("mc", "normal")
    $ Pause(1.0)
    jump qst_JudgementDay_SiegeOverPrison_ReginaVisit

label qst_JudgementDay_SiegeOverPrison_ReginaVisit:
    "As darkness fell in my cell that night, I waited restlessly for my trial to come."
    if InfGetValue() < 75:
        $ InfChangeBy(75, SetTo = True)
    "The aching agony continued to burn, to scorch my hot blood."
    "I became pale, sweat dripping profusely from me as I dazed in and out of consciousness."
    "Would I even make it to the trial by morning's light?"
    REGINA "... Oh, dear."
    scene regina_prison_loop_1 with dissolve
    $ Pause()
    "I looked up to the black shadow stood beyond the bars of my cell."
    "Shifting and moving, they took form as [regina_ref!t] emerged from the shadows."
    REGINA @sad "You poor thing... You look like you're in so much pain."
    "Her attire was different now, from head to toe she wore black, with a strange pointed hat, and the way she carried herself felt different, it felt... {i}dangerous.{/i}"
    "Her hands reached through the bars."
    REGINA "Poor baby, come... Come to [regina_ref!t]."
    "I slapped her hand away as I pulled back."
    MC @angry "... Who are you?"
    "[regina_ref_cap!t] delicately pulled back her hand, her face slightly crestfellen."
    REGINA @sad "You know who I am... I'm still the same person I've always been."
    MC @angry "Don't lie to me! Not anymore!"
    REGINA @angry "I've been trying to protect you!"
    MC @angry "All these years... All these years I've pretended not to see what's staring me in the face."
    MC @angry "Our whole lives you've been LYING to me and Erika about who and what you really are!"
    MC @angry "No more! Who are you really?"
    MC @angry "...{i}What are you?{/i}"
    "The concerning softness on [regina_ref!t]'s expression faded, as in a moment, she became completely calm and collected, with a cold quality to her tone."
    REGINA @talk "... I was born four centuries ago in the village of Lockshire."
    "I listened intently, feeling the room close in around us."
    REGINA @talk "Times were different then, my people were just another school of magecraft, one often misunderstood... And yet, respected as the others were."
    "I felt the sickly blood turn ice cold as I listened."
    MC @surprised "So it is true then..."
    MC @surprised "{i}You're a dark mage.{/i}"
    REGINA "..."
    MC @angry "... Say it!"
    play sound "audio/cfx/detect_magic.ogg"
    scene regina_prison_loop_1_eyes with dissolve
    $ Pause(0.5)
    scene regina_prison_loop_1 with dissolve
    $ Pause()
    REGINA @talk "... I am."
    "Her confession stung like a hot knife pressed into my very soul."
    MC @surprised "Oh gods..."
    MC @surprised "No... I..."
    MC @sad "How could I not see it?"
    REGINA @talk "I was going to tell you... One day."
    MC @angry "Grghh! And you let Erika become an inquisitor anyway?!"
    MC @angry "Knowing full well what you are!"
    MC @angry "ARE YOU MAD?!"
    REGINA @talk "You and her happiness, is the only thing I care about."
    REGINA @talk "If Erika chooses to hate me, then so be it."
    REGINA @talk "But I knew one way or another, if Erika never learned to channel her magecraft, she would only resent herself."
    MC @angry "Don't try and pretend this is just about OUR happiness!"
    MC @angry "You could have done more! We would have understood!"
    REGINA @angry "And confined you to a life of keeping secrets?"
    REGINA @talk "No... I wanted you both to live a normal life, I wanted you both to be happy and make choices for yourselves, not because of me."
    MC @sad "... Is Regina even your real name?"
    REGINA @talk "I've gone by many names over the years."
    REGINA @talk "But Regina was the name I was born with."
    REGINA @talk "I brought it back because I wanted to hear you two call me it."
    MC @sad "..."
    MC @sad "You're no ordinary dark mage, are you?"
    MC @sad "I've never heard of a dark mage living that long."
    "There was a long pause, before Regina finally answered me."
    REGINA @talk "{i}... I am the witch of Barakan.{/i}"
    "I felt my skin begin to crawl."
    "The witch of Barakan..."
    "A story used to scare children, a fable, more myth then legend."
    "A dark mage so terrible her name once reduced kings to feebling wrecks."
    MC @surprised "You..."
    MC @surprised "{i}You're a monster.{/i}"
    MC @surprised "The things you've done, the-"
    REGINA @talk "I love you... I love you and Erika more than anything in this whole wretched world."
    REGINA @talk "And I would burn it all down for you."
    "Before I could answer her, the sudden pangs of pain came surging through as I clutched at my chest."
    "I groaned in agonizing pain, my teeth gnashing as I began to feel my heart ready to tear from my chest as every muscle tightened at once."
    MC "G-GRGHHHH!"
    REGINA @shock "I'm here, dear."
    REGINA @shock "I've come to help."
    MC @angry "What do you—Grghh!"
    REGINA @talk "I knew the moment you walked through that door... I sensed the creature bound to you."
    "To my sudden shock, [regina_ref!t] pressed her soft, ample breasts up against the cell bars."
    scene regina_prison_loop_1_eyes with dissolve
    $ Pause(0.5)
    scene regina_prison_loop_1 with dissolve
    $ Pause()
    REGINA "I know what you need, dear."
    REGINA "Go on... pull it out."
    MC "But... I need—"
    REGINA "Shhh. I know what you {i}need.{/i}"
    REGINA "Come..."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "[regina_ref!t]'s hand slid over her dress."
    $ PlaySoundRandom("tentFlap")
    scene regina_prison_loop_2 with dissolve
    $ Pause()
    "With a few careful movements, her large, bare breasts were suddenly visible—unashamed, exposed just for me."
    MC "[regina_ref!t]!"
    "A sharp pang of pain shot through my body once more, but I couldn't look away."
    scene regina_prison_loop_2_eyes with dissolve
    $ Pause(0.5)
    scene regina_prison_loop_2 with dissolve
    $ Pause()
    REGINA "Shhh... Stop thinking."
    REGINA "I told you I would do {i}anything{/i} to make you happy, and I meant it."
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop.ogg", 1)
    "With trembling, conflicted hands, I pulled out my cock and began stroking it toward her soft, naked chest."
    "[regina_ref!t] let out a soft, pleased moan as her eyes dropped to my hardening shaft."
    REGINA "That's it, dear..."
    REGINA "Keep stroking it."
    "Even from across the bars, I could smell her—sweet, heady, almost unnatural."
    "Her scent filled my senses, making my cock twitch and throb with growing need."
    "It felt like my own mind and body were betraying me, compelled to obey her as my hand moved faster."
    MC "You... Ahh..."
    MC "How long have you—Mhmm—wanted this?"
    "[regina_ref!t] smiled with a knowing, sultry calm."
    REGINA "I know you've wanted this too."
    MC "N-No! Ahh! It's wrong! I—"
    REGINA "I've always noticed..."
    scene regina_prison_loop_2_eyes with dissolve
    $ Pause(0.5)
    scene regina_prison_loop_2 with dissolve
    $ Pause()
    REGINA "And I've always been prepared to give you whatever you needed."
    "I stroked desperately, my cock burning with need."
    "The more I obeyed her, the more the pain eased—replaced by this overwhelming hunger."
    MC "What are you—Ahh—saying?"
    REGINA "You know what I'm saying, dear."
    "With slow, deliberate movement, her eyes locked on mine like a predator that had finally cornered its prey..."
    $ PlaySoundRandom("tentFlap")
    scene regina_prison_loop_3 with dissolve
    $ Pause()
    "She let the rest of her clothing fall to the ground."
    REGINA "{i}I'll do anything to make you happy...{/i}"
    REGINA "Any—"
    REGINA "Thing."
    "My eyes drifted down, drawn to her exposed womanhood between her thighs, framed by a soft tuft of black hair."
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x2.ogg", 1)
    "Like I'd been possessed, I stroked faster."
    "I couldn't tear my gaze away."
    "I grunted like a wild animal, jerking my cock as I worshipped her with my eyes."
    REGINA "...{i}You can have all of this, if you want it, my love.{/i}"
    REGINA "You've grown into such a fine man."
    MC "Gahh..."
    MC "But you're—"
    REGINA "{i}Whatever you... and that massive cock of yours... want me to be.{/i}"
    REGINA "My love."
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x3.ogg", 1)
    "Her words—dripping in desire and something darker—cut straight through me."
    "Too far gone, I felt myself rushing to the edge."
    MC "{i}*Huff*{/i} [regina_ref!t], I'm—{i}*Huff*{/i}"
    "Regina smirked, licking her lips as she pressed her breasts tighter to the bars."
    REGINA "On my tits, dear."
    REGINA "I want to feel your cum cover me."
    "Overwhelmed by need, I grunted loudly as I finally exploded, shooting thick ropes of cum across [regina_ref!t]'s soft, waiting breasts."
    MC "H-Hrghhh...!"
    "[regina_ref!t] bit her lower lip, trembling with pleasure as the hot seed splashed across her bare skin."
    "A soft moan escaped her lips—sweet, involuntary—as she looked down at her cum-coated chest."
    $ PlaySexFx("audio/sex_sounds/adara_hj_finish.ogg")
    scene regina_prison_finish with flash
    $ Pause()
    $ ReduceInfectionFromSex("regina")
    $ UnlockGalSceneAndGrantXp("regina","prison_visit")
    
    REGINA "...You really needed that, huh?"
    "The pain I'd felt only moments ago drained away, replaced by a crushing wave of exhaustion."
    MC "How did you... {i}*Huff*{/i} know that would—"
    "My eyes grew heavy. My body swayed, legs barely able to keep me standing."
    REGINA "Shhhh... Rest now."
    REGINA "You need your energy for what's to come."
    stop music fadeout 5.0
    "The cell blurred before my eyes. My strength left me."
    scene regina_prison_finish_eyes with dissolve:
        blur 5.0
    $ Pause()
    "The last thing I saw before the world faded to black... were [regina_ref!t]'s glowing, violet eyes watching me with something deeper than desire—"
    scene regina_prison_finish_eyes with dissolve:
        blur 10.0
    "Something ancient."
    scene black with dissolve
    ### ftb
    "And then... darkness."
    REGINA "Wake up, Shyahtan."
    scene cg_novaras_siege_shyahtan_flashback with flash
    REGINA "WAKE UP!"
    jump qst_JudgementDay_TrialStart

########################################################################
# The way the trial functions: 
# The player must talk their way out of the situation. They need more positive points than negative points. 
# If negative points exceed positive points, they get a bad ending (execution).
########################################################################
label qst_JudgementDay_TrialStart:
    play sound "audio/cfx/water_splash.ogg" volume 0.6
    "A sudden splash of cold water shocked my system, forcing a desperate gasp from my lips."
    scene bg_prison_cell 
    show mc at center
    with dissolve
    "I coughed, struggling for breath, my vision swimming as I slowly came to."
    show cg_guard as guard1 at left with dissolve
    "As my surroundings became clearer, I saw them."
    show cg_guard as guard2 at right_f with dissolve
    "Guards. Watching. Spears pointed."
    GUARD "Get up."
    GUARD "Your trial will begin shortly."
    show cg_guard as guard1 at cleft with ease
    "Before I even had the chance to rise, rough hands seized me."
    "Cold metal clamped around my wrists and ankles as I was bound in chains."
    hide mc
    hide guard1
    hide guard2
    with dissolve
    stop ambience fadeout 5.0
    "They dragged me from my cell, my feet barely able to find the ground as I was pulled through the winding halls."
    "At last, we stopped before great, heavy, ornate doors."
    "They groaned open, revealing my fate."
    $ LocNameSetTemp(_("Courtroom"))
    scene bg_court_judge with dissolve
    $ Pause(1.0)
    "The courtroom."
    "To my left, seated in perfect rows, were men in deep blue and purple robes, their faces obscured behind silver masks."
    "Above them, seated upon high stone podiums flanking two burning firepits, sat three more figures."
    "Their robes were red, their masks gleaming."
    show mc at cleft with easeinleft
    "Shoved forward into the center of the chamber, I scanned the crowd for familiar faces."
    "None."
    "Only more masked figures. Watching. Waiting."
    GUARD "Judge Falwind. I present to you the prisoner."
    "The murmurs around the chamber quieted as all eyes turned to me."
    JUDGE_FALWIND "Good morning, prisoner nine-six-one."
    JUDGE_FALWIND "Are you aware of the charges laid against you by Head Inquisitor Marion?"
    menu:
        "I'm charged with treason and consorting with dark mages.": 
            JUDGE_FALWIND "Good. Then you understand the seriousness of the matter."
        "These charges are outrageous! I'm an innocent man!":
            JUDGE_FALWIND "That is for the court to decide, nine-six-one."
        "I'm charged with the crime of having a bigger cock than you all.":
            $ QstJudgementDay().CourtNegative()
            play sound2 "audio/cfx/crowd_boo_long.ogg"
            "Angry murmurs erupted across the courtroom until Judge Falwind slammed his gavel down."
            play sound "audio/cfx/court_hammer.ogg"
            stop sound fadeout 3.0
            JUDGE_FALWIND "I will not tolerate such behavior in my courtroom. I suggest you rethink your actions immediately."

    # All choices continue.
    "The judge skimmed over a stack of papers, stroking his beard as he located the page he sought."
    JUDGE_FALWIND "Hmm..."
    JUDGE_FALWIND "Where is the other one?"
    JUDGE_FALWIND "There was to be one more on trial, was there not?"
    show mc at blurin, cleft_f
    "The doors swung open again."
    "A beaten, disheveled Markus was dragged into the chamber."
    "He was barely conscious."
    show mc at shake
    MC @surprised "MARKUS!"
    "I moved to reach him, but the guards immediately blocked my path."
    JUDGE_FALWIND "Remain still, prisoner nine-six-one."
    show mc at blurin, cleft

    "With a cruel *thud,* they dropped Markus beside me."
    "He coughed up blood, his voice weak."
    MARKUS "{i}*Weakly*{/i} [player_name!t]..."
    show mc at center with ease
    show mc at shake
    MC @angry "How is he supposed to defend himself?!"
    MC @angry "He can barely stand, let alone speak!"
    "Judge Falwind's gaze turned toward the guards."
    JUDGE_FALWIND "Explain prisoner eight-four-one's condition."
    show mc at blurin, center_f
    GUARD "Apologies, Judge Falwind. The prisoner was… uncooperative."
    GUARD "We had to use severe restraint."
    show mc at shake
    MC @angry "YOU BEAT HIM HALF TO DEATH!"
    play sound "audio/cfx/court_hammer.ogg"
    show mc at blurin, center
    "*BANG!*"
    "Falwind's gavel slammed down."

    JUDGE_FALWIND "Control your emotions, nine-six-one, or I shall have you reprimanded further."
    "With a heavy sigh, he glanced back at Markus, who lay crumpled on the floor."
    JUDGE_FALWIND "Given the unfortunate state of your accomplice, we will proceed with your testimony speaking on his behalf."
    show mc at left with ease
    menu:
        "That is outrageous!":
            $ QstJudgementDay().CourtNegative()
            JUDGE_FALWIND "Hold your tongue, nine-six-one! I will not tolerate contempt in my court!"
        "My friend... Can't someone tend to his wounds while I give testimony?":
            $ QstJudgementDay().CourtPositive()
            "The judge hesitated, then waved a hand dismissively."
            JUDGE_FALWIND "Very well. Summon a Mage of Palam to tend to him."
        "I will do as you ask, Judge Falwind.":
            "The judge nodded, satisfied with my compliance."

    JUDGE_FALWIND "Has the prosecution arrived?"
    GUARD "She has, Judge Falwind."
    JUDGE_FALWIND "Send her in."
    "The massive doors opened once more."
    "A figure stepped forward."
    "Not Inquisitor Henvak, as expected."
    "But an older woman. Head Inquisitor Marion."
    show marion at right_f with easeinright
    "Uneasy murmurs rose across the court."
    "Even Judge Falwind stiffened at the sight of her."
    JUDGE_FALWIND "H-Head Inquisitor!"
    MARION "I trust I am not late."
    $ CharMeet("marion", DefaultRel = "rel_enemy")
    JUDGE_FALWIND "E-Er, no, Inquisitor. But… on the paperwork, it states that Inquisitor Henvak was to handle the prosecution."
    MARION "Henvak is indisposed."
    MARION "Given the attention this trial has drawn, I have decided to intercede."
    JUDGE_FALWIND "I… see. But Head Inquisitor, this is most unorthodox. Have you had adequate time to prepare?"
    MARION "I have, your honor."
    "The judge clearly did not like this."
    "But denying Marion's authority was… unwise."
    JUDGE_FALWIND "Very well."
    JUDGE_FALWIND "With all parties present, would the prosecution like to make its opening statement?"
    MARION "I would, your honor."
    "The Head Inquisitor stepped forward."
    "Her voice cut through the chamber, sharp and commanding."
    MARION "Today, the prosecution will prove—beyond doubt—that this creature is the result of dark magecraft!"
    MARION "That it has been consorting with the Demorai."
    MARION "That it is at the very heart of a conspiracy to corrupt this city's highest officials!"
    play sound2 "audio/cfx/crowd_boo_long.ogg"
    "The courtroom exploded in voices."
    "Gasps. Whispers. Outright accusations."
    play sound "audio/cfx/court_hammer.ogg"
    "*BANG!*"
    "*BANG!*"
    JUDGE_FALWIND "ORDER! ORDER!"
    stop sound2 fadeout 3.0
    "As silence returned, he exhaled deeply."
    JUDGE_FALWIND "Prosecutor Marion, these are serious accusations on an already charged case. Do you have evidence to support such claims?"
    MARION "I do, your honor."
    JUDGE_FALWIND "Then let us proceed."
    "His gaze turned to me."
    JUDGE_FALWIND "And you, nine-six-one—"
    JUDGE_FALWIND "What is your opening statement?"
    menu:
        "...My name is not nine-six-one. I am [player_name!t]! And my friends and I saved this city! We are innocent men, wrongly accused!":
            show mc at shake
            MC @angry "We are loyal subjects of Alderay! We fought and bled for this empire a thousand times!"
            MC @angry "And we would do it a thousand times more!"
            $ QstJudgementDay().CourtPositive()
            "There was a murmur of approval among the jury."
            pass

        "Your honor, I will prove our innocence and expose these falsehoods. We are innocent.":
            "My voice was steady. Determined."
            pass

        "You bastards owe us your lives! Without us, NONE OF YOU WOULD BE HERE!":
            $ QstJudgementDay().CourtNegative()
            play sound2 "audio/cfx/crowd_boo_long.ogg"
            "The jury turned against me. Angry whispers spread like wildfire."
            "Marion smiled."
            play sound "audio/cfx/court_hammer.ogg"
            "*BANG!*"
            stop sound2 fadeout 3.0
            "*BANG!*"
            JUDGE_FALWIND "ORDER! I will not tolerate outbursts in this court!"
            "The judge sighed."
            pass

    JUDGE_FALWIND "Head Inquisitor Marion, present your first witness."
    MARION @smile "Gladly, your honor."
    MARION @talk "The prosecution calls…"
    MARION @talk "Captain Nyx of the City Guard."
    show marion at center_f with easeinright
    show marion at blurin, center
    "Quiet murmurs rose up as the doors swung open and Captain Nyx, stood proud, made her way silently to the stand, refusing to break her utterly neutral expression."
    show nyx at right_f with easeinright
    MARION @talk "Captain Nyx... Could you tell us more about your rank and what your duty entails?"
    NYX @talk "I am Captain of the city guard of Novaras, I am charged with keeping the city safe both internally and externally from threats, and maintaining peace within the city's walls."
    MARION @smile "I see..."
    MARION @talk "And tell me, what are you direct resonsibilites when it pertains to inquisitor business?"
    NYX @angry "... To report anything suspect of Dark magecraft to the inquisition at once, or anything related to a Demorai pressence in the city."
    MARION @smile "Interesting..."
    MARION @talk "So, tell me."
    MARION @talk "Are these your signatures on these reports?"
    "In her hands, the head inquisitor waved about a series of papers before throwing them down in front of Nyx, who uncomfortably inspected them."
    NYX @angry "Yes... This is my signature."
    MARION @angry "Why then, did you choose to send false reports when asked to investigate prisoners nine-six-one and eight-four-one?"
    "There was a heavy, long pause."
    JUDGE_FALWIND "... Captain Nyx, the prosecution has asked you-"
    NYX @angry "Everything I have done, I have done to defend this city."
    NYX @angry "The guard is woefully desperate and I-"
    MARION @angry "You chose to dangerously override the authority of all others and directly disobey the chain of command!"
    MARION @angry "Your reckless decisions could have endangered everyone in this city!"
    NYX @angry "EVERYONE IS ALREADY ENDANGERED!"
    "The gavel came down once more."
    JUDGE_FALWIND "Control yourself, please."
    MARION @angry "I submit, that Captain Nyx directly defied orders, disobeying the chain of command and endangered everyone."
    JUDGE_FALWIND "Inquisitor Marion, with all due respect, this is not the Captain's trial-"
    MARION @angry "Captain Nyx recognized the potential power of this dark, magecraft abomination and chose to strike a bargain with it!"
    MARION @angry "It would serve her bidding and earn her prestige, in return, she actively has chose to hide it's secrets and protect it whenever she could!"
    MARION @angry "The two cases are inexplicably linked!"
    JUDGE_FALWIND "That be so... I must ask you keep the focus more towards those on trial, inquisitor from now on."
    JUDGE_FALWIND "Captain Nyx's trial is a seperate matter."
    MARION @angry "Tsch..."
    MARION @smile "Of course, your honor."
    hide marion with easeoutright
    "Judge Falwind's eyes lifted towards me."
    JUDGE_FALWIND "Would you like to ask any questions to the witness?"
    $ tmpvar = [1, 2]
    menu qst_JudgementDay_Trial_questions:
        "Captain Nyx... Could you tell us more about the state of the city guard?" if 1 in tmpvar:
            $ tmpvar.remove(1)
            NYX @talk "The state of the guard is in complete disorrey."
            NYX @talk "We are woefully short of everything, including men."
            MC @talk "And why have you been unable to fix these issues, Captain? Isn't it your job?"
            NYX @talk "Resources are given to the city guard {i}last,{/i} and request for supplies and men often takes months to arrive."
            MC @talk "Could your explain your actions in recruiting my help?"
            "There was another long pause."
            NYX @talk "I weighed heavily on the thought of what report to send."
            NYX @talk "But I {i}believed{/i}, you and your friend were good men, who served and fought bravely in the scouts."
            NYX @talk "And in a moment of desperation, or perhaps madness, I took a risk on the two of you."
            MARION @angry "She admits it!"
            JUDGE_FALWIND "Order! Inquisitor Marion!"
            JUDGE_FALWIND "The defence is not done with it's line of questioning."
            MARION @angry "Tsch..."
            JUDGE_FALWIND "Captain Nyx, you do understand you are admitting to forgery and-"
            NYX @angry "If I could go back, I would make the exact same choices!"
            NYX @smile "... They may not be human, but [player_name!t] and his companions have done thankless work to keep this city safe,"
            NYX @smile "And they fought as bravely as any man during the siege!"
            NYX @smile "Without them, this city would have fallen..."
            "Captain Nyx's eyes turned to the jury."
            NYX @talk "Who amongst you would have been brave enough to stand against the defiler, against Zanarak?"
            NYX @angry "Because {i}they{/i} did."
            $ QstJudgementDay().CourtPositive()
            jump qst_JudgementDay_Trial_questions

        "Captain Nyx, I am accused of being a Demorai spy... during the siege, whose side did I fight with?" if 2 in tmpvar:
            $ tmpvar.remove(2)
            NYX @smile "... You fought for Alderay."
            NYX @smile "And you fought with honor."
            $ QstJudgementDay().CourtPositive()
            jump qst_JudgementDay_Trial_questions

        "No further questions, your honor.":
            pass

    $ tmpvar = {}
    if QstGetProgress(RomanceNyx) >= 3 and RomanceNyx().route == "love":
        JUDGE_FALWIND "Very well then, let us proceed on with-"
        show marion at center_f with easeinright
        $ Pause(0.1)
        show marion at blurin, center
        MARION @angry "Objection!"
        JUDGE_FALWIND "... Do you have a further line of questioning, inquisitor?"
        MARION @smile "{i}I do.{/i}"
        MARION @smile "Captain Nyx... {i}Are you in love with the defendant?{/i}"
        "There was an outburst of confusion amongst the jury, as even Nyx appeared flustered."
        NYX @shock "I- What?"
        MARION @smile "What is your relationship with the defendent."
        "Nyx cheeks burned red."
        NYX @blush "I..."
        NYX "..."
        NYX @blush "We have grown closer than I anticipated, yes, we-"
        MARION @angry "I submit to the court full testimony that you were seen in a tavern with prisoner nine-six-one."
        MARION @angry "I submit that Captain Nyx's testimony is clearly blinded by her affections for the prisoner!"
        NYX @angry "I have told nothing but the truth!"
        MARION @angry "If that is so, why did you not reveal your prior relationship to the defendent?"
        NYX @sad "...I..."
        MARION @smile "No further questions, your honor."
        hide marion with easeoutright

        $ QstJudgementDay().CourtNegative()

    JUDGE_FALWIND "If there are no further questions, you may leave the stand, Captain Nyx."
    NYX @shock "But—"
    JUDGE_FALWIND "That will be all, Captain Nyx."
    hide nyx with easeoutright
    "With a heavy sigh, Nyx stepped down from the witness stand."
    "Our eyes met briefly before she was escorted away."
    JUDGE_FALWIND "The court calls its next witness—Royal Mage Kylisa Jadeway."
    show kylisa at right with easeinright
    "As the doors swung open, the royal mage, Kylisa Jadeway, entered in silent, measured steps."
    "She made her way toward the witness stand, her dark robes pristine, her expression unreadable."
    MARION @talk "Lady Jadeway, you have read the official reports regarding the recent siege, correct? Specifically, this creature's involvement?"
    KYLISA @talk "I have."
    MARION @talk "In your expert opinion, could this creature be the result of dark magecraft? Or perhaps... a Demorai abomination?"
    "Kylisa's tone remained even and composed."
    KYLISA @talk "Based on extensive comparisons with my research into dark magecraft and Demorai sorcery, I must confess…"
    KYLISA @talk "It is highly improbable that these creatures have no connection to dark magecraft."
    MARION @talk "And how did you verify this {i}research?{/i}"
    KYLISA @talk "As the court mage, I am granted exclusive access to forbidden texts on dark magic, as well as reports on Demorai magecraft."
    KYLISA @talk "All materials are handled under strict supervision, with safeguards to minimize corruption risks."
    MARION @talk "And your findings are certain?"
    KYLISA @talk "While not absolute, the similarities between this case and past transfiguration incidents involving dark magecraft are... striking."
    MARION @smile "I see."
    MARION @smile "The prosecution rests its case."
    JUDGE_FALWIND "Would the defense like to question the witness?"
    menu:
        "How is it fair that your research is withheld from this trial?":
            MARION @angry "Objection, your honor!"
            MARION @angry "Allowing dark magecraft texts into this courtroom would be reckless, if not outright dangerous!"
            MC @angry "So we're just supposed to take one person's word without any ability to challenge their findings?"
            MARION @angry "Lady Jadeway is one of the finest mages in Alderay, if not all of Mirnos."
            $ QstJudgementDay().CourtNegative()
            JUDGE_FALWIND "I must rule in favor of the prosecution."
            JUDGE_FALWIND "Lady Jadeway's expertise is beyond reproach, and her research is unlikely to be understood by this court."
            JUDGE_FALWIND "Unless you have proof that her findings are flawed, I suggest you drop this line of questioning."
            menu:
                "How can we be sure she hasn't been corrupted?":
                    MARION @angry "This is outrageous!"
                    $ QstJudgementDay().CourtNegative()
                    JUDGE_FALWIND "A mage of Kylisa's standing is regularly checked for corruption."

                "I shall move on, your honor.":
                    JUDGE_FALWIND "Continue."

        "Lady Jadeway… did you not already examine me and Markus for signs of dark magecraft?":
            KYLISA @talk "Yes, I conducted an examination."
            KYLISA @talk "There was no detection of dark magecraft on either you or your friend."
            $ QstJudgementDay().CourtPositive()
            MC @think "Doesn't that clear us, then?"
            KYLISA @talk "Not entirely."
            KYLISA @talk "Magecraft of this level could be… concealed."
            menu:
                "Have you ever personally encountered such a high level of dark magecraft before?":
                    KYLISA @talk "Only once."
                    KYLISA @talk "There are only a handful of recorded cases in history."
                    KYLISA @talk "Rare... but not impossible."

                "But I possess no magecraft {i}at all.{/i}":
                    KYLISA @scared "You... possess no magecraft?"
                    KYLISA @talk "But... you must—"
                    KYLISA @talk "Your bloodline has produced dozens of magecraft users!"
                    MC @talk "Neither I nor Markus have any aptitude for magecraft."
                    MC @talk "You are free to verify this."
                    "A murmur spread through the courtroom as Kylisa hesitated, glancing at the prosecution."
                    MARION @angry "This is—"
                    "Before Marion could finish, Kylisa rose from her seat."
                    "She raised her staff."
                    play sound "audio/cfx/detect_magic.ogg"
                    show vfx_magick_glow with flash:
                        anchor (0.5, 0.5)
                        pos (0.93, 0.19)
                        zoom 0.6
                    "A brilliant white flame erupted from its tip, swirling with a dark core."
                    "All around the room, traces of magecraft flickered into view."
                    hide vfx_magick_glow with dissolve
                    "Those with stronger magical affinities burned brighter."
                    "Markus and I had no such glow."
                    "The magic faded. Silence filled the courtroom."
                    KYLISA @scared "You... possess no magecraft."
                    KYLISA @scared "But... how? I was certain—"
                    $ QstJudgementDay().CourtPositive()
                    MARION @angry "This proves nothing!"
                    MARION @angry "Creatures can be born of dark magecraft yet have no magical affinity!"
                    KYLISA @talk "But the core… If they were born of magecraft, they should still resonate with it."

    MC "No further questions, your honor."
    JUDGE_FALWIND "That concludes questioning for this witness."
    "Kylisa hesitated, as if she wished to say more."
    show kylisa at nod
    hide kylisa with easeoutright
    "But in the end, she simply gave a small bow and stepped down."
    JUDGE_FALWIND "The next witness to take the stand is—"
    MARION @smile "Prisoner Nine-Six-One."
    "The murmurs in the courtroom grew louder. People turned to each other, whispering at this unexpected move."
    JUDGE_FALWIND "Very well. Prisoner Nine-Six-One, you will take the stand."
    show mc at right with easeinleft
    show mc at blurin, right_f
    "Shackles clanking, I stepped forward. Eyes locked onto me. Some with curiosity, others with disgust."
    show marion at cleft with dissolve
    "Marion began to pace, her footsteps measured."
    MARION @smile "Tell us—what happened during your battle with the great terror?"
    MARION @talk "{i}With Zanarak.{/i}"
    "The moment she spoke his name, a visible wave of dread spread through the court."
    "Whispers turned into low, fearful voices. Even hardened men shifted in their seats."
    "Judge Falwind slammed his gavel."
    play sound "audio/cfx/court_hammer.ogg"
    JUDGE_FALWIND "Silence!"
    JUDGE_FALWIND "Proceed."
    MC @talk "...We were sent to investigate a break in the wall's defenses."
    MC @talk "Supplies weren't reaching the soldiers. No word from the defenders."
    MC @talk "We thought we'd find nothing more than some minor sabotage."
    MC @sad "We were wrong."
    MC @talk "Zanarak was waiting for us."
    MARION @talk "A perilous moment. You must have been… {i}terrified.{/i}"
    MC @sad "...Yes."
    MARION @talk "And yet—despite this terror—you still managed to defeat Zanarak?"
    menu:
        "We fought hard and pushed him back.":
            MARION @smile "Really?"
            MARION @smile "Then why do our reports say you were found half-dead on the wall alongside your companions?"
            MC @surprised "U-Uhh... We were exhausted after the fight, we—"
            $ QstJudgementDay().CourtNegative()
            MARION @angry "You were {i}defeated.{/i} Cease your lies!"

        "Actually... We lost.":
            MARION @fury "Is that so?"

    MARION @smile "You see, Nine-Six-One, our reports indicate a {i}blinding light{/i} banished Zanarak from the wall."
    "She paused for effect, letting the words sink in."
    MARION @smile "A light caused by {i}dark magecraft.{/i}"
    MC "..."
    MARION @smile "A dark mage you know quite well."
    MARION @smile "[regina_ref_cap!t]... Is that what you call her?"
    "The courtroom exploded into murmurs. Some gasped. Others looked toward me in outright suspicion."
    "Marion turned the knife deeper."
    MARION @smile "Do you deny it?"

    menu:
        "I had no idea she was a dark mage!":
            show mc at shake
            MC @surprised "I had no idea!"
            MARION @talk "How could you {i}not{/i} know? Are you a fool?"
            MARION @angry "I submit that you DID know, and that you aided her in concealing her secret—just as she aided in concealing {i}yours!{/i}"
            menu:
                "Neither did your own inquisitor!":
                    MARION @think "Hm?"
                    MC @angry "Neither I nor Erika knew the truth!"
                    MARION @angry "Rest assured, the inquisition will be questioning {i}her{/i} soon enough!"
                    "I pondered the thought. How {i}did{/i} I not know? I had {i}suspected something{/i} for so long... yet I had ignored it."
                    "I lifted my head, locking eyes with Marion."
                    MC "The eyes can't see what the heart refuses to believe."
                    "A few members of the court murmured at my words, though I wasn't sure if it swayed them."
                "She hid it from me!":
                    $ QstJudgementDay().CourtNegative()
                    MARION @angry "And the court is supposed to simply believe that?"

        "I refuse to answer.":
            MARION @smile "Ah. Silence."
            MARION @smile "Silence speaks volumes, doesn't it, your honor?"
            $ QstJudgementDay().CourtNegative()
            "Judge Falwind frowned but said nothing."

    MARION @angry "Furthermore!"
    MARION @angry "I have in my possession the official report on the doomed {i}scout expedition.{/i}"
    "She held up a thick document, waving it in front of the jury."
    MARION @talk "The details are {i}censored{/i}, but one thing is clear—a {i}dark mage{/i} was directly involved in whatever {i}foul transformation{/i} turned you into this."
    menu:
        "That proves nothing.":
            MARION @angry "It proves that your entire existence is {i}corrupt!{/i}"
        "What about the rest of my squad? Are they on trial, too?":
            MARION @think "Hmph."
            MARION @talk "We will deal with the others in due time."
    hide marion with easeoutright

    # cont
    JUDGE_FALWIND "I see... does the defense have any witnesses to call?"

    show mc at cleft_f with easeinleft
    $ Pause(0.1)
    show mc at blurin, cleft

    # exhaustive
    $ tmpvar = []
    if QstIsComplete(QstHighFasion):
        $ tmpvar.append("divine")
    if IsGoalComplete(QstJudgementDay, 30):
        $ tmpvar.append("sophira")
    if not QstTheComingStorm().GaveAdaraMoneyForEscape:
        $ tmpvar.append("adara")
    if CharIsMet("nijah") and CharIsAlive("nijah"):
        $ tmpvar.append("nijah")

    menu qst_JudgementDay_TrialStart_SummonMenu:
        "Summon Sister Divine" if "divine" in tmpvar:
            $ tmpvar.remove("divine")
        
            "Sister Divine entered, her presence causing a hush to fall over the room."
            show divine at right_f with easeinright
            "Even the judges bowed their heads in respect as she approached."
            JUDGE_FALWIND "Sister Divine, you have been called to testify on behalf of the defendant."
            JUDGE_FALWIND "Do you believe this creature to be a threat?"
            "Sister Divine closed her eyes, inhaling deeply."
            DIVINE @talk "No."
            DIVINE @talk "I have known this man. I have seen his heart."
            DIVINE @talk "And I have witnessed firsthand his courage and mercy."
            $ QstJudgementDay().CourtPositive()
            "Some in the jury murmured approvingly."
            JUDGE_FALWIND "Does the prosecution wish to question the witness?"
            if QstIsActive(RomanceDivine) or QstIsOver(RomanceDivine):
                MARION @angry "Actually—I do."
                show marion at center_f with easeinright
                $ Pause(0.1)
                show marion at blurin, center
                "Gasps rippled through the court as Marion's lips curled into a sinister smile."
                MARION @smile "Tell me, Sister—"
                MARION @smile "{i}When did your affair with the defendant begin?{/i}"
                "The room exploded into murmurs."
                play sound "audio/cfx/court_hammer.ogg"
                JUDGE_FALWIND "Order! ORDER IN THE COURT!"
                DIVINE @shock "I—"
                "Sister Divine looked around the courtroom—trapped."
                MARION @talk "He seduced you, didn't he?"
                DIVINE @shock "No!"
                MARION @smile "She admits it! The creature {i}corrupted{/i} a holy woman!"
                $ QstJudgementDay().CourtNegative(2)
                "The jury erupted in outrage."
                play sound "audio/cfx/court_hammer.ogg"
                JUDGE_FALWIND "Order! ORDER!"  
                JUDGE_FALWIND "BE SILENT, OR I WILL HAVE YOU REMOVED FROM THIS COURT!"
                MARION @smile "Your honor, I formally request that Sister Divine's testimony be stripped from the record."
                DIVINE @angry "WILL I BE ALLOWED TO SPEAK FOR MYSELF?"  
                JUDGE_FALWIND "Sister Divine, please answer the question clearly and directly."  
                JUDGE_FALWIND "Do you know the defendant carnally?"  
                DIVINE @angry "It's not illegal for a mage of Palam to—"  
                JUDGE_FALWIND "Sister Divine."  
                JUDGE_FALWIND "The question. Please."  
                DIVINE @sad "... Y-Yes."  
                DIVINE @shock "BUT—"  
                hide marion with easeoutright
                play sound "audio/cfx/court_hammer.ogg"
                "The gavel came crashing down."
                JUDGE_FALWIND "I am sorry, Sister Divine, but I must strip your testimony from the trial."  
                JUDGE_FALWIND "And further condemn the wickedness of the defendant for his most cruel seduction!"  
                show divine at shake
                DIVINE @angry "I HAVE A VOICE!"  
                DIVINE @angry "It is not a crime for me to lay with a man, and I am not some foolish woman who would let it sway my opinion in ANY court!"
                DIVINE @angry "They fought bravely! They—"
                JUDGE_FALWIND "That's enough, Sister Divine."  
                JUDGE_FALWIND "It is clear you are not thinking clearly, and your testimony remains stripped."
                JUDGE_FALWIND "Now please, Sister, I do not wish to have the guards forcibly remove you from the stand..."
                hide divine with easeoutright
                "Sister Divine opened her mouth to protest, but stopped herself."  
                "Burning with shame and rage, her emotions silenced by the court, she turned away and left the stand."  
                "Her eyes met mine—a flicker of anger, then sorrow, before she looked away."  
                JUDGE_FALWIND "Now then, let us proceed..."
            else:
                MARION @talk "No, your honor."

            jump qst_JudgementDay_TrialStart_SummonMenu

        "Summon Lady Sophira Marginott" if "sophira" in tmpvar:
            $ tmpvar.remove("sophira")
            "The court doors swung open, and Lady Sophira Marginott entered, her posture regal and her expression unreadable."  
            show sophira at right_f with easeinright
            JUDGE_FALWIND "Lady Marginott, the court trusts you are well?"  
            SOPHIRA @talk "I am, my lord."  
            JUDGE_FALWIND "The defense has summoned you as a witness. Will you recount the events of the siege?"  
            SOPHIRA @talk "Of course, if the court so pleases."  
            scene black with dissolve
            "Lady Marginott recounted the horrific ordeal of the siege, detailing the chaos and bloodshed."  
            "Then, she arrived at the moment she met us."  
            scene bg_court_judge 
            show sophira at right_f
            show mc at cleft
            with dissolve
            SOPHIRA @sad "I must admit..."  
            SOPHIRA @sad "When I first laid eyes upon them, I thought them monsters."
            SOPHIRA @sad "I believed they had come to kill us all."
            SOPHIRA @sad "... But—"  
            "Sophira hesitated, scanning the room."  
            "Praising a monster? Even one who saved her?"  
            "The scandal alone could ruin her standing."  
            SOPHIRA @talk "They fought as bravely, and as valiantly, as any knight in the realm."  
            "A ripple of murmurs spread through the court."  
            "A noblewoman... speaking on behalf of a monster?"  
            SOPHIRA @talk "I can scarcely believe that the men before me today are the same creatures from that night."  
            SOPHIRA @talk "But I would take stock of their courage before rendering judgment."  
            JUDGE_FALWIND "Thank you, Lady Marginott."
            $ QstJudgementDay().CourtPositive()
            JUDGE_FALWIND "Does the prosecution have any questions for the witness?"  
            MARION @angry "... No, your honor."  
            MARION @talk "None at this time."  
            JUDGE_FALWIND "Then the witness is dismissed."  
            hide sophira with easeoutright
            "With a final nod, Lady Marginott left the stand, casting me a sympathetic smile before stepping away."
            jump qst_JudgementDay_TrialStart_SummonMenu

        "Summon Adara" if "adara" in tmpvar:
            $ tmpvar.remove("adara")
            show marion at right_f with easeinright
            MARION @angry "Hold."  
            MARION @angry "I object to this witness's testimony."  
            JUDGE_FALWIND "On what grounds?"  
            MARION @talk "The witness is a childhood friend of the accused and has openly admitted to harboring deep affections for him."  
            MARION @talk "Any testimony she delivers is undoubtedly tainted by personal bias."  
            MARION @talk "Furthermore, she is a commoner. Are we truly to weigh the words of a commoner against the ruling elite of this court?"  
            JUDGE_FALWIND "...Hmm."  
            JUDGE_FALWIND "I must rule in favor of the prosecution."
            JUDGE_FALWIND "The court will not hear from Ms. Adara today."
            hide marion with easeoutright
            JUDGE_FALWIND "Does the defense have another witness to call?"  
            jump qst_JudgementDay_TrialStart_SummonMenu

        "Summon Nijah" if "nijah" in tmpvar:
            $ tmpvar.remove("nijah")
            show marion at right_f with easeinright
            MARION @angry "Objection, your honor!"
            MARION @talk "Only Alderian citizens may give testimony in a trial of this magnitude."  
            MARION @talk "And the opinion of a Ramonian whore is hardly worth considering."
            JUDGE_FALWIND "Agreed. I cannot allow a foreigner to testify in this court."
            hide marion with easeoutright
            JUDGE_FALWIND "Does the defense have a different witness to call forth?"  
            jump qst_JudgementDay_TrialStart_SummonMenu

        "I have no further witnesses to call":
            JUDGE_FALWIND "Very well."
            JUDGE_FALWIND "The jury shall now discuss your sentencing in private."
            JUDGE_FALWIND "A verdict shall be rendered upon your return to this court."
            "The gavel slammed down, sealing my fate—for better or worse."
            pass

    # calculate
    if QstJudgementDay().TrialPoints["pos"] < QstJudgementDay().TrialPoints["neg"]:
        jump qst_JudgementDay_TrialOver_Execution
    else:
        jump qst_JudgementDay_TrialOver_Banishment

##########################################################################################################
# BAD END - EXECUTION (If Negative Points Exceed Positive, or a Draw)
label qst_JudgementDay_TrialOver_Execution:
    scene black with dissolve
    "Dragged away from the court in chains once more alongside Markus… I waited. And waited. And waited."
    "Until at last, I was dragged back into the silent courtroom to await judgment."
    scene bg_court_judge 
    show mc at cleft
    with dissolve
    JUDGE_FALWIND "Having consulted the jury's verdict, and given the overwhelming evidence, I shall now render judgment."
    JUDGE_FALWIND "For the crime of treason, and for consorting with dark magecraft, we find you…"
    "... A heavy silence filled the chamber, the entire court holding its breath in anticipation."
    JUDGE_FALWIND "GUILTY!"  
    show mc at shake
    MC @surprised "WHAT?!"  
    
    MC @angry "No! I—"  
    show mc at shake
    JUDGE_FALWIND "You and your companions are hereby sentenced to death!"
    show mc at center with ease
    MC @surprised "Death?!"
    show mc at shake
    MC @angry "WE SAVED THIS CITY! WE—"

    play sound2 "audio/cfx/darkness_erupt.ogg"
    $ HideUI(True)
    scene cg_novaras_siege_trial_execution with flash
    $ Pause()
    jump defeat_generic

#####################################################################################################
# GOOD END - BANISHMENT (If Positive Points Exceed Negative)
label qst_JudgementDay_TrialOver_Banishment:
    scene black with dissolve
    "Dragged away from the court in chains once more alongside Markus… I waited. And waited. And waited."
    "Until at last, I was dragged back into the silent courtroom to await judgment."
    scene bg_court_judge 
    show markus at left
    show mc at center
    with dissolve
    JUDGE_FALWIND "I must apologize for the delay in this matter, the jury deliberated for much longer than expected."
    JUDGE_FALWIND "On the charge of treason, given the severe lack of evidence, you and your companions are found…"
    JUDGE_FALWIND "NOT GUILTY!"
    "A ripple of applause spread through the jury, and for a fleeting moment, relief washed over me."
    "... Until the judge brought his gavel down once more."
    play sound "audio/cfx/court_hammer.ogg"
    JUDGE_FALWIND "SILENCE!"
    JUDGE_FALWIND "I have not finished!"
    "The room fell into an uneasy hush, my body tensing once more."
    JUDGE_FALWIND "… On the charge of association with dark magecraft, however…"
    JUDGE_FALWIND "The jury has been unable to reach a verdict."
    show marion at right_f with easeinright
    MARION @angry "Then under Article 46 of the Dark Magecraft Law, they are to be retried in an inquisition-only trial!"
    show mc at shake
    MC @angry "That's absurd! Where is the justice in sending us to a court where the verdict is ALWAYS guilty?!"
    MARION @angry "Hold your tongue, dark spawn!"
    MC @angry "You know it's true—and so does everyone here!"
    "The jury erupted into arguments, their voices clashing as the courtroom descended into chaos."
    play sound "audio/cfx/court_hammer.ogg"
    "Judge Falwind smashed his gavel down repeatedly, but the room was already spiraling out of control."
    "At some point, one of the jury members threw a punch at another, and soon, the entire courtroom broke into a small brawl."
    play sound "audio/cfx/court_hammer.ogg"
    JUDGE_FALWIND "ORDER! ORDER!"
    "Guards rushed in to break apart the scuffling jury members."
    "Then, suddenly, the grand doors of the courtroom swung open with force."
    hide markus with easeoutleft
    show mc at left with easeoutleft
    GUARD "Presenting Her Royal Highness, Princess Cecilia!"
    show cecilia at center with dissolve
    "At once, the chaos ceased."
    "A reverent silence filled the air as the Princess stepped forward, graceful and composed."
    "Many members of the jury immediately fell to their knees in her presence."
    menu:
        "Bow.":
            show mc at nod
            "I did my best to bow graciously, though the chains binding my limbs made it an awkward, stiff gesture."  
        "Don't bow.":
            "I remained standing as the Princess approached, meeting her gaze directly."
    
    JUDGE_FALWIND "Princess Cecilia! A court such as this is no place for—"  
    PRINCESS_CECILIA "You will be silent, good judge."  
    "Judge Falwind quickly shut his mouth as the Princess turned to face the entire court."  
    PRINCESS_CECILIA "I have come to speak on behalf of the defendants."  
    JUDGE_FALWIND "P-Princess, you—"  
    PRINCESS_CECILIA "Without their aid, I would not be standing here today."  
    PRINCESS_CECILIA "They fought not only to retrieve my brother during the siege but also to save my life."  
    "A murmur rippled through the chamber."
    PRINCESS_CECILIA "Even the Silver Knight himself has offered written testimony in their defense."
    PRINCESS_CECILIA "Therefore, I ask for a royal pardon for these creatures."
    MARION @talk "Your Highness… The jury cannot determine if these beings are creations of dark magecraft."
    MARION @talk "The law, as decreed by both the Emperor and your father, the late King, is final."
    JUDGE_FALWIND "... Perhaps, there is a compromise."  
    MARION @fury "A compromise?"  
    JUDGE_FALWIND @talk "In light of these highly unusual circumstances, and given the testimony of the Princess herself…"
    JUDGE_FALWIND "I hereby decree that you, and your companions, are to be {b}banished{/b} from the city of Novaras."
    MC @surprised "... Banished?"

    # if there are chars other than markus and erika in that list
    if len(QstJudgementDay().CharactersWhoWereAtTheWall) > 2:
        JUDGE_FALWIND "As for your other companions..."
        if "myu" in QstJudgementDay().CharactersWhoWereAtTheWall:
            $ QstJudgementDay().ImprisonedCharacters.add("myu")
            JUDGE_FALWIND "The slimelark companion of yours will remain confined."
        if "elena" in QstJudgementDay().CharactersWhoWereAtTheWall:
            $ QstJudgementDay().ImprisonedCharacters.add("elena")
            JUDGE_FALWIND "The wolf girl will stay confined too."
        JUDGE_FALWIND "We will conduct further questioning later."
        play sound "audio/cfx/court_hammer.ogg"
        "The gavel slammed down with finality."

    JUDGE_FALWIND "... I pray that, with time, and the Emperor's forgiveness, you may return."
    JUDGE_FALWIND "But for now, for the safety of all Alderay, we must cast you out."
    scene black with dissolve
    $ Pause(1.0)
    $ QstComplete(QstJudgementDay)
    scene cg_novaras_siege_trial_banished with dissolve
    $ Pause()
    scene black with dissolve
    jump qst_JudgementDay_PostQuestTravelToHamun

#######################################################################################################################################################
# Scene cuts to Markus and MC sat outside Ves' tent
label qst_JudgementDay_PostQuestTravelToHamun:
    $ Pause(1.0)
    $ TimeAdvTo(TIME_NOON)
    $ CharHeal("markus")
    $ PartyAddChar("markus", Silent = True)

    show text _("{size=150}ACT 2{/size}") with dissolve:
        yalign 0.5
    $ Pause()
    hide text
    $ HideUI(False)
    $ Pause(1.5)
    if InfectionModule().CurrentValue < 35:
        $ InfChangeBy(35, SetTo = True)
    
    $ LocSet("ves_camp")
    $ LocNameReset()
    $ LocFlush()
    show markus at right_f
    show mc at left
    $ AutoMus(True)
    $ AutoAmb(True)

    with dissolve
    MC "..."
    MARKUS "..."
    show markus at shake
    MARKUS "WELL THIS IS FUCKING SHIT, ISN'T IT?"
    "Markus snapped his head towards me."
    MARKUS "THIS IS YOUR BLOODY FAULT!"
    MC @angry "ME?!"
    MARKUS @angry "Ooooh, we just had to be big fucking heroes!"
    MARKUS @angry "Just had to stick around for the battle and save the day!"
    MARKUS @angry "Now look at us! Don't even have a bucket to piss in!"
    MC @angry "WE'RE IN THE MIDDLE OF THE DESERT YOU FUCKING MORON! YOU CAN PISS WHEREVER YOU WANT!"
    MC @angry "AND WHAT SHOULD WE HAVE DONE THEN, HMM?"
    MC @angry "Wait for everyone to fucking die while we drank ourselves to death in Newyark waiting for the end?"
    MARKUS @angry "OH YES, BECAUSE THAT'S SO MUCH WORSE THAN ROASTING TO DEATH IN THE DESERT!"
    MC @angry "I still don't hear any brilliant solutions coming from you!"

    # Variant 1 - If Ves had died during the prologue
    if QstFromAnotherWorld().LetVesDie:
        show markus at blurin, right_f
        MARKUS @think "...We're lucky we at least found this old campsite."
        show markus at blurin, right
        MARKUS @talk "Who do you think it belonged to?"
        MC @talk "I don't know... Whowever they were, they were well prepared at least."

    # Variant 2 - If Ves survived 
    else:
        $ PlaySoundRandom("tentFlap")
        "The flap of Ves' tent opened as she stepped out towards us."
        show ves at center with dissolve
        VES @talk "Do you two intend to spend all day sitting here sulking?"
        MARKUS @angry "Do you intend to stand there lecturing us all day, {i}orc?{/i}"
        VES @angry "Tsch! Then do as you wish, {i}human.{/i}"
        show ves at blurin, center_f
        "Ves' eyes met mine."
        VES @talk "... I'll prepare some stew shortly."
        MC @talk "Thanks."
        VES @angry "Let's hope your friend apppreciates my {i}'orc-ish'{/i} food."
        hide ves with dissolve
        "Markus said nothing, ignoring the comment entirely."

    # Both variants continued
    show markus at cright_f with easeinright
    show mc at cleft with easeinleft
    MARKUS @sad ".... So what now, then?"
    MARKUS @think "Inma's probably the closest city, but-"
    MARKUS @sad "Inma's probably the least safe place in all of Alderay right now."

    # If players companions are imprisoned (Myu and/or Elena)
    if "myu" in QstJudgementDay().ImprisonedCharacters:
        MC @sad "... I hope Myu is alright."
        MARKUS @talk "I'm sure she's fine."
        MARKUS @smile "She's probably convinced this is some kind of elaborate game."
        MC @sad "{i}I hope so...{/i}"
        MC @sad "The last thing I want is her confused and not understanding what's going on."
        "Markus offered a consoling hand on my shoulder."
        MARKUS @talk "We will get her back, my friend."

    if "elena" in QstJudgementDay().ImprisonedCharacters:
        MC @sad "... Elena."
        MARKUS @talk "That girl is resourceful."
        MARKUS @smile "Gods! She's probably already escaped!"
        MC @talk "I hope so, Markus... I really do."

    "As we sat and pondered our next move, there, across the horizon, a robed figure made their way towards us."
    "I tapped at Markus' shoulder."
    MC @serious "Do you see that?"
    show markus at blurin, cright
    "Markus looked over towards the figure, their silhouette wavy in the heat as they drew closer."
    MARKUS @talk "I do..."
    MARKUS @talk "Do you think they're a bandit, or..."
    MC @talk "What would a bandit be doing wandering out this way in the desert on their own?"

    show mc at left with ease
    show markus at cleft with ease

    "Slowly, as the hooded figure drew closer, they stopped a few feet away from us."
    "Grabbing at their hood, they pulled it back to reveal..."

    $ CharSetVar("kiara", "default_look", "hooded")

    $ CharSetPortrait("kiara", "images/characters/kiara/portrait_hooded.webp")
    $ CharSetClothes("kiara", "normal")
    show kiara at cright_f with easeinright

    KIARA @happy "Did ya boys miss me?"
    MARKUS @shock "KIARA?!"
    KIARA @happy "Glad to see you both made it out alive."
    MC @surprised "What are you doing here?"
    KIARA @talk "It's time... My mistress asked me to escort you both to the free city of Hamun."
    KIARA @happy "Come, follow me."
    show kiara at blurin, cright
    MARKUS @angry "Hold on a minute!"
    show kiara at blurin, cright_f
    MARKUS @sad "We watched you die, Kiara."
    MARKUS @angry "You can't just expect us to follow you through the desert mindlessly without asking at least a few questions!"
    "Kiara paused for a moment."
    KIARA @talk "... Bloody hells, you really gonna make things that difficult for me?"
    KIARA @talk "Fine, I'll answer what I can, ask me whatever you wish."
    menu qst_JudgementDay_PostQuestTravelToHamun_KiaraTalk:
        "How exactly did you survive?":
            KIARA @talk "The mistress found me after the battle..."
            KIARA @talk "She healed-"
            "Kiara pauses for a moment, pondering her choice of words carefully."
            KIARA @blush "{i}She brought me back.{/i}"
            jump qst_JudgementDay_PostQuestTravelToHamun_KiaraTalk
        "Where have you been this whole time?":
            KIARA @talk "Around..."
            KIARA @sad "I'm sorry I couldn't have came to see either of you sooner."
            KIARA @sad "My orders... I..."
            KIARA @sad "I had to obey them."
            jump qst_JudgementDay_PostQuestTravelToHamun_KiaraTalk
        "Who is this mistress you speak of?": 
            KIARA @happy "Mistress Sypha... I believe you two have already met her."
            MARKUS @shock "What?!"
            MARKUS @angry "That Demorai is your master?!"
            MARKUS @angry "Are you mad?"
            KIARA @sad "Please... Things are more complicated than any of us could have imagined back then."
            MARKUS @angry "I just watched those fuckers slaughter half of Novaras!"
            MARKUS @angry "It seems pretty damn simple to me! They're the ENEMY!"
            pass
    menu qst_JudgementDay_PostQuestTravelToHamun_KiaraTalk2:
        "Why did you - I mean, your mistress warn us about the attack?":
            KIARA @talk "It was in the interests of {i}the order of daggers{/i} to ensure the city held."
            MC @think "{i}The order of daggers?{/i}"
            KIARA @sad "I'm sorry... I've probably already said too much."
            jump qst_JudgementDay_PostQuestTravelToHamun_KiaraTalk2
        "Why Hamun?": 
            pass
    show kiara at nod
    "From her sleeve, Kiara produced a sealed, insignia envelope that she handed to us."
    KIARA @talk "Because my mistress and {i}your{/i} Emperor command it so."
    MC @surprised "What?"
    play sound "audio/cfx/letter.ogg"
    show mc at nod
    "Tearing open the letter to read it's contents, Markus crowded slightly beside me to read over my shoulder."
    "{i}If you, and Markus, are reading this, it means the agent has delivered the contents of this message to you in one piece, and you are both still alive.{/i}"
    "{i}While I cannot risk explaining the full details regarding the secrecy of your mission, should this letter fall into unwelcome hands,{/i}"
    "{i}As your Emperor, I must order you to complete two tasks.{/i}"
    "{i}The first, is to follow the agents instructions, and treat their word as if it was my own.{/i}"
    "{i}The second task, is to destroy this letter after reading it.{/i}"
    "{i}Should you succeed in your tasks, perhaps this realm will welcome you back into it's fold once more.{/i}"
    "{i}-Alcott.{/i}"
    "Attached at the bottom was the personal seal of the Emperor himself."
    MARKUS @shock "What in the gods is going on?"
    MARKUS @think "The Emperor... {i}Wants us to work with some Demorai?{/i}"
    MC @think "What are we to do in Hamun then?"
    KIARA @sad "I don't fully know, my mistress Sypha told me she would reveal everything when she joins us."
    MC @surprised "Sypha is coming to Hamun?"
    MC @surprised "But... She's a demorai! If she's seen, she'll be-"
    KIARA @talk "[player_name!t]..."
    KIARA @talk "There's a lot you don't know, handsome."
    KIARA @talk "I'll explain more on the way, but we have to go, and go now."
    show mc at shake
    MC @angry "Kiara! You've hardly told us anything still!"
    MC @angry "What is going on? Why is the Emperor working with a demorai?"
    KIARA @sad "... I know this is probably a lot to throw on you right now."
    KIARA @talk "But I promise, it's still me, I'm still Kiara."
    KIARA @talk "I wouldn't put either of you in harm's way."
    MC @sad "Kiara..."
    MC @sad "How can you expect us to just blindly trust you?"
    MC @sad "You serve the Demorai..."
    MC @angry "We just watched thousands die by their hands!"
    KIARA @talk "No... I serve my mistress."
    MC @think "How are they not one in the same?"
    KIARA @sad "You don't understand... This war..."
    KIARA @sad "{i}To the Demorai, it's a {b}holy war.{/b}{/i}"
    MARKUS @think "What are you talking about?"
    KIARA @sad "I... I've said enough!"
    KIARA @think "My mistress will explain more when she joins us in Hamun."
    KIARA @talk "Now please, it's a long journey to Hamun... Will you join me?"
    "Me and Markus looked to each other."
    MC @serious "You heard the Emperor, there might even be a chance we can return to Novaras."
    MARKUS @angry "... Well, we're just going to fucking die out here if we don't pick somewhere to go, aren't we?"
    MARKUS @sad "Might as well hope for the best, I suppose."
    MARKUS @smile "Besides... Worst case scenario,"
    MARKUS @smile "We catch a boat out to literally anywhere else!"
    MC "(Gods... I hope this is a good idea.)"

    if not QstFromAnotherWorld().LetVesDie:
        show kiara at right_f with ease
        show ves at center_f with dissolve
        VES @talk "So, I managed to find some desert rats that will go nice-"
        show ves at blurin, center
        show ves at cright with ease
        "Ves' eyes widened as she moved closer towards Kiara."
        VES @angry "Who are you?"
        KIARA @shy "A-Ah...!"
        KIARA @think "My mistress mentioned something about an orc, but..."
        KIARA @think "I've never actually seen one before!"
        VES @angry "And I'll be the last one you see if someone doesn't explain to me what's going on!"
        MC @surprised "She's a friend of ours!"
        MC @think "She..."
        MC @talk "It's a long story, we're heading to the free city."
        VES @think "{i}Hamun?{/i}"
        "Ves pondered the thought for a moment."
        VES @talk "I would like to come with you."
        MARKUS @angry "What?!"
        MARKUS @angry "No!"
        MARKUS @angry "She's an orc!"
        VES @angry "The free city is free for all! Including orcs!"
        MC @think "Why do you wish to go to the free city?"
        VES @talk "{i}... I have my own business to attend to there.{/i}"
        "Markus grumbled something under his breath and looked away."
        MC @smile "... Well, I won't say no to an extra pair of hands."
        "Ves smiled, looking up towards Kiara."
        VES @smile "You got a problem with that?"
        KIARA @happy "None at all, but-"
        KIARA @talk "You should probably know, I'm not exactly-"
        show ves at blurin, cright_f
        VES @talk "Don't care."
        hide ves with dissolve
        "Without another word, Ves turned to begin gathering up what essential supplies she'd need for the journey."
        show kiara at cright_f with ease

        KIARA @talk "... Is she always such a charmer?"
        MC @talk "She's... {i}very direct.{/i}"
        MC @smile "A bit like someone else I happen to know."
        KIARA @happy "Come, pack what you need, and let's head off!"
        $ CharHeal("ves")
        $ PartyAddChar("ves")
        
        $ PlayerAddItem("orc_tribal_wear", Silent = True)
        $ PlayerAddItem("orc_tribal_axe", Silent = True)
        $ PlayerAddItem("ves_family_axe", Silent = True)
        $ PlayerAddItem("orc_tribal_necklace", Silent = True)
        $ PlayerPartyCharEquipItem("ves", "orc_tribal_wear")
        $ PlayerPartyCharEquipItem("ves", "orc_tribal_axe")
        $ PlayerPartyCharEquipItem("ves", "ves_family_axe")
        $ PlayerPartyCharEquipItem("ves", "orc_tribal_necklace")
        
    $ CharHeal("kiara")
    $ PartyAddChar("kiara")

    $ PlayerAddItem("corrupted_blade", Silent = True)
    $ PlayerAddItem("duskshroud_raiment", Silent = True)
    $ PlayerAddItem("shadow_ring", Silent = True)
    $ PlayerPartyCharEquipItem("kiara", "corrupted_blade")
    $ PlayerPartyCharEquipItem("kiara", "duskshroud_raiment")
    $ PlayerPartyCharEquipItem("kiara", "shadow_ring")

    scene black with dissolve
    $ LocSet("hamun_gates")
    $ WorldMapLocAdd("hamun_gates")
    $ WorldMapLocAdd("lake_peacing")
    jump qst_JudgementDay_PostQuestArrivedToHamun

########################################################################################################################################
label qst_JudgementDay_PostQuestArrivedToHamun:
    $ Pause(0.5)
    $ PlaySoundRandom("clockWind")
    $ Pause(1.0)
    $ AddGameDays(5)
    $ TimeAdvTo(TIME_DUSK)
    if InfectionModule().CurrentValue < 65:
        $ InfChangeBy(65, SetTo = True)
    "{i}After days of travel...{/i}"
    $ Pause(1.0)
    $ LocFlush(dissolve)
    $ Pause()
    "The great free city of Hamun laid stretched before us, a shining coastal oasis beside the roaring desert dunes."
    "Now under the control of the powerful merchant lords, the city had flourished into one of great splendour... And danger."
    "For beneath it's shiny exterior, there were no {i}laws{/i} as such anymore in Hamun,"
    "Only the many armed guards the various merchant factions paid to maintain their control gave some semblance of peace."
    show markus at left
    show mc at cleft 
    with easeinleft
    "But beyond the ever looming threat not to to cause unncessary trouble, the city was truly free."
    show cg_guard_hamun at cright_f with easeinright
    show cg_guard_hamun at shake
    GUARD "HALT!"
    GUARD "What's your business in the free city?"
    MC @serious "Does it matter?"
    "The guard looked us up and down before laughing."
    GUARD "Only if you cause trouble."
    GUARD "You start something, don't be surprised if you find yourself losing your head."

    menu qst_JudgementDay_PostQuestArrivedToHamun_GuardMenu:
        "Is there really no laws in the free city?":
            GUARD "Neigh."
            GUARD "But no laws doesn't mean no ones in charge."
            GUARD "Pretty much every business in the city has some kind of security... Fuck around, and you'll find yourself skewed on the pointy end of one of them."
            jump qst_JudgementDay_PostQuestArrivedToHamun_GuardMenu
        "Who are the merchant lords who run this place?":
            GUARD "{i}Lord{/i} Iryiad runs the most powerful clique, the Zizi, they run the security detail around the city and control the docks."
            GUARD "But there's also the Quaygon, the Vulmar and an endless sea of smaller gangs who manage the whores, the raza, and the {i}'protection'{/i} of the local businesses."
            MC @think "You seem very forthcoming with all this."
            GUARD "Some people come here and think because we've no laws they can just do {i}whatever{/i} they like."
            GUARD "It's best to let them know that would be a poor choice."
            jump qst_JudgementDay_PostQuestArrivedToHamun_GuardMenu
        "Got any advice for me around the city?":
            GUARD "Do I look like a tour guide?"
            GUARD "Fuck off, buy yourself a couple sellswords and have them show you around!"
            pass

        "Thanks for the advice...":
            GUARD "Go on then, in ya get."
            pass

    scene black with dissolve
    $ LocSet("hamun_dist_docks")
    $ LocFlush(dissolve)
    show mc at center with easeinleft
    show kiara at cleft with easeinleft
    KIARA @happy "Ahh... Finally! We've made it."
    MC @talk "What now?"
    KIARA @talk "{i}The Pale Dragon.{/i}"
    KIARA @talk "It's an inn nearby, we have a room already prepared for us."
    hide kiara with easeoutright
    show markus at cleft with easeinleft
    MARKUS @shock "Gods... Look at this place!"
    MARKUS @shock "I had heard rumors about how much the city had changed since it broke away, but-"
    MARKUS @joy "It's certainly an impressive sight."
    hide markus with easeoutright

    if CharInParty("ves"):
        show mc at cright with easeinleft
        show ves at cleft with easeinleft
        VES @talk "..."
        show mc at blurin, cright_f
        MC @talk "Ves? Are you alright?"
        VES @talk "Yes... Just-"
        VES @blush "It's been a long time since I've been around so many people."
        MC @talk "So, what's your plan now you're here?"
        show ves at blurin, cleft_f
        $ Pause(2.25)
        show ves at blurin, cleft
        VES @talk "I'm looking for someone."
        VES @blush "... But, perhaps if you don't mind, I could stay with you and the others for a while."
        MC @think "Who are you looking for?"
        "Ves opened her mouth to say something, but she paused and smiled awkwardly, changing the subject quickly."
        VES @smile "I'll... tell you about it another time."
        VES @talk "Come, I'm tired... Let's find this {i}Pale Dragon.{/i}"
        hide ves with easeoutright
        show mc at blurin, cright
        $ Pause(0.75)
        

    hide mc with easeoutright
##############################################################################################################################################
    scene black with dissolve
    $ LocSet("hamun_hookah_bar")
    $ LocFlush()
    show rania at cright_f
    with dissolve
    
    "Smoke rose from every corner of the inn, a mixture of strange, hot aromas like that of sweet, crushed flowers all mixed in."
    "With every breath, you could feel a small surge of energy as the whole place seemed embraced by a hazy fog."
    "Sat hudled around tables, men, women, {i}other things,{/i} sat smoking from their pipes as the raza choked the air."
    "In and around the place were guards, always watching, already ready for trouble, as the loosely dressed women served drinks."
    
    show mc at cleft with easeinleft
    show kiara at left with easeinleft
    RANIA @talk "Welcome... Welcome to {i}The Pale dragon,{/i} I am your host, Rania."
    $ CharMeet("rania")
    RANIA @talk "What pleasures do you and your companions seek?"
    RANIA @smile "Perhaps some Raza or... {i}companionship?{/i}"
    "The woman looked towards me and Markus, pulling down her dress slightly to expose a breast as she winked."
    MC @lewd "Well-"
    KIARA @angry "We should be meeting a friend here in one of the rooms upstairs."
    KIARA @talk "{i}The one with a view so you might see the dragon to the east.{/i}"
    "Rania's eyes widened as she smiled."
    RANIA @smile "Ahh... Yes."
    RANIA @smile "Everything is already ready for you, first room on the left upstairs."
    "Rania's eyes glanced over towards those with me."
    RANIA @talk "For your companions, we have some rooms further down the hall."
    RANIA @smile "We hope you enjoy your stay with us."
    hide kiara with easeoutright
    hide mc with easeoutright
    scene black with dissolve

##############################################################################################################################################
    $ LocSet("hamun_hookah_bar_room")
    $ LocFlush(dissolve)
    show mc at cright_f with easeinright
    show kiara at cleft with easeinleft
    MC @talk "... Now what?"
    KIARA @talk "Rest. Stay here the night where it's safe, in the morning then, my mistress should join us."
    MC @think "You still haven't explained everything like you said you would."
    KIARA @talk "In time, for now, just rest."
    KIARA @talk "It's been quite the journey just to get here."
    MC @serious "... Fine."
    KIARA @talk "Just call if you need me."
    show kiara at blurin, cleft_f
    $ Pause(0.3)
    hide kiara with easeoutleft
    $ PlaySoundRandom("woodenDoor")
    $ Pause(0.5)
    show mc at center with easeinleft
    MC "(...Just what am I walking into now?)"
    MC "(I should get some rest.)"
    $ CharSetClothes("mc", "pants")
    $ PlaySoundRandom("tentFlap")
    show mc at nod
    $ Pause(0.5)
    scene black with dissolve
    $ CharSetClothes("mc", "normal")
    $ Pause(0.5)
    jump qst_JudgementDay_PostQuestArrivedToHamun_Dream

label qst_JudgementDay_PostQuestArrivedToHamun_Dream:
    $ AutoTimeFreeze(True)
    $ TimeAdvBy(TIME_2H)
    $ Pause(0.5)
    $ AutoAmb(False)
    $ AutoMus(False)
    stop ambience fadeout 2.0
    $ PlayMusic("audio/music/22_Space_Odyssey.ogg")
    scene cg_phoah_space
    show phoah:
        zoom 0.35
        anchor (0.5, 1.0)
        pos (0.33, 0.61)
    show hirrah:
        zoom 0.35
        xzoom -1.0
        anchor (0.5, 1.0)
        pos (0.4, 0.61)
    with dissolve
    $ Pause()
    "... Swirling around me, an endless black sea cut through by a rift of stars and strange colors."
    "Three bright suns surrounded a great dark circle, radiating a strange power."    
    "Stood on some strange rock platform, the two figures, unlike anything I'd ever seen before, turned their gaze towards me."
    MC "Where... Where am I?"
    "I looked down, gazing for where my hands, my body, {i}something{/i} should be."
    "But there was nothing... It was as though I was just two floating, unblinking eyes, unable to move."
    hide phoah
    hide hirrah
    with Dissolve(0.1)
    show phoah at cleft
    show hirrah at cright_f
    with Dissolve(0.1)
    "I spoke... And yet my mouth did not move."
    HIRRAH "Greetings... [player_name!t]."
    HIRRAH "Or is it, {i}Shyahtan?{/i}"
    "The strange being seemed to chuckle, her soft voice so strangely hypnotic and soothing."
    HIRRAH "Always so hard to keep up these days."
    PHOAH @angry "We're wasting time, Hirrah."
    HIRRAH "The last thing we need is to frighten him."
    MC "Who... Who are you both?"
    MC "What am I doing here?!"
    PHOAH @angry "See? Now the human is panicking anyway!"
    HIRRAH "Human might be quite the stretch given the circumstances."
    MC "W-Where am I?"
    MC "What is this place??"
    MC "WHO ARE YOU?"
    PHOAH @talk "{i}*Sigh*{/i}"
    PHOAH @angry "I am Phoah, goddess of justice."
    PHOAH @talk "This is Hirrah, goddess of fertility."
    "I stared at the strange beings before me in disbelief."
    "Were they..."
    "No, gods and goddesses... Such a ridiculous thing!"
    "This was nothing but some fever dream! A trick of the mind! A-"
    PHOAH @talk "We're real."
    MC "You... You can hear my thoughts?"
    HIRRAH "This place is not real, rather, a neural link projection we've created to speak to you."
    MC "...{i}A what?{/i}"
    HIRRAH "... I-"
    HIRRAH "It matters not."
    PHOAH @angry "Look, human, we need your help."
    MC "{i}Me?{/i}"
    PHOAH @talk "Listen carefully, human."
    PHOAH @talk "This world... It has become the focus of the great deciever's dark plan."
    MC "{i}... The great deciever?{/i}"
    "The goddess' hands tightened into tight fists."
    PHOAH @angry "The lord of lies..."
    PHOAH @angry "{b}Malakai.{/b}"
    PHOAH @angry "The one who bought ruin upon both the old gods and the new with his treacherous war."
    PHOAH @angry "No doubt he yearns to take a physical form once more."
    MC "I... I don't understand."
    MC "Malakai? {i}The{/i} Malakai?"
    "The dark god himself... Every child in Alderay knew the story of Malakai."
    "Legend speak of how his betrayal destroyed the old and new gods in the greatest war to ever be fought."
    MC "This is... This cannot be..."
    MC "He... {i}He's real?{/i}"
    HIRRAH "His flesh may be gone, but his spirit survives... Trapped beyond the gate of midnight."
    HIRRAH "{i}Imprisoned with Arda.{/i}"
    PHOAH @talk "Zanarak, his chosen champion has arrived to serve some purpose we do not fully understand."
    PHOAH @talk "And if that wasn't enough proof, {i}she{/i} is here."
    PHOAH @talk "Malakai's right hand, the chaos goddess, Gimera has taken form once more and walks this place."
    HIRRAH "Human... You must help us."
    HIRRAH "Serve as our champion."
    HIRRAH "While we find and stop Gimera, we must work together!"
    HIRRAH "No matter the cost..."
    HIRRAH "{i}Malakai can never be allowed to walk the physical planes once more.{/i}"
    menu qst_JudgementDay_PostQuestArrivedToHamun_Dream_Menu:
        "Who... {i}What{/i} is Malakai?":
            PHOAH @talk "Malakai destroyed everything we had built."
            PHOAH @talk "All our hopes and dreams, everything Arda spent countless millenia working to achieve."
            PHOAH @talk "{i}The gateways to unite the realms, the unity of the old gods and new...{/i}"
            PHOAH @talk "All of it was undone by Malakai in his quest to re-forge reality in his image."
            "Phoah paused for a moment, the rage slightly softening as she seemed to be thinking back to those dark days."
            PHOAH @sad "{i}... It wasn't always so though.{/i}"
            PHOAH @sad "Before that monster, Gimera decieved him into opening the {i}Macarum,{/i} Malakai went by a different name."
            PHOAH @sad "Malayan the curious."
            MC "The Macarum?"
            PHOAH @talk "{i}When Arda was born, he was a made a being of pure good, pure love.{/i}"
            PHOAH @talk "... But in order to become that, he cast off his darkness... sealed it away into a forbidden box beyond the knowledge and reach of even the gods."
            PHOAH @angry "Guided by terrible visions of an impending war between the old gods and the new, Gimera decieved Malayan that only the power of the box could prevent the war."
            PHOAH @sad "Little did Malayan know by opening it, the visions he fought to stop would come true."
            jump qst_JudgementDay_PostQuestArrivedToHamun_Dream_Menu

        "Where are the gods? Why do they not answer our prayers to help with this damned war?":
            "Hirrah let out a sharp chuckle."
            HIRRAH "And who is supposed to answer?"
            PHOAH @angry "Hirrah!"
            HIRRAH "Do not coddle the human... Letting him put his faith in what can never answer will lead him down a path of destruction."
            MC "{i}The... The gods no longer heard us?{/i}"
            PHOAH @talk "After the war, so few of us remain, even now."
            PHOAH @sad "So many died... Yhoshan... Taruna... Palam."
            HIRRAH "Once, during Arda's reign, thousands of us roamed the stars."
            HIRRAH "Now, perhaps only a few hundred remain... {i}if that.{/i}"
            MC "... So, we truly stand alone then?"
            PHOAH @talk "{i}The gods won't answer your prayers, because the gods can't even save themselves right now.{/i}"
            jump qst_JudgementDay_PostQuestArrivedToHamun_Dream_Menu

        "Tzenvachian... Or whatever you call him, what happened to him?":
            PHOAH @talk "Surely you know the stories?"
            PHOAH @talk "Has it truly been that long that truth has become some kind of warped myth?"
            MC "I know he waged war against Tzenvachian and the new gods."
            "The two goddess' shared a strange look with each other."
            PHOAH @talk "Tzenvachian...?"
            PHOAH @talk "Hmm... Arda took many names, I wonder where that one came from?"
            MC "His name was {i}Arda?{/i}"
            PHOAH @talk "That is how {i}we{/i} knew him long ago..."
            PHOAH @sad "So very... very, long ago."
            "The goddess seemed to drift off into thought before her focus returned to the present."
            PHOAH @talk "He is trapped with Malakai beyond the gate of midnight."
            PHOAH @sad "His... sacrifice saved us all."
            jump qst_JudgementDay_PostQuestArrivedToHamun_Dream_Menu

        "Do all of the gods look so... {i}different?{/i}":
            "The two goddesses looked at each other."
            HIRRAH "Ah... It's probably been so long since of your kind has seen us, it is little surprise you don't know."
            HIRRAH "I am one of the {i}old gods,{/i} crafted in Al'Vazah's original vision."
            PHOAH @talk "And I was born with the new gods, under Arda's light."
            MC "I thought the old gods and the new hated each other?"
            HIRRAH "{i}Not all of us.{/i}"
            HIRRAH "This one's company help's starve off at least a couple centuries of boredom."
            "The goddess Phoah shot her an irritable glance."
            PHOAH @angry "I do wonder {i}why{/i} I keep you around sometimes."
            HIRRAH "Because you'd continue to spiral and despair with the rest of the gods if I didn't drag you to your feet."
            "The goddess let out a heavy sigh."
            PHOAH @talk "There are so few of us left, the old wars hardly seem to matter anymore."
            PHOAH @talk "Just surviving... Just... Hoping Al'Vazah brings us a new light."
            HIRRAH "{i}That's her way of saying she means we're friends.{/i}"
            jump qst_JudgementDay_PostQuestArrivedToHamun_Dream_Menu
        "What do you want from me?":
            pass

    PHOAH @talk "With the being now awakened and attached to you, it cannot be a coincidence that Gimera has decided to suddenly return now."
    MC "{i}Why?{/i} What is so special about the creature...Shyahtan, or whatever it's name is?"
    HIRRAH "We do not know."
    MC "What?! Then how can-"
    PHOAH @talk "The being that is attached itself to you has some kind of great significance to Malakai."
    PHOAH @talk "I have no doubt Zanarak... Gimera herself perhaps."
    PHOAH @angry "{i}Something is coming for you.{/i}"
    MC "I don't understand... Malakai... He was defeated! He's gone!"
    HIRRAH "He was only imprisoned."
    HIRRAH "His spirit if allowed a vessel, may yet break free of his chains."
    MC "But he... How can he harm us?"
    HIRRAH "His shadow stretches far, even beyond his confinment."
    PHOAH @talk "When the time comes, human, stand with us."
    PHOAH @talk "{i}Or the darkness will consume us all...{/i}"
    HIRRAH "Phoah... Do you feel that?"
    PHOAH @shock "What? That can't be-"
    HIRRAH "Sever the connection! He's here! He's-"
    jump qst_JudgementDay_PostQuestArrivedToHamun_WakeUp

label qst_JudgementDay_PostQuestArrivedToHamun_WakeUp:
    $ AutoTimeFreeze(False)
    $ TimeAdvBy(TIME_2H * 2)
    $ CharSetClothes("mc", "pants")
    $ CharSetVar("kiara", "story_form", "demorai")
    $ AutoMus(True)
    $ AutoAmb(True)
    $ LocFlush()
    show mc at cleft
    show kiara at cright_f
    with flash

    "Springing from the bed, I found myself confronting some strange, naked, bat like creature who pulled back startled when they realized I was awake."
    KIARA @scared "{i}*Gasp!*{/i}"
    "As my hand quickly morphed into a set of claws and lunged forward, the creature pulled back and cried out in a familiar voice."
    show kiara at shake
    KIARA @scared "Wait! [player_name!t]! It's me!"
    KIARA @scared "It's Kiara!"
    "As the image before me came clearer, the pale, beautiful bat-like woman waited sheepishly, trembling slightly with fear."
    MC @surprised "... Kiara?"
    MC @surprised "Is that... Really you?"
    "She nodded."
    KIARA @sad "I... I'm sorry."
    KIARA @sad "I came to see you tonight, I wanted to talk and explain things in private."
    MC @angry "What in the hells is going on?!"
    MC @angry "Why do you look so-"
    KIARA @talk "My wounds {i}were{/i} fatal."
    KIARA @talk "The only way my mistress could save me was if I agreed to become a Demorai."
    KIARA @talk "I can appear as a human, but..."
    KIARA @sad "{i}This is the real me now.{/i}"
    MC @sad "... Kiara."
    KIARA @happy "It's alright, love."

    if CharGetVar("kiara", "romanced") == True:
        
        KIARA @happy "I think... I think I've figured it all out."
        MC @think "What are you talking about?"
        KIARA @blush "I think..."
        
        KIARA @blush "{i}I think the gods want us to be together.{/i}"
        MC @laugh "What? The gods?"
        KIARA @scared "Look at us!"
        KIARA @happy "We should both be dead but we're not!"
        KIARA @happy "Isn't it too much of a coincidence?"
        KIARA @happy "Us, here... {i}Right now.{/i}"
        show kiara at center_f with ease
        "Kiara stepped closer towards me."
        KIARA @blush "You and I love, we're star-crossed."
        MC @talk "Kiara, I-"
        KIARA @blush "Come on... Stop thinking so much."
        $ AutoMus(False)
        $ PlayMusicRandom("mus_sex")
        "With a sharp shove, Kiara pushed me back down onto the bed."
        MC "Kiara!"
        $ CharSetClothes("kiara", "naked")
        show kiara at nod
        "Straddling on-top of me, Kiara run her warm hands down my chest, her claws gently pressed enough to feel nice, but not cut."
        KIARA "Come on, lover."
        KIARA "I know you've missed this!"
        $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
        scene kiara_hamun_cowgirl_idle_slow with dissolve
        $ Pause()
        "Rocking back and forth, Kiara rubbed herself against my cock as she let out a trembling, hot moan"
        KIARA "Ahh..."
        KIARA "Fucking hells... Mmm..."
        KIARA "Gods, I thought I loved your cock before but-"
        "With my member coated in her wetness, her slow, deliberate thrusting of her hips caused the hot blood to rush quickly."
        "I reached up to fondle her breasts only for her to playfully smack my hands away."
        KIARA "Ah, ah, ah!"
        KIARA "Not yet, lover."
        KIARA "I wanna drive you fuckin' wild."
        $ PlaySexFx("audio/sex_sounds/forgean_100.ogg", 1)
        scene kiara_hamun_cowgirl_idle_fast with dissolve
        $ Pause()
        "Kiara's hot breath touched my chest as she moved faster, the sweet sweat on her skin glistening in the moonlight."
        MC "Kiara..."
        "I said breathlessly, the two of us already beginning to burn up as our hearts raced."
        KIARA "F-Fuck..."
        KIARA "You're so bloody hard."
        KIARA "Mm... Tell me, my love."
        KIARA "Tell me what you want."
        "One of Kiara's hands gently caressed my face as she leaned forward for a moment to kiss me for a brief, hot moment, slipping her tongue into my mouth."
        KIARA "Mhmm!"
        MC "Ahh...!"
        MC "You, Kiara... I want you."
        $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
        
        scene kiara_hamun_cowgirl_loop_slow with dissolve
        $ Pause()
        "With a smug, satisfied grin, she grabbed a hold of my cock and positioned it carefully, gently sliding down on it."
        "Her tight, wet hole squeezed around me as I filled her up."
        "She closed her eyes, moaning softly once more as her nails dug deeper into my chest."
        KIARA "So big..."
        "She muttered softly, slowly beginning to bounce on my cock."
        "The sounds of flesh colliding filled the room as the softness of her ass pressed down onto me."
        KIARA "Mhmmm!"
        KIARA "*Huff* Fuck me... Fuck me like one of your southern girls! *Huff*"
        "My hands squeezed at her soft ass as she continued to push herself down onto me, at one point grabbing a hold of my hands and pulling them towards her chest."
        $ PlaySexFx("audio/sex_sounds/forgean_150.ogg", 1)
        scene kiara_hamun_cowgirl_loop_fast with dissolve
        $ Pause()
        "Squeezing and fondling her soft breasts, she let out a trembling moan as she began to quickly move faster."
        MC "K-Kiara!"
        "The bed squeaked louder as the board frame knocked continuously against the wall."
        MC "We're gonna wake the whole inn!"
        KIARA "Fuck em!"
        KIARA "Let them know I'm - *huff* having a good time!"
        "Her soft tits felt wonderful to squeeze and play with as her bounced with every movement."
        KIARA "P-Pull them!"
        KIARA "F-Fucking pull my nipples and squeeze my t-tits while I fuck you!"
        "As I tugged and pulled at the nipples, Kiara's expression changed as her eyes widened."
        "Her mouth hung open as her tongue rolled out, moaning hotly as she trembled."
        KIARA "C-Cummhh inhh mheee!"
        KIARA "Pweaseee!"
        "It was all too much, as Kiara dug her nails deeper, drawing blood as her tight cunt now slammed down onto me, the sudden pain interwoven with pleasure was too much to bare."
        MC "K-Kiara!"
        KIARA "F-Fillhh mheee!"
        "Springing forward, I grabbed a hold of Kiara's ass and squeezed as I flooded her womb with my heavy load."
        
        $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
        $ ReduceInfectionFromSex("kiara")
        $ UnlockGalSceneAndGrantXp("kiara", "hamun_cowgirl")
        $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
        scene kiara_hamun_cowgirl_finish with flash
        $ Pause()

        "Kiara shuddered, stopping in hey tracks as her felt the rush of warmth fill her up."
        "Her legs and arms squeezed and tightened around me, as though her whole body went into spasm for a moment."
        "After a few trembling moments, still breathing heavily, she began to relax."
        KIARA "Fucking hells..."
        $ AutoMus(True)
        scene black with dissolve
        "Kiara playfully giggled as she pushed me back down onto the bed, resting her head onto my chest."
        $ LocFlush()
        show kiara at cright_f
        show mc at cleft
        with dissolve
        KIARA "Well, that was a good fuck."
        MC "Well, worth dying for?"
        "Kiara playfully hit at my chest."
        MC "Too soon."
        KIARA "Cheeky fuck."
        "In her faint protest, I silenced her with a soft kiss."
        KIARA "... I'm staying here tonight."
        MC "Oh, are you?"
        KIARA "Last thing I need is people seeing my tits and ass trying to sneak back to my room."
        MC "Is that the only reason?"
        KIARA "... Mmm, can we save the pillow talk for another time?"
        KIARA "I'm quite -" 
        "Kiara yawned as she closed her eyes."
        KIARA "Tired..."
        scene black with dissolve
        $ CharSetClothes("kiara", "normal")
        "As she drifted off into slumber, I gently stroked her soft hair for a while, before drifting off to sleep myself once more."
        "This time... Far more peacefully than before."
        pass

    else:
        KIARA @talk "I... I just wanted you to know you could still trust me."
        KIARA @sad "I'm still your friend, [player_name!t]."
        MC @sad "I..."
        "I looked Kiara up and down, aside from her now pale face, one could hardly tell it was her anymore."
        MC @think "This... Might take a little while to get used to."
        "Kiara chuckled."
        KIARA @happy "You're not exactly how I remember you either!"
        KIARA @blush "I've seen what those tentacles of yours can do!"
        MC @smile "Ha... I suppose that's true."
        KIARA @talk "I'm going to head back to my room."
        KIARA @talk "Goodnight, [player_name!t]."
        MC @talk "Goodnight, Kiara."
        show kiara at nod
        $ Pause(1.0)
        show kiara at blurin, right_f
        $ Pause(0.25)
        hide kiara with easeoutright
        MC "(Gods... My friends becoming Demorai...)"
        show mc at center with ease
        MC "(Nothing makes sense anymore.)"
        scene black with dissolve
        pass

    $ CharSetVar("kiara", "story_form", "human")
    $ CharSetClothes("mc", "normal")
    $ Pause(1.0)
    $ TimeAdvTo(TIME_MORNING)
    $ LocEnter()