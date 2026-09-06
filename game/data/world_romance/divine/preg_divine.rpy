init python:
    @AppendToAllQuests
    @RegisterPregModuleFor("divine")
    class PregDivine(BasePregModule):  
        def __init__(self):
            super().__init__()

            self.CharID = "divine"
            self.GaveBirthNotifText = _("Sister Divine has given birth.")
            return