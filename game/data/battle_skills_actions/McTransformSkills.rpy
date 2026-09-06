init python:
    @RegisterBattleSkill("McTransform")
    class BattleSkill_MCTransform(BattleSkill):
        Icon = "images/battle_skill_icons/mc_transform.webp"
        DisplayName = _("Transform")

        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Infection = 20

        def Execute(self, Target):
            # add vfx
            Battle_PlayCharSkinSound("Transform", self.Owner_BattleChar, Voice = True)

            for EnemyBattleChar in Battle_GetAllEnemiesOfChar(self.Owner_BattleChar):
                Battle_ApplyStatusEffect(TargetChar = EnemyBattleChar, 
                                    StatusEffect = BattleStatusEff_DamageOut(0.6, 2, 
                                        SourceName = self.DisplayName, 
                                        StatusEffectID = "transform_frighten"),
                                    CastOnEnemy = True)

            HPRatio = self.Owner_BattleChar.Health / self.Owner_BattleChar.HealthMax
            Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar, 
                                    StatusEffect = BattleStatusEff_TransformedPara())
            self.Owner_BattleChar.Health = ClampValue(math.ceil(self.Owner_BattleChar.HealthMax * HPRatio), 1, self.Owner_BattleChar.HealthMax)

            Battle_SetBattleCharSkin(self.Owner_BattleChar, self.Owner_BattleChar.SkinID_AltForm)

            Battle_SetBattleCharSkillPool(self.Owner_BattleChar, "AltForm")
            Battle_LoopStep(0.1)
            Battle_RunCharAnim(self.Owner_BattleChar, "idle")

            self.Owner_BattleChar.CharRef["Transformed"] = True
            
            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                String = tra(_("USER_NAME transforms!")))
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Transform into your parasite form.\nWill boost all your attributes by 50% and frighten all enemies, reducing the damage they deal by 40% for 2 turns."))
######################################################################
    @RegisterBattleSkill("McUnTransform")
    class BattleSkill_MCUnTransform(BattleSkill):
        Icon = "images/battle_skill_icons/mc_untransform.webp"
        DisplayName = _("Transform")

        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 20
        AutoSelectNextInPartyOnExecute = False

        def Execute(self, Target):
            # VFX, 
            
            Battle_PlayCharSkinSound("Transform", self.Owner_BattleChar, Voice = True)

            HPRatio = self.Owner_BattleChar.Health / self.Owner_BattleChar.HealthMax
            Battle_RemoveStatusEffect(self.Owner_BattleChar, "transformed_para")
            self.Owner_BattleChar.Health = ClampValue(math.ceil(self.Owner_BattleChar.HealthMax * HPRatio), 1, self.Owner_BattleChar.HealthMax)

            Battle_SetBattleCharSkin(self.Owner_BattleChar, self.Owner_BattleChar.SkinID_Normal)
            Battle_SetBattleCharSkillPool(self.Owner_BattleChar, "Normal")
            Battle_LoopStep(0.1)
            Battle_RunCharAnim(self.Owner_BattleChar, "idle")

            self.Owner_BattleChar.CharRef["Transformed"] = False

            Battle_GrantExtraTurn(self.Owner_BattleChar)

            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                String = tra(_("USER_NAME transforms!")))
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Transform back into your human form and get extra turn."))