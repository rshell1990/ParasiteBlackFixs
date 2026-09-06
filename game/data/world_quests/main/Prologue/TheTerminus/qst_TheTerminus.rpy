init python:
    @AppendToAllQuests
    class QstTerminus(BaseQuest):
        GOALS = {
            0: QuestStage(_("Get gold from the chest"),     
                trackTag = "btn_mc_house_chest",
                hintTxt = _("I will certainly need some currency to handle whatever today brings. There must be some in my chest.")),
            1: QuestStage(_("Head out of your room"),       
                hintTxt = _("It's time to head out."),
                trackTag = "btn_mc_house_bedroom_exit"),
            2: QuestStage(_("Attend the Terminus Ceremony"), 
                trackTag = "btn_nov_palace_gates", 
                hintTxt = _("The Terminus Ceremony is held in the Royal Palace, at the very heart of the City of Novaras. I should make haste.")),
            3: QuestStage(_("Meet Adara at the tavern\nor visit the bordello"), 
                trackTag = ["btn_novaras_tavern", "btn_novaras_bordello"], 
                hintTxt = _("Struck by the prospect of joining the Scouts Corp, I am unsure how to spend the remainder of today. Markus went for the pleasure district to get laid. I remember Adara talking about catching up at the Iron Unicorn tavern, after the ceremony.")),
            4: QuestStage(_("Return home"),                 
                trackTag = "btn_mc_house", 
                hintTxt = _("There goes my last night in the city as a free citizen. I should head home and try to get some sleep.")),
            5: QuestStage(_("Report to Fort Sebastian"),    
                trackTag = "btn_novaras_fort_seb", 
                hintTxt = _("During the Terminus Ceremony held yesterday I have found out that I am to be a part of the Scouts Corp, the reconnaissance branch of Emperor Alcott's army. I am to report to Fort Sebastian to begin my training. Some graduation...")),
            }
        TITLE = _("The Terminus")
        DESCRIPTION = _("As I have come of age, the Terminus Ceremony is about to decide my future for life. I will find out what fate has our kingdom blessed me with. Hopefully, I am prepared for it.")

        def __init__(self):
            super().__init__()
    
            self.XpReward = 50
            self.InitialGold = 80
            self.AdaraOrNijah = None # set to string dep on choice, used by auto-meet
            self.IsMain = True
            self.WalkIntoMarketSeen = False

        def onEnter(self):  
            if GetLocID() == "mc_house_kitchen":
                if self.progress == 1:
                    return TriggeredEvent("qst_Terminus_KitchenEnterMorning")
                elif self.progress == 4:
                    return TriggeredEvent("qst_Terminus_ReturnHomeFromEitherTavernOrBordello")
            elif GetLocID() == "novaras_market_stalls":
                if self.progress == 2:
                    if not self.WalkIntoMarketSeen:
                        self.WalkIntoMarketSeen = True
                        return TriggeredEvent("qst_Terminus_WalkIntoMarket")
            elif GetLocID() == "novaras_royal_palace":
                if self.progress == 2:
                    return TriggeredEvent("qst_Terminus_EnterPalace")
            elif GetLocID() == "novaras_tavern":
                if self.progress == 3:
                    return TriggeredEvent("qst_Terminus_ArriveToAdaraTavern")
            elif GetLocID() == "novaras_bordello_ext":
                if self.progress == 3:
                    return TriggeredEvent("qst_Terminus_ArriveToBordello")
            elif GetLocID() == "novaras_fort_seb_yard":
                if self.progress == 5:
                    return TriggeredEvent("qst_Terminus_ArriveToFort")

        def locationMod(self):
            btnMods = {}
            if self.progress == 0:
                if GetLocID() == "mc_house_bedroom":
                    btnMods["btn_mc_house_bedroom_exit"] = BtnFluffTxt(STR_NAV.LEAVE, _("I should grab my gold first."))
                    btnMods["btn_mc_house_bed"] = BtnJumpLabel(_("Bed"), "qst_Terminus_CantSleep")
                elif GetLocID() == "mc_house_kitchen":
                    btnMods["talkRegina"] = BtnDisabled()
            # stage 2 location blocks/mods, "go to the ceremony",
            # MOST OF THE AREAS (almost all of them) are blocked with narrative at this stage
            elif self.progress == 2:
                if GetLocID() == "novaras_dist_centre":
                    btnMods["btn_nov_palace_gates"] = BtnChangeLoc(STR_LOC.NOV_ROYAL_PALACE, "novaras_royal_palace")
                ## these are all blockers, so that player cant wander where they shouldnt have
                elif GetLocID() == "novaras_dist_house":
                    btnMods["btn_markus_house"] = BtnJumpLabel(STR_LOC.NOV_MARKUS_HOUSE, "qst_Terminus_PathBlockMarkusHouse")
                elif GetLocID() == "novaras_dist_house_south":
                    btnMods["btn_novaras_church"] = BtnJumpLabel(STR_LOC.NOV_CHURCH, "qst_Terminus_PathBlockChurch")
                elif GetLocID() == "novaras_dist_mage":
                    btnMods["btn_novaras_palam_mainhall_door"] = BtnJumpLabel(STR_LOC.NOV_PALAM, "qst_Terminus_PathBlockPalam")
                elif GetLocID() == "novaras_dist_farm":
                    btnMods["btn_novaras_blacksmith"] = BtnJumpLabel(STR_LOC.NOV_BLACKSMITH, "qst_Terminus_PathBlockSmithy")
                elif GetLocID() == "novaras_dist_edu":
                    btnMods["btn_novaras_library"] = BtnJumpLabel(STR_LOC.NOV_LIBRARY_INT, "qst_Terminus_PathBlockLibrary")
                elif GetLocID() == "novaras_dist_army":
                    btnMods["btn_novaras_gates_exit_city"] = BtnJumpLabel(STR_LOC.NOV_GATES, "qst_Terminus_PathBlockGates")
                    btnMods["btn_novaras_fort_seb"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT, "qst_Terminus_PathBlockSebastian")
                elif GetLocID() == "novaras_market_stalls":
                    btnMods["btn_novaras_market_stalls_butcher"] = BtnDisabled()
                elif GetLocID() == "novaras_dist_pleasure":
                    btnMods["btn_novaras_soothsayer_cabin"] = BtnJumpLabel(STR_LOC.NOV_WITCH_HOUSE, "qst_Terminus_PathBlockWitchHouse")
                elif GetLocID() == "novaras_dist_market":
                    btnMods["btn_novaras_clothes"] = BtnJumpLabel(STR_LOC.NOV_CLOTHES_STORE, "qst_Terminus_PathBlockClothesStore")
                    btnMods["btn_novaras_store_int"] = BtnJumpLabel(STR_LOC.NOV_GENERAL_STORE, "qst_Terminus_PathBlockGeneralStore")
                    btnMods["btn_novaras_adv_guild"] = BtnJumpLabel(STR_LOC.NOV_ADV_GUILD, "qst_Terminus_PathBlockAdventurersGuild")
                    btnMods["btn_novaras_tavern"] = BtnJumpLabel(STR_LOC.NOV_TAVERN, "qst_Terminus_PathBlockTavern")
                elif GetLocID() == "mc_house_bedroom":
                    btnMods["btn_mc_house_bed"] = BtnJumpLabel(_("Bed"), "qst_Terminus_CantSleep")
                elif GetLocID() == "mc_house_kitchen":
                    btnMods["talkRegina"] = BtnDisabled()
            # stage 3 location blocks/mods, (RIGGED NIGHT) "go to either adara or nijah"
            elif self.progress == 3:
                if GetLocID() == "novaras_dist_army":
                    btnMods["btn_novaras_gates_exit_city"] = BtnJumpLabel(STR_LOC.NOV_GATES, "qst_Terminus_PathBlockGates")
                    btnMods["btn_novaras_fort_seb"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT, "HouseLock_SebastianGuard")
                elif GetLocID() == "mc_house_bedroom":
                    btnMods["btn_mc_house_bed"] = BtnJumpLabel(_("Bed"), "qst_Terminus_CantSleep")
                elif GetLocID() == "novaras_adv_guild":
                    btnMods["btn_novaras_guild_board"] = BtnJumpLabel(STR_LOC.NOV_ADV_GUILD, "qst_Terminus_GuildBoard")
                elif GetLocID() == "mc_house_kitchen":
                    btnMods["talkRegina"] = BtnDisabled()
            # stage 4 location blocks/mods, (RIGGED NIGHT) "go home"
            elif self.progress == 4:
                if GetLocID() == "novaras_bordello_ext":
                    btnMods["novaras_bordello_door"] = BtnJumpLabel(STR_NAV.ENTER, "qst_Terminus_PathBlockBordelloInterior")
                    btnMods["shani_talk_btn"] = BtnDisabled()
                elif GetLocID() == "novaras_dist_army":
                    btnMods["btn_novaras_gates_exit_city"] = BtnJumpLabel(STR_LOC.NOV_GATES, "qst_Terminus_PathBlockGates")
                    btnMods["btn_novaras_fort_seb"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT, "HouseLock_SebastianGuard")
                elif GetLocID() == "novaras_dist_market":
                    btnMods["btn_novaras_tavern"] = BtnJumpLabel(STR_LOC.NOV_TAVERN, "qst_Terminus_PathBlockTavern2")
                elif GetLocID() == "novaras_adv_guild":
                    btnMods["btn_novaras_guild_board"] = BtnJumpLabel(STR_LOC.NOV_ADV_GUILD, "qst_Terminus_GuildBoard")
                elif GetLocID() == "novaras_dist_house":
                    btnMods["btn_markus_house"] = BtnJumpLabel(STR_LOC.NOV_MARKUS_HOUSE, "qst_Terminus_PathBlockMarkusHouse2")
                elif GetLocID() == "mc_house_kitchen":
                    btnMods["talkRegina"] = BtnDisabled()
            # stage 5 location blocks/mods "go to fort"
            elif self.progress == 5:
                if GetLocID() == "novaras_dist_market":
                    btnMods["btn_novaras_clothes"] = BtnJumpLabel(STR_LOC.NOV_CLOTHES_STORE, "qst_Terminus_PathBlockClothesStore_2")
                elif GetLocID() == "novaras_dist_house":
                    btnMods["btn_markus_house"] = BtnJumpLabel(STR_LOC.NOV_MARKUS_HOUSE, "HouseLockLines")
                    btnMods["btn_mc_house"] = BtnJumpLabel(STR_LOC.NOV_MC_HOUSE, "qst_Terminus_CantGoHomeNow")
                elif GetLocID() == "novaras_dist_army":
                    btnMods["btn_novaras_gates_exit_city"] = BtnJumpLabel(STR_LOC.NOV_GATES, "qst_Terminus_PathBlockGates")
                    btnMods["btn_novaras_fort_seb"] = BtnChangeLoc(STR_LOC.NOV_CITY_FORT, "novaras_fort_seb_yard")
                elif GetLocID() == "novaras_market_stalls":
                    btnMods["btn_novaras_market_stalls_butcher"] = BtnDisabled()
                elif GetLocID() == "novaras_adv_guild":
                    btnMods["btn_novaras_guild_board"] = BtnJumpLabel(STR_LOC.NOV_ADV_GUILD, "qst_Terminus_GuildBoard")
                elif GetLocID() == "novaras_palam_mainhall":
                    btnMods["btn_palam_mainhall_to_w_wing"] = BtnDisabled()
                    btnMods["btn_palam_mainhall_to_e_wing"] = BtnDisabled()
                elif GetLocID() == "novaras_dist_farm":
                    btnMods["btn_novaras_blacksmith"] = BtnJumpLabel(STR_LOC.NOV_BLACKSMITH, "qst_Terminus_PathBlockSmithy2")
                elif GetLocID() == "mc_house_kitchen":
                    btnMods["talkRegina"] = BtnDisabled()

            return LocButtonMod(directMods = btnMods, priority = 1)

        def onStart(self):
            AddItemTo(chest_mc_house, "gold", self.InitialGold)

            store.ShowDialogueHistoryButton = True

            AutoTimeFreeze(True)
            BlockWaitGlobal(True)

            store.gui_parts["location_name"] = True
            store.gui_parts["time_tracker"] = True
            store.gui_parts["access_buttons"] = True
            store.gui_parts["journal"] = True
            store.gui_parts["inventory"] = True
            store.gui_parts["relations"] = True
            store.gui_parts["party_panel"] = True

            # starting this quest is like an "entry point" to initialize all our story chars btw
            QstStart(ContainerMCHouseChest)

            QstStart(DialogueAdara)
            QstStart(DialogueArlena)
            QstStart(DialogueArwen)
            QstStart(DialogueButcher)
            QstStart(DialogueDivine)
            QstStart(DialogueDrax)
            QstStart(DialogueDros)
            QstStart(DialogueFawha)
            QstStart(DialogueGerard)
            QstStart(DialogueHelena)
            QstStart(DialogueLuciusMal)
            QstStart(DialogueMarkus)
            QstStart(DialogueMika)
            QstStart(DialogueNijah)
            QstStart(DialogueNyx)
            QstStart(DialogueRegina)
            QstStart(DialogueShani)
            QstStart(DialogueShay)
            QstStart(DialogueThea)
            QstStart(DialogueVala)

            QstStart(EventMadProphet)
            QstStart(EventNovarasHangings)

            QstStart(HouseLockBlackDiamond)
            QstStart(HouseLockFortSebastian)
            QstStart(HouseLockMarkusHouse)
            QstStart(HouseLockNovPalace)
            QstStart(HouseLockNovarasBordelloDoor)
            QstStart(HouseLockNovarasBordelloExt)
            QstStart(HouseLockNovarasClothesStore)
            QstStart(HouseLockNovarasGeneralStore)
            QstStart(HouseLockNovarasLibrary)
            QstStart(HouseLockNovarasSmithy)
            QstStart(HouseLockPalamTower)
            QstStart(HouseLockPalamTowerRooms)
            QstStart(NovarasSoothsayer)

            return

        def onItemAcquired(self, item_ID, Amount):
            if self.progress == 0:
                if item_ID == "gold":
                    if PlayerItemQty("gold") >= self.InitialGold:
                        renpy.hide_screen("container")
                        renpy.hide_screen("transfer_item")
                        renpy.jump("qst_Terminus_AtHouseGrabbedGold")
            return

        def onComplete(self):
            store.ShowLevelUpFloatingText = True

            AutoTimeFreeze(False)

            # for autofinish
            CharMeet("markus", DefaultRel = "rel_friend", Silent = True)
            CharMeet("adara",  DefaultRel = "rel_friend", Silent = True)
            if self.AdaraOrNijah == "adara":
                CharSetLover("adara", Silent = True)
            if self.AdaraOrNijah == "nijah":
                CharMeet("nijah", Silent = True)
            CharMeet("erika", DefaultRel = "rel_friend", Silent = True)
            RelSet_Erika()
            CharMeet("regina", DefaultRel = "rel_friend", Silent = True)
            RelSet_Regina()
            CharMeet("alcott", Silent = True)
            return

label qst_Terminus_AtHouseGrabbedGold:
    MC "That's better."
    $ QstSetProgress(QstTerminus, 1)
    MC "Time to head out."
    $ LocEnterQ()

label qst_Terminus_PathBlockMarkusHouse:
    MC "Markus' house."
    MC "He must already be at the ceremony!"
    MC "I should get to the Royal Palace."
    $ LocEnterQ()

label qst_Terminus_PathBlockMarkusHouse2:
    MC "Markus must already be sleeping."
    MC "Whatever tomorrow brings, we better face it well-rested..."
    $ LocEnterQ()

label qst_Terminus_PathBlockChurch:
    MC "The Church of Al'Vazah."
    MC "People come here to sate their spiritual hunger."
    MC "Never really worked for me, though."
    $ LocEnterQ()

label qst_Terminus_PathBlockPalam:
    MC "The Mages of Palam tower, the place they study the arcane in."
    MC "Sometimes I wonder what kind of secrets are being explored and exploited within it's walls..."
    $ LocEnterQ()

label qst_Terminus_PathBlockSmithy:
    MC "Here lives one of the most proficient blacksmiths in the whole Novaras, Drax."
    MC "His daughter, Arlena, is quite a piece of work."
    MC "I should really get going."
    MC "Missing the Terminus Ceremony is not a great way to enter one's adulthood..."
    $ LocEnterQ()

label qst_Terminus_PathBlockSmithy2:
    play sound door_knock
    MC "..."
    $ Pause(0.5)
    MC "Looks like nobody's home."
    MC "I should go."
    $ LocEnterQ()

label qst_Terminus_PathBlockLibrary:
    MC "City library."
    MC "I never been too much of a reader, but the ladies here are quite a sight."
    MC "However, today I'll get to steal a glimpse of the princess herself at the Royal Palace!"
    MC "She is quite unmatched in many departments."
    $ LocEnterQ()

label qst_Terminus_PathBlockGates:
    "As I approached the city gates, I couldn't help but marvel at the colossal defenses."
    MC "These gates are the only way in and out of the city."
    MC "Encircled by walls so formidable, Novaras truly is an impenetrable city."
    MC "...or, a death trap."
    $ LocEnterQ()

label qst_Terminus_PathBlockSebastian:
    MC "The great Fort Sebastian. City garrison is stationed here, along with a considerable detachment of Emperor Alcott's army."
    "As I was ogling the walls and towers of the old but well-maintained fort, a guard strolled over my way."
    show cg_guard at center_f with dissolve
    GUARD "Citizen! Shouldn't you be at the ceremony?"
    MC "Oh, I'm on my way there."
    "The guard observed me suspiciously as I moved on."
    $ LocEnter()

label qst_Terminus_WalkIntoMarket:
    MC "This place is the heart of the city's commerce."
    MC "{b}Everything{/b} is being bought or sold here, especially during such an important day of the year."
    "As I walked through the market, I heard various merchants hollering at an agitated crowd of commoners headed towards the Royal Palace."
    MC "What exactly am I doing wandering about here?"
    $ LocEnterQ()

label qst_Terminus_PathBlockClothesStore:
    MC "If memory serves, this place is where all the top ladies go to get some... exquisite garments."
    MC "Not that I needed something like that at the moment."
    $ LocEnterQ()

label qst_Terminus_PathBlockClothesStore_2:
    MC "That's weird, the place seems to be locked down in a hurry."
    MC "There's a paper nailed to the front door..."
    "{i}I had to shut down the store and move out of the city.{/i}"
    "{i}I present my sincerest apology to all the regular clientele.{/i}"
    "{i}It was the only way to avoid a preposterous scandal.{/i}"
    "{i}I won't go into further details here, the only thing I will say is, {b}fuck elves.{/b}{/i}"
    "{i}— Klaus Nevelinge, your humble fashionista.{/i}"
    MC "Elves? What could that be about?"
    $ LocEnterQ()

label qst_Terminus_PathBlockGeneralStore:
    MC "City general store."
    MC "Anything you cannot find at the market can be found in here."
    $ LocEnterQ()

label qst_Terminus_PathBlockAdventurersGuild:
    MC "Oh, the Adventurers Guild."
    MC "A very bizzare way to encourage people to deal with the problems the Emperor's regime can't handle..."
    MC "Although the guild members are quite popular, given the nature of the job."
    $ LocEnterQ()

label qst_Terminus_GuildBoard:
    MC "A guild quest board."
    MC "From what I know about the guild, it is {i}the{/i} way the adventurers are employed."
    MC "Any trouble the state can't handle can be turned into a 'quest' for the guild to present as a contract."
    MC "Not like I'll be involved in any of this, now that I'm a scout..."
    $ LocEnterQ()

label qst_Terminus_PathBlockTavern:
    MC "The Iron Unicorn, a place me and Markus are regulars of."
    MC "I can only imagine what the place will turn into after today's celebration..."
    $ LocEnterQ()

label qst_Terminus_PathBlockTavern2:
    MC "I can hear the celebration from the outside..."
    MC "*Sigh* time to head home for today."
    $ LocEnterQ()

label qst_Terminus_PathBlockBordelloInterior:
    MC "I've had enough 'fun' today..."
    MC "Gotta head home now."
    $ LocEnterQ()

label qst_Terminus_PathBlockWitchHouse:
    MC "Even standing nearby that cabin gives me the creeps..."
    MC "I should go to the ceremony."
    $ LocEnterQ()

label qst_Terminus_CantSleep:
    MC "Now is not the time to rest."
    MC "That comes later."
    $ LocEnterQ()

label qst_Terminus_CantGoHomeNow:
    MC "I... No."
    MC "I cannot make [regina_ref!t] go through any more of this..."
    MC "Let's get on with it and go to Fort Sebastian."
    $ LocEnterQ()

# exclusively for that drafted scene
screen PrologueLetterText():
    zorder -5
    style_prefix "prologue_letter" # for text styles
    label _("Loyal Citizen!"):
        align (0.5, 0.32) 
        style "prologue_letter_title"

    text _("You have been bestowed the honor and privilege of joining\nthe Scouts Corp!"):
        align (0.5, 0.42)
        style "prologue_letter_text_main"
        text_align 0.5

    text _("Please report to Fort Sebastian to begin your training at once!"):
        align (0.5, 0.54)
        style "prologue_letter_text_main"

    text _("Warning: failure to show up in a day since removing the seal from\nthis letter is a capital offense as of 1134.03.19"):
        align (0.5, 0.66)
        style "prologue_letter_text_sub"
        text_align 0.5

    text _("Royal Prosecutor Horace Abertix, 1163.04.20"):
        align (0.5, 0.74)
        style "prologue_letter_text_sub"
