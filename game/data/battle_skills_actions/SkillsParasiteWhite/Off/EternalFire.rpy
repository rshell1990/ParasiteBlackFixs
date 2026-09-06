init python:
    @RegisterBattleSkill("ParasiteWhiteEternalFire")
    class BattleSkill_ParasiteWhiteEternalFire(BattleSkill):
        DisplayName = _("Eternal Fire")

        Icon = "images/battle_skill_icons/parawhite/EternalFire.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 130

        DamageValue = {1:1.6, 2:1.7, 3:1.8, 4:1.9}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.STRONGER_ON_BURNING_ENEMY}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SoundImpact_CustomList = soundLib["Battle_FireImpacts"],
                SoundSwing_CustomList = soundLib["Battle_FireStrikes"],
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [BattleEffect_ExplodeTarget()],
                AnimID = "attack_fire")
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]), Parentheses = True)
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]), Parentheses = True)
            return tra(_("Unleashes a large amount of energy to attack all enemies with an attempt to explode them, causing great damage %s and activating all their burn effects at once.")) % StrikeDamage