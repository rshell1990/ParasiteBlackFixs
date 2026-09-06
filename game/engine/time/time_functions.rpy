default block_wait_global = False # blocks wait long-term (used by quests, like prologue)
default block_wait_dynamic = False # short-term wait blocker, for pauses mostly. is reset by hiding say box!

init -1 python:
    def IsDaytime():
        #return IsInTimeFrame(TIME_DAY_START, TIME_DAY_END)
        # ^ it was this one before, lets see what happens now
        return IsInTimeFrame(TIME_VISUAL_DAWN, TIME_VISUAL_DUSK)
    def IsEvening(): # <- kinda fucked up?
        return rpTime >= TIME_DAY_END
    def IsMorning():
        return IsInTimeFrame(TIME_MORNING, TIME_NOON)
    def IsMorningOrNoon():
        return IsInTimeFrame(TIME_MORNING, TIME_AFTERNOON)
    def IsDawnToNoon():
        return IsInTimeFrame(TIME_DAWN, TIME_AFTERNOON)

    # takes two timeframes, these are defined in nearby time vars file
    # for ex IsInTimeFrame(TIME_DAWN, TIME_DUSK) will return true if clock is within this range
    def IsInTimeFrame(frame_1, frame_2):
        # we're not monsters
        if frame_1 == frame_2:
            return "Fuck you!"
        # in case were' doing a thru-midnight check
        if frame_2 < frame_1:
            # WARNING NOTICE THE < not <= ON SECOND COMPARISON! ELSE PROB OVERLAPS
            return frame_1 <= rpTime <= SECS_IN_DAY or 0 <= rpTime < frame_2
        else:
            #return rpTime >= smollest and rpTime < biggest
            return frame_1 <= rpTime < frame_2

    # advance time to X point (dont reverse please)
    def TimeAdvTo(val):
        # store how many hours into a day we are
        AdvHoursStart = int(store.rpTime / SECS_IN_HOUR)    # 0 to 23

        # calc time to advance by for noon detection
        timeAdvance = val - store.rpTime
        # warp into next day time if necessary
        ModVal = val % SECS_IN_DAY
        # if next day happened, add extra hours to the hour-counting shit
        if ModVal < val:
            ExtraHours = 24 - AdvHoursStart
        else:
            ExtraHours = 0

        # Noon detection system, works periodically so it always works. <-- what the fuck is that retarded line?
        # The same code would work for any other time of day if you replace TIME_NOON with another time constant value
        timeToNxtNoon = (-((store.rpTime - SECS_IN_HALFDAY) % SECS_IN_DAY) + SECS_IN_DAY)
        if timeAdvance >= timeToNxtNoon:
            # For testing noon detection
            for qstObj in GetAllActiveQuests():
                if hasattr(qstObj, "onNoon"):
                    qstObj.onNoon()

        # new day happened
        if ModVal < store.rpTime:
            ### midnight check for quests/logicmods
            for qstObj in GetAllActiveQuests():
                if hasattr(qstObj, "onMidnight"):
                    qstObj.onMidnight()

            if QstIsActive(InfectionModule) and InfectionModule().DailyGain:
                InfChangeBy(RngInt(9, 12))
            AddGameDays(1)

        # check if any hours passed and tick status effects
        AdvHoursEnd = int(ModVal / SECS_IN_HOUR)
        HoursPassed = AdvHoursEnd - AdvHoursStart
        HoursPassed += ExtraHours
        if HoursPassed > 0:
            for i in range(HoursPassed):
                TickStoryStatusEffects()

        TimeSetTo(ModVal)
        return
    
    # shorthand to advance "by" vs "to" from the above
    def TimeAdvBy(val):
        Assert(val <= SECS_IN_DAY, "TimeAdvBy was asked to adv time by more seconds than there are in a day per single increment, cant do that")
        TimeAdvTo(store.rpTime + val)
        return

    def TimeSetTo(Val):
        store.rpTime = Val
        return

    def IsCurWeekday(WeekDay):
        Assert(0 <= WeekDay < 7)
        if GetCurWeekday() == WeekDay:
            return True
        else:
            return False

    # returns weekday index from 0 to 6
    def GetCurWeekday():
        return Time_GetCurDate().weekIdx

    # returns ingame day (for quest logic checks)
    def GetGameDay(): 
        return store.day

    def SetGameDay(val):
        store.day = val
        return

    def AddGameDays(val):
        store.day += val
        return

    # sets the waiting blockers to true-false. global is more general-purpose
    def BlockWaitGlobal(Value):
        store.block_wait_global = Value
        return
    # dynamic is more internal! its for more immediate stuff like during renpy pause. it gets reset to false automatically on sleep, travel, unpause
    def BlockWaitDynamic(Value):
        store.block_wait_dynamic = Value
        return
    def GetBlockWaitDynamic():
        return store.block_wait_dynamic

    # control whether time proceeds or not
    def AutoTimeFreeze(Value):
        store.FreezeAutoTime = Value
        return


### next comes internal stuff
##########################################
    class RpDate(object):
        def __init__(self, year = 0, monthIdx = 0, day = 0, weekIdx = 0):
            self.year = year
            self.monthIdx = monthIdx    # 0->11
            self.day = day              # 1->~30
            self.weekIdx = weekIdx

        def _totalDays(self):
            dayCnt = self.year*rpDate_yearLength
            for mLen, _, _ in rpDate_months[:self.monthIdx]:
                dayCnt += mLen
            return dayCnt + (self.day-1)

        def __repr__(self):
            shortMonthStr = rpDate_months[self.monthIdx][2]
            weekStr = STR_TIME.WEEKDAYS[self.weekIdx]
            return f"{shortMonthStr} {self.day} ({weekStr}), {self.year}"

    #return rpTime < Time_HMSToSeconds and rpTime < TIME_DAY_END
    # get current formatted date: month, day (weekday id), year
    # 'interfaced' with via Time_GetCurDate
    def Time_DateFromDays(gameTotalDays):
        x = gameTotalDays + rpDate_dayZeroDayOffset

        weekIdx = (x + rpDate_dayZeroDate.weekIdx) % 7
        year = x // rpDate_yearLength
        x = x % rpDate_yearLength

        i = 0
        while x >= rpDate_months[i][0]:
            x -= rpDate_months[i][0]
            i += 1

        return RpDate(year, i, x + 1, weekIdx)

    def Time_GetCurDate():
        global rpDate_dateCache
        global rpDate_cachedFor
        if GetGameDay() != rpDate_cachedFor:
            rpDate_dateCache = Time_DateFromDays(GetGameDay())
            rpDate_cachedFor = GetGameDay()
        return rpDate_dateCache

    # convert hour/min to seconds
    def Time_HMSToSeconds(hour = 0, min = 0, sec = 0):
        return sec + 60 * (min + 60 * hour)

    # returns timeframe string, such as "Night" or "Dawn"
    def Time_GUI_GetTimeOfDayName():
        timeFrameVar = "Night"
        for tf_time, tf_name in TIME_FRAME_NAMES.items():
            if rpTime >= tf_time:
                timeFrameVar = tf_name
        return timeFrameVar

    # char increment time callback
    def Time_IncrementTimeCB(event, interact = True, **kwargs):
        if event == "end" and hasattr(store, "rpTime"):
            if not FreezeAutoTime:
                TimeAdvBy(30)

    config.all_character_callbacks.append(Time_IncrementTimeCB)


    store.InLocTransition = False
    # used by time tracker to allow/not allow waiting
    # no idea whats going on here
    def Time_GUI_CanPlayerWait():
        if InLocTransition and wLocs[GetLocID()].CanWait:
            return True
        elif (not block_wait_global 
            and not block_wait_dynamic 
            and wLocs[GetLocID()].CanWait
            and not FreezeAutoTime
            and not renpy.get_screen("say", layer = "screens")
            and not renpy.get_screen("choice", layer = "screens")
            and renpy.get_ongoing_transition() == None):
            return True
        else:
            return False