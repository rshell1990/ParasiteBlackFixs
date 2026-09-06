init python:
    @RegisterBattleSkill("InquisitorEyeForAnEye")
    class BattleSkill_InquisitorEyeForAnEye(BattleSkill):    
        DisplayName = _("Eye for an Eye")

        Icon = "images/battle_skill_icons/inquisitor/EyeForAnEye.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_PercHealthCurr = 0.5
        Cost_Energy = 100

        HpSacrificed = {1:0.5, 2:0.5, 3:0.5}

        TurnsOfBurn = {1:1, 2:2, 3:3}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Burn(
                            BaseValue = self.Owner_BattleChar.Damage,
                            Duration =  self.TurnsOfBurn[self.Level], 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Burn(
                            BaseValue = self.Owner_BattleChar.Damage,
                            Duration =  self.TurnsOfBurn[self.Level], 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Burn(
                            BaseValue = self.Owner_BattleChar.Damage,
                            Duration =  self.TurnsOfBurn[self.Level], 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Stun(
                            Duration = 1, 
                            SourceName = self.DisplayName,
                            ))])
            return

        def GetDesc(self, DescLevel = 1):
            HealthSacrificedPerc = Battle_FormatDescVal(round(self.HpSacrificed[DescLevel] * 100), Percentage = True)
            BurnTurns = Battle_FormatDescVal(self.TurnsOfBurn[DescLevel])
            return tra(_("Sacrifice %s of your current health, in return inflict 3 burning effects on all enemies for %s turns and stun them all for 1 turn.")) % (HealthSacrificedPerc, BurnTurns)