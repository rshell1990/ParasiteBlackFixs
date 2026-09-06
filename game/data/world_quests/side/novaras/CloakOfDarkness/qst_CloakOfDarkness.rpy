init python:
    @AppendToAllQuests
    class PrimerCloakOfDarkness(LogicModule):
        def onEnter(self):  
            if GetLocID() == "mc_house_bedroom":
                if QstDelayCheck(self):
                    return TriggeredEvent("qst_cloakofdarkness_intro", priority = 1)

    @AppendToAllQuests
    class QstCloakOfDarkness(BaseQuest):
        GOALS = {
            0: QuestStage(_("Check your house"), hintTxt = _("I should check our house in the evening."), trackTag = "btn_mc_house"),
            }
        TITLE = _("Under the cloak of darkness")
        DESCRIPTION = _("[regina_ref_cap!t] is heading out tonight ... I should follow her.")

        def __init__(self):
            super().__init__()

            self.XpReward = 250
            self.hadSex = False

        def onEnter(self):  
            if GetLocID() == "mc_house_kitchen":
                if not IsDaytime():
                    if self.progress == 0:
                        return TriggeredEvent("qst_cloakofdarkness_tailing")
