init python:
    @RegisterBattleSkill("AssassinBleedingHearts")
    class BattleSkill_AssassinBleedingHearts(BattleSkill):
        DisplayName = _("Bleeding Hearts")

        Icon = "images/battle_skill_icons/assassin/BleedingHearts.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 90

        HealthDrainedRatio = {
            1:0.15,
            2:0.175,
            3:0.175,
            4:0.2,
        }
        CurseTurns = {
            1:2,
            2:2,
            3:3,
            4:3,
        }

        AITags = {AI_TAGS.FAVOURED_LOWER_TARGET_HP_RATIO, AI_TAGS.HEAL_SELF}

        def Execute(self, Target):
            #  "drain" hp
            DrainMult = (self.HealthDrainedRatio[self.Level] if self.Owner_BattleChar.Health >= Target.Health else self.HealthDrainedRatio[self.Level] * 2)
            HPToDrain = round(Target.Health * DrainMult)
            Battle_DealDamage(Target, HPToDrain, IgnoreArmor = True)

            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = Target,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(StatusEffect = BattleStatusEff_Curse(Duration = 2, SourceName = self.DisplayName)),
                ],
            )

            CharsToHeal = Battle_GetAliveCharsOnSide(self.Owner_BattleChar.BattleSide)

            for BChar in CharsToHeal:
                Battle_RestoreHealth(BChar, HPToDrain / len(CharsToHeal))
            return

        def GetDesc(self, DescLevel = 1):
            DrainPerc = Battle_FormatDescVal(round(self.HealthDrainedRatio[DescLevel] * 100), Percentage = True)
            DrainPercDoubled = Battle_FormatDescVal(round((self.HealthDrainedRatio[DescLevel] * 2) * 100), Percentage = True)

            return tra(_("Drain the enemy target for %s of their current HP and distribute the total HP drained amongst your party members equally.\nIt also grants a harmful curse effect on the enemy for 2 turns.\nIf the enemy current HP is lower than your current HP, double the drain (from %s to %s).")) % (DrainPerc, DrainPerc, DrainPercDoubled)