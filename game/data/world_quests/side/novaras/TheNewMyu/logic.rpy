init python:
    @AppendToAllQuests
    class PrimerQstNewMyu(LogicModule):
        def __init__(self):
            super().__init__()

            self.startDay = GetGameDay() + 1

        def onEnter(self):  
            if GetLocID() in ["azul_safehouse", "azul_safehouse_bedroom"]:
                if GetGameDay() >= self.startDay:
                    return TriggeredEvent("qst_NewMyu_primer")

        def onComplete(self):
            AddItemTo(ShopNovarasGeneral().Items, "qst_sweet_roll", 3)
            QstStart(QstNewMyu)
            return

    @AppendToAllQuests
    class QstNewMyu(BaseQuest):        
        TITLE = _("The New Myu")
        DESCRIPTION = _("Myu seems a little... off? She wants me to buy her some wine and sweet rolls to try, perhaps I should shop around?")
        GOALS = {
                0: QuestStage(_("Get some sweet rolls (3)"),
                    trackTag = "btn_novaras_store_int",
                    hintTxt = _("I should check Novaras General Store. Two or three should suffice.")),
                1: QuestStage(_("Buy a bottle of wine"),
                    trackTag = "btn_novaras_tavern",
                    hintTxt = _("Moving on, Myu wanted some wine. Next stop, the Iron Unicorn.")),
                2: QuestStage(_("Return to Myu"),
                    trackTag = "btn_azul_safehouse",
                    hintTxt = _("I should head back to Azul's safehouse now I've got all the items Myu asked for.")),
                3: QuestStage(_("Let Myu cool down"),
                    trackTag = "btn_azul_safehouse",
                    hintTxt = _("The books never mentioned that liquor and slimelarks don't mix well.\nI should visit Myu later, when she cools down.")),
                4: QuestStage(_("Find Myu"),
                    hintTxt = _("I have walked into Myu while she was having quite a feast. Was she just embarrassed of me seeing her like this when she took off? I don't know.\nShe's out there in the city. I need to find her. Fast.")),
                }

        def __init__(self):
            super().__init__()
            self.XpReward = 350
            self.progress = 0
            
            self.shayWineRevisit = False
            self.haggledWine = False
            self.winePrice = 250
            self.letMyuCoolDown = False
            self.churchFirstTime = True
    
        def OverrideLocBg(self):
            Result = {}
            if GetLocID() == "azul_safehouse_bedroom":
                if self.progress == 3:
                    Result["azul_safehouse_bedroom"] = "bg_azul_bedroom_blood"
                elif self.progress == 4:
                    Result["azul_safehouse_bedroom"] = "bg_azul_bedroom_clean"
            return Result

        def onEnter(self):  
            if self.progress == 0:
                if PlayerItemQty("qst_sweet_roll") >= 2:
                    return TriggeredEvent("qst_NewMyu_0_gotRolls")

            if GetLocID() == "azul_safehouse_bedroom":
                if self.progress == 3:
                    return TriggeredEvent("qst_NewMyu_3_afterCoolDown")

        def onComplete(self):
            while GetItemQty(ShopNovarasGeneral().Items, "qst_sweet_roll") > 0:
                RemItemFrom(ShopNovarasGeneral().Items, "qst_sweet_roll")
            PartyAddChar("myu")

        def extraDialogue(self):
            if self.progress == 1:
                if self.shayWineRevisit:
                    yield ("shay_root", DNode(_("About that wine..."), "qst_NewMyu_1_buyWineShay_revisit"))
                else:
                    yield ("shay_root", DNode(_("Do you have some good wine?"), "qst_NewMyu_1_buyWineShay"))
            if self.progress == 2:
                yield ("myu_root", DNode(_("I have the things you asked for..."), "qst_NewMyu_2_returnMyu"))

        def locationMod(self):
            btnMods = {}
            if self.progress == 3:
                if self.letMyuCoolDown:
                    btnMods["btn_azul_to_bedroom"] = BtnFluffTxt(STR_NAV.TO_BEDROOM, _("I should check up on Myu later, when she cools down."))
            if self.progress == 4:
                btnMods["btn_novaras_church"] = BtnJumpLabel(STR_LOC.NOV_CHURCH, "qst_NewMyu_4_findMyuChurch")
            return LocButtonMod(directMods = btnMods)

        def onNoon(self):
            if self.progress == 3:
                self.letMyuCoolDown = False