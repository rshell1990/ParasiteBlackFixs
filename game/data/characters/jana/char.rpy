default JANA = Character(_("Jana"), image = "jana")
init python:
    CharDefs["jana"] = BuildCharTemplate(CharID = "jana",
        name = _("Jana"),
        portrait ="images/characters/jana/portrait.webp",
        BattleSkin = "jana",
        BattleClass = "warrior",

        Strength = 4,
        Endurance = 6,
        Willpower = 5,
        Agility = 6,
        Dexterity = 6,
        Luck = 3,

        is_mage = True,

        ExtraData = {"clothes":"normal"}) # normal/naked/dress
    config.tag_layer["jana"] = "characters"
    config.tag_layer["jana_uf_back"] = "characters"
    config.tag_layer["jana_dress_back"] = "characters"
