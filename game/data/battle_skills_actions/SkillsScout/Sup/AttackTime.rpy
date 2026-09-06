init python:
    @RegisterBattleSkill("ScoutAttackTime")
    class BattleSkill_ScoutAttackTime(BattleSkill):
        DisplayName = _("Attack Time")
        
        Icon = "images/battle_skill_icons/scout/AttackTime.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 80

        CritRateBuff = {
            1:1.2, 
            2:1.35, 
            3:1.5, 
            4:1.65, 
            5:1.8}
        
        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET}

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_CritChance(
                            Duration = 2, 
                            StatMod_CritChance = self.CritRateBuff[self.Level], 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "scout_atttime_critbuff")),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Immunity(
                            Duration = 2, 
                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            CritRateBuffPerc = Battle_FormatDescVal(round((self.CritRateBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Removes all harmful effects from all allies, then grants a %s increase in critical rate and immunity for 2 turns to all of them.")) % CritRateBuffPerc