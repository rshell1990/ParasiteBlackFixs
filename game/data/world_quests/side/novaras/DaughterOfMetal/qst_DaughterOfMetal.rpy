init python:
    @AppendToAllQuests
    # meeting arlena while supplying drax some bronze
    class QstDaughterOfMetal(BaseQuest):
        TITLE = _("Daughter of Metal")
        DESCRIPTION = _("I wonder if I can get under Arlena's... Fiery attitude.")
        GOALS = {
            0: QuestStage(_("Collect bronze scraps for Drax (20)"), trackTag = "btn_novaras_blacksmith", hintTxt = _("Perhaps helping out Drax will get me closer to her. I can scavenge some bronze scraps from the Demorai lurking out in the Valley of Death. {b}He is only interested in {i}batches of five{/i}{/b}, for whatever reason.")),
            1: QuestStage(_("Visit the Iron Unicorn at night"), trackTag = "btn_novaras_tavern", hintTxt = _("Arlena invited me to spend some quality time at the Iron Unicorn tavern, which she seems to be a regular of.")),
            2: QuestStage(_("Go to the smithy at day"), trackTag = "btn_novaras_blacksmith", hintTxt = _("I should check up on Arlena when she sobers up."))
            }

        def __init__(self):
            super().__init__()

            self.XpReward = 350
            self.suggestedLevel = 3

        def onEnter(self):  
            # stage 1, check if player brought arlena elationships high enough by bringing bronze
            if GetLocID() == "novaras_blacksmith":
                if IsDaytime():
                    if self.progress == 0:
                        if CharGetRel("arlena") >= 3:
                            return TriggeredEvent("DaughterOfMetal_stage_01")
                    if self.progress == 2:
                        return TriggeredEvent("DaughterOfMetal_stage_03")
            # stage 2, visit arlena in tavern. this is split into two progress checks to move locations        
            elif GetLocID() == "novaras_tavern":
                if not IsDaytime():
                    if self.progress == 1:
                        return TriggeredEvent("DaughterOfMetal_stage_02")
            elif GetLocID() == "novaras_dist_market":
                if self.progress == 1.2:
                    return TriggeredEvent("DaughterOfMetal_stage_02_2")

        def onComplete(self):
            DialogueArlena().canEnterRoom = True
            DialogueArlena().dayUnlocked = GetGameDay()
            QstStart(PrimerADazzlingTail)

label DaughterOfMetal_stage_01:
    call qst_DaughterOfMetal_01 from _call_qst_DaughterOfMetal_01
    $ QstSetProgress(QstDaughterOfMetal, 1)
    $ LocEnterQ()

label DaughterOfMetal_stage_02:
    call qst_DaughterOfMetal_02 from _call_qst_DaughterOfMetal_02
    $ QstSetProgress(QstDaughterOfMetal, 1.2)
    $ LocSet("novaras_dist_market")
    $ LocEnterQ()

label DaughterOfMetal_stage_02_2:
    call qst_DaughterOfMetal_02_2 from _call_qst_DaughterOfMetal_02_2
    $ QstSetProgress(QstDaughterOfMetal, 2)
    $ LocSet("novaras_dist_farm")
    $ LocEnterQ()

label DaughterOfMetal_stage_03:
    call qst_DaughterOfMetal_03 from _call_qst_DaughterOfMetal_03
    $ QstComplete(QstDaughterOfMetal)
    $ LocEnterQ()