init python:
    @AppendToAllQuests
    class PrimerTheDarkSpecterOfBiggieSmalls(LogicModule):
        def __init__(self, active=True): #Starts Immediately
            super().__init__()
            self.isActive = active

        def onEnter(PrimerTheDarkSpecterOfBiggieSmalls): #Only "Starts" during the day and walking in hamun
            if IsDaytime():
                if GetLocID() in ["hamun_dist_docks", "hamun_dist_merch_lord"]:
                    return TriggeredEvent("qst_TheDarkSpecterOfBiggieSmalls_intro")

    @AppendToAllQuests
    class QstTheDarkSpecterOfBiggieSmalls(BaseQuest):
        TITLE = _("The Dark Specter of Biggie Smalls")
        DESCRIPTION = _("Garen Quiltshire has summoned me to deal with something urgent... I should find out what it is")
        LABEL = "Test Quest"
        GOALS = {
            0: QuestStage(_("Meet Garen Quiltshire"), 
                trackTag = "btn_hamun_hookah_bar_garen", 
                hintTxt = _("Garen is found at the Pale Dragon")),
            1: QuestStage(_("Defeat Lenin at the library"), 
                trackTag = "btn_hamun_library", 
                hintTxt = _("Lenin can be found at Hamun library")),
            2: QuestStage(_("Deliver Sweetie Fox the cat"),
                trackTag = "hamun_brothel", 
                hintTxt = _("Sweetie Fox can be found at the brothel")),
            3: QuestStage(_("Summon Biggie Smalls at the Pale Dragon"),
                trackTag = "btn_hamun_hookah_bar_garen", 
                hintTxt = _("Return to Garen Quiltshire at {i}The Pale Dragon. one more time to give the Dodgy Tax Receipts.")),
            4: QuestStage(_("Meet Garen Quiltshire at the Pale Dragon"),
                trackTag = "btn_hamun_hookah_bar_garen", 
                hintTxt = _("Return to Garen Quiltshire at {i}The Pale Dragon. repeatable reward")),
        }
        
        def __init__(self):
            super().__init__()
            self.XpReward = 250
            self.TakenQuest = 0
            self.ChosenReward = 0
            ####################
            self.Feline = False
            self.SweetieDelivered = False
            ####################
            self.LeninFound = False
            self.LeninDefeated = False
            ####################
            self.BiggieSummoned = False
            self.BiggieDefeated = False
            self.rewardClaimed = False
            self.GarenRewardClaimed = False
        
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_hookah_bar":
                if QstTheDarkSpecterOfBiggieSmalls().TakenQuest == 0:
                    btnMods["btn_hamun_hookah_bar_garen"] = BtnJumpLabel(_("Talk to Garen"), "qst_TheDarkSpecterOfBiggieSmalls_garen1")
                elif QstTheDarkSpecterOfBiggieSmalls().TakenQuest == 2:
                    btnMods["btn_hamun_hookah_bar_garen"] = BtnJumpLabel(_("Talk to Garen"), "qst_TheDarkSpecterOfBiggieSmalls_garen2")
                elif QstTheDarkSpecterOfBiggieSmalls().BiggieDefeated == True and QstTheDarkSpecterOfBiggieSmalls().GarenRewardClaimed == False:
                    btnMods["btn_hamun_hookah_bar_garen"] = BtnJumpLabel(_("Talk to Garen"), "qst_TheDarkSpecterOfBiggieSmalls_garen4")
                elif QstTheDarkSpecterOfBiggieSmalls().LeninDefeated == True and QstTheDarkSpecterOfBiggieSmalls().SweetieDelivered == True and QstTheDarkSpecterOfBiggieSmalls().BiggieSummoned == False:
                    btnMods["btn_hamun_hookah_bar_garen"] = BtnJumpLabel(_("Talk to Garen"), "qst_TheDarkSpecterOfBiggieSmalls_garen3")
                elif QstTheDarkSpecterOfBiggieSmalls().TakenQuest == 1 and QstTheDarkSpecterOfBiggieSmalls().LeninDefeated == False and QstTheDarkSpecterOfBiggieSmalls().SweetieDelivered == False:
                    btnMods["btn_hamun_hookah_bar_garen"] = BtnJumpLabel(_("Talk to Garen"), "qst_TheDarkSpecterOfBiggieSmalls_garenreturn")
                elif QstTheDarkSpecterOfBiggieSmalls().GarenRewardClaimed == True:
                    btnMods["btn_hamun_hookah_bar_garen"] = BtnJumpLabel(_("Talk to Garen"), "qst_TheDarkSpecterOfBiggieSmalls_garen_postquest")
            return LocButtonMod(directMods = btnMods, priority = 2)

        def onEnter(self):
            if GetLocID() == "hamun_library" and QstTheDarkSpecterOfBiggieSmalls().LeninFound == False:
                return TriggeredEvent("qst_TheDarkSpecterOfBiggieSmalls_lenin")
            elif GetLocID() == "hamun_brothel" and QstTheDarkSpecterOfBiggieSmalls().SweetieDelivered == False:
                if PlayerHasItem("qst_feline"):
                    return TriggeredEvent("qst_TheDarkSpecterOfBiggieSmalls_sweetie1")
                else:
                    return TriggeredEvent("qst_TheDarkSpecterOfBiggieSmalls_sweetie2")
