label event_Elena_training:
    'As my eyes shifted open, I found Elena looming over my bed, arms folded as she glared at me.'
    show elena with dissolve:
        xcenter 0.45
        xzoom -1.0
    ELENA @talk "Come on, it's time... Get up."
    MC @talk 'Huh?'
    ELENA @angry 'UP!'
    'Still half asleep and wiping the sleet from my eyes, I yawned before asking,'
    MC @talk "What's going on?"
    ELENA @grumpy 'Training.'
    MC @talk '{i}Training?{/i}'
    ELENA @talk 'Come, we need to find some place we can train safely, perhaps beyond the city walls.'
    MC @talk 'Urghh, why do we-'
    ELENA @angry "Enough talk! Dress and come to me when you're ready to begin!"
    'Elena waited patiently with her arms folded.'
    MC '(Why do I have a feeling this is going to be difficult?)'
    ELENA @talk 'Are you ready to begin?'
    menu:
        "Yes, I am ready.":
            MC @talk "Yes, I'm ready."
            jump event_Elena_training2
        "I need to get some things done first.":
            ELENA @talk "Okay, I can wait."
            $ QstSetProgress(EventElenaTraining, 1)
            $ LocEnter()

label event_Elena_training2:
    ELENA @talk 'Good, then first, we need to slip out into the Valley of death away from prying eyes.'
    MC @talk 'What is all this-'
    ELENA @talk 'Come!'
    hide elena with dissolve
    'Before my eyes, Elena transformed once again into her wolf form, and moved to wait patiently by the front door for me to join her.'
    MC '{i}*Sigh*{/i}'
    scene black with dissolve
    #Cut to black
    'After some time...'
    #Cut to Elena and MC in the desert
    $ LocSet("novaras_gates")
    $ LocFlush()
    with dissolve
    show mc:
        xcenter 0.15
    show elena:
        xcenter 0.55
        xzoom -1.0
    with dissolve
    MC @talk "Okay, we're here, now-"
    'Suddenly, Elena lunged forward to attack!'
    $ AutoMus(False)
    $ PlayMusic("audio/music/10_Battle1.ogg")
    MC @angry 'Elena!'
    ELENA @angry 'Prepare yourself!'
    $ StartBattle(BattleData(BackgroundImage = "pbat_desert", CharIDList_Right = ["elena"], CharIDList_Left = ["mc"], CanTransform = False))
    $ AutoMus(True)
    $ LocFlush()
    show mc at cleft
    show elena at cright
    with dissolve

    if LastBattleOutcome == "defeat":
        ELENA @grumpy 'Hmm... There is still much work to be done.'
        MC @angry "You didn't even give me any notice!"
        ELENA @angry "And you think the enemy is going to let you know when they'll strike?"
        ELENA @grumpy "Your strikes are clumsy, too obvious for a keen eye and you don't seem to fully grasp that body of yours yet."
        MC @angry "I've only been using this body for a few days!"
        ELENA @grumpy "You're going to need to learn to be more prepared than that, the fights won't always be on {i}your{/i} terms."
    if LastBattleOutcome == "victory":
        ELENA @talk '{i}*Huff*{/i} good...'
        ELENA @grumpy 'But your strikes are still too clumsy, and your moves too predictable for anyone watching.'
        ELENA @talk "And you don't seem to fully grasp that body of yours."
        MC @talk "Elena, I've only been using this body a few days."
        ELENA @talk "Yes... And you were able to handle me pretty well with a spar so, well done."
        'Elena smiled.'
        ELENA @smile "There may be hope for you yet!"

    $ choicemenu = ["a", "b"]
    menu event_Elena_training_menu:
        'What was all this about?' if 'a' in choicemenu:
            ELENA @grumpy '{i}*Sigh*{/i}'
            ELENA @sad "I'm worried [player_name!t], I've watched you fight these last few days, and while you can handle some low level things well."
            ELENA @grumpy "I think you're going to struggle against a real challenge."
            if QstIsComplete(QstValleyOfPrey):
                menu:
                    'I killed a sandworm!': #If player killed one
                        ELENA @angry "If you think a sandworm is the scariest thing you'll face, you're in for a rude awakening."
                        ELENA @grumpy "And that over-confidence is going to get you killed."
                        $ choicemenu.remove('a')
                        jump event_Elena_training_menu
                    "I'll just train more, it'll be fine Elena.":
                        ELENA @sad "I hope so, [player_name!t]... I really do." #Loops back to main menu
                        $ choicemenu.remove('a')
                        jump event_Elena_training_menu
            else:
                MC @talk "I'll just train more, it'll be fine Elena."
                ELENA @sad "I hope so, [player_name!t]... I really do."
                $ choicemenu.remove('a')
                jump event_Elena_training_menu
        'How did you learn to fight like that?' if 'b' in choicemenu:
            ELENA @talk "Lord Vront made it so I was trained daily."
            ELENA @talk "If you think I'm a harsh teacher, you should have seen how the men trained me..."
            MC @talk "What if you didn't want to fight?"
            'Elena raised an eyebrow.'
            ELENA @grumpy "It didn't matter what I wanted."
            ELENA @grumpy "My training was, you either fight... Or you die."
            $ choicemenu.remove('b')
    MC @talk 'Are we done here?' #Continues
    ELENA @talk 'Not yet... There are a few more things I want to go over with you.'
    #fade to black, 'An hour later...' appears on screen
    scene black with dissolve
    'An hour later...'
    $ LocFlush()
    with dissolve
    show mc:
        xcenter 0.12
    show elena:
        xcenter 0.55
        xzoom -1.0
    with dissolve
    ELENA @talk '{i}*Huff*{/i}'
    ELENA @talk 'Yes, I think that will do for today.'
    MC @sad 'Elena, you really pushed yourself to the limits back there.'
    ELENA @grumpy "I have to stay sharp, stay ready."
    ELENA @grumpy "It's the only way."
    'I have the distinct impression that there lays some deep rooted pain within her.'
    "Elena seems to always feel like she is on a knife's edge, and she seems to treat her own life as forfeit."
    MC @talk '...Elena, you do know there is more to life than just fighting right?'
    'Elena seemed taken aback by the comment.'
    ELENA @sad '{i}...Maybe for others.{/i}'
    ELENA @sad 'I live to serve others.'
    MC @sad "Elena... That's not true."
    ELENA @sad '...'
    MC @sad 'Your life is important as well.'
    MC @sad 'You need to learn to-'
    ELENA @angry 'E-Enough!'
    "Elena's hard veneer began to crack, she clearly found this topic extremely difficult."
    ELENA @grumpy '...We should return back now, training is over.'
    $ CharChangeRel("elena", 1)
    hide elena with dissolve
    'Elena stormed off back in the direction of Novaras, transforming back into a wolf as I tailed behind her.'
    scene black with dissolve
    MC '{i}...Elena.{/i}'
    $ QstComplete(EventElenaTraining)
    $ LocSet("mc_house_bedroom")
    $ LocEnter()
