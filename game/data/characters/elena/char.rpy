default ELENA = Character(_("Elena"), image = "elena")
default ELENA_W = Character(_("Blue Wolf"), image = "elena_w")

init python:
    CharDefs["elena"] = BuildCharTemplate(CharID = "elena",
        name = _("Elena"),
        BattleSkin =  "elena_human",

        Strength = 4,
        Endurance = 4,
        Willpower = 3,
        Agility = 7,
        Dexterity = 7,
        Luck = 5,

        BattleClass = "rogue",

        CharSkills = {"RogueFeralStrike":1},
        
        HasAltForm = True,
        
        AltForm_BattleClass = "rogueWolfForm",
        AltForm_BattleSkin = "elena_wolf",

        AltForm_TransformSkill = "ElenaTransform",
        AltForm_UnTransformSkill = "ElenaUnTransform",
        AltForm_CharSkills = {"RogueWolfRipNTear":1},

        portrait = "images/characters/elena/portrait.webp",

        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal", "hide":False},
        IsCompanion = True,
        )
    
    config.tag_layer["elena"] = "characters"
    config.tag_layer["cg_elena_bottle"] = "characters"
    config.tag_layer["cg_elena_reading"] = "characters"
    config.tag_layer["cg_elena_reading_eyesup"] = "characters"
    config.tag_layer["elena_w"] = "characters"
    config.tag_layer["elena_w_book"] = "characters"
    config.tag_layer["cg_mc_elena_kiss_armor"] = "characters"
    config.tag_layer["cg_mc_elena_kiss_lingerie"] = "characters"
    config.tag_layer["cg_mc_elena_kiss_naked"] = "characters"
    config.tag_layer["cg_elena_x_helena"] = "characters"

    RelText["elena"] = {}

    # initial
    RelText["elena"]["initial"] = {
        "order":0,
        "text":_("A wolf-girl, servant to a near extinct noble house. She's agreed to help me as long as I help find the surviving heir to the Thornfalls.")}
    # after romance
    RelText["elena"]["romance"] = {
        "order":1,
        "text":_("The two of us have grown closer, and whilst we're taking things slow, things are certainly passionate...")}    
    
    def TransformElena(Val):
        worldChars["elena"]["Transformed"] = Val
        return

image elena_back_ling:
    "elena_back_ling_base"
    yoffset 60

image elena_back_naked:
    "elena_back_naked_base"
    yoffset 60
image elena_w_book:
    "images/characters/elena/wolf/base_book.webp"
    yoffset 500

image cg_mc_elena_kiss_armor:
    "cg_mc_elena_kiss_armor_base"
    yoffset 80