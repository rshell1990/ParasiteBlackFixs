init python:
    Lib_BattleSkillTrees["parasiteBlack"] = {
        "name":             _("Parasite Black"),
        "skills_string":    _("Parasite skills"),
        "offence":{
            "ParasiteBlackRazorSlash":{
                "Reqs_Attributes":{"Strength" : 5, "Agility" : 4},
                "Reqs_SkillIDs":{},
            },
            "ParasiteBlackVenomousStrike":{
                "Reqs_Attributes":{"Strength" : 7, "Agility" : 4},
                "Reqs_SkillIDs":{"ParasiteBlackRazorSlash"},
            },
            "ParasiteBlackAcidicBurst":{
                "Reqs_Attributes":{"Strength" : 10},
                "Reqs_SkillIDs":{},
            },
            "ParasiteBlackUnstoppable":{
                "Reqs_Attributes":{"Strength" : 20, "Agility" : 5, "Willpower": 7},
                "Reqs_SkillIDs":{"ParasiteBlackAcidicBurst"},
            },
            "ParasiteBlackWindBreaker":{
                "Reqs_Attributes":{"Strength" : 25, "Agility" : 5, "Willpower": 10},
                "Reqs_SkillIDs":{"ParasiteBlackUnstoppable"},
            },
            "ParasiteBlackParasiteAttack":{
                "Reqs_Attributes":{"Strength" : 20, "Willpower": 10},
                "Reqs_SkillIDs":{"ParasiteBlackRazorSlash"},
            },
        },
        "defence":{
            "ParasiteBlackTerrifyingScream":{
                "Reqs_Attributes":{"Strength" : 6, "Agility" : 4},
                "Reqs_SkillIDs":{},
            },
            "ParasiteBlackParasiticSwarm":{
                "Reqs_Attributes":{"Strength" : 8, "Endurance" : 6},
                "Reqs_SkillIDs":{"ParasiteBlackTerrifyingScream"},
            },
            "ParasiteBlackPassiveAggressiveMode":{
                "Reqs_Attributes":{"Strength" : 10, "Endurance" : 6, "Willpower": 6},
                "Reqs_SkillIDs":{},
            },
            "ParasiteBlackHealingWorms":{
                "Reqs_Attributes":{"Strength" : 12, "Endurance" : 8, "Willpower": 8},
                "Reqs_SkillIDs":{"ParasiteBlackPassiveAggressiveMode"},
            },
        },
        "support":{
            "ParasiteBlackPerfectOrganism":{
                "Reqs_Attributes":{"Strength" : 10, "Willpower": 10},
                "Reqs_SkillIDs":{},
            },
            "ParasiteBlackParasiteBalance":{
                "Reqs_Attributes":{"Strength" : 20, "Willpower": 20, "Endurance" : 10},
                "Reqs_SkillIDs":{"ParasiteBlackPassiveAggressiveMode"},
            },
        },
    }