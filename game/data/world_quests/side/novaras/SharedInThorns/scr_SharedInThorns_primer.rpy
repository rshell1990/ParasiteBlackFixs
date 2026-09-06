
######### initial (primer) script
label scr_SharedInThorns_Initial:
    show elena at center_f with dissolve
    ELENA @talk "So, [player_name!t]..."
    MC "Yes?"
    ELENA @grumpy "Now that we've sorted some clothes for me, are you ready to help me find Lady Thornfall?"
    menu:
        "Yes, I'm ready.":
            jump scr_SharedInThorns_0
        'Not yet, I have other things I need to attend to first.':
            ELENA @talk 'Very well... Let me know when you are ready.'
            $ QstSetProgress(PrimerSharedInThorns, 1)
            $ LocEnter()

label scr_SharedInThorns_RepInit:
    ELENA @talk "So, are you ready to help me find Lady Thornfall?"
    menu:
        "Yes, I'm ready.":
            jump scr_SharedInThorns_0
        'Not yet, I have other things I need to attend to first.':
            ELENA @talk 'Very well... Let me know when you are ready.'
            $ LocEnter()

label scr_SharedInThorns_0:
    $ QstComplete(PrimerSharedInThorns)
    $ QstStart(QstSharedInThorns)
    ELENA @talk 'Good, where should we start?'
    $ GoalShow(QstSharedInThorns, 0)
    MC '(Hmmm...)'
    call processDialogue("elena_root") from _call_processDialogue_32
