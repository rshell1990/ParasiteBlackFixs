init python:
    @RegisterBattleSkill("NeutralCalculationMistake")
    class BattleSkill_NeutralCalculationMistake(BattleSkill):
        DisplayName = _("Calculation Mistake")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 60

        DamageValue = {1:1.6}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.REMOVE_BUFFS_ON_TARGET, AI_TAGS.IGNORES_ENEMY_DODGE}

        AIBaseWeight = 2.5

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                GuaranteedHit = True,
                Effects_OnHit_Target = [
                    BattleEffect_RemoveBuffsOnEnemyAndStunIfRemovedAny(
                        StunFor = 1, 
                        SourceName = self.DisplayName)])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Attacks all enemies with a blow that cannot be dodged, dealing %s damage and removing all their beneficial effects. Enemies with removed beneficial effects will be stunned for 1 turn.")) % DamageValue