init python:
    @RegisterBattleSkill("NeutralASmallBlessingMageVariant") # This is a variation for mages, as we don't have much time so I'll just copy and paste it.
    class BattleSkill_NeutralASmallBlessingMageVariant(BattleSkill):
        DisplayName = _("A Small Blessing")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ANY_ALLY
        Cost_Mana = 40

        AITags = {AI_TAGS.HEAL_TARGET, AI_TAGS.REMOVE_DEBUFFS_ON_TARGET, AI_TAGS.EFFECT_SCALES_WITH_AMOUNT_OF_DEBUFFS_ON_TARGET}

        def Execute(self, Target):
            DebuffsCount = 0
            for StatusEffect in Target.StatusEffects:
                if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                    DebuffsCount += 1

            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = Target,
                Effects_OnTarget = [
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_RestoreHealth(RestoreValue = 0.1 + (0.1 * DebuffsCount), RatioFromMax = True)]
            )
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Removes all harmful effects from the target ally and heals their hp by 10% + 10% per harmful effect removed."))