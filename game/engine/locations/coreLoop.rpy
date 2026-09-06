default Story_NavLoop_PotentialEventLabels = []

# this is a label to keep from-clauses, basically for save compat to load ya into proper place
label ProcessLocEvent(EventTag):
    $ Story_NavLoop_PotentialEventLabels = MainLoop_GetTriggeredEvent(EventTag)
    if len(Story_NavLoop_PotentialEventLabels) == 0:
        return
    # this stuff is for waiting screen only, duct-tapey but better than what was
    #
    hide screen WaitClickToStop
    if GetBlockWaitDynamic() == True:
        $ BlockWaitDynamic(False)
    #
    call expression Story_NavLoop_PotentialEventLabels[0] from _call_expression_3
    return

label main_recheck:
    $ ForgetCallStack()
    # clear tmp scope, quite important
    $ tmpvar = {}

    # do exit event check
    # see if any on Exit events exist
    $ Story_NavLoop_PotentialEventLabels = MainLoop_GetTriggeredEvent("Exit")
    if len(Story_NavLoop_PotentialEventLabels) > 0:
        # "undo" movement attempt if any event is found
        $ PlayerPos.goalTag = PlayerPos.lastTag
        window auto
        # call the event label, AFTER processing it, jump to top of nav again
        call expression Story_NavLoop_PotentialEventLabels[0] from _call_main_triggerEvent
        jump main_recheck

    # no exit event happened, we might be moving out of this loc
    if PlayerPos.goalTag != PlayerPos.lastTag:
        if not FreezeAutoTime:
            # advance time
            $ TimeAdvBy(150)

        # finish movement to new location
        $ PlayerPos.lastTag = PlayerPos.goalTag
        # find *enter only* and *enter-reenter* events if any
        $ Story_NavLoop_PotentialEventLabels = MainLoop_GetTriggeredEvent("EnterOnce") + MainLoop_GetTriggeredEvent("Enter")
        # got event, process 0th one
        if len(Story_NavLoop_PotentialEventLabels) > 0:
            window auto  
            # while also showing location bg
            #$ BlockWaitDynamic(True)
            $ InLocTransition = True
            $ LocFlush(transition_move_between_locs)
            $ InLocTransition = False
            #$ BlockWaitDynamic(False)
            call expression Story_NavLoop_PotentialEventLabels[0] from _call_expression_4
            # event processed, jump to top of execution (coz it mightve changed state?)
            jump main_recheck
        # if no events fired but we're moving, we MIGHT BE auto-moving, so process it here: 
        # grab next location and go to root
        if len(autoMoveQ) > 0:
            $ LocSet(autoMoveQ.pop(0))
            jump main_recheck

    # now, if we're here we're not moving, were finally *just at* location
    # so we fire the generic "enter" event here
    $ Story_NavLoop_PotentialEventLabels = MainLoop_GetTriggeredEvent("Enter")

    # if it exists ofc
    if len(Story_NavLoop_PotentialEventLabels) > 0:
        window auto
        #$ BlockWaitDynamic(True)
        $ InLocTransition = True
        $ LocFlush(transition_move_between_locs)
        $ InLocTransition = False
        #$ BlockWaitDynamic(False)
        call expression Story_NavLoop_PotentialEventLabels[0] from _call_main_triggerEvent_1
        jump main_recheck

    # NOW if all the above did not trip us back to top, we show input interface, location clickables
    #$ BlockWaitDynamic(True)
    $ InLocTransition = True
    $ LocFlush()

    window hide

    if DEBUG_FastMode == False:
        with transition_move_between_locs
    # we fade them in *visually* first
    $ renpy.show_screen("loc_%s" % GetLocID(), _transient = True, _layer = "scene_objects")
    if DEBUG_FastMode == False:
        with Dissolve(0.15)
    $ InLocTransition = False
    #$ BlockWaitDynamic(False)
    # then we call same screen to actually read input
    $ btnTag = renpy.call_screen("loc_%s" % GetLocID(), _layer = "scene_objects")
    with None

    # after we have read input, we show static ui to allow fading it away
    $ renpy.show_screen("loc_%s" % GetLocID(), _transient = True, _layer = "scene_objects")
    with None

    # execute button player had selected
    #window auto
    $ PlayerPos.GetLoc().executeBtn(btnTag)
    #window hide

    # jump to top
    jump main_recheck

init python:
    # for convenience: same as checking len of gettrigevent manually
    def HaveEventsToProcess(EventTag):
        return (True if len(MainLoop_GetTriggeredEvent(EventTag)) > 0 else False)

    # make renpy forget parent contexts
    # Rather than carefully keeping track of how many nested "calls" we
    # have in different situations we make main-recheck a generic entry-point
    # for nav logic that forgets prior contexts (since we wont return to them)
    def ForgetCallStack():
        context = renpy.game.context()
        while len(context.return_stack) > 1:
            context.return_stack = context.return_stack[:-1]
            context.call_location_stack = context.call_location_stack[:-1]
            context.dynamic_stack = context.dynamic_stack[:-1]
        return