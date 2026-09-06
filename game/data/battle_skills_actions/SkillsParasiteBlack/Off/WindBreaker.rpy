init python:
    @RegisterBattleSkill("ParasiteBlackWindBreaker")
    class BattleSkill_ParasiteBlackWindBreaker(BattleSkill):
        DisplayName = _("Wind Breaker")
        
        Icon = "images/battle_skill_icons/parablack/WindBreaker.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 140

        EnemyAccuracyAndDodgeFactor = {1:0.6, 2:0.5, 3:0.5,  4:0.4,  5:0.4}
        DamageValue =                 {1:1.0, 2:1.0, 3:1.15, 4:1.15, 5:1.3}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_HIGHEST_DODGE}

        def Execute(self, Target):
            # strike 1 target, stun 1 turn, reduce dodge chance by 40% for 2 turns
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [BattleEffect_ApplyStatusOnEnemy(
                                        StatusEffect = BattleStatusEff_Stun(
                                                Duration = 1,
                                                SourceName = self.DisplayName)),
                                BattleEffect_ApplyStatusOnEnemy(
                                        StatusEffect = BattleStatusEff_StatMod_Dodge(
                                                Duration = 2, 
                                                StatMod_DodgeRating = self.EnemyAccuracyAndDodgeFactor[self.Level], 
                                                StatusEffectID = "parablack_windbreaker_dodge_debuff", 
                                                SourceName = self.DisplayName))])

            # strike all, reduce accuracy by 40% and burn 50% energy
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = BATTLE_TARGETS.ALL_ENEMIES,
                DamageMod = self.DamageValue[self.Level],
                DamageBurn_Energy = 0.5,
                Effects_OnHit_Target = [BattleEffect_ApplyStatusOnEnemy(
                                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                                            Duration = 2, 
                                            StatMod_AttackRating = self.EnemyAccuracyAndDodgeFactor[self.Level], 
                                            StatusEffectID = "parablack_windbreaker_acc_debuff", SourceName = self.DisplayName))])

            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            AccAndDodgePerc = Battle_FormatDescVal(round((1.0 - self.EnemyAccuracyAndDodgeFactor[DescLevel]) * 100), Percentage = True)
            return tra(_("Attacks one target enemy dealing %s damage, stunning them for 1 turn and reducing their dodge chance by %s for 2 turns.\nThen attacks all enemies once more to reduce their accuracy by %s for 2 turns and their energy by 50%% of the damage dealt.")) % (StrikeDamage, AccAndDodgePerc, AccAndDodgePerc)