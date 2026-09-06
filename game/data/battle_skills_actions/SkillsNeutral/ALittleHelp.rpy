init python:
    @RegisterBattleSkill("NeutralALittleHelp")
    class BattleSkill_NeutralALittleHelp(BattleSkill):
        DisplayName = _("A Little Help")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ALLIES
        Cost_Energy = 30

        AITags = {AI_TAGS.HEAL_TARGET, AI_TAGS.REMOVE_DEBUFFS_ON_TARGET}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_RestoreHealth(RestoreValue = 0.2, RatioFromMax = True)]
            )
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Removes all harmful effects from all allies and heals their hp by 20%."))