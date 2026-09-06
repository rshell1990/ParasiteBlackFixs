init python:
    @RegisterBattleSkill("RogueWolfForThePack")
    class BattleSkill_RogueWolfForThePack(BattleSkill):
        DisplayName = _("For the Pack")
        Icon = "images/battle_skill_icons/rogue_wolf/ForThePack.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALLY_NOT_SELF

        Cost_Energy = 40

        ArmorDodgeBuff = {
            1:1.8,
            2:1.9,
            3:2.0}

        AIBaseWeight = 1.1

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = Target,
                Effects_OnSelf = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Armor(Duration = 2, StatMod_Armor = self.ArmorDodgeBuff[self.Level], StatusEffectID = "wolf_forthepack_armorbuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 2, StatMod_DodgeRating = self.ArmorDodgeBuff[self.Level], StatusEffectID = "wolf_forthepack_dodgebuff", SourceName = self.DisplayName))],
                Effects_OnTarget = [BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Protected(Duration = 1, SourceName = self.DisplayName, ProtectedBy = self.Owner_BattleChar))])
            return

        def GetDesc(self, DescLevel = 1):
            ArmorDodgeChancePerc = Battle_FormatDescVal(round((self.ArmorDodgeBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Places an ally in a state of protection for 1 turn and increases your armor and dodge chance by %s for 2 turns.")) % ArmorDodgeChancePerc