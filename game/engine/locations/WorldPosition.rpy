init python:
    # world LOCATION is "novaras church", world POSITION is "mc is currently AT novaras church"
    class WorldPosition(object):
        def __init__(self, initialPos):
            self.goalTag = initialPos
            self.lastTag = initialPos
            self.tmpName = None
            self.tmpNameEnabled = False

            self.DoExitCheck = False # for exit event

        def GetLoc(self):
            if self.goalTag in wLocs:
                return wLocs[self.goalTag]
            else:
                return None
        
        def __repr__(self):
            return str(self.__dict__)

    ### temporary name overrides
        def setTmpName(self,name):
            self.tmpName = name
            self.tmpNameEnabled = True

        def disableTmpName(self):
            self.tmpNameEnabled = False
    ############################
        def getName(self):
            if self.tmpNameEnabled:
                return tra(self.tmpName)
            else:
                locObj = self.GetLoc()
                if locObj is None:
                    return None
                else:
                    return tra(locObj.displayName)

        # theres nothing direct about this
        def setDirect(self, Goal, Last = None):
            Assert(Goal is not None)
            Assert(Goal in wLocs, "tried to LocSet(%s), but %s is a non-existant loc tag!" % (Goal, Goal))
            self.lastTag = self.goalTag
            self.goalTag = Goal

            # optionally manually set last
            if Last is not None:
                Assert(Last in wLocs, "tried to LocSet(..., Last = %s), but %s is a non-existant loc tag!" % (Last, Last))
                self.lastTag = goal            
            return

        def copy(self):
            return copy.deepcopy(self)

        def __eq__(self, other):
            return self.goalTag == other.goalTag

    # sets a location to target ID
    def LocSet(LocID, Last = None):
        PlayerPos.setDirect(Goal = LocID, Last = Last)
        return
    def GetLocID(): # to get loc ID we're at
        return PlayerPos.goalTag


### location names
    def LocNameSetTemp(Name):
        PlayerPos.setTmpName(Name)
        return
    def LocNameReset():
        PlayerPos.disableTmpName()
        return

### loc sound
    def LocUpdateDynSound():
        PlayerPos.GetLoc().UpdateAllDynSound()
        return

### main means to "enter"
    # enter with a transition
    def LocEnter(Trans = dissolve):
        Assert(not isinstance(Trans, str))
        LocFlush(Trans)
        renpy.jump("main_recheck")
        return

    # "quick", enter without transition
    def LocEnterQ():
        LocEnter(Trans = None)
        return
