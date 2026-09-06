init python:
    @RegisterBattleSkill("ParasiteWhiteRegenerativeCocoon")
    class BattleSkill_ParasiteWhiteRegenerativeCocoon(BattleSkill):
        DisplayName = _("Regenerative Cocoon")

        Icon = "images/battle_skill_icons/parawhite/RegenerativeCocoon.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 40

        DamageReductionValue = {1:0.7, 2:0.6, 3:0.6,  4:0.5}
        HealPerTurn =          {1:0.1, 2:0.1, 3:0.15, 4:0.15}

        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET, AI_TAGS.HEAL_SELF, AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE}

        def Execute(self, Target):
            Battle_ScheduledCast(
                 
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_RegenHealth(
                            Duration = 3,
                            RestoreVal = self.HealPerTurn[self.Level], 
                            RatioFromMax = True, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "parawhite_regencocon_hpregen")),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(
                            DamageRecieved_Mod = self.DamageReductionValue[self.Level], 
                            Duration = 2, 
                            SourceName = self.DisplayName,
                            StatusEffectID = "parawhite_regencocon_dmginbuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            HealAmountPerc = Battle_FormatDescVal(round(self.HealPerTurn[DescLevel] * 100), Percentage = True)
            DmgInBuffPerc = Battle_FormatDescVal(round((1.0 - self.DamageReductionValue[DescLevel]) * 100), Percentage = True)
            return tra(_("Removes all harmful effects from yourself, reduces damage received by %s for 2 turns and heals your hp by %s for the next 3 turns.")) % (DmgInBuffPerc, HealAmountPerc)