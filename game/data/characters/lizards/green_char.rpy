default LIZARD_GREEN = Character(_("Forest Skalith"), image = "lizard_green")
init python:
    CharDefs["lizard_green"] = BuildCharTemplate(CharID = "lizard_green",
        name = _("Forest Skalith"),
        ExtraData = {"hair":"normal"}) # normal / bald
    
    config.tag_layer["lizard_green"] = "characters"