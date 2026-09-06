init python:
    @RegisterBattleSkill("ScoutPrepare")
    class BattleSkill_ScoutPrepare(BattleSkill):
        DisplayName = _("Prepare")

        Icon = "images/battle_skill_icons/scout/Prepare.webp"

        Level_Max = 2
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 40

        AccuracyBonus = {1:1.4, 2:1.6}

        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET, AI_TAGS.FAVOURED_HIGH_OWN_HP_RATIO}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Invincibility(Duration = 1, SourceName = self.DisplayName))])
            if self.Owner_BattleChar.Health > self.Owner_BattleChar.HealthMax * 0.5:
                Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar, StatusEffect = BattleStatusEff_StatMod_Accuracy(Duration = 2, StatMod_AttackRating = self.AccuracyBonus[self.Level], StatusEffectID = "scout_prep_accbuff", SourceName = self.DisplayName))
            return

        def GetDesc(self, DescLevel = 1):
            AccBuffPerc = Battle_FormatDescVal(round((self.AccuracyBonus[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Removes all negative effects and grants yourself invincibility for 1 turn. If your hp is above half, grant %s increased accuracy for 2 additional turns.")) % AccBuffPerc