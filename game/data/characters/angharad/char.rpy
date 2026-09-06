default ANGHARAD = Character(_("Angharad"), image = "angharad")
init python:
    CharDefs["angharad"] = BuildCharTemplate(CharID = "angharad",
                ExtraData = {"slave":True})
    config.tag_layer["angharad"] = "characters"
    config.tag_layer["cg_angharad_hostage"] = "characters"
    config.tag_layer["cg_angharad_hostage_killed"] = "characters"
    config.tag_layer["cg_angharad_stabbed"] = "characters"
