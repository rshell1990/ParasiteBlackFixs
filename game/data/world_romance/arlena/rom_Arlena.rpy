init python:
    notesLib["ArlenaRomanceForgeAnal"] = Note(
        _("Arlena request"),
        _("Arlena asked me to come to the smithy at night. That's promising."))
    @AppendToAllQuests
    # arlena romance logic,
    # progress 0 is intro scene, 1+ all the other ones
    class RomanceArlena(LogicModule):
        def __init__(self):
            super().__init__()

            # flag used in bj scene, to transfer locations & trigger onenter
            self.bjRoomCheck = False
            # on loc enter at night, triggers scene after rep. anal setup sequence
            self.forgeAnalFlag = False
            # this to be sure we dont roll more than once a day for sex encounters
            self.checkDay = 0

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_farm":
                if not IsDaytime():
                    if self.forgeAnalFlag:
                        btnMods["btn_novaras_blacksmith"] = BtnJumpLabel(STR_LOC.NOV_BLACKSMITH, "rom_Arlena_stage1_repAnal")
            # priority to make sure it overrides smithy house lock
            return LocButtonMod(directMods = btnMods, priority = 1)

        def onEnter(self):  
            if GetLocID() == "arlena_room":
                if self.progress == 0:
                    if CharGetRel("arlena") >= 4:
                        return TriggeredEvent("rom_Arlena_stage0_intro")
                if self.bjRoomCheck:
                    return TriggeredEvent("rom_Arlena_stage1_repBj_02")

            # all lewds barred under prog 1
            elif GetLocID() == "novaras_blacksmith":
                if IsDaytime():
                    if self.progress == 1:
                        if self.checkDay != GetGameDay():
                            self.checkDay = GetGameDay()
                            # a coinflip gate to choose between two checks
                            if RngInt(1,2) == 1:
                                # bj scene setup chance check
                                if CharGetRel("arlena") >= 5:
                                    # that's what, 25%?
                                    if RngInt(1, 2) == 1:
                                        return TriggeredEvent("rom_Arlena_stage1_repBjSetup")
                            else:
                                if CharGetRel("arlena") >= 6:
                                    # anal scene setup chance check, 25% too
                                    if RngInt(1, 2) == 1:
                                        return TriggeredEvent("rom_Arlena_stage1_repAnalSetup")

        def extraDialogue(self):
            if self.progress == 1:
                if self.delayCheck():
                    if CharGetRel("arlena") >= 6:
                        yield ("arlena_root", DNode(_("Should we indulge some... stress relief?"), "rom_Arlena_stage1_repDoggy"))
                    else:
                        yield ("arlena_root", DNode(_("Should we indulge some... stress relief?"), "rom_Arlena_stage1_repDoggy_no"))

# arlena intro, you can rebuff her at this stage ending the romance altogether
label rom_Arlena_stage0_intro:
    $ CharSetLover("arlena")
    $ CharReplaceRelEntry("arlena", "relation_initial", "relation_lovers")
    call rom_ArlenaIntroDoggy from _call_rom_ArlenaIntroDoggy
    $ QstSetProgress(RomanceArlena, 1)
    $ CharChangeRel("arlena", 1)
    $ QstSetDelay(RomanceArlena, 1)
    $ LocEnter()

# rep bj triggered, moves player to arlena room if they're in
label rom_Arlena_stage1_repBjSetup:
    call rom_ArlenaRepBj from _call_rom_ArlenaRepBj
    # if player refuses arlena. if player agrees, the logic is in the script
    $ LocFlush()
    $ QstSetDelay(RomanceArlena, 1)
    $ CharChangeRel("arlena", -1)
    $ LocEnter()

# rep bj arlena room sequence
label rom_Arlena_stage1_repBj_02:
    $ RomanceArlena().bjRoomCheck = False
    call rom_ArlenaRepBj_02 from _call_rom_ArlenaRepBj_02
    if CharGetRel("arlena") < 7:
        $ CharChangeRel("arlena", 1)
    $ LocSet("novaras_blacksmith")
    $ QstSetDelay(RomanceArlena, 1)
    $ LocEnter()

# rep doggy dialogue option
label rom_Arlena_stage1_repDoggy:
    call rom_ArlenaDoggyRep from _call_rom_ArlenaDoggyRep
    $ CharChangeRel("arlena", 1)
    $ QstSetDelay(RomanceArlena, 1)
    $ LocEnter()

# rep doggy no
label rom_Arlena_stage1_repDoggy_no:
    ARLENA "Not now."
    ARLENA "I'm... busy."
    MC @talk "Well, as you wish."
    "Perhaps I should get a little bit closer to her first."
    return

label rom_Arlena_stage1_repAnalSetup:
    call rom_ArlenaForgeAnalSetup from _call_rom_ArlenaForgeAnalSetup
    # a flag to trigger scene is set in script
    $ LocEnter()

# rep anal night sequence
label rom_Arlena_stage1_repAnal:
    call rom_ArlenaForgeAnalRep from _call_rom_ArlenaForgeAnalRep
    $ RomanceArlena().forgeAnalFlag = False
    $ NoteLock("ArlenaRomanceForgeAnal")
    $ CharChangeRel("arlena", 1)
    $ QstSetDelay(RomanceArlena, 1)
    $ LocSet("novaras_dist_farm")
    $ LocEnterQ()
