init python:
    Lib_BattleSkillTrees["berserker"] = {
        "name":             _("Berserker"),
        "skills_string":    _("Berserker skills"),
        "offence":{
            "BerserkerDeathblow":{
                "Reqs_Attributes":{"Strength" : 6, "Endurance" : 6},
                "Reqs_SkillIDs":{},
            },
            "BerserkerCrush":{
                "Reqs_Attributes":{"Strength" : 8, "Endurance" : 8},
                "Reqs_SkillIDs":{},
            },
            "BerserkerBloodForTheBloodGod":{
                "Reqs_Attributes":{"Strength" : 8, "Endurance" : 12},
                "Reqs_SkillIDs":{},
            },
            "BerserkerFrenziedState":{
                "Reqs_Attributes":{"Strength" : 12, "Endurance" : 15},
                "Reqs_SkillIDs":{},
            },
        },
        "defence":{
            "BerserkerUnbreakable":{
                "Reqs_Attributes":{"Endurance" : 6},
                "Reqs_SkillIDs":{},
            },
            "BerserkerWarCry":{
                "Reqs_Attributes":{"Endurance" : 8},
                "Reqs_SkillIDs":{},
            },
            "BerserkerFuriousWarCry":{
                "Reqs_Attributes":{"Endurance" : 12, "Willpower" : 8},
                "Reqs_SkillIDs":{"BerserkerWarCry"},
            },
            "BerserkerFinalSpirit":{
                "Reqs_Attributes":{"Endurance" : 15, "Strength" : 8},
                "Reqs_SkillIDs":{},
            },
            "BerserkerDeclareWar":{
                "Reqs_Attributes":{"Endurance" : 20, "Willpower" : 10},
                "Reqs_SkillIDs":{"BerserkerFuriousWarCry"},
            },
            "BerserkerHealingWounds":{
                "Reqs_Attributes":{"Endurance" : 20, "Willpower" : 10},
                "Reqs_SkillIDs":{"BerserkerUnbreakable"},
            },
        },
        "support":{
            "BerserkerBerserkerTime":{
                "Reqs_Attributes":{"Endurance" : 12, "Strength": 8},
                "Reqs_SkillIDs":{},
            },
            "BerserkerTheCryOfATrueWarrior":{
                "Reqs_Attributes":{"Endurance" : 15, "Willpower": 15},
                "Reqs_SkillIDs":{},
            },
        },
    }