init python:
    @RegisterBattleSkill("NeutralColdWeather")
    class BattleSkill_NeutralColdWeather(BattleSkill):    
        DisplayName = _("Cold Weather")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        Cost_Mana = 40 # mages only

        DamageValue = {1:1.3}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}
        AIBaseWeight = 3.0

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(StatMod_DodgeRating = 0.6, Duration = 2, SourceName = self.DisplayName, StatusEffectID = "neutral_cw_dodge_debuff")),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(Duration = 2, StatMod_AttackRating = 0.6, SourceName = self.DisplayName, StatusEffectID = "neutral_cw_acc_debuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Attacks the enemy for %s damage with an attempt to freeze them, reducing their accuracy and dodge rate by 40%% for 2 turns.")) % DamageValue