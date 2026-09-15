init 1 python:
    CharDefs["void_spirit"] = BuildCharTemplate(CharID = "void_spirit",
        name = _("Void Spirit"),
        BattleSkin =  "theface", # "e_the_face" is a CharID, not a skin; not in skinLib
        base_health = 90,
        base_damage = 15,
        base_energy = 55,

        Strength = 10,
        Endurance = 10,
        Willpower = 10,
        Agility = 10,
        Dexterity = 10,
        Luck = 10,

        base_xp_value = 20,
        auto_attr_allocation = "fighter",
        CharSkills = {"NeutralTeamUp":1, "NeutralASmallBlessing":1},
        )
