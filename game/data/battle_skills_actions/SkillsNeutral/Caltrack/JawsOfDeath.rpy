init python:
    @RegisterBattleSkill("NeutralJawsOfDeath")
    class BattleSkill_NeutralJawsOfDeath(BattleSkill):
        DisplayName = _("Jaws of Death")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        Cost_Energy = 50

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_LOWER_TARGET_HP_RATIO}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = 1.5,
                GuaranteedCrit = (True if (Target.Health < Target.HealthMax * 0.25) else False),
            )
            return

        def GetDesc(self, DescLevel = 1):
            return "Attack a single enemy for 150% damage, if their health is below 25% crit chance increases to guaranteed 100% (Cost 50)"