init python:
    @RegisterBattleSkill("BerserkerFrenziedState")
    class BattleSkill_BerserkerFrenziedState(BattleSkill):
        DisplayName = _("Frenzied State")

        Icon = "images/battle_skill_icons/berserker/FrenziedState.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 60
        Cost_PercHealthCurr = 0.3
        DamageValue = {1:0.3, 2:0.32, 3:0.34, 4:0.36}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_HIGH_OWN_HP_RATIO, AI_TAGS.FAVOURED_LOWER_TARGET_HP_RATIO}

        def Execute(self, Target):
            DmgMod = self.DamageValue[self.Level] + ((Target.Health / Target.HealthMax) / 2)
            for i in range(4):
                Battle_ScheduledAttack(
                    
                    SourceSkillObj = self,
                    AttackTarget = Target,
                    DamageMod = DmgMod)
            Battle_ApplyStatusEffect(
                TargetChar = self.Owner_BattleChar,
                StatusEffect = BattleStatusEff_StatMod_Armor(
                    Duration = 1, 
                    StatMod_Armor = 1.8, 
                    StatusEffectID = "bers_frenzy_armor_buff", 
                    SourceName = self.DisplayName))
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Sacrifices 30%% of your current hp and attacks the enemy 4 times, dealing %s base damage that increases in proportion to the enemy's missing hp.\nIncreases your armor by 80%% for 1 turn.")) % StrikeDamage