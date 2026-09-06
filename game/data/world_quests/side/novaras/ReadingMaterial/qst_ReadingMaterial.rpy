init python:
    # a logic module that fires an event that initiates the quest
    @AppendToAllQuests
    class PrimerReadingMaterial(LogicModule):
        def __init__(self):
            super().__init__()

            self.dayToStartFiringEvent = -1

        def onEnter(self):  
            if GetLocID() == "mc_house_bedroom":
                if IsDaytime():
                    if self.dayToStartFiringEvent != -1:
                        if GetGameDay() >= self.dayToStartFiringEvent:
                            if not QstIsActive(QstReadingMaterial):
                                if QstIsComplete(QstSharedInThorns):
                                    return TriggeredEvent("scr_ReadingMaterial_primer")

        def onMidnight(self):
            if QstIsComplete(QstSharedInThorns):
                if self.dayToStartFiringEvent == -1:
                    self.dayToStartFiringEvent = GetGameDay() + 2

    # quest itself
    @AppendToAllQuests
    class QstReadingMaterial(BaseQuest):
        TITLE = _("Reading Material")
        DESCRIPTION = _("Elena wants a book.")
        GOALS = {
            0: QuestStage(_("Visit the library"), trackTag = "btn_novaras_library", hintTxt = _("I should head to the library and find some books for Elena.")),
            1: QuestStage(_("Return Home"), trackTag = "btn_mc_house", hintTxt = _("Now that we have the books, let's bring them over to my place."))}

        def __init__(self):
            super().__init__()

            self.XpReward = 300
            self.valaRevisitFlag = False

        def extraDialogue(self):
            if self.progress == 0 and self.valaRevisitFlag:
                yield ("vala_root",DNode(_("About books for Elena..."), "scr_ReadingMaterial_1_revisit"))

        def onEnter(self):  
            if GetLocID() == "novaras_library_int":
                if IsDaytime():
                    if self.progress == 0:
                        if not self.valaRevisitFlag:
                            return TriggeredEvent("scr_ReadingMaterial_1")

            elif GetLocID() == "mc_house_bedroom":
                if self.progress == 1:
                    return TriggeredEvent("scr_ReadingMaterial_2")

        def onComplete(self):
            QstStart(EventElenaMorning)
            QstStart(PrimerWomansTouch)