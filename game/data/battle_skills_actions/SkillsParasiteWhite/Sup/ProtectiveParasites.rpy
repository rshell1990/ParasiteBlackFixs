init python:
    @RegisterBattleSkill("ParasiteWhiteProtectiveParasites")
    class BattleSkill_ParasiteWhiteProtectiveParasites(BattleSkill):
        DisplayName = _("Protective Parasites")

        Icon = "images/battle_skill_icons/parawhite/ProtectiveParasites.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 170

        EnemyArmorDebuff = {1:0.5, 2:0.4, 3:0.3}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        AIBaseWeight = 1.1

        def Execute(self, Target):
            Battle_ScheduledAttack(
                
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = 0.4,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            Duration = 2, 
                            StatMod_Armor = self.EnemyArmorDebuff[self.Level],
                            StatusEffectID = "parawhite_prot_armordebuff", 
                            SourceName = self.DisplayName))])

            Battle_ScheduledCast(
                 
                SourceSkillObj = self, 
                CastTarget = BATTLE_TARGETS.ALL_ALLIES,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Invincibility(
                            Duration = 1, 
                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, 0.4), Parentheses = True)
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, 0.4), Parentheses = True)
            ArmorPercDebuff = Battle_FormatDescVal(round((1.0 - self.EnemyArmorDebuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Fires at all enemies to deal minor damage %s that decreases their armour by %s for 2 turns, then grants invincibility to all allies for 2 turns.")) % (StrikeDamage, ArmorPercDebuff)