label rom_Ves_3_AfterHeat:
    show ves sad at cright_f
    with dissolve
    'I found Ves sat rather sombrely on a rock as she inspected the fang-toothed necklace she usually wore, gently running her fingers along it.'
    show mc at cleft 
    with easeinleft
    VES @sad_talk'... I didn’t think you’d come back.'
    MC @talk'I’m a glutton for punishment.'
    VES @sad_talk'... Do you know what this is?'
    'Ves dangled the necklace in front of me.'
    MC @talk'I take it it’s something important to you?'
    VES @sad_talk'I was smuggled away when I was just a baby by the other tribes.'
    VES @sad_talk'This is the only thing of my mother’s I have left.'
    MC sad'...'
    'Ves turned to look at me with sullen eyes.'
    VES @sad_talk'Both of my parents were slaves.'
    VES @sad_talk'After giving birth to me, my mother was beaten and raped by the master’s right-hand man, a man named Lavak... She died shortly afterwards.'
    VES @sad_talk'My father was killed when he tried to protect her.'
    MC @sad'... Ves.'
    VES @sad_talk'My tribe is all I have left, but the thought of {i}vengeance{/i} has kept me alive so far.'
    show mc
    menu:
        'Promise Ves her vengeance.':
            MC @talk'... There is no redeeming monsters like that.'
            MC @talk'What they did was... {i}unforgivable.{/i}'
            VES @sad'...'
            MC @talk'Ves, you will have your vengeance.'
            VES @talk'... How do you know?'
            MC @talk'{i}Because I’ll help you.{/i}'

        'Tell Ves she should seek justice, not vengeance.':
            MC @talk'... Vengeance won’t bring them back and it won’t heal the wounds left, Ves.'
            VES @sad'...'
            MC @talk'You have to be better than them... You’re not a cold-blooded killer.'
            VES @talk'What makes you so sure of that?'
            VES @talk'What makes you think I don’t intend to cut down THEIR women and children like they did to ours?'
            VES @talk'Like they did to MY family?'
            MC @talk'Because, Ves, I’ll help you bring them to justice... But I won’t help you become a monster yourself.'
            MC @talk'You need to be better than them.'
            VES @angry_talk'Why?'
            VES @angry_talk'There has been no justice for my people! Why must I be better than them? What have they done to deserve that?'
            VES @angry_talk'Why should I not just inflict on them the suffering they have inflicted on others? '
            MC @talk'Because, Ves, vengeance is a fleeting thing... As soon as you have it, it’s over.'
            MC @talk'Justice is meant to be more than that though.'
            MC @talk 'It’s about making them answer for their crimes and letting the world know the truth of what they did so that history cannot repeat itself.'
            VES @talk'... Hmph. I will think on your words.'
            MC @talk'I’m glad to hear that.'
            VES @talk'... You are a strange human.'
            MC '...'
            VES @talk'But I don’t think you’re a bad one.'
    show ves
    VES @talk'... You know you don’t have to help me with this, right?'
    VES @talk'I don’t even know when... {i}if{/i} I’ll ever get a chance to return to Skarshire again...'
    MC @talk'{i}When{/i} we do, Ves, I promise you you’ll get your chance...'
    'Ves stared awkwardly down at the sand before her wide, glassy eyes looked up to stare into mine.'
    show ves:
        xcenter 0.3
        xzoom -1.0
    with easeinright
    'Suddenly, without saying a word she lunged forward from her spot to hug me tightly.'
    'Gently, I wrapped my arms slowly around her, at the sudden affection before she shyly pulled back and looked at me again.'
    show ves:
        xcenter 0.5
        xzoom -1.0
    with easeoutright
    VES @talk'You... Most humans would have run away at the very sight of me.'
    VES @talk'Why did you not?'
    VES @talk'To be an orc is to be an ugly thing...'
    menu:
        'Ves... You are a {i}beautiful{/i} thing...':
            show ves:
                xcenter 0.55
                xzoom -1.0
            with easeoutright
            'Ves cheeks flushed red as my finger and thumb gently cupped under her chin. Nervously, she stepped back, her eyes darting towards the sand. '
            VES @talk'I... I have things I need to prepare for the next hunt! '
            VES @talk'Leave me! Come back another time!'
            hide ves with dissolve
            'I reached out to stop her, but Ves had already scarpered off into the tent, and seemingly wasn’t coming out again. '
        'It’s not my place to judge you.':
            VES @talk'I... I thank you.'
            VES @talk'gradually slipped out from my arms.'
            VES @talk'Perhaps... Just perhaps...'
            VES @talk'{i}Not all{/i} of you are bad.'
            hide ves with dissolve
            'Ves smiled, her eyes seeming to well up slightly as she solemnly dragged herself back into her tent.'
    $ CharChangeRel("ves", 1)
    $ RomanceVes().cooldownDay = GetGameDay() + 1
    $ QstSetProgress(RomanceVes, 7)
    $ NoteLock("VesRomance1")
    $ NoteUnlock("VesRomance2")
    $ LocEnter()
