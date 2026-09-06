init python:
    @RegisterBattleSkill("SlimeFirmingGel")
    class BattleSkill_SlimeFirmingGel(BattleSkill):
        DisplayName = _("Firming Gel")
        
        Icon = "images/battle_skill_icons/slime/Immunity.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 100

        DamageResBuff = {1:0.3, 2:0.2, 3:0.1}

        AITags = {AI_TAGS.RAISE_TARGET_PHYS_DAMAGE_RESISTANCE}

        def Execute(self, Target):
            Battle_ScheduledCast(
                 
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(
                            DamageRecieved_Mod = self.DamageResBuff[self.Level], 
                            Duration = 1, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "slime_firmgel_dmgresbuff")),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Immunity(
                            Duration = 3, 
                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            DmgResBuffPerc = Battle_FormatDescVal(round((1.0 - self.DamageResBuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Increases the damage resistance of all allies by %s for 1 turn and grants immunity to all allies for 3 turns.")) % DmgResBuffPerc