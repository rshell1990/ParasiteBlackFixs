label dros_2_herbs_at_shop:
    #Player heads to the merchant - new buying option appears 'I need to buy these herbs...(Show list)'
    $ QstGracefulRebirth().spokeAboutHerbs = True
    LUCIUSMAL "Huh? What herbs do you have in mind?"
    "I handed over the list Sister Divine has thrown together."
    LUCIUSMAL '...Hmm, quite a curious list.'
    LUCIUSMAL 'Yes... I should be able to get a hold of it.'
    LUCIUSMAL "But it's going to take a couple days to arrive and..."
    'The Merchant grinned as he licked his lips.'
    LUCIUSMAL "Such an exotic list will be quite expensive of course."
    MC @talk "How much?"
    LUCIUSMAL "A thousand coins."
    menu:
        "Thats outrageous! Surely there must be a cheaper alternative!":
            $ QstGracefulRebirth().spokeAboutJurgen = True
            $ GoalShow(QstGracefulRebirth, 1.5)
            LUCIUSMAL "Friend, do you have any idea how exotic some of these herbs and plants are?"
            LUCIUSMAL "Not to mention the import tax from the plants that need to be shipped through."
            MC @talk "Is there nothing to be done?"
            LUCIUSMAL "Well... I would be willing to help you out."
            LUCIUSMAL "But it's not a job for 'clean' hands."
            MC @talk "What do you mean?"
            LUCIUSMAL "...There is a guard who goes by the name of Jurgen."
            LUCIUSMAL "He's become quite a nuisance with all his poking around the Merchants guild's business recently."
            LUCIUSMAL "You know the type, eager to carve out a name for himself and land himself a promotion."
            LUCIUSMAL "If he were to... {i}disappear?{/i}"
            LUCIUSMAL "I'm sure I could get you those herbs."
            menu:
                "I'm not an assassin... Nor a murderer.":
                    LUCIUSMAL "Who said anything about 'murder?' I don't care {i}how{/i} he's dealt with, only that he is."
                    LUCIUSMAL "But, the choice is yours... of course."
                    $ QstGracefulRebirth().jurgenActive = True
                    $ LocEnter()
                "Consider him gone, where is he?":
                    LUCIUSMAL "Whoah!"
                    LUCIUSMAL "Just to clarify, I don't care {i}how{/i} you deal with him, only that he no longer harrasses the Merchant's guild and by extent, my store."
                    LUCIUSMAL "He usually spends his time at the Iron Unicorn in the Evenings."
                    MC @talk "Got it."
                    MC "(Now that's a sidetrack.)"
                    $ QstGracefulRebirth().jurgenActive = True
                    $ LocEnter()
                "I'd need to think on it.":
                    LUCIUSMAL "Of course... Offer still stands."
                    $ QstGracefulRebirth().jurgenActive = True
                    $ LocEnter()
        "I will buy it." (Req_Gold = 1000): # cost
            LUCIUSMAL "Wonderful!"
            $ PlayerRemItem("gold", 1000)
            $ QstGracefulRebirth().boughtHerbs = True
            if QstGracefulRebirth().jurgenActive:
                $ QstGracefulRebirth().jurgenActive = False
            if not QstGracefulRebirth().jurgenGone:
                $ QstGracefulRebirth().jurgenGone = True
            if IsGoalVisible(QstGracefulRebirth, 1.5):
                $ GoalHide(QstGracefulRebirth, 1.5, Silent = True)
            LUCIUSMAL "The herbs will take a while to arrive... Come back in a couple days."
            $ LocEnter()
        "I cannot afford that.":
            LUCIUSMAL "Of course, I can always keep the order on standby, for when you are ready."
            $ LocEnter()

label dros_2_herbs_at_shop_revisit:
    LUCIUSMAL "Yeah, what's it gonna be?"
    LUCIUSMAL "Remember, a thousand coins."
    if not QstGracefulRebirth().spokeAboutJurgen:
        "Lucius leaned in with a cunning grin."
        LUCIUSMAL "Or, a personal service."
    menu:
        "A personal service?" if not QstGracefulRebirth().spokeAboutJurgen:
            $ QstGracefulRebirth().spokeAboutJurgen = True
            LUCIUSMAL "...There is a guard who goes by the name of Jurgen."
            LUCIUSMAL "He's become quite a nuisance with all his poking around the Merchants guild's business recently."
            LUCIUSMAL "You know the type, eager to carve out a name for himself and land himself a promotion."
            LUCIUSMAL "If he were to... {i}disappear?{/i}"
            LUCIUSMAL "I'm sure I could get you those herbs."
            $ GoalShow(QstGracefulRebirth, 1.5)
            menu:
                "I'm not an assassin... Nor a murderer.":
                    LUCIUSMAL "Who said anything about 'murder?' I don't care {i}how{/i} he's dealt with, only that he is."
                    LUCIUSMAL "But, the choice is yours... of course."
                    $ QstGracefulRebirth().jurgenActive = True
                    return
                "Consider him gone, where is he?":
                    LUCIUSMAL "Whoah!"
                    LUCIUSMAL "Just to clarify, I don't care {i}how{/i} you deal with him, only that he no longer harrasses the Merchant's guild and by extent, my store."
                    LUCIUSMAL "He usually spends his time at the Iron Unicorn in the Evenings."
                    MC @talk "Got it."
                    MC "(Now that's a sidetrack.)"
                    $ QstGracefulRebirth().jurgenActive = True
                    $ LocEnter()
                "I'd need to think on it.":
                    LUCIUSMAL "Of course... Offer still stands."
                    $ QstGracefulRebirth().jurgenActive = True
                    return
        "What was my other option again?" if not QstGracefulRebirth().boughtHerbs and QstGracefulRebirth().spokeAboutJurgen and not QstGracefulRebirth().jurgenGone:
            $ GoalShow(QstGracefulRebirth, 1.5)
            LUCIUSMAL "...There is a guard who goes by the name of Jurgen."
            LUCIUSMAL "He's become quite a nuisance with all his poking around the Merchants guild's business recently."
            LUCIUSMAL "You know the type, eager to carve out a name for himself and land himself a promotion."
            LUCIUSMAL "If he were to... {i}disappear?{/i}"
            LUCIUSMAL "I'm sure I could get you those herbs."
            LUCIUSMAL "Jurgen usually hangs out in the tavern."
            return
        "Jurgen's dealt with." if QstGracefulRebirth().jurgenGone and not QstGracefulRebirth().boughtHerbs:
            $ QstGracefulRebirth().boughtHerbs = True
            LUCIUSMAL "Yes... I heard."
            LUCIUSMAL "Well, a deal is a deal my friend."
            LUCIUSMAL "Come back in a couple days... I'll have what you want waiting for you then."
            $ LocEnter()
        "I'll just buy the herbs." (Req_Gold = 1000) if not QstGracefulRebirth().boughtHerbs: # if $
            $ PlayerRemItem("gold", 1000)
            $ QstGracefulRebirth().boughtHerbs = True
            if QstGracefulRebirth().jurgenActive:
                $ QstGracefulRebirth().jurgenActive = False
            if not QstGracefulRebirth().jurgenGone:
                $ QstGracefulRebirth().jurgenGone = True
            if IsGoalVisible(QstGracefulRebirth, 1.5):
                $ GoalHide(QstGracefulRebirth, 1.5, Silent = True)
            LUCIUSMAL "Wonderful!"
            LUCIUSMAL "The herbs will take a while to arrive... Come back in a couple days."
            $ LocEnter()
        "On second thought...":
            return

label dros_2_herbs_at_shop_waiting:
    LUCIUSMAL "Still waiting on the shipment."
    LUCIUSMAL "Come back another day, friend."
    return

label dros_2_herbs_at_shop_arrived:
    LUCIUSMAL "Yeah, the shipment just arrived this morning."
    $ PlayerAddItem("qst_rebirth_herbs")
    LUCIUSMAL "There you go."
    $ QstGracefulRebirth().gotHerbs = True
    $ GoalComplete(QstGracefulRebirth, 1)
    if IsGoalComplete(QstGracefulRebirth, 2) and IsGoalComplete(QstGracefulRebirth, 3):
        $ GoalShow(QstGracefulRebirth, 4)
    return