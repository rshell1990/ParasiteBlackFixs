define ESME = Character(_("Esme"), image = "esme")
init python:
    CharDefs["esme"] = BuildCharTemplate(CharID = "esme",
        name = _("Esme"),
        portrait = "images/characters/esme/portrait.webp",
        ExtraData = {"clothes":"in_gold"},
        RelTextIDs = {"initial"},
        )
    config.tag_layer["esme"] = "characters"
    config.tag_layer["cg_esme_maid_kneel"] = "characters"
    config.tag_layer["cg_esme_maid_leash"] = "characters"

    RelText["esme"] = {}
    # unlocked at start
    RelText["esme"]["initial"] = {
        "order":0,
        "text":_("A playful katai prostitute in the city of Hamun.")}