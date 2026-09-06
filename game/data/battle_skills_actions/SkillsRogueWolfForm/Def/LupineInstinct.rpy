init python:
    @RegisterBattleSkill("RogueWolfLupineInstinct")
    class BattleSkill_RogueWolfLupineInstinct(BattleSkill):
        DisplayName = _("Lupine Instinct")
        Icon = "images/battle_skill_icons/rogue_wolf/LupineInstinct.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 40
        AutoSelectNextInPartyOnExecute = False

        AccCritBuff = {
            1:1.3,
            2:1.4,
            3:1.5}

        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(Duration = 2, StatMod_AttackRating = self.AccCritBuff[self.Level], StatusEffectID = "wolf_lupinst_accbuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_CritChance(Duration = 2, StatMod_CritChance = self.AccCritBuff[self.Level], StatusEffectID = "wolf_lupinst_critbuff", SourceName = self.DisplayName))])
            Battle_GrantExtraTurn(self.Owner_BattleChar)
            return

        def GetDesc(self, DescLevel = 1):
            AccCritBuffPerc = Battle_FormatDescVal(round((self.AccCritBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Removes all harmful effects and increases your accuracy and critical rate by %s and gets another turn immediately.")) % AccCritBuffPerc
