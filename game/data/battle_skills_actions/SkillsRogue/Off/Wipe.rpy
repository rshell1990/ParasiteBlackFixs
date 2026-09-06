init python:
    @RegisterBattleSkill("RogueWipe")
    class BattleSkill_RogueWipe(BattleSkill):
        DisplayName = _("Wipe")
        Icon = "images/battle_skill_icons/rogue/Wipe.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 60

        DamageValue = {1:1.75, 2:1.85, 3:1.95, 4:2.05}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.IGNORES_ENEMY_DODGE}
        
        ShowHitChance = False

        def Execute(self, Target):
            DamageMod =  self.DamageValue[self.Level] + self.Owner_BattleChar.CharRef["Agility"] / 100
            Battle_ScheduledAttack(
                    SourceSkillObj = self,
                    AttackTarget = Target,
                    DamageMod = DamageMod,
                    GuaranteedHit = True)
            Battle_ApplyStatusEffect(TargetChar = self.Owner_BattleChar,
                                    StatusEffect = BattleStatusEff_StatMod_Accuracy(Duration = 2, StatMod_AttackRating = 0.6, StatusEffectID = "roguewipe_accdebuff", SourceName = self.DisplayName))
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageMod =  self.DamageValue[DescLevel] + self.Owner_BattleChar.CharRef["Agility"] / 100
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, DamageMod))
            else:
                DamageMod =  self.DamageValue[DescLevel] + worldChars[self.Owner_PBCharID]["Agility"] / 100
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, DamageMod))
            BaseDmgAsPerc = Battle_FormatDescVal(round(self.DamageValue[DescLevel] * 100))
            DamageMultAsPerc = Battle_FormatDescVal(round(DamageMod * 100), Percentage = True)
            return tra(_("Attacks the enemy with a super sonic blow, dealing %s damage at the cost of reducing your own accuracy by 60%% for 2 turns. The blow cannot be dodged and deals huge damage proportional to your agility. %s (%s + Agility)")) % (StrikeDamage, DamageMultAsPerc, BaseDmgAsPerc)
