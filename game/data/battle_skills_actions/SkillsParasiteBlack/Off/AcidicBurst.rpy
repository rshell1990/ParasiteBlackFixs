init python:
    @RegisterBattleSkill("ParasiteBlackAcidicBurst")
    class BattleSkill_ParasiteBlackAcidicBurst(BattleSkill):
        DisplayName = _("Acidic Burst")
        
        Icon = "images/battle_skill_icons/parablack/AcidicBurst.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 100

        BonusChanceAllRound = {1:0, 2:0.15, 3:0.15, 4:0.30}
        DamageValue =         {1:1.6, 2:1.6, 3:1.9, 4:1.9}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [BattleEffect_ApplyStatusOnEnemy(
                                    Chance = 0.6 + self.BonusChanceAllRound[self.Level], 
                                    StatusEffect = BattleStatusEff_StatMod_Dodge(
                                        Duration = 2,
                                        StatMod_DodgeRating = 0.4,
                                        StatusEffectID = "acidic_burst_dodge_debuff",
                                        SourceName = self.DisplayName)),
                                BattleEffect_ApplyStatusOnEnemy(
                                    Chance = 0.3 + self.BonusChanceAllRound[self.Level], 
                                    StatusEffect = BattleStatusEff_Stun(
                                        Duration = 1,
                                        SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            StunChance = Battle_FormatDescVal(round((0.3 + self.BonusChanceAllRound[DescLevel]) * 100), Percentage = True)
            DodgeDebuffChance = Battle_FormatDescVal(round((0.6 + self.BonusChanceAllRound[DescLevel]) * 100), Percentage = True)
            return tra(_("Release a terrifying burst of acid to hit all enemies (%s damage).\nThe burst stuns them for 1 turn with %s chance and reduces their dodge rating by 60%% with a %s chance for 2 turns.")) % (DamageValue, StunChance, DodgeDebuffChance)