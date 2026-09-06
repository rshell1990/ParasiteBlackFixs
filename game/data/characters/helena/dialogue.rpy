init python:
    @AppendToAllQuests
    class DialogueHelena(LogicModule):
        def locationMod(self):
            btnMods = {}
            if self.progress == 1:
                if GetLocID() == "novaras_bordello_interior":
                    btnMods["helena_talk_btn"] = BtnJumpLabel(_("Talk to Helena"), "nov_helena_obj_talk")
            return LocButtonMod(directMods = btnMods)

        def onEnter(self):  
            if GetLocID() == "novaras_bordello_interior":
                if self.progress == 0:
                    return TriggeredEvent("nov_helena_firstmeet")

        def extraDialogue(self):
            yield ("helena_root", DNode(_("What services do you offer Helena?"), "nov_helena_services"))
            yield ("helena_root", DNode(_("Can you tell me a bit about yourself?"), "nov_helena_about"))
            yield ("helena_root", DNode(_("That is all, thank you."), "nov_helena_bye", nextNode = "DNodeExit", order = -100))

label nov_helena_obj_talk:
    show helena at center with dissolve
    HELENA @talk "Hello again, [player_name!t]."
    call processDialogue("helena_root") from _call_processDialogue_29
    $ LocEnter()