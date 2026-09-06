# this is incremented once each time you finish() a real quest, 
# used only for sorting in journal
# (we get order of completion that way)
default QuestsFinished = 0

init -2 python:
    # this enables QstClass() syntax, its like the . o b j ( ) we had before
    # try to only use it for variable access, like somequest().somevar
    class SingletonQuestMeta(type):
        def __call__(cls, *args, **kwargs):
            Instances = getattr(store, "questObjs", None)
            if Instances is not None:
                if cls.__name__ in Instances:
                    return Instances[cls.__name__]
                else:
                    Instances[cls.__name__] = super(SingletonQuestMeta, cls).__call__(*args, **kwargs)
                    return Instances[cls.__name__]

    # REFERENCE FOR COMPLETION BOOLS
    # isActive      - the quest has been .start()ed, or was active at init. 'is currently running'
    # isComplete    - the quest isOver and was .finish()ed
    # isFailed      - the quest isOver and was .fail()ed
    # isOver        - the quest has been either .finish()ed or .fail()ed, not active anymore regardless the outcome
    class BaseQuest(metaclass = SingletonQuestMeta): # <- this allows to access vars with Class().Var
        GOALS = {}
        TITLE = "<default title>"
        DESCRIPTION = "<default description>"
        START_PROGRESS = 0
        HIDDEN = False

        # If False, no events can trigger during event-delay period. If True Quest needs to do it's own delay checks
        MANUAL_DELAY = False

        # If True, goals/quest-stages are strictly linear and tied to the progress variable
        #     progress = x => All goals with a key < x are marked "complete", goal with key 'x' is marked "visible"
        # If False, goal-states are set manually
        SIMPLE_GOALS = True

        def __init__(self):
            self.priority = 0
            self.progress = -999

            self.XpReward = 250 # base. override per-quest. 0 is same as None

            self.isActive = False
            self.isOver = False
            self.isFailed = False
            self.isComplete = False

            self.isTracked = True
            self.GoalStates = {}
            self.nextEventOnDay = 0 # Similar to progress, not hardcoded to do anything

            self.suggestedLevel = 0

            self.IsMain = False     # just informs player whether its a main/side gig
            self.FinishOrder = 0    # for sort-ing in history tab

            for GoalIndex, GoalStage in self.GOALS.items():
                GoalStage.qstRef = self
                self.GoalStates[GoalIndex] = GoalState.HIDDEN

            self.QuestOverShowInHistory = True

        def __repr__(self):
            return "%s(%s)" % (self.__class__.__name__, self.__dict__)

        def _tryCall(self, funName, *args, **kwargs):
            if hasattr(self, funName):
                getattr(self, funName)(*args, **kwargs)

        def delayEvent(self, delayNum):
            self.nextEventOnDay = GetGameDay() + delayNum
            return

        def delayCheck(self):
            return self.nextEventOnDay <= GetGameDay()

        # utility, returns goalstate of a goal
        def GetGoalState(self, key):
            Assert(key in self.GoalStates, "key %s not found in goalstates for quest %s" % (key, self))
            return self.GoalStates[key]

        def _SetGoalState(self, key, newVal, silent = False):
            potentialNotification = False

            if not silent and not self.HIDDEN:
                if self.GoalStates[key] != newVal:
                    potentialNotification = True

            self.GoalStates[key] = newVal

            if potentialNotification:
                if newVal == GoalState.VISIBLE:
                    AddNotif(tra(_("New objective: ")) + tra(self.GOALS[key].title), Kind = "qst_goal_new")
                if newVal == GoalState.COMPLETE:
                    AddNotif(tra(_("Objective complete: ")) + tra(self.GOALS[key].title), Kind = "qst_goal_complete")
                if newVal == GoalState.FAILED:
                    AddNotif(tra(_("Objective failed: ")) + tra(self.GOALS[key].title), Kind = "qst_goal_failed")

        def setProgress(self, val, silent = False):
            if self.SIMPLE_GOALS:
                for key in sorted(self.GOALS.keys()):
                    if key != val and self.GoalStates[key] == GoalState.OFF:
                        continue
                    elif key < val:
                        self._SetGoalState(key,GoalState.COMPLETE, silent = silent)
                    elif key == val:
                        self._SetGoalState(key,GoalState.VISIBLE, silent = silent)
                    else:
                        self._SetGoalState(key,GoalState.HIDDEN, silent = silent)

            self.progress = val
            self._tryCall("onSetProgress", val)

        def start(self, silent = False):
            if not self.isActive:
                self.isActive = True
                if not silent and not self.HIDDEN:
                    AddNotif(tra(_("New Quest: %s")) % tra(self.TITLE), Kind = "qst_new")

                # Trigger initial goal-setting
                self.setProgress(self.START_PROGRESS, silent = silent)
                self._tryCall("onStart")

        def fail(self, silent = False):
            self.isActive = False
            self.isOver = True
            self.isFailed = True
            if not silent and not self.HIDDEN:
                AddNotif(tra(_("Quest Failed: %s")) % tra(self.TITLE), Kind = "qst_fail")
            self._tryCall("onOver")
            self._tryCall("onFail")
            

        def finish(self, silent = False):
            if self.isActive:
                self.isActive = False
                self.isOver = True
                self.isComplete = True

                self.setProgress(999, silent = True)

                if not self.HIDDEN:
                    if self.XpReward is not None or self.XpReward > 0:
                        AddExpPlayer(self.XpReward)
                    if not silent:
                        AddNotif(tra(_("Quest Complete: %s")) % tra(self.TITLE), Kind = "qst_complete")
                        if Build_Kind == "nosteam":
                            if persistent.ShowAnnoyingPopup:
                                if len([x for x in allQuests if not x().HIDDEN and QstIsOver(x)]) > len([x for x in allQuests if not x().HIDDEN]) / 2:
                                    persistent.ShowAnnoyingPopup = False
                                    renpy.call_screen("ok_popup", label = _("Developer note"), text = _("Hey there!\nWe hope you're enjoying the game so far.\n\nIf you do enjoy it, you can support us by {a=https://store.steampowered.com/app/2174500?utm_source=Ingamelink}{u}{color=#f09148}purchasing the game on steam{/color}{/u}{/a}.\n\nBesides that, we also have a {a=https://subscribestar.adult/damned-studios}{u}{color=#f09148}Subscribestar page{/color}{/u}{/a} you can follow us at.\n\nIf you want to get in touch, {a=https://discord.gg/cApAfqUdWK}{u}{color=#f09148}join our Discord server{/color}{/u}{/a}.\n\nThanks for playing! Enjoy your journey."))

                ### achievement
                global allQuests
                if can_unlock_achievement("YOUVE_BEEN_BUSY") and len([qst for qst in allQuests if hasattr(qst(), "isComplete") and QstIsComplete(qst) and hasattr(qst(), "IsMain") and not qst().IsMain and not qst().HIDDEN and qst not in adv_guild_quests]) >= 5:
                    unlock_achievement("YOUVE_BEEN_BUSY")

                self.FinishOrder = store.QuestsFinished
                store.QuestsFinished += 1

                self._tryCall("onOver")
                self._tryCall("onComplete")
                

        def getActiveStage(self):
            for key in reversed(sorted(self.GoalStates.keys())):
                if self.GoalStates[key] == GoalState.VISIBLE:
                    return self.GOALS[key]
            return None

        # Returns a list of (GoalState,Stage-obj) tuples
        def getOrderedStages(self):
            rv = []
            for key in sorted(self.GOALS.keys()):
                rv.append((self.GoalStates[key], self.GOALS[key]))
            return rv

        # stores currently selected quest in quest log, only needed for ui
        def log_select(self):
            store.questLogCurSel = self.__class__.__name__

        def log_isSelected(self):
            return store.questLogCurSel == self.__class__.__name__

    # Variant of "quest" that is always hidden
    # Meant for handling various in-game logic: events, dialogue triggers, doors, quest primers
    class LogicModule(BaseQuest):
        HIDDEN = True
        isTracked = False

        def __init__(self):
            super().__init__()

    # enum for goal states
    class GoalState:
        OFF =       -1 # OFFed goal is not affected by simplegoals linear progress thingy
        HIDDEN =    0
        VISIBLE =   1
        COMPLETE =  2
        FAILED =    3

    class QuestStage(object):
        def __init__(self,
                title,
                hintTxt = None,
                trackTag = None,
                trackTagWorldMap = None):
            self.qstRef = None
            self.title = title
            self.hintTxt = hintTxt

            self.TrackTag = trackTag
            self.trackTagWorldMap = trackTagWorldMap

init -1 python:
    allQuests = []
    def AppendToAllQuests(QuestClass):
        allQuests.append(QuestClass)
        return QuestClass
