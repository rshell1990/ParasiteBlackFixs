init python:    
    @RegisterBattleSkill("WarriorDualStrike")
    class BattleSkill_WarriorDualStrike(BattleSkill):
        DisplayName = _("Dual Strike")
        
        Icon = "images/battle_skill_icons/warrior/DualStrike.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 50

        DamageValue =  {1:0.7, 2:0.75, 3:0.75, 4:0.8,  5:0.8}
        DebuffChance = {1:80,  2:80,   3:90,   4:90,   5:100}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                CustomImpactVfxID = "Battle_VfxImpactSlashCross",
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = self.DebuffChance[self.Level], 
                        StatusEffect = BattleStatusEff_StatMod_Armor(Duration = 3,
                            StatMod_Armor = 0.4,
                            StatusEffectID = "dual_strike_armor_mod",
                            SourceName = self.DisplayName))])

            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                CustomImpactVfxID = "Battle_VfxImpactSlashCross",
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = self.DebuffChance[self.Level], 
                        StatusEffect = BattleStatusEff_DamageOut(
                            StatusEffectID = "dual_strike_damageout_debuff",
                            DamageDealt_Mod = 0.4,
                            Duration = 3,
                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round(self.Owner_BattleChar.Damage * self.DamageValue[DescLevel])) + "{/color}"
            else:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round(worldChars[self.Owner_PBCharID]["Damage"] * self.DamageValue[DescLevel])) + "{/color}"
            DmgPercentage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round(self.DamageValue[DescLevel] * 100)) + "%{/color}"
            DebuffChance = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(self.DebuffChance[DescLevel]) + "%{/color}"
            return tra(_("Attacks the enemy twice with %s base damage (%s of char's base damage).\nFirst strike has a %s chance to decrease the target's armor by 60%% for 3 turns,\nsecond strike has a %s chance to decrease the target's damage dealt by 60%% for 3 turns.")) % (StrikeDamage, DmgPercentage, DebuffChance, DebuffChance)