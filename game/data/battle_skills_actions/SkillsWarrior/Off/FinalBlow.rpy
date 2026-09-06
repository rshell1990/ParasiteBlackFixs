init python:    
    @RegisterBattleSkill("WarriorFinalBlow")
    class BattleSkill_WarriorFinalBlow(BattleSkill):
        DisplayName = _("Final Blow")
        
        Icon = "images/battle_skill_icons/warrior/FinalBlow.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 70

        DamageValue = {1:1.4, 2:1.5, 3:1.6, 4:1.7}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_LAST_HIT}

        def Execute(self, Target):
            AdditionalDamage = 0.0
            for StatusEff in Target.StatusEffects:
                if StatusEff.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                    AdditionalDamage += 0.1

            Battle_ScheduledAttack( 
                SoundSwing_CustomList = soundLib["Battle_WarriorBladey"],
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level] + AdditionalDamage,
                IgnoreArmor = True,
                Effects_OnKill_User = [
                    BattleEffect_RestoreEnergy(RestoreValue = self.Cost_Energy),
                    BattleEffect_ApplyStatusOnAlly(1.0, 
                        StatusEffect = BattleStatusEff_Willpower(
                            Duration = 1,
                            SourceName = self.DisplayName)
                        )
                    ],
                CustomImpactVfxID = "Battle_VfxImpactBloodyImpact")

            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]) + "{/color}"
            else:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]) + "{/color}"
            DmgPercentage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round(self.DamageValue[DescLevel] * 100)) + "%{/color}"
            return tra(_("Aim at the enemy's guard and attack them, ignoring their armor, with a base damage of %s (%s of char's base damage).\nDamage increases by 10%% for each buff on the enemy.\nIf the enemy is killed with this strike, the energy cost of %s is recovered and you get willpower for 1 turn.")) % (StrikeDamage, DmgPercentage, self.Cost_Energy)