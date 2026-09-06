init python:
    @RegisterBattleSkill("RogueWolfDanceOfTheWolves")
    class BattleSkill_RogueWolfDanceOfTheWolves(BattleSkill):
        DisplayName = _("Dance Of The Wolves")
        Icon = "images/battle_skill_icons/rogue_wolf/DanceOfTheWolves.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 60
        AutoSelectNextInPartyOnExecute = False

        AccDodgeBuff = {
            1:1.8,
            2:1.9,
            3:2.0}

        AIBaseWeight = 1.1

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(Duration = 1, StatMod_AttackRating = self.AccDodgeBuff[self.Level], StatusEffectID = "wolf_dance_accbuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 1, StatMod_DodgeRating = self.AccDodgeBuff[self.Level], StatusEffectID = "wolf_dance_dogebuff", SourceName = self.DisplayName))])
            Battle_GrantExtraTurn(self.Owner_BattleChar)
            return

        def GetDesc(self, DescLevel = 1):
            AccDodgeBuffPerc = Battle_FormatDescVal(round((self.AccDodgeBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Increases your accuracy and dodge by %s for 1 turn and gains another turn immediately.")) % AccDodgeBuffPerc