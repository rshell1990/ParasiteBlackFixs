default LIZARD_BLUE = Character(_("Water Skalith"), image = "lizard_blue")
init python:
    CharDefs["lizard_blue"] = BuildCharTemplate(CharID = "lizard_blue",
        name = _("Water Skalith"),
        ExtraData = {"hair":"normal"}) # normal / bald
    
    config.tag_layer["lizard_blue"] = "characters"