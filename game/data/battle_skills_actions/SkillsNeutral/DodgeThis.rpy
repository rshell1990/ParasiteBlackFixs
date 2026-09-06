init python:
    @RegisterBattleSkill("NeutralDodgeThis")
    class BattleSkill_NeutralDodgeThis(BattleSkill):
        DisplayName = _("Dodge This")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 60

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}
        #AIBaseWeight = 2.0

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = self.ValidTargets,
                DamageMod = 1.0,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.3,
                        StatusEffect = BattleStatusEff_Poison(
                            BaseValue = self.Owner_BattleChar.Damage, 
                            Duration = 2, 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.5,
                        StatusEffect = BattleStatusEff_HealthRecoveryMod(
                            ResRecoverMod_Health = 0.6,
                            Duration = 2, 
                            SourceName = self.DisplayName,
                            StatusEffectID = "neutral_dodgethis_hpregen_debuff")),
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.5,
                        StatusEffect = BattleStatusEff_EnergyRecoveryMod(
                            ResRecoverMod_Energy = 0.6,
                            Duration = 2, 
                            SourceName = self.DisplayName,
                            StatusEffectID = "neutral_dodgethis_energyregen_debuff"))
                    
                ]
            )
            return

        def GetDesc(self, DescLevel = 1):
            return "Attack the player entire party for 100% dmg. Has a 30% chance of inflicting poison on each party member hit. Also has a 50% chance (per party member hit) of reducing any energy and HP recovery by 40% (cost: 60)"