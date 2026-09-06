init python:
    @RegisterBattleSkill("ScoutFastAndPreciseAttack")
    class BattleSkill_ScoutFastAndPreciseAttack(BattleSkill):
        DisplayName = _("Fast and Precise Attack")
        
        Icon = "images/battle_skill_icons/scout/FastAndPreciseAttack.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 40

        DamageValue =          {1:1.3, 2:1.45, 3:1.45, 4:1.6,  5:1.6}
        ArmorReductionChance = {1:0.5, 2:0.5,  3:0.7,  4:0.7,  5:0.9}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = self.ArmorReductionChance[self.Level],
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            Duration = 2, 
                            StatMod_Armor = 0.3,
                            StatusEffectID = "scout_fapa_armordebuff", 
                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            ArmorRedChancePerc = Battle_FormatDescVal(round(self.ArmorReductionChance[DescLevel] * 100), Percentage = True)
            return tra(_("Aim for the enemy's guard and strike them for %s damage, reducing their armor by 70%% for 2 turns with %s chance.")) % (StrikeDamage, ArmorRedChancePerc)