init python:
    @RegisterBattleSkill("ScoutDefensiveMode")
    class BattleSkill_ScoutDefensiveMode(BattleSkill):    
        DisplayName = _("Defensive Mode")
        Icon = "images/battle_skill_icons/scout/DefensiveMode.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 30

        DodgeBuff = {1:1.5, 2:1.6, 3:1.7}

        AITags = {AI_TAGS.HEAL_SELF}

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_RegenHealth(Duration = 2, RestoreVal = 0.1, RatioFromMax = True, SourceName = self.DisplayName, StatusEffectID = "scout_defmode_regen")),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 1, StatMod_DodgeRating = self.DodgeBuff[self.Level], StatusEffectID = "scout_defmode_dodgebuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(Duration = 2, StatMod_AttackRating = 0.8, StatusEffectID = "scout_defmode_accdebuff", SourceName = self.DisplayName)),])
            return

        def GetDesc(self, DescLevel = 1):
            DodgeBuffPerc = Battle_FormatDescVal(round((self.DodgeBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Increases your dodge chance by %s for 1 turn and recovers your health by 10%% of your maximum for the next 2 turns at the expense of 20%% of your accuracy for 2 turns.")) % DodgeBuffPerc