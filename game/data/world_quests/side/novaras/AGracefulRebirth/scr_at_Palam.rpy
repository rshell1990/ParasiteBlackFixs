label dros_1_at_palam:
    #New dialogue choice speaking to Sister Divine 'Can you help me with Dros' problem...
    DIVINE 'Hm? Dros?'
    DIVINE 'You mean, the elven tailor?'
    'Sister Divine seemed to be increasingly uncomfortable with the subject.'
    $ GoalComplete(QstGracefulRebirth, 0)
    $ QstSetProgress(QstGracefulRebirth, 1)
    DIVINE 'What is it now he wants?'
    MC @talk 'He wants to become a woman.'
    DIVINE 'Impossible.'
    MC @talk 'But-'
    DIVINE "Such a thing is far beyond my abilities and powers."
    DIVINE "Perhaps a higher order being, a demon or one of the gods could offer such a thing... But it's not within reach of my powers."
    $ choicemenu = ['a']
    menu dros_1_at_palam_menu:
        "But the Mages of Palam... Aren't you-" if 'a' in choicemenu: # exhausted
            DIVINE "Only by the goddess Palam's will, we have no say ourselves over such matters."
            DIVINE "Nor are we entirely any specific gender."
            $ choicemenu.remove('a')
            jump dros_1_at_palam_menu
            # loops back
        "How could I contact such beings?":
            pass
            # continues below
    DIVINE "You cannot, the new gods come and go as they please and the rituals to summon the old gods to strike a bargain have been lost to most."
    DIVINE "As for demons, I would {i}highly{/i} recommend avoiding such foolish thoughts."
    DIVINE "If the inquisition doesn't execute you, no deal with a demon is ever worth the cost."
    MC @talk 'So is there nothing that could be done?'
    DIVINE "Well..."
    DIVINE "I cannot turn Dros into a woman, it's simply beyond my reach."
    DIVINE "{i}But, perhaps we could help at least with the appearance of being more like a woman.{/i}"
    MC @talk "Is such a thing possible?"
    DIVINE 'It may be so, when Dros first inquired about something similar I did some research into his request.'
    DIVINE "But I'm reluctant to try it, I have no idea if it would even work."
    DIVINE "Not to mention the risk of {i}side effects{/i} with any kind of untested spells like this."
    MC @talk "What do you need?"
    DIVINE "...You're serious?"
    DIVINE "Well, from what I remember of the incantation, I'd need some herbal ingredients..."
    $ GoalShow(QstGracefulRebirth, 1)
    DIVINE "Most merchants should be able to obtain them."
    DIVINE "I'd also need some slimelark remnants, at least five of them."
    $ GoalShow(QstGracefulRebirth, 2)
    $ WorldMapLocAdd("lake_balun")
    'Sister Divine scribbled down onto a piece of paper the list of all the ingredients as she spoke.'
    DIVINE "And finally... I'd need you to talk to Dros about whether he's sure about going through with this."
    $ GoalShow(QstGracefulRebirth, 3)
    DIVINE "He needs to understand the risk he's taking... I can't guarantee his safety."
    MC @talk "Hm, alright then..."
    hide divine with dissolve
    MC "(That's a handful.)"
    $ LocEnterQ()

label dros_3_returnToDivine:
    DIVINE "Yes? Did you do as I asked?"
    menu dros_3_returnToDivine_menu:
        "I have warned Dros." if QstGracefulRebirth().warnedDros and "dros" in QstGracefulRebirth().divinePointsList:
            $ QstGracefulRebirth().divinePointsList.remove("dros")
            DIVINE "Good. Anything else?"
            jump dros_3_returnToDivine_menu
        "I have brought slimelark remains." if PlayerItemQty("slimelark_remains") >= 5 and "remains" in QstGracefulRebirth().divinePointsList:
            $ QstGracefulRebirth().divinePointsList.remove("remains")
            $ PlayerRemItem("slimelark_remains", 5)
            $ GoalComplete(QstGracefulRebirth, 2)
            if IsGoalComplete(QstGracefulRebirth, 1) and IsGoalComplete(QstGracefulRebirth, 3):
                $ GoalShow(QstGracefulRebirth, 4)
            DIVINE "You do?"
            DIVINE "I can only imagine how you acquired these, {i}warrior{/i}."
            "Divine looked me over, biting her lip..."
            MC @talk "There you go."
            jump dros_3_returnToDivine_menu
        "I have brought the herbs." if PlayerItemQty("qst_rebirth_herbs") > 0 and "herbs" in QstGracefulRebirth().divinePointsList:
            $ QstGracefulRebirth().divinePointsList.remove("herbs")
            $ PlayerRemItem("qst_rebirth_herbs")
            DIVINE "Oh, perfect, these are..."
            DIVINE "Yes, ideal for our endeavour."
            DIVINE "Anything else?"
            jump dros_3_returnToDivine_menu
        "Let's begin the ritual." if len(QstGracefulRebirth().divinePointsList) == 0:
            DIVINE "Yes, everything's ready."
            if IsGoalVisible(QstGracefulRebirth, 4):
                $ GoalComplete(QstGracefulRebirth, 4)
            DIVINE "Go get Dros, I'll begin the preparations."
            $ QstSetProgress(QstGracefulRebirth, 2)
            $ GoalShow(QstGracefulRebirth, 5)
            $ LocEnter()
        "Let's talk about something else.":
            DIVINE "Okay, warrior."
            return