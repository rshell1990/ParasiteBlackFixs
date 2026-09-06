init python:
    @AppendToAllQuests
    class EventElenaTraining(LogicModule):
        def __init__(self):
            super().__init__()

            self.canTrain = False

        def onPostSleepMcHouse(self):
            if GetLocID() == "mc_house_bedroom":
                if QstIsOver(EventElenaMorning):
                    if self.progress == 0:
                        return TriggeredEvent("event_Elena_training")

        def extraDialogue(self):
            if self.progress == 1:
                yield ("elena_root",DNode(_("I am ready for training."), "event_Elena_training2"))

        def onComplete(self):
            QstStart(EventElenaDrunk)
            return
