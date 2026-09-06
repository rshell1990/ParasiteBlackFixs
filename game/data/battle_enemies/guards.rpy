init python:
### generic city guard. encountered during Graceful Rebirth (dros TF) quest
### encountered just once, but you can use this guy as a default "guard"
    CharDefs["e_guard"] = BuildCharTemplate(CharID = "e_guard",
        name = _("City guard"),
        IsMob = True,
        BattleSkin =  "guard",
        base_health = 40,
        base_damage = 15,
        base_energy = 55,

        Strength = 0,
        Endurance = 12,
        Willpower = 0,
        Agility = 8,
        Dexterity = 6,
        Luck = 8,

        base_xp_value = 20,
        auto_attr_allocation = "fighter",
        
        CharSkills = {"NeutralASmallBlessing":1})
    LootDropData["e_guard"] = [
        {"ItemID":"gold",
        "MinDropRolls":1,
        "MaxDropRolls":1,
        "ChancePerSingleEntry":0.75,
        "AmountPerSingleEntry":35},
        
        {"ItemID":"potion_heal_minor",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.20}]

### stronger version of the guard, fights on the side of Tarek during damzel in diztrezz quest
    CharDefs["e_corruptGuard"] = BuildCharTemplate(CharID = "e_corruptGuard",
        name = _("Corrupt guard"),
        IsMob = True,
        BattleSkin =  "guard", 

        base_health = 70,
        base_damage = 15,
        base_energy = 50,

        Strength = 0,
        Endurance = 14,
        Willpower = 0,
        Agility = 8,
        Dexterity = 4,
        Luck = 10,

        base_xp_value = 30,
        auto_attr_allocation = "fighter",
        
        CharSkills = {"NeutralASmallBlessing":1})
    LootDropData["e_corruptGuard"] = [
        {"ItemID":"gold",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.75,
        "AmountPerSingleEntry":63},
        
        {"ItemID":"potion_heal_minor",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.20}]

### kinda like a mini-boss. A guard that bothers Lucius Mal during Graceful Rebirth (dros tf) quest
    CharDefs["e_jurgen"] = BuildCharTemplate(CharID = "e_jurgen",
        name = _("Jurgen"),
        IsMob = True,
        BattleSkin =  "guard", 

        base_health = 200,
        base_damage = 40,
        base_energy = 70,
        base_armor = 40,

        #base_mres = 0,
        #base_att_rate = 0,
        #base_crit_chance = 0,
        #base_dodge_rate = 0,

        Strength = 0,
        Endurance = 0,
        Willpower = 0,
        Agility = 10,
        Dexterity = 6,
        Luck = 5,

        base_xp_value = 30,

        CharSkills = {"NeutralLeadership":1, "NeutralSuperHeavyBlow":1},
        )

    LootDropData["e_jurgen"] = [
        {"ItemID":"potion_heal_minor",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.20}]

### generic scout of the scouts corp, currently only fights alongside player in prologue "teamwork" exercises
    CharDefs["e_alderay_scout"] = BuildCharTemplate(CharID = "e_alderay_scout",
        name = _("Scout"),
        IsMob = True,
        BattleSkin =  "alderay_scout",

        Strength = 6,
        Endurance = 4,
        Willpower = 4,
        Agility = 5,
        Dexterity = 5,
        Luck = 5,

        CharSkills = {"WarriorDualStrike":1, "WarriorDodge":1},
        
        )

### hamun variant of guard
    CharDefs["e_guard_hamun"] = BuildCharTemplate(CharID = "e_guard_hamun",
        name = _("Hamun guard"),
        IsMob = True,
        BattleSkin =  "guard_hamun",
        base_health = 290,
        base_damage = 15,
        base_energy = 55,

        Strength = 5,
        Endurance = 5,
        Willpower = 3,
        Agility = 6,
        Dexterity = 6,
        Luck = 8,

        experience = ExpSetToLevel(8),

        base_xp_value = 20,
        auto_attr_allocation = "fighter",
        
        CharSkills = {"NeutralASmallBlessing":1})
    LootDropData["e_guard_hamun"] = [
        {"ItemID":"gold",
        "MinDropRolls":1,
        "MaxDropRolls":1,
        "ChancePerSingleEntry":0.75,
        "AmountPerSingleEntry":35},
        
        {"ItemID":"potion_heal_minor",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.20}]