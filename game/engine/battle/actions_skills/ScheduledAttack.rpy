init python:
    class Battle_ScheduledAttack:
        def __init__(self, 
                SourceSkillObj = None,
                DamageMod = 1.0,
                DamageMod_AdditivePerDebuffOnTarget = None,
                AttackTarget = None,

                Effects_OnHit_Target = None,     
                Effects_OnHit_User = None,     
                Effects_OnKill_User = None,
                Effects_OnCrit_Target = None,
                Effects_OnCrit_User = None,

                IgnoreArmor = False,
                TriggerCounter = True,

                GuaranteedHit = False,
                GuaranteedCrit = False,

                DamageBurn_Mana = None,
                DamageBurn_Energy = None,

                DamageRecoversAttackerEnergy = None,
                DamageRecoversAttackerHealth = None,

                AbsorbTarget_HealthMax = None,

                ExtraCritChancePercentage = None,

                CustomImpactVfxID = None,
                CustomUserVfxID = None,
                ImpactVfxRandomRotation = False,

                SoundImpact_CustomList = None,
                SoundImpact_OneShotList = None,
                SoundSwing_CustomList = None,
                SoundSwing_DoNotCutOffOnImpact = None,

                DamageMod_DoubleIfTargetHasAtleastOneDebuff = False,
                AnimID = "attack"
                ):

            self.SkillName = SourceSkillObj.DisplayName if SourceSkillObj else ""
            self.UserBattleChar = SourceSkillObj.Owner_BattleChar if SourceSkillObj else None
        
            self.DamageMod = DamageMod
            self.DamageMod_AdditivePerDebuffOnTarget = DamageMod_AdditivePerDebuffOnTarget
            self.DamageMod_DoubleIfTargetHasAtleastOneDebuff = DamageMod_DoubleIfTargetHasAtleastOneDebuff

            self.TargetList = Battle_ProcessTargetList(self.UserBattleChar, AttackTarget)

            self.Effects_OnHit_Target = Effects_OnHit_Target if Effects_OnHit_Target is not None else []
            self.Effects_OnHit_User = Effects_OnHit_User if Effects_OnHit_User is not None else []
            self.Effects_OnCrit_Target = Effects_OnCrit_Target if Effects_OnCrit_Target is not None else []
            self.Effects_OnCrit_User = Effects_OnCrit_User if Effects_OnCrit_User is not None else []
            self.Effects_OnKill_User = Effects_OnKill_User if Effects_OnKill_User is not None else []

            self.IgnoreArmor = IgnoreArmor
            self.TriggerCounter = TriggerCounter
            self.GuaranteedCrit = GuaranteedCrit
            self.GuaranteedHit = GuaranteedHit

            self.DamageBurn_Mana = DamageBurn_Mana
            self.DamageBurn_Energy = DamageBurn_Energy

            self.DamageRecoversAttackerEnergy = DamageRecoversAttackerEnergy
            self.DamageRecoversAttackerHealth = DamageRecoversAttackerHealth

            self.AbsorbTarget_HealthMax = AbsorbTarget_HealthMax

            self.ExtraCritChancePercentage = ExtraCritChancePercentage

            self.CustomImpactVfxID = CustomImpactVfxID
            self.CustomUserVfxID = CustomUserVfxID
            self.ImpactVfxRandomRotation = ImpactVfxRandomRotation
            
            self.SoundImpact_CustomList = SoundImpact_CustomList
            self.SoundImpact_OneShotList = SoundImpact_OneShotList

            self.SoundSwing_CustomList = SoundSwing_CustomList
            self.SoundSwing_DoNotCutOffOnImpact = SoundSwing_DoNotCutOffOnImpact

            self.AnimID = AnimID

            BattleScene.ScheduledAttackQueue.insert(0, self)

        def ExecuteAction(self):
            # Safe filtration of dead targets without mutating list while iterating
            self.TargetList = [char for char in self.TargetList if getattr(char, "IsAlive", True)]

            if not self.TargetList:
                return

            if self.AnimID in getattr(self.UserBattleChar.BattleSkin, "AnimsDict", {}):
                PlayedAnim = Battle_RunCharAnim(self.UserBattleChar, self.AnimID)
            else:
                PlayedAnim = Battle_RunCharAnim(self.UserBattleChar, "attack")

            # Vocal grunts
            Battle_PlayCharSkinSound("Char_UseSkill", self.UserBattleChar, Voice=True, Chance=0.25)

            # Swing sound
            if self.SoundSwing_CustomList:
                ExtraSilence = max(getattr(PlayedAnim, "WarmupTo", 0.0) - 0.05, 0.0)
                Battle_PlaySoundOnBattleChar(renpy.random.choice(self.SoundSwing_CustomList), self.UserBattleChar, Voice=False, ExtraSilence=ExtraSilence)
            else:
                Battle_PlayCharSkinSound("BasicAttack_Swing", self.UserBattleChar)

            # User VFX
            if self.CustomUserVfxID is not None:
                Battle_SpawnVfxOnChar(self.UserBattleChar, self.CustomUserVfxID, RandomRotation=False, AutoXFlip=False)

            Battle_LoopStep(PlayedAnim.Warmup)

            if self.SoundImpact_OneShotList:
                Battle_PlaySoundOnBattleChar(renpy.random.choice(self.SoundImpact_OneShotList), self.TargetList[0])

            for Target in self.TargetList:
                if Battle_TryLandStrike(self.UserBattleChar, Target, GuaranteedHit=self.GuaranteedHit):
                    # Invincibility check
                    if Battle_HasStatusEffect(Target, "godmode"):
                        Battle_AddLogEntry_Autoformat(
                            String = _("USER_NAME strikes TARGET_NAME with SKILL_NAME but TARGET_NAME is invincible!"),
                            USER = self.UserBattleChar,
                            TARGET = Target,
                            SKILL_NAME = self.SkillName)
                        continue

                    # Protect check
                    if Battle_HasStatusEffect(Target, "protect"):
                        ProtectedBy = Battle_GetStatusEffect(Target, "protect").ProtectedBy
                        Battle_AddLogEntry_Autoformat(
                            String = _("USER_NAME tries to strike TARGET_NAME with SKILL_NAME but PROTECTOR_NAME moves in to protect!!"),
                            USER = self.UserBattleChar,
                            TARGET = Target,
                            PROTECTOR = ProtectedBy,
                            SKILL_NAME = self.SkillName)
                        Target = ProtectedBy
                    
                    if not self.SoundSwing_DoNotCutOffOnImpact and not getattr(PlayedAnim, "SoundSwing_DoNotCutOffOnImpact", False):
                        Battle_StopSoundOnBattleChar(self.UserBattleChar, Fadeout=0.25)

                    # Burning shield effect
                    if Battle_HasStatusEffect(Target, "brn_shield"):
                        Battle_ApplyStatusEffect(
                            TargetChar = self.UserBattleChar, 
                            StatusEffect = BattleStatusEff_Burn(
                                BaseValue = Target.Damage, 
                                Duration = 3, 
                                SourceName = Battle_GetStatusEffect(Target, "brn_shield").SourceName
                            ), 
                            CastOnEnemy = False
                        )

                    # Reflect damage effect
                    if Battle_HasStatusEffect(Target, "reflect_damage"):
                        Battle_DealDamage(self.UserBattleChar, Battle_GetStatusEffect(Target, "reflect_damage").DamageRateFromBaseCharDmg * Target.Damage)

                    # Impact sound
                    if self.SoundImpact_CustomList:
                        Battle_PlaySoundOnBattleChar(renpy.random.choice(self.SoundImpact_CustomList), Target, Voice=False)
                    else:
                        Battle_PlayCharSkinSound("BasicAttack_Impact", self.UserBattleChar, AudioSourceOverride=Target)

                    # Impact VFX
                    if self.CustomImpactVfxID is not None:
                        Battle_SpawnVfxOnChar(Target, self.CustomImpactVfxID, RandomRotation=self.ImpactVfxRandomRotation)
                    else:
                        Battle_SpawnVfxOnChar(Target, self.UserBattleChar.BattleSkin.BasicAttackImpactImageID, RandomRotation=self.ImpactVfxRandomRotation)

                    # Calculate damage modifiers
                    DmgMod = self.DamageMod
                    if self.DamageMod_AdditivePerDebuffOnTarget is not None:
                        DebuffCountOnTarget = sum(1 for status in Target.StatusEffects if status.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF)
                        DmgMod += (self.DamageMod_AdditivePerDebuffOnTarget * DebuffCountOnTarget)

                    if self.DamageMod_DoubleIfTargetHasAtleastOneDebuff:
                        if any(status.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF for status in Target.StatusEffects):
                            DmgMod *= 2.0

                    TotalStrikeDamage = Battle_BCharDamageRoll(self.UserBattleChar, Mod=DmgMod)

                    # Critical strike check
                    IsCrit = False
                    if self.GuaranteedCrit:
                        IsCrit = True
                    else:
                        CritChance = self.UserBattleChar.CritChance + (self.ExtraCritChancePercentage or 0)
                        if renpy.random.randint(1, 100) <= CritChance:
                            IsCrit = True

                    if IsCrit:
                        TotalStrikeDamage = int(TotalStrikeDamage * 2)
                        for OnCritEffect in self.Effects_OnCrit_Target:
                            OnCritEffect.ApplyEffect(Target)
                        for OnCritEffect in self.Effects_OnCrit_User:
                            OnCritEffect.ApplyEffect(self.UserBattleChar)

                    TargetDamageMod = Battle_GetIncomingDamageMod(Target)
                    ResultDamageValue = round(TotalStrikeDamage * TargetDamageMod)

                    if not self.IgnoreArmor:
                        ResultDamageValue = Battle_GetArmorDamageReduction(ResultDamageValue, Target)

                    # Logging
                    if IsCrit:
                        Battle_AddLogEntry_Autoformat(
                            USER = self.UserBattleChar,
                            TARGET = Target,
                            SKILL_NAME = self.SkillName,
                            DAMAGE_AMOUNT = ResultDamageValue,
                            String = _("USER_NAME lands a {color=[BATTLE_COLORS_LOG.CRITICAL]}critical strike{/color} on TARGET_NAME with SKILL_NAME dealing DAMAGE_AMOUNT {color=[BATTLE_COLORS_LOG.DAMAGE]}damage!{/color}"))
                    else:
                        Battle_AddLogEntry_Autoformat(
                            USER = self.UserBattleChar,
                            TARGET = Target,
                            SKILL_NAME = self.SkillName,
                            DAMAGE_AMOUNT = ResultDamageValue,
                            String = _("USER_NAME strikes TARGET_NAME with SKILL_NAME dealing DAMAGE_AMOUNT {color=[BATTLE_COLORS_LOG.DAMAGE]}damage!{/color}"))

                    Battle_DealDamage(Target, ResultDamageValue, IgnoreArmor=True, IsCrit=IsCrit)

                    if Target.IsAlive:
                        if Battle_HasStatusEffect(self.UserBattleChar, "star_bringers_stealmanastrike"):
                            ManaStolen = min(max(round(ResultDamageValue * 0.05), 1), Target.Mana)
                            if ManaStolen > 0:
                                Battle_BurnMana(Target, ManaStolen)
                                Battle_RestoreMana(self.UserBattleChar, ManaStolen)
                                Battle_AddLogEntry_Autoformat(
                                    USER = self.UserBattleChar,
                                    TARGET = Target,
                                    MANA_STOLEN = ManaStolen,
                                    String = _("USER_NAME steals MANA_STOLEN mana from TARGET_NAME with Star Bringer!"))

                        if Battle_HasStatusEffect(self.UserBattleChar, "shadowreach_stealhpstrike"):
                            HealthStolen = min(max(round(ResultDamageValue * 0.05), 1), Target.Health)
                            if HealthStolen > 0:
                                Battle_RestoreHealth(self.UserBattleChar, HealthStolen)
                                Battle_AddLogEntry_Autoformat(
                                    USER = self.UserBattleChar,
                                    TARGET = Target,
                                    HEALTH_STOLEN = HealthStolen,
                                    String = _("USER_NAME steals HEALTH_STOLEN health from TARGET_NAME with Shadowreach!"))

                    if self.DamageRecoversAttackerEnergy is not None:
                        Battle_RestoreEnergy(self.UserBattleChar, round(ResultDamageValue * self.DamageRecoversAttackerEnergy))
                    if self.DamageRecoversAttackerHealth is not None:
                        Battle_RestoreHealth(self.UserBattleChar, round(ResultDamageValue * self.DamageRecoversAttackerHealth))

                    if Target.IsAlive and self.AbsorbTarget_HealthMax is not None:
                        AbsorbHealthAmount = min(round(self.AbsorbTarget_HealthMax * Target.HealthMax), Target.Health)
                        if AbsorbHealthAmount > 0:
                            Battle_AddLogEntry_Autoformat(
                                USER = self.UserBattleChar,
                                TARGET = Target,
                                ABSORB_AMOUNT = AbsorbHealthAmount,
                                String = _("USER_NAME absorbs ABSORB_AMOUNT of TARGET_NAME's health!"))

                            Battle_DealDamage(Target, AbsorbHealthAmount)
                            Battle_RestoreHealth(self.UserBattleChar, AbsorbHealthAmount)

                    if Target.IsAlive:
                        if self.DamageBurn_Mana is not None:
                            Battle_BurnMana(Target, round(ResultDamageValue * self.DamageBurn_Mana))
                        if self.DamageBurn_Energy is not None:
                            Battle_BurnEnergy(Target, round(ResultDamageValue * self.DamageBurn_Energy))

                        if Battle_HasStatusEffect(self.UserBattleChar, "brn_strikes"):
                            BurnStrikesBurnEffect = BattleEffect_ApplyStatusOnEnemy(
                                StatusEffect = BattleStatusEff_Burn(
                                    self.UserBattleChar.Damage, 
                                    Duration = 2, 
                                    SourceName = Battle_GetStatusEffect(self.UserBattleChar, "brn_strikes").SourceName
                                )
                            )
                            BurnStrikesBurnEffect.ApplyEffect(Target)

                        for OnHitEffect in self.Effects_OnHit_Target:
                            OnHitEffect.ApplyEffect(Target)
                        for OnHitEffect in self.Effects_OnHit_User:
                            OnHitEffect.ApplyEffect(self.UserBattleChar)

                        # Evaluates TriggerCounter flag to prevent infinite counterloops
                        if self.TriggerCounter and Battle_HasStatusEffect(Target, "counter"):
                            Battle_ScheduledAttack(Target.Skill_Attack, AttackTarget=self.UserBattleChar, TriggerCounter=False)

                    if not Target.IsAlive:
                        for OnKillEffect in self.Effects_OnKill_User:
                            OnKillEffect.ApplyEffect(self.UserBattleChar)
                else:
                    Battle_AddLogEntry_Autoformat(
                        USER = self.UserBattleChar,
                        TARGET = Target,
                        SKILL_NAME = self.SkillName,
                        String = _("USER_NAME strikes TARGET_NAME with SKILL_NAME and {color=[BATTLE_COLORS_LOG.MISS]}misses!{/color}"))

            Battle_LoopStep(PlayedAnim.Cooldown)