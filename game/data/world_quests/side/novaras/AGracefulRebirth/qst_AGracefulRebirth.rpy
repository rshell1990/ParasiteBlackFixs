init python:
    notesLib["DrosMoreWomanly"] = Note(
        _("A womanly Dros"),
        _("Dros has asked for your help to become more 'womanly'."))

    @AppendToAllQuests
    class PrimerGracefulRebirth(LogicModule):
        def extraDialogue(self):
            yield ("dros_bordello_root",DNode(_("I will help you become more 'womanly'."), "dros_0_womanly_revisit"))
            yield ("dros_root",DNode(_("I will help you become more 'womanly'."), "dros_0_womanly_revisit"))

        def onStart(self):
            NoteUnlock("DrosMoreWomanly")

        def onComplete(self):
            NoteLock("DrosMoreWomanly")

    @AppendToAllQuests
    class QstGracefulRebirth(BaseQuest):
        TITLE = _("A Graceful Rebirth")
        DESCRIPTION = _("I have agreed to help Dros step over into his... Feminine side.")
        SIMPLE_GOALS = False
        GOALS = {
            0: QuestStage(_("Speak to Sister Divine"),          trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("Dros' intuition led him to the Palam tower, however, the mages turned down his plea for help. I should investigate.")),
            1: QuestStage(_("Get the herbs for the ritual"),    trackTag = "btn_novaras_store_int", hintTxt = _("Sister Divine will need a collection of special herbs to conduct the ritual. I should try a merchant.")),
            1.5: QuestStage(_("Deal with Jurgen"),              trackTag = "btn_novaras_tavern",    hintTxt = _("I could help Lucius Mal deal with a strung-up guard in exchange for the herbs. The guard goes by the name Jurgen, I can find him in the Iron Unicorn.")),
            2: QuestStage(_("Bring five slimelark remains to Sister Divine"), hintTxt = _("I should look for slimelarks near a lake.")),
            3: QuestStage(_("Warn Dros about the ritual"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("The transformation ritual is a dangerous one. I should make sure Dros wants it.")),

            # appears when you do all the three things
            4: QuestStage(_("Report to Sister Divine"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("I should speak to Sister Divine about my progress.")),

            5: QuestStage(_("Get Dros"), hintTxt = _("Sister Divine has everything she needs. Now, gotta bring Dros over."))
        }
        def __init__(self):
            super().__init__()

            self.XpReward = 400
            self.warnedDros = False
            self.broughtSlimelarkRemains = False
            self.spokeAboutHerbs = False
            self.boughtHerbs = False
            self.spokeAboutJurgen = False
            self.jurgenActive = False
            self.jurgenGone = False
            self.knowJurgen = False
            self.spokeToJurgenBoutMerchants = False
            self.gotHerbs = False
            self.tookAmirasFromNijah = False
            self.tookRazaFromFawha = False
            self.getHerbsDay = -1
            self.getHerbsDelay = 2
            self.malHasHerbs = False
            self.divinePointsList = {"dros","herbs","remains"}
            self.suggestedLevel = 7

        def extraDialogue(self):
            if self.progress == 0:
                yield ("divine_root", DNode(_("Dros has a problem you might be able to solve..."), "dros_1_at_palam", order = 100))
            if self.progress == 1:
                yield ("divine_root", DNode(_("About the ritual..."), "dros_3_returnToDivine", order = 100))
            if self.progress == 1 and not self.warnedDros:
                yield ("dros_bordello_root", DNode(_("There is a magic ritual that might make you more 'womanly', but..."), "dros_warn", order = 100))
                yield ("dros_root", DNode(_("There is a magic ritual that might make you more 'womanly', but..."), "dros_warn", order = 100))
            if self.progress == 1 and not self.spokeAboutHerbs:
                yield ("luciusmal_root", DNode(_("I need some special herbs."),"dros_2_herbs_at_shop", order = 100))
            if self.progress == 1 and self.spokeAboutHerbs:
                if self.boughtHerbs:
                    if not self.gotHerbs:
                        if self.malHasHerbs:
                            yield ("luciusmal_root", DNode(_("About these herbs..."),"dros_2_herbs_at_shop_arrived", order = 100))
                        else:
                            yield ("luciusmal_root", DNode(_("About these herbs..."),"dros_2_herbs_at_shop_waiting", order = 100))
                else:
                    yield ("luciusmal_root", DNode(_("About these herbs..."),"dros_2_herbs_at_shop_revisit", order = 100))
                if self.jurgenActive and not self.jurgenGone:
                    if not self.tookAmirasFromNijah:
                        if QstIsComplete(QstDamzelInDiztrezz):
                            yield ("nijah_root", DNode(_("Do you have Amira's tears?"), "jurgen_2_get_amira_nijah", order = 100))
                    if not self.tookRazaFromFawha:
                        yield ("fawha_root", DNode(_("Do you have some Raza?"), "jurgen_2_get_raza_fawha", order = 100))
            if self.progress == 2:
                yield ("dros_root",DNode(_("Sister Divine is ready for you now."), "dros_4_getDros", order = 100))
        def onMidnight(self):
            if self.boughtHerbs:
                if self.getHerbsDay == -1:
                    self.getHerbsDay = GetGameDay() + self.getHerbsDelay
                if GetGameDay() == self.getHerbsDay:
                    self.malHasHerbs = True

        def locationMod(self):
            btnMods = {}
            if QstGracefulRebirth().jurgenActive:
                if not QstGracefulRebirth().jurgenGone:
                    if QstGracefulRebirth().knowJurgen:
                        btnMods["jurgen_tavern_talk_btn"] = BtnJumpLabel(_("Talk to Jurgen"),"jurgen_0_tavern_revisit")
                    else:
                        btnMods["jurgen_tavern_talk_btn"] = BtnJumpLabel(_("Talk to the Guard"),"jurgen_0_tavern")
            return LocButtonMod(directMods=btnMods)