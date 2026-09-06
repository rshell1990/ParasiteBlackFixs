label scr_SharedInThorns_fin:
    ELENA @grumpy '...Curses... Dark deals... Strange temples and possible sacrifices.'
    'Elena became visibly upset.'
    ELENA @sad 'I could have... never imagined.'
    MC @talk "We don't have all the answers yet Elena, I'm sorry."
    ELENA @grumpy 'Yes... I do not believe I shall have my answers till I head to Ramon.'
    ELENA @talk 'Now I know where I must go... She {i}has{/i} to be there.'
    MC @talk 'Travelling to Ramon is not possible at the moment.'
    MC @talk 'The ports for the Free city are closed for now while they try clear the waters of Demorai ships.'
    MC @talk 'Only essential cargo ships are permitted through with military escorts.'
    ELENA @angry 'Then I will sneak on in my other form!'
    MC @talk "Elena, they won't just let a wolf onto the Cargo ships."
    MC @talk "If they catch you they'd probably just kill you."
    ELENA @grumpy 'No matter, I can hide well.'
    MC @talk 'And what when you arrive in Ramon even if you survive the journey? Alone and with no support or friends?'
    'Elena quickly grew frustrated, stomping around my room as she grinded her teeth.'
    ELENA @angry 'I made a vow to protect her!'
    ELENA @angry 'I will find a way!'
    MC @angry 'You are no good to the Lady Thornfall dead!'
    'Elena paused for a moment, taken aback as her rage gave way to fear.'
    ELENA @sad 'Then... what am I to do?'
    ELENA @sad 'The lady... She could be in danger as we speak.'
    MC @talk 'Stay with me for now, travel as my companion.'
    MC @talk 'When the time comes, I will help you find the lady in Ramon.'
    ELENA @shock 'You would travel with me?'
    MC @talk 'I will do what I can to help, I can promise no more than that.'
    ELENA @lewd '...Thank you.'
    ELENA @grumpy 'But why are you determined to help one such as I?'
    menu:
        'I need capable, trustworthy companions to support me when the time comes.':
            ELENA @talk 'Hm, yes, that does make sense.'
        'You needed help, so I gave it.':
            'Elena blushed at the remark.'
            ELENA @lewd 'O-Oh... Right.'
        'I need someone whose capable of defending themselves.':
            ELENA @grumpy 'Hmph... Fine.'
            ELENA @grumpy "But I'm not your assassin, remember that."
    ELENA @talk 'Very well [player_name!t], I agree to travel with you.'
    ELENA @talk 'For now at least... Till I have a chance to head to Ramon.'
    ELENA @talk 'I suppose I better get settled here then.'
    ELENA @talk 'Looks like I might be here for a while...'
    $ CharChangeRel("elena", 1)
    $ GoalComplete(QstSharedInThorns, 7)
    $ QstComplete(QstSharedInThorns)
    $ LocEnter()
