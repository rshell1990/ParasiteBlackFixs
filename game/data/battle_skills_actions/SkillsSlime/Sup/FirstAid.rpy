init python:
    @RegisterBattleSkill("SlimeFirstAid")
    class BattleSkill_SlimeFirstAid(BattleSkill):
        DisplayName = _("First Aid")
        
        Icon = "images/battle_skill_icons/slime/FirstAid.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ANY_ALLY

        Cost_Energy = 60

        HealLevel = {1:0.2, 2:0.25, 3:0.3}

        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET, AI_TAGS.HEAL_TARGET}

        def Execute(self, Target):
            Battle_ScheduledCast(
                 
                SourceSkillObj = self,
                CastTarget = Target,
                Effects_OnTarget = [
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_RestoreHealth(
                        RestoreValue = self.HealLevel[self.Level], 
                        RatioFromMax = True),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Immunity(
                            Duration = 2, 
                            SourceName = self.DisplayName))],
                Effects_OnSelf = [
                    BattleEffect_RestoreHealth(
                        RestoreValue = self.HealLevel[self.Level], 
                        RatioFromMax = True)])
            return

        def GetDesc(self, DescLevel = 1):
            HealRecoverPerc = Battle_FormatDescVal(round(self.HealLevel[DescLevel] * 100), Percentage = True)
            return tra(_("Removes all harmful effects from the target ally and recovers your hp and the hp of the target ally by %s. Grants immunity to the target ally for 2 turns.\nYou can use this skill on yourself.")) % HealRecoverPerc