define PRINCE_NARAN = Character(_("Prince Naran"), image = "naran")

init python:
    CharDefs["naran"] = BuildCharTemplate(CharID = "naran",
        name = _("Prince Naran"),
        portrait = "images/characters/naran/portrait.webp",
        RelTextIDs = {"summary_initial"})

    config.tag_layer["naran"] = "characters"

    # initially present
    RelText["naran"] = {}
    RelText["naran"]["summary_initial"] = {
        "order":0,
        "text":_("The royal prince of Alderay, King Mesamor's son... I am his loyal subject.")}