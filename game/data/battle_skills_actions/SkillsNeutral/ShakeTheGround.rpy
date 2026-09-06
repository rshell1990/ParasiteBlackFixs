init python:
    @RegisterBattleSkill("NeutralShakeTheGround")
    class BattleSkill_NeutralShakeTheGround(BattleSkill):    
        DisplayName = _("Shake The Ground")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 50

        DamageValue = {1:1.5}
        
        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        AIBaseWeight = 3.0

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SoundImpact_OneShotList = soundLib["Battle_EarthlyImpactsHvy"],
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Stun(Duration = 1, SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 2, StatMod_DodgeRating = 0.4, StatusEffectID = "neutral_shakeground_dodgedebuff", SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Attacks all enemies dealing %s damage, stunning them for 1 turn and decreasing their dodge chance by 60%% for 2 turns.")) % DamageValue