init python:
    notesLib["NijahInvitedOver"] = Note(
        _("Visit Nijah"), 
        _("I should visit Nijah down at housing district to discuss her future."))

    # a logic module that adds a line that initiates the quest
    @AppendToAllQuests
    class PrimerDamzelInDiztrezz(LogicModule):
        def extraDialogue(self):
            if QstGetProgress(EventNijahRescue) == 3:
                # offer the line only if the quest aint already taken and rescue event is long into progression
                # this basically to avoid weird shit when we visit nijah_root dialogue node again
                if not QstIsActive(QstDamzelInDiztrezz):
                    yield ("nijah_root", DNode(_("I'm gonna deal with Tarek."), "nijah_damzelDizztrezz_dealwithtarek"))

    # help nijah deal with Tarek quest
    @AppendToAllQuests
    class QstDamzelInDiztrezz(BaseQuest):
        TITLE = _("Damzel In Diztrezz")
        DESCRIPTION = _("I agreed to help Nijah deal with Tarek.")
        SIMPLE_GOALS = False
        GOALS = {
            1: QuestStage(_("Get Markus' help"), 
                hintTxt = _("First step, get Markus. I'll need some backup on this one, that's for sure...")),
            1.5: QuestStage(_("Scout the black diamond"), 
                hintTxt = _("We have to scout the black diamond at night. It should be a shady building in pleasure district.")),
            2: QuestStage(_("Storm the Black Diamond"), 
                hintTxt = _("We have decided on a frontal assault of the Black Diamond, Tarek's... operation. While it did sound pretty straightforward, I wonder if it was a good idea after all.")),
            3: QuestStage(_("Infiltrate the Black Diamond"), 
                hintTxt = _("We have decided to get closer to Tarek by infiltrating the Black Diamond. Once inside, we should be able to get rid of him for good.")),
            4: QuestStage(_("Find Tarek"), 
                hintTxt = _("We have successfully infiltrated the Black Diamond. Now, to find Tarek...")),
            5: QuestStage(_("Learn more about Vulshan"), 
                hintTxt = _("It seems there is some sort of trouble stirring within Tarek's gang. I should try to learn more.")),
            6: QuestStage(_("Signal the guard"), 
                hintTxt = _("I have struck a deal with one of Tarek's guards. They will aid me taking him down. All I need to do is give them a sign.")),
            7: QuestStage(_("Find evidence for Tarek"), 
                hintTxt = _("I have decided to force Tarek out of Novaras by providing proof that he'll inevitably die if he stays. I should ask around the city for any evidence on Tarek's situation.")),
            8: QuestStage(_("Investigate Market at night"), 
                hintTxt = _("Lucius Mal has told me that Vulshan and Khazahs leadership is having secret meetings in the market district, at night. I should investigate.")),
            9: QuestStage(_("Bring Tarek the letter"), 
                hintTxt = _("I have found a rather compromising letter stolen from Tarek by the Khazahs. That should suffice as a proof to show him how shifting his underworld 'empire' is."))
            }

        def __init__(self):
            super().__init__()

            self.XpReward = 650
            # all of these are used for Vulshan revolt route
            self.offendedGuard = False
            self.guardChoiceMenu = ["a","b","c"]
            self.serverPaidFor = False
            self.serverChoiceMenu = ["a"]
            self.serverInfo = False
            self.addictInfo = False
            self.vulshanReady = False
            # whether we know the servant girl name for the lewd scene
            self.fawhaName = False
            # some talk they have once after tj
            self.fawhaOneShotAge = True
            # evidence subquest lines to ask chars
            self.evidenceCharsChoiceMenu = ["regina", "divine", "vala", "ves"]
            self.evidenceRouteCheckDay = 0
            # assault route 'has scouted'
            self.hasScoutedDiamond = False

            self.PlayerSoldNijah = False
            self.PlayerChoseFrontalAssault = False
            self.PlayerAssassinatedTarek = False
            self.PlayerMadeTarekLeaveEvidence = False
            self.PlayerMadeTarekLeaveInquisitors = False
            self.PlayerSidedWithVulshan = False

            self.suggestedLevel = 4

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_black_diamond":
                if self.progress == 0:
                    btnMods["toTarekOffice"] = BtnJumpLabel(_("Go to Tarek's office"), "nijah_damzelDizztrezz_goToTarekOffice")
                    if self.offendedGuard:
                        btnMods["talkGuard"] = BtnJumpLabel(_("Talk to the guard"), "qst_DamzelDizzt_3_ThugGuardOffended")
                    if not self.offendedGuard:
                        btnMods["talkGuard"] = BtnJumpLabel(_("Talk to the guard"), "qst_DamzelDizzt_3_ThugGuard")
                    if self.addictInfo == True:
                        btnMods["talkAddict"] = BtnJumpLabel(_("Talk to the Raza addict"), "qst_DamzelDizzt_3_RazaAddict_gaveMoney")
                    if not self.addictInfo == True:
                        btnMods["talkAddict"] = BtnJumpLabel(_("Talk to the Raza addict"), "qst_DamzelDizzt_3_RazaAddict")
                if self.progress == 3:
                    btnMods["toTarekOffice"] = BtnJumpLabel(_("Go to Tarek's office"), "nijah_damzelDizztrezz_goToTarekOfficeWithEvidence")

                btnMods["talkServer"] = BtnJumpLabel(_("Talk to the servant girl"), "qst_DamzelDizzt_3_Server")
            elif GetLocID() == "novaras_dist_pleasure":
                if self.GoalStates[1.5] == GoalState.VISIBLE and not IsDaytime():
                    btnMods["novaras_diamond"] = BtnJumpLabel(_("Scout Black Diamond"), "qst_DamzelDizzt_2_ScoutDiamond")
            return LocButtonMod(directMods = btnMods, priority = 1)

        def extraDialogue(self):
            if self.progress == 1 and "regina" in self.evidenceCharsChoiceMenu:
                yield ("regina_root", DNode(_("Do you know anything about Tarek or Black Diamond?"), "nijah_damzelDizztrezz_evidenceTalkRegina"))
            if self.progress == 1 and "divine" in self.evidenceCharsChoiceMenu:
                yield ("divine_root", DNode(_("Do you know anything about Tarek or Black Diamond?"), "nijah_damzelDizztrezz_evidenceTalkDivine"))
            if self.progress == 1 and "vala" in self.evidenceCharsChoiceMenu:
                yield ("vala_root", DNode(_("Do you know anything about Tarek or Black Diamond?"), "nijah_damzelDizztrezz_evidenceTalkVala"))
            if self.progress == 1 and "ves" in self.evidenceCharsChoiceMenu:
                yield ("ves_root", DNode(_("Do you know anything about Tarek or Black Diamond?"), "nijah_damzelDizztrezz_evidenceTalkVes"))
            if self.progress == 1:
                yield ("luciusmal_root", DNode(_("Do you know anything about Tarek or Black Diamond?"), "nijah_damzelDizztrezz_evidenceTalkLucius"))

        def onEnter(self):  
            if GetLocID() == "novaras_dist_market":
                if not IsDaytime():
                    if self.progress == 2:
                        if self.evidenceRouteCheckDay != GetGameDay():
                            self.evidenceRouteCheckDay = GetGameDay()
                            return TriggeredEvent("nijah_damzelDizztrezz_evidenceFollowTheMan")
            elif GetLocID() == "novaras_black_diamond":
                if self.progress == 0:
                    HouseLockBlackDiamond().canExit = False

        def onComplete(self):
            if not CharIsAlive("nijah"):
                CharAddRelEntry("nijah", "killed_by_tarek")

        def onOver(self):
            QstComplete(PrimerDamzelInDiztrezz)


label nijah_damzelDizztrezz_dealwithtarek:
    call qst_DamzelDizzt_0 from _call_qst_DamzelDizzt_0
    return

label nijah_damzelDiztrezz_getMarkus:
    # bringing markus over and
    # nijah markus & mc down at home talkin
    $ LocSet("markus_house_livingroom")
    call qst_DamzelDizzt_1 from _call_qst_DamzelDizzt_1
    jump nijah_damzelDizztrezz_chooseRoute

label nijah_damzelDizztrezz_chooseRoute:
    menu:
        'Let’s just reign death upon them.':
            if QstDamzelInDiztrezz().hasScoutedDiamond:
                jump qst_DamzelDizzt_2_frontal_postScout
            else:
                jump qst_DamzelDizzt_2_frontal
        # diplo route null for now, resets menu
        'We should try getting close to Tarek to get rid of him.':
            jump qst_DamzelDizzt_2_sneaky

label nijah_damzelDizztrezz_goToTarekOffice:
    menu:
        'Knock-knock':
            # this is linear from that point up until afteraction
            jump qst_DamzelDizzt_3_headToOffice
        'Not yet':
            $ LocEnterQ()

#############################
# EVIDENCE SUBROUTE LABELS
##############################

label nijah_damzelDizztrezz_evidenceTalkRegina:
    REGINA @talk "Hm? No, sorry dear, I wouldn't know anything about that sort of thing."
    MC @talk 'Thanks anyway.'
    REGINA @talk 'Was there anything else?'
    $ QstDamzelInDiztrezz().evidenceCharsChoiceMenu.remove("regina")
    return

label nijah_damzelDizztrezz_evidenceTalkDivine:
    DIVINE "Hm? Well, I've heard of them but they're the type of people I think you'd do well to stay away from."
    DIVINE "Nothing good comes from Raza gangs like that."
    MC @talk 'Know anyone who might know anything?'
    DIVINE 'Hmm... Perhaps one of the merchants might know something?'
    DIVINE 'Many of them keep a pulse on the underbelly of these kind of things...'
    MC @talk 'Thanks for the advice.'
    DIVINE 'Was there anything else?'
    $ QstDamzelInDiztrezz().evidenceCharsChoiceMenu.remove("divine")
    return

label nijah_damzelDizztrezz_evidenceTalkVala:
    VALA 'Oooh! Well Novaras since the refugee surge of Ramonians has experienced-'
    MC @talk "I was thinking less history lesson, more the current 'inter-politics' going on..."
    VALA "Ah, well, that's not really my area of expertise sorry."
    VALA 'You might want to try find someone whose had experience dealing with them, like another Ramonian or a merchant perhaps?'
    MC @talk 'Thanks for the advice.'
    VALA 'Was there anything else?' #Loops to her default menu.
    $ QstDamzelInDiztrezz().evidenceCharsChoiceMenu.remove("vala")
    return

label nijah_damzelDizztrezz_evidenceTalkVes:
    VES @talk '...A... what now?'
    MC @talk 'Uhh, never mind.'
    $ QstDamzelInDiztrezz().evidenceCharsChoiceMenu.remove("ves")
    return

label nijah_damzelDizztrezz_evidenceTalkLucius:
    # it's in separate file cause its thicc
    jump scr_nijah_damzelDizztrezz_evidenceTalkLucius

label nijah_damzelDizztrezz_evidenceFollowTheMan:
    jump scr_nijah_damzelDizztrezz_evidenceFollowTheMan

label nijah_damzelDizztrezz_goToTarekOfficeWithEvidence:
    menu:
        'Knock-knock':
            # this jumps to its own afteraction sequence
            jump scr_nijah_damzelDizztrezz_goToTarekOfficeWithEvidence
        'Not yet':
            $ LocEnterQ()

#############################
# AFTERACTION SEQUENCE, SAME FOR ALL ROUTES EXCEPT EVIDENCE ONE
##############################
label nijah_damzelDiztrezz_afterAction:
    # show a scene of them returnin'
    # after it, nijah can be found at her place wherever that is
    call qst_DamzelDizzt_2_afterAction from _call_qst_DamzelDizzt_2_afterAction
    $ QstComplete(PrimerDamzelInDiztrezz)
    $ QstComplete(QstDamzelInDiztrezz)
    $ QstComplete(EventNijahRescue)
    $ QstStart(HouseLockNijah)
    $ CharChangeRel("nijah", 1)
    $ NoteLock("NijahStayingAtMCs")
    $ NoteUnlock("NijahInvitedOver")
    $ QstStart(RomanceNijah)
    $ QstStart(HouseLockBlackDiamond)
    $ QstStart(BlackDiamondLogic)
    $ HouseLockBlackDiamond().canExit = True
    $ HouseLockBlackDiamond().canBeAccessed = True
    $ BlockWaitDynamic(False)
    $ LocEnterQ()
