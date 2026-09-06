init python:
    @RegisterBattleSkill("WarriorDefensiveStance")
    class BattleSkill_WarriorDefensiveStance(BattleSkill):
        DisplayName = _("Defensive Stance")
        Icon = "images/battle_skill_icons/warrior/DefensiveStance.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 65

        DamageValue =  {1:0.4, 2:0.4,  3:0.4,  4:0.4}
        TauntChance =  {1:80,  2:80,   3:80,   4:100}
        DamageResBuff ={1:1.4, 2:1.5,  3:1.6,  4:1.6}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE, AI_TAGS.TAUNT_TARGET}

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [BattleEffect_RemoveBuffsOnTarget(Chance = 0.8)])
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [BattleEffect_ApplyStatusOnEnemy(Chance = self.TauntChance[self.Level] / 100, StatusEffect = BattleStatusEff_Taunt(Duration = 1, SourceName = self.DisplayName, TauntedBy = self.Owner_BattleChar))])
            Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar,
                                    StatusEffect = BattleStatusEff_Counter(
                                        Duration = 2,
                                        SourceName = self.DisplayName))
            Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar, 
                                    StatusEffect = BattleStatusEff_DamageIn(
                                        DamageRecieved_Mod = self.DamageResBuff[self.Level] - 1.0,
                                        Duration = 2,
                                        SourceName = self.DisplayName))
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round(self.Owner_BattleChar.Damage * self.DamageValue[DescLevel])) + "{/color}"
            else:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round(worldChars[self.Owner_PBCharID]["Damage"] * self.DamageValue[DescLevel])) + "{/color}"
            TauntChance = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(self.TauntChance[DescLevel]) + "%{/color}"
            DamageResPercentage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round((self.DamageResBuff[DescLevel] - 1.0) * 100)) + "%{/color}"
            return tra(_("Attacks the enemy twice with minor base damage of %s (40%% of char's base damage).\nThe first attack has an 80%% chance to remove all beneficial effects.\nThe second attack provokes the enemy for 1 turn with an %s chance.\nApplies damage resistance buff of %s and a counter status effect on yourself for 2 turns.")) % (StrikeDamage, TauntChance, DamageResPercentage)