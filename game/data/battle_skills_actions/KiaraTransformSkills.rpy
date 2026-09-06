init python:
    @RegisterBattleSkill("KiaraTransform")
    class BattleSkill_KiaraTransform(BattleSkill):
        Icon = "images/battle_skill_icons/kiara_transform.webp"
        DisplayName = _("Transform")

        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 40


        def Execute(self, Target):
            HPRatio = self.Owner_BattleChar.Health / self.Owner_BattleChar.HealthMax
            Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar,
                                    StatusEffect = BattleStatusEff_TransformedDemorai())
            self.Owner_BattleChar.Health = ClampValue(math.ceil(self.Owner_BattleChar.HealthMax * HPRatio), 1, self.Owner_BattleChar.HealthMax)

            Battle_SetBattleCharSkin(self.Owner_BattleChar, self.Owner_BattleChar.SkinID_AltForm)
            Battle_SetBattleCharSkillPool(self.Owner_BattleChar, "AltForm")
            Battle_LoopStep(0.1)
            Battle_RunCharAnim(self.Owner_BattleChar, "idle")

            self.Owner_BattleChar.CharRef["Transformed"] = True

            Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar,
                                    StatusEffect = BattleStatusEff_Immunity(
                                    Duration = 3, 
                                    SourceName = self.DisplayName))
            
            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                String = tra(_("USER_NAME transforms!")))
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Transform into a demorai form. In demorai form, Kiara's agility is increased by 50%. Gains immunity for 3 turns."))

######################################################################
    @RegisterBattleSkill("KiaraUnTransform")
    class BattleSkill_KiaraUnTransform(BattleSkill):
        Icon = "images/battle_skill_icons/kiara_untransform.webp"
        DisplayName = _("Transform")

        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 20

        def Execute(self, Target):
            #Battle_PlayCharSkinSound("Transform", self.Owner_BattleChar, Voice = True)

            HPRatio = self.Owner_BattleChar.Health / self.Owner_BattleChar.HealthMax
            Battle_RemoveStatusEffect(self.Owner_BattleChar, "transformed_demorai")
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
            return tra(_("Transform back into the human form and get extra turn."))