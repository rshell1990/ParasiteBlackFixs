label ev_elena_drunk:
    show cg_elena_bottle with dissolve:
        xcenter 0.45
        xzoom -1.0
    ELENA @talk 'Mhmm! Heyyyy!'
    ELENA @talk 'I found zhis... {i}*Hiccup!*{/i} bottle of wine!'
    ELENA @talk 'Want some?'
    MC @talk 'Where did you find that?'
    ELENA @talk 'Mmm! Nowhereeeeee.'
    MC @talk 'Elena...'
    ELENA @talk 'I maybeeee jusht went out in my other form and grabbhed one!'
    MC @talk 'So you stole it?'
    ELENA @talk "...D-Don't be mad."
    ELENA @talk "They used to make me drink wine and stuff at home when I was learning to have 'proper manners' and sthuff."
    ELENA @talk 'I jhust thought it might remind me of home...'
    MC @talk 'And does it?'
    ELENA @talk 'N-Nuu!'
    ELENA @talk 'This wine-ish terrible!'
    MC @talk 'But you kept drinking it?'
    ELENA @talk "...MMMM-Maybe."
    ELENA @talk 'Whant sum?'
    menu:
        'Take a drink':
            'Grabbing a hold of the bottle, I took a gulp and was hit by a wave of bitterness.'
            MC @talk 'Urgh! This is bad.'
            ELENA @talk 'Seeeee?'
            ELENA @talk 'Told ya!'
        'Take the bottle away from her':
            MC @talk "I think you've had enough of that."
    hide cg_elena_bottle with dissolve
    show elena with dissolve:
        xcenter 0.45
        xzoom -1.0
    #both routes continued
    'Taking the bottle from her, I placed it off to the side and swept up Elena in my arms.'
    ELENA @lewd 'Huh?!'
    ELENA @lewd 'W-What are you doing?'
    MC @talk 'Putting you to bed.'
    "Elena's drunken face burned bright red at the comment."
    ELENA @lewd "{i}Y-You're taking me to bed?{/i}"
    'Gently, I rested Elena down onto my bed and placed the quilts over her as she looked up to me, still blushing with half asleep eyes.'
    MC @talk "Yes, I'm-"
    'Realizing what thoughts were racing through her mind, I hastily added.'
    MC @talk 'N-Not like that!'
    MC @talk "You're drunk... I'm just letting you sleep it off in comfort instead of-"
    "Elena's eyes were already closed before I finished my sentence, curled up into a ball on my bed, she slept softly."
    MC '...' #MC smiles
    $ QstSetProgress(EventElenaDrunk, 1)
    $ CharSetVar("elena", "hide", True)
    $ LocEnter()

label ev_elena_drunk_nextday:
    show elena with dissolve:
        xcenter 0.45
        xzoom -1.0
    ELENA @grumpy 'Urgh... My head.'
    MC @talk "Morning. How's your head?"
    ELENA @grumpy '{i}Sore.{/i}'
    ELENA @talk 'Umm, thank you.'
    ELENA @talk 'You know, for looking after me earlier.'
    ELENA @sad 'I made such a fool of myself.'
    menu:
        'You did not make a fool of yourself':
            ELENA @talk "You're just trying to make me feel better, aren't you?"
            MC @talk "You're allowed to enjoy yourself Elena."
            ELENA @grumpy 'Mmm... I should have had more control over myself.'
        'You did drink quite a bit...':
            ELENA @grumpy "Yes... I'm also paying the price for it right now."
            MC @talk 'Some water and food will fix you up.'
            ELENA @talk 'Ahh... Thanks.'
    $ CharSetVar("elena", "hide", False)
    $ QstComplete(EventElenaDrunk)
    $ LocEnter()
