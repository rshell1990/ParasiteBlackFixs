init python:
    @RegisterBattleSkill("ParasiteBlackHealingWorms")
    class BattleSkill_ParasiteBlackHealingWorms(BattleSkill):
        DisplayName = _("Healing Worms")

        Icon = "images/battle_skill_icons/parablack/HealingWorms.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 100

        RecoverValue = {1:0.2, 2:0.25, 3:0.3}

        AITags = {AI_TAGS.HEAL_SELF, AI_TAGS.EFFECT_SCALES_WITH_AMOUNT_OF_DEBUFFS_ON_TARGET, AI_TAGS.REMOVE_DEBUFFS_ON_TARGET}

        def Execute(self, Target):
            DebuffCountOnSelf = 0
            for StatusEffect in reversed(self.Owner_BattleChar.StatusEffects):
                if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                    DebuffCountOnSelf += 1
                    self.Owner_BattleChar.StatusEffects.remove(StatusEffect)
            RecoverPercentage = round(self.RecoverValue[self.Level] * 100) + (DebuffCountOnSelf * 5)
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [BattleEffect_RestoreHealth(RestoreValue = round((self.Owner_BattleChar.HealthMax / 100) * RecoverPercentage)),
                                    BattleEffect_RestoreEnergy(RestoreValue = round((self.Owner_BattleChar.EnergyMax / 100) * RecoverPercentage))])
            return

        def GetDesc(self, DescLevel = 1):
            RecoverPercentage = Battle_FormatDescVal(round(self.RecoverValue[DescLevel] * 100), Percentage = True)
            return tra(_("Removes all harmful effects on yourself and recovers your energy and health by %s +5%% per harmful effect removed.")) % RecoverPercentage