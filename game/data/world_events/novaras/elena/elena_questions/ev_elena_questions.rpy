init python:
    @AppendToAllQuests
    class EventElenaQuestions(LogicModule):
        def __init__(self):
            super().__init__()

            self.dayToStartFiringEvent = -1
            self.sillyAnswers = 0

        def onMidnight(self):
            if QstIsComplete(QstSharedInThorns):
                if self.dayToStartFiringEvent == -1:
                    self.dayToStartFiringEvent = GetGameDay() + 2

        def onEnter(self):  
            if GetLocID() == "mc_house_bedroom":
                if IsDaytime():
                    if QstIsComplete(QstSharedInThorns):
                        if not self.dayToStartFiringEvent == -1:
                            if GetGameDay() >= self.dayToStartFiringEvent:
                                return TriggeredEvent("scr_event_Elena_QuestionsAfterThorns")
