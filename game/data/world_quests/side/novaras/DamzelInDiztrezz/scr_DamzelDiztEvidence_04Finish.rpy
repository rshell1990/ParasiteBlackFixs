label nijah_damzelDiztrezz_afterActionEvidence:
    #As MC and Markus/Nijah leave the Black Diamond
    $ LocSet("novaras_dist_pleasure")
    $ LocFlush()
    with dissolve
    show nijah at right_f with dissolve
    show markus at center_f with dissolve
    show mc at left with dissolve
    MARKUS 'Well... That went different than expected.'
    NIJAH @happy 'I did not think he would leave so peacefully!'
    MC @smile 'And yet, peacefully he has left.'
    MARKUS 'Why the sudden change in plan though?'
    MC @smile 'I work in mysterious ways!'
    MARKUS "{i}*Sigh*{/i} Do try involve us just a little more in these sudden 'ideas' you get."
    MC @talk 'Nijah, what will you do now?'
    NIJAH 'I... I iz not sure!'
    NIJAH "I need to think now what to do, I don't want to end up in the same situation again..."
    NIJAH "Will you visit me later?"
    NIJAH "Perhaps I will have better idea on what to do now..."
    MC @talk "Sure! I will visit you in a while."
    NIJAH 'Okay, until next time!'
    hide nijah with dissolve
    MARKUS @smile 'Well, sounds like my work here is done.'
    MC @smile 'Thank you Markus.'
    MARKUS @smile 'Anytime friend.'
    hide markus with dissolve
    hide mc with Dissolve(0.2)

    $ QstComplete(PrimerDamzelInDiztrezz)
    $ QstSetProgress(QstDamzelInDiztrezz, 4)
    $ QstComplete(QstDamzelInDiztrezz)
    $ QstComplete(EventNijahRescue)
    $ QstStart(HouseLockNijah)
    $ CharChangeRel("nijah", 1)
    $ NoteLock("NijahStayingAtMCs")
    $ NoteUnlock("NijahInvitedOver")
    $ QstStart(RomanceNijah)
    $ QstStart(HouseLockBlackDiamond)
    $ QstStart(BlackDiamondLogic)
    $ HouseLockBlackDiamond().canExit = True
    $ HouseLockBlackDiamond().canBeAccessed = True
    $ BlockWaitDynamic(False)
    $ LocEnter()
