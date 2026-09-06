init python:
    @AppendToAllQuests
    @RegisterPregModuleFor("lizard_red")
    class PregLizardRed(BasePregModule):     
        def __init__(self):
            super().__init__()

            self.CharID = "lizard_red"
            self.GaveBirthNotifText = _("Red skalith has given birth.")
            return

    @AppendToAllQuests
    @RegisterPregModuleFor("lizard_green")
    class PregLizardGreen(BasePregModule):  
        def __init__(self):
            super().__init__()

            self.CharID = "lizard_green"
            self.GaveBirthNotifText = _("Green skalith has given birth.")
            return

    @AppendToAllQuests
    @RegisterPregModuleFor("lizard_blue")
    class PregLizardBlue(BasePregModule):     
        def __init__(self):
            super().__init__()

            self.CharID = "lizard_blue"
            self.GaveBirthNotifText = _("Blue skalith has given birth.")
            return