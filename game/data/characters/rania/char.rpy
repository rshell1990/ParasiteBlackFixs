default RANIA = Character(_("Rania"), image = "rania")
init python:
    CharDefs["rania"] = BuildCharTemplate(CharID = "rania",
        name = _("Rania"),
        portrait = "images/characters/rania/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData ={"clothes":"normal"})

    config.tag_layer["rania"] = "characters"

    RelText["rania"] = {}

    # unlocked at start
    RelText["rania"]["initial"] = {
        "order":0,
        "text":_("A keeper of the Pale Dragon hookah bar in Hamun.")}