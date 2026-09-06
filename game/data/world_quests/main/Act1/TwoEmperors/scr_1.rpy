label qst_TwoEmperors_meetMarkus_revisitable:
    if QstTwoEmperors().firstMarkusDialogue:
        $ QstTwoEmperors().firstMarkusDialogue = False
        show markus at right_f
        with dissolve
        show mc at left with easeinleft
        MARKUS 'There you are!'
        MARKUS @angry "I take it you got the wakeup call from Captain prick too?"
        MC @talk 'Yeah...'
        MARKUS @angry "This whole thing is bullshit, you know that? BULLSHIT!"
        MC @talk "Well its still shit shovelled our way, so let's just focus on getting this thing done as quickly as we can."
        MARKUS @sad '{i}*Sigh*{/i} ...Damn it.'
        MARKUS @sad "This isn't what I wanted for us."
        MC @talk "...Come on, they've marked where some Demorai were last seen in the Valley of Death."
        MC @talk "Maybe we can find some clues or something out there."
        MARKUS "We should probably change form too when we get out there... Just in case."
        MC @talk "Good idea." 
        MARKUS "So, should we head out?"
        MARKUS "Something tells me that if we head out now, {i}we might not be able to head back and re-supply for a while.{/i}"
    else:
        show markus at center
        with dissolve
        MARKUS "Hey, ready to move out yet?"
    menu:
        "Let's go":
            MARKUS "Alright then, let's move out."
            $ QstSetProgress(QstTwoEmperors, 1)
            jump qst_TwoEmperors_1
        "Not yet":
            MARKUS "Okay, do whatever you have to."
            $ LocEnter()

label qst_TwoEmperors_1:
    scene black with dissolve
    $ LocSet("valley_of_death")
    "We made our way to the Valley of Death, keeping an eye out for anything out of order."
    $ TimeAdvBy(TIME_1H)
    $ LocFlush()
    with dissolve
    show markus_transformed with easeinleft:
        xcenter 0.7
    show mc_transformed with easeinleft:
        xcenter 0.2
    MC 'Do you see anything?'
    MARKUS '{i}...Sand.{/i}'
    MARKUS '...And rocks.'
    MC 'Fucking helpful.'
    MARKUS "It's a desert! What were you hoping for?"
    MARKUS "I'd see a sign saying {i}'All Demorai go this way?'{/i}"
    MC "Let's just look around... There has to be something..."
    hide markus_transformed with easeoutright
    MC '(Hmm?)'
    'Looking down onto the ground, I looked carefully to see the faint track marks of what looked like inhuman feet heading out into the desert.'
    MC 'Markus, look...'
    show markus_transformed with easeinright:
        xcenter 0.7
        xzoom -1.0
    MARKUS 'Tracks?'
    MC 'It looks like it.'
    MARKUS "They're so faint though... The desert winds will cover them up before we have any chance to get wherever they lead."
    BLACK '{i}We can help with that.{/i}'
    WHITE '{i}Do not look with eyes... Sense.{/i}'
    MARKUS 'What do they mean?'
    'As I looked down at the faint tracks before us, I focused in hard, and as I did so, I could smell the wretched outline of their scent, guiding me forward.'
    MC 'Urghh! They reek of death!'
    MARKUS 'I can smell it too now... Its weak though.'
    MARKUS "They must be pretty far away by now."
    MC "Then, let's not lose a moment."
    hide mc_transformed with easeoutright
    show markus_transformed at blurin:
        xzoom 1.0
    hide markus_transformed with easeoutright
    # they leave scene
    scene black with dissolve
    # time passes as these lines go
    'For seemingly miles, we followed the scent as we tracked the tracks deeper and deeper into the Valley of Death.'
    $ TimeAdvBy(TIME_1H)
    'The hot sun beat against our backs as I flung myself forward with my tentacles while Markus glided overhead.'
    $ TimeAdvBy(TIME_1H)
    'The scent grew stronger and stronger with each passing moment, till it became an overpowering stench of death that all Demorai seemed to cake themselves in.'
    $ TimeAdvBy(TIME_1H)
    'Finally, we arrived upon our destination.'
    $ LocSet("demorai_temple")
    $ LocFlush()
    show markus_transformed:
        xcenter 0.1
    show mc_transformed:
        xcenter 0.9
        xzoom -1.0
    with dissolve
    'Ancient ruins were concealed away amidst the desert dunes.'
    'We stared into the flooded blackness of the entrance, the ruins inviting us into their unknown depths.'
    MARKUS '[player_name!t]... What is this place?'
    MC 'I have no idea.'
    MC '...But I can smell them inside.'
    MARKUS 'Are we... {i}actually going to go in there?{/i}'
    "I couldn't help but hesitate for a moment, the daunting darkness of the entrance echoed hollowly."
    MC "I don't think we have much choice."
    $ QstSetProgress(QstTwoEmperors, 2)
    $ BlockWaitGlobal(True)
    MARKUS '{i}*Sigh*{/i} Fucking great.'
    $ LocEnter()

label qst_TwoEmperors_1_onRuinsEnter:
    $ QstTwoEmperors().onTempleEnterLines = False
    show markus_transformed with easeinright:
        xcenter 0.85
        xzoom -1.0
    show mc_transformed with easeinleft:
        xcenter 0.1
    MARKUS 'What is this place?'
    MC 'Some kind of... ancient temple I think?'
    MC 'Tread carefully...'
    $ LocEnter()

####### all three clickables below
label qst_TwoEmperors_temple_clickableRuins:
    if "clickedRuins" in QstTwoEmperors().templeReqEvents:
        $ QstTwoEmperors().templeReqEvents.remove("clickedRuins")
    show markus_transformed with easeinright:
        xcenter 0.85
        xzoom -1.0
    show mc_transformed with easeinleft:
        xcenter 0.1
    MARKUS 'Was this some kind of a temple?'
    MC 'Perhaps.'
    BLACK '{i}(Familiar...){/i}'
    MC 'What was that?'
    BLACK '{i}(This place... Like fragments of a dream.){/i}'
    MC 'What do you remember?'
    BLACK '{i}(...I cannot.){/i}'
    BLACK '{i}(Only glimpses of a time before.){/i}'
    MC 'Hmm... Maybe it will come back to you in time.'
    $ LocEnter()

label qst_TwoEmperors_temple_clickableStatue:
    if "clickedStatue" in QstTwoEmperors().templeReqEvents:
        $ QstTwoEmperors().templeReqEvents.remove("clickedStatue")
    show markus_transformed with easeinright:
        xcenter 0.85
        xzoom -1.0
    show mc_transformed with easeinleft:
        xcenter 0.1
    MARKUS "I've never seen that goddess before, who is she?"
    MC "Maybe she's not one of {i}our{/i} goddesses..."
    $ LocEnter()

label qst_TwoEmperors_temple_clickableWater: # causes the kraken thing to trigger in-quest
    show mc_transformed with easeinleft:
        xcenter 0.1
    'Peering into the depths of the stagnant water over the edges of the erected stone pathways gave me an uneasy feeling.'
    'I could not see what was down there, but I could sense movement beneath that blackened water all the same.'
    'Just how deep did these waters run?'
    if "messedWithWater" in QstTwoEmperors().templeReqEvents:
        $ QstTwoEmperors().templeReqEvents.remove("messedWithWater")
        'I leant down and gently submerged my hand in the cold waters watching the water ripple.'
        '{i}Something{/i} splashed up-ahead in the water once the wave of my ripple passed it.'
        'I quickly pulled my hand out.'
        MC '(Probably not a good idea to do that again...)'
        $ LocEnter()
    menu:
        "Touch the water":
            'Placing my hand into the water, the ripples once again waved across the still waters.'
            scene cg_demorai_temple_kraken with flash
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            'This time though, bursting out of the waters came a fury of tentacles thrashing wildly!'
            MC '(FUCK!)'

            $ TransformMC(True)
            $ TransformMarkus(True)

            $ StartBattle(BattleData(BackgroundImage = "pbat_demorai_temple", CharIDList_Right = ["e_kraken"], ContinueOnDefeat = True))

            $ TransformMC(False)
            $ TransformMarkus(False)
            scene black with dissolve
            if LastBattleOutcome == "defeat":
                "Whipping us away with it's powerful tentacles before retreating into the black depths of the water once more."
                $ LocFlush()
                show mc_transformed at left
                show markus_transformed at right_f
                with dissolve
                "Dazed, me and Markus turned to each other."
                MARKUS "That thing nearly killed us!"
                MC "(We should avoid that thing for now... I don't think it's going to give us a second chance.)"
                $ LocEnter()

            # will fall thru here on victory
            $ QstTwoEmperors().killedKraken = True    
            "After slashing and tearing off one of the beasts' tentacles that dropped down into the waters, the beast howled in rage as it quickly retreated and submerged itself back into the black depths from where it came."
            $ LocFlush()
            show mc_transformed:
                xcenter 0.1
            show markus_transformed:
                xcenter 0.9
                xzoom -1.0
            with dissolve
            MARKUS '{i}*Huff*{/i}... Would you please stop touching everything?!'
            $ AutoMus(True)
            MC '{i}...How the hell does that thing even live down here?{/i}'
            MARKUS "I don't fucking care to find out!"
            "I noticed on the floor, some strange shimmering gem that wasn't there before."
            $ PlayerAddItem("qst_kraken_gem")
            MC '(Huh? What is this thing?)' 
            $ LocEnter()

        "Step away":
            'Deciding it was probably not a good idea to continue messing with the water, I stepped back.'
            MC "(Whatever's in there isn't going to appreciate me splashing around.)"
            $ LocEnter()