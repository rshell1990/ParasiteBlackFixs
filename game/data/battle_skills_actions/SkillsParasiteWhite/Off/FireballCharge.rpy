init python:
    @RegisterBattleSkill("ParasiteWhiteFireballCharge")
    class BattleSkill_ParasiteWhiteFireballCharge(BattleSkill):
        DisplayName = _("Fireball Charge")

        Icon = "images/battle_skill_icons/parawhite/FireballCharge.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 40

        DamageValue =  {1:1.45, 2:1.55,  3:1.65,  4:1.75,  5:1.75}
        BurnTurns =    {1:2,   2:2,    3:2,    4:2,    5:3}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SoundImpact_CustomList = soundLib["Battle_FireImpacts"],
                SoundSwing_CustomList = soundLib["Battle_FireStrikes"],
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Burn(
                            BaseValue = self.Owner_BattleChar.Damage,
                            Duration = self.BurnTurns[self.Level],
                            SourceName = self.DisplayName))],
                AnimID = "attack_fire")
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            BurnTurns = Battle_FormatDescVal(self.BurnTurns[DescLevel])
            return tra(_("Attacks the enemy, dealing %s damage and making them burn for %s turns.")) % (StrikeDamage, BurnTurns)