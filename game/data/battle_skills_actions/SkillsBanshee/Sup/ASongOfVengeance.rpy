init python:
    @RegisterBattleSkill("BansheeASongOfVengeance")
    class BattleSkill_BansheeASongOfVengeance(BattleSkill):    
        DisplayName = _("A song of vengeance")

        Icon = "images/battle_skill_icons/banshee/ASongOfVengeance.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 100

        ArmorBuff = {1:1.3, 2:1.35, 3:1.4, 4:1.5}


        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            Duration = 2, 
                            StatMod_Armor = self.ArmorBuff[self.Level],
                            StatusEffectID = "banshee_asongofvengeance_armorbuff",
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Counter(
                            Duration = 2, 
                            SourceName = self.DisplayName)),
                    ])
            return

        def GetDesc(self, DescLevel = 1):
            ArmorBuffPerc = Battle_FormatDescVal(round((self.ArmorBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Your party is granted a counter buff and an armor buff of %s for 2 turns.")) % ArmorBuffPerc