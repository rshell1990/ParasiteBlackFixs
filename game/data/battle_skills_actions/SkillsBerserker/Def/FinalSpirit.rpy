init python:
    @RegisterBattleSkill("BerserkerFinalSpirit")
    class BattleSkill_BerserkerFinalSpirit(BattleSkill):
        DisplayName = _("Final Spirit")

        Icon = "images/battle_skill_icons/berserker/FinalSpirit.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 45

        DamageDealtBuff = {1:1.3, 2:1.4, 3:1.5, 4:1.7}

        def Execute(self, Target):
            Battle_ScheduledCast(
                 
                SourceSkillObj = self,
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(
                            DamageRecieved_Mod = 1.3,
                            Duration = 2,
                            SourceName = self.DisplayName, 
                            StatusEffectID = "bers_finalspirit_dmgin_debuff")),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageOut(
                            DamageDealt_Mod = self.DamageDealtBuff[self.Level], 
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "bers_finalspirit_dmgout_buff")),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Counter(
                            Duration = 2, 
                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            DamageDealtBuffPerc = Battle_FormatDescVal(round((self.DamageDealtBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("In exchange for decreasing your damage absorbed by 30%% for 2 turns, it increases your damage dealt by %s and counterattacks for 2 turns.")) % DamageDealtBuffPerc