init python:
    @RegisterBattleSkill("InquisitorGreatDodge")
    class BattleSkill_InquisitorGreatDodge(BattleSkill):    
        DisplayName = _("Great Dodge")

        Icon = "images/battle_skill_icons/inquisitor/GreatDodge.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 60

        DodgeBuff = {1:3.0, 2:3.5, 3:4.0, 4:4.5}


        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(
                            StatMod_DodgeRating = self.DodgeBuff[self.Level],
                            StatusEffectID = "inquisitor_greatdodge_dodgebuff",
                            Duration = 2,
                            SourceName = self.DisplayName))])
            Battle_GrantExtraTurn(self.Owner_BattleChar)
            return

        def GetDesc(self, DescLevel = 1):
            DodgeBuffPerc = Battle_FormatDescVal(round((self.DodgeBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("You're quick on your feet, increase your dodge chance by %s for 2 turns and gain another turn immediately.")) % DodgeBuffPerc