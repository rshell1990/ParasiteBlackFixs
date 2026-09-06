label qst_DamzelDizzt_3_talkTarek:
    $ GoalComplete(QstDamzelInDiztrezz, 4)
    menu:
        "*Lie* We are working for the Inquisitors; we have been watching you for a while now.":
            TAREK 'Inquisitors you say?'
            TAREK 'And where is your uniforms {i}inquisitors?{/i}'
            TAREK @angry 'I always presumed you people were far too good for us lowly Ramonians to dress like the rest of us...'
            jump qst_DamzelDizzt_3_lie

        # Diplomatic route
        "I want you to leave Novaras.":
            jump qst_DamzelDizzt_5_evidence
            
        # Sell Nijah route
        "{image=[ICON.HEART_BROKE]} We want gold in exchange for Nijah, we know you want her.":
            jump qst_DamzelDizzt_3_sellNijah 

        # Battle begins
        "{image=[ICON.SWORDS]} Are you ready for the sweet embrace of death?":
            TAREK 'Men! Draw your blades!'
            jump qst_DamzelDizzt_3_ruckus
            

label qst_DamzelDizzt_3_lie:
        menu: #Continued from lie
            "The uniform tends to draw too attention for more... {i}delicate{/i} matters such as this.":
                TAREK '{i}Delicate matters?{/i} What are you talking about?'
                MC @talk "You’re going to flee the city tonight if you know what’s good for you."
                TAREK 'And why would I do that?'
                MC @talk 'We found one of your men trying to haul Nijah into town and arrested him.'
                MC @talk 'He’s confessed to everything, alongside other women who have since stepped forward.'
                jump qst_DamzelDizzt_3_talkTarek_successCharm
            "Fuck it, all this talking is starting to bore me. I'd much rather just fucking eviscerate you.":
                TAREK @angry 'Guards! Draw your blades!'
                jump qst_DamzelDizzt_3_ruckus
                #Battle begins.
            "How about I shove my boot down your throat? If we choose not to wear our uniforms we do so for good reason worm!":
                TAREK @angry "Ahh... There's that Inquisitor superiority shining through!"
                TAREK @angry 'Get to the fucking point, what do you want?'
                MC @talk "You’re going to flee the city tonight, if you know what’s good for you."
                TAREK 'And why would I do that?'
                MC @talk 'We found one of your men trying to haul Nijah into town and arrested him.'
                MC @talk 'He’s confessed to everything, alongside other women who have since stepped forward.'
                TAREK 'I have already paid your people well and was assured the Inquisitors would stay out of my affairs!'
                MC @talk 'The deal has changed.'
                'Tarek began to reach for his blade.'
                TAREK @angry 'No... No no no!'
                TAREK @angry 'This is a trick! You think you are smarter than Tarek?'
                TAREK @angry 'Who do you work for? WHO SENT YOU?!'
                TAREK @angry 'Was it the Vulshan? The Khazahs?'
                MC '(Shit, shit, shit! Think fast!)'

                menu:
                    'I am telling you the truth!':
                        TAREK 'LIAR! Men! Draw your blades!'
                        MC @talk 'Fuck!'
                        MARKUS 'Well, there goes stealth!'
                        jump qst_DamzelDizzt_3_ruckus#BATTLE BEGINS.
                    "Put your blade away fool, we're your only way out of this mess!":
                        TAREK @angry 'Speak quickly before I carve out your hearts!'
                        menu:
                            "...Carve out my heart? You think you can fucking threaten {i}me?{/i}":
                                TAREK @angry 'In all the hells who are you?!'
                                MC @angry "Oh, I'm going to enjoy turning you inside out and watching you bleed out."
                                "Tarek's hand began to tremble as he clutched the blade tighter."
                                TAREK @angry 'GUARDS!'
                                jump qst_DamzelDizzt_3_ruckus#Battle begins.
                            'Do you know how many heads will roll if it becomes public the inquisitors are working with lowlifes such as you?':
                                MC @angry 'Make no mistake, this is self preservation on our part and nothing more.'
                                TAREK '...'
                                MC 'Tarek loosened his grip around his blade, my words seemingly convincing him enough... for now.'
                                TAREK @sad 'But... how? How has this happened?'
                                jump qst_DamzelDizzt_3_talkTarek_successCharm

label qst_DamzelDizzt_3_ruckus:
        hide nijah with easeoutleft
        'Nijah pushed herself into the corner, terrified.'
        'Turning pale white as she watched me and Markus change form, her mouth trembled as she froze still,'
        play sound2 "audio/cfx/transform.ogg"
        
        $ AutoMus(False)
        $ PlayMusic("audio/music/31_Encounter.ogg")
        
        scene black with dissolve
        'But there was little time to explain things now!'
        $ TransformMC(True)
        $ TransformMarkus(True)
         
        $ StartBattle(BattleData(BackgroundImage = "pbat_diamond", CharIDList_Right = ["e_corruptGuard", "tarek", "e_bandit"]))

        $ TransformMC(False)
        $ TransformMarkus(False)

        scene cg_tarek_dead_off_para with dissolve
        $ BlackDiamondLogic().tarekFate = "died"

        'Hearing the ruckus downstairs, the other men came tumbling down the stairs, weapons drawn...'
        jump qst_DamzelDizzt_3_ruckus_TarekDead

label qst_DamzelDizzt_3_ruckus_TarekDead:
        $ TransformMC(True)
        $ TransformMarkus(True)
        
        $ AutoMus(False)
        $ PlayMusic("audio/music/31_Encounter.ogg")

        $ StartBattle(BattleData(BackgroundImage = "pbat_diamond", CharIDList_Right = ["e_thug", "e_bandit", "e_thug"]))
    
        MC "{i}*Huff* *Huff*{/i}"
        MC "(Hell, there's more!)"
         
        $ StartBattle(BattleData(BackgroundImage = "pbat_diamond", CharIDList_Right = ["e_bandit", "e_thug", "e_bandit"]))

        $ TransformMC(False)
        $ TransformMarkus(False)

        "Lifeless bodies fell to the floor, one upon another, torn to shreds by tooth and claw as both me and Markus greedily began to rip apart and devour pieces of their flesh."
        "The parasites inside grumbled in appreciation as we lapped up the delicious red meat."
        'Suddenly, we turned ready as we heard the clatter of feet, claws ready.'
        'Running around the corner was Nijah, whose face turned pale white in horror when she saw us.'
        scene bg_diamond_blood
        show mc_transformed at left
        show markus_transformed at right_f
        with dissolve
        show nijah at center_f with dissolve
        'Frozen in terror at what she was seeing, Nijah raised her hands up protectively, her mouth open ready to scream.'
        NIJAH '...!'
        MC @talk 'Nijah Wait!'
        NIJAH 'Get back! Stay away!'
        MC @talk "Nijah It’s me! It's [player_name!t]!"
        "Gently I moved forward and grabbed Nijah's arm, she screamed in horror before I reiterated it was me."
        MC @talk "It's me!"
        'After a few moments of seeing that I wasn’t going to hurt her, she slowly began to calm down.'
        'Her terrified eyes frantically looking me up and down.'
        NIJAH 'Zis is...'
        NIJAH '... {i}You?{/i}'
        MC @talk 'We don’t have time to explain, we have to leave now!'
        'Nijah, still pale white from seeing us feasting on Tarek, led us back up the stairs in a hurry.'
        NIJAH 'We go now! Guards coming!'
        scene black with dissolve
        $ AutoMus(True)
        $ LocSet("novaras_dist_pleasure")
        'In the distance, we could hear the shouts of the guards heading our way, and quickly clambered onto the rooftops of buildings where under the veil of darkness we crept out of the Pleasure District.'
        'Somehow, we had pulled it off, and behind me down below, I could see the guards rushing towards the chaos below.'
        'But by then, we had long vanished.'
        jump nijah_damzelDiztrezz_afterAction
