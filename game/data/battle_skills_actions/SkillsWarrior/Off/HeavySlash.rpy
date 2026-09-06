init python:
    @RegisterBattleSkill("WarriorHeavySlash")
    class BattleSkill_WarriorHeavySlash(BattleSkill):
        DisplayName = _("Heavy Slash")
        
        Icon = "images/battle_skill_icons/warrior/HeavySlash.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 35

        DamageValue = {1:1.5, 2:1.6, 3:1.7, 4:1.8}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}
        AIBaseWeight = 1.1

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SoundSwing_CustomList = soundLib["Battle_WarriorBladey"],
                CustomImpactVfxID = "Battle_VfxImpactImpactHeavy",
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level])
            return
        
        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]) + "{/color}"
            else:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]) + "{/color}"
            DmgPercentage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round(self.DamageValue[DescLevel] * 100)) + "%{/color}"
            return tra(_("Deliver a powerful blow that deals %s damage (%s of char's base damage).")) % (StrikeDamage, DmgPercentage)