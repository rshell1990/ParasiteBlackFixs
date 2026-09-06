init python:
    @RegisterBattleSkill("AssassinCriticalBlows")
    class BattleSkill_AssassinCriticalBlows(BattleSkill):
        DisplayName = _("Critical Blows")
        Icon = "images/battle_skill_icons/assassin/CriticalBlows.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 100

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.IGNORES_ENEMY_ARMOR}

        DamageValue = {
            1:0.3,
            2:0.35,
            3:0.35,
        }

        # crit bonus is always a flat int
        CritPercentageBonus = {
            1:30,
            2:30,
            3:40,
        }

        def Execute(self, Target):
            for i in range(3):
                Battle_ScheduledAttack(
                    SourceSkillObj = self,
                    AttackTarget = BATTLE_TARGETS.ALL_ENEMIES,
                    DamageMod = self.DamageValue[self.Level],
                    Effects_OnHit_Target = [],
                    IgnoreArmor = True,
                    ExtraCritChancePercentage = self.CritPercentageBonus[self.Level],
                )
            return

        def GetDesc(self, DescLevel = 1):
            DamagePerc = Battle_FormatDescVal(round(self.DamageValue[DescLevel] * 100), Percentage = True)
            if self.Owner_BattleChar:
                DamageValDesc = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValDesc = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            CritChanceBonus = Battle_FormatDescVal(self.CritPercentageBonus[DescLevel], Percentage = True)
            return tra(_("Strike all the enemy team with 3 attacks (3x%s attack damage, %s), ignoring their armour. Receives a %s critical rate bonus when performing this attack.")) % (DamagePerc, DamageValDesc, CritChanceBonus)