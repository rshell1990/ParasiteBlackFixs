init python:
    notesLib["romanceTheaInvite"] = Note(
        _("Invite Thea"), 
        _("I think I've done enough to impress Thea from the Adventurers' Guild now."))
    notesLib["romanceTheaDate"] = Note(
        _("Date Thea"), 
        _("I have a date with Thea. I can meet her at the Iron Unicorn at night."))
    notesLib["romanceTheaEvening"] = Note(
        _("Visit Thea"), 
        _("Thea invited me to her room in the evening, upstairs in the Adventurers Guild."))

    @AppendToAllQuests
    # Thea romance logic
    class RomanceThea(LogicModule):
        def __init__(self):
            super().__init__()

            self.eveningBoobjob = False

        def onStart(self):
            NoteUnlock("romanceTheaInvite")

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_tavern":
                if IsInTimeFrame(TIME_DAY_END, TIME_DAY_START):
                    if self.progress == 1:
                        btnMods["thea_romance_btn"] = BtnJumpLabel(_("Talk to Thea"), "rom_thea_unicorn")
            elif GetLocID() == "novaras_adv_guild":
                if not IsDaytime():
                    if self.eveningBoobjob:
                        btnMods["visitThea"] = BtnChangeLoc(_("Visit Thea"), "thea_room")
            return LocButtonMod(directMods = btnMods)

        def onEnter(self):
            if GetLocID() == "thea_room":
                if not IsDaytime():
                    if self.eveningBoobjob:
                        return TriggeredEvent("rom_thea_after_date")

        def extraDialogue(self):
            if self.progress == 0:
                yield ("thea_root",DNode(_("You wanted to speak to me about something?"), "rom_thea_invite"))
            elif self.progress >= 2 and not self.eveningBoobjob:
                yield ("thea_root",DNode(_("I was wondering if I could visit you again this evening ..."), "rom_thea_rep_invite_boobjob"))


