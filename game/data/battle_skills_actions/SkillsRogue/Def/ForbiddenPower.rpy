init python:
    @RegisterBattleSkill("RogueForbiddenPower")
    class BattleSkill_RogueForbiddenPower(BattleSkill):
        DisplayName = _("Forbidden Power")
        Icon = "images/battle_skill_icons/rogue/ForbiddenPower.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 60

        DamageBoostValue = {1:1.4, 2:1.5, 3:1.6, 4:1.7}
        AutoSelectNextInPartyOnExecute = False

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Immunity(
                            Duration = 3, 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageOut(
                            DamageDealt_Mod = self.DamageBoostValue[self.Level], 
                            Duration = 3, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "roguefobpower_dmgboost"))])
            Battle_GrantExtraTurn(self.Owner_BattleChar)
            return

        def GetDesc(self, DescLevel = 1):
            DamageBoostPerc = Battle_FormatDescVal(round((self.DamageBoostValue[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Unleash your forbidden power, increasing damage dealt by %s and gaining immunity to harmful effects for 3 turns.\nYou gain another turn immediately after using this skill.")) % DamageBoostPerc