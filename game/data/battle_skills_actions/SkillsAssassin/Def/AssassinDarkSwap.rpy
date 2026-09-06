init python:
    @RegisterBattleSkill("AssassinDarkSwap")
    class BattleSkill_AssassinDarkSwap(BattleSkill):    
        DisplayName = _("Dark Swap")

        Icon = "images/battle_skill_icons/assassin/DarkSwap.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_PercHealthMax = 0.3

        AITags = {AI_TAGS.FAVOURED_LOW_OWN_ENERGY_RATIO}

        EnergyRestored = {
            1:0.3,
            2:0.35,
            3:0.4,
        }

        ShowHitChance = False

        def Execute(self, Target):
            EnergyToRestore = max(round(self.Owner_BattleChar.Energy * self.EnergyRestored[self.Level]), 1)
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget =     self.ValidTargets,
                Effects_OnSelf = [
                    BattleEffect_RestoreEnergy(RestoreValue = EnergyToRestore),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Invincibility(Duration = 1, SourceName = self.DisplayName)
                    ),
                ],
            )
            return

        def GetDesc(self, DescLevel = 1):
            EnergyRestoredPercFormatted = Battle_FormatDescVal(round((self.EnergyRestored[DescLevel]) * 100), Percentage = True)
            return tra(_("Sacrifice 30%% of your MAX HP to convert them into restoring %s of your current energy. You also gain invincibility for 1 round.")) % EnergyRestoredPercFormatted