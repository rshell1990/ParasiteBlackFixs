label rom_Ves_5_PostHunt:
    $ LocNameReset()
    "Several hours later of hauling pieces of meat back to Ves’ camp..."
    $ AutoMus(True)
    $ CharSetClothes("mc", "normal")
    $ LocFlush()
    show mc_transformed at cleft
    show ves at cright_f
    with dissolve
    MC '{i}*Huff* *Huff...*{/i}'
    MC @talk 'Okay, I think that’s enough.'
    MC '(I must have dragged back a cart full of stuff by now!)'
    VES @talk  'Well, I think I have enough food for a while!'
    VES @talk 'And we’ve brought a great deal of honour to my tribe for this great kill.'
    MC @talk 'Uhh... Yeah... I think I’m going to need a trip to a tavern after this...'
    MC @talk 'Or maybe a few trips.'
    VES @smile_talk 'That fight was incredible! I can’t wait to tell—'
    show ves sad
    'Ves stopped, her smile turning sombre as she realised there was no one else to tell of the great hunt she had partaken in.'
    MC @talk  '...Ves?'
    VES @sad_talk 'Hm? Oh, nothing.'
    VES @sad_talk 'It’s fine.'
    MC '...'
    $ QstComplete(QstValleyOfPrey)
    show ves smile
    'Ves perked up as best as she could and forced a smile.'
    VES @smile_talk '... You should probably wash yourself before heading back.'
    MC @talk 'Do I smell that bad?'
    VES @smile_talk 'Well, you were in that thing’s gut... You don’t smell great.'
    MC @talk 'But what about your water supplies?'
    MC @talk 'I can bathe back at home; you can’t waste water out here.'
    'Ves smiled and hauled over what seemed like a massive fur pouch covered in blood that reeked.'
    MC @talk 'U-Urgh! What is that?'
    'Cutting into the top of it, the fleshy bag had seeping out of it not blood but... water?'
    'Clear and fresh as day.'
    'Scooping up the small dripping stream in her hand, Ves took a sip.'
    VES @smile_talk 'It’s cool.'
    MC @talk '... Where did—'
    VES @talk  'The Skorn store their water inside these pouches in their bodies for consumption later.'
    VES @talk 'I snagged a couple of their pouches when I was making you haul the meat.'
    MC @talk 'I... Well, that’s kinda gross still but—'
    VES @talk 'It’s the desert... Beggars can’t be choosers.'
    MC @talk '... Point taken.'
    'A short while later Ves filled the small makeshift tub with the water from some of the Skorn’s fleshy pouches and smiled, waiting with her arms folded.'
    VES @smile_talk 'Here you go...'
    MC @talk 'Thanks.'
    VES '...'
    MC @talk '... Uh... If I transform back...'
    show ves
    'Ves frowned at me.'
    VES @surprised '...'
    MC @talk '... Well, you know... I won’t have any clothes on...'
    'Ves flushed red as she caught on to my meaning,'
    VES @talk 'U-Uh... Yes, of course, I shall leave you be.'
    hide ves with dissolve
    # MC TRANSFORMS.
    $ CharSetClothes("mc", "naked")
    hide mc_transformed
    show mc at cleft
    with dissolve
    'Stepping into the water I sighed with relief. It wasn’t cold like she said, but it was cool enough to be pleasant out here in the desert.'
    'My body ached from the intense battle earlier, despite the power coursing through the fingertips of my other form it was still all so new to me.'
    'Fighting came instinctively, and yet, like a new weapon in my hands for the first time, I felt so clumsy in my new body, like a child trying to learn how to walk...'
    'Except this time, I was learning to propel myself through the air while swinging towards my next target.'
    'A short while later, I heard the flap of the tent opening as Ves returned and stepped inside, seemingly more nervous than before.'
    $ PlaySoundRandom("tentFlap")
    'Leaning forward, I quickly moved to cover myself in embarrassment.'
    show ves at cright_f
    with easeinright
    MC @surprised 'Uh, Ves?'
    VES @talk  'How much longer are you going to be?'
    VES @talk 'I need to bathe in the water as well...'
    MC @talk 'You could join... To save water.'
    'Ves seemed taken aback by the comment, her green cheeks once again burning red.'
    VES @surp_talk 'Y-You...'
    VES @surprised 'You want me to—'
    MC @talk 'I mean, if you want to...'
    VES @surprised '... M-Males and females often bathe together in our tribes.'
    VES @surprised 'But...'
    VES @surprised  '{i}For a human to see me naked...{/i}'
    MC @talk  'It’s your choice, Ves.'
    MC @talk 'Just give me a few minutes to finish up and it’s all yours.'
    VES '...'
    'Ves pondered the thought for a moment, before she began to delicately take off the layers of her clothes until she stood naked before me.'
    $ CharSetClothes("ves", "naked")
    show ves at nod
    'Her green skin reflected eerily incandescent in the light as my eyes studied her body.'
    'The areolas around her nipples were dark, and as my eyes wandered down to the groomed bush nestled between her legs, I felt myself begin to throb with excitement.'
    'Nervously, Ves moved forward towards the tub and stepped inside, gently settling down between my legs.'
    play sound "audio/cfx/water_splash_bath.ogg"
    'Catching a good view of her round ass as she sat down, the parasite inside of me thrashed, desperately clawing beneath my skin with a burning desire to take her.'
    'Ves sighed as she leaned back, resting herself on my chest.'
    VES @talk  '... Your body is... strong.'
    MC @talk 'Strong? Is that a compliment I hear?'
    VES @talk 'Don’t get too used to it, human...'
    VES @talk 'Your head will get too big if I give you too many.'
    'As Ves sunk into the bath, her soft ass rubbed up against my hardening member.'
    'She must have noticed but, instead of reacting to it, she simply chose to ignore my hard-on pressing against her cheeks.'
    VES @talk  '... C-Can I ask you something?'
    MC @talk 'Uhh, yes...'
    'I added, struggling to contain my excitement.'
    VES @talk '... Do you...'
    VES @talk 'See me as a {i}friend{/i}?'
    MC @talk 'As a friend? Of course...'
    VES @talk 'N-No... You misunderstand.'
    VES @talk 'Am I a {i}friend{/i} or...'
    MC '...'
    VES @talk 'Do you see me as...'
    'Ves turned to look over her shoulder directly at me.'
    VES @talk '{i}More?{/i}'
    MC @talk 'Oh, you mean...'
    VES @talk '{i}Y-Your mate.{/i}'

    menu:
        '{image=[ICON.HEART]} Yes!': #(Romance route)
            $ CharChangeRel("ves", 1)
            $ CharSetLover("ves")
            pass

        '{image=[ICON.HEART_CROSS]} We should just stay friends...':
            'When she heard those words, Ves rose dejectedly out of the tub.'
            $ CharChangeRel("ves", -1)
            show ves at right_f
            with move
            MC @talk 'But... You just got in?'
            VES @sad_talk 'No... It is fine.'
            VES @talk 'I am glad we are good friends.'
            hide ves with dissolve
            'Her words were tinged with a sullenness, though she desperately tried to hide her disappointment as she climbed out, wrapping a towel around herself before retreating from the tent.'
            scene black with dissolve
            MC @talk '... Damn it.'
            $ TimeAdvBy(TIME_05H)
            $ CharSetClothes("ves", "normal")
            #EN. ALL ROMANCE SCENES END, PLAYER CAN JUST HAVE BASIC INTERACTIONS WITH VES @talk SHOULD THEY CHOOSE JUST TO BE FRIENDS.
            $ QstComplete(RomanceVes)
            $ LocSet("ves_camp")
            $ LocEnter()

    #Continued
    'My cock throbbed at the word and now forced and pressed itself between Ves’ legs, impossible to contain.'
    'Ves stared down at the hard member between her legs as it nestled beneath her pussy.'
    VES @talk '{i}*Heavy breathing*{/i}'
    MC @talk 'Ves, you’re... Sorry... It’s hard to keep...'
    VES @talk '... You like the idea of being my mate?'
    MC @talk '{i}*Huff*{/i} We d-don’t really call it that but—'
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x2.ogg",1)
    scene ves_bath with dissolve
    $ Pause()
    'Ves’ hands softly wrapped around my cock, gently and curiously feeling along the shaft, her breath heavy as she did so.'
    'As my cock rubbed up against her clit and soft bush, she shuddered slightly, biting her lower lip.'
    VES 'It’s... {i}very big...{/i}'
    MC '{i}*Huff*{/i} Ves... I want to...'
    'Ves added hastily, snapping out of her daydream.'
    VES 'Y-You can’t put it in me!'
    VES 'T-That’s too much...'
    MC 'Then what do you want to do?'
    "A soft sound escaped Ves’ lips, almost like a purr as her hands began to gently stroke my cock."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    VES @talk  'T-Touch me...'
    VES @talk  'I want to feel your hands on me.'
    scene ves_bath with dissolve
    $ Pause()
    'As my hands reached around, I gently fondled at her soft breasts, resting my thumb over her dark areola...'
    '...feeling the nipples harden as I lightly squeezed and twirled them between my finger and my thumb.'
    'My other hand glided past her soft stomach towards the smooth black bush.'
    'Ves moaned softly as my fingers rubbed against her clit before they softly pushed inside of her.'
    'Ves’ head rested back on my shoulder as her hands continued to stroke my cock.'
    'Finally, I stopped fondling at her breasts and reached up to raise her chin towards me and placed a soft kiss onto her lips.'
    'She seemed more taken by surprise at this than anything else, her eyes widened in shock before she slowly closed them and sunk into the kiss.'
    'As my tongue slipped into her mouth, I felt myself curiously pass by her fangs before her tongue met mine.'
    'She moaned softly, now gently trembling in my arms, Ves reluctantly pulled away from me, breathing heavily as she leaned her head forward.'
    MC @talk '... Ves'
    VES @talk 'I’m okay, just... {i}*Huff*{/i}'
    VES @talk 'I’ve not done anything like this before...'
    VES @talk 'And not with... {i}you know.{/i}'
    $ StopSexFx()
    $ UnlockGalSceneAndGrantXp("ves","bath")
    $ LocFlush()
    show mc:
        xcenter 0.3
    show ves:
        xcenter 0.7
    with dissolve
    'Nervously, Ves rose out of the bath, wrapping some robes around herself as she did so. When she noticed my hard-on she seemed almost disappointed in herself.'
    $ AutoMus(True)
    VES @sad_talk 'I...'
    VES @talk  'You can deal with that on your own?'
    'Disappointed, I nodded as Ves slipped away once again.'
    $ CharAddRelEntry("ves", "after_bath")
    hide ves with dissolve
    MC '(... Damn it.)'
    BLACK 'The female confuses me... Elevated heart rate and the pheromone release suggests she wanted to mate...'
    BLACK 'Why did she not?'
    MC '(Because it’s... It’s more complicated for her than just wanting to do it.)'
    BLACK '... This phrasing does not make sense to me.'
    MC '(I’m sure it doesn’t.)'
    BLACK 'How can one want something and not want it at the same time?'
    BLACK 'This is an inherent contradiction.'
    MC '(Welcome to emotions.)'
    scene black with dissolve
    $ CharSetClothes("mc", "normal")
    $ CharSetClothes("ves", "normal")
    'A short while later...'
    $ LocSet("ves_camp")
    $ LocFlush()
    show mc at cleft
    with dissolve
    MC '(I think Ves needs a little space...)'
    MC '(Maybe this is all going a little too fast for her.)'
    $ QstSetProgress(RomanceVes, 10)
    $ RomanceVes().cooldownDay = day + 1
    $ NoteUnlock("VesRomance3")
    $ LocEnter()
