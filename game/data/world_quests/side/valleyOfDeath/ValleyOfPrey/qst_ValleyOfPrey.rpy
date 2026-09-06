init python:
    # this one is completely linear
    @AppendToAllQuests
    class QstValleyOfPrey(BaseQuest):
        GOALS = {
            0: QuestStage(_("Accompany Ves on the hunt"), hintTxt=_("We've set out into the desert, looking for Skorn.")),
            1: QuestStage(_("Kill the Bazark") ,hintTxt=_("We have stumbled upon Bazark, a giant worm. Gotta fight our way through this one!")),
            2: QuestStage(_("Return to Ves camp") ,hintTxt=_("I have acquired the power crystal Dros wanted. I should take it to his clothes' store now."))}

        TITLE = _("Valley of Prey")
        DESCRIPTION = _("I have joined Ves on a hunt. Wonder what the day brings...")

        def __init__(self):
            super().__init__()

            self.XpReward = 900
            self.suggestedLevel = 9