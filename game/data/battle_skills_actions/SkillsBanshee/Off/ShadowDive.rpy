init python:
    @RegisterBattleSkill("BansheeShadowDive")
    class BattleSkill_BansheeShadowDive(BattleSkill):
        DisplayName = _("Shadow Dive")

        Icon = "images/battle_skill_icons/banshee/ShadowDive.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 40

        DamageValue = {1:0.55, 2:0.6, 3:0.65, 4:0.7, 5:0.75}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            for i in range(2):
                Battle_ScheduledAttack(
                    SourceSkillObj = self,
                    AttackTarget = Target,
                    DamageMod = self.DamageValue[self.Level],
                    Effects_OnHit_Target = [
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = 0.8,
                            StatusEffect = BattleStatusEff_Bleed(BaseValue = self.Owner_BattleChar.Damage, Duration = 2, SourceName = self.DisplayName))
                    ])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Fly past the enemy and attempt to swipe them with your claws, attacking them twice. Each strike deals %s damage and has a 80%% chance to cause the target to bleed.")) % (StrikeDamage)