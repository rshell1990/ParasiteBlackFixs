label evscr_nijah_rescue_fleecity:
    MC @talk 'I think you should flee the city.'
    NIJAH 'You mean... Leave?'
    MC @talk 'Yes, get out of here before these thugs get to you one way or another.'
    NIJAH 'But I will need gold...'
    MC @talk "I'll help you with that."
    MC "(500 gold should suffice for her to leave safely)"
    menu:
        "Wait here, I'll go get it.":
            NIJAH 'I-I shall wait here.'
            $ LocEnter()

        "{image=[ICON.HEART_BROKE]} Here, take it." (Req_Gold = 500):
            $ PlayerRemItem("gold",500)
            'As Nijah took the coin, she seemed even more lost and confused than before:'
            NIJAH 'But where... Where will I go?'
            MC @talk 'I don’t know Nijah, head towards one of the villages but stay in the North.'
            MC @talk 'Do {i}not{/i} try crossing the Valley of Death to get to the the Free city.'
            'Dejected and defeated, Nijah leaned forward to hug me.'
            NIJAH 'Thank zu for saving me... {i}friend.{/i}'
            NIJAH 'I will pay zu back one day... If I can.'
            MC @talk '... Take some food and gold with you at least.'
            'As tears began to swell in her eyes, Nijah added pitifully:'
            $ CharChangeRel("nijah", 1)
            NIJAH 'You are the only Alderian to treat with kindness...'
            scene black with dissolve
            $ LocSet("novaras_dist_army")
            $ LocFlush()
            with dissolve
            'Placing the handful of gold I gave her in a small pouch with some food, Nijah tearfully waved as she headed off towards the city gate...'
            'No one would stop a refugee from wanting to leave.'
            'No one would enquire or care.'
            'I wondered if I’d made the right choice, but in the end... it was perhaps the most sensible.'
            'Maybe one day she’ll find a better life.'
            'Maybe one day we’ll cross paths again...'
            $ CharSetVar("nijah", "fledNovaras", True)
            $ QstComplete(EventNijahRescue)
            $ NoteLock("NijahStayingAtMCs")
            $ LocEnter()

        "To hells with you leaving! I've changed my mind!":
            NIJAH 'H-Huh?'
            NIJAH 'Then what are you going to do?'
            return
