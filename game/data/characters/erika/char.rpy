default ERIKA = Character(_("Erika"), image = "erika")
init python:
    CharDefs["erika"] = BuildCharTemplate(CharID = "erika",
        name = _("Erika"), 
        portrait = "images/characters/erika/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"},

        BattleSkin =  "erika", 
        Strength    = 5,
        Endurance   = 3,
        Willpower   = 5,
        Agility     = 6,
        Dexterity   = 6,
        Luck        = 8,

        BattleClass = "inquisitor",

        CharSkills = {"InquisitorBurningJudgement": 1, "InquisitorFirewall":1},
        IsCompanion = True,
    )
    config.tag_layer["erika"] = "characters"

    RelText["erika"] = {}
    # unlocked at start
    RelText["erika"]["initial"] = {
        "order":0,
        "text":_("My childhood friend who was also taken in by Regina due to the war. As fierce as she beautiful, Erika has joined the elusive inquisitors. I just hope she's never forced to choose betwen me and them...")}