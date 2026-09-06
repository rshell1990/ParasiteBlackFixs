init python:
    @RegisterBattleSkill("NeutralLeadership")
    class BattleSkill_NeutralLeadership(BattleSkill):    
        DisplayName = _("Leadership")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ALLIES
        Cost_Energy = 40

        AIBaseWeight = 4.0

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_DamageOut(DamageDealt_Mod = 1.4, Duration = 2, SourceName = self.DisplayName, StatusEffectID = "neutral_leadership_dmgbuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Increases damage dealt by all allies by 40% for 2 turns."))