init python:
    @RegisterBattleSkill("AssassinAThousandDaggers")
    class BattleSkill_AssassinAThousandDaggers(BattleSkill):
        DisplayName = _("A Thousand Daggers")

        Icon = "images/battle_skill_icons/assassin/AThousandDaggers.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 70

        DodgeBuff = {
            1:1.8,
            2:1.9,
            3:1.9,
        }
        CounterTurns = {
            1:1,
            2:1,
            3:2,
        }

        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET, AI_TAGS.ONLY_IF_ALLIES_EXIST}

        def Execute(self, Target):
            AlliesToGiveCounterBuff = []
            DodgeList = []
            AllAllies = Battle_GetAllAlliesOfChar(self.Owner_BattleChar)
            for Ally in AllAllies:
                if Battle_HasAnyDebuff(Ally):
                    DodgeList.append(Ally)
                else:
                    AlliesToGiveCounterBuff.append(Ally)

            # case 1 there are allies with debuffs, remove, grant dodge, add counter to those in need
            if len(DodgeList) > 0:
                Battle_ScheduledCast(
                    SourceSkillObj = self, 
                    CastTarget = DodgeList,
                    Effects_OnTarget = [
                        BattleEffect_RemoveDebuffsOnTarget(Amount = 1),
                        BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 2, StatMod_DodgeRating = self.DodgeBuff[self.Level], StatusEffectID = "assassin_thousanddaggers_dodgebuff", SourceName = self.DisplayName))
                    ]
                )
                for AllyToGiveCounter in AlliesToGiveCounterBuff:
                    Battle_ApplyStatusEffect(AllyToGiveCounter, StatusEffect = BattleStatusEff_Counter(Duration = self.CounterTurns[self.Level], SourceName = self.DisplayName))
            # case 2 there's just the dudes without debuffs, so only grant counter to all
            elif len(AlliesToGiveCounterBuff) > 0:
                Battle_ScheduledCast(
                    SourceSkillObj = self, 
                    CastTarget = AlliesToGiveCounterBuff,
                    Effects_OnTarget = [
                        BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_Counter(Duration = self.CounterTurns[self.Level], SourceName = self.DisplayName))
                    ]
                )

            return

        def GetDesc(self, DescLevel = 1):
            DodgeBuffPerc = Battle_FormatDescVal(round((self.DodgeBuff[DescLevel] - 1.0) * 100), Percentage = True)
            CounterTurns = Battle_FormatDescVal(self.CounterTurns[DescLevel])
            return tra(_("Removes 1 harmful effect from all allies and grant to all of them %s of  dodge buff for 2 turns.\nAllies who have no harmful effects BEFORE this ability receive countertrike buff with a duration of %s.")) % (DodgeBuffPerc, CounterTurns)