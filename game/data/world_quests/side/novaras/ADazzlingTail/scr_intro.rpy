# this entire file is an intro dialogue, below you can find branching stuff
label qst_ADazzlingTail_intro:
    'Pulling out a small chest from under her bed, Arlena opened it to reveal small metal plug-like things inside.'
    MC @talk '... What are those things?'
    'Arlena fidgeted on the spot, licking her lips while she thought of what to say.'
    ARLENA 'Okay...'
    ARLENA 'I had this idea a while ago.'
    ARLENA 'Some of the girls down in the brothels were complaining about men who...'
    ARLENA '...You know.'
    MC @talk '... No, I don’t know.'
    ARLENA 'Tsch! Some of the men wanted to take them up the ass.'
    MC @talk 'Oh... OH!'
    ARLENA 'So, some of the girls were complaining that it hurt too much, even with lubricant.'
    ARLENA 'So... I came up with an idea...'
    ARLENA 'Maybe I could make something they could use that would have things uhh...'
    ARLENA 'A little ‘stretched’ back there.'
    MC @talk '... Is that safe?'
    ARLENA 'Of course, it’s safe! Wouldn’t be much bloody good if it wasn’t, would it?'
    ARLENA '... Thing is, they’ve kind of started to take off.'
    ARLENA 'I’ve had a few private requests from some of the ‘upstanding’ citizens.'
    MC @talk 'Really?'
    ARLENA 'Some of them were hoping to spice things up a bit in the bedroom, I guess...'
    ARLENA 'Anyway, thing is though, people also seem to want them a bit more stylish.'
    ARLENA 'Something nice to look at while they’re doing the deed, y’know...'
    MC @talk 'How so?'
    ARLENA 'Well, I’ve had this idea...'
    ARLENA 'If you can get some crude gems...'
    ARLENA 'Practically worthless but shiny.'
    ARLENA 'I could perhaps insert them into the ends of these things, and they should look more... uhh... ‘stylish’.'
    MC @talk 'Where do I find these gems?'
    ARLENA 'You should be able to find some in the Valley of Death, usually in some of the black rocks if you search...'
    ARLENA 'Or you may be able to just buy some from someone who works in the mines if you know anyone...'
    MC @talk 'What’s in it for me?'
    ARLENA 'I’ll give you a cut of the profits, say fifteen percent?'
    # choice to go or not to go
    menu:
        "Count me in!":
            ARLENA "Good boy."
            $ QstStart(QstADazzlingTail)
            $ QstSetProgress(QstADazzlingTail, 1)
            $ NoteLock("ArlenaADazzTailQuest")
            MC @talk '...Thirty-five.'
            ARLENA 'Thirty.'
            MC @talk 'I’m the one to do all the gem hunting!'
            MC @talk 'All alone in the Valley of Death...'
            ARLENA 'And I’m the one who has to hammer these things into being!'
            menu:
                'You need me just as much as I need you.' (Req_Charm = 7):
                    ARLENA '... Fine, thirty-five.'
                    ARLENA 'But no more than that, I want to make something out of this, too.'
                    $ QstADazzlingTail().gemPay = 35
                'Alright, thirty it is.':
                    $ QstADazzlingTail().gemPay = 30
            ARLENA 'Come back when you have the gems. '
            MC @talk 'Okay... I’ll see what I can do.'
            hide arlena with dissolve
            $ LocSet("novaras_dist_farm")
            $ LocEnter()

        "I'll have to pass right now because... reasons.":
            # refusing once will change the lines she says
            $ QstADazzlingTail().askedOnce = True
            ARLENA @angry "Reasons?!"
            ARLENA @angry "You wanna get smashed with a seating appliance again?"
            MC "Appl- Wha? No!"
            ARLENA @angry "Stop wasting my time!"
            ARLENA "Come back if you change your mind though!"
            hide arlena with dissolve
            $ NoteUnlock("ArlenaADazzTailQuest")
            $ LocEnter()
    return

# this is what the player sees if he revisits arlena & asks about the quest
label qst_ADazzlingTail_intro2:
    ARLENA "Changed your mind, eh?"
    ARLENA "A pervert such as you sure can't allow ladies wander about without some fancy... bijouterie."
    call qst_ADazzlingTail_intro2_choice from _call_qst_ADazzlingTail_intro2_choice

label qst_ADazzlingTail_intro2_choice:
    menu:
        "I'm in.":
            ARLENA "Finally, serious talk."
            ARLENA "Bring me, let's say... 20 gems."
            ARLENA "Should suffice for a batch."
            MC "Oh, I'll go get some in no time!"
            ARLENA "And [player_name!t]..."
            "Arlena stumbled for a second."
            ARLENA "Return in one piece, alright?"
            ARLENA "I know you won't just go mine some."
            ARLENA "And... I really need that project to take off."
            MC "Of course, you'll have your diamonds, my princess."
            ARLENA "*sigh* Off you go!"
            $ QstStart(QstADazzlingTail)
            $ QstSetProgress(QstADazzlingTail, 1)
            $ NoteLock("ArlenaADazzTailQuest")
            $ LocSet("novaras_dist_farm")
            $ LocEnter()

        "What was the job again?":
            "Arlena mustered herself against my ignorance."
            ARLENA "Gems!"
            MC "Ah, right."
            ARLENA "I wanna give this city some exquisite... accessories."
            ARLENA "The kind a fine woman puts up her ass."
            MC "*cough*"
            ARLENA "...Either to stretch a bit, or to look fancy doing... whatever it is they do."
            ARLENA "So, what do you say?"
            return
