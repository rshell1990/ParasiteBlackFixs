# (yea we're no big on math)
init python:
    def ClampValue(value, minval, maxval):
        if value < minval: return minval
        if value > maxval: return maxval
        return value