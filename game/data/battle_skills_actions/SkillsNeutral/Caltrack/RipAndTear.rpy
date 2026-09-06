init python:
    @RegisterBattleSkill("NeutralRipAndTear")
    class BattleSkill_NeutralRipAndTear(BattleSkill):
        DisplayName = _("Rip and Tear")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 60

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_LOWER_TARGET_HP_RATIO}

        def Execute(self, Target):
            EnemyList = Battle_GetAllEnemiesOfChar(self.Owner_BattleChar)
            # it only makes sense to randomize if over 2
            if len(EnemyList) > 2:
                renpy.random.shuffle(EnemyList)
                EnemyList = EnemyList[:2]
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = EnemyList,
                DamageMod = 1.2,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.5,
                        StatusEffect = BattleStatusEff_Bleed(
                            BaseValue = self.Owner_BattleChar.Damage * 1.2,
                            Duration = 3,
                            SourceName = self.DisplayName
                        ),
                        IfHealthBelowOrEq = 0.75,
                    ),
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.6,
                        StatusEffect = BattleStatusEff_Stun(
                            Duration = 1,
                            SourceName = self.DisplayName,
                        ),
                        IfHealthBelowOrEq = 0.5,
                    )
                ]
            ) 
            return

        def GetDesc(self, DescLevel = 1):
            return "Attacks two random enemies for 120% damage, if enemies hit HP is below 75%, has a 50% chance of causing bleeding for three rounds. If the enemies HP is below 50%, also has a 60% chance of stunning for 1 round. The effects stack, meaning that enemies with less than 50% HP can suffer both bleeding and stunning. (Cost 60)"
