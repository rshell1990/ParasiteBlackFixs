init python:
    @RegisterBattleSkill("NeutralSuperHeavyBlow")
    class BattleSkill_NeutralSuperHeavyBlow(BattleSkill):
        DisplayName = _("Super Heavy Blow")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        Cost_Energy = 30

        DamageValue = {1:1.7}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        AIBaseWeight = 3.0
        
        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = 1.7,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                            Duration = 1, 
                            StatMod_AttackRating = 0.4, 
                            StatusEffectID = "neutralshblow_accdebuf", 
                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Strikes the enemy to deal %s damage and decrease their accuracy by 60%% for 1 turn.")) % DamageValue