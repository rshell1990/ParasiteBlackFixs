default KYLISA = Character(_("Kylisa"), image = "kylisa")

init python:
    CharDefs["kylisa"] = BuildCharTemplate(CharID = "kylisa",
        name = _("Kylisa"),
        portrait = "images/characters/kylisa/portrait.webp", 
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal", "hood":True})

    config.tag_layer["kylisa"] = "characters"

    RelText["kylisa"] = {}
    RelText["kylisa"]["initial"] = {
        "order":0,
        "text":_("The royal mage, a holy-ordained representative of the new gods. She is well known and loved amongst the common people, often still holding many public services and acts of charity.")}