label dros_0_womanly_revisit:
    #"I'll help you become more 'womanly,' Dros.":
        # under his brothel dialogue lines
    DROS @talk 'You will?'
    DROS @talk 'I mean, uh... Thank you.'
    DROS @talk "I wasn't actually expecting you to-"
    DROS @talk "Never mind, the plan is straight forward actually."
    MC @talk 'Go on?'
    DROS @talk "The Mages of Palam seemed reluctant to help me, even after I offered generous payment."
    DROS @talk "I don't know why, but they HAVE to know something."
    DROS @talk "Speak to them and start there if you're serious about helping me."
    MC @talk "Alright, I'll look into it."
    jump startGracefulRebirth

label startGracefulRebirth:
    $ QstComplete(PrimerGracefulRebirth)
    $ QstStart(QstGracefulRebirth)
    $ GoalShow(QstGracefulRebirth, 0)
    $ LocEnter()