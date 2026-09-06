init python:
    @RegisterBattleSkill("SlimeSlimeRecharge")
    class BattleSkill_SlimeSlimeRecharge(BattleSkill):
        DisplayName = _("Slime Recharge")
        
        Icon = "images/battle_skill_icons/slime/SlimeRecharge.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALLY_NOT_SELF

        Cost_Energy = 90

        RechargeEnergyBy = {1:0.2, 2:0.25, 3:0.3}
        AutoSelectNextInPartyOnExecute = False
        
        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET}

        def Execute(self, Target):
            Battle_ScheduledCast(
                
                SourceSkillObj = self,
                CastTarget = Target,
                Effects_OnTarget = [
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_RestoreEnergyOrMana(
                        RestoreValue = self.RechargeEnergyBy[self.Level], 
                        RatioFromMax = True)])

            Battle_GrantExtraTurn(Target, OnlyIfHasActed = True)
            return

        def GetDesc(self, DescLevel = 1):
            EnergyOrManaRegenPerc = Battle_FormatDescVal(round(self.RechargeEnergyBy[DescLevel] * 100), Percentage = True)
            return tra(_("Removes all harmful effects from an ally, recharges their energy or mana by %s and grants them another turn if they have already acted.")) % EnergyOrManaRegenPerc