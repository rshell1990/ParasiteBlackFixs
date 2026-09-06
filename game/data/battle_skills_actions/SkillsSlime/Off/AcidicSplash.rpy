init python:
    @RegisterBattleSkill("SlimeAcidicSplash")
    class BattleSkill_SlimeAcidicSplash(BattleSkill):
        DisplayName = _("Acidic Splash")

        Icon = "images/battle_skill_icons/slime/AcidicSplash.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 40

        DamageValue =      {1:1.3, 2:1.3, 3:1.5, 4:1.5}
        DamageResDebuff =  {1:1.5, 2:1.6, 3:1.6, 4:1.7}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SoundSwing_CustomList = soundLib["Battle_SlimeAcid"],
                SoundSwing_DoNotCutOffOnImpact = True,
                SoundImpact_CustomList = [],
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                CustomImpactVfxID = "Battle_VfxImpactSlimeyImpact",
                CustomUserVfxID = "Battle_VfxImpactSlimeyProjectileToss",
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_DamageIn(
                            DamageRecieved_Mod = self.DamageResDebuff[self.Level], 
                            Duration = 2, 
                            SourceName = self.DisplayName, 
                            StatusEffectID = "slime_acidsplash_dmgin_debuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            DamageResDebuffPerc = Battle_FormatDescVal(round((self.DamageResDebuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Project corrosive slime to melt through enemy defenses, dealing %s and reducing the target's damage resistance by %s for 2 turns.")) % (StrikeDamage, DamageResDebuffPerc)