init python:
    @RegisterBattleSkill("NeutralPoisonThem")
    class BattleSkill_NeutralPoisonThem(BattleSkill):
        DisplayName = _("Poison Them")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 60

        DamageValue = {1:1.2}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}
        AIBaseWeight = 5.0

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Poison(Duration = 2, BaseValue = self.Owner_BattleChar.Damage, SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            Duration = 2, 
                            StatMod_Armor = 0.7, 
                            StatusEffectID = "poison_them_armordebuff", 
                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Attacks all enemies dealing %s damage and grants a poison effect to all of them for 2 turns. Also reduces the armour of all enemies by 30%% for 2 turns.")) % DamageValue