init python:
    @RegisterBattleSkill("RogueWolfSuddenStrike")
    class BattleSkill_RogueWolfSuddenStrike(BattleSkill):
        DisplayName = _("Sudden Strike")
        Icon = "images/battle_skill_icons/rogue_wolf/SuddenStrike.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 60

        DamageValue = {
            1:1.0,
            2:1.15,
            3:1.3}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.REMOVE_BUFFS_ON_TARGET}

        def Execute(self, Target):
            DmgMod = (self.DamageValue[self.Level] + (8 * self.Owner_BattleChar.CharRef["Agility"] / 100))
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = DmgMod,
                Effects_OnHit_Target = [
                    BattleEffect_RemoveBuffsOnTarget(),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Armor(Duration = 2, StatMod_Armor = 0.3, StatusEffectID = "wolf_suddenstrike_armordebuff", SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DmgMod = (self.DamageValue[DescLevel] + (8 * self.Owner_BattleChar.CharRef["Agility"] / 100))
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DmgMod = (self.DamageValue[DescLevel] + (8 * worldChars[self.Owner_PBCharID]["Agility"] / 100))
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            DmgMultiplierPerc = Battle_FormatDescVal(round(DmgMod * 100), Percentage = True)
            DmgMultiplierBase = Battle_FormatDescVal(round(self.DamageValue[DescLevel] * 100))
            return tra(_("Strike suddenly and unexpectedly to deal %s damage that increases according to your agility. Strips all buffs from the enemy and decreases the enemy's armor by 70%% for 2 turns.\nDamage multiplier: %s (%s + (8 * Agility))")) % (DamageValue, DmgMultiplierPerc, DmgMultiplierBase)