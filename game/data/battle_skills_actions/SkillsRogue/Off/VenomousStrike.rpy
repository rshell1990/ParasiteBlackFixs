init python:
    @RegisterBattleSkill("RogueVenomousStrike")
    class BattleSkill_RogueVenomousStrike(BattleSkill):
        DisplayName = _("Venomous Strike")

        Icon = "images/battle_skill_icons/rogue/VenomousStrike.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 60

        DamageValue =  {1:0.6, 2:0.7, 3:0.7, 4:0.8, 5:0.8}
        DebuffChance = {1:0.3, 2:0.3, 3:0.4, 4:0.4, 5:0.5}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            DamageMod = (3 * (self.DamageValue[self.Level] + self.Owner_BattleChar.CharRef["Agility"] / 100))
            for i in range(3):
                Battle_ScheduledAttack(
                    SourceSkillObj = self,
                    AttackTarget = Target,
                    DamageMod = DamageMod,
                    Effects_OnHit_Target = [
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = self.DebuffChance[self.Level], 
                            StatusEffect = BattleStatusEff_StatMod_Armor(
                                Duration = 2, StatMod_Armor = 0.7, StatusEffectID = "roguevenomstrike_armor_debuff", SourceName = self.DisplayName)),
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = self.DebuffChance[self.Level], 
                            StatusEffect = BattleStatusEff_Poison(
                                            BaseValue = self.Owner_BattleChar.Damage,
                                            Duration = 2,
                                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageMod =  (3 * (self.DamageValue[DescLevel] + self.Owner_BattleChar.CharRef["Agility"] / 100))
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, DamageMod))
            else:
                DamageMod =  (3 * (self.DamageValue[DescLevel] + worldChars[self.Owner_PBCharID]["Agility"] / 100))
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, DamageMod))
            BaseDmgAsPerc = Battle_FormatDescVal(round(self.DamageValue[DescLevel] * 100))
            DamageMultAsPerc = Battle_FormatDescVal(round(DamageMod * 100), Percentage = True)
            DebuffChancePerc = Battle_FormatDescVal(round(self.DebuffChance[DescLevel] * 100), Percentage = True)
            return tra(_("Channel your focus and quickly attack the enemy 3 times at their weak point causing %s damage that increases according to your agility. Each attack has a %s chance of reducing the enemy's armor by 70%% and poisoning the target for 2 turns.\nDamage multiplier: %s (3 * (%s + Agility))")) % (StrikeDamage, DebuffChancePerc, DamageMultAsPerc, BaseDmgAsPerc)