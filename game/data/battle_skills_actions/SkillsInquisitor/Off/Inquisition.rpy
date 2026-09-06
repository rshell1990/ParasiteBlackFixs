init python:
    @RegisterBattleSkill("InquisitorInquisition")
    class BattleSkill_InquisitorInquisition(BattleSkill):    
        DisplayName = _("Inquisition")

        Icon = "images/battle_skill_icons/inquisitor/Inquisition.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 90
        Cost_PercHealthCurr = 0.9

        DamageValue = {1:1.7, 2:1.8, 3:1.9, 4:2.0, 5:2.2}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.EFFECT_SCALES_WITH_AMOUNT_OF_BUFFS_ON_TARGET}

        ShowHitChance = False

        def Execute(self, Target):
            AllTargets = Battle_GetAllEnemiesOfChar(self.Owner_BattleChar)

            for Target in AllTargets:
                BurnsToAdd = 0
                for StatusEffect in reversed(Target.StatusEffects):
                    if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                        Battle_RemoveStatusEffect(Target, StatusEffect.StatusEffectID)
                        BurnsToAdd +=1 

                for BurnToAdd in range(BurnsToAdd):
                    Battle_ApplyStatusEffect(
                        TargetChar = Target, 
                        StatusEffect = BattleStatusEff_Burn(
                            self.Owner_BattleChar.Damage, 
                            Duration = 1,
                            SourceName = self.DisplayName))

            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Bring down the wrath of the gods and sacrifice 90%% of your health to swap the beneficial effects of all enemies for a burning effect that lasts 1 turn while also dealing %s damage to each enemy.")) % StrikeDamage