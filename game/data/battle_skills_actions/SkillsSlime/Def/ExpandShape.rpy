init python:
    @RegisterBattleSkill("SlimeExpandShape")
    class BattleSkill_SlimeExpandShape(BattleSkill):
        DisplayName = _("Expand Shape")
        Icon = "images/battle_skill_icons/slime/ExpandShape.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 70

        OwnDamageResBuff =     {1:0.6, 2:0.5, 3:0.4}
        AlliesDamageResBuff =  {1:0.4, 2:0.3, 3:0.2}

        AITags = {AI_TAGS.RAISE_TARGET_PHYS_DAMAGE_RESISTANCE, AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE}

        def Execute(self, Target):
            Battle_ScheduledCast(
    
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(
                            Duration = 2,
                            DamageRecieved_Mod = self.OwnDamageResBuff[self.Level], 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "slime_expshape_self_dmgres"))])

            TargetAllies = Battle_GetAliveCharsOnSide(self.Owner_BattleChar.BattleSide)
            TargetAllies.remove(self.Owner_BattleChar)
            for Char in TargetAllies:
                Battle_ApplyStatusEffect(
                    TargetChar = Char, 
                    StatusEffect = BattleStatusEff_DamageIn(
                        Duration = 2,
                        DamageRecieved_Mod = self.AlliesDamageResBuff[self.Level], 
                        SourceName = self.DisplayName, 
                        StatusEffectID = "slime_exshape_ally_dmgres"))
            return

        def GetDesc(self, DescLevel = 1):
            OwnDmgResPerc = Battle_FormatDescVal(round((1.0 - self.OwnDamageResBuff[DescLevel]) * 100), Percentage = True)
            AlliesDmgResPerc = Battle_FormatDescVal(round((1.0 - self.AlliesDamageResBuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Increases your damage resistance by %s and that of the allies by %s for 2 turns.")) % (OwnDmgResPerc, AlliesDmgResPerc)
