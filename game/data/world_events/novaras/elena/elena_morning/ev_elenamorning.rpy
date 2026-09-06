init python:
    @AppendToAllQuests
    class EventElenaMorning(LogicModule):
        def __init__(self):
            super().__init__()

            self.dayToStartFiringEvent = -1

        def onMidnight(self):
            if QstIsComplete(QstReadingMaterial):
                if self.dayToStartFiringEvent == -1:
                    self.dayToStartFiringEvent = GetGameDay() + 2

        def onComplete(self):
            QstStart(EventElenaTraining)

        def onPostSleepMcHouse(self):
            if GetLocID() == "mc_house_bedroom":
                if IsDaytime():
                    if QstIsComplete(QstReadingMaterial):
                        if self.dayToStartFiringEvent != -1:
                            if GetGameDay() >= self.dayToStartFiringEvent:
                                return TriggeredEvent("scr_event_Elena_morningAfterBook")
