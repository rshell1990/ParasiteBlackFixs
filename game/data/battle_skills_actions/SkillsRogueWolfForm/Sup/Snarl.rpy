init python:
    @RegisterBattleSkill("RogueWolfSnarl")
    class BattleSkill_RogueWolfSnarl(BattleSkill):
        DisplayName = _("Snarl")
        Icon = "images/battle_skill_icons/rogue_wolf/Snarl.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 60

        DodgeArmorBuff = {
            1:1.6,
            2:1.7,
            3:1.8}

        AITags = {AI_TAGS.TAUNT_TARGET}

        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_DamageOut(DamageDealt_Mod = 0.4, Duration = 2, SourceName = self.DisplayName, StatusEffectID = "wolf_snarl_dmgoutdebuff")),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Taunt(Duration = 1, SourceName = self.DisplayName, TauntedBy = self.Owner_BattleChar))],
                Effects_OnSelf = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Armor(Duration = 1, StatMod_Armor = self.DodgeArmorBuff[self.Level], StatusEffectID = "wolf_snarl_armorbuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 1, StatMod_DodgeRating = self.DodgeArmorBuff[self.Level], StatusEffectID = "wolf_snarl_dodgebuff", SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            DodgeArmorBuffPerc = Battle_FormatDescVal(round((self.DodgeArmorBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Snarls at all enemies, provoking them for 1 turn and decreasing the damage they deal by 60%% for 2 turn. Increases your dodge chance and your armor by %s for 1 turn.")) % DodgeArmorBuffPerc