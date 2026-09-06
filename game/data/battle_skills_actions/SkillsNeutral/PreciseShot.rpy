init python:
    @RegisterBattleSkill("NeutralPreciseShot")
    class BattleSkill_NeutralPreciseShot(BattleSkill):    
        DisplayName = _("Precise Shot")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        Cost_Energy = 40

        DamageValue = {1:1.0}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.IGNORES_ENEMY_ARMOR}

        AIBaseWeight = 3.0

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                IgnoreArmor = True)
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Attacks the enemy dealing %s damage that ignores their armor.")) % DamageValue