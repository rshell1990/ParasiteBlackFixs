label qst_DamzelDizzt_3_headToOffice:
    'Knocking on the iron door, a slider opened as two piercing eyes looked the other side.'
    
    THUG @talk 'Password?'
    menu:
        'Silver':
            'The slider closed, and I could hear the door unlock the other side before it swung open before us with the guard welcoming us in.'
            play sound "audio/interactables/wooden_door_open_1.ogg"
            jump qst_DamzelDizzt_3_enterOffice

        'Gold':
            THUG @talk "What? No that isn't-"
            THUG @talk "Gods! How does every moron keep forgetting the password?! It's one word!"
            THUG @talk 'You know what? Just... Just go away, and when you come back, try again, okay?'
            THUG @talk '{i}*Mutters*{/i} Fucking idiots.'
            $ LocEnterQ()

        'Tits and ass.':
            THUG @talk "...That wasn't even close!"
            THUG @talk 'Go away! Come back with the password before I run you through with my blade!'
            $ LocEnterQ()

label qst_DamzelDizzt_3_enterOffice:
    scene black with dissolve
    'Descending the stairs, we finally arrived into the small, unwelcoming office of Tarek, where he sat behind a small desk filed with gold and an ornate skull on it.'
    $ LocSet("novaras_black_diamond_office")
    $ LocFlush()
    $ GoalHide(QstDamzelInDiztrezz, 5)
    $ GoalHide(QstDamzelInDiztrezz, 6)
    show tarek at cright_f
    with dissolve
    show markus at left
    show mc at cleft
    show nijah at center_f
    with easeinleft
    'His eyes lit up and he grinned when he saw Nijah tailing behind us.'
    TAREK 'Nijah!'
    TAREK 'Iz so good to see you again!'
    NIJAH '... I cannot say zer same.'
    TAREK 'As fiery as always.'
    'Taking a moment to avert his gaze from her, his grin dropped as he sized up me and Markus.'
    TAREK 'Who are you two?'
    MC @talk 'I am Grimlock and this is Shire.'
    TAREK 'Well... Just what do you want Grimlock and Shire?'
    jump qst_DamzelDizzt_3_talkTarek
