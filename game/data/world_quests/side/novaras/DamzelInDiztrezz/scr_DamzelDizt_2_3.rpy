label qst_DamzelDizzt_2_frontal_pit:
    #Boss battle against Betsy - (Can we make the scorpion Red?) Betsy should be a significantly challenging boss because she's basically a meth'd up giant scorpion...
    #Upon winning
    $ TransformMC(True)
    $ TransformMarkus(True)
     
    $ StartBattle(BattleData(BackgroundImage = "pbat_sewer", CharIDList_Right = ["e_scorpionBoss_red"]))

    $ TransformMC(False)
    $ TransformMarkus(False)

    'The thing managed to grab me into one of its claws and began to tighten its clasp around me, with all my strength, I struggled to hold back as the things blade like claws tightened to sever me.'
    "From above, I could hear the men cheering and shouting, the sounds of coins dropping on the floor as they bet on which of us 'Betsy' would kill first."
    TAREK @angry 'Finish them! FINISH THEM NOW!'
    MC "(Shit! I can't hold on much longer! This thing is too-)"
    'Suddenly, Markus charged into the beast, knocking it off balance enough to let me go.'
    MARKUS '(NOW [player_name!t]! WHILE I HAVE IT DISTRACTED!)'
    'Leaping onto the thing, I raised my claws which seemed to glimmer from the only rays of light from the opening above.'
    'Dealing the death blow, I shoved my claws through the things soft eyes and pierced through into its brain, causing the beast to sway before crashing down onto the ground dead.'
    'The laughter and cheers stopped, realization dawning on them as murmurs quickly turned to growing panic and confusion.'
    MC '(Fuck... That was too close.)'
    scene bg_diamond_blood with dissolve
    'Suddenly, the doors burst open as Nijah hurried inside.'
    show nijah at center with dissolve
    NIJAH '[player_name!t]! Markus! You must go! There is talk of mons-'
    "Nijah's face turned pale white in horror when she saw us."
    'She froze, unable to move as her mouth trembled.'
    'Suddenly, while we were distracted, Tarek grabbed Nijah and pulled her towards him, blade at her throat.'
    hide nijah
    show cg_tarek_nijah_hostage at center
    with dissolve
    TAREK angry '...'
    NIJAH sad '..!'
    NIJAH @sad 'L-Let me go!'
    TAREK @angry 'Quiet you!'
    TAREK @angry 'What are you waiting for fools?! Close the fucking door!'
    'We heard the cogs twisting as the trap door began to close above us, the rays of light slowly dissipating.'
    MARKUS '([player_name!t]! Hold on!)'
    'Grabbing onto Markus, he sprung into the air, and riding on his wings we crashed through the door back onto the main floor!'
    TAREK @shock 'K-Kill them you fools! KILL THEM!'
    'Many of the men simply dropped their blades and fled for the door.'
    TAREK @angry 'Where are you all going?! COWARDS!'
    'With most of his men fled, only his most loyal guard remained.'
    NIJAH 'Let me go!'
    MC 'Nijah!'
    TAREK @angry 'Ho ho! The beast speaks!'
    NIJAH '...[player_name!t]? You... You are...'
    TAREK @angry 'Enough!'
    TAREK 'She matters to you, yes? I can see it in your hesitation!'
    TAREK @angry 'Let me pass and leave this place and the girl is yours!'
    TAREK @smile "Otherwise... {i}I'll sever her throat here and now!{/i}"
    MC "Leave the girl Tarek, it's over."
    MC "The guards will soon be storming the place after all this chaos, you won't make it out anyway."
    TAREK @angry 'I will take my chances!'
    TAREK @angry 'Now what will it be? Let me pass or not!'
    MC "(Shit! Why do I say? If I'm not careful now, he could kill Nijah!)"
    MC "(But... What if Tarek somehow manages to escape? We've come this far, we need to finish this!)"
    menu:
        "{image=[ICON.DEATH]} I'll tear you limb from fucking limb!":
            TAREK @angry 'Wrong answer!'
            'I leapt forward to try and stop him, springing out one of my tentacles to whack the blade away but it was too late.'
            hide cg_tarek_nijah_hostage
            show cg_tarek_nijah_hostage_killed at center
            with flash
            'Nijah screamed as the blade slide across her throat, a red line appearing that soon flowed red as she choked on her blood.'
            $ CharKill("nijah")
            $ CharAddRelEntry("nijah", "killed_by_tarek")
            MC 'NIJAH! NO!'
            TAREK @angry 'You should have listened when you had the chance!'
            play sound2 "audio/cfx/transform.ogg"
            $ AutoMus(False)
            $ PlayMusic("audio/music/31_Encounter.ogg")
            TAREK 'Come then, beasts!'
            TAREK 'Kill me if you can!'
            $ TransformMC(True)
            $ TransformMarkus(True)
             
            $ StartBattle(BattleData(BackgroundImage = "pbat_diamond", CharIDList_Right = ["e_corruptGuard", "tarek", "e_bandit"]))

            $ TransformMC(False)
            $ TransformMarkus(False)

            "Tarek's lifeless body fell to the floor, torn to shreds by tooth and claw as both me and Markus greedily began to rip apart and devour pieces of his flesh."
            "The parasites inside grumbled in appreciation as we lapped up the delicious red meat."
            "Slowly, I pried myself away from the bloodlust towards Nijah's body, holding her in both of my arms as she gasped for air..."
            'As the adrenaline passed and the beast subsided, I felt this sickening feeling inside me, my stomach twisting in knots as I looked down at her ever paler face.'
            "I felt myself begin to shake as something moved within me, tears beginning to form around my glassy eyes."
            'Gently, she raised a hand towards my face, carressing it before her hand went limp.'
            scene bg_diamond_blood with dissolve
            show mc_transformed:
                xcenter 0.5
            with dissolve
            MC "I'm sorry... I'm so sorry... I didn't mean for this! This wasn't supposed to happen!"
            'I roared loudly into the air, shaking the very foundations of the building as Markus reached out to grab my shoulder.'
            show mc_transformed:
                xcenter 0.2
            with dissolve
            show markus_transformed with easeinright:
                xcenter 0.8
                xzoom -1.0
            MARKUS '[player_name!t]! We must go!'
            MARKUS 'The guards are here!'
            "From outside, I could hear the footsteps of the guards rushing towards us, and only at Markus' further insistance did I pull away from her."
            MARKUS '(We must go! We must go now!)'
            'Climbing the rafters of the building and out one of the windows, we made our narrow escape into the darkness once again...'

            scene black with dissolve
            $ LocSet("mc_house_bedroom")
            $ LocFlush()
            with dissolve
            show mc at left
            show markus at right_f
            $ AutoMus(True)
            #Scene cuts to MC and Markus in MC bedroom (Human form)
            MC @sad '...'
            MARKUS @sad "[player_name!t]... It wasn't your fault, you tried-"
            MC 'Just go Markus... Please.'
            MARKUS @sad '...I will make sure you are alright in the morning.'
            #MARKUS LEAVES
            hide markus with easeoutright
            scene black with dissolve
            'I started to cry, slumping down onto my bed and curling up into a ball.'
            'Reminded again of what it meant to lose another friend...'
            MC @sad '...Nijah... {i}Nijah...{/i}'

            # quest end sequence
            $ GoalComplete(QstDamzelInDiztrezz, 2)
            $ QstComplete(PrimerDamzelInDiztrezz)
            $ QstComplete(QstDamzelInDiztrezz)
            $ QstComplete(EventNijahRescue)
            $ NoteLock("NijahStayingAtMCs")
            $ QstStart(HouseLockBlackDiamond)
            $ QstStart(BlackDiamondLogic)
            $ HouseLockBlackDiamond().canExit = True
            $ HouseLockBlackDiamond().canBeAccessed = True
            $ BlockWaitDynamic(False)
            $ QstStart(EventBlackDiamondPostMassacre)
            $ LocEnter()

        'Okay! Give us the girl and you can live!':
            TAREK 'A wise decision...'
            "With his blade still at Nijah's throat, he shuffled towards the door."
            show cg_tarek_nijah_hostage at right with easeoutright
            show markus_transformed at left with easeinleft
            MARKUS 'This wont end well for you... The guards are already coming.'
            MARKUS 'Hurting her will achieve nothing!'
            TAREK @angry 'The minute I hand over the bitch you two will tear me to shreds like the others!'
            show mc_transformed at center with easeinleft
            MC 'Give us the girl and we wont!'
            TAREK 'You want her?'
            'Suddenly, Tarek shoved Nijah forward before sharply booting her down the vast opening of the trap door.'
            TAREK @angry 'HAVE HER!'
            scene cg_diamond_pit1 with flash
            'Nijah screamed as she began falling down the hole into darkness!'
            MC '{b}NIJAH!{/b}'
            'I leapt down after her, falling into the darkness, the wind rushing past me as I reached out to grab her.'
            'With both hands I grabbed her, twisting onto my back as I launched the tentacles into the walls, making them drag for the final duration of the drop.'
            scene cg_diamond_pit2 with dissolve
            'Nijah continued to scream, but with enough force, I managed to slow us down enough to stop us slamming into the ground.'
            'Gently, as I let Nijah go, she looked up to me.'
            scene pbat_sewer with dissolve
            show mc_transformed:
                xcenter 0.3
            show nijah:
                xcenter 0.7
                xzoom -1.0
            with dissolve
            NIJAH '[player_name!t]... You... Its...'
            MARKUS '[player_name!t]! Need some help here!'
            scene black with dissolve
            "I gently grabbed Nijah's shoulders, raspily telling her to wait here as I clambered my way frantically to the top once again."
            NIJAH '(...He saved me.)'
            NIJAH '{i}(...What is he?){/i}'
            #Back on surface.
            'Back on top, Tarek was frantically battling against Markus, rolling to dodge the blast of fire before swinging his blade wildy at Markus, cutting his arm.'
            MARKUS '*Growls!*'
            TAREK @angry "So, you beasts want to take me?"
            TAREK @angry 'Come then, beasts!'
            TAREK @angry 'Kill me if you can!'

            $ TransformMC(True)
            $ TransformMarkus(True)
             
            $ StartBattle(BattleData(BackgroundImage = "pbat_diamond", CharIDList_Right = ["e_corruptGuard", "tarek", "e_bandit"]))

            $ TransformMC(False)
            $ TransformMarkus(False)

            $ BlackDiamondLogic().tarekFate = "died"

            "Tarek's lifeless body fell to the floor, torn to shreds by tooth and claw as both me and Markus greedily began to rip apart and devour pieces of his flesh."
            "The parasites inside grumbled in appreciation as we lapped up the delicious red meat."
            'Finally, prying myself away from the delicious meat I shook Markus.'
            scene bg_diamond_blood with dissolve
            show markus_transformed at right_f
            show mc_transformed at left
            with dissolve
            MC 'Footsteps! The guards are coming!'
            MARKUS 'We must go! Now!'
            MARKUS '...Just after one more bite.'
            'I stopped Markus from indulging further.'
            MC 'Nijah! Bring her up quickly!'
            'Markus hissed in acknowledgement, leaping down into the darkness before returning with Nijah in his arms.'
            'Gently, he let her down as she stepped shakily towards me.'
            'Her terrified eyes frantically looking me up and down.'
            'I heard her heart drumming as she rested her hands nervously onto my chest.'
            show nijah at center_f with dissolve
            NIJAH 'Zis is...'
            NIJAH '... {i}You?{/i}'
            'I gently took her hands into mine.'
            MC @talk 'We don’t have time to explain, we have to leave now!'
            NIJAH 'Y-Yes! Go now!'
            scene black with dissolve
            'In the distance, we could hear the shouts of the guards heading our way, and quickly clambered onto the rafters and then out the window with Nijah over my shoulder.'
            'The guards burst through moments later, horrified at the bloody scene before them but we were already gone.'
            'I heard a few trembling voices behind us muttering {i}by the gods... What could have done this?{/i}'
            'But quickly, we were already traversing the rooftops of buildings where under the veil of darkness we crept out of the Pleasure District.'
            'Somehow, we had pulled it off, and behind me down below, I could see more guards rushing towards the chaos below.'
            'And just like that, it was over, and we slipped away and vanished.'
            $ QstStart(EventBlackDiamondPostMassacre)
            $ AutoMus(True)
            $ GoalComplete(QstDamzelInDiztrezz, 2)
            jump nijah_damzelDiztrezz_afterAction
