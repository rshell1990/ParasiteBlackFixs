init python:
    @RegisterBattleSkill("BerserkerBloodForTheBloodGod")
    class BattleSkill_BerserkerBloodForTheBloodGod(BattleSkill):
        DisplayName = _("Blood for the Blood God")

        Icon = "images/battle_skill_icons/berserker/BloodForTheBloodGod.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 80

        DamageValue =      {1:0.4,    2:0.44,     3:0.44,     4:0.48,     5:0.48}
        BuffRemovalChance ={1:0.3,    2:0.3,      3:0.4,      4:0.4,      5:0.5}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.REMOVE_BUFFS_ON_TARGET}

        def Execute(self, Target):
            DmgMod = (self.DamageValue[self.Level] + (self.Owner_BattleChar.CharRef["Endurance"] / 100))
            for i in range(3):
                Battle_ScheduledAttack(
                    SourceSkillObj = self,
                    AttackTarget = self.ValidTargets,
                    DamageMod = DmgMod,
                    Effects_OnHit_Target = [
                        BattleEffect_RemoveRandomBuffOnTarget(Chance = self.BuffRemovalChance[self.Level])])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageMod = (self.DamageValue[DescLevel] + (self.Owner_BattleChar.CharRef["Endurance"] / 100)) * 3
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, DamageMod))
            else:
                DamageMod = (self.DamageValue[DescLevel] + (worldChars[self.Owner_PBCharID]["Endurance"] / 100)) * 3
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, DamageMod))
            BaseDmg = Battle_FormatDescVal(round(self.DamageValue[DescLevel] * 100))
            BuffRemovalChancePerc = Battle_FormatDescVal(round(self.BuffRemovalChance[DescLevel] * 100), Percentage = True)
            DamageMultAsPerc = Battle_FormatDescVal(round(DamageMod * 100), Percentage = True)
            return tra(_("Enters a state of rage, attacking all enemies 3 times and dealing %s damage that increases according to your Endurance. The attack has a %s chance of removing a buff from an enemy.\nDamage multiplier: %s (3 * (%s + Endurance).")) % (StrikeDamage, BuffRemovalChancePerc, DamageMultAsPerc, BaseDmg)