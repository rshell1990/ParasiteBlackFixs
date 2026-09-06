init python:
    @RegisterBattleSkill("ParasiteWhiteFieryCounter")
    class BattleSkill_ParasiteWhiteFieryCounter(BattleSkill):
        DisplayName = _("Fiery Counter")

        Icon = "images/battle_skill_icons/parawhite/FieryCounter.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 60
        ArmorBuffValue = {1:1.4, 2:1.5, 3:1.6}

        AITags = {AI_TAGS.TAUNT_TARGET}

        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledCast(
                SoundUse_CustomList = soundLib["Battle_FireStrikes"],
                SoundImpact_CustomList = soundLib["Battle_FireImpacts"],
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Taunt(
                            Duration = 1, 
                            SourceName = self.DisplayName, 
                            TauntedBy = self.Owner_BattleChar)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Burn(
                            BaseValue = self.Owner_BattleChar.Damage, 
                            Duration = 1, 
                            SourceName = self.DisplayName))],
                Effects_OnSelf = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            Duration = 2, 
                            StatMod_Armor = self.ArmorBuffValue[self.Level], 
                            StatusEffectID = "parawhite_fireycounter_armorbuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            ArmorPerc = Battle_FormatDescVal(round((self.ArmorBuffValue[DescLevel] - 1.0) * 100), Percentage = False)
            return tra(_("Goes into a defensive state, provoking all enemies and setting them on fire for 1 turn and increasing your armour by %s for 2 turns.")) % ArmorPerc