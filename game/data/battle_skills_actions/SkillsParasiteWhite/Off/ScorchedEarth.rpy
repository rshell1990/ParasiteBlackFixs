init python:
    @RegisterBattleSkill("ParasiteWhiteScorchedEarth")
    class BattleSkill_ParasiteWhiteScorchedEarth(BattleSkill):
        DisplayName = _("Scorched Earth")

        Icon = "images/battle_skill_icons/parawhite/ScorchedEarth.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 60

        DamageValue =  {1:1.4, 2:1.5,  3:1.6,  4:1.7,  5:1.7}
        BurnTurns =    {1:2,   2:2,    3:2,    4:2,    5:3}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SoundImpact_CustomList = soundLib["Battle_FireImpacts"],
                SoundSwing_CustomList =  soundLib["Battle_FireStrikes"],
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
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
            return tra(_("Shoot a flame at all the enemies, dealing %s damage and making them burn for %s turns.")) % (StrikeDamage, BurnTurns)