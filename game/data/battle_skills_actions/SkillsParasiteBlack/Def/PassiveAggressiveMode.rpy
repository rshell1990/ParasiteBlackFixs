init python:
    @RegisterBattleSkill("ParasiteBlackPassiveAggressiveMode")
    class BattleSkill_ParasiteBlackPassiveAggressiveMode(BattleSkill):
        DisplayName = _("Passive Aggressive Mode")
        
        Icon = "images/battle_skill_icons/parablack/PassiveAggressiveMode.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 40

        DamageAbsorbtion =   {1:0.6, 2:0.5, 3:0.4, 4:0.4}
        DamageOutReduction = {1:0.8, 2:0.8, 3:0.8, 4:0.9}

        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET, AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE}

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [BattleEffect_RemoveDebuffsOnTarget(),
                                    BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_Counter(
                                            Duration = 2,
                                            SourceName = self.DisplayName)),
                                    BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_DamageIn(
                                            DamageRecieved_Mod =  self.DamageAbsorbtion[self.Level],
                                            Duration = 2,
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "para_pass_aggr_mode_dmgin_buff")),
                                    BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_DamageOut(
                                            DamageDealt_Mod =  self.DamageOutReduction[self.Level],
                                            Duration = 2,
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "para_pass_aggr_mode_dmgout_debuff"))
                                    ]
            )
            return

        def GetDesc(self, DescLevel = 1):
            DmgAbsorbPerc = Battle_FormatDescVal(round((1.0 - self.DamageAbsorbtion[DescLevel]) * 100), Percentage = True)
            DmgDealPerc = Battle_FormatDescVal(round((1.0 - self.DamageOutReduction[DescLevel]) * 100), Percentage = True)
            return tra(_("Removes all harmful effects on yourself and puts yourself in a counter-attack state for 2 turns, increasing the damage you absorb by %s for 2 turns, but decreasing the damage you deal by %s for 2 turns.")) % (DmgAbsorbPerc, DmgDealPerc)