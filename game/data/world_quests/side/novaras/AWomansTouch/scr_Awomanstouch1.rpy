label scr_WomansTouch_1:
    #Scene 19 - Brothel INT - Night
    #Player selects on Helena
    #Elena questline
    HELENA @talk 'And what matter could I help you with?'
    MC @talk 'It is... a young maiden.'
    MC @talk 'Who wishes to speak with someone and understand her desires better.'
    'Helena raised an eyebrow at the comment.'
    HELENA @shock 'And her mother has not taught her these things?'
    MC @talk 'She has no mother, nor father.'
    MC @talk "I don't feel the words of a man are what she wants to hear."
    HELENA @sad 'I see... How tragic, but why me?'
    HELENA @talk 'Surely some other girl closer to you could speak to her.'
    MC @talk 'I believe in this case a stranger might be better...'
    MC @talk 'The situation is... {i}delicate{/i} and silent discretion is needed.'
    HELENA @smile "...A courtesan's silence is bound by coin."
    HELENA @talk "If the matter is as 'delicate' as you say it is, then my help is for a hundred coins at least."
    HELENA @talk 'And that is ONLY to consult with the girl, do not try pushing for anything else.'
    MC @talk 'I agree to your terms.'
    jump scr_WomansTouch_helenaMenu

label scr_WomansTouch_helenaMenu:
    HELENA @talk 'A hundred coins for my services it is.'
    menu:
        'Pay her' (Req_Gold = 100):
            $ PlayerRemItem("gold",100)
            HELENA @talk '...Very well, bring the girl to me.'
            MC @talk 'Is there a room or somewhere private we may go?'
            HELENA @talk 'This way...'
            jump scr_WomansTouch_2

        'Seems I am a little short...':
            HELENA @talk 'Return when you have the coin.'
            $ QstSetProgress(QstWomansTouch, 1)
            $ LocEnter()
        
