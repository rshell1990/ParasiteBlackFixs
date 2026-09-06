init python:
    @RegisterBattleSkill("AssassinTreacherousSlice")
    class BattleSkill_AssassinTreacherousSlice(BattleSkill):
        DisplayName = _("Treacherous Slice")

        Icon = "images/battle_skill_icons/assassin/TreacherousSlice.webp"

        Level_Max = 3

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 50

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        DamageValue = {
            1:2.0,
            2:2.15,
            3:2.15,
        }

        PoisonBleedTurns = {
            1:2,
            2:2,
            3:3,
        }

        def Execute(self, Target):
            AlliesList = Battle_GetAllAlliesOfChar(self.Owner_BattleChar)

            # case 1 no allies
            if len(AlliesList) == 0:
                DamageMult = (self.DamageValue[self.Level] * 0.5)
                ActualTarget = Battle_GetAllEnemiesOfChar(self.Owner_BattleChar)
                
            # case 2 with allies
            else:
                ActualTarget = Target
                DamageMult = self.DamageValue[self.Level]
                #AlliesList.append(self.Owner_BattleChar)
                for Ally in AlliesList:
                    Ally.Health = max(round(Ally.Health * 0.75), 1)

            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = ActualTarget,
                DamageMod = DamageMult,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.8, 
                        StatusEffect = BattleStatusEff_Bleed(
                            BaseValue = self.Owner_BattleChar.Damage,
                            Duration = self.PoisonBleedTurns[self.Level],  
                            SourceName = self.DisplayName
                        )
                    ),
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.8, 
                        StatusEffect = BattleStatusEff_Poison(
                            BaseValue = self.Owner_BattleChar.Damage,
                            Duration = self.PoisonBleedTurns[self.Level],  
                            SourceName = self.DisplayName
                        )
                    )
                ],
            )
            return

        def GetDesc(self, DescLevel = 1):
            DamagePerc = Battle_FormatDescVal(round(self.DamageValue[DescLevel] * 100), Percentage = True)
            if self.Owner_BattleChar:
                DamageVal = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageVal = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Take 25%% of current HP of whole party. Slice at a single target enemy with a horrific strike (%s of attack dmg, %s). Has a 80%% chance to inflict both poisoning and bleeding for 2 turns each on the target. -*IF* no allies are present and player uses the ability regardless, player does a strike that only does 50%% of their normal attack dmg…")) % (DamagePerc, DamageVal)
