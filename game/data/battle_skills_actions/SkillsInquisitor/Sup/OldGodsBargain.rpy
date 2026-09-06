init python:
    @RegisterBattleSkill("InquisitorOldGodsBargain")
    class BattleSkill_InquisitorOldGodsBargain(BattleSkill):    
        DisplayName = _("Old Gods bargain")

        Icon = "images/battle_skill_icons/inquisitor/OldGodsBargain.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 80

        AccAndDamageBuff = {1:1.4, 2:1.4, 3:1.5, 4:1.5}
        ArmorPenalty = {1:0.7, 2:0.75, 3:0.75, 4:0.8}

        AITags = {AI_TAGS.ONLY_IF_ALLIES_EXIST}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                            StatMod_AttackRating = self.AccAndDamageBuff[self.Level],
                            StatusEffectID = "inquisitor_oldgodsbargain_accbuff",
                            Duration = 2, 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageOut(
                            DamageDealt_Mod = self.AccAndDamageBuff[self.Level],
                            StatusEffectID = "inquisitor_oldgodsbargain_dmgbuff",
                            Duration = 2, 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            StatMod_Armor = self.ArmorPenalty[self.Level],
                            StatusEffectID = "inquisitor_oldgodsbargain_armordebuff",
                            Duration = 2, 
                            SourceName = self.DisplayName)),
                            ])
            return

        def GetDesc(self, DescLevel = 1):
            AccDamageBuffPerc = Battle_FormatDescVal(round((self.AccAndDamageBuff[DescLevel] - 1.0) * 100), Percentage = True)
            ArmorPenaltyPerc = Battle_FormatDescVal(round((1.0 - self.ArmorPenalty[DescLevel]) * 100), Percentage = True)
            return tra(_("Increases the accuracy and damage all allies deal by %s in exchange for decreasing their armor by %s for 2 turns.")) % (AccDamageBuffPerc, ArmorPenaltyPerc)