init python:
    @AppendToAllQuests
    @RegisterPregModuleFor("nijah")
    class PregNijah(BasePregModule):  
        def __init__(self):
            super().__init__()

            self.CharID = "nijah"
            self.BabyNameRandomList = [_("Zhyan"), _("Vesek"), _("Loharek")]
            self.GaveBirthNotifText = _("Nijah has given birth.")

############## custom vars
            self.sharedNewsOnChild = False
            self.doPostBirthTalk = False

        def PostImpreg(self):
            self.sharedNewsOnChild = False
            return
    
        def PostBirth(self):
            self.doPostBirthTalk = True
            return

        def onEnter(self):  
            if GetLocID() == "nijah_house_lroom":
                if CharIsVisiblyPreg("nijah"):
                    if not self.sharedNewsOnChild:
                        self.sharedNewsOnChild = True
                        if self.NumImpregs == 1:
                            return TriggeredEvent("preg_Nijah_goodNews_intro")
                        elif self.NumImpregs > 1:
                            return TriggeredEvent("preg_Nijah_secondPreg")
                if self.doPostBirthTalk:
                    self.doPostBirthTalk = False
                    return TriggeredEvent("nijah_post_birth_scene")

        def extraDialogue(self):
            if self.NumBirths > 0:
                yield( "nijah_root", DNode(_("How's %s?") % self.LastBornBabyName, "rom_nijah_howIsChild"))
            if CharIsVisiblyPreg("nijah"):
                yield( "nijah_root", DNode(_("How's your belly?"), "rom_nijah_howIsBaby"))