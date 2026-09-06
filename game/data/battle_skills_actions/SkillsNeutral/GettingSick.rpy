init python:
    @RegisterBattleSkill("NeutralGettingSick")
    class BattleSkill_NeutralGettingSick(BattleSkill):
        DisplayName = _("Getting Sick")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 50

        DamageValue = {1:1.2}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        AIBaseWeight = 4.0

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_HealthRecoveryMod(ResRecoverMod_Health = 0.3, Duration = 2, SourceName = self.DisplayName, StatusEffectID = "neutral_getsick_hpregendebuff")),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_EnergyRecoveryMod(ResRecoverMod_Energy = 0.3, Duration = 2, SourceName = self.DisplayName, StatusEffectID = "neutral_getsick_epregendebuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Attacks all enemies for %s damage and reduces their health and energy recovery by 70%% for 2 turns.")) % DamageValue