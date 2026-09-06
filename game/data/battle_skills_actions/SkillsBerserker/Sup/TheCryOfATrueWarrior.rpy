init python:
    @RegisterBattleSkill("BerserkerTheCryOfATrueWarrior")
    class BattleSkill_BerserkerTheCryOfATrueWarrior(BattleSkill):
        DisplayName = _("Cry of A True Warrior")
        
        Icon = "images/battle_skill_icons/berserker/TheCryOfATrueWarrior.webp"
        Level_Max = 1
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 90

        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET}

        AIBaseWeight = 1.25

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Immunity(
                            Duration = 2,
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Willpower(
                            Duration = 2,
                            SourceName = self.DisplayName)),
                        ])
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Removes all harmful effects from all allies, grants immunity and willpower to all allies for 2 turns.\nAllies under willpower effect cannot die."))
