init python:
    @RegisterBattleSkill("ParasiteWhiteAllForOne")
    class BattleSkill_ParasiteWhiteAllForOne(BattleSkill):
        DisplayName = _("All For One")
        Icon = "images/battle_skill_icons/parawhite/AllForOne.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        
        Cost_Energy = 100
        StolenHealthPercentage = {1:0.05, 2:0.10, 3:0.15}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.HEAL_SELF, AI_TAGS.EFFECT_SCALES_WITH_AMOUNT_OF_BUFFS_ON_TARGET}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                AbsorbTarget_HealthMax = self.StolenHealthPercentage[self.Level],
                DamageMod = 0.4,
                Effects_OnHit_Target = [BattleEffect_StealBuffs(StealingChar = self.Owner_BattleChar)])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, 0.4))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, 0.4))
            HealthPercStolen = Battle_FormatDescVal(round(self.StolenHealthPercentage[DescLevel] * 100), Percentage = True)

            return tra(_("Attacks all enemies dealing minor damage of %s and steals all their beneficial effects and %s of each target's maximum hp.")) % (StrikeDamage, HealthPercStolen)