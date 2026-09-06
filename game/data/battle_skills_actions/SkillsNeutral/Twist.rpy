init python:
    @RegisterBattleSkill("NeutralTwist")
    class BattleSkill_NeutralTwist(BattleSkill):    
        DisplayName = _("Twist")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 50

        DamageValue = {1: 1.5}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        AIBaseWeight = 3.0

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_DamageOut(DamageDealt_Mod = 0.5, Duration = 2, SourceName = self.DisplayName, StatusEffectID = "neutral_twist_dmgout_debuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Attacks all enemies for %s damage and reduces the damage they deal by 50%% for 2 turns.")) % DamageValue
