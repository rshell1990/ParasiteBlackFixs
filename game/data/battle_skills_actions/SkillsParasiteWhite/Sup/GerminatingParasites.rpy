init python:
    @RegisterBattleSkill("ParasiteWhiteGerminatingParasites")
    class BattleSkill_ParasiteWhiteGerminatingParasites(BattleSkill):
        DisplayName = _("Germinating Parasites")

        Icon = "images/battle_skill_icons/parawhite/GerminatingParasites.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES_NOT_SELF

        Cost_Energy = 80
        Cost_PercHealthCurr = 0.2

        AlliedHpRecoveryPerc = {1:0.2, 2:0.25, 3:0.25, 4:0.3, 5:0.3}
        AlliedArmorBuff = {1:1.4, 2:1.4, 3:1.5, 4:1.5, 5:1.6}

        HealTarget = {AI_TAGS.HEAL_TARGET, AI_TAGS.FAVOURED_HIGH_OWN_HP_RATIO}

        def Execute(self, Target):
            Battle_ScheduledCast(
                 
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [BattleEffect_RestoreHealth(RestoreValue = 0.2, RatioFromMax = True),
                                    BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_StatMod_Armor(
                                            Duration = 2, 
                                            StatMod_Armor = self.AlliedArmorBuff[self.Level], 
                                            StatusEffectID = "parawhite_germpara_armorbuff", 
                                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            HealPerc = Battle_FormatDescVal(round(self.AlliedHpRecoveryPerc[DescLevel] * 100), Percentage = True)
            ArmorBuff = Battle_FormatDescVal(round((self.AlliedArmorBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Sacrifice 20%% of your current hp and recover the hp of all other allies by %s, then increase the armor of all allies by %s for 2 turns.")) % (HealPerc, ArmorBuff)
