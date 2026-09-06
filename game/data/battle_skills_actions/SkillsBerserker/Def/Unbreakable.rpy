init python:
    @RegisterBattleSkill("BerserkerUnbreakable")
    class BattleSkill_BerserkerUnbreakable(BattleSkill):
        DisplayName = _("Unbreakable")

        Icon = "images/battle_skill_icons/berserker/Unbreakable.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 30

        ArmorBoost =   {1:1.4, 2:1.5, 3:1.5,   4:1.6,  5:1.6}
        HealPercent =  {1:0.2, 2:0.2, 3:0.25,  4:0.25, 5:0.3}

        AITags = {AI_TAGS.HEAL_SELF}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            StatMod_Armor = self.ArmorBoost[self.Level],
                            StatusEffectID = "bers_unbreakable_armorbuff",
                            Duration = 2, 
                            SourceName = self.DisplayName)),
                    BattleEffect_RestoreHealth(RestoreValue = self.HealPercent[self.Level], RatioFromMax = True)])
            return

        def GetDesc(self, DescLevel = 1):
            HealPerc = Battle_FormatDescVal(round(self.HealPercent[DescLevel] * 100), Percentage = True)
            ArmorBoostPerc = Battle_FormatDescVal(round((self.ArmorBoost[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Recovers your hp by %s and increases your armor by %s for 2 turns.")) % (HealPerc, ArmorBoostPerc)

