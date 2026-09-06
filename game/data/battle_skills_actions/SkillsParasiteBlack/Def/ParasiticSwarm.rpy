init python:
    @RegisterBattleSkill("ParasiteBlackParasiticSwarm")
    class BattleSkill_ParasiteBlackParasiticSwarm(BattleSkill):
        DisplayName = _("Parasitic Swarm")
        
        Icon = "images/battle_skill_icons/parablack/ParasiticSwarm.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 40

        EnemyDamageReduction = {1:0.6, 2:0.5, 3:0.4}

        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [BattleEffect_ApplyStatusOnEnemy(
                                        StatusEffect = BattleStatusEff_HealthRecoveryMod(
                                            ResRecoverMod_Health = 0.4,
                                            Duration = 2, 
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "para_swarm_hp_recover_debuff")),
                                    BattleEffect_ApplyStatusOnEnemy(
                                        StatusEffect = BattleStatusEff_EnergyRecoveryMod(
                                            ResRecoverMod_Energy = 0.4,
                                            Duration = 2, 
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "para_swarm_ep_recover_debuff")),
                                    BattleEffect_ApplyStatusOnEnemy(
                                        StatusEffect = BattleStatusEff_DamageOut(
                                            DamageDealt_Mod = self.EnemyDamageReduction[self.Level], 
                                            Duration = 2, 
                                            SourceName = self.DisplayName, 
                                            StatusEffectID = "para_swarm_dmgout_debuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            DmgReductionPercentage = Battle_FormatDescVal(round((1.0 - self.EnemyDamageReduction[DescLevel]) * 100), Percentage = True)
            return tra(_("Casts a parasitic plague on all enemies reducing the damage they deal by %s and their healing and energy recovery by 60%% for 2 turns.")) % DmgReductionPercentage