
label ev_AdaraDream_KO_friendzone:
    scene black with dissolve
    $ AutoAmb(False)
    play ambience "audio/ambience_scenes/whispers.ogg" fadein 5.0
    "After finishing up my meal I was just about to head out into the city, when I felt my knees weaken."
    MC "What the..."
    "I muttered something to [regina_ref!t] as I headed towards my bedroom."
    $ LocSet("mc_house_bedroom")
    "Falling on my bed face-first I could not force myself to react as [regina_ref!t] followed me, her unnerved voice trying to reach out to me."
    REGINA "[player_name!t]?"
    REGINA "Are you alright?"
    "I felt... Alright?"
    "...As I drifted off {b}into the abyss{/b}."
    REGINA "[player_name!t]!"
    $ Pause(0.5)
    jump ev_AdaraDream


label ev_AdaraDream_KO_posttavern:
    $ LocNameSetTemp("")
    scene black with dissolve
    $ AutoAmb(False)
    play ambience "audio/ambience_scenes/whispers.ogg" fadein 5.0
    if GetLocID() == "novaras_tavern":
        "After leaving the Unicorn I suddenly felt knees weaken."
    else:
        "After parting my ways with Adara I suddenly felt knees weaken."
    MC "What the..."
    $ TimeAdvBy(TIME_1H)
    "A vertigo of familiar street corners, heat waves pulsing inside my skull, I found myself at home."
    "I muttered something to [regina_ref!t] as I headed towards my bedroom."
    $ LocNameReset()
    $ LocSet("mc_house_bedroom")
    "Falling on my bed face-first I could not force myself to react as [regina_ref!t] followed me, her unnerved voice trying to reach out to me."
    REGINA "[player_name!t]?"
    REGINA "Are you alright?"
    "I felt... Alright?"
    "...As I drifted off {b}into the abyss{/b}."
    REGINA "[player_name!t]!"
    $ Pause(0.5)
    jump ev_AdaraDream


label ev_AdaraDream:
    $ LocNameSetTemp(_("The Inner Nebula"))
    stop ambience fadeout 3.0
    $ AutoMus(False)
    $ PlayMusic("audio/music/22_Space_Odyssey.ogg")
    scene cg_space_hand1 with dissolve
    $ Pause()
    '...Laid before me, a great sea of darkness and splendour.'
    'A thousand or so stars seemed pin-pricked from the blanket of darkness, and some strange hypnotic swirling mass laid out in the distance, so far away, and yet, it all yet felt so close, as though it was all around me.'
    'I felt calmness wash over me, serene calmness. '
    'I couldn’t feel my feet touch the ground as I floated adrift in this sea of lights and blackness, reaching out towards those beautiful lights, almost as if I tried hard enough, I might just be able to reach one.'
    MC @talk'What is this place?'
    scene cg_space_hand2 with dissolve
    $ Pause()
    BLACK 'Memories...'
    MC @talk'Memories?'
    BLACK 'As our minds have melded, you now have access to my memories and dreams.'
    $ TimeAdvBy(TIME_1H)
    MC @talk'I thought you couldn’t remember much about the time before?'
    BLACK 'Like glass shattered... My memories are fractured but still there.'
    BLACK 'Buried deep.'
    MC @talk'...What is this place? Why do you remember this?'
    BLACK 'Across the stars we came...'
    BLACK 'Crashing down on worlds like some terrible wave.'
    MC @talk'...Are these memories? {i}Or dreams?{/i}'
    BLACK 'I do not know anymore...'
    $ TimeAdvBy(TIME_1H)
    BLACK 'But I dream of fire.'
    BLACK 'Fire scorching world to world as we move through the darkness of the cosmos.'
    BLACK 'With only one message prevailing... Chasing us as we move.'
    BLACK '{i}The hive must grow... The Hive must survive.{/i}'
    MC @talk'What? '
    BLACK 'With every blink, I see a world, a lifetime, memories of wars and strange things.'
    MC @talk'Your people... There was a war?'
    MC @talk'You’re not making any sense! '
    BLACK 'I cannot remember...'
    $ TimeAdvBy(TIME_1H)
    BLACK 'These memories are hazy, like trying to see clear through a storm.'
    BLACK '...But there’s a girl... A girl deep behind that storm.'
    BLACK 'I can’t remember her face, or her name...'
    BLACK 'But she’s there...'
    MC @talk'Who? What are you talking about?'
    BLACK '{i}Sleep...{/i} '
    BLACK '{i}Rest...{/i}'
    MC @talk'Wait! No! Don’t go!'
    scene black with dissolve
    $ TimeAdvTo(TIME_VISUAL_DAWN)
    $ LocNameReset()
    $ CharSetClothes("mc", "pants")
    $ LocFlush()
    show mc at cleft
    show adara shock at cright_f
    with dissolve
    'Springing up from my bed, sweat dripping off from me with wide eyed panic, I startled poor Adara who stumbled and nearly fell backwards from my abruptness. '
    stop music fadeout 1.0
    $ AutoMus(True)
    MC @talk'...!'
    $ renpy.music.play("audio/music/3_Novaras_L.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    ADARA @shock '[player_name!t]! Calm yourself! '
    MC @talk'Where am I? '
    ADARA @shock 'In your room!'
    MC @talk'I... I am?'
    show adara
    ADARA @talk 'You’ve been running a fever.'
    ADARA @talk 'Neither I nor Regina have been able to wake you.'
    show mc talk
    MC "[regina_ref_cap!t]... Where is she?"
    ADARA @talk 'Gone to fetch some herbs to help ease the fever.'
    'With a heavy sigh, I pressed my hands into my face.'
    'That was unlike any dream... {i}Memory...{/i} Whatever it was.'
    show adara at center_f
    with easeinright
    'Gently, I felt Adara’s hand rest onto me.'
    ADARA @talk 'You had me really worried there.'
    MC @talk'What are you doing here anyway?'
    ADARA @talk 'I came here to see how you are.'
    ADARA @talk "Regina said you've been like this for a while..."
    ADARA @talk "Thrashing around unconscious, muttering something about 'stars' and 'fire' or something."
    MC @talk'...'
    ADARA @talk '...Must have been one strange dream.'
    MC @talk'That’s one way to describe it...'
    'Anxiously, Adara sat beside me.'
    ADARA @talk 'Is it... Is it because of what happened?'
    MC @talk'...'
    ADARA @talk 'All that fighting... Seeing your friends get hurt?'
    MC @talk'...Yeah, it’s because of that.'
    'Adara reached around to hug me, she smelt good, and that familiar hazelnut scent was... {i}arousing.{/i}'
    ADARA @talk 'If there’s anything I can do to help.'
    ADARA @talk 'J-Just ask...'
    'Adara flushed red, and from where her hands clasped together they pushed out her large breasts which my eyes were naturally drawn to.'
    #VARIANT 1: -Not pursued any romance with Adara, just friendship'
    if QstProperReunion().friendZoned:
        ADARA @talk '...I should go.'
        ADARA @talk 'I will speak to you again soon.'
        MC @talk'I’ll walk you to the door.'
        ADARA @talk 'No need, just... get dressed and sort yourself out.'
        hide adara with easeoutright
        #EN. ADARA LEAVES'
        MC @talk'...'
        $ CharSetClothes("mc", "normal")
        $ LocEnter()

    ADARA @talk '...Your... {i}’thing’{/i} is standing to attention again.'
    'Looking down, I noticed my cock stood hard to attention, and once again the desire burned through me like some ferocious flame coursing it’s way up my veins.'
    BLACK "Breed... She's ours... {b}OURS.{/b}"

    MC @talk'I...'
    MC @talk'Adara, you should leave.'
    MC @talk'I’m... Not quite myself at the moment.'
    ADARA '...'
    'Adara paused and looked for a moment, her eyes staring at the member before her before she nervously began to slip off her dress.'
    MC @talk'Adara! What are you-'
    ADARA @talk 'Y-You really like my breasts, don’t you?'
    MC @talk'...'
    ADARA @talk 'You... You can use them if you want.'
    ADARA @talk 'I hear some men like that.'
    MC @talk'...! '
    $ CharSetClothes("adara", "naked")
    show adara at nod
    'As the dress slipped off Adara, my eyes stared at her round, large breasts and curvaceous body.'
    'She was always concerned about how she looked, always insecure.'
    'But when she saw my hard-on stand firm for her, I noticed the twinge of excitement between her legs while nipples hardened... She liked being desired, and she liked knowing it was me.'
    ADARA @talk 'D-Do... Do you want them?'
    menu:
        'Pull Adara onto the bed!':
            show mc at cleft with easeinleft
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            'Suddenly reaching out like a wild animal, I grabbed at Adara’s wrist and flung her onto the bed.'
            ADARA @talk '...! '
            ADARA @talk '[player_name!t]! '
            $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
            scene adara_titjob_loop with dissolve
            $ Pause()
            'Adara’s eyes were wide in shock, I could hear her heart racing as I pinned her down onto the bed, her soft warm skin now pressed against mine.'
            'Between heavy breathes I tore off my clothes and rested my cock between her tits, Adara looked away.'
            ADARA @talk 'It’s... It’s okay.'
            ADARA @talk 'This is what I’m here for, understand?'
            ADARA @talk 'Y-You can take it out on me, i-it’s okay...'
            'Unable to hold back any longer, my eyeballs burning as the animal like lust of the parasite coursed through my veins, I pressed her large breasts together and began to massage my cock with them.'
            ADARA @talk 'Ahh~ '
            ADARA @talk 'Y-Yes... Do they feel good for you?'
            #EN. MC’S DIALOGUE APPEARS LIKE THE PARASITES '
            MC_PARA @talk'I should have claimed you like this before...'
            ADARA @talk 'Y-You can claim me anytime you want! '
            ADARA @talk 'I-It’s okay! You have no idea how long I’ve wanted this! '
            MC_PARA @talk'You are mine...'
            ADARA @talk 'Y-Yes...! I’m a-all yours! {image=[ICON.HEART]}'
            ADARA @talk 'D-Don’t stop! '
            'Adara’s body felt electric, she was terrified but I could feel the excitement pulsing through her... How long I had denied her this.'
            BLACK 'This one... {i}Is goooood{/i}.'
            'Between her soft breasts I pushed together, I continued to pump my cock between them, listening out for her hot moans as she got off from being used by me.'
            'She was unable to truly look me in the eye for longer than a few seconds, whimpering and moaning with pleasure.'
            ADARA @talk 'It feels so... {i}so big{/i}! '
            ADARA @talk 'G-Give it to me...'
            ADARA @talk 'Give it to me please!'
            'Unable to hold on much longer, my hands squeezed roughly at Adara’s tits, making her cry out as my thumbs pressed over her hardened nipples. '
            ADARA @talk 'Mmmfghh!! {image=[ICON.HEART]}'
            scene adara_titjob_finish
            $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
            $ ReduceInfectionFromSex("adara")
            $ UnlockGalSceneAndGrantXp("adara", "titjob")
            with flash
            $ Pause()
            'Unable to hold back any longer, my body teetering on the edge of animalistic madness, I unleashed the first burst of my hot seed onto her, and then another, and another...'
            'Covering Adara in my thick seed, she moaned and writhed on the bed, whimpering hotly as she felt the hot fluid splash onto her.'
            'When I was finally finished, feeling the burning desire drain from me, I loosened my grip around her, and Adara, breathing heavily and in shock at what had just so suddenly happened, slowly opened her eyes to look up to me nervously.'
            ADARA @talk 'Was... Was that good for you?'
            'Pulling myself back from the bed, Adara rose to stand now freed from me.'
            $ CharReplaceRelEntry("adara", "summary_initial", "summary_post_titjob")
            scene bg_mc_house_bedroom
            show mc at left
            show adara at cleft_f
            with dissolve
            'My cum still dripped down from her face and breasts as she stood staring at me, somewhat unsure of what to say.'
            MC @talk'Adara... I-'
            ADARA @talk '{i}I liked it.{/i}'
            $ CharChangeRel("adara", 1)
            $ AutoMus(True)
            MC @talk'...'
            ADARA @talk 'Please... don’t...'
            ADARA @talk 'Don’t keep apologizing every time you use me like that.'
            MC @talk'...'
            ADARA @talk 'I like it...'
            MC @talk'...Adara, I’m not...'
            MC @talk'I’m not always able to control myself.'
            MC @talk'I don’t know if I’ll go too far.'
            ADARA @talk 'I don’t care...'
            MC @talk'...'
            ADARA @talk 'I want you to use me.'
            ADARA @talk 'So... Please stop apologizing.'
            ADARA @talk 'And just... {i}use me.{/i}'
            MC @talk'...'
            ADARA @talk 'Use me, instead of some other girl.'
            MC @talk'...If it was only that simple.'
            MC @talk'I don’t think this ‘thing’ is exactly satisfied with the idea of monogamy.'
            MC @talk'...Alright Adara, I’ll use you more often.'
            hide adara
            $ CharSetClothes("adara", "normal")
            show adara at cleft_f, nod
            'Adara smiled, and promptly after re-dressing herself, leaned forward to give me a kiss on the cheek.'
            #EN. REGINA ENTERS'
            show regina at center_f with easeinright
            REGINA @sad "Ah! [player_name!t]!"
            REGINA @sad 'I was so very-'
            REGINA @talk '...Adara?'
            ADARA @talk 'H-Hmm?'
            REGINA @lewd 'You have something on your face.'
            ADARA @talk '...O-Oh!'
            ADARA @talk 'Uhh, sorry! Just some food.'
            REGINA @lewd 'Tasty, was it?'
            $ CharSetVar("adara", "blush", True)
            ADARA @talk '{i}Very.{/i}'
            'Adara’s eyes widened as she blushed even harder at the comment, realizing what she had just said.'
            REGINA @talk '...Well, you best be heading home dear.'
            REGINA @talk 'I’ll handle things from here.'
            'Adara turned to me and smiled politely.'
            show adara smile
            ADARA @smile 'I will see you soon [player_name!t].'
            MC @talk'See you soon, Adara...'
            hide adara with easeoutright
            $ CharSetVar("adara", "blush", False)
            show regina smile
            'With that, Adara left, and [regina_ref!t] looked at me with a curious raised eyebrow and smirk.'
            MC @talk'...What?'
            REGINA @smile_talk 'I didn’t say anything.'
            MC @talk'You didn’t have to.'
            MC @talk'I know that look.'
            REGINA @smile_talk 'No comment.'
            'Regina smiled, throwing down some fresh clothes for me as she turned to close the door behind her again.'
            REGINA @smile_talk "Don’t stay in bed all day..."
            hide regina with easeoutright
            #EN. REGINA LEAVES'
            MC '{i}*Sigh...*{/i}'
        'No... Not like this!':
            'My whole body burned, enflamed with the desire to take her, thoughts protruding of violent rough sex while I claimed and ‘mated’ with her.'
            'But I understood these thoughts to come from the thing inside me, and as my sweaty hands coiled into a fist, I resisted.'
            MC @talk'A-Adara... Not that I don’t want this but-'
            ADARA @talk '...'
            MC @talk'You need to leave.'
            ADARA @talk '...O-Oh.'
            'I watched as Adara nervously re-dressed herself, her face a mixture of frustration and confusion.'
            $ CharSetClothes("adara", "normal")
            ADARA @talk 'Then... I shall leave you to it.'
            'As Adara made her way to the door, she stopped, turning to look back at me irritably.'
            ADARA @talk 'I don’t understand you.'
            MC @talk'...'
            ADARA @talk 'One minute you want me, the next you don’t.'
            ADARA @talk 'Just what do you want from me?'
            MC @talk'...'
            ADARA @talk '...Fine.'
            hide adara with easeoutright
            'With that, Adara left, closing the door angrily behind her.'
            MC @talk'{i}*Sigh*{/i}'
    $ CharSetClothes("mc", "normal")
    MC "(That dream though...)"
    $ LocEnter()
