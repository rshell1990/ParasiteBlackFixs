init python:
    @RegisterBattleSkill("ScoutPreparationFromTheSkilled")
    class BattleSkill_ScoutPreparationFromTheSkilled(BattleSkill):
        DisplayName = _("Preparation From The Skilled")
        Icon = "images/battle_skill_icons/scout/PreparationFromTheSkilled.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 60

        CritChanceAndDamageDealtBuff = {1:1.3, 2:1.4, 3:1.5, 4:1.6}
        AutoSelectNextInPartyOnExecute = False

        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET}

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_CritChance(
                            Duration = 2, 
                            StatMod_CritChance = self.CritChanceAndDamageDealtBuff[self.Level], 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "scout_pfts_critbuff")),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageOut(
                            DamageDealt_Mod = self.CritChanceAndDamageDealtBuff[self.Level], 
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "scout_pfts_dmgoutbuff"))])
            Battle_GrantExtraTurn(self.Owner_BattleChar)
            return

        def GetDesc(self, DescLevel = 1):
            DmgCritChanceBuffPerc = Battle_FormatDescVal(round((self.CritChanceAndDamageDealtBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Removes all harmful effects on yourself and increases your critical rate and damage dealt by %s for 2 turns. You gain another turn immediately after using this ability.")) % DmgCritChanceBuffPerc