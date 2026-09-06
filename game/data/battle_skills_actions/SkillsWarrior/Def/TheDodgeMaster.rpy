init python:
    @RegisterBattleSkill("WarriorTheDodgeMaster")
    class BattleSkill_WarriorTheDodgeMaster(BattleSkill):    
        DisplayName = _("The Dodge Master")
        
        Icon = "images/battle_skill_icons/warrior/TheDodgeMaster.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 40
        DodgeBuff = {1:1.6, 2:1.7, 3:1.7, 4:1.8, 5:1.8}
        AccDebuff = {1:0.6, 2:0.6, 3:0.5, 4:0.5, 5:0.4}

        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [BattleEffect_ApplyStatusOnEnemy(
                                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                                            Duration = 2,
                                            StatMod_AttackRating = self.AccDebuff[self.Level],
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "warriordodgemaster_acc_debuff"))],
                Effects_OnSelf = [BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_StatMod_Dodge(
                                            Duration = 2,
                                            StatMod_DodgeRating = self.DodgeBuff[self.Level],
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "warriordodgemaster_dodge_buff"))])
            return
        
        def GetDesc(self, DescLevel = 1):
            DodgePercentage = Battle_FormatDescVal(round((self.DodgeBuff[DescLevel] - 1.0) * 100), Percentage = True)
            AccPercentage = Battle_FormatDescVal(round((1.0 - self.AccDebuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Increases your dodge rating by %s for the next 2 turns and decreases the accuracy of all enemies by %s for 1 turn.")) % (DodgePercentage, AccPercentage)