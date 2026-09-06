init python:
    Lib_BattleSkillTrees["slime"] = {
        "name":             _("Slime"),
        "skills_string":    _("Slime skills"),
        "offence":{
            "SlimeAcidicSplash":{
                "Reqs_Attributes":{"Strength" : 2, "Willpower" : 5},
                "Reqs_SkillIDs":{},
            },
            "SlimeCorrosiveCascade":{
                "Reqs_Attributes":{"Strength" : 4, "Willpower" : 7},
                "Reqs_SkillIDs":{"SlimeAcidicSplash"},
            },
        },
        "defence":{
            "SlimeAdaptiveDefense":{
                "Reqs_Attributes":{"Endurance" : 2, "Willpower" : 5},
                "Reqs_SkillIDs":{},
            },
            "SlimeMalleableForm":{
                "Reqs_Attributes":{"Endurance" : 2, "Willpower" : 10},
                "Reqs_SkillIDs":{"SlimeAdaptiveDefense"},
            },
            "SlimeExpandShape":{
                "Reqs_Attributes":{"Endurance" : 5, "Willpower" : 10},
                "Reqs_SkillIDs":{},
            },
        },
        "support":{
            "SlimeFirstAid":{
                "Reqs_Attributes":{"Willpower" : 5},
                "Reqs_SkillIDs":{},
            },
            "SlimeSlimeRecharge":{
                "Reqs_Attributes":{"Willpower" : 8},
                "Reqs_SkillIDs":{},
            },
            "SlimeRegenerativeMire":{
                "Reqs_Attributes":{"Willpower" : 10},
                "Reqs_SkillIDs":{"SlimeFirstAid"},
            },
            "SlimeSoothingGel":{
                "Reqs_Attributes":{"Endurance" : 4, "Willpower" : 8},
                "Reqs_SkillIDs":{},
            },
            "SlimePrimordialUnity":{
                "Reqs_Attributes":{"Endurance" : 4, "Willpower" : 12},
                "Reqs_SkillIDs":{"SlimeSoothingGel"},
            },
            "SlimeFirmingGel":{
                "Reqs_Attributes":{"Endurance" : 6, "Willpower" : 14},
                "Reqs_SkillIDs":{"SlimePrimordialUnity"},
            },
            "SlimeSharingLife":{
                "Reqs_Attributes":{"Endurance" : 10, "Willpower" : 20},
                "Reqs_SkillIDs":{"SlimeRegenerativeMire"},
            },
        },
    }

