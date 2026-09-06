init python:
    @RegisterBattleSkill("NeutralIgniteThem")
    class BattleSkill_NeutralIgniteThem(BattleSkill):    
        DisplayName = _("Ignite Them")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 40

        DamageValue = {1:1.2}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.EFFECT_SCALES_WITH_AMOUNT_OF_DEBUFFS_ON_TARGET}

        AIBaseWeight = 2.0

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                DamageMod_AdditivePerDebuffOnTarget = 0.2,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Burn(Duration = 2, BaseValue = self.Owner_BattleChar.Damage, SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Attacks all enemies for %s damage, applies a burn effect to all of them for 2 turns. The damage of this ability increases by 20%% for each harmful effect on the enemy.")) % DamageValue