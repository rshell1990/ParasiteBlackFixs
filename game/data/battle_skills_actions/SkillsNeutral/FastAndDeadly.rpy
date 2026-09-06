init python:
    @RegisterBattleSkill("NeutralFastAndDeadly")
    class BattleSkill_NeutralFastAndDeadly(BattleSkill):
        DisplayName = _("Fast and Deadly")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        Cost_Energy = 40

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_HIGHER_AGI_THAN_TARGETS, AI_TAGS.IGNORES_ENEMY_ARMOR}

        def Execute(self, Target):
            AgiModifiedDmgMod = (1.3 if self.Owner_BattleChar.CharRef["Agility"] > Target.CharRef["Agility"] else 1.0)

            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = AgiModifiedDmgMod,
                #Effects_OnHit_Target = [],
                IgnoreArmor = True,
            )
            return

            # Targets a single member of the player party 
            # attacks ignoring armor for 100%% dmg, 
            # if his agility is higher than the opposing side, does 130%% dmg

        def GetDesc(self, DescLevel = 1):
            return "Targets a single member of the player party and attacks ignoring armor for 100% dmg, if his agility is higher than the opposing side, does 130% dmg. (Cost 40) "
        