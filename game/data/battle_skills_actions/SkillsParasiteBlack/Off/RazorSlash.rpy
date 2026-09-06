init python:
    @RegisterBattleSkill("ParasiteBlackRazorSlash")
    class BattleSkill_ParasiteBlackRazorSlash(BattleSkill):
        DisplayName = _("Razor Slash")
        
        Icon = "images/battle_skill_icons/parablack/RazorSlash.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 50

        DamageValue =     {1:0.5, 2:0.6, 3:0.6,  4:0.7,  5:0.7}
        DebuffChance =    {1:0.4, 2:0.4, 3:0.55, 4:0.55, 5:0.7}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                CustomImpactVfxID = "Battle_VfxImpactSlashCross",
                Effects_OnHit_Target = [BattleEffect_ApplyStatusOnEnemy(Chance = self.DebuffChance[self.Level], 
                                    StatusEffect = BattleStatusEff_StatMod_Armor(
                                        Duration = 3,
                                        StatMod_Armor = 0.3,
                                        StatusEffectID = "razor_slash_armor_debuff",
                                        SourceName = self.DisplayName))])
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                CustomImpactVfxID = "Battle_VfxImpactSlashCross",
                Effects_OnHit_Target = [BattleEffect_ApplyStatusOnEnemy(Chance = self.DebuffChance[self.Level], 
                                    StatusEffect = BattleStatusEff_StatMod_Armor(
                                        Duration = 3,
                                        StatMod_Armor = 0.3,
                                        StatusEffectID = "razor_slash_armor_debuff",
                                        SourceName = self.DisplayName))])
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                CustomImpactVfxID = "Battle_VfxImpactSlashCross",
                Effects_OnHit_Target = [BattleEffect_ApplyStatusOnEnemy(Chance = self.DebuffChance[self.Level], 
                                    StatusEffect = BattleStatusEff_StatMod_Armor(
                                        Duration = 3,
                                        StatMod_Armor = 0.3,
                                        StatusEffectID = "razor_slash_armor_debuff",
                                        SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            DebuffChancePerc = Battle_FormatDescVal(round(self.DebuffChance[DescLevel] * 100), Percentage = True)
            return tra(_("Slash the enemy with three vicious strikes (%s damage each) applying an armor reduction debuff of 70%% for 3 turns with a %s chance on each attack.")) % (StrikeDamage, DebuffChancePerc)