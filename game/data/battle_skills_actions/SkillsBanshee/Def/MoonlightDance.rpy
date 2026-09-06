init python:
    @RegisterBattleSkill("BansheeMoonlightDance")
    class BattleSkill_BansheeMoonlightDance(BattleSkill):    
        DisplayName = _("Moonlight Dance")

        Icon = "images/battle_skill_icons/banshee/MoonlightDance.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 40

        AITags = {AI_TAGS.TAUNT_TARGET}

        DodgeIncreasePerc = {
            1:1.80,
            2:1.85,
            3:1.90,
        }

        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = Target,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Taunt(
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            TauntedBy = self.Owner_BattleChar))],
                Effects_OnSelf = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 2, StatMod_DodgeRating = self.DodgeIncreasePerc[self.Level], StatusEffectID = "banshee_moonlightdance_dodgebuff", SourceName = self.DisplayName))]
                        )
            return

        def GetDesc(self, DescLevel = 1):
            DodgeIncreasePercFormatted = Battle_FormatDescVal(round((self.DodgeIncreasePerc[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Take to the skies and taunt the enemy for 2 turns and increase dodge by %s for 2 turns.")) % DodgeIncreasePercFormatted