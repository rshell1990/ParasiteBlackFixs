init python:
    @RegisterBattleSkill("NeutralHumiliatingAttack")
    class BattleSkill_NeutralHumiliatingAttack(BattleSkill):    
        DisplayName = _("Humiliating Attack")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 60

        AIBaseWeight = 3.0

        DamageValue = {1:1.5}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.TAUNT_TARGET}

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = 1.5,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_DamageOut(DamageDealt_Mod = 0.6, Duration = 2, SourceName = self.DisplayName, StatusEffectID = "neutral_humattack_dmgout_debuff")),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Taunt(Duration = 1, SourceName = self.DisplayName, TauntedBy = self.Owner_BattleChar)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Bleed(Duration = 1, BaseValue = self.Owner_BattleChar.Damage, SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Attacks all enemies for %s damage reducing the damage they deal by 40% for 2 turns, causing bleeding for 1 turn and taunting them for 1 turn.")) % DamageValue