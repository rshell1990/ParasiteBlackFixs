init python:
    @AppendToAllQuests
    class QstRavenousJelly(BaseQuest):        
        TITLE = _("The Ravenous Jelly")
        DESCRIPTION = _("I have to feed a slimelark I have snatched from the lake.\nWonder if stashing it under my bed was a good idea...")
        GOALS = {
                0: QuestStage(_("Buy some meat from the butcher"),
                    trackTag = "btn_novaras_market_stalls",
                    hintTxt = _("There should be a butcher shop at the market.")),
                1: QuestStage(_("Feed the slime"),
                    trackTag = "btn_mc_house",
                    hintTxt = _("Time to feed my little friend.")),
                2: QuestStage(_("Keep feeding the slime"),
                    trackTag = "btn_novaras_market_stalls",
                    hintTxt = _("The slime seems to grow as I feed it. I should keep supplying it with fresh meat from the market, see what happens.")),
                3: QuestStage(_("Find a new home for Myu"),
                    trackTag = "btn_azul_safehouse",
                    hintTxt = _("I should check if Azul's safehouse was cleared out. It could be a perfect place to keep Myu at, for a while.")),
            }

        def __init__(self):
            super().__init__()

            self.XpReward = 300
            self.fedToday = False
            self.growStage = 1 # 1-4 was it
            self.showMyuScene = False

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "mc_house_bedroom":
                btnMods["btn_slime_jar"] = BtnJumpLabel(_("Inspect the slime"),"qst_ravenJelly_inspectSlime")
            return LocButtonMod(directMods = btnMods)

        def OverrideLocBg(self):
            Result = {}
            if self.showMyuScene:
                Result["azul_safehouse"] = "bg_azul_room_clean"
                Result["azul_safehouse_bedroom"] = "bg_azul_bedroom_clean"
            return Result

        def onEnter(self):  
            if GetLocID() == "mc_house_bedroom":
                if self.showMyuScene:
                    return TriggeredEvent("qst_ravenJelly_enterMyu")

        def onMidnight(self):
            if self.fedToday:
                self.growStage += 1
                self.fedToday = False
                if self.growStage == 5:
                    self.showMyuScene = True

        def onComplete(self):
            QstStart(HouseLockAzul)
            QstStart(DialogueMyu)
            QstStart(QstHumanExp)
            return