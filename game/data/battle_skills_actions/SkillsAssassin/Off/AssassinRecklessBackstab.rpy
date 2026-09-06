init python:
    @RegisterBattleSkill("AssassinRecklessBackstab")
    class BattleSkill_AssassinRecklessBackstab(BattleSkill):
        DisplayName = _("Reckless Backstab")

        Icon = "images/battle_skill_icons/assassin/RecklessBackstab.webp"

        Level_Max = 4

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 40

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_HIGH_OWN_HP_RATIO}

        DamageValue = {
            1:1.5,
            2:1.6,
            3:1.6,
            4:1.6,
        }

        CritPercentageBonus = {
            1:50,
            2:50,
            3:60,
            4:60,
        }

        ArmorModifier = {
            1:0.8,
            2:0.8,
            3:0.8,
            4:0.9,
        }

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                ExtraCritChancePercentage = self.CritPercentageBonus[self.Level],
            )

            # add armor drop to self
            Battle_ApplyStatusEffect(
                TargetChar = self.Owner_BattleChar, 
                StatusEffect = BattleStatusEff_StatMod_Armor(
                    Duration = 2,
                    StatMod_Armor = self.ArmorModifier[self.Level],
                    StatusEffectID = "assassin_recklessbackstab_armordebuff",
                    SourceName = self.DisplayName), 
                CastOnEnemy = False)
            return

        def GetDesc(self, DescLevel = 1):
            DamagePerc = Battle_FormatDescVal(round(self.DamageValue[DescLevel] * 100), Percentage = True)
            CritPerc = Battle_FormatDescVal(self.CritPercentageBonus[DescLevel], Percentage = True)
            if self.Owner_BattleChar:
                DamageValDesc = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValDesc = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            ArmorDropPerc = Battle_FormatDescVal(round((1.0 - self.ArmorModifier[DescLevel]) * 100), Percentage = True)
            return tra(_("Emerging from the darkness, you plunge your dagger into the back of a single enemy for huge damage (%s, %s). Has a %s increase of current crit chance for the strike... But leaves yourself exposed afterwards with an armour drop of %s for 2 round.")) % (DamagePerc, DamageValDesc, CritPerc, ArmorDropPerc)
