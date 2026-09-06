label scr_nijah_damzelDizztrezz_evidenceTalkLucius:
    LUCIUSMAL "Oh? And why do you want to know about them?"
    MC @talk 'How much do you know?'
    LUCIUSMAL "Enough to know their trouble."
    #MC @talk 'Do you know about Tarek and a place called the Black Diamond?'
    #LUCIUSMAL "Of course! I'm a merchant, not a bloody foreigner!"
    LUCIUSMAL "Now get on with telling me what you actually want, time is money and you're wasting mine."
    MC @talk "I'm looking for proof that one of the factions is going to betray Tarek... Any ideas?"
    LUCIUSMAL 'Perhaps... If my pockets were a little heavier by say, fifty coins...'
    menu:
        'Pay the man.' (Req_Gold = 50):
            $ PlayerRemItem('gold', 50)
            LUCIUSMAL "I heard a rumour that for the last few nights, they've been meeting up somewhere in the Market place at Night."
            LUCIUSMAL "No idea what its about, but if the Vulshan leadership is holding secret talks with the Khazahs, something is {i}definitely{/i} amiss."
            MC @talk '(Hmm... That sounds like a promising lead, I should definitely check it out.)'
            LUCIUSMAL 'Now, was there anything else?' #Loops back to default menu.
            $ QstSetProgress(QstDamzelInDiztrezz, 2)
            $ GoalComplete(QstDamzelInDiztrezz, 7)
            $ GoalShow(QstDamzelInDiztrezz, 8)
            return
        'You must be joking!':
            LUCIUSMAL 'Come back when your pockets are a little heavier, otherwise, I know nothing...'
            return
            #Quest update to explore the marketplace at night
            #A bandit appears in the marketplace - once player selects
