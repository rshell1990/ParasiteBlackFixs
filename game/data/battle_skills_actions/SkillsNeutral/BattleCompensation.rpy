init python:
    @RegisterBattleSkill("NeutralBattleCompensation")
    class BattleSkill_NeutralBattleCompensation(BattleSkill):
        DisplayName = _("Battle Compensation")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 40

        DamageValue = {1:0.2}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.EFFECT_SCALES_WITH_AMOUNT_OF_DEBUFFS_ON_TARGET}

        AIBaseWeight = 2.0

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                DamageMod_AdditivePerDebuffOnTarget = 0.8)
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Attacks all enemies with a minor damage of %s that increases significantly with the amount of harmful effects the enemy possesses. 20%% + 80x(Number of beneficial effects)%% damage.")) % DamageValue