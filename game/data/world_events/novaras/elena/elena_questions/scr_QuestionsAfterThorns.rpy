label scr_event_Elena_QuestionsAfterThorns:
    #Scene 14 - MC bedroom
    #Scene occurs a few days after completeting Elena's quest
    show elena with dissolve:
        xcenter 0.45
        xzoom -1.0
    ELENA @talk "I have a few questions if you don't mind me asking."
    MC @talk 'Questions?'
    ELENA @grumpy 'Yes, it occured to me just now that you already seem to know so much about me but I hardly know anything about you.'
    MC @talk 'Well, what do you wish to know?'
    ELENA @talk 'Were you in the army?'
    MC @talk '...Yes.'
    ELENA @talk 'And now you are not?'
    MC @talk 'No.'
    ELENA @talk 'What happened?'
    menu:
        '{i}*Recount the full story to Elena*{/i}':
            scene black with dissolve
            'Sometime later...'
            $ LocFlush()
            with dissolve
            show elena:
                xcenter 0.45
                xzoom -1.0
            ELENA @sad '...I see.'
            ELENA @sad 'That must have been horrible for you, seeing all your friends die like that.'
            MC @talk "It's war, everyone loses someone in the end."
            ELENA @sad 'But still-'
            MC @talk 'Do you have anything else you wish to ask?'
        "I'd rather not say...":
            ELENA @sad "I understand, should you wish to talk about it, I'm all ears."
            MC @talk 'Did you have something else you wished to ask?'
        "I slaughtered entire Demorai legions alone with one hand tied behind my back blind-folded, they decided it was no longer fair on the enemy to keep me on the battlefield.":
            ELENA @angry '...Uhuh.'
            ELENA @grumpy "Well when you're ready to talk seriously about it let me know."
            MC @talk 'Have anything else you want to ask?'
            ELENA @grumpy 'That depends, are you going to offer the same inane answers?'
            MC @talk "You won't know unless you ask!"
            $ EventElenaQuestions().sillyAnswers += 1
    #All choices continued
    ELENA @talk 'Where is your father to now?'
    menu:
        "He's an officer in the army.":
            ELENA @sad 'I see, and is he-'
            MC @talk "He's alive as far as we're aware."
            ELENA @talk "That's good, I am glad to hear it so."
        "He was the world's greatest lover, till he passed on his natural talents to me.":
            ELENA @grumpy 'Do you try use that line with all your prospective mates?'
            MC @talk 'Depends how drunk I am.'
            ELENA @grumpy 'Oh, of course, how did I suspect any different?'
            $ EventElenaQuestions().sillyAnswers += 1
    #Both choices continued
    MC @talk 'Is that all you wish to ask?'
    ELENA @talk 'Just one more for now...'
    ELENA @grumpy 'What do you {i}really{/i} want?'
    ELENA @talk 'I mean, I am helping you but-'
    ELENA @talk 'To what end?'
    menu:
        'I intend to end this war and protect the ones I love.':
            ELENA @grumpy 'Spoken like a true hero.'
            MC @talk 'Is there a problem with that?'
            ELENA @sad 'No... Just fairytale ending stories rarely seem to work out in this world.'
        'I intend to rule this fucking kingdom and crush the Demorai.':
            ELENA @grumpy 'Ambitious...'
            ELENA @grumpy 'Many a warlord has lived and died by the sword you know.'
            MC @talk 'I intend to be the one holding the sword.'
            ELENA @grumpy 'As do all conquerors.'
            MC @talk 'Are my goals a problem for you?'
            ELENA @grumpy 'No... As long as you help me find the Lady Grace, your goals are your own.'
        "I don't know really, I'm pretty much making it up as I go along.":
            ELENA @talk 'Somehow, I find that answer re-assuring.'
            MC @talk 'How so?'
            ELENA @talk 'Plans are dangerous things.'
            ELENA @smile "I'm happy that you're just following your heart, not some ill-thought out venture or scheme."
    #All routes continued
    ELENA @talk 'This... {i}creature{/i} that has attached itself to you.'
    ELENA @talk 'The reason I trusted you enough to leave with you.'
    ELENA @talk 'Does it commune with you?'
    menu:
        'Yes, it speaks to me.':
            ELENA @shock 'Really?'
            ELENA @talk 'What is it like?'
            MC @talk "It's different... It's like if a bug could speak to us."
            MC @talk "It doesn't seem to understand emotions or things quite like us."
            MC @talk "But I think it... {i}wants{/i} to learn."
            ELENA @talk 'Is it listening now? Does it hear every word we say?'
            BLACK '{i}Yes.{/i}'
            MC @talk 'Yes, it can hear us.'
            ELENA @grumpy "That must be... Strange."
            MC @talk "'Strange' doesn't even begin to cover it..."
        "Oh of course, I've actually been working on teaching it to sing you know?":
            ELENA @grumpy '...Is this another one of your poor jokes?'
            MC @talk "First, I'm teaching it a few tavern songs, then from there?"
            MC @talk "The sky's the limits."
            ELENA @angry "Anddd of course you didn't answer that one seriously, because why start now, right?"
            $ EventElenaQuestions().sillyAnswers += 1
    #All routes continued
    ELENA @talk 'Okay... I think I understand you a little more now.'
    if EventElenaQuestions().sillyAnswers >= 3:
        ELENA @talk 'Even if you did answer like a petulant child to some of my questions.'
        MC @talk "It's a talent being as charming as me sometimes."
    #end of special lines
    ELENA @talk 'Thank you for answering my questions.'
    $ QstComplete(EventElenaQuestions)
    $ LocEnter()
