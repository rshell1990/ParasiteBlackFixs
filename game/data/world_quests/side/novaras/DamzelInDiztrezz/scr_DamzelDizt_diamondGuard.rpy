label qst_DamzelDizzt_3_ThugGuard:
    'The guard studied the room with perceptive gaze, then turned to me:'
    THUG 'What is it?'
    menu:
        "Let's get rid of Tarek!" if QstDamzelInDiztrezz().vulshanReady:
            MC "Let's get rid of Tarek!"
            $ GoalComplete(QstDamzelInDiztrezz, 5)
            $ GoalComplete(QstDamzelInDiztrezz, 6)
            jump qst_DamzelDizzt_3_VulshanRevolt
            
        'You should know Tarek is planning to remove the Vulshans.' if QstDamzelInDiztrezz().serverInfo == True and not QstDamzelInDiztrezz().vulshanReady == True:
            THUG @talk 'What? Speak before I cut your tongue out!'
            'Tarek has spoken to the Khazahs and plans to have them take over your territory.'
            THUG @talk 'This is... Why would Tarek do such a thing?'
            menu:
                'Because Tarek hates the Vulshans?':
                    MC 'Because Tarek hates the Vulshans?'
                    MC '(I guess...)'
                    THUG @talk 'What? No... Tarek hates the Zilhan, we have always been fair with Tarek and him with us.'
                    THUG @talk 'Whatever you are playing at, cease now...'
                    THUG @talk 'Before I cut out your tongue!'
                    MC @talk '(Damn it, I think I blew this.)'
                    $ QstDamzelInDiztrezz().offendedGuard = True
                    $ GoalHide(QstDamzelInDiztrezz, 5)
                    $ GoalHide(QstDamzelInDiztrezz, 6)
                    $ LocEnterQ()

                "Because the Khazahs are a safer bet than the Vulshans." if QstDamzelInDiztrezz().addictInfo == True:
                    MC @talk "The Khazahs are a safer bet than the Vulshans."
                    MC @talk "You're losing profits and struggling to hold the territory you have."
                    THUG @talk 'You, how do you know this?'
                    MC @talk "Your product is getting weaker, and likely now in-fighting will finish you off in the Khazah's don't."
                    MC @talk 'Why bet on a losing horse?'
                    THUG @talk 'You just expect me to believe you with no proof?'
                    MC @talk 'The choice is yours, listen to me now, or wither away later thinking about this very conversation...'
                    THUG '...'
                    THUG @talk 'Why are you telling me this?'
                    THUG @talk 'What do you have to gain from this?'
                    MC @talk 'I have a counter offer to make.'
                    MC @talk "Side with me and we take out Tarek together."
                    THUG @talk 'Why do you want Tarek dead?'
                    MC @talk 'My reasons are my own, are you in, or out?'
                    'The man sized up me and Markus.'
                    THUG @talk '...We will be outnumbered, how well can you fight?'
                    MC @talk 'We possess powerful magic to change our form.'
                    'The thug curiously looked us up and down incredulously.'
                    THUG @talk 'Now is not the time for jokes.'
                    MC @talk "I'm not joking."
                    'With a raised hand, I let a claw protrude out of my skin before protracting it, taken aback, the man stepped back in surprise for a moment before moving closer.'
                    'In a hushed tone, he spoke to us as he looked around for who else might be listening.'
                    THUG @talk 'What kind of magic was that?'
                    MC @talk "Do we have a deal or not?"
                    THUG '...'
                    THUG @talk 'Wait here, I will speak to the others.'
                    scene black with dissolve
                    'The man returned a short while later, looking around uneasily for any eyes watching us.'
                    $ LocFlush(dissolve)
                    THUG @talk 'Yes... We are in.'
                    THUG @talk 'When ready, speak to me and I will give the signal.'
                    MC "Nice."
                    $ QstDamzelInDiztrezz().vulshanReady = True
                    $ GoalHide(QstDamzelInDiztrezz, 5)
                    $ GoalShow(QstDamzelInDiztrezz, 6)
                    $ LocEnterQ()


        'So, do you work for Tarek or...' if "c" in QstDamzelInDiztrezz().guardChoiceMenu:
            MC 'So, do you work for Tarek or...'
            THUG @talk "I do not 'work' for Tarek, I am a Vulshan, Tarek merely serves our interests... for now."

        'I heard Vulshans were the weakest crew around.' if not QstDamzelInDiztrezz().vulshanReady:
            MC 'I heard Vulshans were the weakest crew around.'
            THUG @talk 'Do you want to fucking die or something? Get out of my sight!'
            $ QstDamzelInDiztrezz().offendedGuard = True
            $ GoalHide(QstDamzelInDiztrezz, 5)
            $ GoalHide(QstDamzelInDiztrezz, 6)
            $ LocEnterQ()

        'How do I join Vulshan?' if "a" in QstDamzelInDiztrezz().guardChoiceMenu:
            MC 'How do I join Vulshan?'
            'The man laughed.'
            THUG @talk 'Sorry, only those of Ramonian blood can join.'
            $ QstDamzelInDiztrezz().guardChoiceMenu.remove("a")
            jump qst_DamzelDizzt_3_ThugGuard

        'I was just wondering...' if "b" in QstDamzelInDiztrezz().guardChoiceMenu:
            MC 'I was just wondering...'
            THUG @talk 'Then wonder elsewhere and leave me alone.'
            $ QstDamzelInDiztrezz().guardChoiceMenu.remove("b")
            $ LocEnterQ()

        
        
        'I should go.':
            MC 'I should go.'
            THUG @talk 'A wise decision.'
            $ LocEnterQ()


label qst_DamzelDizzt_3_ThugGuardOffended:
    "The guard doesn't seem interested in any more talking."
    THUG 'Go away.'
    $ LocEnterQ()
