default TAREK = Character(_("Tarek"), image = "tarek")

init python:
    CharDefs["tarek"] = BuildCharTemplate(CharID = "tarek",
                                        name = _("Tarek"),
                                        BattleSkin = "skin_tarek",
                                        
                                        base_health = 200,
                                        base_energy = 80,
                                        base_damage = 35,
                                        
                                        Strength = 0,
                                        Endurance = 14,
                                        Willpower = 0,
                                        Agility = 10,
                                        Dexterity = 8,
                                        Luck = 6,

                                        base_xp_value = 35,
                                        auto_attr_allocation = "fighter",
                                        
                                        CharSkills = {"NeutralPreciseShot":1, "NeutralIgniteThem":1},
                                        )
    LootDropData["tarek"] = [
        {"ItemID":"gold",
        "MinDropRolls":1,
        "MaxDropRolls":1,
        "ChancePerSingleEntry":1.00,
        "AmountPerSingleEntry":285},

        {"ItemID":"tarek_blade",
        "MinDropRolls":1,
        "MaxDropRolls":1,
        "ChancePerSingleEntry":1.0}]

    config.tag_layer["tarek"] = "characters"

    config.tag_layer["cg_tarek_nijah_hostage"] = "characters"
    config.tag_layer["cg_tarek_nijah_hostage_killed"] = "characters"
