init python:
    @RegisterBattleSkill("NeutralItCouldHaveBeenWorse")
    class BattleSkill_NeutralItCouldHaveBeenWorse(BattleSkill):
        DisplayName = _("It Could Have Been Worse")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 70

        DamageValue = {1:1.7}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}
        AIBaseWeight = 1.5

        def Execute(self, Target):
            for EnemyChar in Battle_GetAllEnemiesOfChar(self.Owner_BattleChar):
                for StatusEffect in reversed(EnemyChar.StatusEffects):
                    if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                        EnemyChar.StatusEffects.remove(StatusEffect)

            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Armor(Duration = 2, StatMod_Armor = 0.3, StatusEffectID = "neutral_ichbw_armordebuff", SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Attack all enemies dealing %s damage, removing all of their beneficial effects and decreasing their armor by 70%% for 2 turns.")) % DamageValue