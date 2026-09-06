init python:
    @RegisterBattleSkill("RogueWolfHowl")
    class BattleSkill_RogueWolfHowl(BattleSkill):
        DisplayName = _("Howl")
        Icon = "images/battle_skill_icons/rogue_wolf/Howl.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 40

        ArmorAccuracyBuff = {
            1:1.4,
            2:1.5,
            3:1.6}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Armor(Duration = 2, StatMod_Armor = self.ArmorAccuracyBuff[self.Level], StatusEffectID = "wolf_howl_armorbuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(Duration = 2, StatMod_AttackRating = self.ArmorAccuracyBuff[self.Level], StatusEffectID = "wolf_howl_accbuff", SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            ArmorAccBuffPerc = Battle_FormatDescVal(round((self.ArmorAccuracyBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Let the pack know you're in this together. Increases the armor and accuracy of all allies by %s for 2 turns.")) % ArmorAccBuffPerc