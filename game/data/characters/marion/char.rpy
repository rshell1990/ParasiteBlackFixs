default MARION = Character(_("Head Inquisitor Lady Marion"), image = "marion")
init python:
    CharDefs["marion"] = BuildCharTemplate(CharID = "marion",
        name = _("Marion"),
        portrait = "images/characters/marion/portrait.webp",
        ExtraData = {"clothes":"normal"},
        
        RelTextIDs = {"initial"},
        )
    config.tag_layer["marion"] = "characters"

    RelText["marion"] = {}
    # unlocked at start
    RelText["marion"]["initial"] = {
        "order":0,
        "text":_("The current head of the inquisitors... She views my existence as little more than a blight.")}