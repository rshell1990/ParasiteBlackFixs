init python:
    @RegisterBattleSkill("ParasiteBlackPerfectOrganism")
    class BattleSkill_ParasiteBlackPerfectOrganism(BattleSkill):
        DisplayName = _("Perfect Organism")
        
        Icon = "images/battle_skill_icons/parablack/PerfectOrganism.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES_NOT_SELF

        Cost_Energy = 80

        AlliesEnergyRecoveryValue = {1:0.15, 2:0.2, 3:0.25, 4:0.3}

        AITags = {AI_TAGS.RAISE_TARGET_PHYS_DAMAGE_RESISTANCE, AI_TAGS.FAVOURED_LOW_TARGET_ENERGY}

        def Execute(self, Target):            
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = BATTLE_TARGETS.ALL_ALLIES_NOT_SELF,
                Effects_OnTarget = [BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_DamageIn(
                                            DamageRecieved_Mod = 0.6,
                                            Duration = 2,
                                            SourceName = self.DisplayName)),
                                    BattleEffect_RestoreEnergy(self.AlliesEnergyRecoveryValue[self.Level], RatioFromMax = True)],

                Effects_OnSelf = [BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_DamageOut(
                                            DamageDealt_Mod = 0.8, 
                                            Duration = 2, 
                                            SourceName = self.DisplayName, 
                                            StatusEffectID = "parablack_perfectorg_dmg_debuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            EnergyRecoverPerc = Battle_FormatDescVal(round(self.AlliesEnergyRecoveryValue[DescLevel] * 100), Percentage = True)
            return tra(_("Sacrifices the damage you deal by 20%% for 2 turns and increases the damage your allies absorb by 40%% for 2 turns and recovers the energy of all of them (excluding you) by %s.")) % EnergyRecoverPerc