default ALEA = Character(_("Alea"), image = "alea")
init python:
    CharDefs["alea"] = BuildCharTemplate(CharID = "alea", ExtraData = {"clothes":"normal", "mask":True})
    config.tag_layer["alea"] = "characters"