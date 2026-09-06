label qst_bloodhound_2_lake:
    #If player has found the sigil and note 
    'Stepping closer towards the water bank, I glanced down at my reflection flickering in the water for a moment.'
    'I noticed {i}something red and glimmering{/i} approaching almost hypnotically slow.'
    'I felt every hair stand on my neck as I felt the sudden urge to leap back.'
    "As I did so, the thing emerged violently from the water, it's single red eye glaring towards me."
    scene cg_slimelark with flash
    
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_boss")
    "Bound inside its horrifying seal, the Guardians were half dissolved, most already dead, lifelessly floating in the acidic mass."
    $ QstSetProgress(QstTheBloodhound, 3)
    'One though, a girl, all bones with her eyes peeled back as she cried did her best to stretch out a dissolved hand to me.'
    'Screaming inside her silent prison, the slime forced its way down her throat and she trembled as her eyes rolled white.'
    'Then, she was as lifeless as all the others.'
    play sound2 "audio/cfx/transform.ogg"
    'With little time to waste, I tore away at my flesh and stared down the horrific monstrosity before me.'

    $ TransformMC(True)
    $ TransformMarkus(True)

    $ StartBattle(BattleData(BackgroundImage = "pbat_lake", CharIDList_Right = ["e_bigSlimelark"]))

    ### achievement
    if can_unlock_achievement("A_STICKY_TYRANT"):
        $ unlock_achievement("A_STICKY_TYRANT")

    $ TransformMC(False)
    $ TransformMarkus(False)

    "Dissolving into the ground and sizziling, the growling monstrosity's cries began to die down into a distorted murmur till it lay silent."
    jump qst_bloodhound_2_lake_postbattle

label qst_bloodhound_2_lake_postbattle:
    $ LocFlush()
    show mc_transformed:
        xcenter 0.1
    with dissolve
    MC @talk '{i}*Huff... Huff*{/i}'
    $ AutoMus(True)
    MC '(That was too close.)'
    'From behind, I could hear the sounds of painful grunts and scuffling.'
    'I turned quickly expecting some other horror from the lake ready to strike.'
    'Instead, I saw a young knight clad in armour dragging his way across the grass away from me.'
    'His left leg missing as he dragged a trail of blood behind him, I approached him cautiously, reaching out towards him with my hand outstretched.'
    'The man turned weakly to swing his sword at me, but I managed to pull back in time and dodge it.'
    if IsDaytime():
        scene cg_dravenham_day
    else:
        scene cg_dravenham_night
    with dissolve
    'His face was ghosty white, his eyes wide in fear as he cried at me between his heavy, desperate breaths.'

    UNKNOWN 'Back! BACK!'
    MC 'Hold! I am not here to hurt you!'
    UNKNOWN 'You... You speak, {i}beast?{/i}' 
    MC "I'm here for the guardians."
    'The man began to laugh, and then cry as tears streamed down his eyes.'
    UNKNOWN "Hahahaha!"
    UNKNOWN "You've found them!"
    UNKNOWN "At least {i}*cough*{/i} the bits and pieces left of us."
    MC "You're bleeding out, if we don't get the wound treated and sealed soon you'll die."
    UNKNOWN "{i}*Cough!*{/i} It's hopeless... I'm finished."
    MC 'Who are you?' 
    UNKNOWN "Dravenham... At your service... What's left of it."
    
    DRAVENHAM 'They sent {i}you{/i} to rescue us?'
    DRAVENHAM "I've never seen a beast like you before."
    MC "I'm afraid there's no rescue party."
    MC "I came looking for information on a missing person."
    DRAVENHAM 'What?! Are you fucki- *cough*'
    MC "No one knows how dire your adventure ended up."
    'The man began to sob once again, barely managing to hold himself together.' 
    DRAVENHAM 'Elsa... Roca... Twhain... I failed them...'
    MC 'Dravenham, I know you are in pain but I fear our time together is short, I can hear your heartbeat slow down.' 
    DRAVENHAM 'Then ask, {i}beast{/i}... Ask whatever it is you have to.'
    $ choicemenu = ['a','b']
    menu qst_bloodhound_2_lake_postbattle_dravenham:
        # exhaustible options
        'Are there no other survivors?' if 'a' in choicemenu:
            DRAVENHAM 'None... The thing only kept me alive to let its young feed on me.'
            DRAVENHAM "{i}*Huff*{/i} It wouldn't let me leave... It wouldn't let me fucking leave!"
            MC 'Stay with me Dravenham.'
            DRAVENHAM 'Please... Everything is so numb now.'
            $ choicemenu.remove('a')
            jump qst_bloodhound_2_lake_postbattle_dravenham
        'What were you all doing out here?' if 'b' in choicemenu:
            DRAVENHAM "We weren't just here for the quest..."
            DRAVENHAM "A servant of some minor nobles offered to pay us triple if we could capture a baby slimelark and bring it back."
            MC 'But why?'
            DRAVENHAM 'The young... Slimelarks can take many forms, including beautiful women, if trained.'
            DRAVENHAM 'The fucking perverts wanted to keep a few as their own private slaves.'
            MC 'Who?'
            DRAVENHAM "Don't know... The servant only told us he was acting as a intermediary."
            DRAVENHAM "None of them care about us, we're all just expendable to them."
            DRAVENHAM 'Urghh... I feel so dizzy...'
            MC 'Focus! Just a little more!'
            $ choicemenu.remove('b')
            jump qst_bloodhound_2_lake_postbattle_dravenham
        # moves on
        'Do you know a man named Azul?':
            pass
    DRAVENHAM 'Azul? Yes... I know of him.'
    DRAVENHAM 'He would offer us advice on our quests...'
    DRAVENHAM 'For coin.'
    DRAVENHAM 'Something hap-*cough* happened?'
    MC "He's gone missing."
    MC 'What did he talk to you about the last time you saw him?'
    DRAVENHAM 'Missing? Crap...'
    DRAVENHAM 'He was afraid of something.'
    DRAVENHAM 'He said he had information that could end up in...'
    "Dravenham mustered himself, grasping for life slipping away."
    DRAVENHAM '...In the wrong hands.'
    DRAVENHAM '"Send the whole guild into chaos" he said...'
    DRAVENHAM "He then asked if he could hire us for protection, but by then, we'd already taken on... this."
    DRAVENHAM "We were going to help him afterwards..."
    DRAVENHAM "Ha... I guess as you can see, that didn't work out."
    MC 'Where is he now?'
    DRAVENHAM 'He gave... {i}Urghh...{/i} an address to a safehouse of his.'
    DRAVENHAM 'Told us it was too dangerous for him to be out in public anymore.'
    DRAVENHAM 'That {i}some people were after him{/i}.'
    'Hand slid into his breastplate, Dravenham pulled out a bloodied note with something scrawled on it and handed it to me.'
    DRAVENHAM 'He... He gave me this...'
    $ QstSetProgress(QstTheBloodhound, 4)
    $ QstStart(HouseLockAzul)
    DRAVENHAM "Hey... I'm... I'm so cold now."
    DRAVENHAM "I can't... I can't feel anything anymore."
    DRAVENHAM "Please... {i}Please...{/i}"
    DRAVENHAM "I don't want to die... I don't... I don't want to."
    DRAVENHAM 'I need to tell her... I need to tell-'
    'The man began to shake in my arms slightly, his body going into sharp spasms as he briefly wretched up some blood.'
    'His wide young eyes soon began to turn cloudy, and the final gasp escaped his lips as his body went limp.'
    DRAVENHAM '{i}Yuna...{/i}'
    MC '...'
    MC "Rest now, young knight."
    MC "Your battle has ended."
    MC "(I have the safehouse address now, it's not far from my home.)"
    "Attached to Dravenhams armor was a large silver key."
    $ PlayerAddItem("qst_draven_key", 1)
    MC '(I wonder what this opens? Perhaps that box over there...)'
    jump qst_bloodhound_2_lake_openbox