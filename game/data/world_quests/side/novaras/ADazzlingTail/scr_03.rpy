label qst_ADazzlingTail_03:
    # STAGE 3, we get our cut & the quest is complete
    $ CharSetClothes("arlena", "normal")
    show mc at cleft
    show arlena at cright_f
    with dissolve
    ARLENA 'There you are!'
    ARLENA 'Come here!'
    show arlena at center_f with easeinright
    'Leaping onto me, Arlena suddenly planted a kiss of jubilation onto my lips.'
    MC @talk 'Whoa! What was that for?'
    show arlena at cright_f with easeoutright
    ARLENA 'We’re going to be {b}rich!{/b}'
    MC @talk 'So, I take it that they went down well?'
    ARLENA 'So much better than expected! They’ve already placed an order for more of them!'
    MC @talk 'Really?'
    ARLENA 'Oh yes, here’s your cut by the way.'
    $ PlayerAddItem("gold", QstADazzlingTail().gemPay * 10)
    MC @talk 'Hey, that’s quite a heavy bag of gold!'
    ARLENA 'Told ya!'
    ARLENA 'When you’re free, bring me as many gems as you can so I can make some more...'
    MC @talk "I'll be right happy to!"
    hide arlena
    hide mc
    with dissolve
    return
