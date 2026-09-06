label scr_ReadingMaterial_primer:
    show elena at center_f with dissolve
    ELENA @talk 'I have a favor to ask.'
    MC @talk 'Well hello to you too.'
    ELENA @talk 'I was hoping you could help me procure a book.'
    MC @talk 'A book?'
    ELENA @grumpy "Well, being stuck here for so long is going to become maddening if I don't find some way to occupy my mind."
    ELENA @talk 'My walks through Novaras are entertaining enough, but-'
    MC @talk 'Wait, are you sneaking out in the night?'
    ELENA @shock "I'm careful."
    MC @talk 'Elena-'
    ELENA @angry "Well I'm not staying caged here!"
    ELENA @grumpy "When we're not out doing something I'm... {i}bored.{/i}"
    MC @talk "{i}*Sigh*{/i} So you want a book to pass the time?"
    ELENA @talk 'If it would not trouble you, then yes.'
    MC @talk "What's the book?"
    #Elena blushes
    ELENA @lewd "I um, was hoping to grab a few..."
    MC @talk "Well if you don't tell me what it is-"
    ELENA @talk "It's fine, I'll just wander around in my wolf form and bring you what I find."
    MC @talk 'Must you make this so difficult?'
    ELENA @talk '...Will you do it?'
    MC @talk 'If we have time I will see what I can do.'
    ELENA @smile 'Thank you.'
    $ QstStart(QstReadingMaterial)
    $ QstComplete(PrimerReadingMaterial)
    $ LocEnter()

label scr_ReadingMaterial_1:
    #Scene 16 - Library
    #Scene auto plays upon entry
    show mc at left with easeinleft
    'As soon as we entered into the Library, Elena began to quickly move around the place, scanning across the isles of books.'
    'Had anyone other than a pre-occupied Vala been there, it would have raised more than a fair few eyebrows as Elena returned with book after book in her mouth.'
    'Gently planting them down in a stacked pile in front of me before finally, she sat down panting and stared at me.'
    show elena_w_book at cleft, walk_left_right with easeinleft
    MC @smile '...Have enough books then?'
    ELENA_W '{i}*Bark!*{/i}'
    MC @talk 'Thought so.'
    hide elena_w_book with dissolve
    'With the books in hand, I carried them over towards Vala whose eyes widened at the large pile.'
    show vala at cright_f with easeinright
    VALA @surp 'Oh my!'
    VALA @smile 'I never realized you were such an avid reader!'
    MC @talk "Uhh...What can I say? I'm just full of surprises."
    'As Vala scanned through the books, one of the books made her cheeks burn bright red.'
    VALA @surp '...Oh!'
    MC @talk 'What is it?'
    VALA @blush 'Um, I never figured you were into-'
    VALA '{i}*Cough*{/i} Never mind.'
    VALA "That will be one hundred coins to lend."
    menu:
        'Here you go' (Req_Gold = 100):
            $ PlayerRemItem('gold', 100)
            VALA 'Enjoy!'
            VALA @blush "Don't forget to umm... Tell me what you think when you're done."
            MC '(What is she talking about?)'
            $ LocSet("novaras_dist_edu")
            $ LocFlush()
            with dissolve
            show mc at left with easeinleft
            show elena_w at cleft with easeinleft
            MC @talk 'Happy now?'
            ELENA_W @bark '{i}*Bark!*{/i}'
            MC @talk "Alright... Then let's take these things home."
            $ QstSetProgress(QstReadingMaterial, 1)
            $ LocEnter()

        'Can you keep these books on hold for me?':
            VALA 'Of course! Just let me know when you have the coin!'
            $ QstReadingMaterial().valaRevisitFlag = True
            $ LocEnter()

label scr_ReadingMaterial_1_revisit:
    VALA "Ah, right. One hundred coins to lend."
    menu:
        'Here you go' (Req_Gold = 100):
            $ PlayerRemItem('gold', 100)
            VALA 'Enjoy!'
            VALA "Don't forget to umm... Tell me what you think when you're done."
            MC '(What is she talking about?)'
            $ LocSet("novaras_dist_edu")
            $ LocFlush()
            with dissolve
            show mc at left with easeinleft
            show elena_w at cleft with easeinleft
            MC @talk 'Happy now?'
            ELENA_W @bark '{i}*Bark!*{/i}'
            $ CharChangeRel("elena", 1)
            MC @talk "Alright... Then let's take these things home."
            $ QstSetProgress(QstReadingMaterial, 1)
            $ LocEnter()
        'Can you keep these books on hold for me?':
            VALA 'Of course! Just let me know when you have the coin!'
            $ LocEnter()

label scr_ReadingMaterial_2:
    scene black with dissolve
    'As we entered my room, Elena transformed out of a wolf form and began arranging the books into neat rows.'
    $ LocFlush()
    with dissolve
    show elena at center_f with dissolve
    ELENA @talk "Thanks, [player_name!t]!"
    MC @talk "Anytime, Elena."
    $ QstComplete(QstReadingMaterial)
    $ LocEnter()
