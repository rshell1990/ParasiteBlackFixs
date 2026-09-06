default BORRAS = Character(_("Borras"), image = "borras")
init python:
    CharDefs["borras"] = BuildCharTemplate(CharID = "borras",
        name = _("Borras"),
        BattleSkin =  "borras", 

        portrait = "images/characters/borras/portrait.webp",

        RelTextIDs = {"initial"},

        base_health = 160,

        Strength = 14,
        Endurance = 13,
        Willpower = 15,
        Agility = 8,
        Dexterity = 7,

        CharSkills = {"WarriorHeavySlash":1, "WarriorDualStrike":1},

        experience = ExpSetToLevel(10))

    config.tag_layer["borras"] = "characters"

    RelText["borras"] = {}
    RelText["borras"]["initial"] = {
        "order":0,
        "text":_("Captain Duprey's right-hand man, a skilled a decorated warrior.")}

    RelText["borras"]["prol_killed"] = {
        "order":1,
        "text":_("He died a horrible death during our first mission together.")}