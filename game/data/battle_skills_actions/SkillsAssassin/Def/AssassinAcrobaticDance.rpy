init python:
    @RegisterBattleSkill("AssassinAcrobaticDance")
    class BattleSkill_AssassinAcrobaticDance(BattleSkill):
        DisplayName = _("Acrobatic Dance")

        Icon = "images/battle_skill_icons/assassin/AcrobaticDance.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 60

        AITags = {AI_TAGS.TAUNT_TARGET}

        DodgeBuff = {
            1:2.0,
            2:2.2,
            3:2.2,
            4:2.2,
        }

        ShowHitChance = False

        def Execute(self, Target):
            SelfEffectsList = [
                BattleEffect_ApplyStatusOnAlly(
                    StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 3, StatMod_DodgeRating = self.DodgeBuff[self.Level], StatusEffectID = "assassin_acrodance_dodgebuff", SourceName = self.DisplayName)),
                BattleEffect_ApplyStatusOnAlly(
                    StatusEffect = BattleStatusEff_Counter(Duration = 2, SourceName = self.DisplayName))]

            if self.Level >= 2:
                SelfEffectsList.append(
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_RegenHealth(
                            Duration = 1, 
                            RestoreVal = 0.1, 
                            RatioFromMax = True, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "assassin_acrodance_regenbuff")))
            if self.Level >= 3:
                SelfEffectsList.append(
                    BattleEffect_RemoveDebuffsOnTarget(Amount = 2))

            if self.Level >= 4:
                SelfEffectsList.append(
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            Duration = 2,
                            StatMod_Armor = 1.2,
                            StatusEffectID = "assassin_acrodance_armorbuff",
                            SourceName = self.DisplayName)
                    )
                )

            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = Target,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Taunt(
                            Duration = 1, 
                            SourceName = self.DisplayName, 
                            TauntedBy = self.Owner_BattleChar))],
                Effects_OnSelf = SelfEffectsList
            )
            return

        def GetDesc(self, DescLevel = 1):
            DodgeBuffPercFormatted = Battle_FormatDescVal(round((self.DodgeBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Taunt the enemy and draw their attention for 1 turn. Gains %s dodge buff for 3 turns, and counterstrike buff for 2 turns.\nAt level 2, will also recover 10%% of your current HP for 1 round and remove 2 debuffs.\nAt level 3, gives an additional 20%% armor boost for 2 rounds.")) % DodgeBuffPercFormatted
