label divine_ves_med:
    DIVINE 'Oh? What kind of medicine do you seek, child?'
    MC 'The general kind, anything to treat wounds or afflictions common to the Valley of Death.'
    DIVINE 'The Valley of Death, you say? '
    MC 'I do a lot of travelling through there... Some emergency supplies would be of great use.'
    "Sister Divine pondered the thought for a moment."
    DIVINE 'Hmm, yes...'
    DIVINE 'I could cobble together a list of some of the essentials for you.'
    $ QstSetProgress(QstGreenFever, 1)
    DIVINE "But it won’t be for free."
    DIVINE "A hundred coins."
    menu divine_ves_med_menu:
        'There you go.' (Req_Gold = 100) if QstGreenFever().NegotiatedCheaperPrice == False:
            $ PlayerRemItem("gold", 100)
            call divine_ves_med_get from _call_divine_ves_med_get
        'There you go.' (Req_Gold = 70) if QstGreenFever().NegotiatedCheaperPrice == True:
            $ PlayerRemItem("gold", 70)
            call divine_ves_med_get from _call_divine_ves_med_get_1
        'Is there no way I can get it at a more generous rate?' (Req_Barter = 9) if QstGreenFever().NegotiatedCheaperPrice == False:
            $ QstGreenFever().NegotiatedCheaperPrice = True
            'Sister Divine blushed for a moment, whatever thought passing through her head as she bit at her lower lip. '
            DIVINE 'Well... Our goddess is a magnanimous one after all...'
            DIVINE 'Perhaps this one time I could mercifully offer a discount.'
            MC 'You’re too kind...'
            jump divine_ves_med_menu
        'On second thought...':
            DIVINE 'I’ll be waiting should you change your mind.'
            $ QstSetProgress(QstGreenFever, 1)
    $ LocEnter()

label divine_ves_med_get:
    DIVINE 'One moment, please...'
    scene black
    with dissolve
    $ Pause(1.0)
    'Sister Divine left for a short while, returning with basket in hand filled with assorted medicines in various bottles.'
    $ LocFlush()
    show divine at center
    with dissolve
    DIVINE 'My apologies for keeping you waiting...'
    $ PlayerAddItem("qst_green_fever_meds")
    DIVINE 'Here you go... This should cover everything you need out there, or at least, the most common ailments that plague those who frequent the barren lands.'
    DIVINE 'Come back if you need to restock.'
    MC @talk "Thanks."
    MC "(Now, to Ves' camp)"
    $ QstSetProgress(QstGreenFever, 2)
    return


label divine_ves_med_revisit:
    DIVINE "Ah, a hundred coins and it's yours, child."
    jump divine_ves_med_menu
