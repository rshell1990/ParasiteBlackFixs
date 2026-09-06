default SYPHA = Character(_("Sypha"), image = "sypha")

init python:
    CharDefs["sypha"] = BuildCharTemplate(
        CharID = "sypha",
        name = _("Sypha"),
        portrait = "images/characters/sypha/portrait.webp",
        BattleSkin = "sypha",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"}, # normal, normal_2, naked ... (theres more just check imagedef)

        # copied mc
        # Strength =  5,
        # Endurance = 4,
        # Willpower = 5,
        # Agility =   6,
        # Dexterity = 6,
        # Luck =      6,

        BattleClass = "assassin",
        CharSkills = {
            "AssassinDeathByAThousandCuts":1,
            "AssassinADarkGift":1,
        },

        IsCompanion = True,
    )

    config.tag_layer["sypha"] = "characters"

    RelText["sypha"] = {}
    # initial
    RelText["sypha"]["initial"] = {
        "order":0,
        "text":_("A mysterious, beautiful, Demorai girl who helped me and Markus escape. As wary as I am of her... I can't help but feel incredibly drawn to her.")}
