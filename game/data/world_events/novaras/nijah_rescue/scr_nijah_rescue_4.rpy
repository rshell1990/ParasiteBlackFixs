label evscr_nijah_rescue_4:
    #Quest update: Speak to Nijah.
    #Player clicks on Nijah in his bedroom to progress
    show nijah:
        xcenter 0.45
        xzoom -1.0
    with dissolve
    'Nijah, who was sat anxiously on my bed with her hands clasped together shot to her feet when she saw me enter.'
    NIJAH 'Thank you for...'
    'Nijah pondered the phrase for a moment.'
    NIJAH '{i}Helping me.{/i}'
    MC @talk 'Who were those men after you?'
    NIJAH '...'
    MC @talk 'It’s alright, you can tell me.'
    NIJAH "Zey were Tarek's men..."
    MC @talk 'Who’s Tarek?'
    NIJAH '... Not your concern.'
    MC @talk 'Nijah...'
    NIJAH 'Iz not your business!'
    NIJAH 'I handle myself!'
    MC @talk 'Really? After what just happened?'
    NIJAH '...'
    'Nijah suddenly became very anxious again as she buried her face in her hands.'
    NIJAH 'I know not what to do...'
    NIJAH 'He iz cruel man, coin lender.'
    MC @talk 'What happened? Why are you borrowing money from lenders?'
    NIJAH 'No longer work at za District...'
    MC @talk 'Why?'
    NIJAH 'Guard demanded paperwork, iz not possible for people from Farah’Sand to have.'
    NIJAH 'Took my earnings... No longer afford room...'
    NIJAH 'Iz not fair!'
    MC '(Sounds like a shakedown.)'
    MC @talk 'I see...'
    MC @talk 'So, you went to Tarek to borrow coin in the meanwhile?'
    NIJAH 'Yis... While look for new work.'
    NIJAH 'But iz no good...'
    NIJAH 'No one want a Ramonian girl...'
    'Nijah added dejectedly.'
    MC @talk 'How much do you owe Tarek?'
    NIJAH 'Three thousand coins...'
    MC @talk 'Three thousand coins!? That’s absurd!'
    MC @talk 'How much did you borrow?'
    NIJAH 'Five hundred...'
    MC @talk 'That interest is ridiculous! How is anyone supposed to pay that back?'
    NIJAH 'They are not.'
    NIJAH 'Tarek and men only lend for Ramonians.'
    NIJAH 'Honest lenders no borrow to Ramonians, not citizens.'
    NIJAH 'So men like Tarek do what they want.'
    NIJAH 'They know many are desperate.'
    NIJAH 'Can raise interest as much az he likes...'
    NIJAH 'Iz no secret Tarek preys on the vulnerable.'
    NIJAH 'Most people from Farah’Sand cannot find work... Illegal for refugees...'
    NIJAH 'Only work allowed iz low paid or criminal...'
    NIJAH 'Why zo many women turn to {i}za District.{/i}'
    MC @talk 'Do you have somewhere to go?'
    NIJAH '...'
    'Nijah looked uncomfortable with the question.'
    if QstIsActive(QstBiteBark):
        if QstGetProgress(QstBiteBark) == 2 or QstGetProgress(QstBiteBark) == 3:
            NIJAH @smile 'Ooh!'
            NIJAH @smile 'Who iz this?'
            show elena_w with easeinright:
                xcenter 0.55
                xzoom -1.0
            ELENA 'Bark!'
            
            MC @talk "Oh, I haven't given her a name yet."
            MC @talk "She'll be joining me on quests and such from now on hopefully."
            'Nijah smiled as she reached down to pet the slightly stoic looking wolf before she trotted off without saying a word.'
            hide elena_w with easeoutleft
            MC @talk "Don't worry about her, she won't harm you."
    MC @talk 'Nijah... You have to be honest with me.'
    MC @talk "I can't help you if you aren't honest with me."
    'She shook her head despondently.'
    NIJAH 'Not while Tarek after me.'
    NIJAH 'Iz too dangerous to go home...'
    return
