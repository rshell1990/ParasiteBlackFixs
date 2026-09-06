init python:
    @RegisterBattleSkill("NeutralTheGatesOfSevenHells")
    class BattleSkill_NeutralTheGatesOfSevenHells(BattleSkill):
        DisplayName = _("The Gates of Seven Hells")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 70

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj =    self,
                CastTarget =        self.ValidTargets,

                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.25, 
                        StatusEffect = BattleStatusEff_Stun(
                            Duration = 1, 
                            SourceName = self.DisplayName
                        )
                    ),
                    BattleEffect_DealDamageFlat(
                        DamageValue = self.Owner_BattleChar.Damage
                    ),
                    BattleEffect_ApplyStatusOnEnemy(
                        IfWillpowerLowerThanValue = self.Owner_BattleChar.Willpower,
                        StatusEffect = BattleStatusEff_Burn(
                            self.Owner_BattleChar.Damage,
                            Duration = 3, 
                            SourceName = self.DisplayName
                        )
                    ),
                    BattleEffect_ApplyStatusOnEnemy(
                        IfWillpowerLowerThanValue = self.Owner_BattleChar.Willpower,
                        StatusEffect = BattleStatusEff_Bleed(
                            self.Owner_BattleChar.Damage,
                            Duration = 3, 
                            SourceName = self.DisplayName
                        )
                    ),
                    BattleEffect_ApplyStatusOnEnemy(
                        IfWillpowerLowerThanValue = self.Owner_BattleChar.Willpower,
                        StatusEffect = BattleStatusEff_Poison(
                            self.Owner_BattleChar.Damage,
                            Duration = 3, 
                            SourceName = self.DisplayName
                        )
                    ),
                ],
            )
            return

        def GetDesc(self, DescLevel = 1):
            return "Increases the dodge and accuracy of all allies by 60% for 2 turns."
