init python:
    class BattleEffect_ReplaceRandomEnemyBuffWithStatusEff:
        def __init__(self, Chance = 1.0, StatusEffect = None):
            Assert(StatusEffect != None, "BattleEffect_ReplaceRandomEnemyBuffWithStatusEff must have a StatusEffect instance passed in")
            self.Chance = Chance
            self.StatusEffect = StatusEffect

        def ApplyEffect(self, Target):
            if self.Chance != 1.0:
                if RngFloat(0, 1) > self.Chance:
                    return

            Buffs = []
            for StatusEffect in Target.StatusEffects:
                if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                    Buffs.append(StatusEffect)

            BuffToRemove = None
            if len(Buffs) > 0:
                BuffToRemove = renpy.random.choice(Buffs)
                Target.StatusEffects.remove(BuffToRemove)
            
            if BuffToRemove is not None:
                Battle_ApplyStatusEffect(Target, copy.deepcopy(self.StatusEffect), CastOnEnemy = True)
            return

############# it is important to distinguish these two between OnEnemy and OnAlly for status effect duration numbers
    class BattleEffect_ApplyStatusOnEnemy:
        def __init__(self, Chance = 1.0, StatusEffect = None, OnZeroEnergyOnly = False, IfHealthBelowOrEq = 1.0, IfHealthAboveOrEq = 0.0, IfWillpowerLowerThanValue = None):
            Assert(StatusEffect != None, "BattleEffect_ApplyStatusOnEnemy must have a StatusEffect instance passed in")
            self.Chance = Chance
            self.StatusEffect = StatusEffect
            self.OnZeroEnergyOnly = OnZeroEnergyOnly

            self.IfHealthBelowOrEq = IfHealthBelowOrEq
            self.IfHealthAboveOrEq = IfHealthAboveOrEq

            self.IfWillpowerLowerThanValue = IfWillpowerLowerThanValue

        def ApplyEffect(self, Target):
            if self.Chance != 1.0:
                if RngFloat(0, 1) > self.Chance:
                    return
            if self.OnZeroEnergyOnly:
                if Target.Energy > 0:
                    return
            if (Target.Health / Target.HealthMax) > self.IfHealthBelowOrEq:
                return
            if (Target.Health / Target.HealthMax) < self.IfHealthAboveOrEq:
                return
            if self.IfWillpowerLowerThanValue is not None:
                if Target.Willpower >= self.IfWillpowerLowerThanValue:
                    return

            NewStatEff = copy.deepcopy(self.StatusEffect)
            if self.StatusEffect.StatusEffectID == "taunt":
                NewStatEff.TauntedBy = self.StatusEffect.TauntedBy

            Battle_ApplyStatusEffect(Target, NewStatEff, CastOnEnemy = True)
            return

    class BattleEffect_ApplyStatusOnAlly:
        def __init__(self, Chance = 1.0, StatusEffect = None):
            Assert(StatusEffect != None, "BattleEffect_ApplyStatusOnAlly must have a StatusEffect instance passed in")
            self.Chance = Chance
            self.StatusEffect = StatusEffect

        def ApplyEffect(self, Target):
            if self.Chance != 1.0:
                if RngFloat(0, 1) > self.Chance:
                    return

            NewStatEff = copy.deepcopy(self.StatusEffect)
            if self.StatusEffect.StatusEffectID == "protect":
                NewStatEff.ProtectedBy = self.StatusEffect.ProtectedBy
            Battle_ApplyStatusEffect(Target, NewStatEff)
#############################
#Madness for good or bad        
        def Execute(self, Target):
            Caster = self.Owner_BattleChar
            Duration = self.DurationByLevel[self.Level]
            ErraticChance = self.ErraticChanceByLevel[self.Level]

            # Replace with your engine's status application function
            Battle_ApplyStatusEffect(Target, "madness", Duration, ErraticChance)
            return

########################
    # this is more like a wrapper for sanity, to have "grant another turn" as cast/attack effect
    class BattleEffect_GrantExtraTurn:
        def __init__(self, Chance = 1.0, OnlyIfHasActed = False, IgnoreDebuffs = False):
            self.Chance = Chance
            self.OnlyIfHasActed = OnlyIfHasActed
            self.IgnoreDebuffs = IgnoreDebuffs

        def ApplyEffect(self, Target):
            if self.Chance != 1.0:
                if RngFloat(0, 1) > self.Chance:
                    return
            Battle_GrantExtraTurn(Target, OnlyIfHasActed = self.OnlyIfHasActed, IgnoreDebuffs = self.IgnoreDebuffs)

########################
    class BattleEffect_RemoveBuffsOnTarget:
        def __init__(self, Chance = 1.0):
            self.Chance = Chance

        def ApplyEffect(self, Target):
            if self.Chance != 1.0:
                if RngFloat(0, 1) > self.Chance:
                    return
            for StatusEffect in reversed(Target.StatusEffects):
                if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                    Target.StatusEffects.remove(StatusEffect)

    class BattleEffect_RemoveBuffsOnEnemyAndStunIfRemovedAny:
        def __init__(self, Chance = 1.0, StunFor = 1, SourceName = None):
            self.Chance = Chance
            self.StunFor = StunFor
            self.SourceName = SourceName

        def ApplyEffect(self, Target):
            if self.Chance != 1.0:
                if RngFloat(0, 1) > self.Chance:
                    return
            DoStun = False
            for StatusEffect in reversed(Target.StatusEffects):
                if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                    Target.StatusEffects.remove(StatusEffect)
                    DoStun = True
            if DoStun:
                Battle_ApplyStatusEffect(TargetChar = Target, StatusEffect = BattleStatusEff_Stun(Duration = self.StunFor, SourceName = self.SourceName), CastOnEnemy = True)
            return

    class BattleEffect_RemoveDebuffsOnTarget:
        def __init__(self, Chance = 1.0, Amount = -1):
            Assert(Amount == -1 or Amount > 0, "amt of debuffs to rem must be either -1 or greater than 1")
            self.Chance = Chance
            self.Amount = -1 # -1 means "all"

        def ApplyEffect(self, Target):
            if self.Chance != 1.0:
                if RngFloat(0, 1) > self.Chance:
                    return
            if Battle_HasStatusEffect(Target, "stun"):
                Battle_GrantExtraTurn(Target, IgnoreDebuffs = True)
            if self.Amount == -1:
                for StatusEffect in reversed(Target.StatusEffects):
                    if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                        Target.StatusEffects.remove(StatusEffect)
            else:
                for StatusEffect in reversed(Target.StatusEffects[:self.Amount]):
                    if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                        Target.StatusEffects.remove(StatusEffect)

    class BattleEffect_RemoveRandomBuffOnTarget:
        def __init__(self, Chance = 1.0):
            self.Chance = Chance

        def ApplyEffect(self, Target):
            if self.Chance != 1.0:
                if RngFloat(0, 1) > self.Chance:
                    return

            Buffs = []
            for StatusEffect in Target.StatusEffects:
                if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                    Buffs.append(StatusEffect)

            if len(Buffs) > 0:
                BuffToRemove = renpy.random.choice(Buffs)
                Target.StatusEffects.remove(BuffToRemove)
            return

    class BattleEffect_StealBuffs:
        def __init__(self, StealingChar = None, Chance = 1.0):
            self.Chance = Chance
            self.StealingChar = StealingChar

        def ApplyEffect(self, Target):
            if self.Chance != 1.0:
                if RngFloat(0, 1) > self.Chance:
                    return
            for StatusEffect in reversed(Target.StatusEffects):
                if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                    Target.StatusEffects.remove(StatusEffect)
                    self.StealingChar.StatusEffects.append(StatusEffect)

#######################
    class BattleEffect_RestoreEnergy:
        def __init__(self, RestoreValue = 0.0, RatioFromMax = False):
            self.RestoreValue = RestoreValue
            self.RatioFromMax = RatioFromMax
        
        def ApplyEffect(self, Target):
            if self.RatioFromMax:
                Battle_RestoreEnergy(Target, round(self.RestoreValue * Target.EnergyMax))
            else:
                Battle_RestoreEnergy(Target, self.RestoreValue)
            return

    class BattleEffect_RestoreEnergyOrMana:
        def __init__(self, RestoreValue = 0.0, RatioFromMax = False):
            self.RestoreValue = RestoreValue
            self.RatioFromMax = RatioFromMax

        def ApplyEffect(self, Target):
            if self.RatioFromMax:
                if Target.CharRef["is_mage"]:
                    Battle_RestoreMana(Target, round(self.RestoreValue * Target.EnergyMax))
                else:
                    Battle_RestoreEnergy(Target, round(self.RestoreValue * Target.EnergyMax))
            else:
                if Target.CharRef["is_mage"]:
                    Battle_RestoreMana(Target, self.RestoreValue)
                else:
                    Battle_RestoreEnergy(Target, self.RestoreValue)
            return

    class BattleEffect_RestoreHealth:
        def __init__(self, RestoreValue = 0.0, RatioFromMax = False):
            self.RestoreValue = RestoreValue if RestoreValue is not None else 0.0
            self.RatioFromMax = RatioFromMax
        
        def ApplyEffect(self, Target):
            if self.RatioFromMax:
                Battle_RestoreHealth(Target, round(self.RestoreValue * Target.HealthMax))
            else:
                Battle_RestoreHealth(Target, self.RestoreValue)
            return

    class BattleEffect_SetHealth:
        def __init__(self, SetValue = 0.0, RatioFromMax = False):
            self.SetValue = SetValue
            self.RatioFromMax = RatioFromMax
        
        def ApplyEffect(self, Target):
            if self.RatioFromMax:
                Target.Health = round(self.SetValue * Target.HealthMax)
            else:
                Target.Health = self.SetValue
            return

###############################
    class BattleEffect_ExplodeTarget:
        def ApplyEffect(self, Target):
            if Battle_HasStatusEffect(Target, "burn"):
                BurnEff = Battle_GetStatusEffect(Target, "burn")
                DmgValue = BurnEff.Duration * BurnEff.Value
                Battle_AddLogEntry_Autoformat(
                    String = tra(_("TARGET_NAME explodes for DAMAGE_AMOUNT {color=[BATTLE_COLORS_LOG.DAMAGE]}damage!{/color}")),
                    TARGET = Target,
                    DAMAGE_AMOUNT = DmgValue)
                Battle_DealDamage(Target, DmgValue, PierceInvincibility = True)
                Battle_RemoveStatusEffect(Target, "burn")
            return

    # only for goblin bomb (for a scheduled cast that does damage as effect
    # might be useful for sth else too?
    class BattleEffect_DealDamageFlat:
        def __init__(self, DamageValue = 0):
            self.DamageValue = DamageValue

        def ApplyEffect(self, Target):
            Battle_DealDamage(Target, self.DamageValue)
            return

    # for "splash" effect
    class BattleEffect_DealDamageFlat_ToAlliesOfTarget:
        def __init__(self, DamageValue = 0):
            self.DamageValue = DamageValue

        def ApplyEffect(self, Target):
            AlliesList = Battle_GetAllAlliesOfChar(Target)
            for Ally in AlliesList:
                Battle_DealDamage(Ally, self.DamageValue)
            return

    # for spell-ish stuff? 
    # works same way as melee dmg roll 
    # but without attack happening
    class BattleEffect_DealDamageRoll:
        def __init__(self, Char, Multiplier):
            self.DamageDealer = Char
            self.Multiplier = Multiplier

        def ApplyEffect(self, Target):
            # roll dmg
            TotalStrikeDamage = Battle_BCharDamageRoll(self.DamageDealer, Mod = self.Multiplier)
            Battle_DealDamage(Target, TotalStrikeDamage)
            return

################################
    class BattleEffect_DrainHealth:
        def __init__(self, DrainingChar, AmtToDrain):
            self.DrainingChar = DrainingChar
            self.AmtToDrain = AmtToDrain

        def ApplyEffect(self, Target):
            AdjustedAmtToDrain = 0
            if Target.Health < self.AmtToDrain:
                AdjustedAmtToDrain = Target.Health
            else:
                AdjustedAmtToDrain = self.AmtToDrain
            Battle_DealDamage(Target, AdjustedAmtToDrain)
            Battle_RestoreHealth(self.DrainingChar, AdjustedAmtToDrain)
            return

    class BattleEffect_DrainEnergyOrMana:
        def __init__(self, DrainingChar, DrainPercentage, DrainFromCurrent):
            self.DrainingChar = DrainingChar
            self.DrainPercentage = DrainPercentage
            self.DrainFromCurrent = DrainFromCurrent

        def ApplyEffect(self, Target):
            if Target.CharRef["is_mage"]:
                DrainMana = True
            else:
                DrainMana = False

            DrainAmt = 0
            if DrainMana:
                if self.DrainFromCurrent:
                    DrainAmt = round(Target.Mana * self.DrainPercentage)
                else:
                    DrainAmt = min(round(Target.ManaMax * self.DrainPercentage), Target.Mana)
                Battle_BurnMana(Target, DrainAmt)
            else:
                if self.DrainFromCurrent:
                    DrainAmt = round(Target.Energy * self.DrainPercentage)
                else:
                    DrainAmt = min(round(Target.EnergyMax * self.DrainPercentage), Target.Energy)
                Battle_BurnEnergy(Target, DrainAmt)

            if self.DrainingChar.CharRef["is_mage"]:
                Battle_RestoreMana(self.DrainingChar, DrainAmt)
            else:
                Battle_RestoreEnergy(self.DrainingChar, DrainAmt)
            return

################################
    class BattleEffect_Antidote:
        def __init__(self, CharID):
            self.CharID = CharID

        def ApplyEffect(self, Target):
            # global
            if StoryCharIsPoisoned(self.CharID):
                RemoveStatusEffect_Story(self.CharID, "Poison")

            # battle
            ListOfPoisonsOnTargetBattleChar = [Effect.StatusEffectID for Effect in Target.StatusEffects if Effect.StatusEffectID.startswith("poisondot")]
            for EffID in ListOfPoisonsOnTargetBattleChar:
                Battle_RemoveStatusEffect(Target, EffID)

            # remove from list of chars who eaten strange meat or took raza to not apply global poison post-battle
            if Target in BattleScene.PostBattleGlobalPoison:
                BattleScene.PostBattleGlobalPoison.pop(Target)
            return
