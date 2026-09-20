init python:
    def has_arda_dlc():
        return renpy.loadable("arda_scr")
    
    @AppendToAllQuests
    class PrimerArda(LogicModule):
        def __init__(self, active=True):
            super().__init__()
            self.isActive = active

        def onEnter(self):
            if not has_arda_dlc():
                return
            # Check if player is anywhere in Novaras (starts with "novaras_") and QstTwoEmperors is finished
            if GetLocID().startswith("novaras_") and QstIsComplete(QstTwoEmperors) and not QstIsOver(QstArda):
                # arda_intro starts the quest itself (QstStart + QstSetProgress live there)
                renpy.call("arda_intro")

    @AppendToAllQuests
    class QstArda(BaseQuest):
        TITLE = _("DLC: Arda")
        DESCRIPTION = _("The Ringing of the Bells")
        LABEL = "DLC Quest"
        GOALS = {
            0: QuestStage(_("The ringing of the bells..."), 
                trackTag = "btn_novaras_church", 
                hintTxt = _("After hearing some strange bells that no one else can hear... I feel compelled to head to a church for some reason")),
            1: QuestStage(_("Go to your bedroom to think"), 
                trackTag = "novaras_mc_bedroom", 
                hintTxt = _("The voice said it left me a gift... But where")),
        }
        def __init__(self):
            super().__init__()
            self.XpReward = 250

        def onEnter(self):
            if GetLocID() == "novaras_church" and QstIsActive(self) and not IsGoalComplete(self, 0):
                return TriggeredEvent("arda_church")
            elif GetLocID() == "mc_house_bedroom" and IsGoalComplete(self, 0):
                return TriggeredEvent("arda_finish")