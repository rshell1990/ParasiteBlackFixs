init python:
    # a logic module that fires an event that initiates the quest
    @AppendToAllQuests
    class PrimerSharedInThorns(LogicModule):
        def onEnter(self):  
            if GetLocID() == "mc_house_bedroom":
                if IsDaytime():
                    if QstIsComplete(QstBiteBark):
                        if self.progress == 0:
                            return TriggeredEvent("scr_SharedInThorns_Initial")
        def extraDialogue(self):
            if GetLocID() == "mc_house_bedroom":
                if IsDaytime():
                    if QstIsComplete(QstBiteBark):
                        if self.progress == 1:
                            yield ("elena_root",DNode(_("About Lady Thornfall..."), "scr_SharedInThorns_RepInit"))

    # quest itself
    @AppendToAllQuests
    class QstSharedInThorns(BaseQuest):
        TITLE = _("Shared in Thorns")
        DESCRIPTION = _("I have agreed to help Elena find Lady Thornfall.")
        SIMPLE_GOALS = False
        GOALS = {
        0: QuestStage(_("Ask Elena about Lady Thornfall"), trackTag = "btn_mc_house", hintTxt = _("I need to find some evidence about what happened to Lady Thornfall... Perhaps Elena might be able to provide some leads?")),
        1: QuestStage(_("Find out about the Thornfalls' curse"), hintTxt = _("Perhaps a witch of some kind might know about such a curse?")),
        2: QuestStage(_("Look for a book on Thornfall family"), hintTxt = _("The Thornfalls are a particularly old Alderian family, perhaps there is a book on their legacy somewhere?")), #find clue Book (Vala)
        3: QuestStage(_("Find out about Thornfalls trade expeditions"), hintTxt = _("Who might know about about Lady Thornfalls' overseas expedition? Perhaps someone with trade business...")),
        4: QuestStage(_("Talk to Elena about the book"), trackTag = "btn_mc_house", hintTxt = _("I should discuss the book with Elena.")),
        5: QuestStage(_("Talk to Elena about the curse"), trackTag = "btn_mc_house", hintTxt = _("I should discuss the Thornfalls' curse with Elena.")),
        6: QuestStage(_("Talk to Elena about Thornfalls' trade"), trackTag = "btn_mc_house", hintTxt = _("I should discuss the Thornfalls' trading expeditions with Elena.")),
        7: QuestStage(_("Conclude your investigation"), trackTag = "btn_mc_house", hintTxt = _("We should recap what we have found out."))}

        def __init__(self):
            super().__init__()

            self.XpReward = 350
            # valid entries are 'witch' 'trade' 'book'
            self.cluesLearnedAbout = []
            self.cluesCollected = []
            self.cluesTurnedIn = []
            self.threatenedLucius = False

        def extraDialogue(self):
            #if any(["book","witch","trade"]) not in self.cluesLearnedAbout:
            if "book" not in self.cluesLearnedAbout or "witch" not in self.cluesLearnedAbout or "trade" not in self.cluesLearnedAbout:
                yield("elena_root",DNode(_("I have some questions about yourself and the Thornfalls..."), "scr_SharedInThorns_askForClues"))
            if len(self.cluesCollected)>0:
                if any(x not in self.cluesTurnedIn for x in self.cluesCollected):
                    yield("elena_root",DNode(_("Let's discuss what we have found."), "scr_SharedInThorns_turnInClues"))
            if "witch" in self.cluesLearnedAbout and "witch" not in self.cluesCollected:
                yield("babazhul_root",DNode(_("I wish to know about curses..."), "scr_SharedInThorns_babazhulClue"))
            if "trade" in self.cluesLearnedAbout and "trade" not in self.cluesCollected:
                yield("luciusmal_root",DNode(_("Tell me Merchant, do you know of the Thornfalls have any business overseas?"), "scr_SharedInThorns_luciusClue"))
            if "book" in self.cluesLearnedAbout and "book" not in self.cluesCollected:
                yield("vala_root",DNode(_("Do you have any books on old houses such as the Thornfalls?"), "scr_SharedInThorns_valaClue"))
            if len(self.cluesTurnedIn) == 3:
                yield("elena_root",DNode(_("I believe we have found all we can for now."), "scr_SharedInThorns_fin"))

        def onComplete(self):
            PartyAddChar("elena")
            QstStart(PrimerReadingMaterial)
            QstStart(EventElenaQuestions)
            return
