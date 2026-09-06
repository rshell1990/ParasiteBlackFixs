init python:
    @RegisterBattleSkill("RogueWolfRecklessBeast")
    class BattleSkill_RogueWolfRecklessBeast(BattleSkill):
        DisplayName = _("Reckless Beast")
        Icon = "images/battle_skill_icons/rogue_wolf/RecklessBeast.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 70
        Cost_PercHealthCurr = 0.5

        DamageValue = {
            1:1.1,
            2:1.2,
            3:1.3,
            4:1.4}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.FAVOURED_HIGH_OWN_HP_RATIO, AI_TAGS.REMOVE_BUFFS_ON_TARGET}

        def Execute(self, Target):
            FirstTargetList = Battle_GetAllEnemiesOfChar(self.Owner_BattleChar)
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = FirstTargetList,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_RemoveBuffsOnTarget()])
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_RemoveBuffsOnTarget()])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("At the cost of half your current HP, attack the entire enemy party dealing %s damage and removing all their beneficial effects. The selected enemy is attacked a second time.")) % DamageValue