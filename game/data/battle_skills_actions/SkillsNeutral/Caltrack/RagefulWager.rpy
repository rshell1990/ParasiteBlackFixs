init python:
    @RegisterBattleSkill("NeutralRagefulWager")
    class BattleSkill_NeutralRagefulWager(BattleSkill):
        DisplayName = _("Rageful Wager")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        Cost_Energy = 40

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_LOWER_TARGET_HP_RATIO}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = (1.6 if (Target.Health < Target.HealthMax * 0.6) else 0.6),
            )
            return

        def GetDesc(self, DescLevel = 1):
            return "Attack the enemy twice. If the enemy's HP is above 60%, it deals 60% of your damage per hit; otherwise, it deals 160% of your damage per hit. (Cost 40)"
