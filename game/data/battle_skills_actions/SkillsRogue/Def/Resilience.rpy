init python:
    @RegisterBattleSkill("RogueResilience")
    class BattleSkill_RogueResilience(BattleSkill):
        DisplayName = _("Resilience")
        Icon = "images/battle_skill_icons/rogue/Resilience.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 30

        DamageResistanceBoost ={1:0.6, 2:0.5, 3:0.4, 4:0.4}
        DodgeChanceBoost =     {1:1.4, 2:1.5, 3:1.6, 4:1.6}
        HealPerc =             {1:0.2, 2:0.2, 3:0.2, 4:0.3}

        AITags = {AI_TAGS.HEAL_SELF, AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE}

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_RestoreHealth(RestoreValue = self.HealPerc[self.Level], RatioFromMax = True),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(DamageRecieved_Mod = self.DamageResistanceBoost[self.Level], Duration = 2, SourceName = self.DisplayName, StatusEffectID = "rogueresilience_damageres")),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 2, StatMod_DodgeRating = self.DodgeChanceBoost[self.Level], StatusEffectID = "rogueresilience_dodgebuff", SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            DamageResPerc = Battle_FormatDescVal(round((1.0 - self.DamageResistanceBoost[DescLevel]) * 100), Percentage = True)
            DodgePerc = Battle_FormatDescVal(round((self.DodgeChanceBoost[DescLevel] - 1.0) * 100), Percentage = True)
            PercRecovered = Battle_FormatDescVal(round((self.HealPerc[DescLevel]) * 100), Percentage = True)
            return tra(_("Draw upon your wisdom to strengthen your body, gaining %s damage resistance and %s dodge chance for 2 turns and recovering %s of your maximum hp.")) % (DamageResPerc, DodgePerc, PercRecovered)