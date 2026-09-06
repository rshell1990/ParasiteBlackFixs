init python:
    # this is the basic, generic "A attack B" 
    # that can be tweaked hard by passing different input data
    # to understand the rest of the battle sys
    # you should read through this entire file
    # most skills (like 90%) lean on this
    class Battle_ScheduledAttack:
        def __init__(self, 
                SourceSkillObj = None,
                DamageMod = 1.0,

                DamageMod_AdditivePerDebuffOnTarget = None,

                # battlechar, list of battlechars or any enum entry from BATTLE_TARGETS
                AttackTarget = None,

                # look for BattleEffect_
                Effects_OnHit_Target =  [],     
                Effects_OnHit_User =    [],     
                Effects_OnKill_User =   [],
                Effects_OnCrit_Target = [],
                Effects_OnCrit_User =   [],

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

                CustomImpactVfxID = None,               # if not none, image ID to place on enemy on impact
                CustomUserVfxID = None,                 # if not none, image ID to place on attacker
                ImpactVfxRandomRotation = False,        # true to randomly rotate impact fx

                SoundImpact_CustomList = None,          # if not None, a list of sounds to randomly choose from on impact. by default, its basic attack impact sound tied to skin. [] to disable
                SoundImpact_OneShotList =   None, # same as above, but only played once (to not earrape with *targets)
                SoundSwing_CustomList = None,           # if not None, a list of sounds to randomly choose from on use
                SoundSwing_DoNotCutOffOnImpact = None,  # if True, on landing the attack the swing sound will not be silenced

                DamageMod_DoubleIfTargetHasAtleastOneDebuff = False,  # if True, the damage mod will be doubled if the target has at least one debuff on them

                AnimID = "attack",
                ):


            self.SkillName = SourceSkillObj.DisplayName
            self.UserBattleChar = SourceSkillObj.Owner_BattleChar
        
            self.DamageMod = DamageMod
            self.DamageMod_AdditivePerDebuffOnTarget = DamageMod_AdditivePerDebuffOnTarget
            self.DamageMod_DoubleIfTargetHasAtleastOneDebuff = DamageMod_DoubleIfTargetHasAtleastOneDebuff

            self.TargetList = Battle_ProcessTargetList(self.UserBattleChar, AttackTarget)

            self.Effects_OnHit_Target = Effects_OnHit_Target
            self.Effects_OnHit_User = Effects_OnHit_User
            self.Effects_OnCrit_Target = Effects_OnCrit_Target    
            self.Effects_OnCrit_User = Effects_OnCrit_User 
            self.Effects_OnKill_User = Effects_OnKill_User   

            self.IgnoreArmor = IgnoreArmor
            self.GuaranteedCrit = GuaranteedCrit
            self.GuaranteedHit = GuaranteedHit

            self.DamageBurn_Mana =   DamageBurn_Mana
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
            for BattleChar in reversed(self.TargetList):
                if not BattleChar.IsAlive:
                    self.TargetList.remove(BattleChar)

            if len(self.TargetList) == 0:
                return

            if self.AnimID in self.UserBattleChar.BattleSkin.AnimsDict:
                PlayedAnim = Battle_RunCharAnim(self.UserBattleChar, self.AnimID)
            else:
                # fall back to attack in case anim missing
                PlayedAnim = Battle_RunCharAnim(self.UserBattleChar, "attack")

            # vocal grunts n roars
            Battle_PlayCharSkinSound("Char_UseSkill", self.UserBattleChar, Voice = True, Chance = 0.25)

            # actual swing sound
            if self.SoundSwing_CustomList:
                # stopgap, auto-grabs silence from anim length
                ExtraSilence = max(PlayedAnim.WarmupTo - 0.05, 0.0)
                Battle_PlaySoundOnBattleChar(renpy.random.choice(self.SoundSwing_CustomList), self.UserBattleChar, Voice = False, ExtraSilence = ExtraSilence)
            else:
                Battle_PlayCharSkinSound("BasicAttack_Swing", self.UserBattleChar)

            # spawn attack vfx
            if self.CustomUserVfxID is not None:
                Battle_SpawnVfxOnChar(self.UserBattleChar, self.CustomUserVfxID, RandomRotation = False, AutoXFlip = False)

            Battle_LoopStep(PlayedAnim.Warmup)

            if self.SoundImpact_OneShotList:
                Battle_PlaySoundOnBattleChar(renpy.random.choice(self.SoundImpact_OneShotList), self.TargetList[0])

            for Target in self.TargetList:
                if Battle_TryLandStrike(self.UserBattleChar, Target, GuaranteedHit = self.GuaranteedHit):
                    # invincibility cancel
                    if Battle_HasStatusEffect(Target, "godmode"):
                        Battle_AddLogEntry_Autoformat(
                            String = tra(_("USER_NAME strikes TARGET_NAME with SKILL_NAME but TARGET_NAME is invincible!")),
                            USER = self.UserBattleChar,
                            TARGET = Target,
                            SKILL_NAME = self.SkillName)
                        return

                    # protect interception
                    if Battle_HasStatusEffect(Target, "protect"):
                        ProtectedBy = Battle_GetStatusEffect(Target, "protect").ProtectedBy
                        Battle_AddLogEntry_Autoformat(
                            String = tra(_("USER_NAME tries to strike TARGET_NAME with SKILL_NAME but PROTECTOR_NAME moves in to protect!!")),
                            USER = self.UserBattleChar,
                            TARGET = Target,
                            PROTECTOR = ProtectedBy,
                            SKILL_NAME = self.SkillName)
                        Target = ProtectedBy
                    
                    if not self.SoundSwing_DoNotCutOffOnImpact and not PlayedAnim.SoundSwing_DoNotCutOffOnImpact:
                        # stop swing sound as hit is landed
                        Battle_StopSoundOnBattleChar(self.UserBattleChar, Fadeout = 0.25)

                    # burning shield effect
                    if Battle_HasStatusEffect(Target, "brn_shield"):
                        Battle_ApplyStatusEffect(
                            TargetChar = self.UserBattleChar, 
                            StatusEffect = BattleStatusEff_Burn(
                                BaseValue =  Target.Damage, 
                                Duration =   3, 
                                SourceName = Battle_GetStatusEffect(Target, "brn_shield").SourceName
                            ), 
                            CastOnEnemy = False
                        )

                    # reflect damage effect
                    if Battle_HasStatusEffect(Target, "reflect_damage"):
                        Battle_DealDamage(self.UserBattleChar, Battle_GetStatusEffect(Target, "reflect_damage").DamageRateFromBaseCharDmg * Target.Damage)

                    # play impact sound
                    if self.SoundImpact_CustomList is not None:
                        if len(self.SoundImpact_CustomList) > 0:
                            Battle_PlaySoundOnBattleChar(renpy.random.choice(self.SoundImpact_CustomList), Target, Voice = False)
                    else:
                        Battle_PlayCharSkinSound("BasicAttack_Impact", self.UserBattleChar, AudioSourceOverride = Target)
                    

                    # spawn impact vfx
                    if self.CustomImpactVfxID is not None:
                        Battle_SpawnVfxOnChar(Target, self.CustomImpactVfxID, RandomRotation = self.ImpactVfxRandomRotation)
                    else:
                        Battle_SpawnVfxOnChar(Target, self.UserBattleChar.BattleSkin.BasicAttackImpactImageID, RandomRotation = self.ImpactVfxRandomRotation)

                    # apply dmgmod if any
                    DmgMod = self.DamageMod
                    if self.DamageMod_AdditivePerDebuffOnTarget is not None:
                        DebuffCountOnTarget = 0
                        for StatusEffect in Target.StatusEffects:
                            if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                                DebuffCountOnTarget += 1
                        DmgMod = DmgMod + (self.DamageMod_AdditivePerDebuffOnTarget * DebuffCountOnTarget)

                    if self.DamageMod_DoubleIfTargetHasAtleastOneDebuff:
                        HasDebuff = False
                        for StatusEffect in Target.StatusEffects:
                            if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                                HasDebuff = True
                                break
                        if HasDebuff:
                            DmgMod *= 2.0

                    # roll dmg
                    TotalStrikeDamage = Battle_BCharDamageRoll(self.UserBattleChar, Mod = DmgMod)

                    # crit handling
                    IsCrit = False
                    if self.GuaranteedCrit:
                        IsCrit = True
                    else:
                        CritChance = self.UserBattleChar.CritChance
                        if self.ExtraCritChancePercentage is not None:
                            CritChance += self.ExtraCritChancePercentage
                        CritRoll = renpy.random.randint(1, 100)
                        if CritRoll <= CritChance:
                            IsCrit = True

                    if IsCrit:
                        TotalStrikeDamage = int(TotalStrikeDamage * 2)
                        for OnCritEffect in self.Effects_OnCrit_Target:
                            OnCritEffect.ApplyEffect(Target)
                        for OnCritEffect in self.Effects_OnCrit_User:
                            OnCritEffect.ApplyEffect(self.UserBattleChar)

                    # inc dmg modifier
                    TargetDamageMod = Battle_GetIncomingDamageMod(Target)
                    ResultDamageValue = round(TotalStrikeDamage * TargetDamageMod)

                    # armor
                    if not self.IgnoreArmor:
                        ResultDamageValue = Battle_GetArmorDamageReduction(ResultDamageValue, Target)

                    # logging
                    if IsCrit:
                        Battle_AddLogEntry_Autoformat(
                            USER = self.UserBattleChar,
                            TARGET = Target,
                            SKILL_NAME = self.SkillName,
                            DAMAGE_AMOUNT = ResultDamageValue,
                            String = tra(_("USER_NAME lands a {color=[BATTLE_COLORS_LOG.CRITICAL]}critical strike{/color} on TARGET_NAME with SKILL_NAME dealing DAMAGE_AMOUNT {color=[BATTLE_COLORS_LOG.DAMAGE]}damage!{/color}")))
                    else:
                        Battle_AddLogEntry_Autoformat(
                            USER = self.UserBattleChar,
                            TARGET = Target,
                            SKILL_NAME = self.SkillName,
                            DAMAGE_AMOUNT = ResultDamageValue,
                            String = tra(_("USER_NAME strikes TARGET_NAME with SKILL_NAME dealing DAMAGE_AMOUNT {color=[BATTLE_COLORS_LOG.DAMAGE]}damage!{/color}")))

                    # deal dmg          
                    Battle_DealDamage(Target, ResultDamageValue, IgnoreArmor = True, IsCrit = IsCrit)

                    # absorb
                    if self.DamageRecoversAttackerEnergy is not None:
                        Battle_RestoreEnergy(self.UserBattleChar, round(ResultDamageValue * self.DamageRecoversAttackerEnergy))
                    if self.DamageRecoversAttackerHealth is not None:
                        Battle_RestoreHealth(self.UserBattleChar, round(ResultDamageValue * self.DamageRecoversAttackerHealth))

                    # max health absorb
                    if Target.IsAlive:
                        if self.AbsorbTarget_HealthMax is not None:
                            AbsorbHealthAmount = min(round(self.AbsorbTarget_HealthMax * Target.HealthMax), Target.Health)
                            if AbsorbHealthAmount > 0:
                                Battle_AddLogEntry_Autoformat(
                                    USER = self.UserBattleChar,
                                    TARGET = Target,
                                    ABSORB_AMOUNT = AbsorbHealthAmount,
                                    String = tra(_("USER_NAME absorbs ABSORB_AMOUNT of TARGET_NAME's health!")))

                                Battle_DealDamage(Target, AbsorbHealthAmount)
                                Battle_RestoreHealth(self.UserBattleChar, AbsorbHealthAmount)

                    # if theyre alive, burn mana/energy and do var. on-hits
                    if Target.IsAlive:
                        if self.DamageBurn_Mana is not None:
                            Battle_BurnMana(Target, round(ResultDamageValue * self.DamageBurn_Mana))
                        if self.DamageBurn_Energy is not None:
                            Battle_BurnEnergy(Target, round(ResultDamageValue * self.DamageBurn_Energy))

                        # burning strike effect
                        if Battle_HasStatusEffect(self.UserBattleChar, "brn_strikes"):
                            BurnStrikesBurnEffect = BattleEffect_ApplyStatusOnEnemy(
                                StatusEffect = BattleStatusEff_Burn(
                                    self.UserBattleChar.Damage, 
                                    Duration = 2, 
                                    SourceName = Battle_GetStatusEffect(
                                        self.UserBattleChar, "brn_strikes").SourceName
                                )
                            )
                            BurnStrikesBurnEffect.ApplyEffect(Target)

                        for OnHitEffect in self.Effects_OnHit_Target:
                            OnHitEffect.ApplyEffect(Target)
                        for OnHitEffect in self.Effects_OnHit_User:
                            OnHitEffect.ApplyEffect(self.UserBattleChar)

                        if Battle_HasStatusEffect(Target, "counter"):
                            Battle_ScheduledAttack(Target.Skill_Attack, AttackTarget = self.UserBattleChar, TriggerCounter = False)

                    if not Target.IsAlive:
                        for OnKillEffect in self.Effects_OnKill_User:
                            OnKillEffect.ApplyEffect(self.UserBattleChar)
                else:
                    Battle_AddLogEntry_Autoformat(
                        USER = self.UserBattleChar,
                        TARGET = Target,
                        SKILL_NAME = self.SkillName,
                        String = tra(_("USER_NAME strikes TARGET_NAME with SKILL_NAME and {color=[BATTLE_COLORS_LOG.MISS]}misses!{/color}")))

            Battle_LoopStep(PlayedAnim.Cooldown)
            return

    