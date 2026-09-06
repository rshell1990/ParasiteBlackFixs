init python:
    Lib_BattleSkillTrees["scout"] = {
        "name":             _("Scout"),
        "skills_string":    _("Scout skills"),
        "offence":{
            "ScoutFastAndPreciseAttack":{
                "Reqs_Attributes":{"Strength" : 3, "Agility" : 3},
                "Reqs_SkillIDs":{},
            },
            "ScoutBleedEmDry":{
                "Reqs_Attributes":{"Strength" : 4, "Agility" : 6},
                "Reqs_SkillIDs":{},
            },
            "ScoutDanceOfDeath":{
                "Reqs_Attributes":{"Strength" : 4, "Agility" : 8},
                "Reqs_SkillIDs":{"ScoutFastAndPreciseAttack"},
            },
            "ScoutRainOfDeath":{
                "Reqs_Attributes":{"Strength" : 5, "Agility" : 10, "Willpower" : 4},
                "Reqs_SkillIDs":{},
            },
            "ScoutPerfectStrike":{
                "Reqs_Attributes":{"Strength" : 10, "Agility" : 10},
                "Reqs_SkillIDs":{"ScoutDanceOfDeath"},
            },
            "ScoutTheNorthStarStrike":{
                "Reqs_Attributes":{"Strength" : 10, "Agility" : 15},
                "Reqs_SkillIDs":{"ScoutPerfectStrike"},
            },
        },
        "defence":{
            "ScoutDefensiveMode":{
                "Reqs_Attributes":{"Agility" : 2, "Endurance" : 2},
                "Reqs_SkillIDs":{},
            },
            "ScoutPrepare":{
                "Reqs_Attributes":{"Agility" : 4, "Endurance" : 4},
                "Reqs_SkillIDs":{},
            },
            "ScoutPreparationFromTheSkilled":{
                "Reqs_Attributes":{"Agility" : 6, "Endurance" : 4, "Strength" : 6},
                "Reqs_SkillIDs":{"ScoutPrepare"},
            },
        },
        "support":{
            "ScoutKeepUp":{
                "Reqs_Attributes":{"Endurance" : 2, "Strength" : 4},
                "Reqs_SkillIDs":{},
            },
            "ScoutAttackTime":{
                "Reqs_Attributes":{"Endurance" : 4, "Strength" : 8},
                "Reqs_SkillIDs":{},
            },
            "ScoutEaglesEye":{
                "Reqs_Attributes":{"Agility" : 5, "Strength" : 10, "Willpower" : 5},
                "Reqs_SkillIDs":{},
            },
        },
    }