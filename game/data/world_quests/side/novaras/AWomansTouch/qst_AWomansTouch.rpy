init python:
    # a logic module that fires an event that initiates the quest
    @AppendToAllQuests
    class PrimerWomansTouch(LogicModule):
        def __init__(self):
            super().__init__()
            self.dayToStartFiringEvent = -1

        def onMidnight(self):
            if QstIsComplete(QstReadingMaterial):
                if self.dayToStartFiringEvent == -1:
                    self.dayToStartFiringEvent = GetGameDay() + 3

        def onEnter(self):  
            if GetLocID() == "mc_house_bedroom":
                if IsDaytime():
                    if QstIsComplete(QstReadingMaterial):
                        if self.dayToStartFiringEvent != -1:
                            if GetGameDay() >= self.dayToStartFiringEvent:
                                return TriggeredEvent("scr_WomansTouch_primer")

    # quest itself
    @AppendToAllQuests
    class QstWomansTouch(BaseQuest):
        TITLE = _("A woman's touch")
        DESCRIPTION = _("Elena wants advice from a Courtesan about 'desire,' who might be willing to help?")
        GOALS = {
            0: QuestStage(_("Talk to a Courtesan"), 
                hintTxt = _("I should find a woman competent enough to sate Elena's newfound curiosity.")),
            1: QuestStage(_("Pay for Elena's education"), 
                hintTxt = _("Helena, a high-class courtesan in Novaras bordello is willing to help. For a price."))}

        def __init__(self):
            super().__init__()

            self.XpReward = 250

        def extraDialogue(self):
            if self.progress == 0:
                yield ("helena_root", DNode(_("I need your help with a sensitive matter..."), "scr_WomansTouch_1"))
            elif self.progress == 1:
                yield ("helena_root", DNode(_("About a... sensitive matter."), "scr_WomansTouch_helenaMenu"))

        def onComplete(self):
            QstStart(RomanceElena)