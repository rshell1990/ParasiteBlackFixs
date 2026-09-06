label nov_helena_firstmeet:
    show helena with dissolve:
        xcenter 0.3
    HELENA @talk 'Ahh, good evening sir.'
    HELENA @talk "How do you find yourself this Evening?"
    HELENA @smile "I am Helena, and yourself?"
    MC @talk 'A pleasure to meet you Helena, I am called [player_name!t].'
    HELENA @talk 'Hmm, your name sounds familiar...'
    HELENA @shock 'Wait, I know of you.'
    HELENA @talk 'You and your friend are the scouts who survived the recent expedition.'
    HELENA @lewd 'I see they did not exagerrate when they spoke of how handsome you are.'
    $ QstSetProgress(DialogueHelena, 1)
    call processDialogue("helena_root") from _call_processDialogue_30
    $ LocEnter()

label nov_helena_services:
    HELENA @talk "I am afraid my services aren't for you."
    MC @talk 'Wait, what?'
    HELENA @smile 'My clients are a small reserved of a certain social class.'
    HELENA @talk "Only a certain social class I'm afraid."
    MC @talk 'You mean aristocrats and nobles then?'
    HELENA @lewd2 "Not necessarily... I make special priced exceptions for men who have truly carved out a name for themselves."
    HELENA @smile 'Men who get tongues wagging when they see me speaking with them.'
    MC @talk 'Such as?'
    HELENA @smile 'I never kiss and tell.'
    HELENA @joy "But let's just say some adventurers who'd rather have their names kept a secret have come to me before."
    MC @talk 'Humor me, what are your normal prices.'
    HELENA @smile 'A night with me would cost you more than ten thousand coins.'
    'I felt the blood drain from my face.'
    MC @talk 'T-Ten... thousand?'
    MC @talk 'What about charging per act?'
    HELENA @talk "I'm afraid such a thing is far more becoming of a common whore than a courtesan."
    HELENA @talk "The clients a courtesan takes on expect us to be more reserved and discreit, our bodies not used by every passing traveler."
    HELENA @sad "Such a thing could ruin a courtesan's reputation should she behave like an ordinary lady of the night."
    HELENA @talk 'Thus, our companionship is sold for the whole evening... Partly to avoid too much scrutiny.'
    HELENA @smile 'And sometimes our clients simply want us to be a delight on their arms and make other lords and such jealous.'
    MC @talk 'Hmm, I see.'
    MC "(Unless I want to spend a small fortune on her, I'll need to build my reputation through adventuring and such before she offers me better rates for her 'sevices'.)"
    return

label nov_helena_about:
    HELENA @talk 'Hm? I prefer to keep my past to myself... I find men are more drawn to what they see as some alluring mystery.'
    HELENA @lewd2 'Perhaps one day I will tell you.'
    return

label nov_helena_bye:
    HELENA @talk "Speak soon."
    $ LocEnter()
