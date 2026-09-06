init python:
    @RegisterBattleSkill("ScoutPerfectStrike")
    class BattleSkill_ScoutPerfectStrike(BattleSkill):
        DisplayName = _("Perfect Strike")
        
        Icon = "images/battle_skill_icons/scout/PerfectStrike.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 60

        DamageValue = {1:1.3, 2:1.4, 3:1.55, 4:1.7}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_LAST_HIT}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                IgnoreArmor = True,
                Effects_OnKill_User = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Invincibility(Duration = 1, SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Attacks the target enemy with a blow that deals %s damage and ignores the target's armor. Makes you invincible for one turn if the enemy dies.")) % StrikeDamage