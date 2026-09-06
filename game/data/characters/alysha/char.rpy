default ALYSHA = Character(_("Alysha"), image = "alysha")
init python:
    CharDefs["alysha"] = BuildCharTemplate(CharID = "alysha",
                ExtraData = {"clothes":"slave"},
                name = _("Alysha"),
                portrait = "images/characters/alysha/warrior/portrait.webp",
                RelTextIDs = {"initial"}
                )
    config.tag_layer["alysha"] = "characters"

    RelText["alysha"] = {}
    RelText["alysha"]["initial"] = {
        "order":0,
        "text":_("A former slave turned knight... Did Captain Nyx have something to do with that?")}
