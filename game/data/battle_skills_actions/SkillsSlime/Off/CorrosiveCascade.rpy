init python:
    @RegisterBattleSkill("SlimeCorrosiveCascade")
    class BattleSkill_SlimeCorrosiveCascade(BattleSkill):
        DisplayName = _("Corrosive Cascade")

        Icon = "images/battle_skill_icons/slime/CorrosiveCascade.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 70

        DamageValue =      {1:1.4, 2:1.4,  3:1.55, 4:1.55, 5:1.7}
        DamageResDebuff =  {1:1.4, 2:1.55, 3:1.55, 4:1.7,  5:1.7}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SoundSwing_CustomList = soundLib["Battle_SlimeAcid"],
                SoundSwing_DoNotCutOffOnImpact = True,
                SoundImpact_CustomList = [],
                SourceSkillObj = self,
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                CustomUserVfxID = "Battle_VfxImpactSlimeySlash",
                CustomImpactVfxID = "Battle_VfxImpactSlimeyImpact",
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_DamageIn(
                            DamageRecieved_Mod = self.DamageResDebuff[self.Level], 
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "slime_corrcasc_dmgin_debuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            DamageResDebuffPerc = Battle_FormatDescVal(round((self.DamageResDebuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Create a cascading wave of corrosive slime, dealing %s damage to all enemies and reducing their damage resistance by %s for 2 turns.")) % (StrikeDamage, DamageResDebuffPerc)
