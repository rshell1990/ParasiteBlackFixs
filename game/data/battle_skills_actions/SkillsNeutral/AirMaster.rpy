init python:
    @RegisterBattleSkill("NeutralAirMaster")
    class BattleSkill_NeutralAirMaster(BattleSkill):
        DisplayName = _("Air Master")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ALLIES
        Cost_Energy = 35

        AIBaseWeight = 2.0

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 2, StatMod_DodgeRating = 1.6, StatusEffectID = "neut_airmaster_dodgebuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(Duration = 2, StatMod_AttackRating = 1.6, StatusEffectID = "neut_airmaster_accbuff", SourceName = self.DisplayName)),
                ]
            )
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Increases the dodge and accuracy of all allies by 60% for 2 turns."))