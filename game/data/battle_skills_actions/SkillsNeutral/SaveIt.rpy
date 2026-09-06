init python:
    @RegisterBattleSkill("NeutralSaveIt")
    class BattleSkill_NeutralSaveIt(BattleSkill):    
        DisplayName = _("Save It")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.SELF
        Cost_Energy = 30
        
        AITags = {AI_TAGS.HEAL_SELF}

        AIBaseWeight = 1.1

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_RestoreHealth(RestoreValue = 0.3, RatioFromMax = True),
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_Invincibility(Duration = 1, SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Recovers your hp by 30% and places invincibility on yourself for 1 turn."))