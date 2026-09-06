default BESHAR = Character(_("Beshar"), image = "beshar")

init python:
    CharDefs["beshar"] = BuildCharTemplate(CharID = "beshar",
        name = _("Beshar"))

    config.tag_layer["beshar"] = "characters"