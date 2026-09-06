init python:
    @RegisterBattleSkill("SlimePrimordialUnity")
    class BattleSkill_SlimePrimordialUnity(BattleSkill):
        DisplayName = _("Primoridal Unity")
        Icon = "images/battle_skill_icons/slime/PrimordialUnity.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.SELF

        Cost_Energy = 125

        DamageResBuff = {1:0.8, 2:0.7, 3:0.6}

        AITags = {AI_TAGS.RAISE_TARGET_PHYS_DAMAGE_RESISTANCE}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Counter(Duration = 2, SourceName = self.DisplayName))])

            TargetAllies = Battle_GetAliveCharsOnSide(self.Owner_BattleChar.BattleSide)
            TargetAllies.remove(self.Owner_BattleChar)
            for Char in TargetAllies:
                Battle_ApplyStatusEffect(
                    TargetChar = Char, 
                    StatusEffect = BattleStatusEff_DamageIn(
                    Duration = 2,
                    DamageRecieved_Mod = self.DamageResBuff[self.Level], 
                    SourceName = self.DisplayName, 
                    StatusEffectID = "slime_primunity_ally_dmgres"))
            return

        def GetDesc(self, DescLevel = 1):
            DamageResBuff = Battle_FormatDescVal(round((1.0 - self.DamageResBuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Channel the primordial essence of your slime lineage, enter a counter state for 2 turns and enhance the damage resistance of your allies by %s for 2 turns.")) % DamageResBuff