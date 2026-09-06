init python:
    @RegisterBattleSkill("NeutralHealThem")
    class BattleSkill_NeutralHealThem(BattleSkill):
        DisplayName = _("Heal Them")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ALLIES
        Cost_Energy = 20

        AITags = {AI_TAGS.HEAL_TARGET}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_RestoreHealth(RestoreValue = 0.2, RatioFromMax = True)])
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Heals all allies for 20% of their max hp."))