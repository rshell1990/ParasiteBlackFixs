init python:
    @RegisterBattleSkill("SlimeRegenerativeMire")
    class BattleSkill_SlimeRegenerativeMire(BattleSkill):
        DisplayName = _("Regenerative Mire")

        Icon = "images/battle_skill_icons/slime/RegenerativeMire.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 100

        HealPerc =         {1:0.2, 2:0.25, 3:0.25, 4:0.3}
        HealPercPerTurn =  {1:0.1, 2:0.1,  3:0.15, 4:0.15}

        AITags = {AI_TAGS.HEAL_TARGET}
        AIBaseWeight = 1.1

        def Execute(self, Target):
            Battle_ScheduledCast(
                
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_RestoreHealth(
                        RestoreValue = self.HealPerc[self.Level], 
                        RatioFromMax = True),
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Immunity(
                            Duration = 2, 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_RegenHealth(
                            Duration = 2, 
                            RestoreVal = self.HealPercPerTurn[self.Level], 
                            RatioFromMax = True, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "slime_regenmire_hpregen"))])
            return

        def GetDesc(self, DescLevel = 1):
            HealPerc = Battle_FormatDescVal(round(self.HealPerc[DescLevel] * 100), Percentage = True)
            HealPercPerTurn = Battle_FormatDescVal(round(self.HealPercPerTurn[DescLevel] * 100), Percentage = True)
            return tra(_("Removes all harmful effects from all allies and heals their hp by %s. Also grants them immunity and a healing effect of %s of their max health for 2 turns.")) % (HealPerc, HealPercPerTurn)