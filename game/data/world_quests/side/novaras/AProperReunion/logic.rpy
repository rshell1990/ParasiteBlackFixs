init python:
    # a logic module that fires an event that initiates the quest
    @AppendToAllQuests
    class PrimerQstProperReunion(LogicModule):
        def onEnter(self):  
            if GetLocID() == "mc_house_kitchen":
                if IsDaytime():
                    if QstIsComplete(QstFromAnotherWorld):
                        return TriggeredEvent("qst_reunion_home")

    @AppendToAllQuests
    class QstProperReunion(BaseQuest):
        TITLE = _("A Proper Reunion")
        DESCRIPTION = _("I have met Adara for the first time after leaving Novaras.")
        GOALS = {
            0: QuestStage(_("Speak to Adara"), 
                hintTxt = _("I should catch up with Adara, now that I have changed... So much.")),
            1: QuestStage(_("Meet Adara at the Tavern, after dark"), 
                trackTag = "btn_novaras_tavern", 
                hintTxt = _("I have agreed to meet Adara at the Iron Unicorn tavern, after dark. The tavern should be at the market district.")),
            }

        def __init__(self):
            super().__init__()

            self.XpReward = 250
            self.paidForMedicine = False
            self.friendZoned = False
            self.toldParasite = None
            self.toldKiara = None

        def onEnter(self):  
            if GetLocID() == "novaras_tavern":
                if not IsDaytime():
                    if self.progress == 1:
                        return TriggeredEvent("qst_reunion_tavern")
