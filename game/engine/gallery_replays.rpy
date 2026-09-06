# used in sex scenes, AND IN GAL SCENES to pass in as scope
default Sex_SharedRepeatFlag = False
# used in replay mode to not check preg/nopreg state
default Sex_SharedPregFlag = False
init python:
    # "smartly" checks if we're in rep. variant
    def IsFirstTime():
        if Sex_SharedRepeatFlag == True:
            return False
        else:
            return True
    def SetRepeatVariant(Val):
        if _in_replay:
            return
        store.Sex_SharedRepeatFlag = Val
        return

    def StartReplay(Label, Scope = {}):
        renpy.call_replay(Label, scope = Scope)
        return
    def InReplay():
        return store._in_replay
    def StopReplay():
        renpy.end_replay()
        return
    
        