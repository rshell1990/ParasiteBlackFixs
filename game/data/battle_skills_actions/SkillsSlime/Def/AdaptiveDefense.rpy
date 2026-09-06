init python:
    @RegisterBattleSkill("SlimeAdaptiveDefense")
    class BattleSkill_SlimeAdaptiveDefense(BattleSkill):    
        DisplayName = _("Adaptive Defense")

        Icon = "images/battle_skill_icons/slime/AdaptiveDefense.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 40

        HealPerc =     {1:0.2, 2:0.3, 3:0.3, 4:0.4}
        DamageResBuff ={1:0.5, 2:0.5, 3:0.4, 4:0.4}

        AITags = {AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE, AI_TAGS.HEAL_SELF}

        def Execute(self, Target):
            Battle_ScheduledCast(
                 
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(
                            Duration = 2,
                            DamageRecieved_Mod = self.DamageResBuff[self.Level], 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "slime_adefense_dmgres")), 
                    BattleEffect_RestoreHealth(
                        RestoreValue = self.HealPerc[self.Level], 
                        RatioFromMax = True)])
            return

        def GetDesc(self, DescLevel = 1):
            DamageResPerc = Battle_FormatDescVal(round((1.0 - self.DamageResBuff[DescLevel]) * 100), Percentage = True)
            HealPerc = Battle_FormatDescVal(round(self.HealPerc[DescLevel] * 100), Percentage = True)
            return tra(_("Mold your slime form to absorb and reduce incoming damage, gaining %s damage resistance for 2 turns and recovering %s of your max health.")) % (DamageResPerc, HealPerc)