init python:
    @RegisterBattleSkill("RogueWolfPoisonedFangs")
    class BattleSkill_RogueWolfPoisonedFangs(BattleSkill):
        DisplayName = _("Poisoned Fangs")
        Icon = "images/battle_skill_icons/rogue_wolf/PoisonedFangs.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 60

        DamageValue = {
            1:1.2,
            2:1.3,
            3:1.4,
            4:1.5}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            DmgMod = (self.DamageValue[self.Level] + (5 * self.Owner_BattleChar.CharRef["Agility"] / 100))
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = DmgMod,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Poison(BaseValue = self.Owner_BattleChar.Damage, Duration = 1, SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Poison(BaseValue = self.Owner_BattleChar.Damage, Duration = 1, SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Poison(BaseValue = self.Owner_BattleChar.Damage, Duration = 1, SourceName = self.DisplayName))])
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                BattleEffect_ApplyStatusOnAlly(
                    StatusEffect = BattleStatusEff_StatMod_Dodge(
                        Duration = 1,
                        StatMod_DodgeRating = 2.0, 
                        StatusEffectID = "elenawolf_poisonfangs_dodgeboost", 
                        SourceName = self.DisplayName)),
                BattleEffect_ApplyStatusOnAlly(
                    StatusEffect = BattleStatusEff_StatMod_Accuracy(
                        Duration = 1,
                        StatMod_AttackRating = 2.0, 
                        StatusEffectID = "elenawolf_poisonfangs_accboost", 
                        SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DmgMod = (self.DamageValue[DescLevel] + (5 * self.Owner_BattleChar.CharRef["Agility"] / 100))
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, DmgMod))
            else:
                DmgMod = (self.DamageValue[DescLevel] + (5 * worldChars[self.Owner_PBCharID]["Agility"] / 100))
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, DmgMod))
            DmgMultiplierPerc = Battle_FormatDescVal(round(DmgMod * 100), Percentage = True)
            DmgMultiplierBase = Battle_FormatDescVal(round(self.DamageValue[DescLevel] * 100))

            return tra(_("What have you been eating? Attacks the enemy quickly, causing %s damage proportional to your agility, grants 3 poison effects for 1 turn to the enemy and increases your accuracy and dodge by 100%% for 1 turn.\nDamage multiplier: %s (%s + (5 * Agility))")) % (DamageValue, DmgMultiplierPerc, DmgMultiplierBase)