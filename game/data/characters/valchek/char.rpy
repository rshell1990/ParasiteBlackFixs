default VALCHEK = Character(_("Valchek"), image = "valchek")

init python:
    CharDefs["valchek"] = BuildCharTemplate(CharID = "valchek",
        portrait = "images/characters/valchek/portrait_hood.webp", 
        name = _("Valchek"),
        RelTextIDs = {"initial"},

        BattleSkin =  "valchek",
        CharSkills = {"NeutralDodgeThis":1, "NeutralFastAndDeadly":1, "NeutralSmokeBomb":1},

        base_health = 90,
        base_damage = 15,
        base_energy = 55,

        Strength = 0,
        Endurance = 4,
        Willpower = 0,
        Agility = 10,
        Dexterity = 10,
        Luck = 15,

        experience = ExpSetToLevel(10), 

        base_xp_value = 20,
        auto_attr_allocation = "rogue",

        ExtraData = {
            "clothes":"rags", # rags / ???
            })

    config.tag_layer["valchek"] = "characters"
    config.tag_layer["valchek_hood"] = "characters"