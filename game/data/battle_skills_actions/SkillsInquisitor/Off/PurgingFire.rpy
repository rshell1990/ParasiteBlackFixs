init python:
    @RegisterBattleSkill("InquisitorPurgingFire")
    class BattleSkill_InquisitorPurgingFire(BattleSkill):
        DisplayName = _("Purging fire")

        Icon = "images/battle_skill_icons/inquisitor/PurgingFire.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 60

        DamageValue = {1:1.2, 2:1.3, 3:1.4, 4:1.5}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.STRONGER_ON_BURNING_ENEMY}

        def Execute(self, Target):
            Multiplier = 1.0

            if Battle_HasStatusEffect(Target, "burn"):
                Multiplier = 2.0

            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level] * Multiplier,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Burn(
                            BaseValue = self.Owner_BattleChar.Damage,
                            Duration = 3, 
                            SourceName = self.DisplayName))
                ])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Strike an almighty blow at a single enemy dealing %s damage and causing a burning effect for 3 turns. If the enemy already has a burning effect before the strike lands, the strike damage is doubled.")) % StrikeDamage