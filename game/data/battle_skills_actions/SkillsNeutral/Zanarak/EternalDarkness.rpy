init python:
    @RegisterBattleSkill("ZanarakEternalDarkness")
    class BattleSkill_ZanarakEternalDarkness(BattleSkill):
        DisplayName = _("Eternal Darkness")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 160

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.REMOVE_BUFFS_ON_TARGET}
        AIBaseWeight = 2.0

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = self.ValidTargets,
                DamageMod = 2.0,
                DamageBurn_Energy = 0.25,
                DamageBurn_Mana = 0.25,
                DamageRecoversAttackerEnergy = 0.25,
                Effects_OnHit_Target = [BattleEffect_RemoveBuffsOnTarget()]
            )
            return

        def GetDesc(self, DescLevel = 1):
            return "Unleash a devastating blow on the whole enemy team, over 200% dmg. Removes all beneficial effects drains their energy/mana by 25% of the damage caused."