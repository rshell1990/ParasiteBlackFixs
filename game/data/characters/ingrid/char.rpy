define INGRID = Character(_("Ingrid"))
init python:
    CharDefs["ingrid"] = BuildCharTemplate(CharID = "ingrid",
                                            name = _("Ingrid"),
                                            portrait = "images/characters/ingrid/portrait.webp", 
                                            RelTextIDs = {"initial"},
                                            ExtraData = {
                                                "clothes":"normal", # normal ling naked
                                                "mask":False
                                            })
    config.tag_layer["ingrid"] = "characters"

    RelText["ingrid"] = {}
    RelText["ingrid"]["initial"] = {
        "order":0,
        "text":_("Ingrid Castilay, wife of Lord Rollo. It seems she has been imprisoned by Lord Tarbeck as payment for her husbands failure to pay his debt.")}