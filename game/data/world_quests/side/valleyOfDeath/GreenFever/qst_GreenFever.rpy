init python:
    @AppendToAllQuests
    class QstGreenFever(BaseQuest):
        TITLE = _("Green Fever")
        DESCRIPTION = _("Camping out in the Valley of Death all alone, Ves lacks some proper medicine stashed. I have agreed to procure some.")
        GOALS = {
            0: QuestStage(_("Visit the Palam Tower"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("The Mages of Palam will likely have medicine to sell.")),
            1: QuestStage(_("Purchase the medicine package"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("Sister Divine agreed to help me out for some coin. She asks for one hundred in exchange for a broad package of remedies.")),
            2: QuestStage(_("Return with the package"), trackTag = "ves_tent_int_button", hintTxt = _("I have the medicine on me. Now, gotta bring it over to Ves."), trackTagWorldMap = "ves_camp"),
        }

        def __init__(self):
            super().__init__()

            self.XpReward = 300
            self.NegotiatedCheaperPrice = False

        def extraDialogue(self):
            if self.progress == 0:
                yield ("divine_root",DNode(_("I'm looking for some medicine."), "divine_ves_med"))
            if self.progress == 1:
                yield ("divine_root",DNode(_("About that medicine..."), "divine_ves_med_revisit"))
            if self.progress == 2:
                yield ("ves_root",DNode(_("I brought you some medicine."), "greenFeverMedsReturn"))

        def onComplete(self):
            QstSetProgress(RomanceVes, 3)