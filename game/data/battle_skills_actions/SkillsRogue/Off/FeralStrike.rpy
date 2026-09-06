init python:
    @RegisterBattleSkill("RogueFeralStrike")
    class BattleSkill_RogueFeralStrike(BattleSkill):
        DisplayName = _("Feral Strike")
        Icon = "images/battle_skill_icons/rogue/FeralStrike.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 40

        DamageValue = {1:1.3, 2:1.4, 3:1.5, 4:1.6}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.HEAL_SELF}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                ExtraCritChancePercentage = 30,
                DamageRecoversAttackerHealth = 0.3)
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Channel your inner feral nature to deliver a swift and brutal attack that deals %s damage and heals you for 30%% of the damage dealt.\nThis attack has an additional 30%% critical chance.")) % DamageValue