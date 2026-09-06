init python:
    notesLib["meetMarkusPostFaw"] = Note(
        _("Meet Markus at the tavern"), 
        _("I should catch up with Markus at the Iron Unicorn tavern, down at the market district.\nPerhaps a jug of beer or two could help us figure out our next steps."))
    @AppendToAllQuests
    class EventNovarasMarkusTavernPostFaw(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_market":
                btnMods["btn_novaras_tavern"] = BtnJumpLabel(_("Tavern"), "ev_markus_tavern")
            return LocButtonMod(directMods = btnMods)

        def onStart(self):
            NoteUnlock("meetMarkusPostFaw")

        def onComplete(self):
            NoteLock("meetMarkusPostFaw")
            PartyAddChar("markus")
            # for auto-starting
            gui_parts["characters"] = True
            ## markus' gear
            PlayerAddItem("leather_armor", Silent = True)
            PlayerAddItem("scout_sword_rusty", Silent = True)
            PlayerPartyCharEquipItem("markus", "leather_armor")
            PlayerPartyCharEquipItem("markus", "scout_sword_rusty")
            QstStart(PrimerDarkKnight)