init python:    
    @RegisterBattleSkill("WarriorWhirlwindOfSteel")
    class BattleSkill_WarriorWhirlwindOfSteel(BattleSkill):    
        DisplayName = _("Whirlwind of Steel")
        
        Icon = "images/battle_skill_icons/warrior/WhirlwindOfSteel.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 100
        DamageValue = {1:1.9, 2:2.0, 3:2.0, 4:2.2}
        DebuffChance = {1:60, 2:60, 3:80, 4:80}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SoundSwing_CustomList = soundLib["Battle_WarriorBladey"],
                SourceSkillObj = self, 
                AttackTarget = BATTLE_TARGETS.ALL_ENEMIES,
                DamageMod = self.DamageValue[self.Level],
                CustomImpactVfxID = "Battle_VfxImpactSlashCircular",
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = self.DebuffChance[self.Level],
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                            Duration = 1,
                            StatMod_AttackRating = 0.6,
                            SourceName = self.DisplayName,
                            StatusEffectID = "warrior_whirlwind_acc_debuff")),
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = self.DebuffChance[self.Level],
                        StatusEffect = BattleStatusEff_StatMod_Dodge(
                            Duration = 1,
                            StatMod_DodgeRating = 0.6,
                            SourceName = self.DisplayName,
                            StatusEffectID = "warrior_whirlwind_dodge_debuff"))
                ]
            )
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]), Parentheses = True)
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]), Parentheses = True)
            DebuffChance = Battle_FormatDescVal(self.DebuffChance[DescLevel], Percentage = True)
            
            return tra(_("Attacks all enemies causing great damage %s and decreasing their accuracy and dodge chance by 60%% with %s chance.")) % (StrikeDamage, DebuffChance)
