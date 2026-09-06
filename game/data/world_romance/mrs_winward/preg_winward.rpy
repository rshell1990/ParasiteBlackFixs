init python:
    @AppendToAllQuests
    @RegisterPregModuleFor("mrs_winward")
    class PregWinward(BasePregModule):  
        def __init__(self):
            super().__init__()

            self.CharID = "mrs_winward"
            self.GaveBirthNotifText = _("Mrs. Winward has given birth.")

############### custom vars
            self.ShareFirstImpregNews =     False
            self.ShareSecondImpregNews =    False

            self.DoFirstBabyScene =     False
            self.DoRepBabyScene =       False

            self.BabyName1Default = _("Rysa")
            self.BabyName2Default = _("Kylan")

            self.BabyName1 = None
            self.BabyName2 = None

        def PostImpreg(self):
            if self.NumImpregs == 1:
                self.ShareFirstImpregNews = True
            elif self.NumImpregs >= 2:
                self.ShareSecondImpregNews = True
            return

        def PostBirth(self):
            if self.NumBirths == 1:
                self.DoFirstBabyScene = True
            elif self.NumBirths >= 2:
                self.DoRepBabyScene = True
            return

        def onEnter(self):  
            if GetLocID() == "novaras_tanner_shop":
                if CharIsVisiblyPreg("mrs_winward"):
                    if self.ShareFirstImpregNews:
                        if not QstIsOver(EventFirstImpreg):
                            QstStart(EventFirstImpreg)
                        self.ShareFirstImpregNews = False
                        if RomanceWinward().RomanceVariant == "invest":
                            return TriggeredEvent("rom_winward_invest_first_impreg", priority = 1)
                        elif RomanceWinward().RomanceVariant == "divorce":
                            return TriggeredEvent("rom_winward_divorce_murder_first_impreg", priority = 1)
                        elif RomanceWinward().RomanceVariant == "control":
                            return TriggeredEvent("rom_winward_control_impreg_first", priority = 1)
                        elif RomanceWinward().RomanceVariant == "murder":
                            return TriggeredEvent("rom_winward_murder_impreg_first", priority = 1)
                        elif RomanceWinward().RomanceVariant == "pimp":
                            return TriggeredEvent("rom_winward_pimp_rep_impreg", priority = 1)

                    elif self.ShareSecondImpregNews:
                        self.ShareSecondImpregNews = False
                        if RomanceWinward().RomanceVariant == "invest":
                            return TriggeredEvent("rom_winward_invest_rep_impreg", priority = 1)
                        elif RomanceWinward().RomanceVariant == "divorce":
                            return TriggeredEvent("rom_winward_divorce_rep_impreg", priority = 1)
                        elif RomanceWinward().RomanceVariant == "control":
                            return TriggeredEvent("rom_winward_control_impreg_rep", priority = 1)
                        elif RomanceWinward().RomanceVariant == "murder":
                            return TriggeredEvent("rom_winward_murder_impreg_rep", priority = 1)
                        elif RomanceWinward().RomanceVariant == "pimp":
                            return TriggeredEvent("rom_winward_pimp_rep_impreg", priority = 1)

                if self.NumBirths > 0:
                    if self.DoFirstBabyScene:
                        self.DoFirstBabyScene = False
                        if RomanceWinward().RomanceVariant == "invest":
                            return TriggeredEvent("rom_winward_invest_first_birth", priority = 1)
                        elif RomanceWinward().RomanceVariant == "divorce":
                            return TriggeredEvent("rom_winward_divorce_first_birth", priority = 1)
                        elif RomanceWinward().RomanceVariant == "control":
                            return TriggeredEvent("rom_winward_control_birth_first", priority = 1)
                        elif RomanceWinward().RomanceVariant == "murder":
                            return TriggeredEvent("rom_winward_murder_birth_first", priority = 1)
                        elif RomanceWinward().RomanceVariant == "pimp":
                            return TriggeredEvent("rom_winward_pimp_first_birth", priority = 1)
                    elif self.DoRepBabyScene:
                        self.DoRepBabyScene = False
                        if RomanceWinward().RomanceVariant == "invest":
                            return TriggeredEvent("rom_winward_invest_rep_birth", priority = 1)
                        elif RomanceWinward().RomanceVariant == "divorce":
                            return TriggeredEvent("rom_winward_divorce_rep_birth", priority = 1)
                        elif RomanceWinward().RomanceVariant == "control":
                            return TriggeredEvent("rom_winward_control_birth_rep", priority = 1)
                        elif RomanceWinward().RomanceVariant == "murder":
                            return TriggeredEvent("rom_winward_murder_birth_rep", priority = 1)
                        elif RomanceWinward().RomanceVariant == "pimp":
                            return TriggeredEvent("rom_winward_pimp_rep_birth", priority = 1)
