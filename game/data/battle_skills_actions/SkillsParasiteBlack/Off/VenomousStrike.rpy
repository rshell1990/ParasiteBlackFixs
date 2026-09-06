init python:
    @RegisterBattleSkill("ParasiteBlackVenomousStrike")
    class BattleSkill_ParasiteBlackVenomousStrike(BattleSkill):
        DisplayName = _("Venomous Strike")
        
        Icon = "images/battle_skill_icons/parablack/VenomousStrike.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 60

        DamageValue =     {1:1.5, 2:1.65, 3:1.65, 4:1.8,  5:1.8}
        DamageOutDebuff = {1:0.7, 2:0.7,  3:0.55, 4:0.55, 5:0.4}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [BattleEffect_ApplyStatusOnEnemy(
                                    StatusEffect = BattleStatusEff_Poison(
                                        BaseValue = self.Owner_BattleChar.Damage,
                                        Duration = 3,
                                        SourceName = self.DisplayName)),
                                BattleEffect_ApplyStatusOnEnemy(
                                    StatusEffect = BattleStatusEff_DamageOut(
                                        DamageDealt_Mod = self.DamageOutDebuff[self.Level],
                                        Duration = 3,
                                        SourceName = self.DisplayName, 
                                        StatusEffectID = "venomstrike_dmgout_debuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            DamageOutPerc = Battle_FormatDescVal(round((1.0 - self.DamageOutDebuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Inflict a poisonous tail swipe at the enemy, dealing %s damage, poisoning the enemy and reducing the damage they deal by %s for 3 turns.")) % (StrikeDamage, DamageOutPerc)