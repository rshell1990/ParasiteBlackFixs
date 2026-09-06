init -1 python:
####### get/set progress
    def QstSetProgress(Quest, TargetProgress, Silent = False):
        if _in_replay:
            return
        _QstSubst(Quest).setProgress(TargetProgress, silent = Silent)
        return
    def QstGetProgress(Quest):
        return _QstSubst(Quest).progress

####### start/finish/fail
    def QstStart(Quest, Silent = False):
        if _in_replay:
            return
        VerboseLog_General = False
        if VerboseLog_General:
            print("Called QstStart for quest %s" % Quest)
            if QstIsOver(Quest):
                print("Warning: called QstStart for quest %s which is OVER" % Quest)
        _QstSubst(Quest).start(silent = Silent)
        return

    # only two outcomes, win or lose
    def QstComplete(Quest, Silent = False):
        _QstSubst(Quest).finish(silent = Silent)
        return
    def QstFail(Quest, Silent = False):
        _QstSubst(Quest).fail(silent = Silent)
        return

####### day delay set/get
    def QstSetDelay(Quest, Value):
        _QstSubst(Quest).delayEvent(Value)
        return
    def QstDelayCheck(Quest):
        return _QstSubst(Quest).delayCheck()
    def QstGetDelayVal(Quest):
        return _QstSubst(Quest).nextEventOnDay
    def QstSetDelayVal(Quest, Val):
        _QstSubst(Quest).nextEventOnDay = Val

####### is active/over/complete/failed
    def QstIsActive(Quest):
        return _QstSubst(Quest).isActive
    def QstIsOver(Quest):
        return _QstSubst(Quest).isOver
    def QstIsComplete(Quest):
        return _QstSubst(Quest).isComplete
    def QstIsFailed(Quest):
        return _QstSubst(Quest).isFailed

####### separate goal check if seen/completed/failed
    def IsGoalVisible(Quest, key):
        return _QstSubst(Quest).GetGoalState(key) == GoalState.VISIBLE
    def IsGoalComplete(Quest, key):        
        return _QstSubst(Quest).GetGoalState(key) == GoalState.COMPLETE
    def IsGoalFailed(Quest, key):
        return _QstSubst(Quest).GetGoalState(key) == GoalState.FAILED

####### separate goal show/hide/complete
    def GoalShow(Quest, GoalIndex, Silent = False):
        _QstSubst(Quest)._SetGoalState(GoalIndex, GoalState.VISIBLE, silent = Silent)
        return
    def GoalHide(Quest, GoalIndex, Silent = False):
        _QstSubst(Quest)._SetGoalState(GoalIndex, GoalState.HIDDEN, silent = Silent)
        return
    def GoalComplete(Quest, GoalIndex, Silent = False):
        _QstSubst(Quest)._SetGoalState(GoalIndex, GoalState.COMPLETE, silent = Silent)
        return
    def GoalFail(Quest, GoalIndex, Silent = False):
        _QstSubst(Quest)._SetGoalState(GoalIndex, GoalState.FAILED, silent = Silent)
        return

####### quests/active quests
    def GetAllQuests():
        return [QstObj for QstKey, QstObj in questObjs.items()]
    def GetAllGameQuests(): # "game quest" means only those shown to player that have visible stages and shit
        return [QstObj for QstObj in GetAllQuests() if not QstObj.HIDDEN]
    def GetAllActiveQuests():
        return [QstObj for QstObj in GetAllQuests() if QstObj.isActive]

############### internal
    # this exists to allow you to pass either instance (like '.self') or a type (like 'QstSomeQuest') to the front-facing functions
    def _QstSubst(Quest):
        if isinstance(Quest, type):
            return Quest()
        elif isinstance(Quest, BaseQuest):
            return Quest
    
    # created for trade screen this is more like utility, you shouldnt really do this kind of shit manually alot
    def QstGetByName(ClassName):
        return questObjs[ClassName]

    def MainLoop_GetTriggeredEvent(TriggerName):
        VerboseLog_General = False
        if VerboseLog_General:
            print("----------------")
            print("PlayerPos.goalTag %s" % PlayerPos.goalTag)
            print("PlayerPos.lastTag %s" % PlayerPos.lastTag)
            print("checking triggered events %s" % TriggerName)

        # Get triggered events for active quests
        FunctionName = "on%s" % TriggerName
        events = []
        for qstObj in GetAllActiveQuests():
            if (qstObj.MANUAL_DELAY or qstObj.delayCheck()):
                if hasattr(qstObj, FunctionName):
                    rv = getattr(qstObj, FunctionName)()
                    if rv is not None:
                        events.append(rv)
        if len(events) == 0:
            return []
        # Sort events by priority
        events = sorted(events, key=lambda x: x.priority, reverse = True)
        # return first one (no point handling list here tbh)
        if VerboseLog_General:
            print([event.label for event in events])
            print("----------------")
        return [events[0].label]

    def DEBUG_FinishAllQuests():
        for Qst in GetAllGameQuests():
            QstStart(Qst)
            QstComplete(Qst)
