label qst_DamzelDizzt_2_sneaky:
    MC @talk 'We should try getting close to Tarek to get rid of him.'
    MARKUS 'Well, any ideas anyone?'
    'Nijah slowly raised her hand nervously.'
    NIJAH '... I haz idea.'
    'We both turned towards Nijah as she spoke.'
    NIJAH 'There iz a plant people from Ramon grow in their homes.'
    NIJAH 'It iz good for the air, but very bad to consume...'
    MC @talk '... Poison?'
    'Nijah nodded.'
    NIJAH "It iz called {i}‘Amira’s Tears’{/i}."
    NIJAH 'It iz said to have no taste when mixed with wine.'
    $ choicemenu = ["a"]

label qst_DamzelDizzt_2_sneaky_Menu:
    menu:
        'Why is it called Amira’s Tears?' if "a" in choicemenu:
            #1A.) Continued
            NIJAH 'Princess Helma long ago fell in love with Prince Abdel of Aruna, back then, Ramon was many small kingdoms.'
            NIJAH 'They were to wed, but Abdel was still in love with his favourite concubine, Amira, who had known him since they were children.'
            NIJAH 'Amira was too low standing to marry Abdel herself, but she was pregnant with his child.'
            NIJAH 'Amira knew, she could claim legitimacy once zer child was born as long as Abdel was not married.'
            NIJAH 'That way, Princess Helma thought her child would have to be acknowledged.'
            NIJAH 'So, on zer night of zer wedding, Amira poisoned Princess Helma’s cup.'
            NIJAH 'But to her horror, Prince Abdel grabbed her drink by mistake to raise his cup in his new wife’s honour.'
            NIJAH 'He drunk za wine before she could stop him and he died in Helma’s arms.'
            NIJAH 'She cried seven days and nights in regret, while the guards looked for the poisoner.'
            NIJAH 'When zer guards finally discovered her plot, they came to arrest her, but before they could, she flung herself from the tower to her death.'
            NIJAH 'So, we call the flower Amira’s Tears, zo we never forget the pain it can bring.'
            $ choicemenu.remove("a")
            jump qst_DamzelDizzt_2_sneaky_Menu

        "If we give Tarek a bottle with Amira's tears in, that should do the trick?":
            #2A.) Continued
            MARKUS 'Whoa, whoa, whoa, how are we going to get close Tarek? We still need that part of the plan.'
            MARKUS "Ah yes, I know you've never met us before, but if you don't mind having a few sips of this."
            MARKUS "Ah, yes of course it's fine!"
            NIJAH 'I would be bait.'
            MARKUS '...'
            MC @talk '...'
            NIJAH 'What? Iz good idea.'
            NIJAH 'If you take me there with my hands tied, they will take you to Tarek.'
            NIJAH 'Then, give him zer poisoned wine.'
            MC @talk 'If things go wrong, you could get hurt.'
            'Nijah smiled faintly.'
            NIJAH 'We try anyway.'
            MC @talk 'Alright then...'
            NIJAH 'Let me know when you want me to make za poisoned wine...'
            menu:
                'Let’s do it!':
                    #SCENE 5 (ALT) - NIJAH QUEST - (ASSASSIN/DIPLOMATIC CHOICE ROUTE) - THE BLACK DIAMOND - NIGHT
                    scene black with dissolve
                    $ TimeSetTo(TIME_DAY_END)
                    $ LocSet("novaras_dist_pleasure")
                    $ GoalComplete(QstDamzelInDiztrezz, 1)
                    $ GoalShow(QstDamzelInDiztrezz, 3)
                    'Later that night, with the poisoned bottle of wine in hand, we made our way towards the Black Diamond.'
                    "Nijah's hands were only loosely bound for a quick escape if needed."
                    'Knocking on the door, a slider was pulled open for two piercing eyes to glare at us from.'
                    'Satisfied, the slider closed again, and we heard the door unlock and open just wide enough for us to slip inside.'
                    MC @talk 'We’re here to see Tarek.'
                    MC @talk 'We have something he wants.'
                    'The guard looked Nijah up and down and grinned.'
                    'Nijah uncomfortably averted her gaze as the guard allowed us to pass.'
                    'Giving her ass a quick slap as she stumbled by, Nijah scowled at him, and I felt a tinge of rage to lash out at the man but held back.'
                    $ GoalComplete(QstDamzelInDiztrezz, 3)
                    $ GoalShow(QstDamzelInDiztrezz, 4)
                    $ LocSet("novaras_black_diamond")
                    $ LocFlush()
                    show cg_bandit at cright_f
                    show mc at cleft
                    with dissolve
                    'Sprawled about the place were figures half-dazed in a drug fuelled haze, looking up to us in a dream-like state before slipping away back to chasing dragons.'
                    'The air was thick with smoke and difficult to breathe in for one unaccustomed to its harshness,'
                    'But the room smelt of a strange, sweet aroma thanks to the plants they had strategically placed around the place in the hopes they might mask the other less savoury smells.'
                    'A half-naked girl danced on a makeshift bar they had erected.'
                    'She looked a little malnourished, and certainly didn’t want to be here, but if the black eye poorly concealed with makeup gave anything away, I doubt she had much choice in the matter.'
                    'Some of the men played enthusiastically at a card game, the table at one point erupting into loud groans as one of them slammed his cards onto the table and rose up cheering with glee.'
                    MC @talk 'Where is Tarek?'
                    'The guard who had let us pointed towards an iron door at the end of a corridor.'
                    
                    THUG @talk "Head down when you are ready, password is 'Silver'"
                    hide cg_bandit with easeoutright
                    MC '(Before heading down, perhaps we could look around?)'
                    $ HouseLockBlackDiamond().canExit = False
                    $ BlockWaitDynamic(True)
                    $ LocEnter()
                'On a second thought...':
                    jump nijah_damzelDizztrezz_chooseRoute
