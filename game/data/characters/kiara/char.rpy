default KIARA = Character(_("Kiara"), image = "kiara")

init python:
    CharDefs["kiara"] = BuildCharTemplate(CharID = "kiara",
        name = _("Kiara"),
        portrait = "images/characters/kiara/portrait.webp",

        BattleSkin =  "kiara", 

        Strength = 5,
        Endurance = 3,
        Willpower = 5,
        Agility = 6,
        Dexterity = 6,
        Luck = 8,

        BattleClass = "scout",

        CharSkills = {"ScoutFastAndPreciseAttack":1},

################# alt form block (banshee)
        HasAltForm = True,

        AltForm_BattleClass = "banshee",
        AltForm_CharSkills = {"BansheeMoonlightDance": 1, "BansheeASongOfPain":1},
        AltForm_BattleSkin = "kiara_banshee",
        AltForm_TransformSkill = "KiaraTransform",
        AltForm_UnTransformSkill = "KiaraUnTransform",
#################

        RelTextIDs = {"initial"},

        ExtraData = {
            "romanced":False,
            "met":False,                # turned true in prologue, affects some prologue narra
            "clothes":"normal",         # normal is scout/hooded, other values: "naked" "plain" "towel"
            "default_look":"scout",     # < "scout" or "hooded", switched to hooded during that roof scene thing
            "story_form":"human",       # "human" / "demorai" for sprite
            "location":tra(STR_LOC.UNKNOWN),
        },

        IsCompanion = True,
    )

    config.tag_layer["kiara"] = "characters"
    config.tag_layer["cg_kiara_mask"] = "characters"
    config.tag_layer["cg_kiara_hug"] = "characters"
    config.tag_layer["cg_kiara_maid_kneel"] = "characters"

    RelText["kiara"] = {}
    # initial
    RelText["kiara"]["initial"] = {
        "order":0,
        "text":_("A cute, smart girl who befriend me and Markus during our time in the scouts.")}
    # add if romance
    RelText["kiara"]["prol_romance"] = {
        "order":1,
        "text":_("The two of us agreed to spend our (probably) short lives together whilst in the scouts.")}
    # add when killed during prologue
    RelText["kiara"]["prol_killed"] = {
        "order":2,
        "text":_("She was killed by the Demorai, during their assault on the abandoned fort.")}
    # add on resurrected non-romance
    RelText["kiara"]["revive_no_romance"] = {
        "order":3,
        "text":_("We watched her die but... She's alive somehow?")}
    # add on resurrected if romance
    RelText["kiara"]["revive_romance"] = {
        "order":3,
        "text":_("We watched her die but... She's alive somehow? She seems determined to continue our romance, but, is she even the same person I remember?")}

    
    def TransformKiara(Val):
        worldChars["kiara"]["Transformed"] = Val
        return