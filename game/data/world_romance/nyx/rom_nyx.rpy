init python:
    notesLib["romanceNyxStart"] = Note(
        _("Confront Nyx"), 
        _("I should try to talk to Nyx again in a couple of days about what happened during the meeting with the slave master."))
    notesLib["romanceNyxDominant1"] = Note(
        _("Go to Nyx"), 
        _("It seems I've revealed an interesting facet of Nyx. I'm curious to see where this will lead."))
    notesLib["romanceNyxDominant2"] = Note(
        _("Check on Nyx"), 
        _("Maybe I pushed her too hard. I should check on Nyx in the morning."),
        journal_flag_delayed = True)
    notesLib["romanceNyxDominant3"] = Note(
        _("Go to Nyx's room at night"), 
        _("I can't wait to meet Nyx in her room tonight."))

    notesLib["romanceNyxLove1"] = Note(
        _("Check on Nyx"), 
        _("I hope I didn't screw it up with my surprise kiss. I should check on her tomorrow."),
        journal_flag_delayed = True)
    notesLib["romanceNyxLoveUnicorn"] = Note(
        _("Date Nyx"), 
        _("I have a date with Nyx at the Iron Unicorn in the evening."))

    @AppendToAllQuests
    class RomanceNyx(LogicModule):
        MANUAL_DELAY = True
        def __init__(self):
            super().__init__()

            self.route = "" # "dominant" or "love"
            self.progress = 0 # 0 is initial, 1 through 4 is stages (4 last)
            self.guardSilenced = None

        def onStart(self):
            NoteUnlock("romanceNyxStart")
            QstStart(PrimerTheComingStorm)
            return

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_tavern":
                if not IsDaytime():
                    if self.progress == 2:
                        btnMods["unicorn_date_btn"] = BtnJumpLabel(_("Wait for Captain Nyx to join you..."), "rom_nyx_love_unicorn_date")
            return LocButtonMod(directMods = btnMods)

        def onEnter(self):
            if GetLocID() == "novaras_fort_seb_captains_office":
                if self.progress == 0:
                    if QstDelayCheck(self):
                        return TriggeredEvent("rom_nyx_start")
                if self.route == "dominant":
                    if self.progress == 1:
                        return TriggeredEvent("rom_nyx_dominant_1")
                    if self.progress == 2:
                        return TriggeredEvent("rom_nyx_dominant_2")
                elif self.route == "love":
                    if self.progress == 1:
                        return TriggeredEvent("rom_nyx_love_1")

            elif GetLocID() == "novaras_fort_seb_captains_bedroom":
                if self.route == "dominant":
                    if self.progress == 3:
                        if not IsDaytime():
                            return TriggeredEvent("rom_nyx_dominant_facefuck")
                    elif self.progress == 4:
                        if GetGameDay() % 2 == 0:
                            if not IsDaytime():
                                if QstDelayCheck(self):
                                    return TriggeredEvent("rom_nyx_dominant_facefuck_rep")
                        else:
                            return TriggeredEvent("rom_nyx_dominant_facefuck_rep_not_today")


        # yes we need that shit bc of weird-ass logic this LM follows
        def IsRomanced(self):
            if self.isActive or self.isOver:
                if self.route != "":
                    return True
            return False

        def onOver(self):
            QstStart(PrimerTheComingStorm)
            return