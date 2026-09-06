init python:
    @RegisterBattleSkill("BerserkerDeclareWar")
    class BattleSkill_BerserkerDeclareWar(BattleSkill):
        DisplayName = _("Declare War")

        Icon = "images/battle_skill_icons/berserker/DeclareWar.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 105

        DamageDealtDebuff = {1:0.7, 2:0.65, 3:0.6, 4:0.5}

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
                            TauntedBy = self.Owner_BattleChar)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_DamageOut(
                            DamageDealt_Mod = self.DamageDealtDebuff[self.Level], 
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "bers_declarewar_dmgout_debuff"))],
                Effects_OnSelf = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Counter(
                            Duration = 2, 
                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            DamageDealtPerc = Battle_FormatDescVal(round((1.0 - self.DamageDealtDebuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Use your shout to provoke all enemies and reduce the damage they cause by %s for 2 turns each.\nCounters when attacked for 2 turns.")) % DamageDealtPerc