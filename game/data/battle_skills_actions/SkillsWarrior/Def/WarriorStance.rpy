init python:
    @RegisterBattleSkill("WarriorWarriorStance")
    class BattleSkill_WarriorWarriorStance(BattleSkill):
        DisplayName = _("Warrior Stance")
        
        Icon = "images/battle_skill_icons/warrior/WarriorStance.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 85
        
        DamageValue =      {1:0.6, 2:0.6, 3:0.6, 4:0.6, 5:0.6}
        DamageDealtDebuff ={1:0.6, 2:0.6, 3:0.5, 4:0.5, 5:0.4}
        DamageResBuff =    {1:0.8, 2:0.7, 3:0.7, 4:0.6, 5:0.6}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE, AI_TAGS.TAUNT_TARGET}

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                                BattleEffect_ApplyStatusOnEnemy(
                                    StatusEffect = BattleStatusEff_Taunt(
                                        Duration = 1, 
                                        SourceName = self.DisplayName, 
                                        TauntedBy = self.Owner_BattleChar)),
                                BattleEffect_ApplyStatusOnEnemy(
                                    StatusEffect = BattleStatusEff_DamageOut(
                                        StatusEffectID = "warrior_warstance_dmgout_debuff",
                                        DamageDealt_Mod = self.DamageDealtDebuff[self.Level],
                                        Duration = 1,
                                        SourceName = self.DisplayName))])

            Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar,
                                    StatusEffect = BattleStatusEff_Counter(
                                        Duration = 2,
                                        SourceName = self.DisplayName))
            Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar, 
                                    StatusEffect = BattleStatusEff_DamageIn(
                                        DamageRecieved_Mod = self.DamageResBuff[self.Level] - 1.0,
                                        Duration = 2,
                                        SourceName = self.DisplayName))
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            DamageDealtDebuffPerc = Battle_FormatDescVal(round((1.0 - self.DamageDealtDebuff[DescLevel]) * 100), Percentage = True)
            DamageResBuffPerc = Battle_FormatDescVal(round((1.0 - self.DamageResBuff[DescLevel]) * 100), Percentage = True)

            return tra(_("Attacks all enemies quickly, causing minor damage of %s, provoking all enemies hit and reducing the damage they deal by %s for 1 turn.\nDamage you take is reduced by %s as you enter a counter stance for 2 turns.")) % (StrikeDamage, DamageDealtDebuffPerc, DamageResBuffPerc)