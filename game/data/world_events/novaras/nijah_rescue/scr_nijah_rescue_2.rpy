label evscr_nijah_rescue_2:
    # IF PLAYER HAS PAID OFF, THREATENED, OR SLAYED THUGS
    $ LocFlush()
    show mc:
        xcenter 0.15
    show nijah:
        xcenter 0.65
        xzoom -1.0
    with dissolve
    'I turned towards the woman cowering on the floor. As I approached her, she raised her arm defensively in the air.'
    MC @talk 'It’s alright, I’m not going to hurt you.'

    UNKNOWN '...'
    UNKNOWN 'T-Thank you stranger.'
    $ CharChangeRel("nijah", 1)
    MC @talk 'Here, let me help you up.'
    'With my hand out-stretched, I reached out and held her soft hand as I gently pulled her back to her feet.'
    MC @talk 'Did they hurt you?'
    UNKNOWN 'No, I iz fine...'
    'As the woman unwrapped her headscarf to look at me, her eyes now settling from the panic fear.'
    #Version 1: Player has met Nijah before.
    if CharGetVar("nijah", "prologueMet") == True:
        'I immediately recognised who she was.'
        MC @talk "You... You're that woman I met at the pleasure district!"
        'The woman looked at me quizzically for a moment, not quite able to place my face.'
        MC @talk '... Nijah?'
        'Her eyes squinted towards me before recognition dawned on her face as well.'
        $ CharChangeRel("nijah", 1)
        NIJAH 'You... You were za boy...'
        NIJAH 'The one joining zer Scouts...'
        NIJAH '... You looks zerrrr...'
        NIJAH '{i}Different?{/i}'
        MC @talk 'Yeah, uh... it’s a long story.'
        MC @talk 'Listen, we can’t stay here, okay?'
        MC @talk 'Come with me.'
        'Holding out my hand once again, Nijah reached out to gently take it, still slightly shaking in fear.'
        'By hand, I led her out of the alleys and towards the main streets once again, away from what had just happened.'
        NIJAH 'Where are zu taking me?'
        MC @talk 'Somewhere safe we can talk...'
    #Version 2: Player has never met Nijah before.
    else:
        'The beautiful dark tanned beauty looked up to me, eyes bright as her lip quivered.'
        MC @talk "My name is [player_name!t]."
        UNKNOWN 'I... I am Nijah.'
        "Looking around to see the prying eyes watching from the windows, I knew it could quickly become dangerous here if we didn't leave soon."
        MC @talk "Well Nijah, I don't think it's safe to stay here."
        MC @talk 'You should come with me.'
        'Holding out my hand once again, Nijah reached out to gently take it, still slightly shaking in fear.'
        'By hand, I led her out of the alleys and towards the main streets once again, away from what had just happened.'
        $ CharMeet("nijah")
        NIJAH 'Where are zu taking me?'
        MC @talk 'Somewhere safe, away from here...'
    return
