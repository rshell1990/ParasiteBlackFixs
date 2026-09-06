init python:
    @RegisterBattleSkill("NeutralPoisonAttack")
    class BattleSkill_NeutralPoisonAttack(BattleSkill):    
        DisplayName = _("Poison Attack")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        Cost_Energy = 40

        DamageValue = {1:1.6}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}
        AIBaseWeight = 3.0

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Poison(Duration = 3, BaseValue = self.Owner_BattleChar.Damage, SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Attacks an enemy dealing %s damage and applies a poison for 3 turns.")) % DamageValue