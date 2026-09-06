init python:
    ### debug for neutral skills
    CharDefs["e_debug_neutral"] = BuildCharTemplate(CharID = "e_debug_neutral",
        name = "debug enemy",
        IsMob = True,
        BattleSkin =  "debug_skin", 

        CharSkills = {
            "NeutralAirMaster":1,
            "NeutralALittleHelp":1,
            "NeutralAncientCurse":1,
            "NeutralASmallBlessing":1,
            "NeutralBattleCompensation":1,
            "NeutralPoisonAttack":1,

            "NeutralCalculationMistake":1,
            "NeutralFrighten":1,
            "NeutralGettingSick":1,
            "NeutralGreatTaunt":1,
            "NeutralHealThem":1,

            "NeutralHumiliatingAttack":1,
            "NeutralIgniteThem":1,
            "NeutralItCouldHaveBeenWorse":1,
            "NeutralLeadership":1,
            "NeutralMaximumSafety":1,

            "NeutralPreciseShot":1,
            "NeutralSanctuary":1,
            "NeutralSaveIt":1,
            "NeutralShakeTheGround":1,
            "NeutralSuperHeavyBlow":1,

            "NeutralTeamUp":1,
            "NeutralTwist":1},
    )

    ### big worm boss. neutral "wildlife" of valley of death. you encounter it if you go hunt with ves
    CharDefs["e_bazarkWorm"] = BuildCharTemplate(CharID = "e_bazarkWorm",
        name = _("Bazark"),
        IsMob = True,
        BattleSkin =  "bazark_worm",

        base_health = 1340,
        base_damage = 55,
        base_energy = 125,

        Strength = 0,
        Endurance = 26,
        Willpower = 0,
        Agility = 10,
        Dexterity = 2,
        Luck = 2,

        base_xp_value = 100,

        experience = ExpSetToLevel(12),
        
        CharSkills = {"NeutralShakeTheGround":1, "NeutralCalculationMistake":1, "NeutralMaximumSafety":1},
    )

    ### frog boss you walk into during High Fashion quest, it sits beneath palam tower in sewers.
    ### its not demorai, but a spawn of some cultists' doing weird shit
    CharDefs["e_frogBoss"] = BuildCharTemplate(CharID = "e_frogBoss",
        name = _("Demon frog"),
        IsMob = True,
        BattleSkin =  "demorai_frog",


        base_health = 400,
        base_damage = 45,
        base_energy = 80,

        Strength = 0,
        Endurance = 30,
        Willpower = 0,
        Agility = 14,
        Dexterity = 4,
        Luck = 5,

        base_xp_value = 55,
        experience = ExpSetToLevel(6),
        
        CharSkills = {"NeutralShakeTheGround":1, "NeutralGettingSick":1},
    )

    ### giant slimelark, a boss you encounter at lake balun.
    ### local wildlife, essentially a human-eating slime.
    CharDefs["e_bigSlimelark"] = BuildCharTemplate(CharID = "e_bigSlimelark",
        name = _("Giant slimelark"),
        IsMob = True,
        BattleSkin =  "bigSlimelark",
        
        base_health = 860,
        base_damage = 30,
        base_energy = 155,

        Strength = 0,
        Endurance = 28,
        Willpower = 0,
        Agility = 15,
        Dexterity = 0,
        Luck = 0,

        base_xp_value = 60,
        auto_attr_allocation = "hulk",
        
        CharSkills = {"NeutralShakeTheGround":1, "NeutralItCouldHaveBeenWorse":1}
    )

    CharDefs["e_caltrack"] = BuildCharTemplate(CharID = "e_caltrack",
        name = _("Caltrack"),
        IsMob = True,
        BattleSkin = "caltrack",

        base_health = 2860,

        base_damage = 45,
        base_energy = 165,

        Strength = 0,
        Endurance = 28,
        Willpower = 0,
        Agility = 15,
        Dexterity = 0,
        Luck = 0,

        base_xp_value = 60,
        experience = ExpSetToLevel(25),
        auto_attr_allocation = "hulk",

        CharSkills = {
            "NeutralBodySlam":1,
            "NeutralJawsOfDeath":1,
            "NeutralRagefulWager":1,
            "NeutralRipAndTear":1,
            "NeutralSeethingAnger":1,
            }
    )

    CharDefs["e_abomination"] = BuildCharTemplate(CharID = "e_abomination",
        name = _("The Abomination"),
        IsMob = True,
        BattleSkin =  "abomination",
        
        base_health = 860,
        base_damage = 30,
        base_energy = 155,

        Strength = 0,
        Endurance = 28,
        Willpower = 0,
        Agility = 15,
        Dexterity = 0,
        Luck = 0,

        base_xp_value = 60,
        experience = ExpSetToLevel(16),
        auto_attr_allocation = "hulk",
        
        CharSkills = {"NeutralShakeTheGround":1, "NeutralCalculationMistake":1, "NeutralMaximumSafety":1},
    )

    CharDefs["e_green_slime"] = BuildCharTemplate(CharID = "e_green_slime",
        name = _("Green slime"),
        IsMob = True,
        BattleSkin =  "slime_green",
        
        base_health = 1000,
        base_damage = 30,
        base_energy = 155,

        Strength = 0,
        Endurance = 28,
        Willpower = 0,
        Agility = 15,
        Dexterity = 0,
        Luck = 0,

        base_xp_value = 60,
        auto_attr_allocation = "hulk",
        
        CharSkills = {"NeutralShakeTheGround":1, "NeutralItCouldHaveBeenWorse":1}
    )

    ### a boss you encounter in the end of The Bloodhound quest.
    ### I dont really know what the fuck it is lore-wise, ask raven.
    ### I guess its like a dangerous assassin-bot or something
    CharDefs["e_man_in_black"] = BuildCharTemplate(CharID = "e_man_in_black",
        name = _("Man in Black"),
        IsMob = True,
        BattleSkin =  "man_in_black",
        
        base_health = 1100,
        base_damage = 60,
        base_energy = 240,
        
        Strength = 0,
        Endurance = 55,
        Willpower = 0,
        Agility = 60,
        Dexterity = 80,
        Luck = 30,

        experience = ExpShowLevelAsUnknown(),
        base_xp_value = 55,
        
        CharSkills = {"NeutralPreciseShot":1, "NeutralAirMaster":1, "NeutralPoisonThem":1},
    )

    ### generic slimelark. wildlife of Lake Balun
    CharDefs["e_slimelark"] = BuildCharTemplate(CharID = "e_slimelark",
        name = _("Slimelark"),
        IsMob = True,
        BattleSkin =  "slimelark", 
        base_health = 160,
        base_damage = 20,
        base_energy = 95,
        
        Strength = 0,
        Endurance = 10,
        Willpower = 0,
        Agility = 8,
        Dexterity = 2,
        Luck = 0,
        
        base_xp_value = 25,
        auto_attr_allocation = "hulk",
        
        CharSkills = {"NeutralPoisonThem":1, "NeutralTwist":1},
    )

    ### kraken. a stronk boss you encounter during TwoEmperors quest (but you can return another time too)
    ### not a demorai, generic watery wildlife
    CharDefs["e_kraken"] = BuildCharTemplate(CharID = "e_kraken",
        name = _("Kraken"),
        IsMob = True,
        BattleSkin =  "kraken", 
        
        base_health = 4800,
        base_damage = 195,
        base_energy = 135,

        Strength = 0,
        Endurance = 40,
        Willpower = 0,
        Agility = 14,
        Dexterity = 0,
        Luck = 10,

        experience = ExpShowLevelAsUnknown(),
        base_xp_value = 100,
        
        CharSkills = {"NeutralAncientCurse":1, "NeutralItCouldHaveBeenWorse":1},
    )

    ### encountered during adventureres' guild rats quest. Just a crazy rat that nibbled on corpses for too long
    CharDefs["e_crazy_rat"] = BuildCharTemplate(CharID = "e_crazy_rat",
        name = _("Giant rat"),
        IsMob = True,
        BattleSkin =  "crazy_rat", 


        base_health = 180,
        base_damage = 12,
        base_energy = 70,

        Strength = 0,
        Endurance = 8,
        Willpower = 1,
        Agility = 10,
        Dexterity = 10,
        Luck = 0,

        experience = ExpSetToLevel(5),

        base_xp_value = 15,
        auto_attr_allocation = "rogue",
        
        CharSkills = {"NeutralPoisonThem":1},
    )

    ### a leader of the rats from the above entry. should be like controlling them or somethinag
    CharDefs["e_crazy_rat_mother"] = BuildCharTemplate(CharID = "e_crazy_rat_mother",
        name = _("Behemoth"),
        IsMob = True,
        BattleSkin =  "crazy_rat_mother", 

        base_health = 940,
        base_damage = 30,
        base_energy = 145,

        Strength = 0,
        Endurance = 18,
        Willpower = 0,
        Agility = 12,
        Dexterity = 6,
        Luck = 10,

        experience = ExpSetToLevel(10),

        base_xp_value = 35,
        
        CharSkills = {"NeutralPoisonThem":1, "NeutralBattleCompensation":1},
    )

    CharDefs["e_desert_rat_queen"] = BuildCharTemplate(CharID = "e_crazy_rat_mother",
        name = _("Desert rat queen"),
        IsMob = True,
        BattleSkin =  "desert_rat_queen", 

        base_health = 1200,
        base_damage = 40,
        base_energy = 145,

        Strength = 0,
        Endurance = 18,
        Willpower = 0,
        Agility = 12,
        Dexterity = 6,
        Luck = 10,

        experience = ExpSetToLevel(10),

        base_xp_value = 35,
        
        CharSkills = {"NeutralPoisonThem":1, "NeutralBattleCompensation":1},
    )

    ### encountered during DarkMage quest, basically like a random dark mage's experiments' result.
    CharDefs["e_spiderman"] = BuildCharTemplate(CharID = "e_spiderman",
        name = _("Camen"),
        IsMob = True,
        BattleSkin =  "spiderman", 

        base_health = 1005,
        base_damage = 55,
        base_energy = 95,
        
        Strength = 0,
        Endurance = 8,
        Willpower = 0,
        Agility = 16,
        Dexterity = 10,
        Luck = 5,

        experience = ExpSetToLevel(8),

        base_xp_value = 45,
        
        CharSkills = {"NeutralAncientCurse":1, "NeutralPoisonThem":1},
    )

    CharDefs["e_ghoul"] = BuildCharTemplate(CharID = "e_ghoul",
        name = _("Ghoul"),
        IsMob = True,
        BattleSkin =  "ghoul", 
        
        
        base_health = 300,
        base_energy = 75,

        Strength = 5,
        Endurance = 3,
        Willpower = 4,
        Agility = 7,
        Dexterity = 6,
        Luck = 2,

        base_xp_value = 15,
        auto_attr_allocation = "rogue",
        
        CharSkills = {"NeutralTeamUp":1, "NeutralPreciseShot":1, "NeutralTwist":1, "NeutralHealThem":1, "NeutralASmallBlessing":1},
    )

    CharDefs["e_ghoul_big"] = BuildCharTemplate(CharID = "e_ghoul_big",
        name = _("Big ghoul"),
        IsMob = True,
        BattleSkin =  "ghoul_big", 

        base_health = 600,
        base_energy = 175,

        Strength = 5,
        Endurance = 3,
        Willpower = 4,
        Agility = 7,
        Dexterity = 6,
        Luck = 2,

        base_xp_value = 15,
        auto_attr_allocation = "rogue",
        
        CharSkills = {"NeutralTeamUp":1, "NeutralPreciseShot":1, "NeutralTwist":1, "NeutralHealThem":1, "NeutralASmallBlessing":1},
    )

    ### goblin fighters that attack the player if you go hostile on Vizura.
    CharDefs["e_goblin"] = BuildCharTemplate(CharID = "e_goblin",
        name = _("Goblin"),
        IsMob = True,
        BattleSkin =  "goblin", 
        
        base_health = 40,
        base_energy = 70,
        base_damage = 25,

        Strength = 0,
        Endurance = 12,
        Willpower = 0,
        Agility = 4,
        Dexterity = 10,
        Luck = 5,

        base_xp_value = 15,
        auto_attr_allocation = "rogue",

        CharSkills = {"NeutralTeamUp":1, "NeutralASmallBlessing":1},
    )

    CharDefs["e_bear"] = BuildCharTemplate(CharID = "e_bear",
        name = _("Bear"),
        IsMob = True,
        BattleSkin =  "bear", 

        base_health = 300,
        base_energy = 85,
        base_damage = 38,

        Strength = 0,
        Endurance = 18,
        Willpower = 0,
        Agility = 8,
        Dexterity = 4,
        Luck = 5,

        base_xp_value = 15,
        auto_attr_allocation = "hulk",

        experience = ExpSetToLevel(7),

        CharSkills = {"NeutralGreatTaunt":1, "NeutralSuperHeavyBlow":1},
    )

    LootDropData["e_bear"] = [
        {"ItemID":"animal_hide",
            "MinDropRolls":3,
            "MaxDropRolls":4,
            "ChancePerSingleEntry":1.0}]

    CharDefs["e_bear_white"] = BuildCharTemplate(CharID = "e_bear_white",
        name = _("Rhuvan"),
        IsMob = True,
        BattleSkin =  "bear_white", 

        base_health = 360,
        base_energy = 105,
        base_damage = 39,

        Strength = 0,
        Endurance = 22,
        Willpower = 0,
        Agility = 12,
        Dexterity = 6,
        Luck = 5,

        base_xp_value = 25,
        auto_attr_allocation = "hulk",

        experience = ExpSetToLevel(8),

        CharSkills = {"NeutralSuperHeavyBlow":1, "NeutralHumiliatingAttack":1},
    )

    LootDropData["e_bear_white"] = [
        {"ItemID":"white_bear_hide",
            "MinDropRolls":1,
            "MaxDropRolls":2,
            "ChancePerSingleEntry":1.0}]

    CharDefs["e_lizard_red"] = BuildCharTemplate(CharID = "e_lizard_red",
        name = _("Desert Skalith"),
        IsMob = True,
        BattleSkin =  "lizard_red", 

        base_health = 90,
        base_energy = 85,
        base_damage = 15,

        Strength = 0,
        Endurance = 16,
        Willpower = 0,
        Agility = 12,
        Dexterity = 6,
        Luck = 5,

        base_xp_value = 20,
        auto_attr_allocation = "hulk",
        
        CharSkills = {"NeutralPoisonAttack":1, "NeutralGettingSick":1},
    )

    LootDropData["e_lizard_red"] = [
        {"ItemID":"potion_heal_minor",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.20}]

    CharDefs["e_lizard_blue"] = BuildCharTemplate(CharID = "e_lizard_blue",
        name = _("Water Skalith"),
        IsMob = True,
        BattleSkin =  "lizard_blue", 

        base_health = 90,
        base_energy = 85,
        base_damage = 15,

        Strength = 0,
        Endurance = 14,
        Willpower = 0,
        Agility = 15,
        Dexterity = 8,
        Luck = 6,

        base_xp_value = 15,
        auto_attr_allocation = "hulk",
        
        CharSkills = {"NeutralPoisonAttack":1, "NeutralPoisonThem":1},
    )

    LootDropData["e_lizard_blue"] = [
        {"ItemID":"potion_heal_minor",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.20}]

    CharDefs["e_lizard_green"] = BuildCharTemplate(CharID = "e_lizard_green",
        name = _("Forest Skalith"),
        IsMob = True,
        BattleSkin =  "lizard_green",

        base_health = 140,
        base_energy = 95,
        base_damage = 15,

        Strength = 0,
        Endurance = 10,
        Willpower = 0,
        Agility = 15,
        Dexterity = 8,
        Luck = 5,

        base_xp_value = 15,
        auto_attr_allocation = "hulk",
        
        CharSkills = {"NeutralPoisonAttack":1, "NeutralTeamUp":1},
    )

    LootDropData["e_lizard_green"] = [
        {"ItemID":"potion_heal_minor",
        "MinDropRolls":1,
        "MaxDropRolls":2,
        "ChancePerSingleEntry":0.20}]

    CharDefs["e_wolf"] = BuildCharTemplate(CharID = "e_wolf",
        name = _("Wolf"),
        IsMob = True,
        BattleSkin =  "wolf", 

        base_health = 70,
        base_energy = 65,
        base_damage = 14,

        Strength = 0,
        Endurance = 8,
        Willpower = 0,
        Agility = 12,
        Dexterity = 8,
        Luck = 10,

        base_xp_value = 15,
        auto_attr_allocation = "hulk",

        CharSkills = {"NeutralTeamUp":1},
    )

    LootDropData["e_wolf"] = [
        {"ItemID":"animal_hide",
            "MinDropRolls":1,
            "MaxDropRolls":1,
            "ChancePerSingleEntry":1.0}]

    CharDefs["e_wolf_dire"] = BuildCharTemplate(CharID = "e_wolf_dire",
        name = _("Great Dire Wolf"),
        IsMob = True,
        BattleSkin =  "wolf_dire", 

        base_health = 170,
        base_energy = 165,
        base_damage = 28,

        Strength = 0,
        Endurance = 8,
        Willpower = 0,
        Agility = 12,
        Dexterity = 8,
        Luck = 10,

        base_xp_value = 15,
        auto_attr_allocation = "hulk",

        CharSkills = {"NeutralTeamUp":1},
    )

    LootDropData["e_wolf"] = [
        {"ItemID":"animal_hide",
            "MinDropRolls":1,
            "MaxDropRolls":1,
            "ChancePerSingleEntry":1.0}]

    CharDefs["e_stag"] = BuildCharTemplate(CharID = "e_stag",
        name = _("Stag"),
        IsMob = True,
        BattleSkin =  "stag", 

        base_health = 310,
        base_energy = 55,
        base_damage = 35,

        Strength = 0,
        Endurance = 10,
        Willpower = 0,
        Agility = 12,
        Dexterity = 8,
        Luck = 5,

        experience = ExpSetToLevel(6),

        base_xp_value = 15,
        auto_attr_allocation = "hulk",
        
        CharSkills = {"NeutralSuperHeavyBlow":1},
    )

    LootDropData["e_stag"] = [
        {"ItemID":"animal_hide",
            "MinDropRolls":1,
            "MaxDropRolls":1,
            "ChancePerSingleEntry":1.0},
        {"ItemID":"red_meat",
            "MinDropRolls":1,
            "MaxDropRolls":1,
            "ChancePerSingleEntry":1.0}]
    
#############
    CharDefs["e_merlanian_soldier"] = BuildCharTemplate(CharID = "e_merlanian_soldier",
        name = _("Merlanian Soldier"),
        IsMob = True,
        BattleSkin =  "merlanian_soldier", 

        base_health = 200,
        base_energy = 85,
        base_damage = 30,

        Strength = 0,
        Endurance = 16,
        Willpower = 0,
        Agility = 12,
        Dexterity = 6,
        Luck = 5,

        experience = ExpSetToLevel(11),

        base_xp_value = 20,
        auto_attr_allocation = "hulk",
        
        CharSkills = {"NeutralPoisonAttack":1, "NeutralGettingSick":1},
    )

    CharDefs["e_merlanian_general"] = BuildCharTemplate(CharID = "e_merlanian_general",
        name = _("Merlanian General"),
        IsMob = True,
        BattleSkin =  "merlanian_general", 

        base_health = 690,
        base_energy = 120,
        base_damage = 65,

        Strength = 0,
        Endurance = 16,
        Willpower = 0,
        Agility = 12,
        Dexterity = 6,
        Luck = 5,

        base_xp_value = 20,
        auto_attr_allocation = "hulk",

        experience = ExpSetToLevel(16),
        
        CharSkills = {"NeutralPoisonAttack":1, "NeutralGettingSick":1},
    )
    
    # a mob for story flashback shit
    CharDefs["shyahtan"] = BuildCharTemplate(CharID = "shyahtan",
        name = _("Shyahtan"),
        IsMob = True,
        BattleSkin =  "mc_transformed", 

        base_health = 1220,

        base_energy = 130,
        base_damage = 20,

        Strength = 10,
        Endurance = 16,
        Willpower = 10,
        Agility = 12,
        Dexterity = 16,
        Luck = 15,

        experience = ExpSetToLevel(32),

        # skills are auto-set to maxed out mc-transformed skills below
        CharSkills = {},
    )

init 3 python:
    # goes over all the skills in mc-transformed skill tree and adds all skills at max level to shyahtan
    for SkillBranch in ["offence", "defence", "support"]:
        for SkillID in Lib_BattleSkillTrees["parasiteBlack"][SkillBranch]:
            CharDefs["shyahtan"]["CharSkills"][SkillID] = SkillLib[SkillID].Level_Max

init python:
    CharDefs["e_corpse_eater"] = BuildCharTemplate(CharID = "e_corpse_eater",
        name = _("Corpse Eater"),
        IsMob = True,
        BattleSkin =  "corpse_eater", 

        base_health = 800,
        base_energy = 100,
        base_damage = 30,

        Strength = 7,
        Endurance = 8,
        Willpower = 3,
        Agility = 12,
        Dexterity = 6,
        Luck = 5,

        experience = ExpSetToLevel(11),

        base_xp_value = 20,
        auto_attr_allocation = "hulk",
        
        CharSkills = {"NeutralPoisonAttack":1, "NeutralGettingSick":1},
    )

    # TODO to raven: chars from here and below dont have base_xp_value set, which makes them reward 0 xp    
    CharDefs["e_succubus"] = BuildCharTemplate(CharID = "e_succubus",
        name = _("Succubus"),
        IsMob = True,
        BattleSkin =  "succubus", 

        base_health = 500,
        base_energy = 100,
        base_damage = 20,

        Strength = 5,
        Endurance = 5,
        Willpower = 9,
        Agility = 12,
        Dexterity = 8,
        Luck = 7,

        experience = ExpSetToLevel(10),
        
        CharSkills = {
            "NeutralTheGatesOfSevenHells":1
        },
    )

    CharDefs["e_x71"] = BuildCharTemplate(CharID = "e_x71",
        name = _("X-71"),
        IsMob = True,
        BattleSkin =  "x71", 

        base_health = 1020,
        base_energy = 100,
        base_damage = 20,

        Strength = 6,
        Endurance = 6,
        Willpower = 9,
        Agility = 12,
        Dexterity = 8,
        Luck = 7,

        experience = ExpSetToLevel(12),
        
        CharSkills = {
            "NeutralTwist":1, "NeutralPreciseShot":1, "NeutralItCouldHaveBeenWorse":1,
        },
    )

    CharDefs["e_the_face"] = BuildCharTemplate(CharID = "e_the_face",
        name = _("The Face"),
        IsMob = True,
        BattleSkin =  "theface",

        base_health = 1500,
        base_energy = 120,
        base_damage = 20,

        Strength = 5,
        Endurance = 5,
        Willpower = 9,
        Agility = 12,
        Dexterity = 8,
        Luck = 7,

        experience = ExpSetToLevel(12),
        
        CharSkills = {
            "NeutralTheGatesOfSevenHells":1, "NeutralTwist":1, "NeutralGettingSick":1, "NeutralSuperHeavyBlow":1,
        },
    )

    CharDefs["e_lizardmonster"] = BuildCharTemplate(CharID = "e_lizardmonster",
        name = _("Lizard monster"),
        IsMob = True,
        BattleSkin =  "lizardmonster",

        base_health = 650,
        base_energy = 150,
        base_damage = 20,

        Strength = 10,
        Endurance = 10,
        Willpower = 10,
        Agility = 10,
        Dexterity = 10,
        Luck = 16, 

        auto_attr_allocation = "fighter",

        #experience = ExpSetToLevel(10),

        CharSkills = {
            "NeutralPoisonAttack":1,
            "NeutralFrighten":1,
            "NeutralPreciseShot":1,
            "NeutralShakeTheGround":1,
            "NeutralJawsOfDeath":1,
            "BerserkerFrenziedState":1,
            "BerserkerHealingWounds":1,


        },
    )

    CharDefs["e_zombie_half"] = BuildCharTemplate(CharID = "e_zombie_half",
        name = _("Zombie"),
        IsMob = True,
        BattleSkin =  "zombie_half",

        base_health = 325,
        base_energy = 200,
        base_damage = 20,

        Strength = 9,
        Endurance = 8,
        Willpower = 3,
        Agility = 12,
        Dexterity = 6,
        Luck = 5,

        auto_attr_allocation = "fighter",

        experience = ExpSetToLevel(12),

        CharSkills = {
            "NeutralPoisonAttack":1,
            "NeutralFrighten":1,
            "NeutralTeamUp":1,
        },
    )

    CharDefs["e_zombie_fem"] = BuildCharTemplate(CharID = "e_zombie_fem",
        name = _("Zombie"),
        IsMob = True,
        BattleSkin =  "zombie_fem",

        base_health = 200,
        base_energy = 150,
        base_damage = 13,

        Strength = 7,
        Endurance = 8,
        Willpower = 3,
        Agility = 12,
        Dexterity = 6,
        Luck = 5,

        auto_attr_allocation = "fighter",

        experience = ExpSetToLevel(11),

        CharSkills = {
            "NeutralPoisonAttack":1,
            "NeutralFrighten":1,
        },
    )

    CharDefs["e_ghost_babyface"] = BuildCharTemplate(CharID = "e_ghost_babyface",
        name = _("Dark specter"), 
        IsMob = True,
        BattleSkin =  "ghost_babyface",

        base_health = 850,
        base_energy = 200,
        base_damage = 15,

        Strength = 7,
        Endurance = 8,
        Willpower = 3,
        Agility = 12,
        Dexterity = 6,
        Luck = 5,

        auto_attr_allocation = "fighter",

        experience = ExpSetToLevel(15),

        CharSkills = {
            "NeutralPoisonAttack":1,
            "NeutralFrighten":1,
            #"NeutralPreciseShot":1,
            #"NeutralShakeTheGround":1,
            #"NeutralJawsOfDeath":1,
            "BerserkerFrenziedState":1,
            "BerserkerHealingWounds":1,
        },
    )

    CharDefs["e_zombie_butcher"] = BuildCharTemplate(CharID = "e_zombie_butcher",
            name = _("Zombie butcher"),
            IsMob = True,
            BattleSkin =  "zombie_butcher",

            base_health = 1050,
            base_energy = 100,
            base_damage = 15,

            Strength = 7,
            Endurance = 8,
            Willpower = 3,
            Agility = 12,
            Dexterity = 6,
            Luck = 5,

            auto_attr_allocation = "fighter",

            experience = ExpSetToLevel(14),

            CharSkills = {
                "NeutralFrighten":1,
                "NeutralShakeTheGround":1,
                "NeutralSuperHeavyBlow":1,
        },
    )
    CharDefs["e_gator"] = BuildCharTemplate(CharID = "e_gator",
            name = _("Gator"),
            IsMob = True,
            BattleSkin =  "gator",

            base_health = 1050,
            base_energy = 100,
            base_damage = 15,

            Strength  = 7,
            Endurance = 8,
            Willpower = 3,
            Agility   = 12,
            Dexterity = 6,
            Luck      = 5,

            auto_attr_allocation = "fighter",

            experience = ExpSetToLevel(14),

            CharSkills = {
                "NeutralFrighten":1,
                "NeutralShakeTheGround":1,
                "NeutralSuperHeavyBlow":1,
        },
    )
    CharDefs["e_nightmare_head"] = BuildCharTemplate(CharID = "e_nightmare_head",
        name = _("Nightmare head"),
        IsMob = True,
        BattleSkin =  "nightmare_head",

        base_health = 1550,
        base_energy = 100,
        base_damage = 15,

        Strength = 7,
        Endurance = 8,
        Willpower = 3,
        Agility = 12,
        Dexterity = 6,
        Luck = 5,

        auto_attr_allocation = "fighter",

        experience = ExpSetToLevel(16),

        CharSkills = {
            "NeutralFrighten":1,
            "NeutralIgniteThem":1,
            "NeutralItCouldHaveBeenWorse":1,
        },
    )
    CharDefs["e_nightmare_left_hand"] = BuildCharTemplate(CharID = "e_nightmare_left_hand",
        name = _("Left hand"),
        IsMob = True,
        BattleSkin =  "nightmare_right_hand",

        base_health = 750,
        base_energy = 100,
        base_damage = 15,

        Strength = 7,
        Endurance = 8,
        Willpower = 3,
        Agility = 12,
        Dexterity = 6,
        Luck = 5,

        auto_attr_allocation = "fighter",

        experience = ExpSetToLevel(12),

        CharSkills = {
            "NeutralHealThem":1,
            "NeutralTeamUp":1,
            "NeutralASmallBlessing":1,
        },
    )
    CharDefs["e_nightmare_right_hand"] = BuildCharTemplate(CharID = "e_nightmare_right_hand",
        name = _("Right hand"),
        IsMob = True,
        BattleSkin =  "nightmare_left_hand",

        base_health = 750,
        base_energy = 100,
        base_damage = 15,

        Strength = 7,
        Endurance = 8,
        Willpower = 3,
        Agility = 12,
        Dexterity = 6,
        Luck = 5,

        auto_attr_allocation = "fighter",

        experience = ExpSetToLevel(12),

        CharSkills = {
            "NeutralFrighten":1,
            "NeutralShakeTheGround":1,
            "NeutralSuperHeavyBlow":1,
        },
    )
    CharDefs["e_floating_eye"] = BuildCharTemplate(CharID = "e_floating_eye",
        name = _("Floating eye"), 
        IsMob = True,
        BattleSkin =  "floating_eye",

        base_health = 750,
        base_energy = 200,
        base_damage = 15,

        Strength = 7,
        Endurance = 8,
        Willpower = 3,
        Agility = 12,
        Dexterity = 6,
        Luck = 5,

        auto_attr_allocation = "fighter",

        experience = ExpSetToLevel(11),

        CharSkills = {
            "NeutralFrighten":1,
            "NeutralPreciseShot":1,
            "BerserkerHealingWounds":1,
        },
    )
    CharDefs["e_hugo"] = BuildCharTemplate(CharID = "e_hugo",
        name = _("Hugo"), 
        IsMob = True,
        BattleSkin =  "hugo",

        base_health = 1250,
        base_energy = 180,
        base_damage = 15,

        Strength = 7,
        Endurance = 9,
        Willpower = 3,
        Agility = 11,
        Dexterity = 6,
        Luck = 5,

        auto_attr_allocation = "fighter",

        experience = ExpSetToLevel(14),

        CharSkills = {
            "NeutralFrighten":1,
            "NeutralShakeTheGround":1,
            "NeutralSuperHeavyBlow":1,
            "BerserkerHealingWounds":1,
        },
    )
    CharDefs["e_monstorus_experiment"] = BuildCharTemplate(CharID = "e_monstorus_experiment",
        name = _("Monstrous Experiment"), 
        IsMob = True,
        BattleSkin =  "hugo",

        base_health = 790,
        base_energy = 180,
        base_damage = 14,

        Strength = 7,
        Endurance = 9,
        Willpower = 3,
        Agility = 11,
        Dexterity = 6,
        Luck = 5,

        auto_attr_allocation = "fighter",

        experience = ExpSetToLevel(14),

        CharSkills = {
            "NeutralFrighten":1,
            "NeutralSuperHeavyBlow":1,
            "BerserkerHealingWounds":1,
        },
    )
