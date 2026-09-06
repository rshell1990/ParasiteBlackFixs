init python:
    # a logic module that fires an event that initiates the quest
    @AppendToAllQuests
    class PrimerDarkKnight(LogicModule):
        def onEnter(self):  
            if GetLocID() == "mc_house_kitchen":
                if IsDaytime():
                    if QstIsComplete(QstFromAnotherWorld):
                        if QstIsOver(EventNovarasMarkusTavernPostFaw):
                            return TriggeredEvent("qst_DarkKnight_0_startEvent", priority = 1)

    @AppendToAllQuests
    class QstDarkKnight(BaseQuest):
        TITLE = _("The Dark Knight")
        DESCRIPTION = _("Novaras City Guard needs my help.")
        GOALS = {
            0: QuestStage(_("Speak to Captain Nyx"), trackTag = "btn_novaras_fort_seb", hintTxt = _("I received a letter saying Novaras guard needs my help dealing with security issues. I am to find Captain Nyx at Fort Sebastian.")),
            1: QuestStage(_("Eliminate three bandit groups"), hintTxt = _("I have agreed to help Captain Nyx deal with the bandit problem. I need to patrol Novaras city at night, taking on any thugs I encounter. Three groups taken down should suffice.")),
            2: QuestStage(_("Return to Captain Nyx"), trackTag = "btn_novaras_fort_seb", hintTxt = _("I have dealt with enough thugs. Time to report to Captain Nyx."))
            }

        def __init__(self):
            super().__init__()

            self.XpReward = 400
            self.firstEnter = True
            self.wasBriefed = False
            self.gangsSlain = 0
            self.suggestedLevel = 4
            self.IsMain = True

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_army":
                if self.progress == 0:
                    if not self.wasBriefed:
                        HouseLockFortSebastian().CanEnterFreely = True
                        btnMods["btn_novaras_fort_seb"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT, "qst_DarkKnight_1_GoToCaptainNyxOffice")
            # priority to override the post-prologue fort blocker
            return LocButtonMod(directMods = btnMods, priority = 5) 

        def extraDialogue(self):
            if self.progress == 0:
                if self.wasBriefed:
                    yield ("nyx_root",DNode(_("About these bandits..."), "qst_DarkKnight_1_atCaptainNyxOfficeRevisit"))
            elif self.progress == 1:
                yield ("nyx_root",DNode(_("About these bandits..."), "qst_DarkKnight_1_atCaptainNyxOfficeInProg"))
            elif self.progress == 2:
                yield ("nyx_root",DNode(_("I've delivered the message."), "qst_DarkKnight_2_returnToNyx"))

        def onEnter(self):  
            renpy.hide_screen("NovarasPatrolScreen")
            if self.progress == 1:
                if not IsDaytime():
                    if GetLocID() in LocIDList_NovarasCityStreets:
                        renpy.show_screen("NovarasPatrolScreen")

        def onStart(self):
            QstComplete(EventSebastianGuardPostFawOneOff)
            return