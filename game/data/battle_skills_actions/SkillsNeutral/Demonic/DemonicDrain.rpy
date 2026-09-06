init python:
    @RegisterBattleSkill("NeutralDemonicDrain")
    class BattleSkill_NeutralDemonicDrain(BattleSkill):
        DisplayName = _("Demonic Drain")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        Cost_Energy = 40

        AITags = {AI_TAGS.HEAL_SELF}

        def Execute(self, Target):
            # Drain 50 % of current mana/energy from the target
            # Drain 10 % of total hp of target
            # Drain 5 % of current hp from other active members of the target’s party.
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = Target,

                Effects_OnTarget = [
                    BattleEffect_DrainHealth(
                        DrainingChar = self.Owner_BattleChar,
                        AmtToDrain = Target.Health * 0.1,
                    ),
                    BattleEffect_DrainEnergyOrMana(
                        DrainingChar = self.Owner_BattleChar,
                        DrainPercentage = 0.5,
                        DrainFromCurrent = True,
                    )
                ],
            )
            AllEnemyAllies = Battle_GetAllAlliesOfChar(Target)
            for Enemy in AllEnemyAllies:
                BattleEffect_DrainHealth(self.Owner_BattleChar, Enemy.HealthMax * 0.05).ApplyEffect(Enemy)
            return

        def GetDesc(self, DescLevel = 1):
            return "Drain 50% of current mana/energy from the target. Drain 10% of total hp of target. Drain 5% of total hp from other active members of the target’s party."
