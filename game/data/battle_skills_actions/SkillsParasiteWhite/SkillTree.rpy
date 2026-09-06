init python:
    Lib_BattleSkillTrees["parasiteWhite"] = {
        "name":             _("Parasite White"),
        "skills_string":    _("Parasite skills"),
        "offence":{
            "ParasiteWhiteFireballCharge":{
                "Reqs_Attributes":{"Strength" : 6},
                "Reqs_SkillIDs":{},
            },
            "ParasiteWhiteScorchedEarth":{
                "Reqs_Attributes":{"Strength" : 8},
                "Reqs_SkillIDs":{"ParasiteWhiteFireballCharge"},
            },
            "ParasiteWhiteCrimsonSky":{
                "Reqs_Attributes":{"Strength" : 12, "Willpower": 8},
                "Reqs_SkillIDs":{"ParasiteWhiteScorchedEarth"},
            },
            "ParasiteWhiteEternalFire":{
                "Reqs_Attributes":{"Strength" : 15, "Willpower": 12},
                "Reqs_SkillIDs":{"ParasiteWhiteCrimsonSky"},
            },
            "ParasiteWhiteParasiteCurse":{
                "Reqs_Attributes":{"Strength" : 8, "Willpower": 8, "Agility" : 8},
                "Reqs_SkillIDs":{},
            },
            "ParasiteWhiteCursedConnection":{
                "Reqs_Attributes":{"Strength" : 15, "Willpower": 10, "Agility" : 10},
                "Reqs_SkillIDs":{},
            },
        },
        "defence":{
            "ParasiteWhiteFieryCounter":{
                "Reqs_Attributes":{"Willpower" : 6, "Endurance" : 8},
                "Reqs_SkillIDs":{},
            },
            "ParasiteWhiteRegenerativeCocoon":{
                "Reqs_Attributes":{"Willpower" : 8, "Endurance" : 8},
                "Reqs_SkillIDs":{},
            },
            "ParasiteWhiteInfernalParasite":{
                "Reqs_Attributes":{"Willpower" : 10, "Endurance" : 8},
                "Reqs_SkillIDs":{},
            },
            "ParasiteWhiteAllForOne":{
                "Reqs_Attributes":{"Willpower" : 10, "Endurance" : 10, "Strength" : 10},
                "Reqs_SkillIDs":{"ParasiteWhiteInfernalParasite"},
            },
        },
        "support":{
            "ParasiteWhiteGerminatingParasites":{
                "Reqs_Attributes":{"Endurance" : 8, "Willpower": 8},
                "Reqs_SkillIDs":{},
            },
            "ParasiteWhiteProtectiveParasites":{
                "Reqs_Attributes":{"Endurance" : 15, "Willpower": 15, "Strength" : 20},
                "Reqs_SkillIDs":{"ParasiteWhiteGerminatingParasites"},
            },
        },
    }