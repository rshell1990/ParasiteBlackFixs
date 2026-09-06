init python:
    @RegisterBattleSkill("NeutralMaximumSafety")
    class BattleSkill_NeutralMaximumSafety(BattleSkill):    
        DisplayName = _("Maximum Safety")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.SELF
        Cost_Energy = 80

        AIBaseWeight = 3.0

        AITags = {AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_StatMod_Armor(Duration = 3, StatMod_Armor = 1.7, StatusEffectID = "neutral_safety_armorbuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_Immunity(Duration = 3, SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Grants yourself immunity and a 70% increase in armour for 3 turns."))