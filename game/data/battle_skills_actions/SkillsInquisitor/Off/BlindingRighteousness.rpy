init python:
    @RegisterBattleSkill("InquisitorBlindingRighteousness")
    class BattleSkill_InquisitorBlindingRighteousness(BattleSkill):
        DisplayName = _("Blinding Righteousness")

        Icon = "images/battle_skill_icons/inquisitor/BlindingRighteousness.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 70

        DamageValue = {1:1.5, 2:1.6, 3:1.7, 4:1.8}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level])
            
            StunTargets = Battle_GetAllEnemiesOfChar(self.Owner_BattleChar)
            for Enemy in StunTargets:
                if RngFloat(0.0, 1.0) <= 0.6:
                    Battle_ApplyStatusEffect(
                        TargetChar = Enemy,
                        StatusEffect = BattleStatusEff_Stun(
                            Duration = 1,
                            SourceName = self.DisplayName),
                        CastOnEnemy = True)
                    Battle_RunCharAnim(Enemy, "hit")

            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Slash at a single enemy inflicting %s damage. The blinding light from your blade can stun all enemies for 1 turn with 60%% chance.")) % StrikeDamage