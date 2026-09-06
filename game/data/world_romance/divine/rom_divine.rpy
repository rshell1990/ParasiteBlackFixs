init python:
    notesLib["MeetDivineAtNight"] = Note(
        _("Meet Sister Divine at night"), 
        _("Sister Divine gave me a stone that is supposed to allow me entrance to the Palam tower, come nightfall. I wonder what she has in mind..."))
    @AppendToAllQuests
    # divine romance logic,
    # the module is turned on by helping her deal with the frog monster
    # progress 0 is her catching up with you in the mainhall at night (intro scene), 
    # 1 her hanging out in her quarters greeting you at night
    # 2 is afterwards
    class RomanceDivine(LogicModule):
        def __init__(self):
            super().__init__()

            self.CanRepeatSex = True # toggled off on first-time-aftersex and repeat-aftersex

        def onEnter(self):  
            if GetLocID() == "novaras_palam_mainhall":
                if not IsDaytime():
                    if self.progress == 0:
                        return TriggeredEvent("rom_divine_meetplayer")
            elif GetLocID() == "novaras_palam_divine_quarters":
                if not IsDaytime():
                    if QstDelayCheck(self):
                        if self.progress >= 1:
                            return TriggeredEvent("rom_divine_progress_1_enter_quarters")

        def onStart(self):
            NoteUnlock("MeetDivineAtNight")
            return

        def onNoon(self):
            if day % 2 == 0:
                self.CanRepeatSex = True

        def extraDialogue(self):
            if self.progress == 0:
                yield ("divine_root", DNode(_("About your invitation..."), "rom_divine_progress_0_come_at_night_instead"))
            if self.progress == 1:
                yield ("divine_root", DNode(_("How about some fun?"), "rom_divine_progress_1_come_at_night_instead"))

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_palam_divine_quarters":
                if not IsDaytime():
                    if self.progress == 1:
                        btnMods["btn_talk_divine_quarters"] = BtnJumpLabel(_("Talk to Sister Divine"), "divine_talk_quarters")
            return LocButtonMod(directMods=btnMods)

label rom_divine_progress_0_come_at_night_instead:
    DIVINE "Not now."
    DIVINE "Come at night,"
    "She toned it down to a whisper and leaned in:"
    DIVINE "{i}My beast.{/i}"
    MC "...Okay."
    return

label rom_divine_progress_1_come_at_night_instead:
    "She giggled:"
    DIVINE @happy "Not now, my beast."
    DIVINE "Come see me in my quarters when the night falls."
    MC "...Okay."
    return

label rom_divine_progress_1_enter_quarters:
    show divine at center with dissolve
    $ QstSetProgress(RomanceDivine, 2)
    DIVINE @happy "I was wondering when you'd come back..."
    DIVINE "Let's not waste any time, shall we?"
    menu:
        "Totally!":
            jump rom_divine_rep_sex
        "Hold on a moment...":
            DIVINE "As you wish, my beast."
            $ LocEnter()

label divine_talk_quarters:
    show divine at center with dissolve
    if RomanceDivine().CanRepeatSex:
        DIVINE "Are you in for some fun now, beast?"
        menu:
            "Indeed I am!":
                jump rom_divine_rep_sex
            "Hold on a moment...":
                DIVINE "As you wish, my beast."
                $ LocEnter()
    else:
        DIVINE "There you are, my beast."
        MC @talk "Hey, what about..."
        DIVINE "Not now."
        DIVINE "I have work to do."
        DIVINE "Visit me another night."
        DIVINE "We will..."
        DIVINE @lewd "Catch up."
        $ LocEnter()