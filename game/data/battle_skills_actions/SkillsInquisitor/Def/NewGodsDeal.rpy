init python:
    @RegisterBattleSkill("InquisitorNewGodsDeal")
    class BattleSkill_InquisitorNewGodsDeal(BattleSkill):
        DisplayName = _("New God's deal")

        Icon = "images/battle_skill_icons/inquisitor/NewGodsDeal.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 90

        DamageAndAccuracyDebuff = {1:0.4, 2:.3, 3:0.2}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = 0.4,
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                            Duration = 3,
                            StatMod_AttackRating = self.DamageAndAccuracyDebuff[self.Level],
                            StatusEffectID = "inquisitor_newgodsdeal_accdebuff",
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_DamageOut(
                            DamageDealt_Mod = self.DamageAndAccuracyDebuff[self.Level],
                            Duration = 3,
                            SourceName = self.DisplayName,
                            StatusEffectID = "inquisitor_newgodsdeal_dmgdebuff"))
                ])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, 0.4))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, 0.4))

            return tra(_("Attacks the enemy with a weak blow dealing %s damage, reducing an enemy's damage and accuracy by 60%% for 3 turns.")) % StrikeDamage
