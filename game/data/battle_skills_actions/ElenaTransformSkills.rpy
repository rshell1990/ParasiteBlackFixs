init python:
    @RegisterBattleSkill("ElenaTransform")
    class BattleSkill_ElenaTransform(BattleSkill):
        DisplayName = _("Transform")
        Icon = "images/characters/elena/portrait_wolf.webp"
        
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 50
        AutoSelectNextInPartyOnExecute = False

        def Execute(self, Target):
            # add VFX
            Battle_PlayCharSkinSound("Transform", self.Owner_BattleChar, Voice = True)

            HPRatio = self.Owner_BattleChar.Health / self.Owner_BattleChar.HealthMax
            Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar,
                                    StatusEffect = BattleStatusEff_TransformedWolf())
            self.Owner_BattleChar.Health = ClampValue(math.ceil(self.Owner_BattleChar.HealthMax * HPRatio), 1, self.Owner_BattleChar.HealthMax)

            Battle_SetBattleCharSkin(self.Owner_BattleChar, self.Owner_BattleChar.SkinID_AltForm)
            Battle_SetBattleCharSkillPool(self.Owner_BattleChar, "AltForm")
            Battle_LoopStep(0.1)
            Battle_RunCharAnim(self.Owner_BattleChar, "idle")

            self.Owner_BattleChar.CharRef["Transformed"] = True

            Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar,
                                    StatusEffect = BattleStatusEff_DamageOut(
                                        DamageDealt_Mod = 1.4,
                                        Duration = 2,
                                        SourceName = self.DisplayName))

            Battle_GrantExtraTurn(self.Owner_BattleChar)
            
            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                String = tra(_("USER_NAME transforms!")))
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Transform into the wolf form.\nIn wolf form, Elena's strength and agility are increased by 50%, but her endurance is reduced by 25%.\nIncreases your damage dealt by 40% for 2 turns and gains another turn immediately."))

######################################################################
    @RegisterBattleSkill("ElenaUnTransform")
    class BattleSkill_ElenaUnTransform(BattleSkill):
        Icon = "images/characters/elena/portrait.webp"
        DisplayName = _("Transform")

        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 30
        AutoSelectNextInPartyOnExecute = False

        def Execute(self, Target):
            # VFX, 
            # Attr multiplier status effect remove
            # scale HP/EP accordingly
            Battle_PlayCharSkinSound("Transform", self.Owner_BattleChar, Voice = True)
            Battle_SetBattleCharSkin(self.Owner_BattleChar, self.Owner_BattleChar.SkinID_Normal)

            HPRatio = self.Owner_BattleChar.Health / self.Owner_BattleChar.HealthMax
            Battle_RemoveStatusEffect(self.Owner_BattleChar, "transformed_wolf")
            self.Owner_BattleChar.Health = ClampValue(math.ceil(self.Owner_BattleChar.HealthMax * HPRatio), 1, self.Owner_BattleChar.HealthMax)

            Battle_SetBattleCharSkillPool(self.Owner_BattleChar, "Normal")
            Battle_LoopStep(0.1)
            Battle_RunCharAnim(self.Owner_BattleChar, "idle")

            self.Owner_BattleChar.CharRef["Transformed"] = False

            Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar,
                                    StatusEffect = BattleStatusEff_StatMod_Armor(
                                        StatMod_Armor = 1.4,
                                        Duration = 2,
                                        SourceName = self.DisplayName))

            Battle_GrantExtraTurn(self.Owner_BattleChar)

            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                String = tra(_("USER_NAME transforms!")))
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Transform back into the human form.\nIncreases your armor by 40% for 2 turns and gains another turn immediately."))