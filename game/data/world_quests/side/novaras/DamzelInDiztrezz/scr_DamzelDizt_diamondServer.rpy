label qst_DamzelDizzt_3_Server:
    if QstDamzelInDiztrezz().fawhaName:
        $ FAWHA = Character(_("Fawha"), image="fawha")
    else:
        $ FAWHA = Character(_("Serving Girl"), image="fawha")
    show fawha with dissolve:
        xcenter 0.3
    "The serving girl seemed lost in thought for a moment, perhaps due to all the Raza smoke..."
    FAWHA 'Yes?'
    menu qst_damzeldizzt_3_server_menu:
        'I could use a drink.' if not QstDamzelInDiztrezz().serverPaidFor:
            MC "I could use a drink."
            FAWHA "Sure, five gold for a glass of Diamond Special."
            if PlayerItemQty("gold") >= 5:
                menu:
                    "Sure, I'll take it." (Req_Gold = 5):
                        MC "Sure, I'll take it."
                        $ PlayerRemItem("gold",5)
                        $ QstDamzelInDiztrezz().serverPaidFor = True
                        FAWHA @talk 'Here you go sir, enjoy.'
                        jump qst_damzeldizzt_3_server_menu
                    "I'll pass.":
                        FAWHA @talk 'Fine, if you change your mind...'
                        jump qst_damzeldizzt_3_server_menu
            else:
                MC 'Oh, nevermind...'
                jump qst_damzeldizzt_3_server_menu

        "The guards here all seem... {i}tense.{/i}" if QstDamzelInDiztrezz().serverPaidFor and not QstDamzelInDiztrezz().serverInfo and QstGetProgress(QstDamzelInDiztrezz) == 0:
            FAWHA @talk '...I should not be telling you this-'
            FAWHA @talk 'There are worries about in-fighting between the Khazahs and the Vulshans.'
            FAWHA @talk 'Tarek is struggling to keep these two co-operating, he is planning a meeting later to smooth things over between the sides.'
            FAWHA @talk 'Please, tell no one I told you this!'
            MC @talk 'Your secret is safe with me.'
            MC '(Perhaps I can use this information to my advantage.)' #unlocks sub choice.
            hide fawha with dissolve
            $ QstDamzelInDiztrezz().serverInfo = True
            $ GoalShow(QstDamzelInDiztrezz, 5)
            $ LocEnterQ()

        'Are they always like this with Raza? They seem barely alive.' if "a" in QstDamzelInDiztrezz().serverChoiceMenu:
            FAWHA @talk 'I-'
            FAWHA @talk 'You must be new here.'
            FAWHA @talk 'Raza feels wonderful when you start.'
            FAWHA @talk 'You are filed with energy and life.'
            FAWHA @talk 'But before you know it, the energy wears off quicker and quicker each time.'
            FAWHA @talk 'And instead of giving you energy, you begin to feel tired even with it, and insufferable without.'
            FAWHA @talk 'But by then, you {i}need{/i} it.'
            MC @talk 'You sound like you speak from experience.'
            FAWHA @talk '...Many girls here addicted, I have stayed away.'
            FAWHA @talk 'If they see me talking to you too long, they will ask questions.'
            FAWHA @talk 'Please, let us discuss something else.'
            $ QstDamzelInDiztrezz().serverChoiceMenu.remove("a")
            jump qst_damzeldizzt_3_server_menu

        "How much for your 'private' services?":
            'Nijah glanced over towards me, visibly confused.'
            FAWHA @talk "For just you, or your friend as well?"
            MARKUS "Uhh, [player_name!t], not that I'm complaining friend... But do we really have time for this?"
            FAWHA @talk 'One hundred coins to use my breasts.'
            FAWHA @talk 'Two hundred if I must bring a girl to assist with your friend.'
            menu:
                "I'll pay just for me!" (Req_Gold = 100):
                    $ PlayerRemItem("gold",100)
                    if not QstDamzelInDiztrezz().fawhaName:
                        FAWHA 'Very well, take a seat...'
                        MC @talk 'But before we begin, what is your name?'
                        FAWHA 'I-'
                        FAWHA @talk 'Fawha sir.'
                        $ QstDamzelInDiztrezz().fawhaName = True
                        $ FAWHA = Character(_("Fawha"), image = "fawha")
                        MC 'Is that your real name or the one you give to patrons?'
                        FAWHA 'Does it concern you my lord?'
                        MC 'Not at all, I just make it a policy to try and remember the names of girls who wrap their tits around my cock.'
                        'Fawha smirked at the remark.'
                        FAWHA 'I did not realize I was dealing with such a romantic.'
                    FAWHA 'Come, sit down...'
                    $ AutoMus(False)
                    $ PlayMusicRandom("mus_sex")
                    FAWHA "Shall I wear my mask while I please you my lord? Or do you wish to see my face?"
                    menu:
                        'Keep the Mask on':
                            FAWHA 'As you wish my lord...'
                            'Sitting down onto the soft, slightly worn down couch, Fawha fumbled with my belt as she pulled out my hardened cock, her eyes doing a double blink as she smiled looking at the member in front of her.'
                            FAWHA 'Mmm... I like it big.'
                            MC "Glad to serve..."
                            scene fawha_tj_mask with dissolve
                            $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
                            $ Pause()
                            'Wrapping both of her large nipple pierced brown tits around my cock, I let out a soft moan as she began to bop up and down, watching with a glint her eye for any changes in my expression.'
                            FAWHA 'Would you like me to talk dirty sir?'
                            MC 'Ahh... Yes...'
                            MC 'Well Fawha, keep moving those tits and milk me dry!'
                            FAWHA 'Of course sir!'
                            MC 'Mmm... G-Good...'
                            FAWHA 'Do you like that my lord? My master?'
                            FAWHA 'Do you like feeling these fat tits stroking your wonderful, thick cock dry?'
                            MC 'K-Keep going... Ahh...!'
                            'Fawha pressed her large breasts together, wrapping them around my cock as she moved rhythmically up and down...'
                            'The warm soft sensation of her breasts left me breathing heavily as I tried to control the impulse to leap onto her and fuck her senseless.'
                            "All the while, Fawha's sultry eyes remained locked onto me, biting at her lower lip as I felt her body become flushed with desire."
                            FAWHA 'Y-You... You are close...!'
                            MC 'Y-Yes!'
                            FAWHA 'Cum my lord! Cover me in your load!'
                            scene fawha_tj_mask_finish with flash
                            $ UnlockGalFlag("bd_girls","fawha_tj","var_mask")
                        'Show me your face.':
                            FAWHA 'As you wish my lord...'
                            'Sitting down onto the soft, slightly worn down couch, Fawha fumbled with my belt as she pulled out my hardened cock, her eyes doing a double blink as she smiled looking at the member in front of her.'
                            FAWHA 'Mmm... I like it big.'
                            MC "Glad to serve..."
                            scene fawha_tj_nomask with dissolve
                            $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
                            $ Pause()
                            'Wrapping both of her large nipple pierced brown tits around my cock, I let out a soft moan as she began to bop up and down, watching with a glint her eye for any changes in my expression.'
                            FAWHA 'Would you like me to talk dirty sir?'
                            MC 'Ahh... Yes...'
                            MC 'Well Fawha, keep moving those tits and milk me dry!'
                            FAWHA 'Of course sir!'
                            MC 'Mmm... G-Good...'
                            FAWHA 'Do you like that my lord? My master?'
                            FAWHA 'Do you like feeling these fat tits stroking your wonderful, thick cock dry?'
                            MC 'K-Keep going... Ahh...!'
                            'Fawha pressed her large breasts together, wrapping them around my cock as she moved rhythmically up and down...'
                            'The warm soft sensation of her breasts left me breathing heavily as I tried to control the impulse to leap onto her and fuck her senseless.'
                            "All the while, Fawha's sultry eyes remained locked onto me, biting at her lower lip as I felt her body become flushed with desire."
                            FAWHA 'Y-You... You are close...!'
                            MC 'Y-Yes!'
                            FAWHA 'Cum my lord! Cover me in your load!'
                            scene fawha_tj_nomask_finish with flash
                            $ UnlockGalFlag("bd_girls","fawha_tj","var_nomask")
                    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
                    $ ReduceInfectionFromSex("fawha")
                    $ UnlockGalSceneAndGrantXp("bd_girls","fawha_tj")
                    $ Pause()
                    MC 'Grghhh...!'
                    MC '{i}*Huff...*{/i}'
                    FAWHA 'I hope this was satisfying for you sir...'
                    MC '{i}Very.{/i}'
                    if QstDamzelInDiztrezz().fawhaOneShotAge == True:
                        FAWHA "I'm glad I could please you my lord."
                        FAWHA 'I must admit, there are younger girls here to choose... why me?'
                        MC 'Hm? How old are you Fawha?'
                        FAWHA 'I... I am forty four sir.'
                        menu:
                            "I'd have never guessed! You're beautiful for your age!":
                                FAWHA 'I... You are too kind my lord.'
                                FAWHA 'L-Let me know should you wish for my services again!'
                            "Don't worry, your body is still built to drain some cocks dry.":
                                FAWHA '...Is that so my lord?'
                                FAWHA 'Then return to me whenever you are need of my services.'
                                FAWHA '{i}*Whispering*{/i} And this old lady will drain your balls better than any of the other whores here.'
                                MC 'You know just the right thing to say...'
                    $ QstDamzelInDiztrezz().fawhaOneShotAge = False
                    scene black with dissolve
                    $ AutoMus(True)
                    $ LocFlush()
                    with dissolve
                    $ QstDamzelInDiztrezz().serverPaidFor = True
                    NIJAH 'C-Can we move on now please?'
                    $ LocEnterQ()

                "I'll pay for the two of us!" (Req_Gold = 200):

                    $ PlayerRemItem("gold", 200)
                    if not QstDamzelInDiztrezz().fawhaName:
                        FAWHA 'Very well, take a seat...'
                        MC @talk 'But before we begin, what is your name?'
                        FAWHA 'I-'
                        FAWHA @talk 'Fawha sir.'
                        $ QstDamzelInDiztrezz().fawhaName = True
                        $ FAWHA = Character("Fawha",image="fawha")
                        MC 'Is that your real name or the one you give to patrons?'
                        FAWHA 'Does it concern you my lord?'
                        MC 'Not at all, I just make it a policy to try and remember the names of girls who wrap their tits around my cock.'
                        'Fawha smirked at the remark.'
                        FAWHA 'I did not realize I was dealing with such a romantic.'

                    FAWHA 'Come, sit down...'
                    $ AutoMus(False)
                    $ PlayMusicRandom("mus_sex")
                    FAWHA "Shall I wear my mask while I please you my lord? Or do you wish to see my face?"
                    menu:
                        'Keep the Mask on':
                            FAWHA 'As you wish my lord...'
                            'Sitting down onto the soft, slightly worn down couch, Fawha fumbled with my belt as she pulled out my hardened cock, her eyes doing a double blink as she smiled looking at the member in front of her.'
                            FAWHA 'Mmm... I like it big.'
                            MC "Glad to serve..."
                            scene fawha_tj_mask with dissolve
                            $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
                            $ Pause()
                            'Wrapping both of her large nipple pierced brown tits around my cock, I let out a soft moan as she began to bop up and down, watching with a glint her eye for any changes in my expression.'
                            FAWHA 'Would you like me to talk dirty sir?'
                            MC 'Ahh... Yes...'
                            MC 'Well Fawha, keep moving those tits and milk me dry!'
                            FAWHA 'Of course sir!'
                            MC 'Mmm... G-Good...'
                            FAWHA 'Do you like that my lord? My master?'
                            FAWHA 'Do you like feeling these fat tits stroking your wonderful, thick cock dry?'
                            MC 'K-Keep going... Ahh...!'
                            'Fawha pressed her large breasts together, wrapping them around my cock as she moved rhythmically up and down...'
                            'The warm soft sensation of her breasts left me breathing heavily as I tried to control the impulse to leap onto her and fuck her senseless.'
                            "All the while, Fawha's sultry eyes remained locked onto me, biting at her lower lip as I felt her body become flushed with desire."
                            FAWHA 'Y-You... You are close...!'
                            MC 'Y-Yes!'
                            FAWHA 'Cum my lord! Cover me in your load!'
                            scene fawha_tj_mask_finish with flash
                            $ UnlockGalFlag("bd_girls","fawha_tj","var_mask")
                        'Show me your face.':
                            FAWHA 'As you wish my lord...'
                            $ CharSetVar("fawha", "mask", False)
                            'Sitting down onto the soft, slightly worn down couch, Fawha fumbled with my belt as she pulled out my hardened cock, her eyes doing a double blink as she smiled looking at the member in front of her.'
                            FAWHA 'Mmm... I like it big.'
                            MC "Glad to serve..."
                            scene fawha_tj_nomask with dissolve
                            $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
                            $ Pause()
                            'Wrapping both of her large nipple pierced brown tits around my cock, I let out a soft moan as she began to bop up and down, watching with a glint her eye for any changes in my expression.'
                            FAWHA 'Would you like me to talk dirty sir?'
                            MC 'Ahh... Yes...'
                            MC 'Well Fawha, keep moving those tits and milk me dry!'
                            FAWHA 'Of course sir!'
                            MC 'Mmm... G-Good...'
                            FAWHA 'Do you like that my lord? My master?'
                            FAWHA 'Do you like feeling these fat tits stroking your wonderful, thick cock dry?'
                            MC 'K-Keep going... Ahh...!'
                            'Fawha pressed her large breasts together, wrapping them around my cock as she moved rhythmically up and down...'
                            'The warm soft sensation of her breasts left me breathing heavily as I tried to control the impulse to leap onto her and fuck her senseless.'
                            "All the while, Fawha's sultry eyes remained locked onto me, biting at her lower lip as I felt her body become flushed with desire."
                            FAWHA 'Y-You... You are close...!'
                            MC 'Y-Yes!'
                            FAWHA 'Cum my lord! Cover me in your load!'
                            scene fawha_tj_nomask_finish with flash
                            $ UnlockGalFlag("bd_girls","fawha_tj","var_nomask")

                    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
                    $ ReduceInfectionFromSex("fawha")
                    $ UnlockGalSceneAndGrantXp("bd_girls","fawha_tj")
                    $ CharSetVar("fawha", "mask", True)
                    FAWHA 'Alea! Come here girl! Your help is needed.'
                    MARKUS '...Shall I just-'
                    FAWHA 'Sit, Alea shall be with you shortly.'
                    'Markus took a seat down onto the couch and waited patiently.'
                    FAWHA 'As for {i}you{/i}, shall we begin my lord?'
                    scene black with dissolve
                    $ Pause()
                    $ LocFlush()
                    with dissolve
                    '...While [player_name!t] was pre-occupied with his girl, I saw Alea approach me in her green dress, crouching down onto her knees as she crawled her way towards me.'
                    show alea with dissolve:
                        xcenter 0.5
                    ALEA 'So... Your friend has paid for you?'
                    MARKUS 'He has.'
                    ALEA 'How lucky I am to be given a client so handsome.'
                    'Alea licked her lips enticingly.'
                    ALEA "It's your lucky day, I'm going to rinse you dry for everything you've got."
                    ALEA 'But first... Mask on or off?'
                    menu:
                        'Keep it on!':
                            ALEA 'As you wish my lord...'
                            'Alea yanked at my belt and greedily pulled out my cock, her eye hungrily looking at it up and down.'
                            ALEA 'Mmm, if only they all came here like you.'
                            'Beside me, I could see the girl wrapping her tits around [player_name!t], rhythmically bouncing them as she spoke something to him.'
                            ALEA 'Ah ah...! Eyes on me now.'
                            ALEA "Now, let's have some fun with this!"
                            scene alea_tj_mask with dissolve
                            $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
                            "Alea's soft breasts wrapped around my cock as she began to rhythmically motion up and down teasingly."
                            "She kept glancing towards [player_name!t]'s girl, and I got the distinct impression there was some kind of small competition between them that neither of spoke openly about."
                            ALEA 'How do they feel my lord? Are my tits not better at stroking your cock than your little wife?'
                            MARKUS 'Ahh! I have no wife.'
                            ALEA 'What? No lovers? Mistress at least?'
                            MARKUS 'Mhhmm... N-Not yet.'
                            MARKUS 'Though I have familiarized myself with a few of the brothels now!'
                            ALEA "Mmm... No matter, I'm going to make this unforgettable for you anyway!"
                            "Alea's tits bounced up and down faster as she pressed them together tightly with her hands, there was a wild glint in her eyes as she grinned watching me writhe and squirm in her grip."
                            MARKUS "{i}*Huff!*{/i} I don't know how much longer I can hold like this!"
                            MARKUS 'Gods woman! Where did you learn to do this?'
                            ALEA 'Hush my lord, focus on covering this poor, depraved, Ramonian whores tits.'
                            ALEA 'A-Ah...! I can feel your cock twitching!'
                            ALEA 'Are you close?'
                            MARKUS "Yes! Grgh! I can't hold it much longer!"
                            ALEA "Don't, cover me in your hot seed! Come on! Do it! DO IT!"
                            scene alea_tj_mask_finish with flash
                            $ UnlockGalFlag("bd_girls","alea_tj","var_mask")

                        'Take the Mask off!':
                            ALEA 'As you wish my lord...'
                            $ CharSetVar("alea", "mask", False)
                            'Alea yanked at my belt and greedily pulled out my cock, her eye hungrily looking at it up and down.'
                            ALEA 'Mmm, if only they all came here like you.'
                            'Beside me, I could see the girl wrapping her tits around [player_name!t], rhythmically bouncing them as she spoke something to him.'
                            ALEA 'Ah ah...! Eyes on me now.'
                            ALEA "Now, let's have some fun with this!"
                            scene alea_tj_nomask with dissolve
                            $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
                            "Alea's soft breasts wrapped around my cock as she began to rhythmically motion up and down teasingly."
                            "She kept glancing towards [player_name!t]'s girl, and I got the distinct impression there was some kind of small competition between them that neither of spoke openly about."
                            ALEA 'How do they feel my lord? Are my tits not better at stroking your cock than your little wife?'
                            MARKUS 'Ahh! I have no wife.'
                            ALEA 'What? No lovers? Mistress at least?'
                            MARKUS 'Mhhmm... N-Not yet.'
                            MARKUS 'Though I have familiarized myself with a few of the brothels now!'
                            ALEA "Mmm... No matter, I'm going to make this unforgettable for you anyway!"
                            "Alea's tits bounced up and down faster as she pressed them together tightly with her hands, there was a wild glint in her eyes as she grinned watching me writhe and squirm in her grip."
                            MARKUS "{i}*Huff!*{/i} I don't know how much longer I can hold like this!"
                            MARKUS 'Gods woman! Where did you learn to do this?'
                            ALEA 'Hush my lord, focus on covering this poor, depraved, Ramonian whores tits.'
                            ALEA 'A-Ah...! I can feel your cock twitching!'
                            ALEA 'Are you close?'
                            MARKUS "Yes! Grgh! I can't hold it much longer!"
                            ALEA "Don't, cover me in your hot seed! Come on! Do it! DO IT!"
                            scene alea_tj_nomask_finish with flash
                            $ UnlockGalFlag("bd_girls","alea_tj","var_nomask")

                    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
                    $ ReduceInfectionFromSex("alea")
                    $ UnlockGalSceneAndGrantXp("bd_girls","alea_tj")
                    ALEA 'Oooh!'
                    MARKUS 'Gods...'
                    ALEA '{i}*Giggles*{/i} Well... That was a lot.'
                    MARKUS 'Thank you.'
                    ALEA "Fawha seems keen on your friend... But don't worry, I prefer my men blonde."
                    MARKUS "I'll make sure to look out for you the next time I'm here."
                    ALEA "You do that, and {i}maybe{/i} I'll give you something even more special than my tits to just fuck next time."
                    MARKUS '...!'
                    MC "Markus! You done?"
                    ALEA "Hm... Looks like Time's up my lord."
                    ALEA 'Well, we hope you were both satisfied.'
                    MC @talk '{i}Very.{/i}.'
                    ALEA "Come back anytime both... {i}*giggles*{/i}"
                    $ CharSetVar("alea", "mask", True)
                    scene black with dissolve
                    $ AutoMus(True)
                    $ LocFlush()
                    with dissolve
                    $ QstDamzelInDiztrezz().serverPaidFor = True
                    if QstDamzelInDiztrezz().fawhaOneShotAge == True:
                        show fawha with dissolve:
                            xcenter 0.3
                        FAWHA "I'm glad I could please you my lord."
                        FAWHA 'I must admit, there are younger girls here to choose... why me?'
                        MC 'Hm? How old are you Fawha?'
                        FAWHA 'I... I am forty four sir.'
                        menu:
                            "I'd have never guessed! You're beautiful for your age!":
                                FAWHA 'I... You are too kind my lord.'
                                FAWHA 'L-Let me know should you wish for my services again!'
                            "Don't worry, your body is still built to drain some cocks dry.":
                                FAWHA '...Is that so my lord?'
                                FAWHA 'Then return to me whenever you are need of my services.'
                                FAWHA '{i}*Whispering*{/i} And this old lady will drain your balls better than any of the other whores here.'
                                MC 'You know just the right thing to say...'
                    scene black with dissolve
                    $ LocFlush()
                    with dissolve
                    MARKUS 'Well, that was quite something!'
                    NIJAH 'Are you both done now please?'
                    $ LocEnterQ()

                'On second thought...': #Reverts back to menu.
                    MC "Actually, forget it."
                    jump qst_damzeldizzt_3_server_menu

        "I should go.":
            MC "I should go."
            FAWHA 'Alright, have a nice evening!'
            $ LocEnter()