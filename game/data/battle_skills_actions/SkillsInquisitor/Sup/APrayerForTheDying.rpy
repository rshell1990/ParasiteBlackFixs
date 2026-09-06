init python:
    @RegisterBattleSkill("InquisitorAPrayerForTheDying")
    class BattleSkill_InquisitorAPrayerForTheDying(BattleSkill):    
        DisplayName = _("A prayer for the dying")

        Icon = "images/battle_skill_icons/inquisitor/APrayerForTheDying.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ANY_ALLY

        Cost_Energy = 40

        RestoreHealthAmt = {1:0.1, 2:0.15, 3:0.15}
        RestoreHealthTurns = {1:2, 2:2, 3:3}

        AITags = {AI_TAGS.FAVOURED_LOWER_TARGET_HP_RATIO}

        def Execute(self, Target):
            Battle_RemoveAllDebuffs(Target)
            Battle_RestoreHealth(Target, 0.3, RatioFromMax = True)
            
            if (Target.Health / Target.HealthMax) < 0.6:
                Battle_ApplyStatusEffect(
                    TargetChar = Target,
                    StatusEffect = BattleStatusEff_RegenHealth(
                        Duration = self.RestoreHealthTurns[self.Level], 
                        RestoreVal = self.RestoreHealthAmt[self.Level], 
                        RatioFromMax = True, 
                        SourceName = self.DisplayName, 
                        StatusEffectID = "inquisitor_prayerfordying_healthrege"))
            return

        def GetDesc(self, DescLevel = 1):
            RegenPerc = Battle_FormatDescVal(round(self.RestoreHealthAmt[DescLevel] * 100), Percentage = True)
            RegenTurns = Battle_FormatDescVal(self.RestoreHealthTurns[DescLevel])
            return tra(_("Remove all debuffs from a target ally and heal them by 30%%.\nIf the ally's health remains below 60%% after healing, apply a healing effect of %s health per turn for %s turns.")) % (RegenPerc, RegenTurns)