init python:
    @AppendToAllQuests
    class EventElenaNightmares(LogicModule):
        def onPreSleepMcHouse(self):
            if GetLocID() == "mc_house_bedroom":
                if IsDaytime():
                    if QstIsOver(EventElenaDrunk):
                        if RngInt(1, 2) == 1:
                            return TriggeredEvent("event_Elena_nightmares")
