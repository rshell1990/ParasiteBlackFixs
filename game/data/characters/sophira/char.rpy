default SOPHIRA = Character(_("Sophira"), image = "sophira")

init python:
    CharDefs["sophira"] = BuildCharTemplate(CharID = "sophira",
        name = _("Sophira"),
        portrait = "images/characters/sophira/portrait.webp",
        ExtraData = {"clothes":"normal"},
        RelTextIDs = {"initial"})
    config.tag_layer["sophira"] = "characters"
    config.tag_layer["cg_sophira_snakeman_dead"] = "characters"
    config.tag_layer["cg_sophira_dress_hand_up"] = "characters"
    config.tag_layer["cg_sophira_ling_hand_up"] = "characters"
    config.tag_layer["cg_sophira_nude_hand_up"] = "characters"

    
    RelText["sophira"] = {}
    RelText["sophira"]["initial"] = {
        "order":0,
        "text":_("A young, beautiful, aristocrat's wife... She oddly reminds me of Adara?"),
    }

    RelText["sophira"]["died_during_siege"] = {
        "order":2,
        "text":_("She was killed by a Demorai abomination during the Siege of Novaras.")
    }