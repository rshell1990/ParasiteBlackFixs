init python:    
    @RegisterBattleSkill("WarriorObliteratingBlow")
    class BattleSkill_WarriorObliteratingBlow(BattleSkill):
        DisplayName = _("Obliterating Blow")
        
        Icon = "images/battle_skill_icons/warrior/ObliteratingBlow.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 60
        Cost_PercHealthCurr = 0.5

        DamageValue =  {1:3.0, 2:3.0, 3:3.2, 4:3.2}
        ArmorBuff =    {1:2.0, 2:2.2, 3:2.2, 4:2.4}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_HIGH_OWN_HP_RATIO}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SoundSwing_CustomList = soundLib["Battle_WarriorBladey"],
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                CustomImpactVfxID = "Battle_VfxImpactSlashUppercutPiercey")
            Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar, 
                StatusEffect = BattleStatusEff_StatMod_Armor(Duration = 2, 
                    StatMod_Armor = self.ArmorBuff[self.Level], 
                    StatusEffectID = "warrior_obl_blow_armorbuff", 
                    SourceName = self.DisplayName))
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}(" + Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]) + "){/color}"
                HpToLose = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}(" + str(max(int(self.Owner_BattleChar.Health * self.Cost_PercHealthCurr), 1)) + "){/color}"
            else:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}(" + Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]) + "){/color}"
                HpToLose = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}(" + str(max(int(worldChars[self.Owner_PBCharID]["Health"] * self.Cost_PercHealthCurr), 1)) + "){/color}"
            ArmorBuff = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round((self.ArmorBuff[DescLevel] - 1.0) * 100)) + "%{/color}"
            
            return tra(_("Sacrifices 50%% of your current hp %s to attack the enemy, causing great damage %s and then increases your armor by %s for two turns.")) % (HpToLose, StrikeDamage, ArmorBuff)