init python:
    @RegisterBattleSkill("AssassinCalculatingSwipe")
    class BattleSkill_AssassinCalculatingSwipe(BattleSkill):
        DisplayName = _("Calculating Swipe")

        Icon = "images/battle_skill_icons/assassin/CalculatingSwipe.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 80

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        DamageValue = {
            1:1.25,
            2:1.35,
            3:1.35,
            4:1.35,
            5:1.35,
        }
        BleedingChance = {
            1:0.5,
            2:0.5,
            3:0.6,
            4:0.6,
            5:0.6,
        }
        BleedingTurns = {
            1:1,
            2:1,
            3:1,
            4:1,
            5:2,
        }
        AlliesAccuracyBuff = {
            1:1.6,
            2:1.6,
            3:1.6,
            4:1.7,
            5:1.7,
        }

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = BATTLE_TARGETS.ALL_ENEMIES,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = self.BleedingChance[self.Level],
                        StatusEffect = BattleStatusEff_Bleed(
                            BaseValue = self.Owner_BattleChar.Damage,
                            Duration = self.BleedingTurns[self.Level], 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.5,
                        StatusEffect = BattleStatusEff_Poison(
                            BaseValue = self.Owner_BattleChar.Damage,
                            Duration = 1, 
                            SourceName = self.DisplayName)),
                    ])

            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = Battle_GetAllAlliesOfChar(self.Owner_BattleChar),
                GenericLogLine = False,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                        Duration = 2, 
                        StatMod_AttackRating = self.AlliesAccuracyBuff[self.Level],
                        SourceName = self.DisplayName, 
                        StatusEffectID = "assassin_calcswipe_allyaccbuff"))],
            )
            return

        def GetDesc(self, DescLevel = 1):
            # % first
            DamagePerc = Battle_FormatDescVal(round((self.DamageValue[DescLevel]) * 100), Percentage = True)
            # not a % but actual dmg tuple 
            if self.Owner_BattleChar:
                DamageValDesc = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValDesc = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            BleedChance = Battle_FormatDescVal(round(self.BleedingChance[DescLevel] * 100), Percentage = True)
            BleedTurns =  Battle_FormatDescVal(self.BleedingTurns[DescLevel])
            AllyAccBuffPerc = Battle_FormatDescVal(round((self.AlliesAccuracyBuff[DescLevel] - 1) * 100), Percentage = True)
            return tra(_("With calculated swipe, strike at all the enemies with your spear (%s attack damage: %s). Has on each enemy hit a %s chance to inflict bleeding with a duration of %s and a 50%% chance to inflict poison for 1 turn. After this attack, all allies receive an accuracy increase of %s for 2 turns.")) % (DamagePerc, DamageValDesc, BleedChance, BleedTurns, AllyAccBuffPerc)
