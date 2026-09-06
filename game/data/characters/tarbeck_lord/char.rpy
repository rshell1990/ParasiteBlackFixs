define TARBECK = Character(_("Lord Tarbeck"), image = "lord_tarbeck")
init python:
    CharDefs["lord_tarbeck"] = BuildCharTemplate(CharID = "lord_tarbeck",
        name = _("Lord Tarbeck"),
        portrait = "images/characters/lord_tarbeck/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"}) # just normal 

    config.tag_layer["lord_tarbeck"] = "characters"

    RelText["lord_tarbeck"] = {}
    RelText["lord_tarbeck"]["initial"] = {
        "order":0,
        "text":_("A rich, powerful merchant lord famous for his decadence and lust... He is as cunning as he is brutal.")}
