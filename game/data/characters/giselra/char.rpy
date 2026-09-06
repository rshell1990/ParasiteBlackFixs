define GISELRA = Character(_("Giselra"), image = "giselra")
init python:
    CharDefs["giselra"] = BuildCharTemplate(CharID = "giselra",
        name = _("Giselra"),
        portrait = "images/characters/giselra/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"} # naked/ling/normal
    )
    RelText["giselra"] = {}
    RelText["giselra"]["initial"] = {
        "order":0,
        "text":_("Giselra, the owner of Giselra's tailor. A charming, if slightly lonely, older woman from Hamun who runs a popular tailors.")}

    config.tag_layer["giselra"] = "characters"

