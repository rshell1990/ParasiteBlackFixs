init python:
    ### quick & agile lurker of demorai army they use for scoutin'
    CharDefs["e_demorai_scout"] = BuildCharTemplate(CharID = "e_demorai_scout",
        name = _("Scout"),
        IsMob = True,
        BattleSkin =  "demorai_scout", 
        
        base_health = 80,
        base_damage = 10,
        base_energy = 55,

        Strength = 0,
        Endurance = 5,
        Willpower = 0,
        Agility = 8,
        Dexterity = 5,
        Luck = 5,

        auto_attr_allocation = "rogue",
        base_xp_value = 30,

        CharSkills = {"NeutralTeamUp":1},
        )
    LootDropData["e_demorai_scout"] = [
            {"ItemID":"bronze_scraps",
            # at least 2 drop rolls will happen
            "MinDropRolls":2,
            # at most 4 drop rolls
            "MaxDropRolls":2,
            # each roll will be 100%
            "ChancePerSingleEntry":1.0},

            {"ItemID":"gems",
            "MinDropRolls":2,
            "MaxDropRolls":4,
            "ChancePerSingleEntry":0.60},
            
            {"ItemID":"potion_heal_minor",
            "MinDropRolls":1,
            "MaxDropRolls":2,
            "ChancePerSingleEntry":0.30}]

    ### heavy slow bulky demorai warrior
    CharDefs["e_demorai_brute"] = BuildCharTemplate(CharID = "e_demorai_brute",
        name = _("Brute"),
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
    LootDropData["e_demorai_brute"] = [
        {"ItemID":"strange_meat",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.50},
        
        {"ItemID":"potion_heal_minor",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.20}]

    ### huge scorpion of demorai nature you encounter during prologue. spits acid, super big guy
    CharDefs["e_scorpionBoss"] = BuildCharTemplate(CharID = "e_scorpionBoss",
        name = _("Scorpion"),
        IsMob = True,
        BattleSkin =  "demorai_scorpion",

        base_health = 750,
        base_damage = 65,

        Strength = 0,
        Endurance = 15,
        Willpower = 8,
        Agility = 10,
        Dexterity = 6,
        Luck = 5,

        experience = ExpShowLevelAsUnknown(),
        base_xp_value = 200,
        
        CharSkills = {"NeutralShakeTheGround":1, "NeutralMaximumSafety":1},
        )

    ### a pet scorpion of Tarek, encountered during damzel in diztrezz quest. weaker than prologue scorpion
    CharDefs["e_scorpionBoss_red"] = BuildCharTemplate(CharID = "e_scorpionBoss_red",
        name = _("Betsy?"),
        IsMob = True,
        BattleSkin =  "demorai_scorpion_red",

        base_health = 300,
        base_energy = 85,
        base_damage = 45,
        
        Strength = 0,
        Endurance = 15,
        Willpower = 0,
        Agility = 12,
        Dexterity = 8,
        Luck = 10,

        base_xp_value = 120,
        
        CharSkills = {"NeutralShakeTheGround":1},
        )

    ### unused
    CharDefs["e_dark_soldier"] = BuildCharTemplate(CharID = "e_dark_soldier",
        name = _("Dark Soldier"),
        IsMob = True,
        BattleSkin =  "dark_soldier",
        
        base_health = 60,
        base_damage = 30,
        base_energy = 80,
        
        Strength = 0,
        Endurance = 22,
        Willpower = 0,
        Agility = 12,
        Dexterity = 10,
        Luck = 10,

        base_xp_value = 225,
        auto_attr_allocation = "fighter",
        
        CharSkills = {"NeutralTwist":1, "NeutralLeadership":1},
        )

    ### he's not a mob, be aware! 
    # he has stats that carry over battle to battle n shiiiet
    CharDefs["zanarak"] = BuildCharTemplate(CharID = "zanarak",
        name = _("Zanarak"),
        BattleSkin =  "zanarak",

        base_health = 1800,
        base_energy = 440,
        base_damage = 75,
        base_armor = 50,

        Strength = 0,
        Endurance = 0,
        Willpower = 0,
        Agility = 10,
        Dexterity = 5,
        Luck = 5,

        base_xp_value = 120,

        experience = ExpSetToLevel(20),

        CharSkills = {
            "ZanarakBlackLight":1,
            "ZanarakDarkSun":1,
            "ZanarakEternalDarkness":1,
            "ZanarakMalakaisCurse":1,
            "ZanarakUnstoppableRage":1
        }
    )
    ### 
    CharDefs["e_poltrik"] = BuildCharTemplate(CharID = "e_poltrik",
        name = _("Poltrik"),
        IsMob = True,
        BattleSkin =  "poltrik",

        base_health = 900,
        base_energy = 90,
        base_damage = 68,
        base_armor = 57,

        #base_mres = 0,
        #base_att_rate = 0,
        #base_crit_chance = 0,
        #base_dodge_rate = 0,

        Strength = 0,
        Endurance = 0,
        Willpower = 0,
        Agility = 12,
        Dexterity = 8,
        Luck = 10,

        base_xp_value = 120,
        
        CharSkills = {
            "NeutralPoisonAttack":1,
            "NeutralGettingSick":1,
            "NeutralShakeTheGround":1,
            "NeutralTwist":1,
            "NeutralFrighten":1},
        )
    ### 
    CharDefs["e_snakeman"] = BuildCharTemplate(CharID = "e_snakeman",
        name = _("Snakeman"),
        IsMob = True,
        BattleSkin =  "snakeman",

        base_health = 540,
        base_energy = 90,
        base_damage = 55,
        base_armor = 48,

        #base_mres = 0,
        #base_att_rate = 0,
        #base_crit_chance = 0,
        #base_dodge_rate = 0,
        
        Strength = 0,
        Endurance = 0,
        Willpower = 0,
        Agility = 10,
        Dexterity = 8,
        Luck = 6,

        base_xp_value = 120,
        
        CharSkills = {"NeutralPoisonThem":1, "NeutralAncientCurse":1},
        )

    ### 
    CharDefs["e_ghoul_red"] = BuildCharTemplate(CharID = "e_ghoul_red",
        name = _("Red ghoul"),
        IsMob = True,
        BattleSkin =  "ghoul_red",

        base_health = 680,
        base_energy = 90,
        base_damage = 52,
        base_armor = 42,

        #base_mres = 0,
        #base_att_rate = 0,
        #base_crit_chance = 0,
        #base_dodge_rate = 0,
        
        Strength = 0,
        Endurance = 0,
        Willpower = 0,
        Agility = 12,
        Dexterity = 7,
        Luck = 5,

        base_xp_value = 120,
        
        CharSkills = {
            "NeutralCalculationMistake":1,
            "NeutralGettingSick":1,
            "NeutralMaximumSafety":1,
            "NeutralLeadership":1},
        )