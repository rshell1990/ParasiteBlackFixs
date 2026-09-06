init python:
    @RegisterBattleSkill("BansheeWingsOfDarkness")
    class BattleSkill_BansheeWingsOfDarkness(BattleSkill):
        DisplayName = _("Wings of Darkness")

        Icon = "images/battle_skill_icons/banshee/WingsOfDarkness.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 80
        Cost_PercHealthCurr = 0.3

        DamageValue = {1:2.2, 2:2.3, 3:2.4, 4:2.5}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_LAST_HIT}
        
        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                GuaranteedHit = True,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnKill_User = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Willpower(Duration = 1, SourceName = self.DisplayName))])
            Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar,
                                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                                            Duration = 2, 
                                            StatMod_AttackRating = 0.7, 
                                            StatusEffectID = "banshee_wings_acc_debuff", 
                                            SourceName = self.DisplayName))
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Sacrifice 30%% of your current health and attack the enemy with a devastating blow, dealing %s damage. The blow cannot be dodged.\nAfter the attack, your accuracy will be reduced by 30%% for 2 turns.\nIf the enemy is killed by this attack, you recieve a Willpower buff for 1 turn. Units under the effect of Willpower buff cannot die.")) % StrikeDamage