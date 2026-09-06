default LIZARD_RED = Character(_("Desert Skalith"), image = "lizard_red")
init python:
    CharDefs["lizard_red"] = BuildCharTemplate(CharID = "lizard_red",
        name = _("Desert Skalith"),
        ExtraData = {"hair":"normal"}) # normal / bald
    
    config.tag_layer["lizard_red"] = "characters"