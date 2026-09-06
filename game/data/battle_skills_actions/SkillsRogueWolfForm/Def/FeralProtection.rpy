init python:
    @RegisterBattleSkill("RogueWolfFeralProtection")
    class BattleSkill_RogueWolfFeralProtection(BattleSkill):
        DisplayName = _("Feral Protection")
        Icon = "images/battle_skill_icons/rogue_wolf/FeralProtection.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 40

        RecoveryBuff = {
            1:2.0, 
            2:2.2, 
            3:2.4}

        AITags = {AI_TAGS.REMOVE_DEBUFFS_ON_TARGET}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_RemoveDebuffsOnTarget(),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Invincibility(Duration = 1, SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_HealthRecoveryMod(ResRecoverMod_Health = self.RecoveryBuff[self.Level], Duration = 2, SourceName = self.DisplayName, StatusEffectID = "wolf_feralprot_hpregenbuff")),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_EnergyRecoveryMod(ResRecoverMod_Energy = self.RecoveryBuff[self.Level], Duration = 2, SourceName = self.DisplayName, StatusEffectID = "wolf_feralprot_epregenbuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            RecoveryBuffPerc = Battle_FormatDescVal(round((self.RecoveryBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Removes all harmful effects, becomes invincible for 1 turn and increases health recovery by %s for 2 turns.")) % RecoveryBuffPerc
            