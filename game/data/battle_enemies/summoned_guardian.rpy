init python:
    # A temporary battle-only ally created by the Summoner's Summon skill.
    # It is a mob so it is built fresh for every battle and never changes story
    # character data or awards loot.
    CharDefs["e_summoned_guardian"] = BuildCharTemplate(
        CharID = "e_summoned_guardian",
        name = _("Spectral Guardian"),
        IsMob = True,
        BattleSkin = "ghost_babyface",

        base_health = 75,
        base_damage = 12,
        base_energy = 55,

        Strength = 5,
        Endurance = 7,
        Willpower = 5,
        Agility = 7,
        Dexterity = 5,
        Luck = 5,

        base_xp_value = 0,
        auto_attr_allocation = "fighter",
        CharSkills = {"NeutralTeamUp": 1, "NeutralASmallBlessing": 1},
        )
