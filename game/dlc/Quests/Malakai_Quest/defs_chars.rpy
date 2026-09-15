init 1 python:
    CharDefs["colossalbeast"] = BuildCharTemplate(CharID = "colossalbeast",
        name = _("Colossal Beast"),
        BattleSkin =  "abomination", # placeholder skin, "e_titan" doesn't exist in skinLib
        base_health = 90,
        base_damage = 15,
        base_energy = 55,

        Strength = 5,
        Endurance = 7,
        Willpower = 5,
        Agility = 7,
        Dexterity = 5,
        Luck = 5,

        base_xp_value = 20,
        auto_attr_allocation = "fighter",
        CharSkills = {"NeutralTeamUp":1, "NeutralASmallBlessing":1},
        )