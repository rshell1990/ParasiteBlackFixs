default DRAX = Character(_("Drax"), image = "drax")
init python:    
    CharDefs["drax"] = BuildCharTemplate(CharID = "drax",
        name = _("Drax"),
        RelTextIDs = {"initial"},
        portrait = "images/characters/drax/portrait.webp",
        ExtraData = {"clothes":"normal"} # normal, normal_ash
        )
    config.tag_layer["drax"] = "characters"

    RelText["drax"] = {}
    RelText["drax"]["initial"] = {
        "order":0,
        "text":_("A respectable blacksmith in Novaras, and Arlena's father. He raised her alone since his wife died.")}