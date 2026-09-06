init python:
    @RegisterBattleSkill("AssassinALovingKissOfDeath")
    class BattleSkill_AssassinALovingKissOfDeath(BattleSkill):
        DisplayName = _("A Loving Kiss Of Death")

        Icon = "images/battle_skill_icons/assassin/ALovingKissOfDeath.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ANY_ALLY

        Cost_Energy = 50

        AITags = {AI_TAGS.FAVOURED_HIGH_OWN_HP_RATIO, AI_TAGS.ONLY_IF_ALLIES_EXIST}

        def Execute(self, Target):
            ## does the swap here
            SelfHPRatio = self.Owner_BattleChar.Health / self.Owner_BattleChar.HealthMax
            SelfEnergyRatio = (self.Owner_BattleChar.Energy - self.Cost_Energy) / self.Owner_BattleChar.EnergyMax

            TargetHPRatio = Target.Health / Target.HealthMax
            TargetEnergyRatio = Target.Energy / Target.EnergyMax

            Target.Health = min(max(round(Target.HealthMax * SelfHPRatio), 1),     Target.HealthMax)
            Target.Energy = min(max(round(Target.EnergyMax * SelfEnergyRatio), 1), Target.EnergyMax)

            self.Owner_BattleChar.Health = min(max(round(self.Owner_BattleChar.HealthMax * TargetHPRatio), 1), self.Owner_BattleChar.HealthMax)
            self.Owner_BattleChar.Energy = min(max(round(self.Owner_BattleChar.EnergyMax * TargetEnergyRatio), 1), self.Owner_BattleChar.EnergyMax)

            ## effects
            TargetEffects = []
            TargetEffects.append(BattleEffect_ApplyStatusOnAlly(Chance = 1.0, StatusEffect = BattleStatusEff_Invincibility(Duration = 1, SourceName = self.DisplayName)))
            if self.Level >= 2:
                TargetEffects.append(BattleEffect_ApplyStatusOnAlly(Chance = 1.0, StatusEffect = BattleStatusEff_DamageOut(DamageDealt_Mod = 1.25, Duration = 1, SourceName = self.DisplayName, StatusEffectID = "assassin_lovingkiss_dmgoutbuff")))
            if self.Level >= 3:
                TargetEffects.append(BattleEffect_ApplyStatusOnAlly(Chance = 1.0, StatusEffect = BattleStatusEff_StatMod_CritChance(Duration = 1, StatMod_CritChance = 1.3, StatusEffectID = "assassin_lovingkiss_critchancebuff", SourceName = self.DisplayName)))

            # self eff here
            SelfEffects = [BattleEffect_ApplyStatusOnAlly(Chance = 1.0, StatusEffect = BattleStatusEff_Stun(Duration = 1, SourceName = self.DisplayName))]

            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = Target,
                Effects_OnTarget = TargetEffects,
                Effects_OnSelf = SelfEffects,
            )
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("(After consuming the cost of using the skill) Switch your current HP and energy percent with a party member and grant them invincibility for 1 turn.\nAt level 2, will also increase their total dmg to 125% for 1 round.\nAt level 3, will increase their crit chance by 30% for 1 round.\nYou are stunned for 1 turn after using this skill."))