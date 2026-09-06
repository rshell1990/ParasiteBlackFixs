init python:
    @RegisterBattleSkill("WarriorDodge")
    class BattleSkill_WarriorDodge(BattleSkill):
        DisplayName = _("Dodge")
        
        Icon = "images/battle_skill_icons/warrior/Dodge.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 35
        DodgeAccBuff = {1:1.5, 2:1.6, 3:1.7}

        AIBaseWeight = 1.1

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self,
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_StatMod_Dodge(
                                        Duration = 2,
                                        StatMod_DodgeRating = 1.5,
                                        SourceName = self.DisplayName)),
                                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_StatMod_Accuracy(
                                        Duration = 2,
                                        StatMod_AttackRating = 1.5,
                                        SourceName = self.DisplayName))])
            Battle_GrantExtraTurn(self.Owner_BattleChar)
            return

        def GetDesc(self, DescLevel = 1):
            PercentageBuff = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round((self.DodgeAccBuff[DescLevel] - 1.0) * 100)) + "%{/color}"
            return tra(_("Increases your attack rating and dodge rating by %s for 2 turns and grants you an extra turn.")) % PercentageBuff