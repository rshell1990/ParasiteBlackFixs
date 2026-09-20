init python:
    def has_malakai_dlc():
        return renpy.loadable("malakai_scr")
    
    @AppendToAllQuests
    class PrimerMalakai(LogicModule):
        def __init__(self, active=True):
            super().__init__()
            self.isActive = active

        def onEnter(self):
            if not has_malakai_dlc():
                return
            if not QstIsComplete(QstTwoEmperors):
                return
            if GetLocID() == "mc_house_bedroom" and not QstIsOver(QstMalakai):
                # call directly instead of returning a TriggeredEvent, so a same-priority
                # competing onEnter (elena/nijah/etc.) can't win the tie-break and silently eat this trigger
                renpy.call("malakai_intro")

    @AppendToAllQuests
    class QstMalakai(BaseQuest):
        TITLE = _("DLC: Malakai")
        DESCRIPTION = _("A mysterious letter was found on my bed saying someone would contact me in my dreams... Surely this is a joke?")
        LABEL = "DLC Quest"
        GOALS = {
            0: QuestStage(_("Sweet dreams..."),
                trackTag = "novaras_mc_bedroom_bed",
                hintTxt = _("go to sleep in your bed")),
        }
        def __init__(self):
            super().__init__()
            self.XpReward = 250

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "mc_house_bedroom" and QstIsComplete(PrimerMalakai) and QstIsActive(QstMalakai):
                btnMods["btn_mc_house_bed"] = BtnJumpLabel(_("Go to sleep?"), "malakai")
            return LocButtonMod(directMods = btnMods)
