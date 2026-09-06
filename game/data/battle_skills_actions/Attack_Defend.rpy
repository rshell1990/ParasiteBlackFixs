init python:
    class BattleSkill_Attack(BattleSkill):
        DisplayName = _("Basic Attack")
        Icon = "images/battle_skill_icons/std_attack.webp"

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        OncePerTurn = False
        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        AIBaseWeight = 0.75

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self, 
                AttackTarget = Target, 
                ImpactVfxRandomRotation = True
            )
            return

        def GetDesc(self, DescLevel = 1):
            StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar), Parentheses = True)
            return tra(_("Deal 75%%-125%% %s damage.")) % StrikeDamage
######################################################################
    class BattleSkill_Defend(BattleSkill):
        DisplayName = _("Defend")
        Icon = "images/battle_skill_icons/std_defend.webp"

        ValidTargets = BATTLE_TARGETS.SELF
        AITags = {AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE}

        AIBaseWeight = 0.5

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = self.Owner_BattleChar,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_DamageIn(
                            DamageRecieved_Mod = 0.6,
                            Duration = 1,
                            SourceName = self.DisplayName,
                            StatusEffectID = "defend_damagemod_buff")
                    ),
                    BattleEffect_ApplyStatusOnAlly(
                        Chance = 1,
                        StatusEffect = BattleStatusEff_HealthRecoveryMod(
                            ResRecoverMod_Health = 2.0,
                            Duration = 2, 
                            SourceName = self.DisplayName,
                            StatusEffectID = "defend_hp_recover_buff")
                    ),
                    BattleEffect_ApplyStatusOnAlly(
                        Chance = 1,
                        StatusEffect = BattleStatusEff_EnergyRecoveryMod(
                            ResRecoverMod_Energy = 2.0,
                            Duration = 2, 
                            SourceName = self.DisplayName,
                            StatusEffectID = "defend_ep_recover_buff")
                    )
                ]
            )
            return

        def GetDesc(self, DescLevel = 1):
            return tra(_("Damage taken is reduced by 40% for 1 turn. The amount of healing and energy recovery is also increased by 100% for 2 turns."))
