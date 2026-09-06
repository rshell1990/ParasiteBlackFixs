init python:
    @RegisterBattleSkill("BerserkerDeathblow")
    class BattleSkill_BerserkerDeathblow(BattleSkill):
        DisplayName = _("Deathblow")
        
        Icon = "images/battle_skill_icons/berserker/Deathblow.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 40
        
        DamageValue = {1:1.8, 2:1.9, 3:2.0, 4:2.1}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level])
            Battle_ApplyStatusEffect(
                TargetChar = self.Owner_BattleChar,
                StatusEffect = BattleStatusEff_StatMod_Accuracy(
                    Duration = 2, 
                    StatMod_AttackRating = 0.7, 
                    StatusEffectID = "bers_deathblow_acc_debuff", 
                    SourceName = self.DisplayName))
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Attacks the enemy with a devastating blow that deals %s damage at the cost of reducing your accuracy by 30%% for the next 2 turns.")) % StrikeDamage