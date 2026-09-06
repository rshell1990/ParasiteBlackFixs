default KENNELMASTER = Character(_("Kennel Master"), image = "kennelmaster")

init python:
    CharDefs["kennelmaster"] = BuildCharTemplate(CharID = "kennelmaster")
    config.tag_layer["kennelmaster"] = "characters"