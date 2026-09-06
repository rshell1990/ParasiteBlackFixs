init python:
    @AppendToAllQuests
    class DrosInBordello(LogicModule): # activated as reward for high fashion
        def __init__(self):
            super().__init__()

            self.bordelloCooldown = 5
            self.bordelloNight = False
            self.bordelloFirstMeet = True
            self.bordelloFirstFuck = True # ticked off, prompts romance dialogue if pre-tf

        def onNoon(self):
            self.bordelloCooldown -= 1
            self.bordelloNight = False
            if self.bordelloCooldown == 0:
                self.bordelloCooldown = 4
                self.bordelloNight = True

        def locationMod(self):
            btnMods = {}
            if self.bordelloNight:
                if self.bordelloFirstMeet:
                    btnMods["dros_bordello_talk_btn"] = BtnJumpLabel(_("Dros?"), "dros_firstmeet_bordello")
                else:
                    btnMods["dros_bordello_talk_btn"] = BtnJumpLabel(tra(_("Talk to %s")) % tra(CharGetVar("dros", "name")), "dros_talk_bordello")

            return LocButtonMod(directMods = btnMods)

        def onEnter(self):  
            if GetLocID() == "novaras_bordello_interior":
                if self.bordelloNight:
                    CharSetClothes("dros", "dress")
                    if self.bordelloFirstMeet:
                        return TriggeredEvent("dros_firstmeet_bordello")
            # we're setting dros' clothes to normal *on pleasure district* not the exterior, 
            # otherwise it instantly makes him shift into normal clothes (visibly) on exiting bordello
            elif GetLocID() == "novaras_dist_pleasure":
                CharSetClothes("dros", "normal")

        def extraDialogue(self):
            yield ("dros_bordello_root", DNode(_("I've gotta go."), "dros_bordello_bye", nextNode = "DNodeExit", order = -100))
            if CharGetVar("dros", "Transformed") == False:
                if self.bordelloFirstFuck:
                    yield ("dros_bordello_root",DNode(_("Let's have some fun."), "rom_Dros_preTf_lines"))
                else:
                    yield ("dros_bordello_root",DNode(_("Let's have some fun."), "dros_preTf_payMenu"))
            else:
                yield ("dros_bordello_root",DNode(_("Let's have some fun."), "dros_postTf_payMenu"))
        
        def onComplete(self):
            QstComplete(EventBrothelAd)
            return

###########################
label dros_talk_bordello:
    show dros at center

    if QstIsActive(RomanceDros):
        DROS @smile "Ahh! There you are!"
        DROS @lewd "I was um... Worried you wouldn't show up." #Dialogue for first time
    else:
        DROS "Yeah?"
    call processDialogue("dros_bordello_root") from _call_processDialogue_44
    $ LocEnter()

label dros_bordello_bye:
    DROS "Okay, goodbye."
    return