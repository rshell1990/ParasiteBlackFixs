init python in BATTLE_STATUS_EFFECT_STACKING:
    _constant = True
    ADDITIVE = 0
    REPLACE = 1
    ADD_AS_NEW = 2

init python in BATTLE_STATUS_EFFECT_TYPE:
    _constant = True
    BUFF = 0    # green frame, counted as buff for logic
    DEBUFF = 1  # red frame, counted as debuff for logc
    NEUTRAL = 2 # yellow frame, counted as neither, used for TF and something else, taunt? I guess

init python:
    class BattleStatusEff:
        def __init__(self, Duration, StatusEffectID, SourceName = None):
            self.EffectName = "unnamed"                                 # set by skill
            self.SourceName = SourceName                                # pass in to display source on hover

            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.BUFF            # many logic depends on this

            self.Owner_BattleChar = None                                # set via apply function

            self.Duration = Duration                                    # all durations tick each time any team's turn begins
            self.StatusEffectID = StatusEffectID                        # must be unique for each distinct status effect, tied to stacking

            self.StackingMethod = BATTLE_STATUS_EFFECT_STACKING.REPLACE # by default skills with same id dont stack in any way but replace

            self.TickOn_Ally = 0                                        # 0 == tick at turn start, 1 == tick at turn end, 
            self.TickOn_Enemy = 1                                       
            self.TickOn = None                                          # set on apply to either 0 or 1

            self.Icon = "images/battle_status_eff_icons/Undefined.webp" 

            self.AttrMod_StrengthMul = None                             # float modifiers like 1.25 -> +25%
            self.AttrMod_EnduranceMul = None
            self.AttrMod_WillpowerMul = None
            self.AttrMod_AgilityMul = None
            self.AttrMod_DexterityMul = None
            self.AttrMod_LuckMul = None

            self.AttrMod_StrengthAdd = None                             # int modifiers like 1, 2, 10
            self.AttrMod_EnduranceAdd = None
            self.AttrMod_WillpowerAdd = None
            self.AttrMod_AgilityAdd = None
            self.AttrMod_DexterityAdd = None
            self.AttrMod_LuckAdd = None

            self.Permanent = (True if Duration == -1 else False)        # only tf

            self.DamageRecieved_Mod = 1.0                               # the higher the more damage char takes
            self.DamageDealt_Mod = 1.0                                  # the higher the more damage char deals

            self.StatMod_Armor = None                                   # float modifeirs like 1.25 -> +25%
            self.StatMod_MagicRes = None
            self.StatMod_AttackRating = None
            self.StatMod_DodgeRating = None
            self.StatMod_CritChance = None
            
            self.TauntedBy = None                                       # taunted by battlechar reference
            self.ProtectedBy = None                                     # protected by battlechar reference

            self.ResRecoverMod_Health = None                            # if not none, alters resource recovery. 1.0 == 100%
            self.ResRecoverMod_Energy = None
            self.ResRecoverMod_Mana = None
