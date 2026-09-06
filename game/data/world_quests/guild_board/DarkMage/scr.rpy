label qst_guild_darkmage:
    ##############################################################################################
    #D-Tier QUEST 3 - 'Rumours of a Dark Mage...'
    #Quest description:
    #Fade to black upon selecting the quest 
    scene black with dissolve
    "...Before taking the quest, the guild ensured we were looked over and were fully rested before allowing us to take the quest."
    $ TimeAdvTo(TIME_DAY_END)
    "Piecing together what we could from the reports on the dark Mage, we knew the dark mage was likely hiding somewhere within the southern housing district."
    $ LocSet("novaras_dist_house_south")
    $ LocFlush()
    with dissolve
    show mc at left with easeinleft
    "While I didn't possess any magic, there was a distinctly foul 'scent' that stood out amongst the rest, and the more I focused in on, the more I suspected it would lead us to the Mage."
    BLACK "{i}Death ... I smell Death.{/i}"
    MC "(Are you sure you aren't just going to lead us to a crypt?)"
    MC "(This city isn't exactly short on death)."
    BLACK "{i}Different ... Smell not right.{/i}"
    BLACK "{i}This way.{/i}"
    hide mc with easeoutright
    scene black with dissolve
    # music? experiments or sth
    # also deafen ambience about here
    "Following the dark passengers' guidance, we headed deeper into the city slums."
    "Eventually, we tracked our way towards one of the many ramshackle houses in the Novaras slums, blending in almost indistinguishable from the rest, and entered inside."
    $ LocSet("novaras_darkmage_room")
    $ Pause(0.25)
    $ LocFlush()
    with dissolve
    #DAMAGED ROOM
    #Player has to find the secret passageway - clicking the bookcase reveals a secret wall with strange markings and a face on it.
    MC '(... What is this place?)'
    BLACK "{i}Something is here ... Look around.{/i}"
    $ LocEnterQ()

label qst_guild_darkmage_shelf_click:
    # show wall behind shellf here
    show bg_darkmage_room_wall with dissolve
    play sound "audio/cfx/darkness_erupt.ogg"
    show darkmage_wall_face with dissolve
    MC '(...!)' 
    MC "What the-"
    $ AutoAmb(False)
    play ambience "audio/ambience_scenes/whispers.ogg"
    DARKMAGE_WALL_FACE @talk 'Three riddles are the key to passage beyond this veil.'
    $ QstSetProgress(QstGuildDarkMage, 1)
    DARKMAGE_WALL_FACE @talk 'For each wrong you give, in blood shall you pay.'
    while QstGuildDarkMage().correct_answers < 3:
        # recopy and reshuffle in case player somehow failed thru all 12
        if len(QstGuildDarkMage().active_riddles_list) == 0:
            $ QstGuildDarkMage().active_riddles_list = QstGuildDarkMage().riddles_label_list.copy()
            $ renpy.random.shuffle(QstGuildDarkMage().active_riddles_list)
        call expression QstGuildDarkMage().active_riddles_list[-1] from _call_expression
        $ QstGuildDarkMage().active_riddles_list.pop()
        if _return == False:
            call qst_guild_darkmage_riddle_wrong_answer from _call_qst_guild_darkmage_riddle_wrong_answer
        else:
            $ QstGuildDarkMage().correct_answers += 1
    jump qst_guild_darkmage_wall_enter

label qst_guild_darkmage_riddle_wrong_answer:
    play sound "audio/cfx/magic_earthy_cast1.ogg"
    $ Pause(0.5)
    $ LocFlush()
    show bg_darkmage_room_wall
    show darkmage_wall_face
    with flash
    $ DamagePlayer(25, Lethal = False)
    "A bolt of lightning from the faces' eyes painfully zapped at me before dispersing."
    MC '(Hrgh! Fuck)!'
    MC '(Better chose more carefully next time...)'
    return

label qst_guild_darkmage_wall_enter:
    $ AutoAmb(True)
    'The face on the wall began to dissipate, and with it, so did the wall behind it, revealing a passageway down into the depths below.'
    play sound "audio/cfx/earthy_rustle.ogg"
    hide darkmage_wall_face with dissolve
    show bg_darkmage_room_open with dissolve
    'Taking the first step onto the first cold stone step, a series of purple torches lit themselves, guiding our way down the spiral stairs.'
    scene black with dissolve
    'As we drew closer, strange chants and other sounds grew louder and louder till we found ourselves stood in the doorway of some kind of make-shift laboratory.'
    scene bg_darkmage_lab
    show cg_dark_mage at cright
    with dissolve
    'Littered about the place were various trinkets potions and scrolls as the tall, dark robed figure stood over a blood-dripping altar with a pale lifeless woman gutted and strapped to it.'
    show mc at left with easeinleft
    show cg_dark_mage at cright_f, blurin
    DARK_MAGE '{i}How did you get down here!?{/i}'
    DARK_MAGE 'Who are you?'
    menu qst_guild_darkmage_wall_enter_menu:
        "What horror is all this?":
            DARK_MAGE 'Why, my experiments of course!' 
            DARK_MAGE "A lung here ... A heart there, it's all come together so wonderfully!"
            DARK_MAGE "No one will miss these unfortunate souls anyway, in truth ... {i}I feel like I'm doing them a favor.{/i}"
            DARK_MAGE "Here, let me show you my latest... project."
            DARK_MAGE "{i}Camen! Come!{/i}"
        "Surrender now, and I pledge to take you in alive!":
            DARK_MAGE "{i} ... Surrender?{/i}"
            DARK_MAGE "Why, whatever for?"
            DARK_MAGE "With my creations, we may finally be able to start winning this war!"
            MC @angry "What in all of the names of the gods are you talking about?"
            DARK_MAGE "{i}Camen! Come!{/i}"
        "I'm going to enjoy tearing you limb from limb.":
            DARK_MAGE 'Ooooh! I see!'
            DARK_MAGE "You're here to steal my research!"
            DARK_MAGE "Well you can't have it! IT'S MINE!"
            DARK_MAGE "With it, I'll be able to finally win this war and they'll recognize my work for the heroism it deserves!"
            MC @angry "You're gutting women like fish ... What 'heroism' is there to recognize here you lunatic?"
            DARK_MAGE 'HO HO HO!'
            DARK_MAGE '{i}Camen! Come!{/i}'
    'Dragging itself forward from the darkness, a wretched mass of flesh unleashing an horrifying growl like that of a distorted human, as though the cords had been dragged and pulled.'
    'The sickening sight of what seemed to be at least a dozen people merged together into some warped abomination, limbs merged together with a horrifying skull like face protruding out the center of this human spider.'
    MC @scared "...What in all of the gods is that thing?"
    DARK_MAGE "Why, this is what we {i}need{/i} to win this war!"
    DARK_MAGE "If we but sacrificed a few hundred of our own, think of how many of these I could make!"
    MC @angry "You're insane!"
    DARK_MAGE "{i}... Insane?{/i}"
    show cg_dark_mage at shake
    DARK_MAGE "INSANE?!"
    DARK_MAGE "The only insanity is letting these fools continue this futile war!"
    DARK_MAGE "If someone must be the monster to save you all then I welcome the role with open arms!"
    "The horrifying creature crawled it's way towards the Dark Mage as he began to affectionately pet it."
    DARK_MAGE "See? It's perfectly obedient and-"
    play sound "audio/cfx/duprey_headbutt.ogg"
    hide cg_dark_mage
    show cg_dark_mage_noarm at cright
    with flash
    "The beast suddenly lunged, tearing off the Dark Mage's hand whole."
    show cg_dark_mage_noarm at shake
    DARK_MAGE "AHHHHHHHH!"
    hide cg_dark_mage_noarm with easeoutright
    'The Dark mage waved around the stump where his hand used to be, pumping out blood as the creature violently whacked him with one of its spider-like legs, sending him hurdling across the room.' 
    "Slamming against the wall, he weakly reached his other hand out towards the creature as a pool of blood began to envelop him."
    show mc at center with easeinleft
    DARK_MAGE "CAMEN! Nooo!"
    DARK_MAGE "O-OBEY ME! ARGHH! I AM YOUR MASTER!"
    MC @surprised "I don't think he's listening anymore!"
    play sound "audio/cfx/scorpion_roar.ogg"
    if GetPartySize() > 1:
        "The beast snarled towards us."
    else:
        "The beast snarled towards me."
    MC @angry " ...Shit!"
    $ QstSetProgress(QstGuildDarkMage, 2)

    if GetPartySize() > 1:
        'The human spider let out another dry, blood curling cry as it scurried towards us.'
    else:
        'The human spider let out another dry, blood curling cry as it scurried towards me.'

    scene black with dissolve

    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")

    if GetPartySize() > 1:
        'As the others leapt out in front to try and battle the creature, I transformed and prepared for battle once again!'
    else:
        "I transformed, preparing for battle!"

    play sound2 "audio/cfx/transform.ogg"

    $ TransformMC(True)
    $ TransformMarkus(True)

    $ StartBattle(BattleData(BackgroundImage = "pbat_dungeon_2", CharIDList_Right = ["e_spiderman"]))

    $ TransformMC(False)
    $ TransformMarkus(False)

    "With tentacles thrust through the creature's eyes, it howled in pain as I dug in through the eye-sockets, blood poured out as it flailed to still desperately claw at me before tearing it's head apart vertically."
    "The thing slumped down in front of me, pitiful sounds escaping its dying breathes as a pool of blood enveloped around the creature, and it finally stopped breathing."
    scene bg_darkmage_lab
    show mc_transformed at left
    show cg_dark_mage_noarm at right
    with dissolve
    $ AutoMus(True)
    DARK_MAGE "Noooo! NO! NO! What have you done?"
    DARK_MAGE "My {i}*Cough!*{/i} beautiful creature!"
    DARK_MAGE "You fool! Don't you - Ahh! See?"
    DARK_MAGE "Only with my - {i}*Cough!*{/i} work could we turn the tide of this war!"
    MC "Delude yourself you're a hero all you want, Mage."
    MC "Do you truly think anyone would accept these creatures into the army?"
    MC "You're just a madman playing god, looking for an excuse to justify this horror show you've created."
    DARK_MAGE "N-No ... They would! {i}They would!{/i}"
    DARK_MAGE "They'll - {i}*Cough!* *Cough!*{/i} take me seriously when they see what I can make!"
    'As he looked over at his dead creation, his voice sounded weaker and weaker as he tried to convince himself.'
    DARK_MAGE 'They ... They would ... They .... They ...'
    hide cg_dark_mage_noarm with dissolve
    'The Mage lifelessly slumped his head down onto the cold floor in a pool of his blood.'
    scene black with dissolve
    $ QstSetProgress(QstGuildDarkMage, 3)
    "Looking over at his research notes, I figured that if I can find a buyer, they could make a pretty coin."
    "...That is, assuming I could find someone who would {i}want{/i} this madman's research."
    $ PlayerAddItem("darkmage_design_notes")
    $ TimeAdvBy(TIME_2H)
    'Changing back into my human form, I returned with the head of the Dark Mage and plumped it down onto the table of the adventurer guild, letting the guards clean up the mess of the site.'
    $ QstComplete(QstGuildDarkMage)
    $ LocSet("novaras_adv_guild")
    $ Pause(0.25)
    $ LocEnter()

#########################################
################ riddles ################
label qst_guild_darkmage_riddle_0:
    DARKMAGE_WALL_FACE @talk '{i}The person who makes it has no need of it; the person who buys it has no use for it. The person who uses it can neither see nor feel it. What is it?{/i}'
    menu:
        'A coffin.':
            DARKMAGE_WALL_FACE @talk 'This is the correct answer.'
            return True
        'A sword.': 
            DARKMAGE_WALL_FACE @talk 'You have chosen unwisely.'
            return False
        'A chair.':
            DARKMAGE_WALL_FACE @talk 'You have chosen unwisely.'
            return False

label qst_guild_darkmage_riddle_1:
    DARKMAGE_WALL_FACE @talk "{i}I am a shield with no spear or sword. I sit on a bridge, where soldiers stand guard. What am I?{/i}"
    menu:
        'The sun.':
            DARKMAGE_WALL_FACE @talk 'How wrong you are...' 
            return False
        'The moon.': 
            DARKMAGE_WALL_FACE @talk 'How wrong you are...'
            return False
        'A rainbow.':
            DARKMAGE_WALL_FACE @talk 'A good choice you have made.'
            return True

label qst_guild_darkmage_riddle_2:
    DARKMAGE_WALL_FACE @talk "{i}I soar without wings; I see without eyes. I've traveled the universe to and fro. I've conquered the world, yet I've never been anywhere but home. Who am I?{/i}"
    menu:
        'Ambition.':
            DARKMAGE_WALL_FACE @talk 'You have chosen poorly.' 
            return False
        'Imagination.':
            DARKMAGE_WALL_FACE @talk 'This is the correct answer.'
            return True
        'Hope.':
            DARKMAGE_WALL_FACE @talk 'You have chosen poorly.' 
            return False

label qst_guild_darkmage_riddle_3:
    DARKMAGE_WALL_FACE @talk "{i}The more you take, the more you leave behind. What am I?{/i}"
    menu:
        'Greed.':
            DARKMAGE_WALL_FACE @talk 'Your answer is wrong.'
            return False
        'Time.':
            DARKMAGE_WALL_FACE @talk 'Your answer is wrong.' 
            return False
        'Footsteps.':
            DARKMAGE_WALL_FACE @talk 'This is the correct answer.'
            return True

label qst_guild_darkmage_riddle_4:
    DARKMAGE_WALL_FACE @talk "{i}I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?{/i}"
    menu:
        'Fire.':
            DARKMAGE_WALL_FACE @talk 'A wise choice.'
            return True
        'Tree.':
            DARKMAGE_WALL_FACE @talk 'How unfortunate...'
            return False
        'Wind.':
            DARKMAGE_WALL_FACE @talk 'How unfortunate...'
            return False

label qst_guild_darkmage_riddle_5:
    DARKMAGE_WALL_FACE @talk "{i}I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?{/i}"
    menu:
        'An echo.':
            DARKMAGE_WALL_FACE @talk 'You are correct.'
            return True
        'A whistle.':
            DARKMAGE_WALL_FACE @talk 'It is not so.' 
            return False
        'Music.':
            DARKMAGE_WALL_FACE @talk 'It is not so.' 
            return False

label qst_guild_darkmage_riddle_6:
    DARKMAGE_WALL_FACE @talk "{i}I am always hungry, I must always be fed. The finger I touch, will soon turn red. What am I?{/i}"
    menu:
        'Fire.':
            DARKMAGE_WALL_FACE @talk 'Indeed I am!'
            return True
        'Time.':
            DARKMAGE_WALL_FACE @talk 'No ... You are wrong.' 
            return False
        'Ambition.':
            DARKMAGE_WALL_FACE @talk 'No ... You are wrong.' 
            return False

label qst_guild_darkmage_riddle_7:
    DARKMAGE_WALL_FACE @talk "{i}I am not alive, but I grow; I don't have a mouth, but I need water to survive. What am I?{/i}"
    menu:
        'A shadow.':
            DARKMAGE_WALL_FACE @talk 'You have chosen wrongly. Pity.' 
            return False
        'A plant.':
            DARKMAGE_WALL_FACE @talk 'Yes! It is so!'
            return True
        'A mirror.':
            DARKMAGE_WALL_FACE @talk 'You have chosen wrongly. Pity.' 
            return False

label qst_guild_darkmage_riddle_8:
    DARKMAGE_WALL_FACE @talk "{i}I am seen in the water, if seen in the sky, I am in the rainbow, a jolly sight to see. What am I?{/i}"
    menu:
        'Dragon.':
            DARKMAGE_WALL_FACE @talk 'You are mistaken.' 
            return False
        'Mermaid.':
            DARKMAGE_WALL_FACE @talk 'Your words ring true.'
            return True
        'Sun.': 
            DARKMAGE_WALL_FACE @talk 'You are mistaken.' 
            return False

label qst_guild_darkmage_riddle_9:
    DARKMAGE_WALL_FACE @talk "{i}I am always hungry, I must always be fed. The finger I touch, will soon turn red. What am I?{/i}"
    menu:
        'Fire.':
            DARKMAGE_WALL_FACE @talk 'Yes! Wonderful!'
            return True
        'Dragon.':
            DARKMAGE_WALL_FACE @talk 'No ... This is not correct.' 
            return False
        'Goblin.':
            DARKMAGE_WALL_FACE @talk 'No ... This is not correct.' 
            return False

label qst_guild_darkmage_riddle_10:
    DARKMAGE_WALL_FACE @talk "{i}What is so fragile that saying its name breaks it?{/i}"
    menu:
        'Silence.':
            DARKMAGE_WALL_FACE @talk 'That it is!'
            return True
        'Crystal.': 
            DARKMAGE_WALL_FACE @talk 'No ... That is not it.' 
            return False
        'Ice.':
            DARKMAGE_WALL_FACE @talk 'No ... That is not it.' 
            return False

label qst_guild_darkmage_riddle_11:
    DARKMAGE_WALL_FACE @talk "{i}I am not alive, but I grow; I don't have a mouth, but I need wind to survive. What am I?{/i}"
    menu:
        'Castle.':
            DARKMAGE_WALL_FACE @talk '{i}*Sigh*{/i}' 
            return False
        'Flag.':
            DARKMAGE_WALL_FACE @talk 'Indeed it is!'
            return True
        'Wizard.':
            DARKMAGE_WALL_FACE @talk '{i}*Sigh*{/i}' 
            return False
