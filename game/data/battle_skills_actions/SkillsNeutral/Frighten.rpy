init python:
    @RegisterBattleSkill("NeutralFrighten")
    class BattleSkill_NeutralFrighten(BattleSkill):
        DisplayName = _("Frighten")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 40

        AIBaseWeight = 1.1

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(StatusEffect = BattleStatusEff_DamageOut(DamageDealt_Mod = 0.7, Duration = 2, SourceName = self.DisplayName, StatusEffectID = "neutral_frighten_dmgoutdebuff")),
                    BattleEffect_ApplyStatusOnEnemy(StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 2, StatMod_DodgeRating = 0.7, StatusEffectID = "neutral_frighten_dodgedebuff", SourceName = self.DisplayName))])

            for AllyChar in Battle_GetAliveCharsOnSide(self.Owner_BattleChar.BattleSide):
                Battle_ApplyStatusEffect(AllyChar, StatusEffect = BattleStatusEff_DamageOut(DamageDealt_Mod = 1.3, Duration = 2, SourceName = self.DisplayName, StatusEffectID = "neutral_frighten_damagebuff"))
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Shouts to frighten all enemies, decreasing the damage they deal and their dodge by 30% for 2 turns and increasing the damage dealt by allies by 30% for 2 turns."))