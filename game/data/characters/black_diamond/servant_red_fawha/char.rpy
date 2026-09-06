default FAWHA = Character(_("Fawha"), image = "fawha")
init python:
    CharDefs["fawha"] = BuildCharTemplate(CharID = "fawha", ExtraData = {"clothes":"normal", "mask":True})
    config.tag_layer["fawha"] = "characters"