init python:
    @AppendToAllQuests
    @RegisterPregModuleFor("jackal_girl")
    class PregJackalGirl(BasePregModule):  
        def __init__(self):
            super().__init__()

            self.CharID = "jackal_girl"
            self.GaveBirthNotifText = _("Jackal girl has given birth.")

########### custom vars
            self.NumBabiesShown = 0 # triggers that camp visit scene
    