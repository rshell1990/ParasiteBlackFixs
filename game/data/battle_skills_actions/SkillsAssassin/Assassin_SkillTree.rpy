init python:
    Lib_BattleSkillTrees["assassin"] = {
        "name":             _("Assassin"),
        "skills_string":    _("Assassin skills"),
        "offence":{
            "AssassinDeathByAThousandCuts":{
                "Reqs_Attributes":{}, # <these can or can not be present, theres an "in" check anyway
                "Reqs_SkillIDs":{},
            },
            "AssassinRecklessBackstab":{
                "Reqs_Attributes":{"Strength":4, "Agility":8, "Luck":11},
                "Reqs_SkillIDs":{},
            },
            "AssassinCalculatingSwipe":{
                "Reqs_Attributes":{"Agility":10, "Dexterity":7, "Luck":6},
                "Reqs_SkillIDs":{},
            },
            "AssassinTreacherousSlice":{
                "Reqs_Attributes":{"Strength":8, "Luck":7},
                "Reqs_SkillIDs":{},
            },
            "AssassinCriticalBlows":{
                "Reqs_Attributes":{"Strength":9, "Luck":10},
                "Reqs_SkillIDs":{},
            }
        },
        "defence":{
            "AssassinAcrobaticDance":{
                "Reqs_Attributes":{"Agility":7, "Dexterity":8},
                "Reqs_SkillIDs":{},
            },
            "AssassinRecover":{
                "Reqs_Attributes":{"Willpower":7},
                "Reqs_SkillIDs":{},
            },
            "AssassinDarkSwap":{
                "Reqs_Attributes":{"Endurance":8, "Willpower":10},
                "Reqs_SkillIDs":{},
            },
        },
        "support":{
            "AssassinADarkGift":{
                "Reqs_Attributes":{},
                "Reqs_SkillIDs":{},
            },
            "AssassinAThousandDaggers":{
                "Reqs_Attributes":{"Dexterity":6, "Willpower":6, "Luck":5},
                "Reqs_SkillIDs":{},
            },
            "AssassinBleedingHearts":{
                "Reqs_Attributes":{"Agility":7, "Willpower":10},
                "Reqs_SkillIDs":{},
            },
            "AssassinALovingKissOfDeath":{
                "Reqs_Attributes":{"Willpower":9},
                "Reqs_SkillIDs":{},
            },
        },
    }