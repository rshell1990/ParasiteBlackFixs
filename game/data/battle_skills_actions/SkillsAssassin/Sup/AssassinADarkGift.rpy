init python:
    @RegisterBattleSkill("AssassinADarkGift")
    class BattleSkill_AssassinADarkGift(BattleSkill):
        DisplayName = _("A Dark Gift")

        Icon = "images/battle_skill_icons/assassin/ADarkGift.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 30

        AITags = {AI_TAGS.GAIN_TURN, AI_TAGS.ONLY_IF_ALLIES_EXIST}

        CritBuff = {
            1:1.2,
            2:1.3,
            3:1.4,
        }

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_CritChance(
                            Duration = 2, 
                            StatMod_CritChance = self.CritBuff[self.Level],
                            SourceName = self.DisplayName, 
                            StatusEffectID = "assassin_darkgift_critbuff"))],
                Effects_OnSelf = [
                    BattleEffect_GrantExtraTurn()
                ],
            )
            return

        def GetDesc(self, DescLevel = 1):
            CritBuffPerc = Battle_FormatDescVal(round((self.CritBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Increases the critical rate of all allies by %s for 2 turns and you get another turn immediately.")) % CritBuffPerc