init python:
    @RegisterBattleSkill("ParasiteBlackTerrifyingScream")
    class BattleSkill_ParasiteBlackTerrifyingScream(BattleSkill):
        DisplayName = _("Terrifying Scream")
        
        Icon = "images/battle_skill_icons/parablack/TerrScream.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 40

        AccuracyBoostValues =  {1:1.6, 2:1.6, 3:1.8, 4:1.8}
        EnemyDamageReduction = {1:0.6, 2:0.5, 3:0.5, 4:0.4}

        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                PlayCharSkinUseSkillSound = False,
                SoundUse_CustomList = ["audio/battle/battle_chars/mc_transformed/skill_terrifyingscream.ogg"],
                Effects_OnTarget = [BattleEffect_ApplyStatusOnEnemy(
                                        StatusEffect = BattleStatusEff_DamageOut(
                                            DamageDealt_Mod = self.EnemyDamageReduction[self.Level],
                                            Duration = 2,
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "para_terrifyingscream_dmgout_debuff"))],
                Effects_OnSelf = [BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                                            StatMod_AttackRating = self.AccuracyBoostValues[self.Level],
                                            Duration = 2,
                                            SourceName = self.DisplayName,
                                            StatusEffectID = "para_terrifyingscream_acc_buff"))])
            
            return

        def GetDesc(self, DescLevel = 1):
            EnemyDamageDealtPercentage = Battle_FormatDescVal(round((1.0 - self.EnemyDamageReduction[DescLevel]) * 100), Percentage = True)
            AccuracyBoostPercentage = Battle_FormatDescVal(round((self.AccuracyBoostValues[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Fires a terrifying scream reducing the damage dealt by all enemies by %s for 2 turns and increasing your accuracy by %s for 2 turns.")) % (EnemyDamageDealtPercentage, AccuracyBoostPercentage)