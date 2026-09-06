init python:
    Lib_BattleSkillTrees["warrior"] = {
        "name":             _("Warrior"),
        "skills_string":    _("Warrior skills"),
        "offence":{
            "WarriorHeavySlash":{
                "Reqs_Attributes":{"Strength" : 5},
                "Reqs_SkillIDs":{},
            },
            "WarriorDualStrike":{
                "Reqs_Attributes":{"Strength" : 6, "Agility" : 5},
                "Reqs_SkillIDs":{},
            },
            "WarriorFlailingStrikes":{
                "Reqs_Attributes":{"Strength" : 10, "Agility" : 8},
                "Reqs_SkillIDs":{},
            },
            "WarriorObliteratingBlow":{
                "Reqs_Attributes":{"Strength" : 14},
                "Reqs_SkillIDs":{"WarriorHeavySlash"},
            },
            "WarriorFinalBlow":{
                "Reqs_Attributes":{"Strength" : 14, "Agility" : 8},
                "Reqs_SkillIDs":{"WarriorDualStrike"},
            },
            "WarriorWhirlwindOfSteel":{
                "Reqs_Attributes":{"Strength" : 20},
                "Reqs_SkillIDs":{"WarriorFlailingStrikes"},
            },
        },
        "defence":{
            "WarriorDodge":{
                "Reqs_Attributes":{"Agility" : 4},
                "Reqs_SkillIDs":{},
            },
            "WarriorDefensiveStance":{
                "Reqs_Attributes":{"Strength" : 10, "Endurance" : 5},
                "Reqs_SkillIDs":{},
            },
            "WarriorTheDodgeMaster":{
                "Reqs_Attributes":{"Strength" : 10, "Agility" : 8},
                "Reqs_SkillIDs":{"WarriorDodge"},
            },
            "WarriorWarriorStance":{
                "Reqs_Attributes":{"Strength" : 10, "Endurance" : 10},
                "Reqs_SkillIDs":{"WarriorDefensiveStance"},
            },
        },
        "support":{
            "WarriorGuardiansShield":{
                "Reqs_Attributes":{"Endurance" : 5},
                "Reqs_SkillIDs":{},
            },
            "WarriorLeadersCall":{
                "Reqs_Attributes":{"Strength" : 15, "Endurance" : 5},
                "Reqs_SkillIDs":{},
            },
        },
    }
