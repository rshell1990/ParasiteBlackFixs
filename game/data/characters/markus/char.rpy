default MARKUS = Character(_("Markus"), image = "markus")
default MARKUS_FEM = Character(_("Markus"), image = "markus_fem")
default WHITE = Character(_("Parasite White"), what_color = "#ff0000", image = "white", show_slow_effect = slow_slide_up(25), show_slow_effect_delay = 0.5, show_always_effect = always_shake(x = 0, y = 1))
init python:
##### markus
    CharDefs["markus"] = BuildCharTemplate(
        CharID = "markus",
        portrait = "characters/markus/portrait_p.webp",
        BattleSkin =  "markus",
        name = _("Markus"),

        Strength = 6,
        Endurance = 5,
        Willpower = 4,
        Agility = 4,
        Dexterity = 5,
        Luck = 7,

        RelTextIDs = {"initial"},

        BattleClass = "warrior",

        HasAltForm = True,

        AltForm_BattleClass = "parasiteWhite",
        AltForm_CharSkills = {"ParasiteWhiteFireballCharge":1},
        AltForm_BattleSkin = "markus_transformed",

        AltForm_TransformSkill = "MarkusTransform",
        AltForm_UnTransformSkill = "MarkusUnTransform",

        ExtraData = {
            "clothes":"normal"
        },
        IsCompanion = True,
    )

    config.tag_layer["markus"] = "characters"
    config.tag_layer["markusprologue"] = "characters"
    config.tag_layer["markus_transformed"] = "characters"
    config.tag_layer["cg_markus_mug"] = "characters"
    config.tag_layer["cg_markus_tf_young"] = "characters"
    config.tag_layer["cg_markus_fem_maid_kneel"] = "characters"
    config.tag_layer["markus_fem"] = "characters"

    def TransformMarkus(Val):
        worldChars["markus"]["Transformed"] = Val
        return

    RelText["markus"] = {}
    # initially visible
    RelText["markus"]["initial"] = {
        "order":0,
        "text":_("My oldest friend.")}

    # add after tehy both become scouts
    RelText["markus"]["after_scouts"] = {
        "order":1,
        "text":_("The two of us planned to land ourselves some safe, well paying administrative jobs and avoid the war... Guess that's not on the cards anymore.")}