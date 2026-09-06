init python:
    notesLib["VesRomance0"] = Note(
        _("Ves is out hunting"),
        _("I tried to have some time alone with Ves, but she went out hunting. Perhaps I should try catch up with her some other time."),
        journal_flag_delayed = True)
    notesLib["VesRomance1"] = Note(
        _("Heated argument"),
        _("Our recent interaction with Ves escalated out of control. I should visit her after she cools down."),
        journal_flag_delayed = True)
    notesLib["VesRomance2"] = Note(
        _("Visit Ves another time"),
        _("That was better. I've managed to make it up for the last time. I should visit Ves after a while."),
        journal_flag_delayed = True)
    notesLib["VesRomance3"] = Note(
        _("Ves needs some space"),
        _("I think I should slow my courting down. Perhaps visit Ves another time. Maybe try after dark?"))
    notesLib["VesHelpCamp"] = Note(
        _("Ves could use some help"),
        _("Ves wants to set up some defences around her camp. I could lend a hand."))
    notesLib["VesLingerie"] = Note(
        _("A gift for Ves"),
        _("I should get Ves a gift. A set of lingerie?"))
    notesLib["VesLingerieInProg"] = Note(
        _("A gift for Ves"),
        _("Dros is working on a set of lingerie for Ves. I should pick it up in a couple days."),
        journal_flag_delayed = True)
    notesLib["VesLingerieReady"] = Note(
        _("A gift for Ves"),
        _("I have picked up a set of a lingerie. Now, gonna give it to Ves."))
    @AppendToAllQuests
    # progress 12 - sexytimes unlock stage
    class RomanceVes(LogicModule):
        def __init__(self):
            super().__init__()

            self.wearsLing = False
            self.lingerie = 0 # 0 is "get it", 1 "in progress", 2 ready, 3 in inv, 4 brought to ves"
            self.cooldownDay = -1 # used multiple times

        def extraDialogue(self):
            if self.progress == 0:
                yield ("ves_root",DNode(_("I’ve come to see how you are..."), "rom_Ves_0_checkup"))
            if self.progress == 4:
                yield ("ves_root",DNode(_("Do you still need help with your camp?"), "rom_Ves_2_FortAndCook_Rev"))
            if self.progress == 9:
                yield ("ves_root",DNode(_("Let's go hunting!"), "rom_Ves_4_HuntPitchRev"))
            if self.progress == 12:
                if IsInTimeFrame(TIME_AFTERNOON,TIME_NIGHT):
                    yield ("ves_root",DNode(_("Let's spend the night together."),"rom_Ves_SpendNight"))
                else:
                    yield ("ves_root",DNode(_("Let's spend the night together."),"rom_Ves_SpendNightWrong"))

                yield ("ves_root",DNode(_("Wanna have some fun?"),"rom_Ves_HaveSomeFun"))

                if self.lingerie == 0:
                    yield ("dros_root",DNode(_("I need a set of lingerie for an orc lady."),"rom_Ves_7_GetLing"))
                if self.lingerie == 1:
                    yield ("dros_root",DNode(_("About that orc lingerie..."),"rom_Ves_7_GetLingInProgress"))
                if self.lingerie == 2:
                    yield ("dros_root",DNode(_("I've come to pick up that orc lingerie."),"rom_Ves_7_GetLingReady"))
                if self.lingerie == 3:
                    yield ("ves_root",DNode(_("I have brought you something..."),"rom_Ves_7_GetLingGive"))

        def onEnter(self):
            if GetLocID() == "ves_tent_int":
                if self.progress == 1:
                    return TriggeredEvent("rom_Ves_1_GetMeds")
                elif self.progress == 8:
                    return TriggeredEvent("rom_Ves_4_HuntPitch")
                elif self.progress == 11:
                    if not IsDaytime():
                        return TriggeredEvent("rom_Ves_6_Drunk")

            elif GetLocID() == "ves_camp":
                if self.progress == 6:
                    return TriggeredEvent("rom_Ves_3_AfterHeat")
                elif self.progress == 11:
                    if not IsDaytime():
                        return TriggeredEvent("rom_Ves_6_Drunk")

        def locationMod(self):
            btnMods = {}
            if GetLocID() in ["ves_camp", "ves_tent_int"]:
                if self.progress == 5:
                    btnMods["ves_tent_int_button"] = BtnDisabled()
                if self.progress == 7:
                    btnMods["ves_tent_int_button"] = BtnDisabled()
            return LocButtonMod(directMods = btnMods)

        def onMidnight(self):
            if self.progress == 5:
                if self.cooldownDay != -1:
                    if GetGameDay() >= self.cooldownDay:
                        self.setProgress(6)
                        self.cooldownDay = -1
            elif self.progress == 7:
                if self.cooldownDay != -1:
                    if GetGameDay() >= self.cooldownDay:
                        self.setProgress(8)
                        self.cooldownDay = -1

            elif self.progress == 10:
                if self.cooldownDay != -1:
                    if GetGameDay() >= self.cooldownDay:
                        self.setProgress(11)
                        self.cooldownDay = -1

            elif self.progress == 12:
                if self.lingerie == 1:
                    if self.cooldownDay != -1:
                        if GetGameDay() >= self.cooldownDay:
                            self.lingerie += 1
                            self.cooldownDay = -1
