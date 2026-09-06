init python:
    # primer, adds lines
    @AppendToAllQuests
    class PrimerADazzlingTail(LogicModule):
        def extraDialogue(self):
            if not QstIsActive(QstADazzlingTail):
                if GetGameDay() < DialogueArlena().dayUnlocked + 2:
                    yield ("arlena_root", DNode(_("Hey, you mentioned having a job for me?"),"arlena_dazzlingtail_wait"))
                elif GetGameDay() >= DialogueArlena().dayUnlocked + 2:
                    yield ("arlena_root", DNode(_("Hey, you mentioned having a job for me?"),"arlena_dazzlingtail_start"))

    # Arlena makes diamond buttplugs quest
    notesLib["ArlenaADazzTailQuest"] = Note(
        _("Arlena has a job"),
        _("Arlena, daughter of Novaras blacksmith, mentioned having a job for me. Wonder what that might be."))
    notesLib["ArlenaGems"] = Note(
        _("Arlena needs gems"),
        _("Novaras blacksmith's daughter Arlena is now supplying the city's ladies with exquisite, jewelry-grade buttplugs. She will take 20 gems off me in exchange for gold."),
        journal_flag_persistent = True)
    @AppendToAllQuests
    class QstADazzlingTail(BaseQuest):
        TITLE = _("A Dazzling Tail")
        DESCRIPTION = _("Arlena asked for my help on one of her rather elaborate 'projects'. Of course it deals with supple backsides...")
        GOALS = {
            1: QuestStage(_("Gather gems for Arlena"), trackTag = "btn_novaras_gates_exit_city", hintTxt = _("I guess Demorai scout parties lurking at the Valley of Death might carry some gems around. Arlena will need 20 of those.")),
            2: QuestStage(_("Visit Arlena after she finishes her work"), trackTag = "btn_novaras_blacksmith", hintTxt = _("The lady's hammering down on those gems, says she needs a day. Can't wait to see what she'll produce...")),
            3: QuestStage(_("Get your cut of the profits"), trackTag = "btn_novaras_blacksmith", hintTxt = _("The... accessories Arlena produced surely proven to be magnificent. She's gonna need a day to deliver the product to the pleasure district. I can collect my share of gold afterwards."))}
        def __init__(self):
            super().__init__()

            self.XpReward = 300
            self.gemPay = 30
            self.askedOnce = False

        def extraDialogue(self):
            if self.progress == 1:
                if PlayerItemQty("gems") >= 20:
                    yield ("arlena_root",DNode(_("Hey, I brought gems you wanted!"), "arlena_dazzlingtail_broughtgems"))

        def onEnter(self):  
            # stage 2, delayed event, arlena's done & playing with her 'work'
            if GetLocID() == "novaras_blacksmith":
                if IsDaytime():
                    if self.progress == 2:
                        return TriggeredEvent("arlena_dazzlingtail_workdone_day")
                else:
                    if self.progress == 2:
                        return TriggeredEvent("arlena_dazzlingtail_workdone_night")

            # stage 3, we're to get our profits
            elif GetLocID() == "arlena_room":
                if IsDaytime():
                    if self.progress == 3:
                        return TriggeredEvent("arlena_dazzlingtail_getprofits")
        
        def onStart(self):
            QstComplete(PrimerADazzlingTail)
            return

label arlena_dazzlingtail_wait:
    ARLENA "Yeah, I'll need a couple days to set everything up."
    MC "Huh? A surprise job?"
    ARLENA "Come back later, and please now, I need to get back to work!"
    $ NoteUnlock("ArlenaADazzTailQuest")
    MC "Hmmm... Okay then."
    return

label arlena_dazzlingtail_start:
    # original dialogue if player agrees straight up
    if QstADazzlingTail().askedOnce == False:
        ARLENA "You're right on time."
        ARLENA "Here, let me show you..."
        call qst_ADazzlingTail_intro from _call_qst_ADazzlingTail_intro
    # dialogue if player refuses & re-visits arlena
    else:
        call qst_ADazzlingTail_intro2 from _call_qst_ADazzlingTail_intro2
    $ LocEnterQ()

label arlena_dazzlingtail_broughtgems:
    call qst_ADazzlingTail_01 from _call_qst_ADazzlingTail_01
    hide arlena with dissolve
    $ PlayerRemItem("gems", 20)
    $ QstSetProgress(QstADazzlingTail, 2)
    $ QstSetDelay(QstADazzlingTail, 1)
    $ LocEnterQ()

# day variant of stage 2
label arlena_dazzlingtail_workdone_day:
    call qst_ADazzlingTail_02_day from _call_qst_ADazzlingTail_02_day
    $ QstSetProgress(QstADazzlingTail, 3)
    $ QstSetDelay(QstADazzlingTail, 1)
    $ LocSet("novaras_blacksmith")
    $ LocEnterQ()

# night variant of stage 2
label arlena_dazzlingtail_workdone_night:
    call qst_ADazzlingTail_02_night from _call_qst_ADazzlingTail_02_night
    $ QstSetProgress(QstADazzlingTail, 3)
    $ QstSetDelay(QstADazzlingTail, 1)
    $ LocSet("novaras_dist_farm")
    $ LocEnterQ()

# stage 3, we return to get profits
label arlena_dazzlingtail_getprofits:
    call qst_ADazzlingTail_03 from _call_qst_ADazzlingTail_03
    $ QstComplete(QstADazzlingTail)
    $ NoteUnlock("ArlenaGems")
    $ QstStart(RomanceArlena)
    $ CharAddRel("arlena", 1)

    $ QstStart(EventReginaButtplug)
    $ QstSetDelay(EventReginaButtplug, 1)

    $ LocSet("novaras_dist_farm")
    $ LocEnter()

