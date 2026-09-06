init python:
    @RegisterBattleSkill("NeutralGreatTaunt")
    class BattleSkill_NeutralGreatTaunt(BattleSkill):
        DisplayName = _("Great Taunt")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 35

        AIBaseWeight = 2.5

        AITags = {AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE, AI_TAGS.TAUNT_TARGET}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnSelf = [
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_DamageIn(DamageRecieved_Mod = 0.3, Duration = 2, SourceName = self.DisplayName, StatusEffectID = "neutral_greattaunt_dmgresbuff"))],
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Taunt(Duration = 2, SourceName = self.DisplayName, TauntedBy = self.Owner_BattleChar))])
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Shouts to provoke all enemies with a 70% chance for 2 turn and increases your damage resistance by 70% for 2 turns."))