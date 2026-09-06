label scr_WomansTouch_2:
    scene bg_weeping_heart_brothel_room with dissolve
    #Use old brothel bedroom BG here as placeholder
    show helena with dissolve:
        xcenter 0.65
    show mc with easeinleft:
        xcenter 0.15
    HELENA @talk 'Well, where is this girl you speak of?'
    MC @talk "Elena! It's alright to come in."
    'Elena trotted into the room, and Helena stared at the blue wolf before her before scoffing.'
    show elena_w with easeinleft:
        xcenter 0.2
    HELENA @angry '{i}...Surely this is some kind of jest?{/i}'
    'I turned to look towards Elena.'
    MC @talk "It's alright Elena, show her your true form."
    scene black with dissolve
    'In that moment, as Elena rose up on hind legs and transformed into the wolf girl before her, Helena stepped back, at first anxious and afraid of what she was seeing.'
    play sound "audio/cfx/detect_magic.ogg"
    HELENA @shock 'You...'
    scene bg_weeping_heart_brothel_room
    with dissolve
    $ CharSetClothes("elena", "naked")
    show helena:
        xcenter 0.65
    show mc:
        xcenter 0.15
    show elena:
        xcenter 0.35
        xzoom -1.0
    with dissolve
    "Elena gave a curtly bow and Helena's frightened pale expression began to ease up slightly as she heard the wolf girl speak softly."
    ELENA @talk 'I am sorry to alarm you so...'
    ELENA @talk 'As you can see, this is why secrecy was so important.'
    'It was almost surprising how quickly Helena managed to recompose herself as she looked the wolf girl up and down.'
    HELENA @talk '...Yes, I see.'
    HELENA @talk '[player_name!t], might you give us a minute?'
    MC @talk 'Hm?'
    HELENA @smile 'Such talk would be easier had without you shadowing over us.'
    MC @talk 'Ah, very well... I shall leave you both to it.'
    'Reluctantly, I stepped outside of the room and waited.'
    $ LocFlush(dissolve)
    'As a few minutes passed, I began to grow impatient.'
    MC '(...Perhaps I should peer in and try listen to what they are saying?)'
    menu:
        'Peek through the door.':
            'Gently, I pushed open the door ever so slightly to peer in on the two girls as they spoke.'
            scene bg_weeping_heart_brothel_room
            show helena at cleft:
                zoom 0.8
                xoffset 50
                yoffset 100
            show elena at cright_f:
                zoom 0.78
                xoffset -50
                yoffset 100
            show cg_overlay_peeking onlayer characters
            with dissolve
            HELENA @sad 'It must have been difficult for you, having no mother in your life.'
            "Helena pulled a soft expression, one that seemed to understand Elena's pain in ways perhaps I could not."
            HELENA @sad "And I can't imagine it was too easy fitting in and making friends looking so different."
            ELENA @grumpy 'It was difficult, but I struggled through.'
            HELENA @sad 'As all woman must do.'
            ELENA @angry '...I was raised to be strong, to fight, to protect the lady Grace.'
            ELENA @angry "For years, I never even thought of myself as much of a person really, only an extension of her and the family's will."
            HELENA @sad 'You saw yourself as nothing but a tool.'
            ELENA @grumpy 'I am a tool, that is my purpose.'
            HELENA @sad '{i}You are a woman Elena.{/i}'
            HELENA @talk 'You are not a tool, you are a woman with her own mind and emotions.'
            ELENA @sad '...I feel dirty for wanting more.'
            ELENA @sad 'For wanting to be held and to...to...'
            HELENA @lewd '{i}To taste a man?{/i}'
            "Elena's cheeks burned brightly as her eyes dropped to the floor, unable to even lift them as she whispered her answer."
            ELENA @sad '{i}Yes...{/i}'
            HELENA @lewd 'You are not sullied or dirty for wanting these things Elena, to supress them for so long the way you have is unnatural.'
            ELENA @shock "But... Humans... I'm not-"
            HELENA @talk 'My first love was a dark elf.'
            HELENA @talk 'Gold eyes, almost like a cats.'
            ELENA @shock 'You loved a dark elf?'
            HELENA @talk 'Yes... We cannot help who we fall in love with or desire, Elena.'
            ELENA @talk 'What happened to him?'
            HELENA @sad "Oh, that's a story for another time."
            ELENA @talk "Mmm, alright then."
            'Helena motioned her head towards where I was, at the other side of the door.'
            HELENA @talk '{i}And him?{/i}'
            ELENA @shock 'W-What?'
            HELENA @talk 'Do you want him?'
            ELENA @lewd 'I...'
            ELENA @sad 'I doubt he wants me that way.'
            HELENA @smile 'How do you know? Have you asked him?'
            'Elena paused blushing, and Helena laughed in response.'
            HELENA @talk 'Do what you feel is right Elena, but nothing ventured is nothing gained.'
            HELENA @talk 'Do you understand now Elena?'
            ELENA @talk 'Yes, I think I understand.'
            HELENA @talk 'Now, do you think we should call him back in?'
            ELENA @talk 'Yes... Yes I think so.'
            $ LocFlush()
            with dissolve
            'I pulled away from the door just in time as Elena opened the door to let me inside.'
        'Wait patiently':
            "Deciding to respect their privacy, I waited patiently till the door opened and Elena appeared."
            #Both routes continued
    show elena with easeinright:
        xcenter 0.65
        xzoom -1.0
    ELENA @talk 'We are finished now.'
    hide elena with dissolve
    'I headed back into the room as both Elena and Helena smiled at me.'
    scene bg_weeping_heart_brothel_room
    show helena:
        xcenter 0.3
        zoom 0.9
        yoffset 30
    show elena:
        xcenter 0.6
        zoom 0.8
        yoffset 100
        xzoom -1.0
    with dissolve
    HELENA @talk 'You have quite the special lady [player_name!t], I trust you wil look after her well.'
    'Elena blushed at the comment, her tail swooshing from side to side slightly.'
    MC @talk 'Thank you for your help.'
    MC @smile "You've been... professional."
    HELENA @talk 'I always am.'
    HELENA @smile 'But if I may, I have something I wish to ask back.'
    ELENA @talk 'Hm?'
    HELENA @lewd2 'I have never been with one such as you Elena... I should like to kiss you if I can.'
    ELENA @shock 'K-Kiss me?!'
    'Elena turned to look towards me, cheeks burning red, unsure of what to do.'
    menu:
        'Do what you feel is right Elena.':
            'Elena turned towards Helena and nervously stepped closer.'
            'As she did so, Elena leaned forward for a kiss before Helena gently placed a finger over her lips to stop her.'
            HELENA @smile 'Is this your first kiss with a girl?'
            'Elena nodded.'
            HELENA @lewd 'Then let me make it more special.'

            scene black with dissolve
            $ CharSetClothes("helena", "ling")
            'Helena undid the laces on her dress and let it drop to the floor, revealing the white lingerie she wore beneath.'
            scene bg_weeping_heart_brothel_room
            show helena:
                xcenter 0.3
                zoom 0.9
                yoffset 30
            show elena:
                xcenter 0.55
                zoom 0.8
                yoffset 100
                xzoom -1.0
            with dissolve
            "Elena's eyes widened as she bit down on her lower lip, cheeks burning red."
            HELENA @talk 'Now, come closer...'
            scene black with dissolve
            show cg_elena_x_helena at sexy_flyby_upwards(-100):
                xcenter 0.5
            $ Pause()
            "Elena and Helena for a few moments shared a passionate kiss, their hands trailing over each other's bodies."
            #Elena/Helena makeout art
            "The two girls briefly groped at each other, running their hands over each other's breasts before moving down to squeeze their asses."
            "Helena pulled away, a silvery trail of saliva between their mouths disipating onto the floor as Elena let out a soft little moan."
            scene bg_weeping_heart_brothel_room
            show helena:
                xcenter 0.3
                zoom 0.9
                yoffset 30
            show elena:
                xcenter 0.55
                zoom 0.8
                yoffset 100
                xzoom -1.0
            with dissolve
            HELENA @joy "Thank you both for indulging me... Now if you'll excuse me, I must take my leave."
            show helena at alpha_out
            'Feverishly pleased, Helena put her green dress back on.'
            $ CharSetClothes("helena", "normal")
            show helena at alpha_in
            'She then graciously made her way back into the main hall as I moved to pick up a dreamy Elena.'
            hide helena with easeoutleft

            MC @talk 'Are you okay?'
            ELENA @lewd 'Y-Yes... Who knew girls could kiss so well.'
            MC @talk "Come, let's get you home."
        "I think she's got enough to think about as it is...":
            HELENA @talk 'Hm... Very well.'
            HELENA @talk 'I am glad to have assisted you both, I shall take my leave.'
            'Helena graciously made her way back into the main Hall as Elena moved beside me.'
            ELENA @talk 'Can we return back to your home now?'
            MC @talk 'Yes, of course, Elena.'
    $ CharSetClothes("elena", "normal")
    $ CharChangeRel("elena", 1)
    $ QstComplete(QstWomansTouch)
    $ LocEnter()
    