init python:
    @RegisterBattleSkill("SlimeMalleableForm")
    class BattleSkill_SlimeMalleableForm(BattleSkill):
        DisplayName = _("Malleable Form")

        Icon = "images/battle_skill_icons/slime/MalleableForm.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 70

        DodgeBuff =    {1:1.8, 2:1.8, 3:1.9, 4:1.9}
        HealPerc =     {1:0.3, 2:0.4, 3:0.4, 4:0.5}

        AITags = {AI_TAGS.HEAL_SELF}

        def Execute(self, Target):
            Battle_ScheduledCast(
                 
                SourceSkillObj = self,
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(
                            Duration = 1, 
                            StatMod_DodgeRating = self.DodgeBuff[self.Level], 
                            StatusEffectID = "slime_mallform_dodgebuff")),
                    BattleEffect_RestoreHealth(RestoreValue = self.HealPerc[self.Level], RatioFromMax = True)])
            return

        def GetDesc(self, DescLevel = 1):
            DodgeBuffPerc = Battle_FormatDescVal(round((self.DodgeBuff[DescLevel] - 1.0) * 100), Percentage = True)
            HealPerc = Battle_FormatDescVal(round(self.HealPerc[DescLevel] * 100), Percentage = True)
            return tra(_("Manipulate your slime to reshape and reform your body, increasing the chance of dodging by %s for 1 turn and restoring %s of your max health.")) % (DodgeBuffPerc, HealPerc)