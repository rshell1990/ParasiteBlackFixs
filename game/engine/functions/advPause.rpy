default PausedInNarrative = False

init python:

    # always use this pause instead of direct renpy pause: important for travel/wait code
    def Pause(sec = None):
        BlockWaitDynamic(True)
        store.PausedInNarrative = True
        renpy.pause(delay = sec)
        store.PausedInNarrative = False
        BlockWaitDynamic(False)
        return