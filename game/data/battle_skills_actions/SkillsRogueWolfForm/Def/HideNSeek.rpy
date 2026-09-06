init python:
    @RegisterBattleSkill("RogueWolfHideNSeek")
    class BattleSkill_RogueWolfHideNSeek(BattleSkill):
        DisplayName = _("Hide and Seek")
        Icon = "images/battle_skill_icons/rogue_wolf/HideNSeek.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 60

        DmgDodgeBuff = {
            1:2.0,
            2:2.1,
            3:2.2,
            4:2.3,
            5:2.4}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 1, StatMod_DodgeRating = self.DmgDodgeBuff[self.Level], StatusEffectID = "wolf_hideseek_dodgebuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageOut(DamageDealt_Mod = self.DmgDodgeBuff[self.Level], Duration = 1, SourceName = self.DisplayName, StatusEffectID = "wolf_hdennseek_dmgoutbuff")),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Counter(Duration = 2, SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            DmgDodgeBuffPerc = Battle_FormatDescVal(round((self.DmgDodgeBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Increases your dodge chance by %s, increases the damage you deal by %s for 1 turn and counterattacks for 2 turn.")) % (DmgDodgeBuffPerc, DmgDodgeBuffPerc)