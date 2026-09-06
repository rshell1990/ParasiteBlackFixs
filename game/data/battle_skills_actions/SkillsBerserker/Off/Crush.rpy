init python:
    @RegisterBattleSkill("BerserkerCrush")
    class BattleSkill_BerserkerCrush(BattleSkill):
        DisplayName = _("Crush")

        Icon = "images/battle_skill_icons/berserker/Crush.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 40

        DamageValue = {1:1.2, 2:1.3, 3:1.4, 4:1.5}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.TAUNT_TARGET}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                DamageBurn_Mana = 0.3,
                DamageBurn_Energy = 0.3,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(StatusEffect = 
                        BattleStatusEff_Taunt(Duration = 1, TauntedBy = self.Owner_BattleChar))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Attacks the enemy dealing %s in an attempt to crush them, decreasing their energy or mana by 30%% of the damage dealt and provoking them for 1 turn.")) % StrikeDamage