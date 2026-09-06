init python:
    @RegisterBattleSkill("RogueAcrobaticManeuvers")
    class BattleSkill_RogueAcrobaticManeuvers(BattleSkill):
        DisplayName = _("Acrobatic Maneuvers")

        Icon = "images/battle_skill_icons/rogue/AcrobaticManeuvers.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 50

        AlliesAccDodgeBonus = {1:1.4, 2:1.5, 3:1.6}

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = BATTLE_TARGETS.ALL_ALLIES,
                Effects_OnTarget = [BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                                            StatMod_AttackRating = self.AlliesAccDodgeBonus[self.Level],
                                            Duration = 2,
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "rogueacro_acc_buff")),
                                    BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_StatMod_Dodge(
                                            StatMod_DodgeRating = self.AlliesAccDodgeBonus[self.Level],
                                            Duration = 2,
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "rogueacro_dodge_buff"))],
                Effects_OnSelf = [BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_Invincibility(
                                            Duration = 1, 
                                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            AccDodgePerc = Battle_FormatDescVal(round((self.AlliesAccDodgeBonus[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Perform daring acrobatics to confound enemies becoming invincible for 1 turn and granting a %s accuracy and dodge chance increase to your allies for 2 turns.")) % AccDodgePerc