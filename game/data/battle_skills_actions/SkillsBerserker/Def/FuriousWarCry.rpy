init python:
    @RegisterBattleSkill("BerserkerFuriousWarCry")
    class BattleSkill_BerserkerFuriousWarCry(BattleSkill):
        DisplayName = _("Furious War Cry")

        Icon = "images/battle_skill_icons/berserker/FuriousWarCry.webp"

        Level_Max = 1

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 80

        AutoSelectNextInPartyOnExecute = False

        AITags = {AI_TAGS.TAUNT_TARGET}

        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Taunt(
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            TauntedBy = self.Owner_BattleChar))])
            Battle_GrantExtraTurn(self.Owner_BattleChar)
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Use your shout to provoke all enemies for 2 turns and gain another turn instantly."))