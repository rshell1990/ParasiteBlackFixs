init python:
    @RegisterBattleSkill("NeutralInfernalBlast")
    class BattleSkill_NeutralInfernalBlast(BattleSkill):
        DisplayName = _("Infernal Blast")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        Cost_Energy = 60

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE,}

        def Execute(self, Target):
            for i in range(3):
                Battle_ScheduledAttack(
                    SourceSkillObj = self,
                    AttackTarget = Target,
                    DamageMod = 0.5,
                    Effects_OnHit_Target = [
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = 0.3,
                            StatusEffect = BattleStatusEff_Burn(
                                BaseValue = self.Owner_BattleChar.Damage,
                                Duration = 4,
                                SourceName = self.DisplayName
                            )
                        ),
                        BattleEffect_DealDamageFlat_ToAlliesOfTarget(
                            DamageValue = self.Owner_BattleChar.Damage * 0.25
                        )
                    ],
                )
            return

        def GetDesc(self, DescLevel = 1):
            return "The target is hit three times for 50% of damage. Each hit has a 30% chance to inflict burning for 4 rounds. If attack is landed, also deals 25% damage to other members of the target’s party."