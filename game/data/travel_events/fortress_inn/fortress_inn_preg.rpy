init python:
    @AppendToAllQuests
    @RegisterPregModuleFor("betty")
    class PregFortressInnBetty(BasePregModule):
        def __init__(self):
            super().__init__()

            self.CharID = "betty"
            self.GaveBirthNotifText = _("Betty has given birth.")

            self.BabyName = _("Karnesh")

            ############## custom vars
            self.ShareImpregNews    = False
            self.DoBabyScene        = False
            return

        def PostImpreg(self):
            # 1st time
            if self.NumImpregs == 1:
                self.ShareImpregNews = True
            elif self.NumImpregs > 1:
                self.ShareImpregNews = True
            return

        def PostBirth(self):
            if self.NumBirths >= 1:
                self.DoBabyScene = True
            return

    @AppendToAllQuests
    @RegisterPregModuleFor("vivian")
    class PregFortressInnVivian(BasePregModule):
        def __init__(self):
            super().__init__()

            self.CharID = "vivian"
            self.GaveBirthNotifText = _("Vivian has given birth.")

            self.BabyName = _("Kara")

            ############## custom vars
            self.ShareImpregNews    = False
            self.DoBabyScene        = False
            return

        def PostImpreg(self):
            # 1st time
            if self.NumImpregs == 1:
                self.ShareImpregNews = True
            elif self.NumImpregs > 1:
                self.ShareImpregNews = True
            return

        def PostBirth(self):
            if self.NumBirths >= 1:
                self.DoBabyScene = True
            return

    @AppendToAllQuests
    @RegisterPregModuleFor("lucy")
    class PregFortressInnLucy(BasePregModule):
        def __init__(self):
            super().__init__()

            self.CharID = "lucy"
            self.GaveBirthNotifText = _("Lucy has given birth.")

            self.BabyName = _("Viska")

            ############## custom vars
            self.ShareImpregNews    = False
            self.DoBabyScene        = False
            return

        def PostImpreg(self):
            # 1st time
            if self.NumImpregs == 1:
                self.ShareImpregNews = True
            elif self.NumImpregs > 1:
                self.ShareImpregNews = True
            return

        def PostBirth(self):
            if self.NumBirths >= 1:
                self.DoBabyScene = True
            return
