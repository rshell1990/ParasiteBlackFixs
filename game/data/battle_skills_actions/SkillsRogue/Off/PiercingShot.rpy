init python:
    @RegisterBattleSkill("RoguePiercingShot")
    class BattleSkill_RoguePiercingShot(BattleSkill):
        DisplayName = _("Piercing Shot")
        Icon = "images/battle_skill_icons/rogue/PiercingShot.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 50
        DamageValue = {1:0.9, 2:1.0, 3:1.1, 4:1.2}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_HIGHER_AGI_THAN_TARGETS}

        def Execute(self, Target):
            DamageMod = self.DamageValue[self.Level] + (self.Owner_BattleChar.CharRef["Agility"] / 100)
            if Target.CharRef["Agility"] < self.Owner_BattleChar.CharRef["Agility"]:
                DamageMod *= 2
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = DamageMod)
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageMod = self.DamageValue[DescLevel] + (self.Owner_BattleChar.CharRef["Agility"] / 100)
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, DamageMod))
            else:
                DamageMod = self.DamageValue[DescLevel] + (worldChars[self.Owner_PBCharID]["Agility"] / 100)
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, DamageMod))
            BaseDmgAsPerc = Battle_FormatDescVal(round(self.DamageValue[DescLevel] * 100))
            DamageMultAsPerc = Battle_FormatDescVal(round(DamageMod * 100), Percentage = True)
            return tra(_("Aim with precision to deal %s damage that increases according to your agility. The damage multiplier is doubled if your agility is higher than the enemy agility.\nDamage multiplier: %s (%s + Agility)")) % (StrikeDamage, DamageMultAsPerc, BaseDmgAsPerc)