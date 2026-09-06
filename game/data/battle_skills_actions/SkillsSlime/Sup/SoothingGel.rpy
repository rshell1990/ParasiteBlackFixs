init python:
    @RegisterBattleSkill("SlimeSoothingGel")
    class BattleSkill_SlimeSoothingGel(BattleSkill):
        DisplayName = _("Soothing Gel")
        
        Icon = "images/battle_skill_icons/slime/SoothingGel.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 70

        DamageResBuff = {1:0.6, 2:0.5, 3:0.4}

        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET, AI_TAGS.RAISE_TARGET_PHYS_DAMAGE_RESISTANCE}

        def Execute(self, Target):
            Battle_ScheduledCast(
                
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(
                            DamageRecieved_Mod = self.DamageResBuff[self.Level], 
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "slime_soothgel_dmgresbuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            DamageResPerc = Battle_FormatDescVal(round((1.0 - self.DamageResBuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Emit a soothing gel that cleanses negative effects from allies and increases their damage resistance by %s for 2 turns.")) % DamageResPerc