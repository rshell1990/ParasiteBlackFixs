init python:    
    @RegisterBattleSkill("ChargedStrike")
    class BattleSkill_BerserkerChargedStrike(BattleSkill):
        DisplayName = _("Charged Strike")
        
        Icon = "images/battle_skill_icons/neutral/ChargedStrike.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 50

        DamageValue =  {1: 2.0, 2: 2.2, 3: 2.4, 4: 2.6, 5: 3.0}
        DebuffChance = {1: 80,  2: 80,  3: 90,  4: 90,  5: 100}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            actor = self.Owner_BattleChar
            
            charge_effect = Battle_GetStatusEffect(actor, "ChargedStrikeState")

            if charge_effect is None:
                # --- PHASE 1: BEGIN CHARGING ---
                actor.StatusEffects.append(
                    BattleStatusEff_ChargedStrikeState(
                        Duration = 1,
                        StatusEffectID = "ChargedStrikeState",
                        SourceName = self.DisplayName,
                        SkillRef = self,
                        Target = Target,
                        Owner = actor
                    )
                )

                if hasattr(actor, "PlayAnim"):
                    actor.PlayAnim("charge_pose")
                    
                Battle_AddLogEntry(tra(_("{color=[BATTLE_COLORS_LOG.BATTLE_STATUS]}%s begins gathering power for a Charged Strike!{/color}")) % actor.DisplayName)

            else:
                # --- PHASE 2: RELEASE ATTACK ---
                if charge_effect in actor.StatusEffects:
                    actor.StatusEffects.remove(charge_effect)

                # Scheduled attack execution without undefined VFX or bad image IDs
                Battle_ScheduledAttack( 
                    SourceSkillObj = self, 
                    AttackTarget = Target,
                    DamageMod = self.DamageValue[self.Level],
                    CustomImpactVfxID = None,
                    Effects_OnHit_Target = [
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = self.DebuffChance[self.Level], 
                            StatusEffect = BattleStatusEff_StatMod_Armor(
                                Duration = 3,
                                StatMod_Armor = 0.5,
                                StatusEffectID = "charged_strike_armor_debuff",
                                SourceName = self.DisplayName
                            )
                        )
                    ]
                )
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round(self.Owner_BattleChar.Damage * self.DamageValue[DescLevel])) + "{/color}"
            else:
                StrikeDamage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round(worldChars[self.Owner_PBCharID]["Damage"] * self.DamageValue[DescLevel])) + "{/color}"
            DmgPercentage = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(round(self.DamageValue[DescLevel] * 100)) + "%{/color}"
            DebuffChance = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}" + str(self.DebuffChance[DescLevel]) + "%{/color}"
            return tra(_("Spend 1 turn gathering energy, then release a powerful blow dealing %s physical damage (%s of char's base damage).\nHas a %s chance to reduce target armor by 50%% for 3 turns.")) % (StrikeDamage, DmgPercentage, DebuffChance)


    # -------------------------------------------------------------------------
    # Helper Status Effect Class
    # -------------------------------------------------------------------------
    class BattleStatusEff_ChargedStrikeState(object):
        StatusEffectID = "ChargedStrikeState"
        IsPermanent = False
        Permanent = False
        TickOn = 0
        
        StatMod_Armor = None
        StatMod_MagicRes = None
        StatMod_AttackRating = None
        StatMod_DodgeRating = None
        StatMod_CritChance = None
        ResRecoverMod_Energy = None
        ResRecoverMod_Mana = None

        def __init__(self, Duration=1, StatusEffectID="ChargedStrikeState", SourceName="", SkillRef=None, Target=None, Owner=None, **kwargs):
            self.Owner = Owner or kwargs.get("owner", None)
            self.Duration = Duration
            self.StatusEffectID = StatusEffectID
            self.SourceName = SourceName
            self.SkillRef = SkillRef
            self.Target = Target

            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.BUFF
            self.Name = "Charging"
            self.Description = "Gathering power for a Charged Strike."
            self.Icon = "gui/vfx/status_atk_up.png"

        def OnTurnStart(self):
            if self.Target and getattr(self.Target, "IsAlive", True):
                self.SkillRef.Execute(self.Target)
            else:
                actor = self.SkillRef.Owner_BattleChar
                alive_enemies = Battle_GetAliveCharsOnSide(1 if actor.BattleSide == 0 else 0)
                if alive_enemies:
                    self.SkillRef.Execute(alive_enemies[0])
                else:
                    if self in actor.StatusEffects:
                        actor.StatusEffects.remove(self)

        def TickDuration(self, AtEnd = False):
            pass