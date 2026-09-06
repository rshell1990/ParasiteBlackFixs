init python:
    @AppendToAllQuests
    class EventReginaDildo(LogicModule):
        def __init__(self):
            super().__init__()
    
            self.dildoEvent = False

        def onPreSleepMcHouse(self):
            if self.dildoEvent and GetLocID() == "mc_house_bedroom":
                if RngInt(1, 3) == 1:
                    return TriggeredEvent("reginaPackage_dildo")

label reginaPackage_dildo:
    call regina_dildo_peek from _call_regina_dildo_peek
    return
