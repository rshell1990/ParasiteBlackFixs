init python:
    notesLib["meetMarkusPostTwoEmps"] = Note(
        _("Meet Markus at the tavern, night time"),
        _("I should catch up with Markus at the Iron Unicorn tavern, down at the market district.\nI need to share what Alcott had told me.\nMarkus will be there at night."))
    @AppendToAllQuests
    class EventNovarasMarkusTavernTwoEmps(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_market":
                if IsInTimeFrame(TIME_LATEEVENING, TIME_DAWN):
                    btnMods["btn_novaras_tavern"] = BtnJumpLabel(_("Tavern"), "ev_Markus_tavern_postTwoEmps")
            return LocButtonMod(directMods = btnMods)

        def onStart(self):
            NoteUnlock("meetMarkusPostTwoEmps")
            return

        def onComplete(self):
            NoteLock("meetMarkusPostTwoEmps")

            # thats more like save compat
            CharUnKill("kiara")
            if CharGetVar("kiara", "romanced") == True:
                CharAddRelEntry("kiara", "revive_romance")
            else:
                CharAddRelEntry("kiara", "revive_no_romance")

            QstStart(PrimerTheComingStorm)
            return
