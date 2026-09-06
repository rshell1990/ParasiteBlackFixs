init python:
    @RegisterBattleSkill("ParasiteBlackUnstoppable")
    class BattleSkill_ParasiteBlackUnstoppable(BattleSkill):
        DisplayName = _("Unstoppable")
        
        Icon = "images/battle_skill_icons/parablack/Unstoppable.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 120

        DamageValue = {1:0.6, 2:0.6, 3:0.65, 4:0.65, 5:0.7}
        ArmorDebuff = {1:0.5, 2:0.4, 3:0.4,  4:0.3,  5:0.3}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}
        

        def Execute(self, Target):
            # cannot be dodged, remove 1 buff from enemy
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [BattleEffect_RemoveRandomBuffOnTarget()],
                GuaranteedHit = True)
    
            # apply armor debuff of X for 2 turns
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [BattleEffect_ApplyStatusOnEnemy(
                                        StatusEffect = BattleStatusEff_StatMod_Armor(
                                            Duration = 2,
                                            StatMod_Armor = self.ArmorDebuff[self.Level],
                                            StatusEffectID = "parablack_unstoppable_armor_debuff",
                                            SourceName = self.DisplayName))])

            # absorb energy for 50% of damage dealt
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                DamageRecoversAttackerEnergy = 0.5)
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            ArmorDebuffPerc = Battle_FormatDescVal(round((1.0 - self.ArmorDebuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Attack all enemies 3 times, dealing %s damage with each strike.\nThe first attack cannot be dodged and removes a random buff from the enemy.\nThe second attack decreases their armor by %s for 2 turns and the third attack absorbs their energy for 50%% of the damage dealt.")) % (StrikeDamage, ArmorDebuffPerc)