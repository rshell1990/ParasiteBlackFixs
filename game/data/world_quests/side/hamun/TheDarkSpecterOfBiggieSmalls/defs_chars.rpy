init python:
### kinda stronger bandit you meet in the docks of hamun, part of TheDarkSpecterOfBiggieSmalls quest
    CharDefs["BiggieSmalls"] = BuildCharTemplate(CharID = "BiggieSmalls",
        name = _("Biggie Smalls"),
        IsMob = True,
        BattleSkin =  "demorai_brute", 
        base_health = 125,
        base_damage = 25,
        base_energy = 80,

        Strength = 0,
        Endurance = 15,
        Willpower = 0,
        Agility = 2,
        Dexterity = 4,
        Luck = 1,

        base_xp_value = 45,
        auto_attr_allocation = "hulk",
        
        CharSkills = {"NeutralSuperHeavyBlow":1, "NeutralHumiliatingAttack":1},
        )
### kinda stronger bandit you meet in various places in game
    CharDefs["lenin"] = BuildCharTemplate(CharID = "lenin",
        name = _("Lenin"),
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
        Luck = 15,

        base_xp_value = 20,
        auto_attr_allocation = "fighter",
        CharSkills = {"NeutralTeamUp":1, "NeutralASmallBlessing":1},
        )

    LootDropData["lenin"] = [
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

### lenin's thug, a generic bandit you meet in Hamun docks, part of TheDarkSpecterOfBiggieSmalls quest
    CharDefs["lenins_thug1"] = BuildCharTemplate(CharID = "lenins_thug1",
        name = _("lenin's thug"),
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
    LootDropData["lenins_thug"] = [
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
    CharDefs["lenins_thug2"] = BuildCharTemplate(CharID = "lenins_thug2",
        name = _("lenin's thug2"),
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
    LootDropData["lenins_thug2"] = [
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