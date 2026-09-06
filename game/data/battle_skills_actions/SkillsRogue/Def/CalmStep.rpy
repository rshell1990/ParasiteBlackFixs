init python:
    @RegisterBattleSkill("RogueCalmStep")
    class BattleSkill_RogueCalmStep(BattleSkill):
        DisplayName = _("Calm Step")
        
        Icon = "images/battle_skill_icons/rogue/CalmStep.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 40

        DodgeBoost =   {1:1.4, 2:1.55, 3:1.7, 4:1.7}
        HealPerc =     {1:0.3, 2:0.3,  3:0.3, 4:0.4}

        AITags = {AI_TAGS.HEAL_SELF, AI_TAGS.REMOVE_BUFFS_ON_TARGET}

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [BattleEffect_RemoveDebuffsOnTarget(),
                                    BattleEffect_RestoreHealth(
                                        RestoreValue = self.HealPerc[self.Level],
                                        RatioFromMax = True),
                                    BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_Immunity(
                                            Duration = 2,
                                            SourceName = self.DisplayName)),
                                    BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_StatMod_Dodge(
                                            Duration = 2,
                                            StatMod_DodgeRating = self.DodgeBoost[self.Level], 
                                            StatusEffectID = "calmstep_dodgeboost", 
                                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            HealPerc = Battle_FormatDescVal(round(self.HealPerc[DescLevel] * 100), Percentage = True)
            DodgePerc = Battle_FormatDescVal(round((self.DodgeBoost[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Break free from harmful effects, heals %s of maximum hp, becomes immune to any harmful effects and increases dodge chance by %s for 2 turns each.")) % (HealPerc, DodgePerc)