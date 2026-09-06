init python:
    @RegisterBattleSkill("InquisitorFirewall")
    class BattleSkill_InquisitorFirewall(BattleSkill):    
        DisplayName = _("Firewall")

        Icon = "images/battle_skill_icons/inquisitor/Firewall.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 50

        DamageDealtDebuff = {1:0.2, 2:0.3, 3:0.4, 4:0.5}

        AITags = {AI_TAGS.FAVOURED_HIGH_OWN_HP_RATIO}

        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Burn(
                            BaseValue = self.Owner_BattleChar.Damage,
                            Duration = 2,
                            SourceName = self.DisplayName))],
                Effects_OnSelf = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(
                            DamageRecieved_Mod = 0.3,
                            Duration = 2,
                            SourceName = self.DisplayName,
                            StatusEffectID = "inquisitor_firewall_dmgin_buff")),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageOut(
                            DamageDealt_Mod = self.DamageDealtDebuff[self.Level],
                            Duration = 2,
                            SourceName = self.DisplayName,
                            StatusEffectID = "inquisitor_firewall_dmgin_debuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            DamageDealtDebuffPerc = Battle_FormatDescVal(round((1.0 - self.DamageDealtDebuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Create a firewall around yourself, inflicting 1 burning effect to all enemies for 2 turns. Also decreases damage received by 70%%, but decreases the damage you deal by %s for 2 turns. ")) % DamageDealtDebuffPerc