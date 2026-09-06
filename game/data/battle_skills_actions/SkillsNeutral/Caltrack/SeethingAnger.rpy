init python:
    @RegisterBattleSkill("NeutralSeethingAnger")
    class BattleSkill_NeutralSeethingAnger(BattleSkill):
        DisplayName = _("Seething Anger")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.SELF
        Cost_Energy = 55

        AITags = {AI_TAGS.HEAL_SELF}

        def Execute(self, Target):
            AmountOfEnemiesForAtkBuff = 0
            EnemyList = Battle_GetAllEnemiesOfChar(self.Owner_BattleChar)
            for EnemyChar in EnemyList:
                if (EnemyChar.Health / EnemyChar.HealthMax) < 0.6:
                    AmountOfEnemiesForAtkBuff += 1
                
            EffectList = [
                BattleEffect_ApplyStatusOnAlly(
                    Chance = 1.0,
                    StatusEffect = BattleStatusEff_StatMod_Armor(
                        Duration = 2, 
                        StatusEffectID = "seething_anger_armor_buff", 
                        SourceName = self.DisplayName
                    )
                ),
                BattleEffect_ApplyStatusOnAlly(
                    Chance = 1.0,
                    StatusEffect = BattleStatusEff_RegenHealth(
                        Duration = 2, 
                        RestoreVal = 0.2,
                        RatioFromMax = True,
                        StatusEffectID = "seething_anger_health_regen",
                        SourceName = self.DisplayName)
                )
            ]

            if AmountOfEnemiesForAtkBuff > 0:
                EffectList.append(
                    BattleEffect_ApplyStatusOnAlly(
                    Chance = 1.0,
                    StatusEffect = BattleStatusEff_DamageOut(
                        DamageDealt_Mod = 1.0 + 0.1 * AmountOfEnemiesForAtkBuff,
                        Duration = 3, 
                        StatusEffectID = "seething_anger_dmg_buff",
                        SourceName = self.DisplayName)
                ))


            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = Target,
                Effects_OnTarget = EffectList
            )
            return

        def GetDesc(self, DescLevel = 1):
            return "Increases your armor by 80% and receives a 20% healing effect for 2 turns. Additionally, increases your damage (Attack buff) for 3 turns by 10% for each enemy with 60% or less HP."

