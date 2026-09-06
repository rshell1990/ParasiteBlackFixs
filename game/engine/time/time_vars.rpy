init python:
######## time frames
    TIME_LATENIGHT =    Time_HMSToSeconds(hour = 1, min = 31) # 01:31 till 04:30
    TIME_DAWN =         Time_HMSToSeconds(hour = 4, min = 31) # 04:31 till 07:30
    TIME_MORNING =      Time_HMSToSeconds(hour = 7, min = 31) # 07:31 till 10:30
    TIME_NOON =         Time_HMSToSeconds(hour = 10, min = 31) # 10:31 till 13:30 (37,860 seconds - 45,000 seconds)
    TIME_AFTERNOON =    Time_HMSToSeconds(hour = 13, min = 31) # 13:31 till 16:30
    TIME_DUSK =         Time_HMSToSeconds(hour = 16, min = 31) # 16:31 till 19:30
    TIME_LATEEVENING =  Time_HMSToSeconds(hour = 19, min = 31) # 19:31 till 22:30
    TIME_NIGHT =        Time_HMSToSeconds(hour = 22, min = 31) # 22:31 till 01:30
    TIME_MIDNIGHT =     Time_HMSToSeconds(hour = 0) # exact 00:00

######### time shorthands in seconds
    TIME_1H = 3600
    TIME_2H = 7200
    TIME_3H = TIME_1H * 3
    TIME_4H = TIME_1H * 4

    TIME_05H =  TIME_1H  * 0.5
    TIME_025H = TIME_1H * 0.25

######## aliases for week days
    WEEKDAY_MON = 0
    WEEKDAY_TUE = 1
    WEEKDAY_WED = 2
    WEEKDAY_THU = 3
    WEEKDAY_FRI = 4
    WEEKDAY_SAT = 5
    WEEKDAY_SUN = 6

###################### internals next mostly
    rpDate_dateCache = None
    rpDate_cachedFor = None
    # list of (day length, full month name, short month name)
    rpDate_months = [
        (31, STR_TIME.MONTH_1, STR_TIME.MONTH_1_SHORT),
        (29, STR_TIME.MONTH_2, STR_TIME.MONTH_2_SHORT),
        (31, STR_TIME.MONTH_3, STR_TIME.MONTH_3_SHORT),
        (30, STR_TIME.MONTH_4, STR_TIME.MONTH_4_SHORT),
        (31, STR_TIME.MONTH_5, STR_TIME.MONTH_5_SHORT),
        (29, STR_TIME.MONTH_6, STR_TIME.MONTH_6_SHORT),
        (31, STR_TIME.MONTH_7, STR_TIME.MONTH_7_SHORT),
        (31, STR_TIME.MONTH_8, STR_TIME.MONTH_8_SHORT),
        (29, STR_TIME.MONTH_9, STR_TIME.MONTH_9_SHORT),
        (31, STR_TIME.MONTH_10, STR_TIME.MONTH_10_SHORT),
        (30, STR_TIME.MONTH_11, STR_TIME.MONTH_11_SHORT),
        (31, STR_TIME.MONTH_12, STR_TIME.MONTH_12_SHORT)]

    SECS_IN_DAY = 60 * 60 * 24
    SECS_IN_HOUR = 60 * 60
    SECS_IN_HALFDAY = 60 * 60 * 12

    # more timeframes, there are for logic
    TIME_DAY_START = TIME_DAWN
    TIME_DAY_END = TIME_LATEEVENING

    # these are "halfway through" the first (or last) daylight part of a daytime wheel
    # DO YOU UNDERSTAND
    TIME_VISUAL_DAWN = TIME_DAWN + ((TIME_MORNING -     TIME_DAWN) / 2)
    TIME_VISUAL_DUSK = TIME_DUSK + ((TIME_LATEEVENING - TIME_DUSK) / 2)

    # for ui
    TIME_FRAME_NAMES = {
    TIME_LATENIGHT: STR_TIME.LATENIGHT,
    TIME_DAWN:      STR_TIME.DAWN,
    TIME_MORNING:   STR_TIME.MORNING,
    TIME_NOON:      STR_TIME.NOON,
    TIME_AFTERNOON: STR_TIME.AFTERNOON,
    TIME_DUSK:      STR_TIME.DUSK,
    TIME_LATEEVENING:STR_TIME.LATEEVENING,
    TIME_NIGHT:     STR_TIME.NIGHT
    }

    rpDate_yearLength = 0
    def TimeCalcYearLen():
        for mLen, v1, v2 in rpDate_months:
            store.rpDate_yearLength += mLen
    TimeCalcYearLen()

    # When total game days = 0, this is the date
    rpDate_dayZeroDate = RpDate(year = 1163, monthIdx = 5, day = 27, weekIdx = 0)
    rpDate_dayZeroDayOffset = rpDate_dayZeroDate._totalDays()
