label scr_SharedInThorns_turnInClues:
    ELENA @talk "What have we uncovered so far?"
    menu scr_SharedInThorns_turnInClues_menu:
        'The book raised my suspicious about the Thornfalls being cursed' if 'book' in QstSharedInThorns().cluesCollected and 'book' not in QstSharedInThorns().cluesTurnedIn: #Note: IF CLUE BOOK available after clue 1 is investigated
            ELENA @grumpy 'Yes, I believe you may be correct.'
            MC @talk 'All four of his wives died under horrific circumstances during their pregnancies.'
            MC @talk 'Not to mention his sudden rise to fortune just before all the tragedy plagued his life...'
            MC @talk 'Very suspicious.'
            ELENA @shock "You don't think he made some kind of... 'deal' do you?"
            MC @talk 'As in witchery or demonic?'
            MC @talk "Well, you knew the late Lord Vront personally."
            MC @talk 'Do you believe he would be capable of doing such a thing?'
            'Elena quickly became uncomfortable.'
            ELENA @grumpy 'I do not know.'
            "Elena's face seemed to darken for a moment."
            ELENA @grumpy '{i}Trading the souls of your children for fortune... it... no....{/i}'
            ELENA @shock 'But what of the Lady Grace? Does she not disprove this?'
            MC @talk 'The lady Grace remains an enigma in this puzzle.'
            MC @talk 'But the fact her mother was so unknown itself raises more questions than answers.'
            ELENA @sad 'I... I see.'
            ELENA @talk 'We need to keep digging, there has to be more.'
            $ GoalComplete(QstSharedInThorns, 4)
            $ QstSharedInThorns().cluesTurnedIn.append("book")
            if not any(x in QstSharedInThorns().cluesCollected for x in QstSharedInThorns().cluesTurnedIn):
                jump scr_SharedInThorns_turnInClues_menu
            if len(QstSharedInThorns().cluesTurnedIn) == 3:
                $ GoalShow(QstSharedInThorns, 7)
                return
        "What do you know of the Lady Grace's expeditions in Ramon?" if 'trade' in QstSharedInThorns().cluesCollected and 'trade' not in QstSharedInThorns().cluesTurnedIn: #Note: IF CLUE TRADE Available after clue 2 is investigated
            ELENA @talk 'I was not privy to such information in my time at the Estate.'
            ELENA @talk '{i}Nor did I even know she had visited Ramon till now...{/i}'
            MC @talk 'Could she still be there now?'
            ELENA @grumpy "It's possible..."
            MC @talk 'Surely the lady Grace must have told you something?'
            ELENA @sad "We spoke of many things, but... She told me her work overseas was 'family business' and would elaborate no further."
            MC @talk 'Knowing her father visited Ramon some years before, there must be some correlation.'
            ELENA @talk 'I do not know, the late Lord Vronts years in Ramon were before my time, and he rarely spoke of them.'
            MC @talk 'And what of the murders?'
            ELENA @sad "W-We don't know for sure about that."
            MC @talk 'Do you think Lord Vront would be willing to silence people to protect his secrets?'
            ELENA @sad 'Perhaps Lord Vront but... The Lady Grace...'
            MC @talk 'Hmm, I see.'
            ELENA @talk 'We need to find more, we must keep searching for answers.'
            $ GoalComplete(QstSharedInThorns, 6)
            $ QstSharedInThorns().cluesTurnedIn.append('trade')
            if not any(x in QstSharedInThorns().cluesCollected for x in QstSharedInThorns().cluesTurnedIn):
                jump scr_SharedInThorns_turnInClues_menu
            if len(QstSharedInThorns().cluesTurnedIn) == 3:
                $ GoalShow(QstSharedInThorns, 7)
                return
        'What do you make of the soothsayers riddle?' if 'witch' in QstSharedInThorns().cluesCollected and 'witch' not in QstSharedInThorns().cluesTurnedIn: #Note: IF CLUE WITCH Available after clue 3 is investigated
            ELENA @angry 'The hag was simply toying with us.'
            MC @talk "I don't believe it so."
            ELENA @angry 'She has answers and withholds them! What more can be said?'
            MC @talk '{i}Come darkness falls, the toll is paid.{/i}'
            MC @talk "{i}Come morning light, their souls are saved.{/i}"
            MC @talk "Did you not mention that you were forbidden to leave your room at night?"
            ELENA @shock 'Y-Yes but-'
            MC @talk 'And the scratching at the door?'
            ELENA @sad 'You think the late Lord Vront... {i}was turning into a monster?{/i}'
            MC @talk 'Did he ever mention anything of this nature?'
            ELENA @angry 'No, of course not!'
            ELENA @sad 'He... He said I needed to stay in my room for protection, that the surrounding lands were too dangerous at night because of bandits.'
            MC @talk 'Elena...'
            ELENA @angry 'Enough of this speculation!'
            ELENA @grumpy "Let's... Let's just keep searching, shall we?"
            $ GoalComplete(QstSharedInThorns, 5)
            $ QstSharedInThorns().cluesTurnedIn.append("witch")
            if not any(x in QstSharedInThorns().cluesCollected for x in QstSharedInThorns().cluesTurnedIn):
                jump scr_SharedInThorns_turnInClues_menu
            if len(QstSharedInThorns().cluesTurnedIn) == 3:
                $ GoalShow(QstSharedInThorns, 7)
                return
        "That's all for now.":
            ELENA @talk "Very well, let's keep looking."
            $ LocEnter()