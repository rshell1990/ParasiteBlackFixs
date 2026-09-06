init python:
    @AppendToAllQuests
    class EventElenaDrunk(LogicModule):
        def __init__(self):
            super().__init__()

            self.dayToGetDrunk = -1

        def onMidnight(self):
            if QstIsOver(EventElenaTraining):
                if self.dayToGetDrunk == -1:
                    self.dayToGetDrunk = GetGameDay() + 2
            return

        def onEnter(self):  
            if GetLocID() == "mc_house_bedroom":
                if IsDaytime():
                    if QstIsOver(EventElenaTraining):
                        if self.progress == 0:
                            if GetGameDay() >= self.dayToGetDrunk:
                                if self.dayToGetDrunk != -1:
                                    return TriggeredEvent("ev_elena_drunk")
                        elif self.progress == 1:
                            if GetGameDay() >= self.dayToGetDrunk + 1:
                                return TriggeredEvent("ev_elena_drunk_nextday")

        def onPostSleepMcHouse(self):
            if GetLocID() == "mc_house_bedroom":
                if self.progress == 1:
                    return TriggeredEvent("ev_elena_drunk_nextday")

        def onComplete(self):
            QstStart(EventElenaNightmares)
            return