init python:
    @RegisterBattleSkill("ScoutTheNorthStarStrike")
    class BattleSkill_ScoutTheNorthStarStrike(BattleSkill):
        DisplayName = _("The North Star Strike")

        Icon = "images/battle_skill_icons/scout/TheNorthStarStrike.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 90

        DamageValue = {1:0.5, 2:0.53, 3:0.56, 4:0.59}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.EFFECT_SCALES_WITH_AMOUNT_OF_BUFFS_ON_TARGET}

        def Execute(self, Target):
            for i in range(4):
                Battle_ScheduledAttack(
                    SourceSkillObj = self, 
                    AttackTarget = Target,
                    DamageMod = self.DamageValue[self.Level],
                    Effects_OnCrit_Target = [
                        BattleEffect_ReplaceRandomEnemyBuffWithStatusEff(
                            StatusEffect = BattleStatusEff_Bleed(
                                BaseValue = self.Owner_BattleChar.Damage, 
                                Duration = 1,
                                SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Attacks the enemy 4 times, dealing %s damage on each strike. Whenever you land a critical hit, you swap an enemy's buff for a bleed effect for 1 turn.")) % StrikeDamage