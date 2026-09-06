init python:
    notesLib["romance_faymore_meet_at_next_night"] = Note(
        _("Meet with Faymore ladies"), 
        _("The Faymore ladies have invited me to return to their home tomorrow evening so they might give me my... {i}'reward.'{/i}"),
        )
    notesLib["romance_faymore_meet_at_night"] = Note(
        _("Meet with Faymore ladies"), 
        _("The Faymore ladies have invited me to join their bed in the evenings... Perhaps, I should take them up on that offer from time to time?"),
        )
    @AppendToAllQuests
    class RomanceFaymoreGirls(LogicModule):
        def __init__(self):
            super().__init__()
            self.DayHadSex = 0
            self.ScheduledSexEventAt = None # these happen at night when player enters their place
            self.AskedAboutSexToday = False

        def extraDialogue(self):
            # chanyi
            if CharIsVisiblyPreg("chanyi"):
                yield ("chanyi_root", DNode(_("How goes your condition?"), "rom_faymore_chanyi_askpreg"))
            if PregFaymoreGirls().NumBirths > 0:
                yield ("chanyi_root", DNode(_("How is our daughter?"), "rom_faymore_chanyi_askdaughter"))
            if self.ScheduledSexEventAt == None:
                yield ("chanyi_root", DNode(_("Would you and Anya be interested in... {i}some evening entertainment tonight?{/i}"), "rom_faymore_chanyi_asksex"))

            # anya
            if CharIsVisiblyPreg("chanyi"):
                yield ("anya_root", DNode(_("Is... the pregnancy going well?"), "rom_faymore_anya_howispreg"))
            if PregFaymoreGirls().NumBirths > 0:
                yield ("anya_root", DNode(_("How is our son?"), "rom_faymore_anya_howisson"))

        def onEnter(self):
            if GetLocID() == "hamun_faymore_manor":
                if self.ScheduledSexEventAt is not None:
                    if not IsDaytime():
                        if ((GetGameDay() == self.ScheduledSexEventAt) and IsInTimeFrame(TIME_DAY_END, TIME_MIDNIGHT)) or (GetGameDay() > self.ScheduledSexEventAt):
                            return TriggeredEvent("rom_faymore_pick_sexscene")

        def onMidnight(self):
            self.AskedAboutSexToday = False

label rom_faymore_pick_sexscene:
    $ RomanceFaymoreGirls().ScheduledSexEventAt = None
    $ RomanceFaymoreGirls().DayHadSex = GetGameDay()
    # first time, forced "first time" threesome variant
    if QstGetProgress(RomanceFaymoreGirls) == 0:
        $ QstSetProgress(RomanceFaymoreGirls, 1)
        $ NoteLock("romance_faymore_meet_at_next_night")
        $ SetRepeatVariant(False)
        jump romance_faymore_girls_threesome
    # non-first time, picks between non-first threesome and balcony
    elif QstGetProgress(RomanceFaymoreGirls) == 1:
        $ NoteLock("romance_faymore_meet_at_night")
        $ tmpvar = RngInt(1, 10)
        if config.developer:
            "DEBUG: balcony variant?"
            menu:
                "DEBUG: yes":
                    $ tmpvar = 1
                "DEBUG: no":
                    $ tmpvar = 8
        if tmpvar <= 3:
            # balcony
            jump rom_faymore_girls_balcony
        else:
            # threesome
            $ SetRepeatVariant(True)
            $ tmpvar = {}
            jump romance_faymore_girls_threesome


### ### Speaking to Chanyi
label rom_faymore_chanyi_askpreg:
    CHANYI @serious "Urghh... Must you remind me that I carry your spawn?"
    CHANYI @serious "If you must know, she kicks a lot."
    CHANYI @serious "I have back ache, my breasts are sore."
    CHANYI @talk "Oh... And I have a craving for grapes."
    MC @think "She?"
    MC @think "How do you know it's a girl?"
    CHANYI @laugh "Intuition."
    "For the briefest moment, Chanyi looks down and gently rubs her belly,"
    "a slight warm smile on her face that she quickly hides."
    CHANYI @serious "Anyway, enough about the child."
    CHANYI @talk "Is there anything else you wish to discuss?"
    return

label rom_faymore_chanyi_askdaughter:
    CHANYI @laugh "She is well. Today she even tried crawling!"
    CHANYI @laugh "Naturally, any child I made would be superior to the usual stock!"
    "You raise a brow and smirk at the strangely proud maternal instinct she's showing."
    CHANYI @serious "{i}*Ahem*{/i} Not that I care THAT much."
    CHANYI @talk "Anyway, is that all you came to ask?"
    return

label rom_faymore_chanyi_asksex:
    if GetGameDay() < (RomanceFaymoreGirls().DayHadSex + 2):
        $ tmpvar = False
    else:
        if RomanceFaymoreGirls().AskedAboutSexToday == True:
            $ tmpvar = False
        else:
            $ tmpvar = (True if RngFloat(0.0, 1.0) <= 0.7 else False)
            $ RomanceFaymoreGirls().AskedAboutSexToday = True

    if tmpvar == True:
        $ RomanceFaymoreGirls().ScheduledSexEventAt = GetGameDay()
        CHANYI @lewd "Some evening entertainment is just what we need."
        CHANYI @talk "Come back after dark... We'll be waiting."
        $ NoteUnlock("romance_faymore_meet_at_night")
        return
    else:
        CHANYI @sad "Not tonight, I'm afraid."
        CHANYI @talk "Anya and I have other engagements to attend to."
        return

   
######## Speaking to Anya
label rom_faymore_anya_howispreg:
    ANYA @happy "I think so."
    ANYA @think "Though I swear I feel like I have even more energy now than usual?"
    ANYA @think "How strange."
    return

label rom_faymore_anya_howisson:
    ANYA @happy "The most adorable thing in the world!"
    ANYA @happy "I swear, just the other day, they reached out to wrap their tiny hands around my finger!"
    ANYA @talk "My heart could have melted!"
    return