init python:
    @RegisterBattleSkill("AssassinRecover")
    class BattleSkill_AssassinRecover(BattleSkill):    
        DisplayName = _("Recover")

        Icon = "images/battle_skill_icons/assassin/Recover.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        # (no cost)

        AITags = {AI_TAGS.HEAL_SELF, AI_TAGS.FAVOURED_LOW_OWN_ENERGY_RATIO}

        HealthRestoredRatioFromCurrent = {
            1:0.3,
            2:0.4,
            3:0.4,
        }

        EnergyRestoredRatioFromCurrent = {
            1:0.2,
            2:0.2,
            3:0.3,
        }

        ShowHitChance = False

        def Execute(self, Target):
            HealthToRestore = max(round(self.HealthRestoredRatioFromCurrent[self.Level] * self.Owner_BattleChar.Health), 1)
            EnergyToRestore = max(round(self.EnergyRestoredRatioFromCurrent[self.Level] * self.Owner_BattleChar.Energy), 1)

            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget =     self.ValidTargets,
                Effects_OnSelf = [
                    BattleEffect_RestoreHealth(HealthToRestore),
                    BattleEffect_RestoreEnergy(EnergyToRestore),
                ],
            )
            return

        def GetDesc(self, DescLevel = 1):
            HealthRestoredPercFormatted = Battle_FormatDescVal(round((self.HealthRestoredRatioFromCurrent[DescLevel]) * 100), Percentage = True)

            EnergyRestoredPercFormatted = Battle_FormatDescVal(round((self.EnergyRestoredRatioFromCurrent[DescLevel]) * 100), Percentage = True)
            # battle mode
            if self.Owner_BattleChar is not None:
                HealthRestoredValue = Battle_FormatDescVal(max(round(self.HealthRestoredRatioFromCurrent[DescLevel] * self.Owner_BattleChar.Health), 1), Parentheses = True)

                EnergyRestoredValue = Battle_FormatDescVal(max(round(self.EnergyRestoredRatioFromCurrent[DescLevel] * self.Owner_BattleChar.Energy), 1), Parentheses = True)
            # story mode
            else:
                HealthRestoredValue = Battle_FormatDescVal(max(round(self.HealthRestoredRatioFromCurrent[DescLevel] * worldChars[self.Owner_PBCharID]["Health"]), 1), Parentheses = True)

                EnergyRestoredValue = Battle_FormatDescVal(max(round(self.EnergyRestoredRatioFromCurrent[DescLevel] * worldChars[self.Owner_PBCharID]["Energy"]), 1), Parentheses = True)
            
            return tra(_("Take a moment to catch your breath. Restore your hit points by %s of your CURRENT HP %s and energy by %s of your CURRENT ENERGY %s. Increases your armor by 80%% for 2 turns.")) % (HealthRestoredPercFormatted, HealthRestoredValue , EnergyRestoredPercFormatted, EnergyRestoredValue)