init python:
    @RegisterBattleSkill("BerserkerBerserkerTime")
    class BattleSkill_BerserkerBerserkerTime(BattleSkill):
        DisplayName = _("Berserker Time")

        Icon = "images/battle_skill_icons/berserker/BerserkerTime.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 50

        AllyDamageBonus = {1:1.4, 2:1.5, 3:1.6, 4:1.7}

        def Execute(self, Target):
            Battle_ScheduledCast(
                 
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageOut(
                            DamageDealt_Mod = self.AllyDamageBonus[self.Level], 
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "bers_berstime_dmgbuff")),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(
                            DamageRecieved_Mod = 1.2,
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "bers_berstime_dmgtakendebuff")),
                        ])
            return

        def GetDesc(self, DescLevel = 1):
            AllyDamageBonusPerc = Battle_FormatDescVal(round((self.AllyDamageBonus[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Increases the damage all allies deal by %s in exchange for increasing the damage they take by 20%% for 2 turns each.")) % AllyDamageBonusPerc