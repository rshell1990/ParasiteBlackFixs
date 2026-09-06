init python:    
    @RegisterBattleSkill("WarriorFlailingStrikes")
    class BattleSkill_WarriorFlailingStikes(BattleSkill):
        DisplayName = _("Flailing Strikes")
        
        Icon = "images/battle_skill_icons/warrior/FlailingStrikes.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 70

        DamageValue =          {1:1.6, 2:1.7,  3:1.7,  4:1.8,  5:1.8}
        AccuracyDebuffChance = {1:60,  2:60,   3:70,   4:70,   5:80}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = BATTLE_TARGETS.ALL_ENEMIES,
                DamageMod = self.DamageValue[self.Level],
                CustomImpactVfxID = "Battle_VfxImpactSlashCross",
                Effects_OnHit_Target = [BattleEffect_ApplyStatusOnEnemy(
                                    Chance = self.AccuracyDebuffChance[self.Level],
                                    StatusEffect = BattleStatusEff_StatMod_Accuracy(
                                        Duration = 2,
                                        StatMod_AttackRating = 0.6,
                                        SourceName = self.DisplayName,
                                        StatusEffectID = "flailingstrike_acc_debuff"))
                                ]
            )
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]) + "{/color}"
            else:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]) + "{/color}"
            DmgPercentage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round(self.DamageValue[DescLevel] * 100)) + "%{/color}"
            DebuffChance = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(self.AccuracyDebuffChance[DescLevel]) + "%{/color}"
            return tra(_("Attacks all enemies causing %s damage (%s of char's base damage).\nWith %s chance, applies an accuracy debuff of 60%% for 2 turns.")) % (StrikeDamage, DmgPercentage, DebuffChance)