init python:
    @RegisterBattleSkill("BansheeASongOfSacrifice")
    class BattleSkill_BansheeASongOfSacrifice(BattleSkill):
        DisplayName = _("A song of sacrifice")

        Icon = "images/battle_skill_icons/banshee/ASongOfSacrifice.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 70

        HealValue = {1:0.6, 2:0.7, 3:0.8, 4:0.9}


        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_RestoreHealth(
                        RestoreValue = self.HealValue[self.Level],
                        RatioFromMax = True,
                        )],
                Effects_OnSelf = [BattleEffect_SetHealth(SetValue = 1)])
            self.Owner_BattleChar.Health = 1
            return

        def GetDesc(self, DescLevel = 1):
            HealPercentage = Battle_FormatDescVal(round(self.HealValue[DescLevel] * 100), Percentage = True)
            return tra(_("Your song uplifts everyone to fight on!\nThe party is healed by %s, but your health is reduced to 1.")) % HealPercentage