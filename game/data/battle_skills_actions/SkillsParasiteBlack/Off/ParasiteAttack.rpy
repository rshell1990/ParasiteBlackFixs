init python:
    @RegisterBattleSkill("ParasiteBlackParasiteAttack")
    class BattleSkill_ParasiteBlackParasiteAttack(BattleSkill):
        DisplayName = _("Parasite Attack")

        Icon = "images/battle_skill_icons/parablack/ParaAttack.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        BurnEnemyEnergyByDamage = {1:0.5, 2:0.6, 3:0.7, 4:0.8, 5:0.9}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_HIGH_OWN_ENERGY_RATIO}

        def Execute(self, Target):
            EnergyToBurn = self.Owner_BattleChar.Energy
            DamageMultiplier = self.BurnEnemyEnergyByDamage[self.Level] + (EnergyToBurn / 100) * 1.3

            Battle_BurnEnergy(self.Owner_BattleChar, EnergyToBurn)
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = DamageMultiplier,
                DamageBurn_Energy = 0.3,
                DamageBurn_Mana = 0.3,
                Effects_OnHit_Target = [BattleEffect_ApplyStatusOnEnemy(
                                    OnZeroEnergyOnly = True,
                                    StatusEffect = BattleStatusEff_Stun(
                                        Duration = 1,
                                        SourceName = self.DisplayName))])
            return

        def CanExecute(self):
            if self.Owner_BattleChar.Energy < 1:
                return False
            return True

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                EnergyToBurn = self.Owner_BattleChar.Energy
                DamageMultiplier = self.BurnEnemyEnergyByDamage[DescLevel] + (EnergyToBurn / 100) * 1.3
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, DamageMultiplier))
            else:
                EnergyToBurn = worldChars[self.Owner_PBCharID]["Energy"]
                DamageMultiplier = self.BurnEnemyEnergyByDamage[DescLevel] + (EnergyToBurn / 100) * 1.3
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, DamageMultiplier))
            return tra(_("Burns all your energy to attack the enemy with a blow that deals damage that increases according to the amount of energy burned (%s damage). Burns the enemy's energy or mana by 30%% of the damage dealt. If the enemy's energy reaches zero they are stunned for 1 turn.")) % StrikeDamage
