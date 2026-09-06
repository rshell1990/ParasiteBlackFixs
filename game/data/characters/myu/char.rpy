default MYU = Character(_("Myu"), image="myu")
default MYU_RED = Character(_("Myu"), image = "myu", what_color = "#ff0000", show_always_effect = always_shake(x = 1, y = 0))

init python:
    CharDefs["myu"] = BuildCharTemplate(CharID = "myu",
        BattleSkin =  "myu", 

        Strength = 4,
        Endurance = 6,
        Willpower = 5,
        Agility = 6,
        Dexterity = 6,
        Luck = 3,

        BattleClass = "slime",

        CharSkills = {"SlimeAcidicSplash":1},

        portrait = "images/characters/myu/portrait.webp",
        name = _("Myu"),

        RelTextIDs = {"initial", "initial_no_romance"},

        ExtraData = {"hide":False}, # in azul's place
        IsCompanion = True,
    )

    config.tag_layer["myu"] = "characters"

    config.tag_layer["cg_myu_monster"] = "characters"
    config.tag_layer["cg_myu_monster_blood"] = "characters"
    
    config.tag_layer["cg_myu_baby"] = "characters"

    config.tag_layer["cg_myu_hug"] = "characters"
    config.tag_layer["cg_myu_hug_grab"] = "characters"

    config.tag_layer["cg_myu_bimbo"] = "characters"
    config.tag_layer["cg_myu_bimbo_blush"] = "characters"

    RelText["myu"] = {}
    # initial
    RelText["myu"]["initial"] = {
        "order":0,
        "text":_("A slime whose attached herself to me and taken the form of a woman.")}

    # initial too
    RelText["myu"]["initial_no_romance"] = {
        "order":1,
        "text":_("Perhaps she could prove a useful ally?")}

    # replaces above line on romance
    RelText["myu"]["initial_romance"] = {
        "order":1,
        "text":_("Her attachment to me has gone beyond platonic, she views me as her 'mate' now.")}