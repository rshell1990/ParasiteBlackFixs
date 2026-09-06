init python:
    @RegisterBattleSkill("ParasiteWhiteInfernalParasite")
    class BattleSkill_ParasiteWhiteInfernalParasite(BattleSkill):
        DisplayName = _("Infernal Parasite")
        
        Icon = "images/battle_skill_icons/parawhite/InfernalParasite.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 50

        EnemyRecoveryDebuff =      {1:0.6,     2:0.5,  3:0.4,  4:0.4}
        StolenHealthPercentage =   {1:0.05,    2:0.05, 3:0.05, 4:0.1} 

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.HEAL_SELF}

        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledAttack(
                GuaranteedHit = True,
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                AbsorbTarget_HealthMax = self.StolenHealthPercentage[self.Level],
                DamageMod = 0.4,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_HealthRecoveryMod(
                            ResRecoverMod_Health = self.EnemyRecoveryDebuff[self.Level], 
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "parawhite_infernal_hp_regen_debuff")),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_EnergyRecoveryMod(
                            ResRecoverMod_Energy = self.EnemyRecoveryDebuff[self.Level], 
                            Duration = 2,
                            SourceName = self.DisplayName, 
                            StatusEffectID = "parawhite_infernal_ep_regen_debuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, 0.4), Parentheses = False)
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, 0.4), Parentheses = False)

            RecoveryPercentage = Battle_FormatDescVal(round((1.0 - self.EnemyRecoveryDebuff[DescLevel]) * 100), Percentage = True)
            HealthAbsorbedPerc = Battle_FormatDescVal(round(self.StolenHealthPercentage[DescLevel] * 100), Percentage = True)
            return tra(_("Unleashes small parasites on all enemies, dealing %s damage and decreasing their health and energy recovery by %s for 2 turns.\nAbsorbs each target's health equal to %s of their max hitpoints.")) % (StrikeDamage, RecoveryPercentage, HealthAbsorbedPerc)