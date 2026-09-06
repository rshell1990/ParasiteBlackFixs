init python:
    @RegisterBattleSkill("ZanarakUnstoppableRage")
    class BattleSkill_ZanarakUnstoppableRage(BattleSkill):
        DisplayName = _("Unstoppable Rage")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.SELF
        Cost_Energy = 80

        AITags = {AI_TAGS.INCREASE_SELF_DAMAGE, AI_TAGS.GAIN_TURN, AI_TAGS.HEAL_SELF}
        AIBaseWeight = 10.0


        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_Immunity(Duration = 1, SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_DamageOut(DamageDealt_Mod = 1.5, Duration = 3, SourceName = self.DisplayName, StatusEffectID = "zanarak_unstoppablerage_dmgoutbuff")),
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_StatMod_CritChance(Duration = 2, StatMod_CritChance = 1.2, StatusEffectID = "zanarak_unstoppablerage_critchancebuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_RegenHealth(Duration = 1, RestoreVal = 0.15, RatioFromMax = True, SourceName = self.DisplayName, StatusEffectID = "zanarak_unstoppablerage_regen"))
                ]
            )

            Battle_GrantExtraTurn(self.Owner_BattleChar)
            return

        def GetDesc(self, DescLevel = 1):
            return "Zanarak is granted immunity for 1 round. His DMG is boosted by 50% for 3 rounds and his critical rate is also boosted by 20% for 2 rounds - and he has a small heal effect of 15% for 1 rounds. Also gains another turn immediately."