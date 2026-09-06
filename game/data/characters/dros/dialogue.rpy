init python:
    @AppendToAllQuests
    class DialogueDros(LogicModule):
        def __init__(self):
            super().__init__()

            self.shopWorks = False
            self.discount = 0 # altered thru rebirth quest

        def OverrideLocBg(self):
            Result = {}
            if self.shopWorks:
                Result["novaras_clothes_int"] = "bg_clothes_shop_on"
            return Result

        def locationMod(self):
            btnMods = {}
            if self.progress >= 1: # only show dros past firstmeet sequence
                btnMods["talkdros"] = BtnJumpLabel(tra(_("Talk to %s")) % tra(CharGetVar("dros", "name")), "dros_talk")
            return LocButtonMod(directMods = btnMods)

        def onEnter(self):  
            if GetLocID() == "novaras_clothes_int":
                if self.progress == 0:
                    if IsDaytime():
                        if QstIsComplete(QstFromAnotherWorld):
                            return TriggeredEvent("dros_firstmeet")

        def extraDialogue(self):
            yield ("dros_root", DNode(_("I should go."), "dros_bye", nextNode = "DNodeExit", order = -100))

        def onStart(self):
            store.dros_player_ref = store.player_name
            return

##############################
label dros_talk:
    show dros at center
    if QstIsActive(RomanceDros):
        DROS @lewd "H-Hey... I've missed you!"
        DROS @smile "What can I do for you, [dros_player_ref!t]?"
    else:
        if QstIsComplete(QstGracefulRebirth):
            DROS @talk 'Ah! Hello friend, how are you?'
        else:
            DROS 'How can I help?'
    call processDialogue("dros_root") from _call_processDialogue_42
    $ LocEnter()

label dros_bye:
    DROS "Okay."
    return

################################
# firstmeet, also pops High Fashion
label dros_firstmeet:
    call scr_first_meet_dros from _call_scr_first_meet_dros
    scene black with dissolve
    # set progress to 1 to avoid re-triggering this scene
    $ QstSetProgress(DialogueDros, 1)
    $ QstStart(QstHighFasion)
    $ QstSetProgress(QstHighFasion, 1)
    $ LocSet("novaras_dist_market")
    $ LocEnter()