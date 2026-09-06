init python:
    @RegisterBattleSkill("BansheeWingShield")
    class BattleSkill_BansheeWingShield(BattleSkill):    
        DisplayName = _("Wing Shield")

        Icon = "images/battle_skill_icons/banshee/WingShield.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 30

        DamageReductionPercentage = {1:0.7, 2:0.6, 3:0.5}

        AITags = {AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(
                            DamageRecieved_Mod = self.DamageReductionPercentage[self.Level],
                            Duration = 3,
                            SourceName = self.DisplayName, 
                            StatusEffectID = "banshee_wingshield_dmgtakenbuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            DamageReductionPercentageFmt = Battle_FormatDescVal(round((1.0 - self.DamageReductionPercentage[DescLevel]) * 100), Percentage = True)
            return tra(_("Shield yourself using your wings - reduce incoming damage by %s for the next 3 turns.")) % DamageReductionPercentageFmt