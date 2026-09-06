init python:
    Lib_BattleSkillTrees["rogueWolfForm"] = {
        "name":             _("Wolf form"),
        "skills_string":    _("Wolf form skills"),
        "offence":{
            "RogueWolfRipNTear":{
                "Reqs_Attributes":{"Strength" : 2, "Agility": 5},
                "Reqs_SkillIDs":{},
            },
            "RogueWolfFeralStrikes":{
                "Reqs_Attributes":{"Strength" : 8, "Agility": 8},
                "Reqs_SkillIDs":{"RogueWolfRipNTear"},
            },
            "RogueWolfRecklessBeast":{
                "Reqs_Attributes":{"Strength" : 8, "Agility": 10},
                "Reqs_SkillIDs":{},
            },
            "RogueWolfPoisonedFangs":{
                "Reqs_Attributes":{"Strength" : 8, "Agility": 12},
                "Reqs_SkillIDs":{"RogueWolfRipNTear"},
            },
            "RogueWolfSuddenStrike":{
                "Reqs_Attributes":{"Strength" : 8, "Agility": 12},
                "Reqs_SkillIDs":{"RogueWolfRipNTear"},
            },
        },
        "defence":{
            "RogueWolfDanceOfTheWolves":{
                "Reqs_Attributes":{"Dexterity" : 8, "Agility": 6},
                "Reqs_SkillIDs":{},
            },
            "RogueWolfLupineInstinct":{
                "Reqs_Attributes":{"Endurance" : 6, "Agility": 8},
                "Reqs_SkillIDs":{"RogueWolfDanceOfTheWolves"},
            },
            "RogueWolfFeralProtection":{
                "Reqs_Attributes":{"Endurance" : 8, "Willpower": 6},
                "Reqs_SkillIDs":{},
            },
            "RogueWolfHideNSeek":{
                "Reqs_Attributes":{"Endurance" : 8, "Willpower": 6},
                "Reqs_SkillIDs":{},
            },
        },
        "support":{
            "RogueWolfHowl":{
                "Reqs_Attributes":{"Endurance" : 6, "Willpower": 6, "Dexterity": 8},
                "Reqs_SkillIDs":{},
            },
            "RogueWolfForThePack":{
                "Reqs_Attributes":{"Endurance" : 6, "Willpower": 6, "Dexterity": 8},
                "Reqs_SkillIDs":{},
            },
            "RogueWolfSnarl":{
                "Reqs_Attributes":{"Endurance" : 10, "Willpower": 8, "Dexterity": 10},
                "Reqs_SkillIDs":{},
            },
        },
    }
