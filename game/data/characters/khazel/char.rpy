default KHAZEL = Character(_("Khazel"), image = "khazel")
init python:
    CharDefs["khazel"] = BuildCharTemplate(CharID = "khazel", ExtraData = {"clothes":"normal"})
    config.tag_layer["khazel"] = "characters"