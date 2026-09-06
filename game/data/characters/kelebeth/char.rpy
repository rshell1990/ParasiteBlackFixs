define KELEBETH = Character(_("Kelebeth"), image = "kelebeth")
init python:
    CharDefs["kelebeth"] = BuildCharTemplate(CharID = "kelebeth",
        name = _("Kelebeth"),
        portrait = "images/characters/kelebeth/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"naked"}, # naked only at the time of writing

        BattleSkin =  "succubus", 

        base_health = 820,
        base_energy = 150,
        base_damage = 25,

        Strength = 5,
        Endurance = 5,
        Willpower = 9,
        Agility = 12,
        Dexterity = 8,
        Luck = 8,

        experience = ExpSetToLevel(13),

        CharSkills = {
            "NeutralHellfireWall":1,
            "NeutralInfernalBlast":1,
        },
    )
    RelText["kelebeth"] = {}
    RelText["kelebeth"]["initial"] = {
        "order":0,
        "text":_("A succubus from the lust realm of the seven hells... She seems particularly interested in Shyahtan.")}

    config.tag_layer["kelebeth"] = "characters"
