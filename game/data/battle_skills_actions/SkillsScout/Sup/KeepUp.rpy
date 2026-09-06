init python:
    @RegisterBattleSkill("ScoutKeepUp")
    class BattleSkill_ScoutKeepUp(BattleSkill):
        DisplayName = _("Keep Up")
        
        Icon = "images/battle_skill_icons/scout/KeepUp.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 70

        CritRateAndArmorBuff = {1:1.4, 2:1.5, 3:1.6}

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            Duration = 2, 
                            StatMod_Armor = self.CritRateAndArmorBuff[self.Level], 
                            StatusEffectID = "scout_keepup_armor_debuff", 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_CritChance(
                            Duration = 2, 
                            StatMod_CritChance = self.CritRateAndArmorBuff[self.Level], 
                            StatusEffectID = "scout_keepup_critbuff", 
                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            CritRateBuffPerc = Battle_FormatDescVal(round((self.CritRateAndArmorBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Increases the armor of all allies and their critical rates by %s for 2 turns.")) % CritRateBuffPerc