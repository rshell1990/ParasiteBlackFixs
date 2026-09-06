init python:
    Lib_BattleSkillTrees["rogue"] = {
        "name":             _("Rogue"),
        "skills_string":    _("Rogue skills"),
        "offence":{
            "RogueFeralStrike":{
                "Reqs_Attributes":{"Strength" : 2, "Agility" : 5},
                "Reqs_SkillIDs":{},
            },
            "RoguePiercingShot":{
                "Reqs_Attributes":{"Agility" : 8, "Dexterity": 5},
                "Reqs_SkillIDs":{},
            },
            "RogueSquall":{
                "Reqs_Attributes":{"Agility" : 10, "Dexterity": 10},
                "Reqs_SkillIDs":{"RoguePiercingShot"},
            },
            "RogueVenomousStrike":{
                "Reqs_Attributes":{"Agility" : 15, "Dexterity": 10},
                "Reqs_SkillIDs":{},
            },
            "RogueWipe":{
                "Reqs_Attributes":{"Agility" : 20, "Dexterity": 10},
                "Reqs_SkillIDs":{"RogueSquall"},
            },
        },
        "defence":{
            "RogueResilience":{
                "Reqs_Attributes":{"Dexterity" : 4, "Endurance" : 4},
                "Reqs_SkillIDs":{},
            },
            "RogueCalmStep":{
                "Reqs_Attributes":{"Dexterity" : 8, "Endurance" : 4},
                "Reqs_SkillIDs":{"RogueResilience"},
            },
            "RogueForbiddenPower":{
                "Reqs_Attributes":{"Strength" : 5, "Agility" : 15, "Dexterity" : 10},
                "Reqs_SkillIDs":{},
            },
            "RogueDarkening":{
                "Reqs_Attributes":{"Strength" : 5, "Agility" : 15, "Dexterity" : 15},
                "Reqs_SkillIDs":{"RogueResilience"},
            },
        },
        "support":{
            "RogueAcrobaticManeuvers":{
                "Reqs_Attributes":{"Agility" : 4, "Dexterity" : 4},
                "Reqs_SkillIDs":{},
            },
            "RogueTeamUp":{
                "Reqs_Attributes":{"Agility" : 4, "Dexterity" : 6},
                "Reqs_SkillIDs":{},
            },
            "RogueHowlOfWar":{
                "Reqs_Attributes":{"Agility" : 10, "Dexterity" : 10},
                "Reqs_SkillIDs":{"RogueAcrobaticManeuvers"},
            },
        },
    }