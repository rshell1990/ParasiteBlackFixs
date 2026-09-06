init python:
    # a logic module that fires an event that initiates the quest
    @AppendToAllQuests
    class PrimerBiteBark(LogicModule):
        def onEnter(self):  
            if GetLocID() == "mc_house_kitchen":
                if IsDaytime():
                    if QstIsComplete(QstFromAnotherWorld):
                        if not QstIsComplete(QstBiteBark):
                            if QstIsComplete(QstProperReunion):
                                if QstIsComplete(QstTheBloodhound):
                                    return TriggeredEvent("qst_BiteBark_0_startEvent")

    # quest itself
    # prog: 0 visit kennels, 1 buy a pet, 2 return home w/pet
    @AppendToAllQuests
    class QstBiteBark(BaseQuest):
        TITLE = _("All Bite No Bark")
        DESCRIPTION = _("[regina_ref_cap!t] suggests I get myself a pet.")
        GOALS = {
            0: QuestStage(_("Visit the kennels"), 
                trackTag = "btn_kennels", 
                hintTxt = _("Well, first place coming to mind is, army district kennels.")),
            1: QuestStage(_("Buy a blue wolf"), 
                trackTag = "btn_kennels", 
                hintTxt = _("I've spoken to the kennel master and quickly stumbled upon a curious animal... A blue wolf with a reputation. Kennel master asks for 750 gold in exchange for her.")),
            2: QuestStage(_("Return home"), 
                trackTag = "btn_mc_house", 
                hintTxt = _("Well, now that I've got my new 'companion' with me, I better go show her to [regina_ref!t].")),
            3: QuestStage(_("Feed the Dog"), 
                trackTag = ["btn_novaras_market_stalls", "btn_novaras_market_stalls_butcher"], 
                hintTxt = _("My new 'companion' is hungry, I'm sure I can find something special for her at the market.")),
            4: QuestStage(_("Find your pet"), 
                hintTxt = _("And just like that, my 'companion' took off. I should check around the city, she couldn't have gone far.")),
            5: QuestStage(_("Return home"), 
                trackTag = "btn_mc_house", 
                hintTxt = _("I've found my troublesome companion. I should return home now.")),
            6: QuestStage(_("Get your 'pet' dressed"), 
                hintTxt = _("Turns out, my companion is something more of a plain blue wolf. I need to get some proper clothes for {i}her{/i}.")),
            7: QuestStage(_("Return to Dros in a couple days"), 
                trackTag = "btn_novaras_clothes", 
                hintTxt = _("I have commissioned an outfit for Elena. Dros should have it ready soon."))
        }

        def __init__(self):
            super().__init__()
        
            self.XpReward = 350
            self.DrosRevisit = False
            self.DrosArmorDayToComplete = 0
            self.priority = 1

        def extraDialogue(self):
            # add lines to ask bout wolf
            if self.progress == 4:
                yield ("regina_root",   DNode(_("Have you seen a blue wolf anywhere?"), "qst_BiteBark_5_SeenWolfRegina"))
                yield ("luciusmal_root",DNode(_("Have you seen a blue wolf anywhere?"), "qst_BiteBark_5_SeenWolfLucius"))
                yield ("arlena_root",   DNode(_("Have you seen a blue wolf anywhere?"), "qst_BiteBark_5_SeenWolfArlena"))
                yield ("divine_root",   DNode(_("Have you seen a blue wolf anywhere?"), "qst_BiteBark_5_SeenWolfDivine"))
            elif self.progress == 6:
                if self.DrosRevisit:
                    yield ("dros_root", DNode(_("About armour for Elena..."), "qst_BiteBark_7_DrosLinesRevisit"))
                if not self.DrosRevisit and QstIsComplete(QstHighFasion):
                    yield ("dros_root", DNode(_("I was wondering if you would be able to make some light armour for a companion of mine."), "qst_BiteBark_7_DrosLines"))
                if not self.DrosRevisit and QstIsActive(QstHighFasion):
                    yield ("dros_root", DNode(_("I was wondering if you would be able to make some light armour for a companion of mine."), "qst_BiteBark_7_DrosNeedCrystal"))
            elif self.progress == 7:
                if GetGameDay() >= self.DrosArmorDayToComplete:
                    yield ("dros_root", DNode(_("About armour for Elena..."), "qst_BiteBark_7_DrosLinesArmourDone"))
                else:
                    yield ("dros_root", DNode(_("About armour for Elena..."), "qst_BiteBark_7_DrosLinesComeBackLater"))

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_army":
                if IsDaytime():
                    btnMods["btn_kennels"] = BtnChangeLoc(STR_LOC.NOV_KENNELS, "novaras_kennels")
            # talkable kennelmaster stage 0-1
            elif GetLocID() == "novaras_kennels":
                if IsDaytime():
                    if self.progress == 1:
                        btnMods["kennelmaster_talk_btn"] = BtnJumpLabel(_("Talk to the Kennel Master"),"qst_BiteBark_2_RepTalkToKennelMaster")
                    if self.progress == 4:
                        btnMods["kennelmaster_talk_btn"] = BtnJumpLabel(_("Talk to the Kennel Master"),"qst_BiteBark_5_SeenWolfKennelMaster")
            # trader for feed the dog, st 3
            elif GetLocID() == "novaras_market_stalls":
                if IsDaytime():
                    if self.progress == 3:
                        btnMods["btn_novaras_market_stalls_butcher"] = BtnJumpLabel(_("Talk to the Butcher"), "qst_BiteBark_4_BuyMeat")
            return LocButtonMod(directMods = btnMods, priority = 2)

        def onEnter(self):
            # as opposed to tons of if-checks, maybe this approach is saner?
            # what we do is, first statically define all possible events
            Events = [
                # loc_id, progress, [predicates], label, priority
                ("novaras_kennels", 0,  [IsDaytime], "qst_BiteBark_1_TalkToKennelMaster", 0),
                ("mc_house_kitchen", 2, [IsDaytime], "qst_BiteBark_3_ReturnToRegina", 0),
                ("mc_house_kitchen", 5, [], "qst_BiteBark_6_McRoomResolution", 0),
                ("mc_house_kitchen", 8, [], "qst_BiteBark_8_ReturnWithClothes", 0),
                ("novaras_soothsayer_cabin", 4, [], "qst_BiteBark_5_FoundWolfAtBaba", 100),
            ]

            # then we iterate over all events and evaluate them
            for LocID, Progress, Predicates, Label, Priority in Events:
                if GetLocID() == LocID:
                    if self.progress == Progress:
                        for Predicate in Predicates:
                            if not Predicate():
                                continue
                        return TriggeredEvent(Label, Priority)
            

        def onStart(self):
            QstStart(EventElenaWhoIsNijah)

        def onComplete(self):
            CharMeet("elena", Silent = True)
            QstStart(PrimerSharedInThorns)
            QstComplete(EventElenaWhoIsNijah)
            return