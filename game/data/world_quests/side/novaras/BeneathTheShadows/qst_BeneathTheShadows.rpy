init python:
    notesLib["QstBeneathShadowsPrimerNote"] = Note(
        _("Visit the Weeping Heart bordello"), 
        _("Captain Nyx wants me to come to the Weeping Heart bordello tonight, to meet someone... I wonder who can that be."))
    # a logic module that fires an event that initiates the quest
    @AppendToAllQuests
    class PrimerBeneathTheShadows(LogicModule):
        def onEnter(self):  
            if self.progress == 0:
                if GetLocID() in LocIDList_NovarasCityStreets:
                    return TriggeredEvent("qst_beneath_shadows_messenger", priority = 1)
            elif self.progress == 1:
                if GetLocID() == "novaras_bordello_interior":
                    return TriggeredEvent("qst_beneath_shadows_enter_bordello_meet_carina", priority = 1)
            return

        def onComplete(self):
            return

    # quest itself
    @AppendToAllQuests
    class QstBeneathTheShadows(BaseQuest):
        TITLE = _("Beneath the Shadows")
        DESCRIPTION = _("Carina Calworth, a menacing owner of the Weeping Heart bordello, needs my help collecting from her... 'businesses'?")
        GOALS = {
            10: QuestStage(_("Collect (Market District)"), hintTxt = _("I must find a dealer at the Market District to collect Carina's money. Dealers only operate at night.")),
            20: QuestStage(_("Collect (Housing District)"), hintTxt = _("I need to pick up Carina's money from a dealer down at the Housing District.")),
            30: QuestStage(_("Collect (Mage District)"), hintTxt = _("I need to find a dealer in the Mage District and collect Carina's money.")),
            40: QuestStage(_("Turn in"), hintTxt = _("Now I need to return the gold I have collected to Carina."), trackTag = "btn_kennels"),
            }

        # we have three simultaneous goals
        SIMPLE_GOALS = False

        def __init__(self):
            super().__init__()

            self.XpReward = 250

            # money to collect from each dealer
            self.CollectAmount = 250

            # can negotiate upwards
            self.RewardGoldBase = 300 
            self.RewardGold = self.RewardGoldBase

            # can negotiate to undress
            self.RewardUndress = False

        def locationMod(self):
            btnMods = {}
            # these dealers should only appear at night
            if not IsDaytime():
                if GetLocID() == "novaras_dist_mage":
                    if not IsGoalComplete(self, 30):
                        btnMods["btn_novaras_mage_dist_dealer"] = BtnJumpLabel(_("Look for a dealer"), "qst_beneath_shadows_dealer_mage_dist")
                elif GetLocID() == "novaras_dist_market":
                    if not IsGoalComplete(self, 10):
                        btnMods["btn_novaras_market_dist_dealer"] = BtnJumpLabel(_("Look for a dealer"), "qst_beneath_shadows_dealer_market_dist")
                elif GetLocID() == "novaras_dist_house":
                    if not IsGoalComplete(self, 20):
                        btnMods["btn_novaras_house_dist_dealer"] = BtnJumpLabel(_("Look for a dealer"), "qst_beneath_shadows_dealer_house_dist")
            return LocButtonMod(directMods = btnMods)
            
        def onComplete(self):
            QstStart(NovarasSexDungeon)
            # for auto-complete
            if not QstIsActive(NovarasDealer):
                QstStart(NovarasDealer)
            return

        def onStart(self):
            ### fix some prior events
            QstStart(DoorNovarasBordelloOffice)
            CharMeet("carina", Silent = True)
            # (for auto-completion) in case mc havent met arwen before, the quest does that
            if QstGetProgress(DialogueArwen) == 0:
                CharMeet("arwen", Silent = True)
                QstSetProgress(DialogueArwen, 1)
            ### onwards with the quest
            QstStart(DialogueCarina)
            QstComplete(PrimerBeneathTheShadows)
            return

        def extraDialogue(self):
            yield ("carina_root", DNode(_("About your money..."), "qst_beneath_shadows_talk_carina_office"))
