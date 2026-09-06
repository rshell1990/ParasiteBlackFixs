init python:
    @RegisterBattleSkill("BansheeASongOfDarkBargains")
    class BattleSkill_BansheeASongOfDarkBargains(BattleSkill):
        DisplayName = _("A song of dark bargains")

        Icon = "images/battle_skill_icons/banshee/ASongOfDarkBargains.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 70

        DamageDealtBoostValue = {1:1.4, 2:1.5, 3:1.6, 4:1.7}

        AITags = {AI_TAGS.FAVOURED_HIGH_OWN_HP_RATIO}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageOut(
                            DamageDealt_Mod = self.DamageDealtBoostValue[self.Level],
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "banshee_bargains_song_dmgout_buff")),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(
                            DamageRecieved_Mod = 1.2,
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "banshee_bargains_song_dmgin_dbuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            DamageDealtPercentage = Battle_FormatDescVal(round((self.DamageDealtBoostValue[DescLevel] - 1) * 100), Percentage = True)
            return tra(_("Increases the damage all allies deal by %s in exchange for increasing the damage they take by 20%% for 2 turns each.")) % DamageDealtPercentage