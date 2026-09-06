init python:
    @RegisterBattleSkill("ZanarakDarkSun")
    class BattleSkill_ZanarakDarkSun(BattleSkill):
        DisplayName = _("Darksun")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        Cost_Energy = 90

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}
        AIBaseWeight = 2.0


        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = 0.7,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.75,
                        StatusEffect = BattleStatusEff_Burn(
                            BaseValue = self.Owner_BattleChar.Damage, 
                            Duration = 3, 
                            SourceName = self.DisplayName))
                ]
            )
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = 1.0,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.75,
                        StatusEffect = BattleStatusEff_Burn(
                            BaseValue = self.Owner_BattleChar.Damage, 
                            Duration = 3, 
                            SourceName = self.DisplayName))
                ]
            )
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = 1.25,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.75,
                        StatusEffect = BattleStatusEff_Burn(
                            BaseValue = self.Owner_BattleChar.Damage, 
                            Duration = 3, 
                            SourceName = self.DisplayName))
                ]
            )
            return

        def GetDesc(self, DescLevel = 1):
            return "Attack a single enemy unit 3 times, each strike progressing in strength, 70% - 100% - 125%, each strike has a 75% chance of causing 1 burning for 3 rounds"