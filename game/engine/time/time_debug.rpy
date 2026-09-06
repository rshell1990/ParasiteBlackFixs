init python:
    # get time as numbers: hh:mm:ss
    def DEBUG_ShowTimeAsNumbers():
        totalSecs = rpTime
        secs = totalSecs % 60
        totalSecs = totalSecs // 60
        mins = totalSecs % 60
        totalSecs = totalSecs // 60
        hours = totalSecs % 24
        return "%d:%02d:%02d" % (hours, mins, secs)
