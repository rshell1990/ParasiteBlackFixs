default SWINDLER = Character(_("Swindler"), image = "swindler")

init python:
    CharDefs["swindler"] = BuildCharTemplate(CharID = "swindler",
                                                name = _("Swindler"),
                                                ExtraData = {"pose":"normal"}) # normal/knife

    config.tag_layer["swindler"] = "characters"