init -1 python:
    ### attribute descriptions ###
    # last updated 23/09/2023
    # "Strength":     5, # +5 melee damage per point
    # "Endurance":    5, # +5 hp per point OVER 5, its value also equals phys damage resistance (armor)

    # "Willpower":    5, # +5 max energy per point OVER 5
    # "mana_power":   5, # +5 max mana per point, UNUSED

    # "Agility":      5, # value equals attack rating (which affects to-hit chance)
    # "Dexterity":    5, # value equals dodge rating (which is tested against attack rating)

    # "Luck":         5, # to-crit, flat % value

    # these are narrative-only
    # "Charisma":     5, # unlocks charisma-based dialogue choices
    # "Barter":       5, # the higher barter skill, the lower shop prices + some unique dialogue options 

    baseCharTemplate = {
        "_derived": {
            "HealthMax":    healthMaxCalc, # red bar
            "EnergyMax":    energyMaxCalc, # green bar (aka stamina)
            "ManaMax":      manaMaxCalc, # blue bar (for mages)

            "Damage":       damageCalc,
            "Armor":        armorCalc,
            "MagicRes":     magicResCalc,
            "AttackRating": AttackRatingCalc, # to-hit chance, agi-based
            "DodgeRating":  DodgeRatingCalc, # to-dodge chance, dex-based
            "CritChance":   CritChanceCalc, # luck-based

            # these include item buffs
            # there must be a better way to do this    
            "derived_Strength":     StrengthCalc,
            "derived_Endurance":    EnduranceCalc, 
            "derived_Willpower":    WillpowerCalc, 
            "derived_Agility":      AgiCalc,
            "derived_Dexterity":    DexCalc,
            "derived_Luck":         LuckCalc,
            "derived_Charisma":     CharismaCalc,
            "derived_Barter":       BarterCalc,
        },

        "name":         "[player_name]",
        "portrait":     "characters/mc/portrait.webp",
        "is_mage":      False,

        # used for dros, markus, elena, mc, stored here to not repeat shit
        # used IN BATTLE TOO
        "Transformed":    False, 

        # if set to true, this char will be instantiated right before battle and healed to full hp
        # if false, this char will end up in worldChars
        "IsMob":        False, 

        # current hp/ep/mp, is recalculated on game start/battle start
        "Health":       100,
        "Energy":       100,
        "Mana":         100,

        # base hp/ep/mp, will be added to calculated max
        "base_health":  50,
        "base_energy":  100,
        "base_mana":    100,

        ### to allow for adding stats directly vs einsteining through attribute math
        # damage = base_damage + damage derived from attrs/items
        "base_damage":      0,
        "base_armor":       0,
        "base_mres":        0,
        "base_att_rate":    0,
        "base_dodge_rate":  0,
        "base_crit_chance": 0,
    
        ### base attributes, changeable on levelup
        # desc might be obsolete
        "Strength":     5, # +5 melee damage per point
        "Endurance":    5, # +5 hp per point OVER 5, its value also equals phys damage resistance (armor)

        "Willpower":    5, # +5 max energy per point OVER 5
        "Mana_Power":   5, # +5 max mana per point, UNUSED

        "Agility":      5, # value equals attack rating (which affects to-hit chance)
        "Dexterity":    5, # value equals dodge rating (which is tested against attack rating)

        "Luck":         5, # to-crit, flat % value

        "Charisma":     5, # likelihood of persuasive arguments working
        "Barter":       5, # the higher barter skill, the lower shop prices + some unique dialogue options 

        ### levelling-related
        "experience":                   0,
        "lvlPoints":                    0, # aka attribute points
        "skillPoints":                  0, 
        
        "perks":                        [], # a list of perk IDs (only makes sense for MC)
        "auto_attr_allocation":         None, # used for mobs to auto-allocate attribute points

        # auto-recalculation-related
        "directly_added_attribute_points":  0, # for cases such as mc using an item or getting an attr boost through story, we track all these "direct" increases

        ### relationship-related
        # mc-char relation lvl, -10 to +10 (+9actually) [-10, -9, ... -1, 0, 1, ... 8, 9]
        # changed/clamped by CharChangeRel function
        "relation":                     0,
        # relationship status ID.
        # look for Rel_Status_ID_Strings to learn wtf it is
        "relstatus":                    "rel_acquaintance",
        # a list of unlocked/seen rel entries
        "RelTextIDs":                   set(),
        # purely cosmetic
        # ^ not anymore, let's be using this for tracking actual dead/alive state of a char in-game
        "relisdead":                    False,
        
        ### yes everyone can get pregnant :muscle: even men
        "preg":                         0,

        ### battle only, stores ID of skin to use
        "BattleSkin":                   None,

        "BattleClass":                  None,       # It's a string, example : 'warrior'
        "CharSkills":                   dict(),     # SkillID:SkillLevel

        "base_xp_value":                0,

        ### alternate form (mc/ markus, elena)
        "HasAltForm":                   False,
        "AltForm_Unlocked":             True,

        "AltForm_SkillPoints":          0,

        "AltForm_BattleClass":          None,
        "AltForm_BattleSkin":           None,

        "AltForm_CharSkills":           dict(),     # SkillID:SkillLevel

        "AltForm_TransformSkill":       None,
        "AltForm_UnTransformSkill":     None,

        ### equipment slots
        "eqp_chest":    None,
        "eqp_neck":     None,
        "eqp_ring1":    None,
        "eqp_ring2":    None,
        "eqp_hand1":    None,
        "eqp_hand2":    None,

        ### battle only, stores a reference to a battle char.
        # this is a crutchy way to alter *calc functions by allowing DataObj.BattleChar access
        "BattleChar":   None,

        ### 
        # whether this char will ever be a player companion in the game
        "IsCompanion":  False,
    }