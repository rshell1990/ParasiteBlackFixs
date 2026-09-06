default GELA = Character(_("Gela"), image = "gela")
init python:
    # this only exists to store "clothes"
    CharDefs["gela"] = BuildCharTemplate(CharID = "gela",
        ExtraData = {"clothes":"normal"})

    config.tag_layer["gela"] = "characters"
