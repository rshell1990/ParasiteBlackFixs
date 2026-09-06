init python:
    @RegisterBattleSkill("RogueSquall")
    class BattleSkill_RogueSquall(BattleSkill):
        DisplayName = _("Squall")

        Icon = "images/battle_skill_icons/rogue/Squall.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 60

        DamageValue = {1:1.25, 2:1.35, 3:1.45, 4:1.55}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_HIGHER_DEX_THAN_TARGETS}

        def Execute(self, Target):
            DamageMod = self.DamageValue[self.Level] + (2 * (self.Owner_BattleChar.CharRef["Agility"] / 100))
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                GuaranteedCrit = (True if self.Owner_BattleChar.CharRef["Dexterity"] > Target.CharRef["Dexterity"] else False),
                Effects_OnCrit_User = [
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 2, StatMod_DodgeRating = 1.6, StatusEffectID = "roguesquall_dodgebuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_StatMod_Accuracy(Duration = 2, StatMod_AttackRating = 1.6, StatusEffectID = "roguesquall_arbuff", SourceName = self.DisplayName))],
                DamageMod = DamageMod)
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageMod = self.DamageValue[DescLevel] + (2 * (self.Owner_BattleChar.CharRef["Agility"] / 100))
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, DamageMod))
            else:
                DamageMod = self.DamageValue[DescLevel] + (2 * (worldChars[self.Owner_PBCharID]["Agility"] / 100))
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, DamageMod))
            BaseDmgAsPerc = Battle_FormatDescVal(round(self.DamageValue[DescLevel] * 100))
            DamageMultAsPerc = Battle_FormatDescVal(round(DamageMod * 100), Percentage = True)
            return tra(_("Leap to a target to deal %s damage that increases according to your agility. Improve your accuracy and dodge chance by 60%% for 2 turns if it lands a critical hit. This attack always lands a critical hit if your dexterity is higher than the enemy's dexterity.\nDamage multiplier: %s (%s + 2 * Agility)")) % (StrikeDamage, DamageMultAsPerc, BaseDmgAsPerc)