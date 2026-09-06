label qst_BiteBark_6_McRoomResolution:
    #Scene 7 - MC Bedroom
    #Scene plays auto upon entering the room
    $ LocSet("mc_house_bedroom")
    $ LocFlush()
    with dissolve
    show elena_w:
        zoom 0.45
        xcenter 0.4
        ypos 0.25
        xzoom -1.0
    'Elena paced out into the center of my bedroom and sat down silently facing me.'
    $ choicemenu = ['a', 'b', 'c', 'd']
    menu qst_BiteBark_6_McRoomResolution_menu:
        "You're not a real wolf... Are you?" if 'a' in choicemenu:
            ELENA_W '...'
            $ choicemenu.remove('a')
            jump qst_BiteBark_6_McRoomResolution_menu
        'Elena... Your name is Elena?' if 'b' in choicemenu:
            ELENA_W '...'
            $ choicemenu.remove('b')
            jump qst_BiteBark_6_McRoomResolution_menu
        'Why did you run off like that?' if 'c' in choicemenu:
            ELENA_W '...'
            $ choicemenu.remove('c')
            jump qst_BiteBark_6_McRoomResolution_menu
        'What or who are you looking for?' if 'd' in choicemenu:
            ELENA_W '...'
            $ choicemenu.remove('d')
            jump qst_BiteBark_6_McRoomResolution_menu
            #All choices Elena stares blankly at the player to.
    MC @talk "{i}*Sigh*{/i} This is hopeless... I don't know what you are, but if you don't talk I can't help you."
    'Rubbing my forehead in frustration, I was just about to turn and leave the wolf here alone when suddenly-'
    play sound "audio/cfx/detect_magic.ogg"
    scene black with flash
    $ AutoMus(False)
    $ PlayMusic("audio/music/33_Elena.ogg")
    'As Elena stood up onto her hind legs, her form began to shift and shape rapidly, till the slender naked form of what seemed like a half human, half wolf stood before me.'
    $ LocFlush()
    $ CharSetClothes("elena", "naked")
    show elena:
        xcenter 0.15
    with dissolve
    show mc with easeinright:
        xzoom -1.0
        xcenter 0.65
    MC @surprised '...You-!'
    ELENA @talk 'Hello...'
    $ ELENA_W = Character(_("Elena (wolf form)"), image = "elena_w")
    $ CharMeet("elena")
    MC @angry 'Who are you really? Why did you not show your form to me before!'
    ELENA @angry 'Why would I show this form to a human? Your kind have long made sport of wiping my kind out when found.'
    MC @talk 'Then why come with me? Why were you in the care of that beast master?'
    ELENA @angry 'Because you were the first one I could smell in a long time who was... {i}different.{/i}'
    ELENA @grumpy "Let's not pretend I'm the only one hiding amongst humans."
    MC @talk 'I am human.'
    'Elena smiled.'
    MC @sad '...A being has... attached itself to me.'
    MC @talk "But I am {i}still{/i} human."
    ELENA @grumpy "You sure about that?"
    ELENA @grumpy 'And do you really think other humans will care about the difference?'
    MC @talk "What do you want... Elena, is it?"
    "The wolf girls face softened as she spoke, her words soft like feathers."
    ELENA @grumpy '...{i}Help...{/i} I want help.'
    MC @talk 'What are you talking about?'
    ELENA @grumpy 'The girl I was meant to protect... The one that wretched Beastmaster told you had vanished.'
    ELENA @grumpy "I must find her, I made a vow to her father."
    MC @talk 'And you thought I would help you?'
    ELENA @grumpy 'Who else is there to trust? Humans are... Not kind to those different from them.'
    ELENA @grumpy "They've become cruel and hardened by war."
    # quest triggers (love points?)for those dialogue options
    $ choicemenu = ['a']
    menu qst_BiteBark_6_McRoomResolution_menu2:
        'I will help you... Elena.':
            "The wolf girls ears perked up, her face one of surprise that I had even agreed."
            ELENA @shock 'Just like that?'
            ELENA @shock "You don't want anything in return?"
            menu:
                'Remain a companion to me on my travels and I will help you find Lady Thornfall.':
                    'Elena pondered the idea for a moment before she bowed curtly.'
                    ELENA @talk 'Very well...'
                    ELENA @talk "I agree to your terms."

                'Do you have any coin?':
                    ELENA @grumpy 'Do I look like I carry coin on me?'
                    MC @talk 'Hmm... Then perhaps you can consider my services on loan?'
                    ELENA @talk 'Y-Yes... Lady Thornfall is very affluent, I am sure she will reward you generously for your services.'
                    MC @talk '...Very well.'
                    ELENA @smile 'Good, then we have a deal!'

                'Turn around for me.':
                    ELENA @shock '...W-What?'
                    MC @smile 'Turn around.'
                    MC @bitelip 'I want to get a better look at you.'
                    'From the grin on my face, Elena realized quickly what I wanted, and with flushed cheeks she nervously turned around.'
                    hide elena with dissolve
                    show elena_back_naked with dissolve:
                        xzoom -1.0
                        xoffset 50
                        yoffset 25
                    #Show Elena turned around naked, have camera pan from top to bottom on camera model
                    'As my eyes looked over her cute ass, Elena let me gaze for a few moments before chiming in,'
                    ELENA '{i}Are you done yet?{/i}'
                    MC @talk 'Yes.'
                    hide elena_back_naked with dissolve
                    show elena with dissolve:
                        xcenter 0.15
                    'Elena turned back to face me, still red in the face.'
                    ELENA @grumpy 'So... Will you help me?'
                    MC @smile 'Always happy to help a beautiful lady in need!'
                    ELENA @shock '{i}Beautiful?{/i}'
                    ELENA @lewd 'I... see.'
                    ELENA @smile 'Alright, moving on...!'
        'Who is this girl? If I am to help you, I need to know more.' if 'a' in choicemenu:
            ELENA @grumpy 'Lady Grace Thornfall, the last of the Thornfall line.'
            ELENA @grumpy 'Her father Lord Vront made me swear a vow before his passing that I would protect her.'
            ELENA @grumpy "She was meant to return home from her business abroad but... She has simply vanished."
            ELENA @grumpy 'I have been looking for her since... Trying to find what I can.'
            MC @talk "How do you know she isn't just dead?"
            ELENA @sad 'I do not know... Yet whatever the answer, I must know.'
            ELENA @sad 'So, will you help me?'
            $ choicemenu.remove('a')
            jump qst_BiteBark_6_McRoomResolution_menu2
        '{image=[ICON.HEART_BROKE]} I am sorry Elena, I cannot help you':
            ELENA @sad '{i}*sigh*{/i} very well... I am sorry for deceiving you so.'
            ELENA @grumpy 'But I must go now.'
            MC @surprised "Are you sure you don't wish to stay? There is no need to leave so soon."
            ELENA @grumpy "Your offer is kind, but no... She's still out there, I can feel it."
            ELENA @sad "I cannot rest till the lady is safe."
            ELENA @grumpy 'Farewell... Strange traveller.'
            hide elena with dissolve
            play sound "audio/cfx/detect_magic.ogg"
            scene black with dissolve
            'In that moment, Elena once again morphed herself down into her blue wolf form, and before I knew it, she had sprinted past me out of the door.'
            'I heard [regina_ref!t] cry out as Elena no doubt bolted out of the front door, and she quickly rushed inside to speak to me.'
            $ LocFlush()
            show mc:
                xcenter 0.15
            with dissolve
            show regina at cright_f with easeinright
            REGINA @shock_talk 'What happened? The wolf-'
            MC @sad "It's alright, just let her go."
            '[regina_ref_cap!t] opened her mouth to say something, but instead she angrily slammed the side of the fist lightly into the wall muttering under her breathe.'
            REGINA @angry '{i}Damn it...{/i}'
            hide regina with easeoutright
            MC @sad "(I feel bad I couldn't help her but... I'd only be taking on more unnecessary risk for myself.)"
            MC "(I hope she finds what she is looking for, perhaps one day our paths will cross again?)"
            $ QstComplete(QstBiteBark)
            $ GoalHide(QstBiteBark, 6)
            $ GoalHide(QstBiteBark, 7)
            $ LocEnter()

        

    #All choices continued
    ELENA @grumpy 'Oh... One thing... While in this city, I will likely have to remain in my wolf form in a fight.'
    ELENA @grumpy 'Too dangerous to show my true form.'
    MC @talk 'I understand.'
    'As my eyes scanned the wolf girl up and down, I felt the tinge of excitement staring at her slender, nude body.'
    'Noticing this, Elena raised an eyebrow inquiring.'
    ELENA @grumpy 'Is something the matter?'
    MC @surprised "I... Well you're..."
    ELENA @grumpy '...My form bothers you?'
    MC @surprised 'N-No! You look beautiful!'
    MC @talk 'But, perhaps some clothes are in order?'
    ELENA @grumpy 'Urgh, why are you humans so determined to coat yourselves in fabrics and such?'
    ELENA @talk 'You all seem so ashamed almost of your natural forms.'
    MC @talk "We're not ashamed, just more reserved."
    MC @talk 'And there may call for an occasion where clothes {i}are{/i} needed.'
    ELENA @talk 'Hmph... A valid point I suppose.'
    ELENA @talk 'I have these rags I found scavenging...'
    'Elena presented to me the loose torn rags which she wrapped around herself.'
    ELENA @talk 'Better?'
    MC @talk "Well... That's better than nothing."
    MC @talk 'But I think something a little more pragmatic is in order than just rags.'
    ELENA @grumpy 'But who could we trust to make something for me?'
    #If player has met the elven tailor before
    if QstGetProgress(DialogueDros) > 0:
        MC '(Hmm... Perhaps the elf might be of assistance?)'
    else:
    #If player hasn't met the elven tailor
        MC '(I suppose I should look around the city more... There has to be someone who can help.)'
    $ AutoMus(True)
    $ QstSetProgress(QstBiteBark, 6)
    $ LocEnter()
