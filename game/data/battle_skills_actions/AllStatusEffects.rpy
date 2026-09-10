init 2 python:
    # cheat sheet of hard-coded stat eff ids.
    # stat effs such as DamageIn have varied status effect ID based on their causing skill.
    # bleed/poison/burn :: lose hp per turn
    # godmode           :: invincibility, attacks cant hit char
    # immunity          :: cant recieve debuffs
    # curse             :: cant recieve buffs
    # willpower         :: hp cant go below 1
    # counter           :: strike back with basic attack if attacked
    # taunt             :: attack single char with basic attacks only
    # protect           :: attacks against char will be redirected to their protector
    # stun              :: cant act
    # brn_strikes       :: apply burn on each attack
    # brn_shield        :: apply burn on being attacked

    # ignore effect of sched. attack
    class BattleStatusEff_Invincibility(BattleStatusEff):
        def __init__(self, Duration, SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = "godmode", SourceName = SourceName)
            self.EffectName = _("Invincibility")
            self.Icon = "images/battle_status_eff_icons/Godmode.webp"

        def GetDesc(self):
            return tra(_("This character cannot be damaged by any attack."))
######################################################################
    # alter incoming damage modifier in %
    class BattleStatusEff_DamageIn(BattleStatusEff):
        def __init__(self, DamageRecieved_Mod, Duration, SourceName = None, StatusEffectID = "damage_res"):
            super().__init__(Duration = Duration, StatusEffectID = StatusEffectID, SourceName = SourceName)
            if DamageRecieved_Mod > 1.0:
                self.EffectName = _("Damage resistance debuff")
                self.Icon = "images/battle_status_eff_icons/DamageInDebuff.webp"
                self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF
            else:
                self.EffectName = _("Damage resistance buff")
                self.Icon = "images/battle_status_eff_icons/DamageInBuff.webp"

            ##################################################
            self.DamageRecieved_Mod = DamageRecieved_Mod

        def GetDesc(self):
            if self.DamageRecieved_Mod > 1.0:
                DamagePercentage = round((self.DamageRecieved_Mod - 1.0) * 100)
                return tra(_("Damage resistance lowered by %s%%")) % DamagePercentage
            else:
                DamagePercentage = round((1.0 - self.DamageRecieved_Mod) * 100)
                return tra(_("Damage resistance increased by %s%%")) % DamagePercentage

        def IsBetterThanAnotherEffect(self, Other):
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                if self.DamageRecieved_Mod <= Other.DamageRecieved_Mod:
                    return True
                else:
                    return False
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                if self.DamageRecieved_Mod >= Other.DamageRecieved_Mod:
                    return True
                else:
                    return False

######################################################################
    # alter outgoing damage modifier in %
    class BattleStatusEff_DamageOut(BattleStatusEff):
        def __init__(self, DamageDealt_Mod, Duration, SourceName = None, StatusEffectID = "damage_dealt"):
            super().__init__(Duration = Duration, StatusEffectID = StatusEffectID, SourceName = SourceName)

            if DamageDealt_Mod > 1.0:
                self.EffectName = _("Damage buff")
                self.Icon = "images/battle_status_eff_icons/DamageOutBuff.webp"

            else:
                self.EffectName = _("Damage debuff")
                self.Icon = "images/battle_status_eff_icons/DamageOutDebuff.webp"

            if DamageDealt_Mod < 1.0:
                self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF

            ##################################################
            self.DamageDealt_Mod = DamageDealt_Mod

        def GetDesc(self):
            if self.DamageDealt_Mod > 1.0:
                DamagePercentage = round((self.DamageDealt_Mod - 1.0) * 100)
                return tra(_("Damage dealt increased by %s%%")) % DamagePercentage
            else:
                DamagePercentage = round((1.0 - self.DamageDealt_Mod) * 100)
                return tra(_("Damage dealt lowered by %s%%")) % DamagePercentage

        def IsBetterThanAnotherEffect(self, Other):
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                if self.DamageDealt_Mod >= Other.DamageDealt_Mod:
                    return True
                else:
                    return False
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                if self.DamageDealt_Mod <= Other.DamageDealt_Mod:
                    return True
                else:
                    return False
######################################################################
    # do damage each turn
    class BattleStatusEff_Bleed(BattleStatusEff):
        def __init__(self, BaseValue, Duration, SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = "bleed", SourceName = SourceName)

            self.EffectName = _("Bleeding")

            self.Icon = "images/battle_status_eff_icons/Bleed.webp"
            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF
            self.StackingMethod = BATTLE_STATUS_EFFECT_STACKING.ADD_AS_NEW
            ##################################################
            self.Value = max(round(BaseValue * 0.15), 1)

            self.TickOn_Ally = 1

        def GetDesc(self):
            return tra(_("Each turn the character suffers %s damage.")) % self.Value

        def OnTurnStart(self):
            Battle_AddLogEntry_Autoformat(
                String = tra(_("TARGET_NAME suffers BLEED_DAMAGE_AMOUNT {color=[BATTLE_COLORS_LOG.DAMAGE_BLEED]}bleed damage!{/color}")),
                TARGET = self.Owner_BattleChar,
                BLEED_DAMAGE_AMOUNT = self.Value)

            Battle_PlaySoundOnBattleChar(renpy.random.choice(soundLib["Battle_StatEff_Bleed"]), self.Owner_BattleChar, Voice = False, ExtraSilence = 0.0, RelVolume = 0.6)
            Battle_DealDamage(self.Owner_BattleChar, self.Value, IgnoreArmor = True, FloatingTextKind = 5)
            return
######################################################################
    # do damage each turn
    class BattleStatusEff_Poison(BattleStatusEff):
        def __init__(self, BaseValue, Duration, SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = "poisondot", SourceName = SourceName)

            self.EffectName = _("Poisoned")

            self.Icon = "images/battle_status_eff_icons/Poison.webp"
            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF
            self.StackingMethod = BATTLE_STATUS_EFFECT_STACKING.ADD_AS_NEW
            ##################################################
            self.Value = max(round(BaseValue * 0.15), 1)

            self.TickOn_Ally = 1

        def GetDesc(self):
            return tra(_("Each turn the character suffers %s damage.")) % self.Value

        def OnTurnStart(self):
            Battle_AddLogEntry_Autoformat(
                String = tra(_("TARGET_NAME suffers POISON_DAMAGE_AMOUNT {color=[BATTLE_COLORS_LOG.DAMAGE_POISON]}poison damage!{/color}")),
                TARGET = self.Owner_BattleChar,
                POISON_DAMAGE_AMOUNT = self.Value)
            
            Battle_PlaySoundOnBattleChar(renpy.random.choice(soundLib["Battle_StatEff_Poison"]), self.Owner_BattleChar, Voice = False, ExtraSilence = 0.0, RelVolume = 0.45)
            Battle_DealDamage(self.Owner_BattleChar, self.Value, IgnoreArmor = True, FloatingTextKind = 4)
            return
######################################################################
    # do damage each turn
    class BattleStatusEff_Burn(BattleStatusEff):
        def __init__(self, BaseValue, Duration, SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = "burn", SourceName = SourceName)

            self.EffectName = _("Burn")

            self.Icon = "images/battle_status_eff_icons/Burn.webp"
            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF
            self.StackingMethod = BATTLE_STATUS_EFFECT_STACKING.ADD_AS_NEW
            ##################################################
            self.Value = max(round(BaseValue * 0.15), 1)

            self.TickOn_Ally = 1

        def GetDesc(self):
            return tra(_("Each turn the character suffers %s damage.")) % self.Value

        def OnTurnStart(self):
            Battle_AddLogEntry_Autoformat(
                String = tra(_("TARGET_NAME suffers BURN_DAMAGE_AMOUNT {color=[BATTLE_COLORS_LOG.DAMAGE_BURN]}burn damage!{/color}")),
                TARGET = self.Owner_BattleChar,
                BURN_DAMAGE_AMOUNT = self.Value)

            Battle_PlaySoundOnBattleChar(renpy.random.choice(soundLib["Battle_FireStrikes"]), self.Owner_BattleChar, Voice = False, ExtraSilence = 0.0, RelVolume = 0.3)
            Battle_DealDamage(self.Owner_BattleChar, self.Value, IgnoreArmor = True, FloatingTextKind = 3)
            return
######################################################################
    # provoke char to only basic attack a single enemy for duration
    class BattleStatusEff_Taunt(BattleStatusEff):
        def __init__(self, Duration, SourceName = None, TauntedBy = None):
            Assert(TauntedBy is not None, "Taunt must have a taunted-by char ref set")
            super().__init__(Duration = Duration, StatusEffectID = "taunt", SourceName = SourceName)
            self.Icon = "images/battle_status_eff_icons/Taunt.webp"
            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF

            self.EffectName = _("Taunt")

            self.TickOn_Ally = 1

            ##################################################
            self.TauntedBy = TauntedBy

        def GetDesc(self):
            return tra(_("Taunted character will attack it's target (%s) with basic attacks only for the duration of the effect.")) % self.TauntedBy.CharRef["name"]

        def OnTurnStart(self):
            if not self.TauntedBy.IsAlive:
                Battle_RemoveStatusEffect(self.Owner_BattleChar, "taunt") # isnt this suicidal
            return
######################################################################
    # char under curse cant recieve buffs
    class BattleStatusEff_Curse(BattleStatusEff):
        def __init__(self, Duration, SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = "curse", SourceName = SourceName)
            self.Icon = "images/battle_status_eff_icons/Curse.webp"
            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF

            self.EffectName = _("Cursed")

        def GetDesc(self):
            return tra(_("Cursed character cannot recieve any buffs."))

    # strike back
    class BattleStatusEff_Counter(BattleStatusEff):
        def __init__(self, Duration, SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = "counter", SourceName = SourceName)
            self.Icon = "images/battle_status_eff_icons/Counter.webp"
            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.BUFF

            self.EffectName = _("Counter")


        def GetDesc(self):
            return tra(_("Character will counter attack against any damaging ability with their basic attack."))
######################################################################
    # mc and markus
    class BattleStatusEff_TransformedPara(BattleStatusEff):
        def __init__(self, Duration = -1):
            super().__init__(Duration = Duration, StatusEffectID = "transformed_para")
            self.Icon = "images/battle_status_eff_icons/Transform.webp"
            self.EffectName = _("Parasite Form")

            self.AttrMod_StrengthMul = 1.5
            self.AttrMod_EnduranceMul = 1.5
            self.AttrMod_WillpowerMul = 1.5
            self.AttrMod_AgilityMul = 1.5
            self.AttrMod_DexterityMul = 1.5
            self.AttrMod_LuckMul = 1.5

            self.Permanent = True

            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.NEUTRAL

        def GetDesc(self):
            return tra(_("All the character's attributes are increased by 50%."))
######################################################################
    # elena
    class BattleStatusEff_TransformedWolf(BattleStatusEff):
        def __init__(self):
            super().__init__(Duration = -1, StatusEffectID = "transformed_wolf")
            self.Icon = "images/battle_status_eff_icons/Transform.webp"
            self.EffectName = _("Wolf Form")

            self.AttrMod_StrengthMul = 1.5
            self.AttrMod_EnduranceMul = 0.75
            self.AttrMod_AgilityMul = 1.5

            self.Permanent = True

            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.NEUTRAL

        def GetDesc(self):
            return tra(_("In wolf form, Elena's strength and agility are increased by 50%, but her endurance is reduced by 25%."))
######################################################################
    # Kiara
    class BattleStatusEff_TransformedDemorai(BattleStatusEff):
        def __init__(self):
            super().__init__(Duration = -1, StatusEffectID = "transformed_demorai")
            self.Icon = "images/battle_status_eff_icons/Transform.webp"
            self.EffectName = _("Demorai Form")

            self.AttrMod_AgilityMul = 1.5

            self.Permanent = True

            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.NEUTRAL

        def GetDesc(self):
            return tra(_("In demorai form, Kiara's agility is increased by 50%."))
######################################################################
    # buff dodge
    class BattleStatusEff_StatMod_Dodge(BattleStatusEff):
        def __init__(self, Duration, StatMod_DodgeRating = 1.0, StatusEffectID = "dodge_mod", SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = StatusEffectID, SourceName = SourceName)
            self.StatMod_DodgeRating = StatMod_DodgeRating
            if StatMod_DodgeRating > 1.0:
                self.Icon = "images/battle_status_eff_icons/DodgeBuff.webp"
                self.EffectName = _("Dodge Rating buff")
            else:
                self.Icon = "images/battle_status_eff_icons/DodgeDebuff.webp"
                self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF
                self.EffectName = _("Dodge Rating debuff")

        def IsBetterThanAnotherEffect(self, Other):
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                if self.StatMod_DodgeRating >= Other.StatMod_DodgeRating:
                    return True
                else:
                    return False
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                if self.StatMod_DodgeRating <= Other.StatMod_DodgeRating:
                    return True
                else:
                    return False

        def GetDesc(self):
            if self.StatMod_DodgeRating > 1.0:
                EffectPercentage = round((self.StatMod_DodgeRating - 1.0) * 100)
                return tra(_("The character's Dodge Rating is increased by %s%%")) % EffectPercentage
            else:
                EffectPercentage = round((1.0 - self.StatMod_DodgeRating) * 100)
                return tra(_("The character's Dodge Rating is decreased by %s%%")) % EffectPercentage
######################################################################
    # buff acc
    class BattleStatusEff_StatMod_Accuracy(BattleStatusEff):
        def __init__(self, Duration, StatMod_AttackRating = 1.0, StatusEffectID = "acc_mod", SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = StatusEffectID, SourceName = SourceName)
            self.StatMod_AttackRating = StatMod_AttackRating

            if StatMod_AttackRating > 1.0:
                self.Icon = "images/battle_status_eff_icons/AttackRatingBuff.webp"
                self.EffectName = _("Attack Rating buff")
            else:
                self.Icon = "images/battle_status_eff_icons/AttackRatingDebuff.webp"
                self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF
                self.EffectName = _("Attack Rating debuff")

        def GetDesc(self):
            if self.StatMod_AttackRating > 1.0:
                EffectPercentage = round((self.StatMod_AttackRating - 1.0) * 100)
                return tra(_("The character's Attack Rating is increased by %s%%")) % EffectPercentage
            else:
                EffectPercentage = round((1.0 - self.StatMod_AttackRating) * 100)
                return tra(_("The character's Attack Rating is decreased by %s%%")) % EffectPercentage

        def IsBetterThanAnotherEffect(self, Other):
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                if self.StatMod_AttackRating >= Other.StatMod_AttackRating:
                    return True
                else:
                    return False
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                if self.StatMod_AttackRating <= Other.StatMod_AttackRating:
                    return True
                else:
                    return False
######################################################################
    # raise crit chance
    class BattleStatusEff_StatMod_CritChance(BattleStatusEff):
        def __init__(self, Duration, StatMod_CritChance = 1.0, StatusEffectID = "critchance_mod", SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = StatusEffectID, SourceName = SourceName)
            self.StatMod_CritChance = StatMod_CritChance

            if StatMod_CritChance > 1.0:
                self.Icon = "images/battle_status_eff_icons/CritBuff.webp"
                self.EffectName = _("Crit Chance buff")
            else:
                self.Icon = "images/battle_status_eff_icons/CritDebuff.webp"
                self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF
                self.EffectName = _("Crit Chance debuff")

        def GetDesc(self):
            if self.StatMod_CritChance > 1.0:
                EffectPercentage = round((self.StatMod_CritChance - 1.0) * 100)
                return tra(_("The character's Crit Chance is increased by %s%%")) % EffectPercentage
            else:
                EffectPercentage = round((1.0 - self.StatMod_CritChance) * 100)
                return tra(_("The character's Crit Chance is decreased by %s%%")) % EffectPercentage

        def IsBetterThanAnotherEffect(self, Other):
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                if self.StatMod_CritChance >= Other.StatMod_CritChance:
                    return True
                else:
                    return False
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                if self.StatMod_CritChance <= Other.StatMod_CritChance:
                    return True
                else:
                    return False
######################################################################
    class BattleStatusEff_StatMod_Armor(BattleStatusEff):
        def __init__(self, Duration, StatMod_Armor = 1.0, StatusEffectID = "armor_mod", SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = StatusEffectID, SourceName = SourceName)
            self.StatMod_Armor = StatMod_Armor

            if StatMod_Armor > 1.0:
                self.Icon = "images/battle_status_eff_icons/ArmorBuff.webp"
                self.EffectName = _("Armor buff")
            else:
                self.Icon = "images/battle_status_eff_icons/ArmorDebuff.webp"
                self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF
                self.EffectName = _("Armor debuff")

        def GetDesc(self):
            if self.StatMod_Armor > 1.0:
                EffectPercentage = round((self.StatMod_Armor - 1.0) * 100)
                return tra(_("The character's Armor is increased by %s%%")) % EffectPercentage
            else:
                EffectPercentage = round((1.0 - self.StatMod_Armor) * 100)
                return tra(_("The character's Armor is decreased by %s%%")) % EffectPercentage

        def IsBetterThanAnotherEffect(self, Other):
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                if self.StatMod_Armor >= Other.StatMod_Armor:
                    return True
                else:
                    return False
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                if self.StatMod_Armor <= Other.StatMod_Armor:
                    return True
                else:
                    return False
######################################################################
    # protect char redirecting all ScheduledAttacks made against them on yourself
    class BattleStatusEff_Protected(BattleStatusEff):
        def __init__(self, Duration, SourceName = None, ProtectedBy = None, AllowMultiple = False):
            Assert(ProtectedBy is not None, "Protected must have a ProtectedBy char ref set")
            super().__init__(Duration = Duration, StatusEffectID = "protect", SourceName = SourceName)
            self.Icon = "images/battle_status_eff_icons/Protect.webp"
            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.BUFF

            self.AllowMultiple = AllowMultiple

            self.EffectName = _("Protected")
            ##################################################
            self.ProtectedBy = ProtectedBy

        def GetDesc(self):
            return tra(_("Any attack made against a protected character will be redirected towards %s.")) % self.ProtectedBy.CharRef["name"]
######################################################################
    # cannot accept debuffs
    class BattleStatusEff_Immunity(BattleStatusEff):
        def __init__(self, Duration, SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = "immunity", SourceName = SourceName)
            self.Icon = "images/battle_status_eff_icons/Immunity.webp"
            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.BUFF

            self.EffectName = _("Immune")

        def GetDesc(self):
            return tra(_("Negative status effects will not be applied to this character as long as they are immune."))
######################################################################
    # hp cant get below 1 (cant die)
    class BattleStatusEff_Willpower(BattleStatusEff):
        def __init__(self, Duration, SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = "willpower", SourceName = SourceName)
            self.Icon = "images/battle_status_eff_icons/Will.webp"
            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.BUFF

            self.EffectName = _("Willpower")

        def GetDesc(self):
            return tra(_("Health points of this character can never go below 1."))
######################################################################
    # alter health recovery
    class BattleStatusEff_HealthRecoveryMod(BattleStatusEff):
        def __init__(self, ResRecoverMod_Health, Duration, SourceName = None, StatusEffectID = "health_recovery"):
            super().__init__(Duration = Duration, StatusEffectID = StatusEffectID, SourceName = SourceName)
            if ResRecoverMod_Health < 1.0:
                self.EffectName = _("Health regained debuff")
                self.Icon = "images/battle_status_eff_icons/RecoverDebuff.webp"
                self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF
            else:
                self.EffectName = _("Health regained buff")
                self.Icon = "images/battle_status_eff_icons/RecoverBuff.webp"
            ##################################################
            self.ResRecoverMod_Health = ResRecoverMod_Health

        def GetDesc(self):
            if self.ResRecoverMod_Health < 1.0:
                HealthRecoveryPercentage = round((1.0 - self.ResRecoverMod_Health) * 100)
                return tra(_("Health recovered from any sources is lowered by %s%%")) % HealthRecoveryPercentage
            else:
                HealthRecoveryPercentage = round((self.ResRecoverMod_Health - 1.0) * 100)
                return tra(_("Health recovered from any sources is raised by %s%%")) % HealthRecoveryPercentage

        def IsBetterThanAnotherEffect(self, Other):
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                if self.ResRecoverMod_Health >= Other.ResRecoverMod_Health:
                    return True
                else:
                    return False
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                if self.ResRecoverMod_Health <= Other.ResRecoverMod_Health:
                    return True
                else:
                    return False
######################################################################
    # alter energy recovery
    class BattleStatusEff_EnergyRecoveryMod(BattleStatusEff):
        def __init__(self, ResRecoverMod_Energy, Duration, SourceName = None, StatusEffectID = "energy_recovery"):
            super().__init__(Duration = Duration, StatusEffectID = StatusEffectID, SourceName = SourceName)
            if ResRecoverMod_Energy < 1.0:
                self.EffectName = _("Energy regained debuff")
                self.Icon = "images/battle_status_eff_icons/RecoverDebuff.webp"
                self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF
            else:
                self.EffectName = _("Energy regained buff")
                self.Icon = "images/battle_status_eff_icons/RecoverBuff.webp"
            ##################################################
            self.ResRecoverMod_Energy = ResRecoverMod_Energy

        def GetDesc(self):
            if self.ResRecoverMod_Energy < 1.0:
                EnergyRecoveryPercentage = round((1.0 - self.ResRecoverMod_Energy) * 100)
                return tra(_("Energy recovered from any sources is lowered by %s%%")) % EnergyRecoveryPercentage
            else:
                EnergyRecoveryPercentage = round((self.ResRecoverMod_Energy - 1.0) * 100)
                return tra(_("Energy recovered from any sources is raised by %s%%")) % EnergyRecoveryPercentage

        def IsBetterThanAnotherEffect(self, Other):
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                if self.ResRecoverMod_Energy >= Other.ResRecoverMod_Energy:
                    return True
                else:
                    return False
            if self.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                if self.ResRecoverMod_Energy <= Other.ResRecoverMod_Energy:
                    return True
                else:
                    return False
######################################################################
    # stunned char skips turn
    class BattleStatusEff_Stun(BattleStatusEff):
        def __init__(self, Duration, SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = "stun", SourceName = SourceName)
            self.Icon = "images/battle_status_eff_icons/Stun.webp"
            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF

            self.EffectName = _("Stun")
            ##################################################

        def GetDesc(self):
            return tra(_("Stunned character is unable to act."))
######################################################################
    # restore X hp per turn
    class BattleStatusEff_RegenHealth(BattleStatusEff):
        def __init__(self, Duration, RestoreVal = 0, RatioFromMax = False, SourceName = None, StatusEffectID = "health_regen"):
            super().__init__(Duration = Duration, StatusEffectID = StatusEffectID, SourceName = SourceName)
            self.Icon = "images/battle_status_eff_icons/Regen.webp"
            self.RestoreVal = RestoreVal
            self.RatioFromMax = RatioFromMax

            self.EffectName = _("Healing")

            self.TickOn_Enemy = 0
            ##################################################

        def OnTurnStart(self):
            if self.RatioFromMax:
                Battle_RestoreHealth(self.Owner_BattleChar, round((self.RestoreVal * self.Owner_BattleChar.HealthMax) * Battle_GetHealthRecoveryMod(self.Owner_BattleChar)))
            else:
                Battle_RestoreHealth(self.Owner_BattleChar, round((self.RestoreVal * Battle_GetHealthRecoveryMod(self.Owner_BattleChar))))
            return

        def GetDesc(self):
            if self.RatioFromMax:
                HealthRecovered = round(self.RestoreVal * self.Owner_BattleChar.HealthMax * Battle_GetHealthRecoveryMod(self.Owner_BattleChar))
            else:
                HealthRecovered = round(self.RestoreVal * Battle_GetHealthRecoveryMod(self.Owner_BattleChar))
            return tra(_("This character will recover %s health per turn.")) % HealthRecovered

        def IsBetterThanAnotherEffect(self, Other):
            # warning this assumes that heals with same ID have same ratiofrommax setting
            if self.RestoreVal >= Other.RestoreVal:
                return True
            else:
                return False
######################################################################
    # raza seed
    class BattleStatusEff_RazaSeed(BattleStatusEff):
        def __init__(self):
            super().__init__(Duration = -1, StatusEffectID = "raza_seed")
            self.Icon = "images/battle_skill_icons/parawhite/AllForOne.webp"
            self.EffectName = _("Raza")
            self.Permanent = True

            self.AttrMod_StrengthAdd = 1
            self.AttrMod_EnduranceAdd = 1
            self.AttrMod_DexterityAdd = -2

            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.NEUTRAL

        def GetDesc(self):
            return tra(_("The character's endurance and strength are increased by 1, but dexterity is lowered by 2."))
######################################################################
    # burning strikes, makes attack apply burn based on char's attack dmg
    class BattleStatusEff_BurningStrikes(BattleStatusEff):
        def __init__(self, Duration, SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = "brn_strikes", SourceName = SourceName)
            self.Icon = "images/battle_status_eff_icons/Burn.webp"
            self.EffectName = _("Burning Strikes")
            self.StackingMethod = BATTLE_STATUS_EFFECT_STACKING.REPLACE

            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.BUFF

        def GetDesc(self):
            return tra(_("All character's melee attacks will cause a burning status effect."))
######################################################################
    # burning shield, makes any attack done againbst this guy apply burn to attacker
    class BattleStatusEff_BurningShield(BattleStatusEff):
        def __init__(self, Duration, SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = "brn_shield", SourceName = SourceName)
            self.Icon = "images/battle_status_eff_icons/Burn.webp"
            self.EffectName = _("Burning Shield")
            self.StackingMethod = BATTLE_STATUS_EFFECT_STACKING.REPLACE

            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.BUFF

        def GetDesc(self):
            return tra(_("Attacks made against this character will cause a burn status effect to be applied to the attacker."))
######################################################################
    # reflect damage, deals damage to attacker on being struck
    class BattleStatusEff_ReflectDamage(BattleStatusEff):
        def __init__(self, Duration, DamageRateFromBaseCharDmg = 0.1, SourceName = None):
            super().__init__(Duration = Duration, StatusEffectID = "reflect_damage", SourceName = SourceName)
            self.DamageRateFromBaseCharDmg = DamageRateFromBaseCharDmg

            self.Icon = "images/battle_status_eff_icons/ArmorBuff.webp"
            self.EffectName = _("Reflect Damage")
            self.StackingMethod = BATTLE_STATUS_EFFECT_STACKING.REPLACE

            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.BUFF

        def GetDesc(self):
            return tra(_("Attacks made against this character will damage the attacker for %s%% of this character's base damage.")) % int(self.DamageRateFromBaseCharDmg * 100)
######################################################################
    # restore X hp OF CURRENT per turn, forever
    # (its a copy of regenhealth for the most part)
    # (for faymore items)
    class BattleStatusEff_RegenHealthCurrPermanent(BattleStatusEff):
        def __init__(self, RestoreVal = 0, SourceName = None, StatusEffectID = "health_regen_curr_perma"):
            super().__init__(Duration = -1, StatusEffectID = StatusEffectID, SourceName = SourceName)
            self.Icon = "images/battle_status_eff_icons/Regen.webp"
            self.RestoreVal = RestoreVal

            self.Permanent = True

            self.EffectName = _("Healing")

            self.TickOn_Enemy = 0
            ##################################################

        def OnTurnStart(self):
            Battle_RestoreHealth(self.Owner_BattleChar, math.ceil((self.RestoreVal * self.Owner_BattleChar.Health) * Battle_GetHealthRecoveryMod(self.Owner_BattleChar)))
            return

        def GetDesc(self):
            HealthRecovered = math.ceil((self.RestoreVal * self.Owner_BattleChar.Health) * Battle_GetHealthRecoveryMod(self.Owner_BattleChar))
            return tra(_("This character will recover %s health per turn.")) % HealthRecovered

        def IsBetterThanAnotherEffect(self, Other):
            # warning this assumes that heals with same ID have same ratiofrommax setting
            if self.RestoreVal >= Other.RestoreVal:
                return True
            else:
                return False