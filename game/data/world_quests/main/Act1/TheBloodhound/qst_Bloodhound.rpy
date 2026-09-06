init python:
    @AppendToAllQuests
    class QstTheBloodhound(BaseQuest):
        TITLE = _("The Bloodhound")
        DESCRIPTION = _("Novaras City Guard informant has gone missing.")
        GOALS = {
            0: QuestStage(_("Speak to Captain Nyx"), 
                trackTag = "btn_novaras_fort_seb", 
                hintTxt = _("I should speak to Captain Nyx about the informant.")),
            1: QuestStage(_("Investigate The Adventurers Guild"), 
                trackTag = "btn_novaras_adv_guild", 
                hintTxt = _("Azul, the Novaras Guard informant was last seen speaking to a certain group of adventurers at the guild. I should start there.")),
            2: QuestStage(_("Go to the Balun lake"), 
                hintTxt = _("The Guardians of the Realm, an adventurers group Azul was in contact with, went out to tackle a giant slimelark. Thea says the thing is dangerous, I should prepare before I head out to catch up with them."),
                trackTagWorldMap = "lake_balun"),
            3: QuestStage(_("Defeat the Giant Slimelark"), 
                hintTxt = _("No wonder I could not find the Guardians group. They have met their horrible end at the... hands of a giant slimelark.")),
            4: QuestStage(_("Go to Azul's safehouse"), 
                hintTxt = _("Dravenham, a knight that almost survived a giant slimelark encounter, gave me an address of Azul's safehouse. It's in housing district, not far from my home..."), 
                trackTag = "btn_azul_safehouse"),
            5: QuestStage(_("Survive the Man in Black"), 
                hintTxt = _("I have found Azul. What's left of him anyways. The... thing that had him turned into a bird cage is after me now. No turning back, I've gotta fight for my life."))
            }

        def __init__(self):
            super().__init__()

            self.XpReward = 1100
            self.clues = [] # at camp, clicking some stuff adds to this
            self.sawChainedUpBox = False
            self.rugPulled = False
            self.basementOpen = False
            self.azulSafehouseOneOff = True
            self.basementHatchOpen = False
            self.suggestedLevel = 7

            self.IsMain = True


        def extraDialogue(self):
            if self.progress == 0:
                yield ("nyx_root", DNode(_("About this job..."), "qst_bloodhound_0_pitch_revisit"))
            elif self.progress == 1:
                yield ("thea_root", DNode(_("What can you tell me about the 'Guardians of the Realm?'"), "qst_bloodhound_1_TheaOnGuardians"))

        def onEnterOnce(self):
            if GetLocID() == "novaras_adv_guild":
                if IsDaytime():
                    if self.progress == 1:
                        return TriggeredEvent("qst_bloodhound_1_guild_onEnter")

        def OverrideLocBg(self):
            Result = {}
            if GetLocID() == "lake_balun":
                if self.progress in [2, 3]:
                    Result["lake_balun"] = "bg_lake_balun_camp"
            elif GetLocID() == "azul_safehouse":
                if self.progress == 4:
                    Result["azul_safehouse"] = "bg_azul_room_dirty_rug"
                    if self.rugPulled:
                        if self.basementHatchOpen:
                            Result["azul_safehouse"] = "bg_azul_room_dirty_open"
                        else:
                            Result["azul_safehouse"] = "bg_azul_room_dirty_norug"
            elif GetLocID() == "azul_safehouse_bedroom":
                if self.progress == 4:
                    Result["azul_safehouse_bedroom"] = "bg_azul_bedroom_dirty"
            return Result

        def onEnter(self):  
            if GetLocID() == "azul_safehouse":
                if self.progress == 4:
                    wLocs["azul_safehouse"].dn_music.dayTrack = "audio/music/13_AbandFort.ogg"
                    wLocs["azul_safehouse"].dn_music.nightTrack = "audio/music/13_AbandFort.ogg"
                    if self.azulSafehouseOneOff:
                        return TriggeredEvent("qst_bloodhound_3_safehouse_onenter")    
            elif GetLocID() == "azul_safehouse_bedroom":
                if self.progress == 4:
                    wLocs["azul_safehouse_bedroom"].dn_music.dayTrack = "audio/music/13_AbandFort.ogg"
                    wLocs["azul_safehouse_bedroom"].dn_music.nightTrack = "audio/music/13_AbandFort.ogg"

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "lake_balun":
                if self.progress == 2:
                    btnMods["lake_balun_camp"] = BtnJumpLabel(_("Camp"), "qst_bloodhound_2_camp")
                    if all(x in QstTheBloodhound().clues for x in ['note', 'sigil']):
                        btnMods["lake_balun_water"] = BtnJumpLabel(_("Approach the lake"),"qst_bloodhound_2_lake")
            elif GetLocID() == "azul_safehouse":
                if self.progress == 4:
                    if not self.rugPulled:
                        btnMods["btn_azul_rug"] = BtnJumpLabel(_("A rug"),"qst_bloodhound_3_azul_rug")
                    if self.rugPulled:
                        if self.basementOpen:
                            btnMods["btn_azul_to_basement"] = BtnJumpLabel(_("Basement hatch"),"qst_bloodhound_3_azul_hatch_unlock")
                        else:
                            btnMods["btn_azul_to_basement"] = BtnJumpLabel(_("Basement hatch"),"qst_bloodhound_3_azul_hatch_cant_unlock")
                        if self.basementHatchOpen:
                            btnMods["btn_azul_to_basement"] = BtnJumpLabel(_("Basement hatch"),"qst_bloodhound_3_azul_basement_hatch")
                    btnMods["btn_azul_fireplace"] = BtnJumpLabel(_("A fireplace"), "qst_bloodhound_3_fireplace")
            elif GetLocID() == "azul_safehouse_bedroom":
                if self.progress == 4:
                    btnMods["btn_azul_monster_drawing"] = BtnJumpLabel(_("Drawing of a monster"), "qst_bloodhound_3_azul_monster")
                    btnMods["btn_azul_mad_ramblings"] = BtnJumpLabel(_("Mad ramblings"), "qst_bloodhound_3_azul_mad_ramblings")
                    btnMods["btn_azul_bed"] = BtnJumpLabel(_("A bed"), "qst_bloodhound_3_azul_filthy_bed")
                    btnMods["btn_azul_strange_book"] = BtnJumpLabel(_("Strange purple book"), "qst_bloodhound_3_azul_strange_book")
            return LocButtonMod(directMods = btnMods)

        def onComplete(self):
            QstStart(EventMcNewArmor)
            QstStart(PrimerTwoEmperors)
            if PlayerItemQty("qst_slime_jar") > 0:
                QstStart(PrimerSlimeJar)
            QstComplete(HouseLockAzul)
            QstStart(PrimerTheSlavemaster)
            QstSetDelay(PrimerTheSlavemaster, 2)
            QstStart(PrimerGirlTroubles)
            return