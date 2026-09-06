init python:
    @RegisterBattleSkill("NeutralCruelGame")
    class BattleSkill_NeutralCruelGame(BattleSkill):
        DisplayName = _("Cruel Game")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 75

        AITags = {AI_TAGS.TAUNT_TARGET, AI_TAGS.INCREASE_SELF_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.5,
                        StatusEffect = BattleStatusEff_Taunt(
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            TauntedBy = self.Owner_BattleChar))
                ],
                Effects_OnSelf = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            Duration = 2, 
                            StatMod_Armor = 1.8, 
                            StatusEffectID = "cruel_game_armor_mod", 
                            SourceName = self.DisplayName,
                        )
                    ),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Counter(
                            Duration = 2, 
                            SourceName = self.DisplayName,
                        )
                    ),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_BurningStrikes(
                            Duration = 3,
                            SourceName = self.DisplayName
                        )
                    )
                ]
            )
            return

        def GetDesc(self, DescLevel = 1):
            return "The user’s armour increases by 80% for 2 rounds The user gains counterattack for 2 rounds, all strikes have a 100% chance of causing burning for 3 rounds. 50% chance to taunt each member of the opposing party for 2 rounds."

