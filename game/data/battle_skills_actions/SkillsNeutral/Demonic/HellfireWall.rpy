init python:
    @RegisterBattleSkill("NeutralHellfireWall")
    class BattleSkill_NeutralHellfireWall(BattleSkill):
        DisplayName = _("Hellfire Wall")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ALLIES
        Cost_Energy = 100


        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj =    self,
                CastTarget =        self.ValidTargets,
                Effects_OnTarget =          [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            Duration = 2, 
                            StatMod_Armor = 1.6, 
                            StatusEffectID = "hellfirewall_armor_mod", 
                            SourceName = self.DisplayName
                        )
                    ),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_BurningShield(
                            Duration = 3,
                            SourceName = self.DisplayName
                        )
                    ),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_ReflectDamage(
                            Duration = 4,
                            SourceName = self.DisplayName,
                            DamageRateFromBaseCharDmg = 0.3,
                        )
                    )
                ],
                Effects_OnSelf = [],
            )

            AllEnemies = Battle_GetAllEnemiesOfChar(self.Owner_BattleChar)
            for EnemyChar in AllEnemies:
                Battle_ApplyStatusEffect(
                    TargetChar = EnemyChar, 
                    CastOnEnemy = True,
                    StatusEffect = BattleStatusEff_StatMod_Accuracy(
                        Duration = 4, 
                        StatMod_AttackRating = 0.7, 
                        StatusEffectID = "hellfirewall_enemy_ar_mod", 
                        SourceName = self.DisplayName
                    ),
                )
            return

        def GetDesc(self, DescLevel = 1):
            return "The entire party has its armour increased by 60% for 2 rounds, also, if any of those units are hit, the attacking side receives burning for 3 rounds. The opposing party’s attack rating is decreased by 30% for 4 rounds. The user’s party gains a buff for 4 rounds. The buff deals 30% of the user’s damage when hit and inflicts burning on the attacking target."
