init python:
    @RegisterBattleSkill("BansheeASongOfMadness")
    class BattleSkill_BansheeASongOfMadness(BattleSkill):    
        DisplayName = _("A song of madness")

        Icon = "images/battle_skill_icons/banshee/ASongOfMadness.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 40

        SharedDebuffRate = {1:0.7, 2:0.6, 3:0.5}

        ShowHitChance = False


        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(
                            Duration = 2, 
                            StatMod_DodgeRating = self.SharedDebuffRate[self.Level],
                            StatusEffectID = "banshee_asongofmadness_debuff_dodge",
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                            Duration = 2, 
                            StatMod_AttackRating = self.SharedDebuffRate[self.Level],
                            StatusEffectID = "banshee_asongofmadness_debuff_accuracy",
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            Duration = 2, 
                            StatMod_Armor = self.SharedDebuffRate[self.Level],
                            StatusEffectID = "banshee_asongofmadness_debuff_armor",
                            SourceName = self.DisplayName))])

            return

        def GetDesc(self, DescLevel = 1):
            DebuffPercentage = Battle_FormatDescVal(round((1.0 - self.SharedDebuffRate[DescLevel]) * 100), Percentage = True)
            return tra(_("Poison the enemies minds with your enchanting song. The enemy team is debuffed in dodge, accuracy and armor by %s for 2 turns.")) % DebuffPercentage