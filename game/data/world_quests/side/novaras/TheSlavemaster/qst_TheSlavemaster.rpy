init python:
    notesLib["qstTheSlavemasterCall"] = Note(
        _("Captain Nyx' request"),
        _("Captain Nyx wants to speak to me in her office."))

    # a logic module that fires an event that initiates the quest
    @AppendToAllQuests
    class PrimerTheSlavemaster(LogicModule):
        def onExit(self):
            if GetLocID() == "novaras_gates":
                if PlayerPos.lastTag == "novaras_dist_army":
                    if QstDelayCheck(self):
                        if self.progress == 0:
                            return TriggeredEvent("qsttheslavemaster_intro", priority = 1)

        def onEnter(self):  
            if GetLocID() == "novaras_fort_seb_captains_office":
                if QstDelayCheck(self):
                    if self.progress == 1:
                        return TriggeredEvent("qsttheslavemaster_pitch", priority = 1)

    @AppendToAllQuests
    class QstTheSlavemaster(BaseQuest):
        TITLE = _("The Slavemaster")
        DESCRIPTION = _("Captain Nyx has requested my urgent help capturing a notorious slavemaster.")
        SIMPLE_GOALS = False
        MANUAL_DELAY = True
        GOALS = {
            0: QuestStage(_("Read the notes"), trackTag = "btn_novaras_fort_seb", hintTxt = _("Read the notes on trades and slavers and report to Captain Nyx in her office.")),
            1: QuestStage(_("Return to Captain Nyx tomorrow night"), trackTag = "btn_novaras_fort_seb", hintTxt = _("Return to Captain Nyx tomorrow at night.")),
            2: QuestStage(_("Join Captain Nyx at the bordello"), trackTag = "btn_novaras_bordello", hintTxt = _("Join Captain Nyx at the bordello.")),
            3: QuestStage(_("Get your reward"), trackTag = "btn_novaras_fort_seb", hintTxt = _("Return to Captain Nyx in her office tomorrow to claim your reward.")),
            4: QuestStage(_("Get your reward"), trackTag = "btn_novaras_fort_seb", hintTxt = _("Return to Captain Nyx in her office to claim your reward in few days, once she's recovered."))
            }

        def __init__(self):
            super().__init__()

            self.XpReward = 400
            self.reward = "" # valid values "amulet", "money_success", "skill", "panties_success"
            self.suggestedLevel = 3
            self.AlyshaDead = False

        def extraDialogue(self):
            if self.progress == 0:
                yield ("nyx_root", DNode(_("About this slave master..."), "qsttheslavemaster_pitch"))

        def onEnter(self):  
            if self.progress == 1:
                if GetLocID() == "novaras_fort_seb_captains_office":
                    if not IsDaytime():
                        if QstDelayCheck(self):
                            return TriggeredEvent("qsttheslavemaster_noslave")                
            elif self.progress == 2:
                if GetLocID() == "novaras_bordello_interior":
                    if not IsDaytime():
                        if QstDelayCheck(self):
                            return TriggeredEvent("qsttheslavemaster_meeting")
            elif self.progress in (3, 4):
                if GetLocID() == "novaras_fort_seb_captains_office":
                    return TriggeredEvent("qsttheslavemaster_reward")

        def onOver(self):
            QstStart(RomanceNyx)
            QstSetDelay(RomanceNyx, 2)
            return

