init python:    
### kinda stronger bandit you meet in various places in game
    CharDefs["e_thug"] = BuildCharTemplate(CharID = "e_thug",
        name = _("Thug"),
        IsMob = True,
        BattleSkin =  "bandit_1",
        base_health = 90,
        base_damage = 15,
        base_energy = 55,

        Strength = 0,
        Endurance = 4,
        Willpower = 0,
        Agility = 10,
        Dexterity = 10,
        Luck = 10,

        base_xp_value = 20,
        auto_attr_allocation = "fighter",
        CharSkills = {"NeutralTeamUp":1, "NeutralASmallBlessing":1},
        )

    LootDropData["e_thug"] = [
        {"ItemID":"gold",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.75,
        "AmountPerSingleEntry":22},

        {"ItemID":"raza_seed",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.25},
        
        {"ItemID":"potion_heal_minor",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.30}]

### generic bandit you meet in novaras
    CharDefs["e_bandit"] = BuildCharTemplate(CharID = "e_bandit",
        name = _("Bandit"),
        IsMob = True,
        BattleSkin =  "bandit_2",
        
        base_health = 40,
        base_damage = 20,
        base_energy = 55,

        Strength = 0,
        Endurance = 10,
        Willpower = 0,
        Agility = 6,
        Dexterity = 6,
        Luck = 8,

        base_xp_value = 10,
        auto_attr_allocation = "rogue",
        
        CharSkills = {"NeutralPreciseShot":1, "NeutralASmallBlessing":1},
        )
    LootDropData["e_bandit"] = [
        {"ItemID":"gold",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.40,
        "AmountPerSingleEntry":15},

        {"ItemID":"raza_seed",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.25},
        
        {"ItemID":"potion_heal_minor",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.30}]

    ### stronger bandits that roam outside the city (freemap and PriceLife quest)
    CharDefs["e_raider"] = BuildCharTemplate(CharID = "e_raider",
        name = _("Raider"),
        IsMob = True,
        BattleSkin =  "raider",

        base_health = 90,
        base_damage = 30,
        base_energy = 80,

        Strength = 0,
        Endurance = 10,
        Willpower = 0,
        Agility = 8,
        Dexterity = 6,
        Luck = 5,

        base_xp_value = 25,
        auto_attr_allocation = "fighter",

        CharSkills = {"NeutralTwist":1, "NeutralLeadership":1, "NeutralASmallBlessing":1},
        )
    LootDropData["e_raider"] = [
        {"ItemID":"gold",
        "MinDropRolls":1,
        "MaxDropRolls":3,
        "ChancePerSingleEntry":0.25,
        "AmountPerSingleEntry":18},

        {"ItemID":"raza_seed",
        "MinDropRolls":1,
        "MaxDropRolls":3,
        "ChancePerSingleEntry":0.40},

        {"ItemID":"potion_heal_minor",
        "MinDropRolls":1,
        "MaxDropRolls":3,
        "ChancePerSingleEntry":0.40}
        ]
    ### khazah leader
    CharDefs["e_khazah_leader"] = BuildCharTemplate(CharID = "e_khazah_leader",
        name = _("Khazah leader"),
        IsMob = True,
        BattleSkin =  "assassin",

        base_health = 520,
        base_damage = 15,
        base_energy = 75,

        Strength = 0,
        Endurance = 4,
        Willpower = 0,
        Agility = 10,
        Dexterity = 10,
        Luck = 10,

        base_xp_value = 20,
        auto_attr_allocation = "fighter",
        CharSkills = {"NeutralDodgeThis":1, "NeutralFastAndDeadly":1, "NeutralSmokeBomb":1},
        )
    LootDropData["e_khazah_leader"] = [
        {"ItemID":"gold",
        "MinDropRolls":1,
        "MaxDropRolls":3,
        "ChancePerSingleEntry":0.25,
        "AmountPerSingleEntry":18},

        {"ItemID":"raza_seed",
        "MinDropRolls":1,
        "MaxDropRolls":3,
        "ChancePerSingleEntry":0.40},

        {"ItemID":"potion_heal_minor",
        "MinDropRolls":1,
        "MaxDropRolls":3,
        "ChancePerSingleEntry":0.40}
        ]


    ### kinda stronger bandit you meet in various places in game
    CharDefs["e_swindler"] = BuildCharTemplate(CharID = "e_swindler",
        name = _("Swindler"),
        IsMob = True,
        BattleSkin =  "skin_swindler",
        base_health = 80,
        base_damage = 25,
        base_energy = 55,

        Strength = 0,
        Endurance = 10,
        Willpower = 0,
        Agility = 8,
        Dexterity = 8,
        Luck = 8,

        experience = ExpSetToLevel(3),
        base_xp_value = 20,
        auto_attr_allocation = "rogue",
        
        CharSkills = {"NeutralPreciseShot":1, "NeutralAirMaster":1},
    )

    LootDropData["e_swindler"] = [
        {"ItemID":"gold",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.75,
        "AmountPerSingleEntry":40}]

    ### coming storm vala investigation route enemy
    CharDefs["e_assassin"] = BuildCharTemplate(CharID = "e_assassin",
        name = _("Assassin"),
        IsMob = True,
        BattleSkin =  "assassin",

        base_health = 520,
        base_damage = 15,
        base_energy = 75,

        Strength = 0,
        Endurance = 4,
        Willpower = 0,
        Agility = 10,
        Dexterity = 10,
        Luck = 10,

        base_xp_value = 20,
        auto_attr_allocation = "fighter",
        CharSkills = {"NeutralDodgeThis":1, "NeutralFastAndDeadly":1, "NeutralSmokeBomb":1},
    )
    ### tarbeck pt 2 
    CharDefs["e_kidnapper"] = BuildCharTemplate(CharID = "e_kidnapper",
        name = _("Kidnapper"),
        IsMob = True,
        BattleSkin =  "assassin",

        base_health = 675,
        base_damage = 14,
        base_energy = 80,

        Strength = 0,
        Endurance = 4,
        Willpower = 0,
        Agility = 11,
        Dexterity = 10,
        Luck = 10,

        base_xp_value = 20,
        auto_attr_allocation = "fighter",
        CharSkills = {"NeutralTeamUp":1, "NeutralFastAndDeadly":1, "NeutralSmokeBomb":1},
    )