init python:
    @RegisterBattleSkill("ParasiteWhiteCursedConnection")
    class BattleSkill_ParasiteWhiteCursedConnection(BattleSkill):
        DisplayName = _("Cursed Connection")

        Icon = "images/battle_skill_icons/parawhite/CursedConnection.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 120

        DamageValue = {1:1.3, 2:1.4, 3:1.5, 4:1.6}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        AIBaseWeight = 1.1

        def Execute(self, Target):
            Battle_ScheduledAttack(
                 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level] + (3 * (self.Owner_BattleChar.CharRef["Agility"] / 100)),
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.75,
                        StatusEffect = BattleStatusEff_Stun(
                            Duration = 1, 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.75,
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                            Duration = 2, 
                            StatMod_AttackRating = 0.5, 
                            StatusEffectID = "parawhite_cursedcon_accdebuff", 
                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DmgMod = self.DamageValue[DescLevel] + (3 * (self.Owner_BattleChar.CharRef["Agility"] / 100))
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, DmgMod))
            else:
                DmgMod = self.DamageValue[DescLevel] + (3 * (worldChars[self.Owner_PBCharID]["Agility"] / 100))
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, DmgMod))

            BaseDmgAsPerc = Battle_FormatDescVal(round(self.DamageValue[DescLevel] * 100), Percentage = True)
            DamageMultAsPerc = Battle_FormatDescVal(round(DmgMod * 100), Percentage = True)

            return tra(_("Attacks all enemies with a swift blow that deals %s damage and stuns them for 1 turn and reduces their accuracy by 50%% for 2 turns with a 75%% chance each. The damage of this skill increases according to your agility.\nDamage multiplier: %s (%s + 3 * Agility)")) % (StrikeDamage, DamageMultAsPerc, BaseDmgAsPerc)