default VES = Character(_("Ves"), image="ves")

init python:
    CharDefs["ves"] = BuildCharTemplate(
        CharID = "ves",
        BattleSkin =  "ves",

        Strength =  10,
        Endurance = 10,
        Willpower = 6,
        Agility =   8,
        Dexterity = 6,
        Luck =      5,

        BattleClass = "berserker",

        CharSkills = {"BerserkerDeathblow":3, "BerserkerCrush":2, "BerserkerUnbreakable":5},

        portrait = "images/characters/ves/portrait.webp",

        experience = ExpSetToLevel(8),

        RelTextIDs = {"initial"},
        name = _("Ves"),
        ExtraData = {
            "love":False,
            "clothes":"normal"
        },
        IsCompanion = True,
    )

    config.tag_layer["ves"] = "characters"
    config.tag_layer["cg_ves_maid_kneel"] = "characters"

    RelText["ves"] = {}
    # initial
    RelText["ves"]["initial"] = {
        "order":0,
        "text":_("An orc residing in the Valley of death, stranded from her people. Our people are at war still, despite the demorai invasion, so there's still a great deal of mistrust between us, yet for now, we share an uneasy truce.")}

    # add after bath scene
    RelText["ves"]["after_bath"] = {
        "order":1,
        "text":_("Our time together has changed our perceptions of each other greatly. Whereas once, I saw an enemy, now I see a friend. ...And perhaps, something more? The more I get to know her, the more I realize how strangely beautiful she is...")}
