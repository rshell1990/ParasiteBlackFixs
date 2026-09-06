init python:
    @RegisterBattleSkill("InquisitorDefenderOfTheWeak")
    class BattleSkill_InquisitorDefenderOfTheWeak(BattleSkill):    
        DisplayName = _("Defender of the weak")

        Icon = "images/battle_skill_icons/inquisitor/DefenderOfTheWeak.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 50

        DamageReductionBuff = {1:0.8, 2:0.75, 3:0.7, 4:0.65}

        AITags = {AI_TAGS.ONLY_IF_ALLIES_EXIST, AI_TAGS.FAVOURED_HIGH_OWN_HP_RATIO}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Willpower(
                            Duration = 1, 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(
                            DamageRecieved_Mod = self.DamageReductionBuff[self.Level],
                            StatusEffectID = "inquisitor_defenderoftheweak_dmgtakenbuff",
                            Duration = 2, 
                            SourceName = self.DisplayName)),
                            ])

            TargetList = Battle_GetAllAlliesOfChar(self.Owner_BattleChar)

            for Target in reversed(TargetList):
                if (Target.Health / Target.HealthMax) > 0.5:
                    TargetList.remove(Target)
            
            if len(TargetList) > 0:
                for Target in TargetList:
                    Battle_ApplyStatusEffect(
                        TargetChar = Target,
                        StatusEffect = BattleStatusEff_Protected(
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            ProtectedBy = self.Owner_BattleChar,
                            AllowMultiple = True))
            return

        def GetDesc(self, DescLevel = 1):
            DamageReductionPerc = Battle_FormatDescVal(round((1.0 - self.DamageReductionBuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Protect all allies on your team below 50%% health, taking the hit for them for 2 turns.\nYou gain a willpower status effect for 1 turn and %s damage reduction for 2 turns.")) % DamageReductionPerc