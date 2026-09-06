init python:
    notesLib["NijahRomanceInvested"] = Note(
        _("Nijah's market stall"), 
        _("I have invested in Nijah's 'food' business. She has a stall of her own down at Novaras market district. I can find her there occasionally."),
        journal_flag_persistent = True)
    notesLib["NijahRomancePimp"] = Note(
        _("Nijah's pimp"), 
        _("I have became Nijah's pimp. I can find her working 'night shifts' in pleasure district."),
        journal_flag_persistent = True)
    notesLib["NijahRomanceCanCollect"] = Note(
        _("Nijah's earnings"), 
        _("I can come and collect my share of Nijah's earnings."))

    @AppendToAllQuests
    class ShopNijahStall(BaseShopLM):
        def __init__(self):
            super().__init__()
            self.WillNotBuyCategories = GetAllItemShopCats() - {"food"}

        def onStart(self):
            AddItemTo(self.Items, "gold", 300)
            AddItemTo(self.Items, "ramonian_twister")
            AddItemTo(self.Items, "ramonian_twister")
            self.onMidnight() # 1st restock is manual

        # daily restock 
        def onMidnight(self):
            super().SimulateTradingItems(self, 
                TargetGold = 500,
                TargetStockValue = 500,
                RestockItemsPool = {
                    "ramonian_twister":{
                        "restock_if_below":5,
                        "daily_amt":2.0},
                },
            )

    @AppendToAllQuests
    # nijah romance logic
    # progress 0 is intro scene, 1+ all the other ones
    class RomanceNijah(LogicModule):
        def __init__(self):
            super().__init__()

            self.investBusiness = False
            self.storeOpen = False
            
            # stored day, used to flip nijah back n forth between market & home
            # also used to roll for clients during pimp route
            self.checkDay = 0
            
            self.becamePimp = False
            self.pimpDayCounter = 0
            self.pimpPaycheck = False            
            self.pimpEarnRange = 200 # pimpin gets 400 + this much random range up and down, so 200-600
            self.checkDayPimp = 0

        def onEnter(self):
            if GetLocID() == "nijah_house_lroom":
                if self.progress == 0:
                    return TriggeredEvent("rom_Nijah_stage0_intro")

            elif GetLocID() == "novaras_dist_pleasure":
                if not IsDaytime():
                    if self.becamePimp == True:        
                        if self.checkDay != GetGameDay():
                            self.checkDay = GetGameDay()
                            if RngInt(1, 3) == 1:
                                return TriggeredEvent("rom_Nijah_stage2_pimpSelectScene")
            
        def onNoon(self):
            # pimp day counter
            if self.becamePimp == True:
                if self.checkDayPimp != GetGameDay():
                    self.checkDayPimp = GetGameDay()
                    if self.pimpDayCounter < 5:
                        self.pimpDayCounter += 1
                    if self.pimpDayCounter == 5:
                        self.pimpPaycheck = True
                        NoteUnlock("NijahRomanceCanCollect")
                        self.pimpDayCounter = 0
            return

        def onMidnight(self):
            if self.investBusiness == True:                    
                if self.checkDay != GetGameDay():
                    self.checkDay = GetGameDay()
                    self.storeOpen = not self.storeOpen
            return


        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_market_stalls":
                if RomanceNijah().storeOpen:
                    btnMods["nijah_market_stalls_btn"] = BtnJumpLabel(_("Check up on Nijah"), "rom_Nijah_stage2_stall_lines")
            return LocButtonMod(directMods=btnMods)

        def extraDialogue(self):
            if self.progress == 1:
                yield ("nijah_root",DNode(_("What are you gonna do now?"), "rom_Nijah_stage1_future"))
            # menu to choose scenes from
            if self.progress >= 2:
                yield ("nijah_root",DNode(_("Your master wants you right now."), "rom_Nijah_stage2_sexoptions_lines"))
            # if can collect
            if self.becamePimp and self.pimpPaycheck:
                yield ("nijah_root",DNode(_("I've come to collect my share of your earnings."), 'rom_Nijah_stage2_pimpCollect'))
            # stall
            if self.investBusiness:
                yield( "nijah_root",DNode(_("How goes the stall?"), "nijah_howgoesthestall_lines"))
            # howareyou
            if self.progress >= 2:
                yield( "nijah_root",DNode(_("How are things?"), "rom_nijah_howarethings"))
            if self.progress >= 2:
                yield( "nijah_root",DNode(_("How about a kiss?"), "rom_Nijah_gimmeakiss"))

# nijah intro, just some lines she says
label rom_Nijah_stage0_intro:
    # show the sequence of MC entering her house
    $ CharSetLover("nijah")
    call rom_Nijah_stage0_intro_lines from _call_rom_Nijah_stage0_intro_lines
    $ NoteLock("NijahInvitedOver")
    $ QstSetProgress(RomanceNijah, 1)
    $ LocEnterQ()

# pimp or invest choice
# invest choice jumps to afterInvest sexytimes
# pimp too
label rom_Nijah_stage1_future:
    call rom_Nijah_stage1_future_lines from _call_rom_Nijah_stage1_future_lines
    $ LocEnterQ()

label rom_Nijah_stage2_pimpSelectScene:
    MC @talk '(Nijah is probably working tonight... Perhaps I should see how she is getting on?)'
    menu:
        "Visit Nijah's workplace":
            scene black with dissolve
            "Navigating streets of Novaras, I soon found Nijah's working place."
            $ Pause()
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            $ LocNameSetTemp(_("Brothel"))
            $ rng = RngInt(1,3)
            if rng == 1:
                call rom_Nijah_pimp_anal from _call_rom_Nijah_pimp_anal
                $ UnlockGalSceneAndGrantXp("nijah","pimp_anal")
            if rng == 2:
                call rom_Nijah_pimp_threeHands from _call_rom_Nijah_pimp_threeHands
                $ UnlockGalSceneAndGrantXp("nijah","pimp_bukk")
            if rng == 3:
                call rom_Nijah_pimp_threesome from _call_rom_Nijah_pimp_threesome
                $ UnlockGalSceneAndGrantXp("nijah","pimp_threes")
        "Don't":
            $ LocEnterQ()
    $ AutoMus(True)
    $ LocNameReset()
    $ LocEnter()

label rom_Nijah_stage2_pimpCollect:
    MC "Hey Nijah, I've come to collect my share of your... business."
    NIJAH "Sure, there you go, [player_name!t]."
    "Nijah handed me a pouch of coins."
    $ PlayerAddItem("gold", 400 + (RngInt(-RomanceNijah().pimpEarnRange, RomanceNijah().pimpEarnRange)))
    $ RomanceNijah().pimpPaycheck = False
    $ NoteLock("NijahRomanceCanCollect")
    MC "Nice, thank you."
    NIJAH "Yeah, been working!"
    return
