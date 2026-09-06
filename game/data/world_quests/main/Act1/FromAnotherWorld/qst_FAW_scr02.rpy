label qst_FromAnotherWorld_ReturnHome:
    $ LocSet("mc_house_kitchen")
    $ LocFlush()
    show regina at cleft
    with dissolve
    show mc at cright_f with easeinright
    $ AutoMus(True)
    'As I pushed open the door, I was instantly greeted by the wide-eyed, shocked look of Regina who rushed towards me, pulling me into an embrace so tight I struggled to breathe.'
    show regina at center with move
    REGINA @shock '{i}*Gasp!*{/i}'
    REGINA @shock_talk 'You’re home!'
    MC @talk 'Yes, everything is gonna be alright now.'
    MC @talk 'Both me and Markus are safe.'
    REGINA @shock_talk 'When they said you and Markus were the only survivors, I couldn’t believe it!'
    MC @talk 'Who told you?'
    REGINA @shock_talk 'Haven’t you heard the criers in the streets?'
    REGINA @shock_talk 'Your posters have been put up everywhere!'
    REGINA @shock_talk 'You’re basically famous!'
    REGINA @talk 'When I told them I thought it was you, they brought me in to identify you both.'
    MC @talk 'I’m sorry you had to see me like that.'
    REGINA @sad_talk 'It was better than not seeing you at all.'
    'Tears began to well in her eyes and she cupped my face with her warm hands before wrapping her arms around me for a second time, clinging to me for as long as I let her.'
    REGINA @smile_talk 'Gods be praised.'
    REGINA @smile_talk 'It’s a miracle you’re both alive.'
    $ tmpvar["faw_regina_talk_on_return"] = ["questions", "you_okay", "where_erika"]
    menu qst_FromAnotherWorld_ReturnHome_ReginaTalk:
        'Did they ask any unusual questions?' if 'questions' in tmpvar["faw_regina_talk_on_return"]:
            $ tmpvar["faw_regina_talk_on_return"].remove('questions')
            REGINA @talk 'I think they were suspicious that you and Markus had managed to survive through some sort of black magecraft.'
            REGINA @talk 'They searched your room but found nothing.'
            MC @talk 'What did you tell them?'
            REGINA @talk 'Just that you weren’t blessed with any kind of magecraft, let alone black.'
            REGINA @talk 'It’s on your school record either way, don’t know why they made such a fuss.'
            MC @talk '... I see.'
            REGINA @talk 'The investigation was brief, Erika helped ease things along without too much trouble.'
            jump qst_FromAnotherWorld_ReturnHome_ReginaTalk
        'Are you okay?' if 'you_okay' in tmpvar["faw_regina_talk_on_return"]:
            $ tmpvar["faw_regina_talk_on_return"].remove('you_okay')
            REGINA @talk 'I’m fine.'
            REGINA @talk 'Been worried sick about the pair of you ever since you left but other than that I’m okay.'
            MC @talk 'We made it back, that’s what matters.'
            jump qst_FromAnotherWorld_ReturnHome_ReginaTalk
        'Where is Erika?' if 'where_erika' in tmpvar["faw_regina_talk_on_return"]:
            $ tmpvar["faw_regina_talk_on_return"].remove('where_erika')
            REGINA @talk 'Busy dealing with her usual Inquisitor business... You know how she is, always busy.'
            MC @talk 'Did she visit me on the ward?'
            REGINA @talk 'I don’t know, but she came to see me to make sure I was coping alright.'
            MC @talk '... I’m sorry for putting you both through so much.'
            REGINA @angry_talk 'Don’t talk nonsense!'
            REGINA @talk 'We’re both just relieved you’re alive.'
            jump qst_FromAnotherWorld_ReturnHome_ReginaTalk
    $ tmpvar = {}
    'Regina pulled back to look at me properly, examining my new physique.'
    REGINA @shy_talk 'You... {i}You got taller.{/i}'
    MC @talk 'Uhh... yeah.'
    REGINA @shy_talk 'And, so much... um... {i}bigger.{/i}'
    MC @talk 'Y-Yes... The Scouts had us training rigorously... a lot.'
    'Regina raised a sceptical eyebrow, obviously not buying my excuse but letting it slide for now.'
    REGINA @talk 'What happened to you both out there?'
    MC @talk 'I...'
    MC @talk 'I don’t really know.'
    REGINA @talk 'Well, I’ve heard everything from you both stole horses and fought your way back like a pair of men possessed, riding day and night till you got home...'
    REGINA @talk 'To the spirit of Newheart himself helped guide you back.'
    MC @talk 'I can safely assure you that a ghost didn’t save us.'
    REGINA @talk 'Then what really happened out there?'
    REGINA @talk 'Nobody even knows what you were all doing so deep in Demorai lands.'
    REGINA @talk 'No one’s been sent that far in years, and for what reason?'
    MC @talk 'I don’t fully remember...'
    MC @talk 'We were brought in to investigate some old, abandoned fort and...'
    MC @talk '{i}There was an attack.{/i}'
    REGINA @talk'How did you survive?'
    MC @talk 'Me and Markus fled deeper into this cave...'
    MC @talk 'There was some type of laboratory inside and we managed to seal the door to it shut.'
    REGINA @shock_talk '... Laboratory?'
    REGINA @talk 'What happened next?'
    menu:
        'Tell the truth.':
            MC @talk 'There were... {i}these pillars{/i}.'
            MC @talk 'White and black marble things...'
            MC @talk 'When we touched them, something leapt onto us.'
            'Regina’s expression was unusually neutral as I told her what little I could remember.'
            MC @talk '... And that was it, we just woke up on the ward.'
            REGINA @talk '... Tell no one what you’ve just told me.'
            MC @talk 'What? But— '
            REGINA @angry_talk'Tell. No. One.'
            REGINA @talk 'People will think you were possessed by some dark spirit or something.'
            MC @talk 'But... {i}what if I was?{/i}'
            REGINA @talk 'Then be thankful that the spirit saved your life and keep your mouth shut.'
            REGINA @talk 'If it turns out that {i}was{/i} a spirit that’s attached itself to you and it’s dangerous, then I will deal with it.'
            MC @talk 'How are you going to do that?'
            REGINA @talk 'Don’t concern yourself with that.'
            REGINA @talk '{i}I have my ways.{/i}'
            MC @talk 'So... you just want me to be quiet in the meantime?'
            REGINA @talk 'We don’t understand what happened... Scaring people with no actual knowledge and a load of aggrandized speculation will just make matters worse.'
            REGINA @talk 'If you notice anything strange...'
            REGINA @talk 'Come to me and only me right away.'
            MC @talk '... There was... a voice last night...'
            REGINA @shock_talk 'What kind of voice?'
            MC @talk 'I think whatever it is... or {i}was{/i}... wanted to keep me safe.'
            REGINA @talk '... Hmm.'
            REGINA @talk 'I see.'
            MC @talk 'Do you think I should be worried? How serious is this?'
            REGINA @talk 'I think you should {i}keep quiet{/i} till we know more about what exactly it is we’re dealing with.'
            REGINA @talk '... But thank you for trusting me.'
            $ CharChangeRel("regina", 1)
        'Omit the truth.':
            MC @talk 'I can’t remember anything after that...'
            REGINA @talk 'Hmm... I see.'
            REGINA @talk 'Well, we best keep an eye on you for the next few days.'
            REGINA @talk 'But I’m glad you’re home safe, I’ve really missed you.'
    'Regina looked back to the brewing pot then snapped her fingers with realisation.'
    REGINA @shock_talk 'I didn’t buy enough food for two!'
    MC @talk '[regina_ref_cap!t], it’s no problem.'
    REGINA @talk 'No, wait here!'
    REGINA @talk 'I’ll come back with some more vegetables to make you a decent stew, it’s the least I can do.'
    MC @talk 'I’m meant to be meeting Mark—'
    REGINA @smile_talk 'I’ll be back in just a moment!'
    hide regina with easeoutright
    $ PlaySoundRandom("woodenDoor")
    'Before I could stop her, [regina_ref!t] was out of the door hurrying to buy some food.'
    MC @talk '{i}*Sigh*{/i}'
    scene black with dissolve
    $ LocSet("mc_house_bedroom")
    $ LocFlush(dissolve)
    show mc at cleft with easeinleft
    'Peering at the crack in the doorway to my bedroom, I ventured inside.'
    'The room was warm, but untouched since I had last been in it.'
    '[regina_ref_cap!t] had made sure to dust and make the bed, maintaining it for my improbable return.'
    "It was odd standing in it again."
    'It felt like it belonged to some different time from a world now far away that I was no longer a part of.'
    show mc at blurin, cright_f with easeoutright
    'All of mine and Markus’ nights of scheming unfolded here, often spent dreamily looking out towards the palace.'
    'It all seemed so simple back then... even in a world as chaotic as this one.'
    'Now, everything seems so uncertain, like we are charting a course into some terrible storm, unable to stop ourselves as we are pulled into the watery ravages of the dreaded Black Ocean.'
    show mc at blurin, cleft with easeoutleft
    'Both of us should have died that night at the fort, and a part of me {i}still feels like we did{/i}.'
    'Turning to look at the old, cracked mirror, I stared into it, hoping to invoke that strange voice from last night.'
    MC @talk '...Hello?'
    MC @talk 'Are you there? '
    MC @talk '{i}Spirit?{/i}'
    'Unsurprisingly, no answer came.'
    MC 'Hm...'
    'Heading over to my old bed, I flopped down onto it.'
    'The frame creaked, struggling more than ever to support me, but as I sunk into the softness of it, I sighed with relief.'
    'I hadn’t felt something so comfortable in months, the luxuriousness of it was almost like some distant memory.'
    scene black with Dissolve(1.0)
    'Closing my eyes for a moment, I felt...'
    $ AutoMus(False)
    $ AutoAmb(False)
    stop music fadeout 0.0
    stop ambience fadeout 0.0
    scene cg_kiaradeath with flash
    $ Pause(1.0)
    $ LocFlush()
    show mc at center_f
    'My eyes shot open as I sat upright, desperately gasping for air.'
    $ AutoAmb(True)
    $ AutoMus(True)
    MC @surprised '{i}... Fuck.{/i}'
    $ PlaySoundRandom("woodenDoor")
    "I heard the front door swing open once again to announce [regina_ref!t]'s return."
    REGINA @talk 'Are you still here?'
    MC @talk 'I’m just in my room.'
    'After listening out, a few moments later I heard some soft footsteps as the door crept open and [regina_ref!t] peeked inside.'
    show regina at left with easeinleft
    REGINA @talk 'Is everything okay, dear?'
    MC @talk 'I’m fine...'
    MC @talk 'It’s just...'
    MC @talk 'Strange being back here, is all.'
    'Regina gave me a sympathetic look as she nodded in some small understanding.'
    REGINA @sad_talk 'Come, I’m about to put the stew on for you.'
    MC @talk 'Alright...'
    MC @talk '... [regina_ref_cap!t]?'
    REGINA @talk 'Yes?'
    MC @talk 'Thank you, for everything.'
    'Regina smiled warmly, her eyes welling up ever so slightly before sliding out of the doorway back towards her cooking pot.'
    hide regina with easeoutleft
    scene black with dissolve
    $ LocSet("mc_house_kitchen")
    'A short while later, the homely food was served and I devoured every last scrap of it.'
    'We talked about many things, the good and the bad of my experiences with the Scouts, but I did my best to avoid discussing the fort and Duprey and Borras’ deaths.'
    'Regina informed me that Adara had visited nearly every day to find out if I’d written any letters home that she could read.'
    "I explained to [regina_ref!t] that I was a part of the Adventurers' guild now. It made her uncomfortable given that I had barely survived my trek with the Scouts..."
    '...But she didn’t let her displeasure be known through anything other than pursing her lips and going a little quiet.'
    'Finally, placing my bowl down onto the table, I rose from my seat.'
    $ LocFlush()
    show mc at cleft
    show regina at cright_f
    with dissolve
    MC @talk "I have to go meet Markus now, we’ve got to show up at the Adventurers' Guild."
    $ QstSetProgress(QstFromAnotherWorld, 1)
    REGINA @talk 'Will you be back later?'
    MC @talk 'Of course, though it might not be till quite a bit later...'
    MC @talk 'Do you need anything?'
    REGINA @talk 'Hmm... Well, if you’re offering...'
    REGINA @talk 'Could you pick up something for me from the Blacksmiths?'
    MC @talk 'What is it?'
    MC @talk '[regina_ref_cap!t] blushed as she spoke but waved off the question before I could ask any more.'
    REGINA @talk 'Nothing, just a little something for myself...'
    REGINA @talk 'It should be wrapped in a box, just tell them it’s for me.'
    MC @talk 'Sure.'
    $ QstStart(QstReginaPackage)
    MC @talk 'Well, I best get a move on.'
    REGINA @talk 'Okay, dear.'
    REGINA @talk 'Just... {i}be safe.{/i}'
    show mc at center with ease
    'As I was about to leave, I once again felt her press up against me.'
    "Slowly, [regina_ref!t]'s embrace lessened as she let me head off and finally make my way towards Markus' house."
    hide mc with easeoutright
    $ Pause(0.5)
    scene black with dissolve
    $ PlaySoundRandom("woodenDoor")
    jump qst_FromAnotherWorld_GoToMarkusHouse