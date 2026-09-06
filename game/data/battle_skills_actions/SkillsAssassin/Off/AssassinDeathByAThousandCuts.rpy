init python:
    @RegisterBattleSkill("AssassinDeathByAThousandCuts")
    class BattleSkill_AssassinDeathByAThousandCuts(BattleSkill):
        DisplayName = _("Death By A Thousand Cuts")

        Icon = "images/battle_skill_icons/assassin/DeathByAThousandCuts.webp"

        Level_Max = 4

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES # <- actually rolls random

        Cost_Energy = 40

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        DamageValue = {
            1:0.3,
            2:0.4,
            3:0.5,
            4:0.5,
        }

        BleedChance = {
            1:0.2,
            2:0.2,
            3:0.2,
            4:0.35,
        }

        def Execute(self, Target):
            ActualTarget = renpy.random.choice(Battle_GetAllEnemiesOfChar(self.Owner_BattleChar))

            for i in range(5):
                Battle_ScheduledAttack(
                    SourceSkillObj = self,
                    AttackTarget = ActualTarget,
                    DamageMod = self.DamageValue[self.Level],
                    Effects_OnHit_Target = [
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = self.BleedChance[self.Level], 
                            StatusEffect = BattleStatusEff_Bleed(
                                BaseValue = self.Owner_BattleChar.Damage,
                                Duration = 2, 
                                SourceName = self.DisplayName
                            )
                        )
                    ],
                )
            return

        def GetDesc(self, DescLevel = 1):
            DamagePerc = Battle_FormatDescVal(round(self.DamageValue[DescLevel] * 100), Percentage = True)
            if self.Owner_BattleChar:
                DamageValDesc = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]), Parentheses = True)
            else:
                DamageValDesc = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]), Parentheses = True)
            BleedChance = Battle_FormatDescVal(round(self.BleedChance[DescLevel] * 100), Percentage = True)
            
            return tra(_("Target a random enemy, hits them 5 times with attacks %s of the usual dmg %s. Each hit has a %s chance of inflicting bleeding for 2 turns.")) % (DamagePerc, DamageValDesc, BleedChance)
