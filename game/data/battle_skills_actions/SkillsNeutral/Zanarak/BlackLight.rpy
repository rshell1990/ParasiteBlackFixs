init python:
    @RegisterBattleSkill("ZanarakBlackLight")
    class BattleSkill_ZanarakBlackLight(BattleSkill):
        DisplayName = _("Black Light")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ALLIES
        Cost_Energy = 100

        AITags = {AI_TAGS.HEAL_SELF, AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE}


        def Execute(self, Target):
            Battle_RestoreHealth(self.Owner_BattleChar, 0.15, RatioFromMax = True)
            PartyTargetList = Battle_GetAliveCharsOnSide(self.Owner_BattleChar.BattleSide)
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = PartyTargetList,
                Effects_OnTarget = [
                    BattleEffect_RestoreHealth(RestoreValue = 0.2, RatioFromMax = True),
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_DamageOut(DamageDealt_Mod = 1.2, Duration = 2, SourceName = self.DisplayName, StatusEffectID = "zanarak_unstoppablerage_dmgbuff")),
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_StatMod_Armor(Duration = 2, StatMod_Armor = 1.2, StatusEffectID = "zanarak_unstoppablerage_armorbuff"))]
            )
            return

        def GetDesc(self, DescLevel = 1):
            return "Heals self by 35%, heals the rest of the party by 20%. Also provides both a damage boost of 20% and an Armor boost of 20% to Zanarak and the party for 2 turns."