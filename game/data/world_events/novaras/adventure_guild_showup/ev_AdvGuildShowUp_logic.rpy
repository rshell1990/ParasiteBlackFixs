init python:
    notesLib["ShowUpAtAdventurersGuild"] = Note(
        _("Visit the Adventurers Guild"), 
        _("Given I am officially an Adventurer now, I should introduce myself to the Adventurers' Guild of Novaras."))

    @AppendToAllQuests
    class EventAdventureGuildShowUp(LogicModule):
        def __init__(self):
            super().__init__()

            self.MarkusWasInPartyAlready = True # set to False as you walk in if you havent seen tavern scene
            self.SeenAtNightScene = False

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_market":
                if IsDaytime():
                    btnMods["btn_novaras_adv_guild"] = BtnJumpLabel(STR_LOC.NOV_ADV_GUILD, "ev_AdvGuildShowUpPostFaw_scr")
            return LocButtonMod(directMods = btnMods)

        def onEnterOnce(self):
            if GetLocID() == "novaras_adv_guild":
                if not IsDaytime():
                    if self.SeenAtNightScene == False:
                        return TriggeredEvent("ev_AdvGuildShowUpPostFaw_AtNight")
        
        def onExit(self):
            self.SeenAtNightScene = False
            return

        def onStart(self):
            NoteUnlock("ShowUpAtAdventurersGuild")
            return

        def onComplete(self):
            NoteLock("ShowUpAtAdventurersGuild")
            QstStart(NovarasAdvBoard)
            CharMeet("celeste", Silent = True)
            return

label ev_AdvGuildShowUpPostFaw_AtNight:
    $ EventAdventureGuildShowUp().SeenAtNightScene = True
    show mc at left with easeinleft
    MC "Hmm... Doesn't seem like there's anyone to talk to really."
    MC "Perhaps I should come by daytime."
    $ LocEnter()