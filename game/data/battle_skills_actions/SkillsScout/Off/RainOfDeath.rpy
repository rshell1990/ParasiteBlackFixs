init python:
    @RegisterBattleSkill("ScoutRainOfDeath")
    class BattleSkill_ScoutRainOfDeath(BattleSkill):
        DisplayName = _("Rain Of Death")
        Icon = "images/battle_skill_icons/scout/RainOfDeath.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 80

        DamageValue = {1:0.4,  2:0.43,  3:0.43, 4:0.46, 5:0.46}
        BleedChance = {1:0.1,  2:0.1,   3:0.2,  4:0.2,  5:0.35}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            # do first 3 attacks
            for i in range(3):
                Battle_ScheduledAttack(
                    SourceSkillObj = self, 
                    AttackTarget = self.ValidTargets,
                    DamageMod = self.DamageValue[self.Level],
                    Effects_OnHit_Target = [
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = self.BleedChance[self.Level],
                            StatusEffect = BattleStatusEff_Bleed(
                                BaseValue = self.Owner_BattleChar.Damage, 
                                Duration = 1,
                                SourceName = self.DisplayName))])

            # random enemies for last 2 attacks
            for i in range(2):
                EnemyList = Battle_GetAllEnemiesOfChar(self.Owner_BattleChar)
                for Enemy in reversed(EnemyList):
                    if renpy.random.randint(1, 2) == 1:
                        EnemyList.remove(Enemy)

                Battle_ScheduledAttack(
                    SourceSkillObj = self, 
                    AttackTarget = EnemyList,
                    DamageMod = self.DamageValue[self.Level],
                    Effects_OnHit_Target = [
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = self.BleedChance[self.Level],
                            StatusEffect = BattleStatusEff_Bleed(
                                BaseValue = self.Owner_BattleChar.Damage, 
                                Duration = 1,
                                SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            BleedChancePerc = Battle_FormatDescVal(round(self.BleedChance[DescLevel] * 100), Percentage = True)
            return tra(_("Attacks all enemies 3 to 5 times, dealing %s damage and making them bleed for 1 turn with %s on each attack.")) % (StrikeDamage, BleedChancePerc)