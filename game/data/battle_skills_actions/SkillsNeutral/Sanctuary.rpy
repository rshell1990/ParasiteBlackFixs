init python:
    @RegisterBattleSkill("NeutralSanctuary")
    class BattleSkill_NeutralSanctuary(BattleSkill):    
        DisplayName = _("Sanctuary")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ALLIES
        Cost_Energy = 40

        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_Immunity(Duration = 3, SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Removes all harmful effects from all allies and grants them negative status effect immunity for 3 turns."))