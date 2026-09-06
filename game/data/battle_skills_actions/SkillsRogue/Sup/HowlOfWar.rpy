init python:
    @RegisterBattleSkill("RogueHowlOfWar")
    class BattleSkill_RogueHowlOfWar(BattleSkill):
        DisplayName = _("Howl of War")
        Icon = "images/battle_skill_icons/rogue/HowlOfWar.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES_NOT_SELF

        Cost_Energy = 80

        AccuracyDamageBuff = {1:1.3, 2:1.4, 3:1.5}

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = BATTLE_TARGETS.ALL_ALLIES,
                Effects_OnTarget = [BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                                            StatMod_AttackRating = self.AccuracyDamageBuff[self.Level],
                                            Duration = 2,
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "roguehowl_acc_buff")),
                                    BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_DamageOut(
                                            DamageDealt_Mod = self.AccuracyDamageBuff[self.Level],
                                            Duration = 2,
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "roguehowl_dmg_buff")),
                                    BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_Immunity(
                                            Duration = 2,
                                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            AccDmgBuffPerc = Battle_FormatDescVal(round((self.AccuracyDamageBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Fire your war cry and strengthen your allies by increasing their accuracy and the damage they deal by %s for 2 turns. Also grants immunity to all allies for 2 turns.")) % AccDmgBuffPerc
