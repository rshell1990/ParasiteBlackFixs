init python:
    @RegisterBattleSkill("RogueDarkening")
    class BattleSkill_RogueDarkening(BattleSkill):
        DisplayName = _("Darkening")

        Icon = "images/battle_skill_icons/rogue/Darkening.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 70

        SelfDodgeAccBuff =     {1:1.4, 2:1.5, 3:1.5, 4:1.6}
        EnemyDodgeAccDebuff =  {1:0.7, 2:0.7, 3:0.6, 4:0.6}

        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 2, StatMod_DodgeRating = self.EnemyDodgeAccDebuff[self.Level], StatusEffectID = "roguedarkening_dodgedebuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(StatusEffect = BattleStatusEff_StatMod_Accuracy(Duration = 2, StatMod_AttackRating = self.EnemyDodgeAccDebuff[self.Level], StatusEffectID = "roguedarkening_accdebuff", SourceName = self.DisplayName))],
                Effects_OnSelf = [
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 2, StatMod_DodgeRating = self.SelfDodgeAccBuff[self.Level], StatusEffectID = "roguedarkening_dodgebuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_StatMod_Accuracy(Duration = 2, StatMod_AttackRating = self.SelfDodgeAccBuff[self.Level], StatusEffectID = "roguedarkening_accbuff", SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            AccDodgeBuffPerc = Battle_FormatDescVal(round((self.SelfDodgeAccBuff[DescLevel] - 1.0) * 100), Percentage = True)
            AccDodgeDebuffPerc = Battle_FormatDescVal(round((1.0 - self.EnemyDodgeAccDebuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Uses a miserly power to increase your dodge chance and accuracy by %s for 2 turns and decrease the accuracy and dodge of all enemies by %s for 2 turns.")) % (AccDodgeBuffPerc, AccDodgeDebuffPerc)