init python:
    @AppendToAllQuests
    class PrimerTwoEmperors(LogicModule):
        def onEnter(self):  
            if GetLocID() == "mc_house_kitchen":
                if IsDaytime():
                    return TriggeredEvent("qst_TwoEmperors_0", priority = 2)

    @AppendToAllQuests
    class QstTwoEmperors(BaseQuest):
        TITLE = _("A tale of two Emperors")
        DESCRIPTION = _("Emperor Alcott himself has ordered me and Markus to investigate suspicious Demorai activity in the Valley of Death.")
        GOALS = {
            0: QuestStage(_("Meet Markus at the city gates"),   trackTag = "btn_novaras_gates_exit_city", hintTxt = _("Markus should be waiting to join me outside the city gates.")),
            1: QuestStage(_("Head out into the Valley of Death"), hintTxt = _("We have teamed up with Markus and set out for the Valley of Death. I wonder what we will find there...")),
            2: QuestStage(_("Explore the suspicious ruins"),    hintTxt = _("A Demorai trail led us to what seems to be a ruined temple amidst the desert. We should tread carefully.")),
            3: QuestStage(_("Report your findings"),            hintTxt = _("Apparently, the Demorai talk. Me and Markus have seen Some Demorai overlord beating the war drum real loud in an abandoned temple, east of the Valley of Death.\nWe should return to Novaras and report what we have seen."))
            }

        def __init__(self):
            super().__init__()

            self.XpReward = 600
            self.goldReward = 500 # default, can be bartered higher
            self.firstMarkusDialogue = True # markus lines when we talk to them outside city
            self.templeReqEvents = ["clickedRuins","clickedStatue","messedWithWater"]
            self.killedKraken = False # if false at quest end, enables kraken boss revisit thing
            self.onTempleEnterLines = True
            self.tookSyphaHelp = False 
            self.suggestedLevel = 8
            self.IsMain = True

        def onEnterOnce(self):
            if GetLocID() == "novaras_gates":
                if self.progress == 3:
                    return TriggeredEvent("qst_TwoEmperors_3")

        def onEnter(self):  
            if GetLocID()=="demorai_temple_interior":
                if self.onTempleEnterLines == True:
                    return TriggeredEvent("qst_TwoEmperors_1_onRuinsEnter")
                if len(self.templeReqEvents) == 0:
                    return TriggeredEvent("qst_TwoEmperors_2")
            elif GetLocID() == "novaras_dist_army":
                if self.progress == 3:
                    return TriggeredEvent("qst_TwoEmperors_3_guardDebrief")

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_gates":
                if IsDaytime():
                    if self.progress == 0:
                        btnMods["btn_twoEmperorsTalkMarkus"] = BtnJumpLabel(_("Talk to Markus"),"qst_TwoEmperors_meetMarkus_revisitable")
                if self.progress == 3:
                    btnMods["novaras_gates_travel"] = BtnJumpLabel(_("Travel"), "qst_TwoEmperors_needToReportFindings")
            elif GetLocID() == "demorai_temple_interior":
                btnMods["BtnFluffRuins"] = BtnJumpLabel(_("Ruins"), "qst_TwoEmperors_temple_clickableRuins")
                btnMods["BtnFluffStatue"] = BtnJumpLabel(_("Statue"), "qst_TwoEmperors_temple_clickableStatue")
                if not self.killedKraken:
                    btnMods["BtnKrakenWater"] = BtnJumpLabel(_("Water"), "qst_TwoEmperors_temple_clickableWater")
            return LocButtonMod(directMods = btnMods, priority = 1)

        def onStart(self):
            QstComplete(PrimerTwoEmperors)
            QstStart(EventKrishanaDay)
            return

        def onComplete(self):
            BlockWaitGlobal(False)
            QstStart(EventNovarasMarkusTavernTwoEmps)
            WorldMapLocAdd("demorai_temple")
            QstStart(TravelButtonDemoraiTemple)
            if not self.killedKraken:
                QstStart(DemoraiTempleKraken)
            QstStart(DemoraiTempleRevisit)
            QstStart(PrimerCloakOfDarkness)
            QstSetDelay(PrimerCloakOfDarkness, 1)
            if QstIsOver(QstHighFasion):
                QstStart(PrimerBeneathTheShadows)
            return

label qst_TwoEmperors_needToReportFindings:
    "(Not now.)"
    "(I need to report my findings first.)"
    $ LocEnterQ()