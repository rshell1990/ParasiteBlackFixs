init python:
    @RegisterBattleSkill("BerserkerWarCry")
    class BattleSkill_BerserkerWarCry(BattleSkill):
        DisplayName = _("War Cry")

        Icon = "images/battle_skill_icons/berserker/WarCry.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 45

        DamageTakenBuff = {1:0.4, 2:0.3, 3:0.2}

        AITags = {AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE, AI_TAGS.TAUNT_TARGET}

        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledCast(
                 
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Taunt(Duration = 1, SourceName = self.DisplayName, TauntedBy = self.Owner_BattleChar))],
                Effects_OnSelf = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(DamageRecieved_Mod = self.DamageTakenBuff[self.Level], Duration = 1, SourceName = self.DisplayName, StatusEffectID = "bers_warcry_dmgin_buff"))])
            return

        def GetDesc(self, DescLevel = 1):
            DamageTakenPerc = Battle_FormatDescVal(round((1.0 - self.DamageTakenBuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Unleashes a war cry to provoke all enemies for 1 turn and reduces damage taken by %s for 1 turn.")) % DamageTakenPerc
