init python:
    @RegisterBattleSkill("WarriorLeadersCall")
    class BattleSkill_WarriorLeadersCall(BattleSkill):
        DisplayName = _("Leader's Call")
        Icon = "images/battle_skill_icons/warrior/LeadersCall.webp"
        

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 80
        DamageDealtBuff = {1:1.4, 2:1.5, 3:1.6}

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                SoundUse_CustomList = soundLib["Battle_WarriorShout"],
                Effects_OnTarget = [BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_Immunity(
                                        Duration = 2,
                                        SourceName = self.DisplayName)),
                                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_DamageOut(
                                        DamageDealt_Mod = self.DamageDealtBuff[self.Level], 
                                        Duration = 2, 
                                        SourceName = self.DisplayName, 
                                        StatusEffectID = "warrior_leaders_call_dmgout_buff"))])
            return

        def GetDesc(self, DescLevel = 1):
            DamageDealtPercentage = Battle_FormatDescVal(round((self.DamageDealtBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Increases the damage dealt by all allies by %s and grants them debuff immunity for 2 turns.")) % DamageDealtPercentage