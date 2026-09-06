default ARWEN = Character(_("Arwen"), image = "arwen")
init python:
    CharDefs["arwen"] = BuildCharTemplate(CharID = "arwen",
                                        name = _("Arwen"),
                                        portrait = "images/characters/arwen/portrait.webp", 
                                        RelTextIDs = {"initial"},
                                        ExtraData = {"clothes":"normal"})
    config.tag_layer["arwen"] = "characters"

    RelText["arwen"] = {}
    RelText["arwen"]["initial"] = {
        "order":0,
        "text":_("A rising-star courtesan, very popular and renowned for her passion.")}