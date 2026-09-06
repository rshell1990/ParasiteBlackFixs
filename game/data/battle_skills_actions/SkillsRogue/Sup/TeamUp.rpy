init python:
    @RegisterBattleSkill("RogueTeamUp")
    class BattleSkill_RogueTeamUp(BattleSkill):
        DisplayName = _("Team Up")

        Icon = "images/battle_skill_icons/rogue/TeamUp.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ALLY

        Cost_Energy = 40

        AccuracyBuff = {1:1.5, 2:1.5, 3:1.6, 4:1.6}
        HealPerc =     {1:0.2, 2:0.3, 3:0.3, 4:0.4}

        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET, AI_TAGS.HEAL_TARGET}

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = Target,
                Effects_OnTarget = [BattleEffect_RemoveDebuffsOnTarget(),
                                    BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                                            StatMod_AttackRating = self.AccuracyBuff[self.Level],
                                            Duration = 2,
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "rogueteamup_acc_buff")),
                                    BattleEffect_RestoreHealth(RestoreValue = self.HealPerc[self.Level], RatioFromMax = True)],
                Effects_OnSelf = [BattleEffect_RemoveDebuffsOnTarget(),
                                    BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                                            StatMod_AttackRating = self.AccuracyBuff[self.Level],
                                            Duration = 2,
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "rogueteamup_acc_buff")),
                                    BattleEffect_RestoreHealth(RestoreValue = self.HealPerc[self.Level], RatioFromMax = True)])
            return

        def GetDesc(self, DescLevel = 1):
            AccBuffPerc = Battle_FormatDescVal(round((self.AccuracyBuff[DescLevel] - 1.0) * 100), Percentage = True)
            HealPerc = Battle_FormatDescVal(round(self.HealPerc[DescLevel] * 100), Percentage = True)
            return tra(_("Removes all harmful effects from you and the target ally and recovers hp by %s and grants increased accuracy by %s for 2 turns for both.")) % (HealPerc, AccBuffPerc)