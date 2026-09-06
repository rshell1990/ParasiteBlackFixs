init python:
    @RegisterBattleSkill("InquisitorPhoahsGlory")
    class BattleSkill_InquisitorPhoahsGlory(BattleSkill):
        DisplayName = _("Phoah's Glory")

        Icon = "images/battle_skill_icons/inquisitor/PhoahsGlory.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 40

        ArmorBuff = {1:1.8, 2:1.9, 3:2.0}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Counter(
                            Duration = 2,
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            Duration = 2,
                            StatMod_Armor = self.ArmorBuff[self.Level],
                            StatusEffectID = "inquisitor_phoahs_glory_armor_buff",
                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            ArmorBuffPerc = Battle_FormatDescVal(round((self.ArmorBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Enter a counter stance and buff your armor by %s for 2 turns.")) % ArmorBuffPerc