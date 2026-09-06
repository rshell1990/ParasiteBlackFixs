init python:
    @RegisterBattleSkill("BerserkerHealingWounds")
    class BattleSkill_BerserkerHealingWounds(BattleSkill):
        DisplayName = _("Healing Wounds")

        Icon = "images/battle_skill_icons/berserker/HealingWounds.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 70

        HealthRecoveredValues = {1:0.1, 2:0.15, 3:0.25}

        AITags = {AI_TAGS.HEAL_SELF, AI_TAGS.EFFECT_SCALES_WITH_AMOUNT_OF_DEBUFFS_ON_TARGET, AI_TAGS.REMOVE_DEBUFFS_ON_TARGET}

        def Execute(self, Target):
            DebuffsFound = 0
            for StatusEffect in self.Owner_BattleChar.StatusEffects:
                if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                    DebuffsFound += 1

            Battle_ScheduledCast(
                 
                SourceSkillObj = self,
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_RestoreHealth(RestoreValue = self.HealthRecoveredValues[self.Level] + (0.15 * DebuffsFound), RatioFromMax = True),
                    BattleEffect_RemoveDebuffsOnTarget()])

            if DebuffsFound > 0:
                Battle_ApplyStatusEffect(
                    TargetChar = self.Owner_BattleChar, 
                    StatusEffect = BattleStatusEff_DamageOut(
                        DamageDealt_Mod = 1.0 + (0.15 * DebuffsFound), 
                        Duration = 1, 
                        SourceName = self.DisplayName,
                        StatusEffectID = "bers_healingwounds_dmgout"))
            return

        def GetDesc(self, DescLevel = 1):
            BaseHealthRecoveredPerc = Battle_FormatDescVal(round(self.HealthRecoveredValues[DescLevel] * 100), Percentage = True)
            return tra(_("Removes all harmful effects and recovers your hp by %s + 15%% for each harmful effect removed. It also increases your damage dealt by 15%% for each harmful effect removed for 1 turns.")) % BaseHealthRecoveredPerc