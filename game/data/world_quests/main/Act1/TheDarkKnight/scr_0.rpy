label qst_DarkKnight_0_startEvent:
    # Scene 3 - MC home living room
    # Regina approaches MC returning home
    show mc at center_f with dissolve
    show regina at left with easeinleft
    REGINA @talk 'Ah, [player_name!t], there you are.'
    MC @talk '[regina_ref_cap!t]? What is it?'
    REGINA @talk 'An Officer came by with some men today, Lukkan I think it was?'
    REGINA @talk "He brought a letter which I've left on your bed, says he has some urgent work for you to do."
    REGINA @talk 'Any idea what all this is about?'
    MC @talk 'No clue.'
    REGINA @talk "Hmm, well, hopefully it's nothing too dangerous dear..."
    menu:
        "Don't worry, I'll be careful.":
            REGINA @talk 'I know you will dear.'
            REGINA @talk "I know you can handle yourself, but that doesn't mean you're invincible."
            REGINA @talk "Take your time and prepare for something if you don't feel ready."
            # cont
        'Did he say anything else?':
            REGINA @talk "No, he just 'congratulated' me for raising one of the Scouts' finest and told me to give you that letter."
            MC @talk "I take it you didn't like him?"
            REGINA @talk "Hmph, not him but say... More I'd never trust anyone in the Alderian government."
            # cont
        'I am the danger.':
            '[regina_ref_cap!t] feigned a smile at the remark.'
            REGINA @talk 'Dear... You need to learn to use more than your fists to win every fight.'
            MC @talk "That's why I have my blade."
            REGINA @talk "That's not..."
            MC @talk "Don't worry [regina_ref!t], I know what you meant."
            #ALL Choices continued
    REGINA @talk 'Anyway, I shall leave you to it.'
    MC @talk 'Thanks [regina_ref!t].'
    hide regina with easeoutleft
    $ LocSet("mc_house_bedroom")
    $ LocFlush()
    show mc:
        xcenter 0.35
    with dissolve
    MC '(Hmm...)'
    MC '(The letter has the official seal on it, so it looks like it means business.)'
    MC "(Let's see...)"
    LUKKAN '[player_name!t], it has come to my attention that Captain Nyx of the City Watch is in dire need of some support tackling security issues inside and outside the Capital.'
    LUKKAN 'I have put forward your name for this endeavor, and request you speak to her as soon as possible - Head down to her office at the city fort.'
    LUKKAN 'Any work you do for her will be graciously rewarded.'
    MC "(Great... So much for all our worries being behind us.)"
    MC "(I should look into this as soon as I can... It's not wise to keep officials waiting.)"
    $ QstStart(QstDarkKnight)
    $ QstComplete(PrimerDarkKnight)
    $ LocEnter()