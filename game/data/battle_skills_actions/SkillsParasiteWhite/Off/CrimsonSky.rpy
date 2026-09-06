init python:
    @RegisterBattleSkill("ParasiteWhiteCrimsonSky")
    class BattleSkill_ParasiteWhiteCrimsonSky(BattleSkill):
        DisplayName = _("Crimson Sky")
        Icon = "images/battle_skill_icons/parawhite/CrimsonSky.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 100

        DamageValue = {1:0.4,  2:0.43, 3:0.43, 4:0.46, 5:0.46}
        BurnChance =  {1:0.3,  2:0.3,  3:0.5, 4:0.5, 5:0.7}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            # do first 3 attacks
            for i in range(3):
                Battle_ScheduledAttack(
                    SoundImpact_CustomList = soundLib["Battle_FireImpacts"],
                    SoundSwing_CustomList = soundLib["Battle_FireStrikes"],
                    SourceSkillObj = self, 
                    AttackTarget = self.ValidTargets,
                    DamageMod = self.DamageValue[self.Level],
                    Effects_OnHit_Target = [
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = self.BurnChance[self.Level],
                            StatusEffect = BattleStatusEff_Burn(
                                BaseValue = self.Owner_BattleChar.Damage, 
                                Duration = 2, 
                                SourceName = self.DisplayName))],
                    AnimID = "attack_fire")

            # random enemies for last 2 attacks
            for i in range(2):
                EnemyList = Battle_GetAllEnemiesOfChar(self.Owner_BattleChar)
                for Enemy in reversed(EnemyList):
                    if renpy.random.randint(1, 2) == 1:
                        EnemyList.remove(Enemy)

                Battle_ScheduledAttack(
                    SoundImpact_CustomList = soundLib["Battle_FireImpacts"],
                    SoundSwing_CustomList = soundLib["Battle_FireStrikes"],
                    SourceSkillObj = self, 
                    AttackTarget = EnemyList,
                    DamageMod = self.DamageValue[self.Level],
                    Effects_OnHit_Target = [
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = self.BurnChance[self.Level],
                            StatusEffect = BattleStatusEff_Burn(
                                BaseValue = self.Owner_BattleChar.Damage, 
                                Duration = 2, 
                                SourceName = self.DisplayName))],
                    AnimID = "attack_fire")
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            BurnChancePerc = Battle_FormatDescVal(round(self.BurnChance[DescLevel] * 100), Percentage = True)
            return tra(_("Release hellfire into the skies causing all enemies to receive 3 to 5 random attacks dealing %s damage that cause an additional burn for 2 turns with a %s chance on each attack.")) % (StrikeDamage, BurnChancePerc)